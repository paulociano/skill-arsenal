# oh-my-claudecode (2026-11-09)

## Fonte
- https://github.com/Yeachan-Heo/oh-my-claudecode — commit `b91b30e` (2026-11-09), pacote `oh-my-claude-sisyphus` v5.8.2, MIT
- Lidos: descrições das 85 skills em `skills/`, lista de 19 agentes em `agents/`, `package.json`; SKILL.md completos de `benchmark-checklist`, `correct`, `show-me-your-work`, `why` e `arena`
- Avaliação anterior relacionada: `evaluations/2026-10-10-context-marketing-pstack-effect.md` (pstack-claude mantido como referência externa, sem absorção). Cinco skills do OMC são ports de pstack e foram reavaliadas sob a regra de 2026-10-15 (implementar antes de declarar concluído).

## O que é
Plugin de orquestração multiagente para Claude Code, inspirado no oh-my-opencode: 85 skills, 19 agentes especializados (planner, architect, executor, critic, verifier, security-reviewer…), modos autônomos (autopilot, ralph, ultragoal, team, swarm), hooks, HUD, servidor MCP, roteamento de modelos entre Claude/Codex/Gemini e um harness de entrega ("shipyard") com estado em `.omc/`. READMEs em 13 idiomas, incluindo português. Muito ativo (commit no dia da avaliação).

## Decisão geral
**Não instalar o plugin.** É um sistema operacional paralelo para o Claude Code: hooks, estado próprio em `.omc/`, CLI `omc`, modos que rodam em loop até concluir e roteamento para outros provedores. Sobrepõe-se ao que o Arsenal já organiza (`arsenal-router`, stacks, `software-engineering-cycle`, superpowers e mattpocock já avaliados) e mudaria o comportamento padrão de todas as sessões. Absorvidos cinco métodos portáveis que não tinham owner.

## Absorvido (ABSORB_METHOD, implementado)

| Skill OMC | Owner no Arsenal | O que entrou |
|---|---|---|
| `benchmark-checklist` | `verify-before-claim` | números medidos: nomear limitante, medir o trabalho afirmado, ≥5 repetições com mediana e dispersão, descartar o observador, rotular medido/inferido/palpite |
| `correct` | `session-learn` | escada de enforcement para erros recorrentes (lint → tipo → runtime → script → texto) com prova de que dispara |
| `show-me-your-work` | `handoff` | trilha de decisões append-only escrita no momento da decisão |
| `why` | `code-understanding-audit` | arqueologia de código com fontes em ordem de autoridade e rótulos evidência/inferência/palpite |
| `arena` | `multi-agent-orchestration` | N candidatos no mesmo brief, rubrica oculta, juiz cruzado, escolha por critério, enxerto e verificação |

## Já coberto no Arsenal (ALREADY_OWNED)
- Planejamento, especificação e entrevista: `plan`, `ralplan`, `sdd`, `deep-interview`, `sharpen`, `in-your-own-words`, `intent`, `ask-navigator` → `deep-grill`, `wayfinder`, `project-planning`, `architectural-design-cycle`.
- Execução, TDD e depuração: `execute`, `tdd`, `debug`, `trace`, `fix-merge-conflicts`, `minimal-code-discipline`, `typescript-best-practices`, `ai-slop-cleaner` → `software-engineering-cycle`, `debug-and-fix`, `diagnosing-bugs`, `tdd`, `software-testing-engineering`, `merge-conflict-resolution`.
- Revisão e verificação: `review`, `verify`, `interrogate`, `blast-radius`, `visual-verdict`, `create-verification-skill`, `maintain-verification-skill` → `code-review`, `verify-before-claim`, `runtime-ui-verification`, `architecture-visualization` (blast radius de PR).
- Arquitetura e explicação: `architect`, `architecture-survey`, `how`, `teach`, `diagram`, `loft` → `codebase-design`, `code-understanding-audit`, `teach`, `architecture-visualization`, `python-interactive-prototyping`.
- Escrita: `technical-writing`, `minimal-prose-discipline`, `agent-doc-discipline`, `bro` → `writing-quality`, `plain-writing`, `prose-lint`, `project-skill-architecture`.
- Memória e sessão: `remember`, `recall`, `session-flow`, `wiki`, `personal-mode`, `reflect`, `refit`, `skillify` → `agent-memory-engineering`, `session-learn`, `handoff`, `skill-builder`. O `personal-mode` (perfil de comportamento a partir de transcripts) não foi adotado: a memória do Claude já cumpre esse papel com regras de privacidade.
- Pesquisa e loops de melhoria: `research`, `external-context`, `autoresearch`, `hillclimb`, `self-improve` → `discovery-research-synthesis`, `research-question-design`, `experiment-design`, `loop-engineering`.
- Orquestração: `team`, `graph`, `launch`, `figure-it-out`, `map`, `principles` → `multi-agent-orchestration`, `graph-engineering`, `arsenal-router`, `functional-skill-architecture`.
- Verificação formal: `create-formal-verification-skill`, `maintain-formal-verification-skill`, `statechart` → `formal-methods-reconciler`.
- Git/PR: `pr`, `get-pr-comments`, `babysit`, `fix-ci`, `stacked-delivery`, `release`, `project-session-manager` → `code-review`, `git-worktree-lifecycle`, `work-delivery-flow`, `progressive-delivery-verification`.

## Não adotado (D — runtime do plugin)
`autopilot`, `ralph`, `ultragoal`, `cancel`, `hud`, `omc-setup`, `omc-doctor`, `models`, `configure-notifications`, `ask`, `skill`, `drydock`, `harbor`, `deepinit`, `ketchup`, `ketchup-video`, `what-did-i-get-done`, `arena` (parte de runtime), `benchmark`/`geobench`: dependem do CLI `omc`, do estado `.omc/`, de hooks ou de roteamento multi-provedor. `ketchup` e `what-did-i-get-done` (resumos de status e de commits) são úteis mas triviais de reproduzir com um pedido direto; registrados como referência.

## Segurança e portabilidade
Nada foi executado (repositório clonado só para leitura). Riscos de instalar o plugin: hooks em todas as sessões; modos autônomos em loop ("até concluir") com custo de tokens alto; roteamento para Codex/Gemini/Grok/Cursor envia código a outros provedores; notificações para Telegram/Discord/Slack; HUD e estado local em `.omc/`. Nenhum problema de código malicioso foi procurado ou encontrado nesta leitura documental.

## Limites
Lidas integralmente apenas as cinco skills absorvidas; as demais pela descrição. Agentes, hooks, `src/` e o harness shipyard não foram lidos.

## Arquivos atualizados
- skills/verify-before-claim/SKILL.md
- skills/session-learn/SKILL.md
- skills/handoff/SKILL.md
- skills/code-understanding-audit/SKILL.md
- skills/multi-agent-orchestration/SKILL.md
- evaluations/2026-11-09-oh-my-claudecode.md (novo)
