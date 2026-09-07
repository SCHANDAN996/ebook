"""Resumable batches with actual workflow dependencies and provenance."""
from datetime import datetime, timezone
import time
import config
from steps.contracts import (OUTPUT_SYSTEM, catalog_issues, digest, fingerprint,
                             required_items, settings_hash, valid_record)
from steps.storage import load_json, save_json


def _params(prompt):
    params = {"model": config.MODEL, "max_tokens": config.OUTPUT_MAX_TOKENS,
              "system": OUTPUT_SYSTEM, "messages": [{"role": "user", "content": prompt}]}
    if config.OUTPUT_EFFORT:
        params["output_config"] = {"effort": config.OUTPUT_EFFORT}
    return params


def _snapshot(catalog):
    return digest({"catalog": catalog, "settings": settings_hash()})


def ready_items(catalog, outputs, attempted=()):
    return [i for i in required_items(catalog, outputs)
            if i["prompt"] is not None and i["key"] not in attempted
            and not valid_record(outputs.get(i["key"]), i["prompt"])]


def _wait(client, batch_id, poll_seconds, timeout):
    deadline = time.monotonic() + timeout
    while True:
        batch = client.messages.batches.retrieve(batch_id)
        if batch.processing_status == "ended":
            return
        if time.monotonic() >= deadline:
            raise TimeoutError("Batch still running; saved state intact. Run outputs again to resume.")
        print(f"  Batch {batch_id}: {batch.processing_status}", flush=True)
        time.sleep(min(poll_seconds, max(0, deadline - time.monotonic())))


def _usage(message):
    usage = getattr(message, "usage", None)
    if hasattr(usage, "model_dump"):
        return usage.model_dump()
    return {name: getattr(usage, name, 0) for name in ("input_tokens", "output_tokens")}


def _harvest(client, state, outputs):
    failures = load_json(config.FAILURE_JSON, {})
    usage_log = load_json(config.USAGE_JSON, {})
    seen = set()
    items = {i["key"]: i for i in state["items"]}
    for result in client.messages.batches.results(state["batch_id"]):
        key = result.custom_id
        if key not in items or key in seen:
            raise ValueError("Unexpected/duplicate result ID; batch state preserved")
        seen.add(key)
        kind = result.result.type
        reason = kind
        if kind == "succeeded":
            msg = result.result.message
            text = "\n".join(b.text for b in msg.content if b.type == "text").strip()
            reason = getattr(msg, "stop_reason", None)
            usage = _usage(msg)
            # Truncated/refused messages are billed too. Reharvesting must not double-count.
            usage_log[f"{state['batch_id']}:{key}"] = {
                "stage": "outputs", "batch": True, "usage": usage,
                "model": getattr(msg, "model", config.MODEL), "stop_reason": reason,
                "estimated_usd": (usage.get("input_tokens", 0) * config.PRICE_IN_PER_MTOK
                                  + usage.get("output_tokens", 0) * config.PRICE_OUT_PER_MTOK)
                                  / 1e6 * config.BATCH_DISCOUNT}
            save_json(config.USAGE_JSON, usage_log)
            if reason == "end_turn" and text:
                outputs[key] = {"status": "succeeded", "stop_reason": reason,
                                "input": items[key]["prompt"], "output": text,
                                "fingerprint": fingerprint(items[key]["prompt"]),
                                "output_sha256": digest(text),
                                "generated_at": datetime.now(timezone.utc).isoformat(),
                                "model": getattr(msg, "model", config.MODEL),
                                "batch_id": state["batch_id"], "usage": usage}
                failures.pop(key, None)
                save_json(config.OUTPUTS_JSON, outputs)
                save_json(config.FAILURE_JSON, failures)
                continue
            reason = reason if text else "empty"
        failures[key] = {"reason": reason, "batch_id": state["batch_id"],
                         "fingerprint": fingerprint(items[key]["prompt"])}
        save_json(config.FAILURE_JSON, failures)
    if seen != set(items):
        raise ValueError("Incomplete result stream; resume preserved batch, do not resubmit")


def run(catalog, poll_seconds=30, timeout=3600, client=None):
    if poll_seconds < 1 or timeout < 1:
        raise ValueError("poll and timeout must be positive")
    problems = catalog_issues(catalog)
    if problems:
        raise ValueError("Catalog invalid: " + "; ".join(problems[:10]))
    state = load_json(config.BATCH_STATE, {})
    snapshot = _snapshot(catalog)
    if state and state.get("snapshot") != snapshot:
        raise ValueError("Pending batch has different catalog/settings. Restore those before resuming.")
    if state and not state.get("batch_id"):
        raise ValueError("Submission outcome uncertain. Check provider batch list and recover its ID "
                         "in batch_state.json; do not blindly resubmit or delete state.")
    live_client = client is None
    if live_client:
        import anthropic
        from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
        from anthropic.types.messages.batch_create_params import Request
        client = anthropic.Anthropic(max_retries=0)
    outputs = load_json(config.OUTPUTS_JSON, {})
    attempted = set()
    if state:
        _wait(client, state["batch_id"], poll_seconds, timeout)
        _harvest(client, state, outputs)
        attempted.update(i["key"] for i in state["items"])
        save_json(config.BATCH_STATE, {})
    while True:
        items = ready_items(catalog, outputs, attempted)
        if not items:
            break
        # Intent before network: a timeout is ambiguous, not permission to retry.
        state = {"snapshot": snapshot, "items": items, "status": "submitting"}
        save_json(config.BATCH_STATE, state)
        requests = ([Request(custom_id=i["key"],
                             params=MessageCreateParamsNonStreaming(**_params(i["prompt"])))
                     for i in items] if live_client else
                    [{"custom_id": i["key"], "params": _params(i["prompt"])} for i in items])
        batch = client.messages.batches.create(requests=requests)
        state.update(batch_id=batch.id, status="submitted")
        save_json(config.BATCH_STATE, state)
        print(f"  Submitted {len(items)} requests in {batch.id}")
        _wait(client, batch.id, poll_seconds, timeout)
        _harvest(client, state, outputs)
        attempted.update(i["key"] for i in items)
        save_json(config.BATCH_STATE, {})
        # Successful predecessor output now unlocks the next workflow step.
    missing = [i["key"] for i in required_items(catalog, outputs)
               if i["prompt"] is None or not valid_record(outputs.get(i["key"]), i["prompt"])]
    if missing:
        raise ValueError(f"{len(missing)} outputs failed/blocked; inspect failures.json. "
                         "No automatic retries. Re-running may spend money.")
    return outputs
