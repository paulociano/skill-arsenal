---
name: product-metrics-diagnostics
description: "Diagnosticar movimentos de métricas por definição, funil, cohort, segmento, drivers e qualidade de dados antes de propor ação."
---

# product-metrics-diagnostics

## Objetivo

Responder "o que mudou e por quê?" em métricas de produto ou negócio com decomposição estruturada, evitando narrativas causais precipitadas.

## Quando usar

- KPI subiu/caiu;
- funil, activation, retention, churn ou engagement;
- comparação de cohort/segmento;
- dashboards que mostram movimento sem explicar drivers;
- preparação de executive briefing.

## Workflow

1. Confirmar definição, fórmula, grain, população, timezone e janela.
2. Validar freshness, missingness, tracking e mudanças de schema.
3. Quantificar magnitude vs baseline e sazonalidade.
4. Decompor:
   - volume;
   - mix;
   - conversion rate;
   - frequency;
   - retention/churn;
   - segment/cohort.
5. Identificar onde o movimento aparece e onde não aparece.
6. Mapear eventos ou mudanças plausíveis no período.
7. Formular hipóteses falsificáveis.
8. Usar root-cause-analysis para causalidade mais profunda.
9. Diferenciar driver aritmético de causa comportamental.
10. Recomendar próximos dados/testes e métricas de acompanhamento.

## Métricas

Evitar escolher north-star ou KPI apenas por popularidade. Uma métrica útil precisa ter:
- definição estável;
- relação com valor entregue;
- sensibilidade suficiente;
- baixa manipulabilidade;
- decomposição em drivers operacionais.

## Regras

- Mudança de tracking pode parecer mudança de produto.
- Média agregada pode esconder cohorts/segmentos.
- Percentual sem denominador é perigoso.
- Funil não implica causalidade entre etapas.
- Experiment result e observational trend têm força de evidência diferente.

## Integração

dashboard-design, root-cause-analysis, experiment-design, web-analytics-ga4, social-analytics e scenario-forecasting.

## Origem metodológica

Adaptada de padrões de product analytics, experimentação e semantic metrics observados em PostHog, GrowthBook e MetricFlow.
