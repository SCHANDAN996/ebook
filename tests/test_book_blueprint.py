import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "toolkit"))
from steps import book_content


class BookBlueprintTests(unittest.TestCase):
    def test_real_blueprint_passes(self):
        summary = book_content.check(ROOT / "book")
        self.assertEqual(summary, {"chapters": 10, "prompts": 300,
                                   "workflows": 12, "sample_outputs": 60})

    def test_subtopic_mismatch_fails(self):
        original = book_content.load_blueprint(ROOT / "book")
        changed = copy.deepcopy(original)
        changed["chapters"][0]["subtopics"]["complete-lessons"] -= 1
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            (target / "manifest.json").write_text(json.dumps(changed), encoding="utf-8")
            # Missing source files create additional issues, but allocation must still be explicit.
            issues = book_content.blueprint_issues(target)
        self.assertTrue(any("subtopic counts" in issue for issue in issues))

    def test_duplicate_chapter_id_fails(self):
        original = book_content.load_blueprint(ROOT / "book")
        changed = copy.deepcopy(original)
        changed["chapters"][1]["id"] = changed["chapters"][0]["id"]
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            (target / "manifest.json").write_text(json.dumps(changed), encoding="utf-8")
            issues = book_content.blueprint_issues(target)
        self.assertTrue(any("unique kebab-case" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()

