---
name: project-planning
description: "Transformar objetivos em plano executável com outcomes, workstreams, marcos, dependências, caminho crítico, capacidade, riscos e critérios de conclusão sem falsa precisão."
---

# project-planning

## Objetivo

Converter um objetivo ou iniciativa em plano executável que mostre o que precisa acontecer, em que ordem, com quais dependências e quais sinais indicam progresso ou risco.

## Workflow

1. Definir outcome, escopo, não-escopo, restrições e definição de concluído.
2. Identificar entregáveis ou capacidades necessárias antes de listar tarefas.
3. Agrupar trabalho em workstreams coerentes.
4. Definir marcos verificáveis por resultado, não apenas por data.
5. Mapear dependências entre marcos e workstreams.
6. Identificar caminho crítico ou, com incerteza alta, as dependências que mais restringem a sequência.
7. Estimar esforço e capacidade em faixas quando não houver evidência para precisão maior.
8. Mapear riscos, assumptions e decisões pendentes.
9. Definir owners por papel quando pessoas não estiverem confirmadas.
10. Sequenciar execução, destacando trabalho que pode rodar em paralelo.
11. Definir checkpoints, critérios de aceite e gatilhos de replanning.
12. Passar decomposição detalhada para `to-tickets` quando tickets forem realmente necessários.

## Artefato mínimo

- outcome e definição de concluído;
- escopo / não-escopo;
- workstreams;
- marcos;
- dependências;
- caminho crítico ou restrições dominantes;
- riscos e assumptions;
- capacidade e horizonte;
- owners;
- próximos passos e checkpoints.

## Regras

- Não produzir Gantt por padrão.
- Não transformar estimativa fraca em data exata.
- Não confundir atividade com marco.
- Dependência precisa dizer o que bloqueia o quê.
- Plano deve mostrar o que pode mudar e quando reavaliar.
- Se a incerteza for dominante, usar descoberta e decision gates antes de detalhar tarefas distantes.

## Integração

project-complexity-management, graph-engineering, prioritization-engine, wayfinder, to-spec, to-tickets e project-health-review.

## Origem metodológica

Sintetiza práticas observadas em britt/agent-skills, borghei/Claude-Skills, janellecipriano/pm-skills, Nikoxkx/Agent-Skills e silvainfm/claude-skills. Integrações específicas de Jira/Linear/GitHub são opcionais e só devem ser usadas quando realmente conectadas.
