---
name: dashboard-design
description: "Projetar dashboards orientados a decisão com métricas confiáveis, hierarquia, comparação, filtros e narrativa operacional sem confundir painel com depósito de gráficos."
---

# dashboard-design

## Objetivo

Projetar dashboards como interfaces de decisão e monitoramento, conectando pergunta de negócio, métrica, visualização, contexto e ação.

## Quando usar

- dashboards executivos, comerciais, produto, operações ou finanças;
- Power BI, Tableau, Looker, Superset, Metabase, Grafana, Streamlit, Dash, Evidence ou web custom;
- redesign de painéis existentes;
- escolha de KPIs e hierarquia visual.

## Workflow

1. Definir usuário, decisão e cadência de uso.
2. Para cada pergunta, definir métrica e grain.
3. Confirmar fonte, atualização, timezone, população e definição.
4. Separar:
   - headline KPIs;
   - drivers;
   - diagnostics;
   - detalhes operacionais.
5. Escolher comparação apropriada: meta, período anterior, benchmark ou cohort.
6. Escolher visual pelo tipo de pergunta:
   - tendência;
   - ranking;
   - composição;
   - distribuição;
   - relação;
   - fluxo/funil;
   - tabela detalhada.
7. Construir hierarquia visual e ordem de leitura.
8. Adicionar filtros somente quando ajudam uma decisão real.
9. Projetar estados de loading, vazio, erro e dados incompletos.
10. Testar consistência métrica, legibilidade e uso em viewport real.
11. Registrar definições e ownership das métricas críticas.

## Regras

- Um KPI sem comparação ou contexto frequentemente não informa ação.
- Não usar pie/donut/gauge/map por hábito; justificar pela pergunta.
- Evitar dashboard de "uma tela com tudo".
- Cor deve codificar significado consistente.
- Não esconder denominadores, filtros ou períodos relevantes.
- Interatividade não substitui hierarquia.
- Dashboard executivo deve permitir aprofundamento, mas não exigir exploração para entender o estado.

## Integração

product-metrics-diagnostics, scenario-forecasting, data/storytelling workflows, web-design-engineer, Power BI engineering e verify-before-claim.

## Origem metodológica

Sintetiza padrões observados em Superset, Metabase, Grafana, Dash, Streamlit, Evidence e Observable Framework, com foco em decisão e sem depender de uma plataforma.
