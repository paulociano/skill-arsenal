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

## Gate de viabilidade antes da construção

Em ideias de novos produtos, SaaS e mudanças de funcionalidades ainda não aprovadas, faça primeiro uma revisão curta da necessidade e dos riscos antes de especificar implementação. Distinga demanda e comprador, alternativa atual, distribuição/aquisição, diferencial verificável, custo de manutenção e hipótese de falha mais provável. Dê um veredito operacional: `construir pequeno`, `validar primeiro`, `pivotar primeiro` ou `não construir ainda`, com um teste barato e observável para reduzir a incerteza dominante. Para produto interno, portfólio ou aprendizado, avalie propósito e escopo, não imponha arbitrariamente critérios de tração comercial. Não bloqueie implementação rotineira já decidida e não transforme esse gate em questionário longo. Evidência insuficiente deve ser marcada como hipótese.

Origem complementar: https://github.com/bin1874/before-you-build-skill; metodologia absorvida sem `npx`, install ou Case Memory externo.

## Pipeline RPI com decisões persistentes

Para mudanças complexas em software, use *research → design → implement* somente na profundidade exigida:

1. **Research**: perguntas ainda abertas, mapa de componentes e dependências, evidência citada por arquivo/commit; não começar a implementar de suposições.
2. **Design**: escolher a forma proporcional ao risco: discussão de trade-offs, PRD, desenho técnico ou TDD. Registrar decisões e alternativas rejeitadas.
3. **Implementation outline**: decompor em slices testáveis, arquivos/owners, dependências, riscos e critérios de aceite.
4. **Implement**: mudar apenas escopo acordado, testar, revisar e registrar diferenças entre design e entrega.
5. **Continuity**: persistir artefatos em pasta de tarefa definida pelo projeto com origem/revisão dos repositórios, pontos resolvidos, pendências e próximo passo. Retomar a partir da última decisão válida, sem recriar documentos existentes.
6. Separar criação de documento, iteração e implementação; manter handoff autocontido quando mudar de sessão.

Não exigir subagentes, comandos `/rpi` ou `$rpi`, nem diretório `.agents/artifacts` quando o runtime ou projeto não os comportar. Não interromper tarefas claras apenas para perguntar qual formato de fluxo o usuário deseja.

**Origem adaptada:** https://github.com/humanlayer/skills/blob/main/plugins/rpi/skills/rpi/SKILL.md
