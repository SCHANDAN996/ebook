"""No API keys, AI SDK, or network calls. Fake provider exercises execution semantics."""
import copy
from datetime import datetime, timezone
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "toolkit"))
import config
import lead_magnet
import run
from steps import build, contracts as c, outputs
from steps.keys import custom_id
from steps.storage import load_json, save_json


def fixture():
    sections = {}
    for section in config.SECTIONS:
        sections[section["id"]] = [
            {"slug": f"prompt-{n}", "title": f"Practice {n}", "use_case": "Plan practice",
             "grade_band": "3-5", "subject": "Math", "variables": ["TOPIC"],
             "prompt": "Make a worksheet about [TOPIC] with answers.",
             "example_filled_prompt": f"Make a fractions worksheet with answers, example {n}."}
            for n in range(section["count"])]
    workflows = [{"slug": f"workflow-{n}", "title": "Lesson to quiz", "goal": "A complete draft",
                  "replaces": "Planning tasks", "steps": [
                      {"step": 1, "title": "Plan", "prompt": "Plan a fractions lesson.",
                       "example_filled_prompt": "Plan a Grade 4 fractions lesson."},
                      {"step": 2, "title": "Worksheet", "prompt": "Use {{PREVIOUS_OUTPUT}} to create practice.",
                       "example_filled_prompt": "Use {{PREVIOUS_OUTPUT}} to create practice."},
                      {"step": 3, "title": "Quiz", "prompt": "Use {{PREVIOUS_OUTPUT}} to create a quiz.",
                       "example_filled_prompt": "Use {{PREVIOUS_OUTPUT}} to create a quiz."}]}
                 for n in range(config.WORKFLOW_COUNT)]
    return {"sections": sections, "workflows": workflows}


def record(prompt, text=None):
    text = text or "A concrete fictional teaching artifact with correct worked examples and a teacher review checklist. " * 3
    return {"status": "succeeded", "stop_reason": "end_turn", "input": prompt, "output": text,
            "fingerprint": c.fingerprint(prompt), "output_sha256": c.digest(text),
            "model": config.MODEL, "generated_at": datetime.now(timezone.utc).isoformat()}


def all_records(cat):
    result = {}
    for _ in range(7):
        for i in outputs.ready_items(cat, result):
            result[i["key"]] = record(i["prompt"])
    return result


class FakeBatches:
    def __init__(self, failure=None):
        self.calls = []
        self.failure = failure
        self.saved = {}

    def create(self, requests):
        self.calls.append(copy.deepcopy(requests))
        bid = f"batch-{len(self.calls)}"
        self.saved[bid] = requests
        return NS(id=bid)

    def retrieve(self, batch_id):
        return NS(processing_status="ended")

    def results(self, batch_id):
        for req in reversed(self.saved[batch_id]):
            key = req["custom_id"]
            if self.failure == key:
                yield NS(custom_id=key, result=NS(type="errored"))
            else:
                text = f"Completed {key}: " + "Fictional worked example, answer key and teacher review checks. " * 4
                yield NS(custom_id=key, result=NS(type="succeeded", message=NS(
                    model=config.MODEL, stop_reason="end_turn", usage=NS(input_tokens=100, output_tokens=100),
                    content=[NS(type="text", text=text)])))


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root_patch = patch.object(config, "ROOT", Path(self.temp.name))
        self.root_patch.start()
        config.configure("pilot")
        self.cat = fixture()

    def tearDown(self):
        self.root_patch.stop()
        config.configure()
        self.temp.cleanup()

    def test_default_pilot_is_bounded(self):
        self.assertEqual(sum(s["count"] for s in config.SECTIONS), 5)
        self.assertEqual(config.WORKFLOW_COUNT, 1)

    def test_profile_caches_are_isolated(self):
        pilot = config.BUILD
        config.configure("beta")
        self.assertNotEqual(pilot, config.BUILD)
        self.assertEqual(sum(s["count"] for s in config.SECTIONS), 30)
        self.assertEqual(config.WORKFLOW_COUNT, 3)
        config.configure("full")
        self.assertEqual(sum(s["count"] for s in config.SECTIONS), 300)

    def test_no_settings_aliasing(self):
        config.SECTIONS[0]["count"] = 99
        config.configure("pilot")
        self.assertEqual(config.SECTIONS[0]["count"], 5)

    def test_zero_outputs_fails_qc(self):
        self.assertTrue(build.qc(self.cat, {}))

    def test_missing_workflows_fails(self):
        self.cat["workflows"] = []
        self.assertTrue(c.catalog_issues(self.cat))

    def test_missing_count_fails(self):
        self.cat["sections"]["lesson-planning"].pop()
        self.assertTrue(c.catalog_issues(self.cat))

    def test_duplicate_slug_fails(self):
        ps = self.cat["sections"]["lesson-planning"]
        ps[1]["slug"] = ps[0]["slug"]
        self.assertTrue(c.catalog_issues(self.cat))

    def test_bad_grade_band_fails(self):
        self.cat["sections"]["lesson-planning"][0]["grade_band"] = "college"
        self.assertTrue(c.catalog_issues(self.cat))

    def test_placeholder_leak_fails(self):
        self.cat["sections"]["lesson-planning"][0]["example_filled_prompt"] = "Teach [TOPIC]"
        self.assertTrue(c.catalog_issues(self.cat))

    def test_variable_mismatch_fails(self):
        self.cat["sections"]["lesson-planning"][0]["variables"] = []
        self.assertTrue(c.catalog_issues(self.cat))

    def test_workflow_order_fails(self):
        self.cat["workflows"][0]["steps"][1]["step"] = 1
        self.assertTrue(c.catalog_issues(self.cat))

    def test_workflow_without_chain_marker_fails(self):
        self.cat["workflows"][0]["steps"][1]["example_filled_prompt"] = "Use the previous response."
        self.assertTrue(c.catalog_issues(self.cat))

    def test_changed_prompt_invalidates_cache(self):
        self.assertFalse(c.valid_record(record("old"), "new"))

    def test_changed_model_invalidates_cache(self):
        r = record("example")
        with patch.object(config, "MODEL", "different-model"):
            self.assertFalse(c.valid_record(r, "example"))

    def test_output_tampering_invalidates_hash(self):
        r = record("example")
        r["output"] += " extra text"
        self.assertFalse(c.valid_record(r, "example"))

    def test_legacy_strings_are_not_verified(self):
        self.assertFalse(c.valid_record("legacy text", "example"))

    def test_workflow_uses_actual_previous_output(self):
        batches = FakeBatches()
        result = outputs.run(self.cat, client=NS(messages=NS(batches=batches)))
        self.assertEqual(len(batches.calls), 3)
        self.assertEqual(len(batches.calls[0]), 6)  # 5 prompts plus first workflow step
        second = batches.calls[1][0]["params"]["messages"][0]["content"]
        self.assertIn(result["wf__workflow-0__s1"]["output"], second)
        self.assertNotIn(config.PREVIOUS_OUTPUT, second)
        self.assertFalse(c.quality_issues(self.cat, result))

    def test_second_run_does_not_resubmit(self):
        batches = FakeBatches()
        client = NS(messages=NS(batches=batches))
        outputs.run(self.cat, client=client)
        outputs.run(self.cat, client=client)
        self.assertEqual(len(batches.calls), 3)

    def test_failure_blocks_dependent_steps(self):
        batches = FakeBatches(failure="wf__workflow-0__s1")
        with self.assertRaises(ValueError):
            outputs.run(self.cat, client=NS(messages=NS(batches=batches)))
        self.assertEqual(len(batches.calls), 1)
        self.assertIn("wf__workflow-0__s1", load_json(config.FAILURE_JSON))

    def test_truncated_refused_empty_outputs_rejected_and_usage_logged(self):
        for reason, text in [("max_tokens", "unfinished"), ("refusal", "No"), ("end_turn", "")]:
            with self.subTest(reason=reason):
                msg = NS(content=[NS(type="text", text=text)], stop_reason=reason,
                         usage=NS(input_tokens=10, output_tokens=20), model=config.MODEL)
                r = NS(custom_id="test", result=NS(type="succeeded", message=msg))
                client = NS(messages=NS(batches=NS(results=lambda _: iter([r]))))
                state = {"batch_id": "fake", "items": [{"key": "test", "prompt": "Example"}]}
                saved = {}
                outputs._harvest(client, state, saved)
                self.assertEqual(saved, {})
                self.assertIn("fake:test", load_json(config.USAGE_JSON))

    def test_resumes_existing_batch(self):
        batches = FakeBatches()
        items = outputs.ready_items(self.cat, {})
        batch = batches.create([{"custom_id": i["key"], "params": outputs._params(i["prompt"])} for i in items])
        save_json(config.BATCH_STATE, {"batch_id": batch.id, "snapshot": outputs._snapshot(self.cat), "items": items})
        outputs.run(self.cat, client=NS(messages=NS(batches=batches)))
        self.assertEqual(len(batches.calls), 3)

    def test_uncertain_submission_does_not_resubmit(self):
        save_json(config.BATCH_STATE, {"snapshot": outputs._snapshot(self.cat), "status": "submitting"})
        with self.assertRaisesRegex(ValueError, "uncertain"):
            outputs.run(self.cat, client=NS())

    def test_changed_pending_snapshot_stops(self):
        save_json(config.BATCH_STATE, {"snapshot": "other", "batch_id": "saved"})
        with self.assertRaisesRegex(ValueError, "different"):
            outputs.run(self.cat, client=NS())

    def test_missing_result_preserves_error(self):
        client = NS(messages=NS(batches=NS(results=lambda _: iter([]))))
        with self.assertRaisesRegex(ValueError, "Incomplete"):
            outputs._harvest(client, {"batch_id": "fake", "items": [{"key": "x", "prompt": "hi"}]}, {})

    def test_atomic_json_round_trip(self):
        path = config.BUILD / "check.json"
        save_json(path, {"text": "हिंदी"})
        self.assertEqual(load_json(path), {"text": "हिंदी"})
        self.assertEqual(list(path.parent.glob("*.tmp")), [])

    def test_corrupt_json_is_not_silently_reset(self):
        path = Path(self.temp.name) / "corrupt.json"
        path.write_text("{", encoding="utf-8")
        with self.assertRaises(ValueError):
            load_json(path, {})

    def test_ids_safe_collision_resistant(self):
        self.assertNotEqual(custom_id("a/b"), custom_id("a.b"))
        self.assertLessEqual(len(custom_id("x" * 300)), 64)

    def test_release_needs_current_reviews_and_contact(self):
        records = all_records(self.cat)
        self.assertFalse(c.quality_issues(self.cat, records))
        self.assertTrue(c.quality_issues(self.cat, records, release=True))
        reviews = {k: {"approved": True, "reviewer": "TEST FIXTURE ONLY", "reviewed_at": "2026-09-07",
                       "notes": "Synthetic test approval, not a real teacher review", "fingerprint": r["fingerprint"],
                       "output_sha256": r["output_sha256"]} for k, r in records.items()}
        with patch.dict(config.PRODUCT, {"support_email": "test@invalid.test"}):
            self.assertFalse(c.quality_issues(self.cat, records, reviews, release=True))
            reviews[next(iter(reviews))]["output_sha256"] = "old"
            self.assertTrue(c.quality_issues(self.cat, records, reviews, release=True))

    def test_build_fails_closed_before_html(self):
        save_json(config.CATALOG_JSON, self.cat)
        with self.assertRaises(ValueError):
            build.run(html_only=True)
        self.assertFalse(config.BOOK_HTML.exists())

    def test_explicit_draft_is_marked(self):
        save_json(config.CATALOG_JSON, self.cat)
        build.run(draft=True, html_only=True)
        self.assertIn("DEVELOPMENT DRAFT", config.BOOK_HTML.read_text())

    def test_render_contains_exact_input_and_model(self):
        html = build.render_html(self.cat, all_records(self.cat))
        self.assertIn("Exact example input", html)
        self.assertIn(config.MODEL, html)

    def test_html_escapes_untrusted_content(self):
        self.cat["sections"]["lesson-planning"][0]["title"] = '<script>alert("x")</script>'
        self.assertNotIn("<script>", build.render_html(self.cat, {}))

    def test_markdown_tables_are_rendered_and_escaped(self):
        rendered = build._md("Before\n\n| Skill | Score |\n| --- | --- |\n| <script> | 2 |\n\nAfter")
        self.assertIn("<table>", rendered)
        self.assertIn("&lt;script&gt;", rendered)
        self.assertIn("After", rendered)

    def test_paid_command_without_approval_never_imports_sdk(self):
        with patch.dict(sys.modules, {"anthropic": None}), patch("sys.stderr", new=io.StringIO()):
            self.assertEqual(run.main(["all"]), 1)

    def test_paid_command_requires_budget_even_with_yes(self):
        with patch("sys.stderr", new=io.StringIO()):
            self.assertEqual(run.main(["catalog", "--yes"]), 1)

    def test_nan_budget_rejected(self):
        with patch("sys.stderr", new=io.StringIO()):
            self.assertEqual(run.main(["catalog", "--yes", "--budget-usd", "nan"]), 1)

    def test_offline_cli_works_without_sdk(self):
        with patch.dict(sys.modules, {"anthropic": None}):
            self.assertEqual(run.main(["estimate"]), 0)
            self.assertEqual(run.main(["status"]), 0)

    def test_preview_has_no_unproven_claims_or_fake_support(self):
        html = lead_magnet.render()
        for forbidden in ["CHANGE_ME", "Save Teachers 5 Hours", "Use initials", "Works in ChatGPT"]:
            self.assertNotIn(forbidden, html)
        self.assertEqual(len(lead_magnet.PROMPTS), 25)
        self.assertIn("not recorded API outputs", html)
        self.assertIn("Do not infer identity", html)

    @unittest.skipUnless(importlib.util.find_spec("reportlab") and importlib.util.find_spec("pypdf"), "PDF extras not installed")
    def test_pdf_has_links_bookmarks_and_all_prompts(self):
        from pypdf import PdfReader
        lead_magnet.main(["--output-dir", self.temp.name])
        pdf = PdfReader(Path(self.temp.name) / "lead-magnet.pdf")
        self.assertGreater(len(pdf.outline), 5)
        self.assertGreater(sum(len(p.get("/Annots", [])) for p in pdf.pages), 5)
        text = "\n".join(p.extract_text() for p in pdf.pages)
        self.assertIn("25. Morning meeting", text)
        self.assertNotIn("CHANGE_ME", text)
        self.assertTrue(all(len(p.extract_text()) > 250 for p in pdf.pages))


if __name__ == "__main__":
    unittest.main()
