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

## Validar resposta gerada por SQL ou text-to-SQL

Quando um número vier de consulta gerada por agente, planilha com fórmula ou ferramenta NL-to-SQL, checar consulta, linhas e texto separadamente; a consulta rodar sem erro não prova que respondeu à pergunta.

1. **Pergunta material antes de consultar:** população e exclusões; medida, unidade e grão; agrupamento e distinct; período, data de corte e base de comparação; status/versão válidos. Ambiguidade material é perguntada, não preenchida com o default conveniente. Não trocar a medida por outra de nome parecido.
2. **Inspecionar a consulta:** todos os filtros, joins e predicados de tempo presentes; joins pelas chaves certas; agregar no grão do detalhe antes de juntar a um resumo; não somar uma métrica já agregada depois de um join um-para-muitos (fanout); não trocar quantidade por taxa ou média.
3. **Checar as linhas de forma independente:** chaves, cardinalidade, unidades, período e denominador; recalcular totais e razões simples. Vazio ou nulo não é zero. Resultado truncado não prova lista completa, ranking ou total.
4. **Checar o texto:** começar pelos valores retornados; separar observado, calculado, modelado, previsto e recomendado. Associação não é causa.
5. **Recibo:** pergunta, fonte, consulta, linhas, contagem, truncamento, resposta e lacunas; nunca credenciais.

Adaptado de `skills/nvidia-ontology-query/references/query-validation.md` em [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) (Apache-2.0), avaliado em 2026-11-10, sem exigir o servidor, NIM ou MCP da fonte.

## Integração

dashboard-design, root-cause-analysis, experiment-design, web-analytics-ga4, social-analytics e scenario-forecasting.

## Origem metodológica

Adaptada de padrões de product analytics, experimentação e semantic metrics observados em PostHog, GrowthBook e MetricFlow.
