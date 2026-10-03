---
name: local-llm-inference-engineering
description: "Projetar e avaliar inferência local/on-device de LLMs com quantização, offload de pesos, streaming de experts, caching/prefetch, adapters e benchmarks de memória/latência/qualidade sem confundir throughput com experiência real."
---

# Local LLM Inference Engineering

## Objetivo

Executar modelos grandes em hardware limitado com trade-offs explícitos entre memória, armazenamento, latência, throughput e qualidade.

## Quando usar

- inferência local;
- on-device LLM;
- Apple Silicon / mobile / consumer GPU;
- quantização;
- weight offload;
- sparse MoE;
- model streaming;
- adapter serving;
- benchmark de runtime.

## Princípio central

**O limite real é o working set ativo, não necessariamente o tamanho total do modelo.**

## Workflow

1. **Workload contract**
   - model architecture;
   - dense vs sparse/MoE;
   - context length;
   - target hardware;
   - RAM/VRAM;
   - storage bandwidth;
   - latency target;
   - quality floor.

2. **Baseline**
   - peak memory;
   - cold/warm prefill;
   - decode throughput;
   - time-to-first-token;
   - end-to-end task latency;
   - quality benchmark at same task settings.

3. **Quantization**
   - bit width;
   - calibration/training method;
   - affected modules;
   - quality delta;
   - keep quality measurement paired with runtime gains.

4. **Offload**
   - identify weights that need not stay resident;
   - SSD/CPU/GPU movement;
   - mmap/streaming when appropriate;
   - active working set budget;
   - cold vs warm behavior.

5. **Prediction/prefetch**
   - when future routing/access can be predicted, overlap I/O with compute;
   - track prediction hit/miss;
   - do not hide stalls with average throughput only;
   - prefetch policy must respect storage pressure and cache size.

6. **Adapters**
   - keep immutable base separate from replaceable adapters when useful;
   - record adapter provenance/version;
   - test base-only vs adapted quality;
   - avoid silent merge when independent swap/versioning matters.

7. **Backend boundary**
   - isolate platform/backend-specific code behind a stable facade;
   - keep model/core semantics independent when practical;
   - platform-native runtimes may differ, but contracts should remain comparable.

8. **Benchmark**
   - same prompt/task;
   - cold and warm runs;
   - memory peak;
   - TTFT;
   - decode;
   - total wall time;
   - energy/thermal behavior when material;
   - matched-quality comparison.

9. **Failure modes**
   - storage thrash;
   - cache pollution;
   - prediction misses;
   - long-context KV growth;
   - adapter incompatibility;
   - platform-specific numerical drift;
   - thermal throttling.

## Regras

- tokens/s alone is not enough;
- cold-start and warm-cache behavior must be separated;
- quantization gain without quality measurement is incomplete;
- benchmark claims from another machine are not guarantees;
- roadmap feature is not current capability;
- local inference reduces network exposure but does not automatically make model/data handling safe;
- model/license terms must be checked before deployment.

## Integração

`codex-cost-efficiency`, `llm-observability-evaluation`, `software-performance-engineering` when available, `crossplatform-mobile-engineering`, `model-routing-gateway`.

## Provenance

Adaptada de Edge0-AI/Edge0. Preserva SSD expert offload, active-set memory budgeting, prerouter/prefetch, adapter separation, backend isolation e matched-quality benchmarking sem presumir Edge0 models, MLX, Vulkan ou hardware específico.
