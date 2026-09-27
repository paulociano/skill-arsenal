#!/usr/bin/env python3
"""Execute real Laya decisions; benchmark or reuse a resident model via JSONL."""
import argparse
import importlib.metadata
import json
import math
import platform
import statistics
import sys
import time
from pathlib import Path

MODEL = "convaiinnovations/laya-multilingual"
REVISION = "e4e9ddf21a7b1903b7acffd8814ad4307bf63a67"
QUESTIONS = {
    "domain": {
        "type": "choice",
        "instructions": "Qual domínio melhor corresponde ao pedido?",
        "criteria": {
            "writing": "escrever ou revisar textos",
            "code": "implementar ou corrigir software",
            "decision": "comparar alternativas e tomar uma decisão",
            "other": "nenhum dos domínios anteriores",
        },
    }
}
CASES = [
    ("Revise este texto para deixá-lo mais claro.", "writing"),
    ("Corrija o erro de login na aplicação Python.", "code"),
    ("Compare os fornecedores por custo, prazo e risco.", "decision"),
]


def emit(value):
    print(json.dumps(value, ensure_ascii=False), flush=True)


def validate_request(request):
    if not isinstance(request, dict) or "state" not in request:
        raise ValueError("request must contain state and questions")
    questions = request.get("questions")
    if not isinstance(questions, dict) or not questions:
        raise ValueError("questions must be a nonempty object")
    for question in questions.values():
        if not isinstance(question, dict) or question.get("type") not in ("choice", "score", "noul"):
            raise ValueError("question type must be choice, score or noul")
    return request["state"], questions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--revision", default=REVISION, help="Immutable model revision; override with --model")
    parser.add_argument("--device", choices=["cpu", "cuda", "mps"], default="cpu")
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--iterations", type=int, default=5)
    parser.add_argument("--warmup", type=int, default=2)
    parser.add_argument("--max-len", type=int, default=1024)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--request", type=Path, help="JSON with state and questions")
    mode.add_argument("--jsonl", action="store_true", help="Keep model resident; read one JSON request per line")
    args = parser.parse_args()
    if args.iterations < 1 or args.warmup < 0 or args.threads < 1 or args.max_len < 1:
        parser.error("iterations, threads and max-len must be positive; warmup cannot be negative")

    started = time.perf_counter()
    import torch
    import laya
    torch.set_num_threads(args.threads)
    if args.device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but unavailable")
    from huggingface_hub import snapshot_download
    model_path = snapshot_download(args.model, revision=args.revision)
    model = laya.load(model_path, device=args.device)
    def sync():
        if args.device == "cuda":
            torch.cuda.synchronize()
        elif args.device == "mps":
            torch.mps.synchronize()
    sync()
    load_seconds = time.perf_counter() - started

    def predict(request):
        state, questions = validate_request(request)
        sync()
        start = time.perf_counter()
        with torch.inference_mode():
            result = model.predict(state, questions, max_len=args.max_len)
        sync()
        return {"elapsed_ms": (time.perf_counter() - start) * 1000, "result": result}

    if args.jsonl:
        print(json.dumps({"ready": True, "load_seconds": load_seconds}), file=sys.stderr, flush=True)
        for line in sys.stdin:
            if not line.strip():
                continue
            try:
                emit(predict(json.loads(line)))
            except Exception as exc:
                emit({"status": "error", "error_type": type(exc).__name__, "message": str(exc)})
        return

    if args.request:
        request = json.loads(args.request.read_text(encoding="utf-8"))
        emit({"load_seconds": load_seconds, **predict(request)})
        return

    for _ in range(args.warmup):
        predict({"state": CASES[0][0], "questions": QUESTIONS})
    latencies, samples = [], []
    correct = 0
    for iteration in range(args.iterations):
        for state, expected in CASES:
            result = predict({"state": state, "questions": QUESTIONS})
            actual = result["result"]["answers"]["domain"]["choice"]
            latencies.append(result["elapsed_ms"])
            correct += actual == expected
            if iteration == 0:
                samples.append({"state": state, "expected": expected, "actual": actual,
                                "answer": result["result"]["answers"]["domain"]})
    ordered = sorted(latencies)
    emit({
        "status": "measured",
        "model": args.model, "revision": args.revision, "device": args.device,
        "python": platform.python_version(), "machine": platform.machine(),
        "versions": {name: importlib.metadata.version(name)
                     for name in ["laya", "torch", "transformers", "huggingface-hub"]},
        "threads": args.threads, "max_len": args.max_len, "load_seconds": load_seconds,
        "warmup_requests": args.warmup, "measured_requests": len(latencies),
        "questions_per_request": 1, "batch_size": 1,
        "latency_ms": {"median": statistics.median(latencies),
                       "p95_nearest_rank": ordered[math.ceil(0.95 * len(ordered)) - 1],
                       "min": min(latencies), "max": max(latencies)},
        "raw_latency_ms": latencies, "correct_replays": correct,
        "unique_cases": len(CASES), "samples": samples,
        "limitations": "Synthetic smoke cases repeated for latency; not a held-out accuracy evaluation. "
                       "Load includes imports and possible downloads. No authorization to execute decisions.",
    })


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        emit({"status": "error", "error_type": type(exc).__name__, "message": str(exc)})
        sys.exit(1)
