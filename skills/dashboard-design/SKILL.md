---
name: dashboard-design
description: "Projetar dashboards e sistemas de gestão à vista orientados a decisão, exceção e ação, com métricas confiáveis, ownership, cadência, comparação e hierarquia operacional."
---

# dashboard-design

## Objetivo

Projetar dashboards como interfaces de decisão e sistemas de gestão à vista: mostrar estado, desvio, causa provável e ação necessária com o mínimo de fricção.

## Quando usar

- dashboards executivos, comerciais, produto, projetos, operações ou finanças;
- gestão à vista diária ou semanal;
- Power BI, Tableau, Looker, Superset, Metabase, Grafana, Streamlit, Dash, Evidence ou web custom;
- redesign de painéis existentes;
- escolha de KPIs, scorecards e hierarquia visual.

## Modelo de gestão à vista

Uma visão operacional madura deve permitir responder rapidamente:

1. Estamos dentro do esperado?
2. Onde está a exceção?
3. Há quanto tempo ela existe?
4. Qual é o impacto?
5. Quem é o owner?
6. Qual é a próxima ação ou decisão?
7. Quando isso será revisto?

## Workflow

1. Definir usuário, decisão, horizonte e cadência de uso.
2. Para cada pergunta, definir métrica, grain, fonte e owner.
3. Confirmar atualização, timezone, população, definição e qualidade dos dados.
4. Separar camadas:
   - headline KPIs;
   - estado e exceções;
   - drivers;
   - diagnostics;
   - fila de ações;
   - detalhe operacional.
5. Definir comparação apropriada: meta, período anterior, benchmark, cohort ou baseline.
6. Quando houver status/RAG, definir limiares explícitos e permitir UNKNOWN.
7. Para gestão de projetos/equipes, incluir quando útil: próximo marco, aging, blockers, dependências, owner, ação, prazo/review date e tendência desde o último checkpoint.
8. Escolher visual pelo tipo de pergunta: tendência, ranking, composição, distribuição, relação, fluxo/funil, matriz de exceções ou tabela operacional.
9. Construir hierarquia visual e ordem de leitura: estado → exceção → explicação → ação.
10. Adicionar filtros somente quando ajudam uma decisão real.
11. Projetar estados de loading, vazio, erro, stale e dados incompletos.
12. Testar consistência métrica, legibilidade e uso em viewport real.
13. Registrar definições, ownership, cadência e regras de alerta das métricas críticas.
14. Quando o painel sustentar ritual de gestão, definir explicitamente o que acontece após cada alerta.

## Princípios de interface

- Exception-first: destacar desvio que requer atenção, não decorar todo número.
- Progressive disclosure: resumo executivo primeiro, detalhe sob demanda.
- Actionability: alerta sem owner ou próxima ação é ruído.
- Aging visível: exceção antiga deve ser distinguível de exceção recém-criada.
- Consistência temporal: comparação precisa usar períodos equivalentes.
- Densidade útil: informação compacta sem virar parede de widgets.
- Histórico: decisões melhoram quando estado atual pode ser comparado ao checkpoint anterior.

## Regras

- Um KPI sem comparação ou contexto frequentemente não informa ação.
- Não usar pie/donut/gauge/map por hábito; justificar pela pergunta.
- Evitar dashboard de "uma tela com tudo".
- Cor deve codificar significado consistente.
- Não esconder denominadores, filtros ou períodos relevantes.
- Interatividade não substitui hierarquia.
- Dashboard executivo deve permitir aprofundamento, mas não exigir exploração para entender o estado.
- Não mostrar GREEN quando a informação está ausente ou desatualizada.
- Não usar scores compostas quando dimensões conflitantes precisam permanecer visíveis.

## Integração

project-health-review, product-metrics-diagnostics, scenario-forecasting, prioritization-engine, web-design-engineer, powerbi-engineering e verify-before-claim.

## Origem metodológica

Evolui a síntese anterior de Superset, Metabase, Grafana, Dash, Streamlit, Evidence e Observable Framework com padrões de gestão à vista, project health e operational dashboards observados em borghei/Claude-Skills, alirezarezvani/claude-skills, SkillMedev/skills, KirKruglov/claude-skills-kit e synthesisengineering.
