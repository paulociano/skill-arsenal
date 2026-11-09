# claude-code-templates — reavaliação (2026-11-09)

## Fonte
- https://github.com/davila7/claude-code-templates — commit `280a697` (2026-11-09), MIT
- Avaliação anterior: `evaluations/2026-10-11-ten-repos-memory-web-code-skills.md` (KEEP_EXTERNAL_REFERENCE como radar de descoberta; owner `arsenal-autopilot`)
- Lidos nesta passagem: `README.md`, estrutura de `cli-tool/components/`, frontmatter dos 18 loops, um loop completo (`human-approval-loop`), `mods/README.md`

## O que mudou desde 2026-10-11
O catálogo cresceu para ~925 skills, ~420 agents, ~350 commands, 64 hooks, ~127 MCPs e 80 settings, e ganhou três categorias novas: **loops** (18 rotinas recorrentes com condição de parada e componentes referenciados), **mods** (plugins de interface/comportamento do Claude Code via function hooks, Claude Code 2.1.287+) e **sandbox** (Cloudflare, Docker, E2B). O CLI também oferece `--analytics` (monitor de sessões em localhost:3333) e `--chats` (leitura e busca das conversas em localhost:9876). Site de navegação: aitmpl.com.

## Decisão
| Item | Classe | Decisão |
|---|---|---|
| Catálogo e instalador (`npx claude-code-templates`) | D | **KEEP_EXTERNAL_REFERENCE** (mantida) — radar de descoberta; avaliar cada componente pela fonte original antes de adotar |
| Loops: condições de parada | **B** | **ABSORB_METHOD** — catálogo de condições de parada incorporado em `loop-engineering` |
| Mods, sandbox, analytics, chats | D | NÃO ADOTAR — runtime do Claude Code; `--chats` expõe o histórico de conversas num servidor local, usar só com consciência disso |

Absorção em massa das ~925 skills foi descartada: é um agregador de terceiros (muitas importadas de outros repositórios, inclusive fontes que o Arsenal já avaliou na origem), e o caminho correto é avaliar a fonte original de cada componente quando houver demanda.

## Implementado
- `skills/loop-engineering/SKILL.md`: seção "Catálogo de condições de parada" (contrato de conclusão, anti-spin, sequência de qualidade, construtor + revisor, advogado do diabo, aprovação humana, refinador de objetivo, manutenção incremental, orçamento de desempenho).

## Segurança
Nada executado (clone parcial, só leitura). O instalador baixa e grava componentes de terceiros em `.claude/`; hooks e mods passam a rodar em todas as sessões do projeto. `--yes` pula a confirmação: não usar. Componentes "vendored" de terceiros mantêm a licença original.

## Limites
Lidos só o frontmatter dos loops e um loop completo; skills, agents, hooks e mods não foram inspecionados individualmente.
