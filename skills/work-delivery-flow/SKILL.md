---
name: work-delivery-flow
description: "Operar fluxo de trabalho e entregas por um record único de itens, estados, owners, prazos, dependências, WIP, aging e exceções, conectando planejamento, execução e gestão à vista sem transformar atividade em progresso."
---

# Work Delivery Flow

## Objetivo
Projetar ou revisar o sistema operacional de execução de uma equipe: como trabalho entra, é priorizado, assume owner, flui por estados, encontra dependências, vence prazos, entrega valor e aparece em gestão à vista.

## Quando usar
- pipeline operacional;
- kanban ou board de entregas;
- gestão de prazos e milestones;
- carteira de projetos/tarefas;
- desenho de workflow;
- gestão à vista de execução;
- redução de trabalho parado, overload ou handoffs opacos;
- implantação/revisão de ferramentas de project/work management.

Para construir o plano inicial de um projeto, usar project-planning. Para revisar saúde de projetos já em andamento, usar project-health-review.

## Work record
Cada unidade rastreável deve ter somente os campos necessários, entre:
- id/título;
- outcome ou deliverable relacionado;
- tipo;
- status;
- owner;
- prioridade;
- created/started/due/completed dates;
- milestone/cycle;
- dependencies/blockers;
- estimate/size quando útil;
- labels/workstream;
- next action;
- review date;
- source/evidence.

Views diferentes devem projetar o mesmo record. Board, list, calendar, timeline, dashboard e relatório não devem criar verdades concorrentes.

## Workflow
1. Definir a unidade de trabalho e o que significa DONE.
2. Mapear estados reais do fluxo, incluindo waiting/blocked quando material.
3. Definir entry/exit criteria apenas onde reduzem ambiguidade.
4. Explicitar owner e próximo movimento.
5. Registrar prazo e milestone separadamente do status.
6. Mapear dependências que realmente bloqueiam sequência.
7. Definir WIP/capacidade quando overload ou multitarefa prejudicam fluxo.
8. Tornar aging visível por estado e por blocker.
9. Criar views por decisão: individual, equipe, prazo, milestone, exceção, portfolio.
10. Definir cadência de triage/check-in/review.
11. Medir fluxo apenas quando a definição dos eventos é confiável.
12. Usar a revisão para decidir ação, não apenas atualizar percentuais.

## Gestão de prazo
Distinguir:
- target date;
- committed date;
- external deadline;
- forecast;
- milestone;
- review/checkpoint.

Não transformar target em compromisso silenciosamente. Quando forecast mudar, preservar a diferença entre baseline e expectativa atual.

## Fluxo
Sinais úteis, quando calculáveis com dados consistentes:
- WIP;
- throughput;
- cycle time;
- lead time;
- aging WIP;
- blocked time;
- arrival vs completion rate;
- milestone hit/miss;
- overdue count e overdue age.

Métrica de fluxo serve para diagnosticar sistema, não para rankear pessoas.

## Gestão à vista
A visão operacional deve favorecer:
1. overdue/at risk;
2. blocked e aging;
3. próximo milestone;
4. dependências críticas;
5. overload/capacidade;
6. decisões pendentes;
7. owner + próxima ação + review date.

Quantidade total de tarefas é contexto, não headline automática.

## Cadência
Separar ritmos quando necessário:
- intake/triage;
- daily/async flow check;
- weekly delivery review;
- milestone review;
- portfolio review;
- retrospective.

Cada ritual precisa de pergunta decisória e consequência. Não criar reunião apenas porque existe um board.

## Regras
- Não usar percent complete sem definição observável.
- Não considerar item movido como valor entregue.
- Não esconder waiting/blocked dentro de "in progress".
- Não aumentar WIP para compensar atraso.
- Não atribuir atraso automaticamente a performance individual.
- Não usar deadline inventado para criar urgência.
- Não duplicar manualmente o mesmo status em board, planilha e apresentação.
- UNKNOWN/stale deve permanecer visível.

## Integração
project-planning, project-health-review, dashboard-design, prioritization-engine, team-health-management, meeting-to-actions, agenda-operations, after-action-review e scenario-forecasting.

## Origem metodológica
Síntese de padrões observados em OpenProject, Plane, Leantime, Taiga, Kanboard, Wekan, PLANKA, Nextcloud Deck, Kaneo, ZenTao, Operately e plataformas de métricas de entrega como Apache DevLake e Metrik. Os runtimes permanecem referências externas.
