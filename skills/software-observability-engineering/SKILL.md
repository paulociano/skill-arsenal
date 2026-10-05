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


## Contrato SLI/SLO/SLA e orçamento de erro

Para disponibilidade ou SLA, explicitar:
- SLI observado, SLO interno e compromisso contratual separados;
- jornada, população elegível, eventos bons/totais, janela móvel ou calendário, timezone e fonte;
- exclusões somente quando definidas na política/contrato; nunca retirar falhas para melhorar a métrica;
- disponibilidade por tempo e por requisições não são intercambiáveis;
- denominador zero ou telemetria ausente significa evidência insuficiente, não 100%.

Para SLO por eventos com alvo t entre 0 e 1: SLI = good/total; orçamento permitido = (1-t)*total; consumido = bad; restante = permitido-consumido. Burn rate = (bad/total)/(1-t), sobre a mesma população/janela. Alvo de 100% exige tratamento próprio: não dividir por zero. Orçamento negativo representa excesso; não ocultá-lo por truncamento.

Combinar janelas longas e curtas para alertar consumo sustentado e rápido do orçamento. Definir limiares por duração, urgência e runbook; não copiar números sem verificar volume e tráfego. Testar falha sustentada, pico breve, recuperação, ausência de dados e baixo tráfego. Deduplicação, agrupamento, silenciamento e inibição precisam de owner e limites explícitos.

Probes externos complementam métricas internas; status page não demonstra sozinha cumprimento contratual. Preservar fonte, consulta, período e incidentes usados em relatórios. Encaminhar matriz de controles e provas a saas-compliance-evidence.

Fontes: [SLO Generator](https://github.com/google/slo-generator), [Pyrra](https://github.com/pyrra-dev/pyrra), [Sloth](https://github.com/slok/sloth), [Alertmanager](https://github.com/prometheus/alertmanager) e [Blackbox Exporter](https://github.com/prometheus/blackbox_exporter). Revisões em ../../evaluations/2026-10-05-saas-sla-compliance-repositories.md.
