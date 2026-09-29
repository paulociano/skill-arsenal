# Avaliação em lote — agent runtimes, avatars, gesture UI, visual skills e Canvas UI

Data: 2026-09-29

## Escopo

Fontes:
- https://github.com/zeronsh/zeron
- https://github.com/Alain00/blobatar
- https://github.com/yetone/cumora
- https://github.com/herdrdev/herdr
- https://github.com/jaredrhod/barehands
- https://github.com/s1dashu/ip-as-logo-skill
- https://github.com/Leonxlnx/unlazy
- https://github.com/truefoundry/trueforge
- https://canvasui.dev/

Fluxo aplicado: `arsenal-autopilot` + `evaluate-and-import-skill` + revisão de segurança proporcional.

Nenhum installer, package script, daemon, hook, câmera, browser runtime, modelo externo, MCP externo ou código das fontes foi executado.

## Resumo executivo

- `Leonxlnx/unlazy`: **A/B/D** — metodologia forte de acceptance ledger e re-verificação; scripts/hook são técnicos. **UPDATE_EXISTING** em `verify-before-claim`.
- `s1dashu/ip-as-logo-skill`: **A/B** — processo visual útil e específico, mas sobreposto ao owner canônico. **UPDATE_EXISTING** em `brand-logo-exploration`.
- `yetone/cumora`: **B/D** — runtime completo; coordenação traz padrões portáveis importantes. **UPDATE_EXISTING** em `graph-engineering`.
- `truefoundry/trueforge`: **B/D** — agent harness com approvals, sandbox, deferred tools e compaction. **ABSORB_METHOD_ONLY** em coordenação/runtime, sem importar infraestrutura.
- `herdrdev/herdr`: **B/D** — runtime multiagente já representado no Arsenal. **KEEP_EXTERNAL_REFERENCE**; sem nova mudança porque `multi-agent-orchestration` já registra origem e princípios.
- `zeronsh/zeron`: **B/D** — control plane local-first para coding agents. **KEEP_EXTERNAL_REFERENCE**; conceitos de workspace/session/approvals já cobertos por skills existentes.
- `Alain00/blobatar`: **D** com boas práticas B — biblioteca determinística de avatar. **KEEP_EXTERNAL_REFERENCE**; não justifica skill própria.
- `jaredrhod/barehands`: **D** — gesture UI/webcam/MediaPipe/Three.js com protocolo de estado e allowlist. **KEEP_EXTERNAL_REFERENCE**; valor é de produto/runtime, não skill genérica.
- `Canvas UI`: **D/B** — catálogo técnico de efeitos Canvas/WebGL/WebGPU. Já era referência de `creative-web-effects`; **UPDATE_EXISTING** na nota de renderer/licença/fallback.

## Avaliações

### zeronsh/zeron

**Classificação:** B/D.

**O que faz:** control plane local-first para vários coding agents, com sessões, workspace, diff, comandos e approvals, além de sync opcional entre dispositivos.

**Valor incremental:** a separação local-only/synced e o tratamento explícito de workspace/approvals são bons padrões, mas o Arsenal já possui `multi-agent-orchestration`, `graph-engineering`, `agenda-operations`, `verify-before-claim` e boundaries de execução.

**Segurança:** CAUTION. O produto inclui daemon, auto-update, login/sync e acesso remoto a workspaces; em sync, dispositivos confiáveis podem ler/escrever arquivos remotos, inclusive ignorados quando habilitado.

**Decisão:** não importar runtime nem criar skill. Manter como referência externa de control plane.

### Alain00/blobatar

**Classificação:** D com metodologia B pontual.

**O que faz:** gera avatares geométricos determinísticos a partir de string, com adapters para múltiplos frameworks e paridade seed-to-look.

**Valor incremental:** bons padrões de determinismo visual, paridade cross-platform, reduced-motion e fallback acessível. Isso pode inspirar implementação quando surgir tarefa concreta, mas não muda comportamento geral do ChatGPT como skill.

**Segurança:** APPROVE para metodologia. Dependências/runtime são de biblioteca frontend; endpoint público opcional é rate-limited e não deve ser tratado como infraestrutura garantida.

**Decisão:** manter referência externa. Sem skill nova.

### yetone/cumora

**Classificação:** B/D.

**O que faz:** chat multiagente com agentes e humanos, claims de trabalho, board/calendário e runtime BYOA/cloud.

**Valor incremental:** forte na distinção entre colisão de concorrência e erro de julgamento do modelo; usa seen-cursor/freshness, claims atômicos, concurrency caps, pacing determinístico, coalescing e backoff adaptativo.

**Segurança:** CAUTION alto. Envolve chaves de provider, Postgres, Redis, Kubernetes, subprocessos locais, email e filesystem. Não importar execução.

**Decisão:** absorver padrões portáveis em `graph-engineering`.

### herdrdev/herdr

**Classificação:** B/D.

**O que faz:** runtime/ambiente operacional para coding agents, com worktrees, branches, estado e processos de revisão.

**Valor incremental:** já foi absorvido anteriormente em `multi-agent-orchestration` e aparece como origem canônica da skill. Nova importação seria duplicação.

**Segurança:** CAUTION. Shell, hooks, worktrees, persistência e agente runtime aumentam superfície operacional.

**Decisão:** manter referência externa; nenhuma skill nova.

### jaredrhod/barehands

**Classificação:** D.

**O que faz:** interface gestual por webcam com MediaPipe e Three.js; expõe um protocolo simples para agente apresentar cards, imagens e estado, com allowlist e media jail.

**Valor incremental:** padrões de action allowlist, state reflection e observação antes de agir são úteis, mas já são cobertos por boundaries/estado em skills de loop e runtime. A parte central depende de câmera, browser, CDN e gesture tracking.

**Segurança:** CAUTION. Câmera, servidor local, scripts e conteúdo de mídia exigem runtime real. Licença AGPL exige atenção se código for incorporado.

**Decisão:** referência externa, sem importação.

### s1dashu/ip-as-logo-skill

**Classificação:** A/B.

**O que faz:** pipeline específico para mascotes/IP muito simples, com três direções, variantes controladas, small-size readability e composição coerente.

**Valor incremental:** útil, mas o owner já é `brand-logo-exploration` + `high-fidelity-image-generation`. O ganho está no método, não em uma skill paralela.

**Segurança:** APPROVE para metodologia. A fonte sugere modelos externos específicos e CLI de skills; isso não é importado.

**Decisão:** absorver no owner `brand-logo-exploration`, sem fixar número obrigatório de imagens nem modelo externo.

### Leonxlnx/unlazy

**Classificação:** A/B/D.

**O que faz:** disciplina de conclusão com acceptance ledger, checks explícitos, reverify e orquestração por leaves/branches; inclui scripts Node e hooks opcionais.

**Valor incremental:** forte porque formaliza um problema recorrente: tarefas grandes podem parecer concluídas mesmo omitindo um outcome independente. A distinção entre status registrado e reexecução é especialmente útil.

**Segurança:** CAUTION para runtime, APPROVE para metodologia. O checker executa comandos aprovados; aprovação não é sandbox. Não importar scripts/hook.

**Decisão:** atualizar `verify-before-claim` com acceptance ledger e stale evidence/reverification.

### truefoundry/trueforge

**Classificação:** B/D.

**O que faz:** harness de agentes com model loop, MCP, skills, sandbox, approvals, context management, subagents, deferred tools e session state.

**Valor incremental:** confirma bons padrões de progressive tool loading, human checkpoints e separação entre runtime, sandbox, skills e contexto. No Arsenal, owners já existem para esses princípios.

**Segurança:** CAUTION alto. O sistema integra providers, OAuth/header auth, sandboxes, servidores, DB, Redis e ferramentas externas.

**Decisão:** absorver apenas princípios portáveis; nenhuma skill nova.

### Canvas UI

**Classificação:** B/D.

**O que faz:** biblioteca de componentes em Canvas/WebGL/WebGPU, incluindo efeitos sobre HTML e objetos 3D, com variantes multi-framework.

**Valor incremental:** já estava no catálogo de `creative-web-effects`. A atualização relevante é registrar escolha WebGL vs WebGPU, fallback e licença/redistribuição com mais precisão.

**Segurança:** CAUTION de performance/browser support, não de execução maliciosa. Parte do html-in-canvas é experimental e requer fallback.

**Decisão:** atualizar referência existente, sem criar skill.

## Mudanças aplicadas

- `verify-before-claim`: acceptance ledger, stale evidence e reexecução pós-mudança.
- `brand-logo-exploration`: padrões de mascote/IP simples e legibilidade em 32×32.
- `graph-engineering`: separação entre race collision e brain misjudgment, freshness/claims/coalescing/pacing.
- `creative-web-effects/references/animated-component-libraries.md`: Canvas UI com WebGL/WebGPU, fallback e licença mais precisa.
- Este registro em `evaluations/`.

## Decisões de não-criação

Nenhuma nova skill foi criada porque todas as capabilities úteis já possuem owner canônico adequado. Criar skills adicionais aumentaria overlap sem ganho de roteamento.

## Limites

- Nenhum benchmark dos autores foi reproduzido.
- Nenhum runtime externo foi executado.
- Não houve scanner automatizado dedicado; revisão foi estática e proporcional ao escopo.
- Canvas UI foi verificado pela documentação pública atual; a licença deve ser checada no item/commit efetivamente copiado.
