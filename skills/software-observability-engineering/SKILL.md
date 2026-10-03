---
name: software-observability-engineering
description: "Projetar observabilidade de software com traces, metrics, logs, correlation, telemetry pipelines, sampling, SLO signals e debugging de produção sem confundir coleta de dados com entendimento operacional."
---

# Software Observability Engineering

## Objetivo

Tornar sistemas operáveis por sinais correlacionáveis que permitam responder o que falhou, onde, por quê e com qual impacto.

## Quando usar

- traces/metrics/logs;
- OpenTelemetry;
- production debugging;
- telemetry pipeline;
- SLO/SLI instrumentation;
- distributed tracing;
- alert design.

## Princípio central

**Observabilidade começa em perguntas operacionais, não em coletar tudo.**

## Workflow

1. **Questions**
   - quais jornadas são críticas?
   - que falhas precisam ser detectadas?
   - quais SLOs existem?
   - quais dimensões ajudam explicar variação?

2. **Signals**
   - metrics para tendência/alerta;
   - traces para causalidade distribuída;
   - logs para detalhe contextual;
   - events quando mudança discreta importa.

3. **Instrumentation**
   - semantic names;
   - service/resource identity;
   - trace/span correlation;
   - error/status semantics;
   - business/domain identifiers apenas quando necessários e seguros.

4. **Pipeline**
   `receive → process → export`
   - receivers;
   - processors;
   - batching;
   - filtering/redaction;
   - sampling;
   - exporters;
   - backpressure/retry.

5. **Cardinality**
   - não colocar IDs ilimitados em metric labels;
   - traces/logs podem carregar granularidade maior;
   - budgets explícitos.

6. **Sampling**
   - head/tail conforme objetivo;
   - preservar errors/slow traces quando policy exigir;
   - sampled data precisa ser interpretada como amostra.

7. **SLO signals**
   - latency;
   - errors;
   - traffic;
   - saturation;
   - domain success rate quando técnico não basta.

8. **Alerting**
   - alertar sintoma acionável;
   - reduzir duplicação;
   - incluir runbook/context;
   - medir alert fatigue.

9. **Telemetry health**
   - dropped spans/logs;
   - queue pressure;
   - exporter failures;
   - collector resource use;
   - pipeline itself must be observable.

10. **Debug loop**
    - detect → correlate → isolate → verify hypothesis → remediate → confirm recovery.

## Privacy/security

- redigir secrets/tokens;
- evitar PII em labels/logs;
- retention proporcional;
- telemetry endpoint/auth tratados como superfície de segurança.

## Regras

- mais logs não significa mais observabilidade;
- dashboard não é observabilidade se não responde perguntas;
- trace sem propagation/correlation perde valor;
- telemetry pipeline pode falhar e deve ser monitorado;
- vendor-specific backend é substituível, semantic contract não.

## Integração

`system-design-engineering`, `diagnosing-bugs`, `production-go-live`, `secure-code-privacy-review`, `dashboard-design`.

## Provenance

Consolidada de OpenTelemetry Collector e Sentry. Mantém receive/process/export, correlation e produção-debugging sem presumir backend/vendor específico.
