# Radar experimental — spatial interfaces, generative UI e human-AI co-creation

Data: 2026-09-30

## Objetivo

Pesquisar 30 projetos/repositórios experimentais fora da categoria simples de "alternativa a SaaS", buscando novas primitivas de interação entre humano, IA, conhecimento, canvas, agentes e criação.

Fluxo: `arsenal-autopilot`.

Nenhum installer, Docker image, script, agente, modelo, MCP, plugin ou serviço externo foi executado.

## Radar de 30 candidatos

### Generative UI / adaptive interfaces
1. `miurla/morphic` — search engine com respostas grounded/citadas e UI gerada por streamed JSON spec.
2. `cacheplane/cacheplane` — candidato de generative interface encontrado por discovery; referência experimental.
3. `LibreChat-AI/LibreChat` — artifacts/UI de chat extensível; referência de produto.
4. `nick-tonjum/open-webui-artifacts-overhaul` — experiments sobre artifacts em Open WebUI.
5. `genaiwithshubham/opennapkinai` — texto→visual estruturado, diagrams/sketches e RoughJS.

### Spatial / multimodal canvas
6. `joyedz/melda` — infinite multimodal canvas + proactive agent + workflow, unificados por Session Context Graph.
7. `jonbrown66/bananacanvas-ai` — AI infinite canvas; discovery/reference.
8. `sparklumina/sparklumina` — collaborative whiteboard + AI-generated Excalidraw elements + tutoring/TTS.
9. `vcmf/dim0` — canvas/AI experiment; discovery/reference.
10. `miha0001963/mikes-open-canvas` — open AI canvas experiment.
11. `KanishkRajTech/SmartCanvas` — smart/AI canvas experiment.
12. `chuck00lin/canvai` — AI canvas experiment.
13. `AtomicNixon/theblueai-whiteboard` — AI whiteboard experiment.
14. `bluevisor/open-bot-canvas` — governance/art experiment where agents evolve repository; kept as conceptual reference only.
15. `xiaohuaihua/Open-Source-AI-drawing-board-Experimental---ai-` — experimental AI drawing board.

### Knowledge / research / second-brain interfaces
16. `khoj-ai/khoj` — self-hostable personal AI, semantic search, docs/web, agents, automations.
17. `DeadWaveWave/opencove` — AI research canvas candidate.
18. `Susanth-kotagiri/ARC-AI-Research-Canvas` — research canvas candidate.
19. `MirzaMukarram0/Intelligent-Research-Canvas` — research canvas candidate.
20. `yibie/project-nodal` — spatial/graph knowledge candidate.
21. `dirmacs/project-nodal` — related/fork candidate; discovery only.
22. `himanshu-webkul/graphrag-workbench` — GraphRAG workbench/visualization.
23. `vedant-io/GraphRAG-Atlas` — graph-oriented RAG visualization candidate.
24. `NirDiamant/Agent_Memory_Techniques` — memory techniques catalog; discovery/reference.

### Visual workflow / agent builders
25. Flowise ecosystem — visual agent/workflow graph; source resolution required before adoption.
26. Langflow ecosystem — visual LLM flow builder; source resolution required before adoption.
27. Sim Studio ecosystem — visual AI workflow builder; source resolution required before adoption.
28. Dify ecosystem — workflow/agent application builder; source resolution required before adoption.
29. `LudwigKienle/ai-video-production-editor` — visual production workflow; already evaluated in creative-AI batch.
30. `presenton/presenton` — generative presentation editor; already evaluated, retained here as example of AI generation followed by direct-manipulation editing.

## Aprofundamento e capabilities

### 1. Generative UI não deve ser "modelo gera código arbitrário"

Morphic explicita uma abordagem melhor:
`answer/reasoning → streamed structured spec → known UI components`.

Capability incremental:
- forma da resposta pode se adaptar ao conteúdo;
- renderer continua sendo owner do comportamento e acessibilidade;
- schema controla quais componentes/props existem;
- provenance/citations permanecem no conteúdo;
- UI generation não implica execução de código irrestrito.

**Decisão:** A/B/D → UPDATE_EXISTING `structured-output-contract`.

### 2. Canvas pode ser uma view do contexto

Melda descreve um Session Context Graph compartilhado:
- projects;
- canvases;
- nodes;
- edges;
- assets;
- agent state;
- generation/analysis jobs;
- references/groups;
- semantic search.

A inovação metodológica não é "infinite canvas". É o mesmo record estrutural servir a:
- agente;
- interface;
- workflow;
- retrieval.

Isso reduz a duplicação entre "chat memory", "canvas state" e "pipeline state".

**Decisão:** A/B/D → UPDATE_EXISTING `kb-retriever`.

### 3. Context packing espacial

Canvas inteiro não deve ir ao modelo a cada turno.

Padrão derivado:
`goal + selected/focused nodes + explicit refs + relevant graph neighborhood + token budget → context pack`.

Guardrail:
proximidade espacial é um sinal de organização humana, não prova de relação semântica.

### 4. Direct manipulation + generation

Os projetos mais interessantes convergem para:
`generate → place in workspace → inspect/manipulate directly → reference/reuse → regenerate locally`.

Isso é superior, em muitos trabalhos criativos, a uma conversa que só produz outputs finais desconectados.

O Arsenal já cobre partes via image generation, web visual editing, presentation editing e artifact workflows. Nenhuma nova skill necessária neste lote.

### 5. AI as collaborator, not owner of every action

Projetos com proactive agents mostram valor de sugestões contextuais, mas autonomia precisa de limites:
- suggestion ≠ execution;
- idle/focus state pode sugerir oportunidade, não consentimento;
- ações externas permanecem sob approval;
- agente deve poder ser silenciado/snoozed;
- contexto observado não autoriza inferências pessoais desnecessárias.

Mantido como referência de interaction design, não novo owner.

### 6. Spatial knowledge ≠ knowledge truth

Graph/canvas interfaces são ótimas para navegação e sensemaking, mas:
- layout não substitui provenance;
- edge gerada por IA precisa ser distinguível de edge observada/declarada;
- cluster visual não prova causalidade;
- derived summaries não substituem source;
- canvas é uma projection/view quando o record canônico existe em outro lugar.

### 7. Agent-generated project governance

`bluevisor/open-bot-canvas` é experimentalmente interessante por tratar o próprio repositório como meio criativo e permitir propostas de agentes com governança humana/veto.

Não absorver o princípio "AI decide tudo". Para o Arsenal, o valor é mais estreito:
- provenance de qual modelo/agente propôs mudança;
- disclosure de input humano;
- incremental changes;
- human veto/approval boundary;
- deterministic artifacts quando possível.

Esses princípios já pertencem a `multi-agent-orchestration`, `agent-choice-audit` e `verify-before-claim`.

## Mudanças canônicas

### UPDATE — `structured-output-contract`

Adicionado **Generative UI como contrato estruturado**:
- schema de componentes;
- component registry;
- props tipadas;
- states;
- safe unknown handling;
- streaming não substitui validação;
- conteúdo recuperado não pode elevar privilégios;
- presentation separada de actions/effects.

### UPDATE — `kb-retriever`

Adicionado **Contexto espacial e grafo de sessão**:
- nodes/edges/groups;
- references;
- selection/focus como signal;
- context packing por budget;
- spatial proximity não é semantic truth;
- canvas/search/UI como views sobre record persistente quando aplicável.

## O que não virou skill

- "AI canvas" genérico;
- "second brain" genérico;
- "proactive agent" genérico;
- "GraphRAG visualizer";
- "AI whiteboard";
- "agent builds everything";
- "generative UI framework".

Esses nomes descrevem produtos/arquiteturas amplas. O valor incremental foi absorvido nos owners menores corretos.

## Segurança e portabilidade

- nenhum runtime externo foi executado;
- nenhum provider/API key foi conectado;
- nenhuma automação proativa foi ativada;
- nenhuma fonte privada foi indexada;
- nenhum graph/embedding store externo foi criado;
- UI gerada não foi tratada como código confiável;
- self-hosted/local não foi tratado como garantia automática de privacidade;
- forks e resultados de discovery não substituem upstream canônico;
- claims de roadmap não foram tratados como capability entregue sem evidência.

## Conclusão

A primitive mais interessante deste lote é:

`shared structured context → multiple views → selective context pack → generation/action → persistent update`.

Em vez de fazer o chat carregar todo o trabalho, o chat passa a ser uma das interfaces sobre um workspace persistente. Canvas, busca, timeline, artifacts e agentes podem ser projections diferentes do mesmo contexto estruturado.

Isso é mais promissor para human-AI co-creation do que simplesmente adicionar mais um chatbot ou mais um gerador.
