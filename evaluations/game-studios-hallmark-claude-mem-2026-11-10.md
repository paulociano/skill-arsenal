# Avaliação: Claude-Code-Game-Studios, Hallmark v2 e claude-mem

- Data: 2026-11-10
- Fluxo: `evaluate-and-import-skill` + `skill-security-review` (inspeção estática; nada instalado ou executado)

| Fonte | Classe | Decisão | Owner atualizado |
|---|---|---|---|
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | A/D | UPDATE_EXISTING | `skills/game-development-engineering/SKILL.md` |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) v2.0.0 | A/D | UPDATE_EXISTING (reavaliação) | `skills/web-design-engineer/SKILL.md` |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) v15.15.2 | D | ABSORB_METHOD_ONLY | `skills/agent-memory-engineering/SKILL.md` |

## 1. Claude-Code-Game-Studios

- Evidência: README, `.claude/settings.json`, lista de `.claude/agents` (49), `.claude/skills` (78), `.claude/hooks` (18), `skills/prototype/SKILL.md`.
- Função real: template de projeto Claude Code que simula um estúdio (diretores, programadores, QA etc.). O fluxo principal `/prototype` faz perguntas por gênero → brief de uma página → jogo HTML jogável → checagem headless → cartão de entrega → PROCEED/PIVOT/KILL; depois cresce para Vite/TS com uma feature por sessão.
- Delta: rastreio brief → build linha a linha com status *built/missing/broken/not assessed* e cartão de entrega que declara "ainda não jogado por uma pessoa". O Arsenal já tinha runtime evidence e loops pequenos em `game-development-engineering` e `game-development-cycle`, mas não esse contrato de entrega.
- Não incorporado: os 49 agentes-persona (sobrepõem as 19 skills `game-*` do Arsenal), hooks, scripts bash e permissões.
- Segurança: **CAUTION**. `settings.json` pré-autoriza dezenas de scripts bash, `npm install`, `git commit` e tags; 18 hooks rodam em sessão, leitura, escrita, commit e push. Bloqueia `rm -rf`. Usar só numa cópia do repositório dedicada ao jogo, revisando hooks antes.
- Instalar no Claude: não é skill nem plugin, é um template para clonar e abrir no Claude Code. Faz sentido como ponto de partida de um jogo novo em navegador; não misturar com os projetos de jogo já em andamento.
- Licença: MIT.

## 2. Hallmark v2 (reavaliação)

- Evidência: README, `package.json` (2.0.0), `skills/hallmark/SKILL.md`, `references/gates.md`, `scripts/` (grep de rede/exec).
- v1 já absorvida em 2026-09-20 (seleção estrutural em `web-design-engineer` e `landing-craft`).
- Delta v2: gates em camadas Piso / Reflexo / Acabamento, com dispensa registrada exigindo evidência e motivo específico, e relato separado de falhas de Piso. Incorporado como parágrafo em `web-design-engineer`.
- Não incorporado: 50 temas, 755 fotos, sloplint (≈5,7 mil linhas), crítica pré-emissão com notas 1–5 (nota subjetiva não é prova, mesma decisão de 2026-09-20), proibições estéticas categóricas.
- Segurança: **CAUTION**. `capture.mjs` usa Puppeteer/Chrome e `execSync('npm root -g')`; `imagegen.mjs` envia prompts a `api.together.xyz` com `TOGETHER_API_KEY` (opt-in); `install-hook.mjs` instala hook de lint.
- Instalar no Claude: possível como skill no Claude Code (`skills/hallmark`). Sobrepõe skills já instaladas (`unslop`, `impeccable`, `design-taste-frontend`, `no-ai-slop`); não recomendado acumular mais uma skill anti-slop. No Claude chat, scripts não rodam.

## 3. claude-mem

- Evidência: README, `package.json`, `plugin/hooks/hooks.json`, `docs/CHANGELOG.md` (grep privacidade/telemetria).
- Função real: plugin de memória persistente para Claude Code/Codex/Cursor etc. Hooks em 9 eventos (Setup, SessionStart, UserPromptSubmit, Pre/PostToolUse, PostToolUseFailure, Stop, SubagentStop, SessionEnd) enviam cada chamada de ferramenta a um worker local; um agente observador (Claude Agent SDK) resume em observações; SQLite + FTS5 e Chroma; na sessão seguinte injeta índice compacto.
- Delta: `agent-memory-engineering` já cobre retrieval progressivo, índices reconstruíveis, redaction e consentimento para hooks. Acrescentadas duas lições: redigir blocos privados **antes** de truncar (bug real corrigido no #5663) e tratar o agente observador como trust boundary com custo próprio.
- Segurança: **CAUTION alto**. Captura toda atividade de ferramentas (inclui conteúdo de arquivos lidos); chamadas extras ao modelo por observação; worker HTTP local em background; telemetria PostHog (com consentimento, segundo changelog); hook Setup executa shell longo que procura versões em `~/.nvm`; sincronização em nuvem e autenticação (`better-auth`) presentes.
- Instalar no Claude: no Claude chat não se aplica (já há memória nativa). No Claude Code, só se a perda de contexto entre sessões for um problema real; conferir telemetria/sync desligados e usar `<private>` para dados sensíveis.
- Licença: Apache-2.0.

## Limites da validação
Leitura de README, manifestos, um SKILL.md por fonte, `gates.md`, `hooks.json` e grep de scripts. Código-fonte completo, dependências e comportamento em runtime não auditados.
