# Avaliação em lote — compression gateway, persistent agent workspace, whiteboard SDK, ambient terminal, repo fleet status e photo abstraction

Data: 2026-09-30

## Escopo

Fontes:
- https://github.com/Paritok-official/paritok-4b-v1
- https://github.com/kirodotdev/KiroCrew
- https://github.com/quickdrawjs/quickdraw
- https://github.com/palamim/starboard
- https://github.com/yetidevworks/drydock
- https://github.com/Evianis/travel-photo-abstraction

Fluxo aplicado: `arsenal-autopilot`.

Nenhum installer, modelo, proxy, daemon, app desktop, MCP, script ou binário das fontes foi executado.

## Resumo

| Fonte | Classe | Decisão | Owner |
| --- | --- | --- | --- |
| Paritok | A/B/D | UPDATE_EXISTING / ALREADY_COVERED | `llm-observability-evaluation`, `codex-cost-efficiency` |
| KiroCrew | A/B/D | KEEP_EXTERNAL_REFERENCE | `multi-agent-orchestration`, `loop-engineering`, `session-learn` |
| Quickdraw | B/D | KEEP_EXTERNAL_REFERENCE | `visual-explanation-sketch`, `interactive-system-diagram` |
| Starboard | D/B | KEEP_EXTERNAL_REFERENCE | UI/runtime reference only |
| Drydock | A/B/D | ABSORB_METHOD_ONLY | `project-health-review`, `project-complexity-management` |
| travel-photo-abstraction | A | CREATE_NEW | `photo-relational-abstraction` |

## Paritok

### O que faz
Gateway intermediário entre agente e LLM que reduz schemas de ferramentas, comprime tool results/file reads, resume histórico antigo e permite recuperar originais sob demanda.

### Valor incremental
O Arsenal já possui critérios robustos para medir compressão em `llm-observability-evaluation` e economia em `codex-cost-efficiency`. O ganho desta fonte é reforçar três pontos:
- separar tool-schema filtering, content compression e history summarization como alavancas distintas;
- preservar caminho de recuperação do original e medir chamadas de expansão;
- manter conjunto de ferramentas selecionadas estável quando cache de prefixo for parte do objetivo.

Os percentuais, projeções de crescimento e custos publicados não foram promovidos a garantias.

### Decisão
Não criar nova skill nem instalar proxy/modelo. Manter como referência técnica para avaliações futuras de compressão.

## KiroCrew

### O que faz
Workspace persistente para agentes, com sessões, memória, skills, jobs longos, schedules, heartbeats, subagentes, apps e controles de segurança.

### Valor incremental
A metodologia mais útil é:
- checkpoints duráveis para trabalho longo;
- lições com escopo global ou por repositório;
- promoção de padrões recorrentes para skills inspecionáveis;
- separação entre schedules determinísticos e agentic runs;
- execução visível com approvals, logs e estado;
- policy ceiling acima da autonomia do agente.

### Decisão
Manter como runtime externo. Os owners `multi-agent-orchestration`, `loop-engineering`, `session-learn`, `skill-builder` e `verify-before-claim` já cobrem o comportamento metodológico.

## Quickdraw

### O que faz
SDK de infinite canvas/whiteboard com engine headless, React/React Native bindings, diffs JSON, undo/redo por gesto e export.

### Valor incremental
Boa referência para:
- estado imutável por records;
- mutation transactions que emitem diffs;
- undo como composição/inversão de diffs;
- remote diffs que não contaminam undo local;
- replay/audit por stream de diffs;
- canvas responsivo e input multimodal.

### Decisão
Referência técnica. Não cria skill nova porque o Arsenal já possui owners de sketching e diagramas; a maior parte depende de SDK/runtime.

## Starboard

### O que faz
Terminal macOS permanentemente ancorado ao Dock, com shell persistente e presença em todos os Spaces.

### Valor incremental
Traz uma ideia forte de UI: ferramenta ambiental que reduz custo de summon/focus/context switch. Entretanto a maior parte do valor é produto macOS específico, dependente de Accessibility, AppKit e shell persistente.

### Decisão
Manter referência externa para interaction design/runtime. Sem owner novo.

## Drydock

### O que faz
Dashboard local para dezenas ou centenas de repositórios, mostrando dirty/unpushed/behind/release state, atividade, conflicts e freshness.

### Valor incremental
Metodologia útil de fleet health:
- separar working state de release state;
- distinguir dado atual de dado baseado no último fetch;
- usar UNKNOWN/never-fetched em vez de zero quando não houve verificação;
- tiering de probes: sinais baratos sempre, sinais caros sob cache/freshness;
- não usar timestamps que ferramentas modificam incidentalmente como proxy de atividade;
- fetch/network é efeito externo e fica opt-in;
- filtros e contagens devem preservar semântica compatível para consumidores JSON.

### Decisão
Absorver como referência metodológica para portfolio/project health e observabilidade operacional, sem importar CLI/TUI.

## travel-photo-abstraction

### O que faz
Skill visual que decompõe fotografia em evidências, reduz essas relações a marks mínimos e reconstrói uma composição abstrata não literal.

### Valor incremental
Há capability nova e bem delimitada: preservar identidade relacional da foto sem style transfer nem miniature redraw. O método evidence → relation → mark é operacional e distinto dos owners existentes.

### Decisão
Criar `photo-relational-abstraction` no Arsenal, generalizada para diferentes layouts editoriais e sem importar scripts, assets, showcase, microtipografia ou restrições de execução da fonte.

## Mudanças publicadas

- CREATE `skills/photo-relational-abstraction/SKILL.md`
- UPDATE `ARSENAL INDEX.md` com a nova skill
- CREATE este registro de avaliação

## Segurança e portabilidade

- Nenhum proxy/modelo Paritok foi instalado ou executado.
- KiroCrew envolve persistência, hooks, jobs e conectores; nenhuma autonomia foi ativada.
- Quickdraw e Starboard foram avaliados como produtos/runtimes, não capacidades nativas.
- Drydock faz fetch opcional e shell-out para git; nenhuma operação foi executada.
- travel-photo-abstraction possui licença source-available com proibição de derivados; a skill do Arsenal foi escrita como síntese metodológica independente, sem copiar scripts, assets, showcase, layout proprietário ou blocos extensos de texto.

## Conclusão

Uma nova skill foi justificada: `photo-relational-abstraction`. As demais fontes reforçam owners existentes ou funcionam melhor como referências técnicas.
