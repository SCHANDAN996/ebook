#!/usr/bin/env python3
"""Default to isolated pilot; offline commands never import the AI SDK."""
import argparse
import math
import sys
import config
from steps.storage import load_json


def cost(inp, out, batch=False):
    return (inp * config.PRICE_IN_PER_MTOK + out * config.PRICE_OUT_PER_MTOK) / 1e6 * (
        config.BATCH_DISCOUNT if batch else 1)


def estimate_values():
    prompts = sum(s["count"] for s in config.SECTIONS)
    chunks = sum(math.ceil(s["count"] / config.CATALOG_CHUNK) for s in config.SECTIONS)
    chunks += math.ceil(config.WORKFLOW_COUNT / config.WORKFLOW_CHUNK)
    expected = cost(chunks * 3000, chunks * 9000) + cost(
        (prompts + config.WORKFLOW_COUNT * 4) * 3000,
        (prompts + config.WORKFLOW_COUNT * 4) * 2500, True)
    # Planning allowance, NOT a provider-enforced cap: assumes <=24K input tokens/request.
    allowance = cost(chunks * 24000, chunks * config.CATALOG_MAX_TOKENS) + cost(
        (prompts + config.WORKFLOW_COUNT * 6) * 24000,
        (prompts + config.WORKFLOW_COUNT * 6) * config.OUTPUT_MAX_TOKENS, True)
    return {"prompts": prompts, "workflows": config.WORKFLOW_COUNT,
            "expected_usd": round(expected, 4), "planning_allowance_usd": round(allowance, 4)}


def estimate():
    v = estimate_values()
    print(f"Profile: {config.PROFILE}; {v['prompts']} prompts + {v['workflows']} workflows")
    print(f"Model: {config.MODEL}; illustrative estimate ${v['expected_usd']:.2f}")
    print(f"Planning allowance: ${v['planning_allowance_usd']:.2f}")
    print("Not a guaranteed bill/hard cap. Uses configured prices and assumed input sizes.")
    print("Set provider spend limits too. Retries, pricing and changed inputs can increase cost.")
    return v


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=["estimate", "status", "book-check", "beta-check", "design-preview", "catalog", "outputs", "build", "qc", "all"])
    ap.add_argument("--profile", choices=["pilot", "beta", "full"], default="pilot")
    ap.add_argument("-y", "--yes", action="store_true", help="Explicitly approve API spending")
    ap.add_argument("--budget-usd", type=float, help="Planning allowance acknowledged for this run")
    ap.add_argument("--poll", type=int, default=30)
    ap.add_argument("--timeout", type=int, default=3600)
    ap.add_argument("--release", action="store_true", help="Require human review, contact and PDF")
    ap.add_argument("--draft", action="store_true", help="Marked preview despite QC errors")
    ap.add_argument("--html-only", action="store_true")
    args = ap.parse_args(argv)
    config.configure(args.profile)
    try:
        if args.release and (args.draft or args.html_only):
            raise ValueError("A release cannot use --draft or --html-only")
        if args.poll < 1 or args.timeout < 1:
            raise ValueError("poll and timeout must be positive")
        if args.command == "estimate":
            estimate()
            return 0
        if args.command == "status":
            print(f"Profile: {config.PROFILE}; files: {config.BUILD}")
            print("Catalog:", "present" if config.CATALOG_JSON.exists() else "not generated")
            print("Stored outputs (not necessarily current):", len(load_json(config.OUTPUTS_JSON, {})))
            usage = load_json(config.USAGE_JSON, {})
            print("Recorded estimated spend: $", round(sum(v.get("estimated_usd", 0) for v in usage.values()), 4))
            print("Batch state:", load_json(config.BATCH_STATE, {}).get("status", "idle"))
            return 0
        if args.command == "book-check":
            from steps import book_content
            summary = book_content.check()
            print(f"Book blueprint passed: {summary['chapters']} chapters, "
                  f"{summary['prompts']} prompts, {summary['workflows']} workflows, "
                  f"{summary['sample_outputs']} selected full sample outputs.")
            return 0
        if args.command == "beta-check":
            from steps import book_content
            summary = book_content.check_beta()
            print(f"Beta content passed: {summary['prompts']} prompts, "
                  f"{summary['workflows']} workflows, "
                  f"{summary['sample_outputs']} sample-output markers.")
            return 0
        if args.command == "design-preview":
            import book_design_preview
            pdf, companion = book_design_preview.run()
            print(f"Design prototype PDF: {pdf}")
            print(f"Copy-enabled companion HTML: {companion}")
            return 0
        if args.command in {"catalog", "outputs", "all"}:
            v = estimate()
            if (not args.yes or args.budget_usd is None or not math.isfinite(args.budget_usd)
                    or args.budget_usd < v["planning_allowance_usd"]):
                raise ValueError("No API calls made. Require --yes and --budget-usd at least "
                                 f"{v['planning_allowance_usd']:.4f}; first set provider spend limits.")
        if args.command in {"catalog", "all"}:
            from steps import catalog
            catalog.run()
        if args.command in {"outputs", "all"}:
            from steps import outputs
            cat = load_json(config.CATALOG_JSON)
            if cat is None:
                raise ValueError("Generate the catalog for this profile first")
            outputs.run(cat, poll_seconds=args.poll, timeout=args.timeout)
        if args.command in {"build", "qc", "all"}:
            from steps import build
            if not config.CATALOG_JSON.exists():
                raise ValueError("No catalog for this profile. Offline build needs existing data.")
            if args.command == "qc":
                issues = build.qc(load_json(config.CATALOG_JSON), load_json(config.OUTPUTS_JSON, {}),
                                  release=args.release)
                print("\n".join(issues) if issues else "Automated QC passed; not a teaching-quality certification.")
                return int(bool(issues))
            build.run(draft=args.draft, release=args.release, html_only=args.html_only)
        return 0
    except (ValueError, OSError, TimeoutError, ImportError) as exc:
        print(f"Stopped: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
