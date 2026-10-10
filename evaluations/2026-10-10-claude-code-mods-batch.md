# Avaliação em lote: oito projetos Claude Code (2026-10-10)

## Escopo e fontes
Fonte canônica consultada primeiro: [ARSENAL INDEX](https://github.com/paulociano/skill-arsenal/blob/master/ARSENAL%20INDEX.md). Router: `stacks/arsenal-autopilot/STACK.md`, incluindo `evaluate-and-import-skill` e critério de `skill-security-review`. Evidência: READMEs dos oito projetos, sem instalação ou execução de código. Classificações refletem **portabilidade ao ChatGPT**, não a qualidade absoluta dos mods em seu ambiente original.

| Fonte | Capacidade concreta | Classe | Decisão e owner |
|---|---|---|---|
| [savvy-progress](https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress) | Barra de progresso de tarefas e painel de subagentes com etapas, tempos e custos estimados via hooks/MCP | D | KEEP_EXTERNAL_REFERENCE. UX depende do mod runtime e APIs de subagentes do Claude Code. Não prometer painel ou dados de execução no ChatGPT. |
| [claude-skins](https://github.com/hellosverre/claude-skins) | 15 temas e cards para ferramentas, diffs, markdown, Mermaid e uso | D | KEEP_EXTERNAL_REFERENCE. Renderização da interface nativa do Claude Code, sem API equivalente para repintar o ChatGPT. |
| [claude-code-filetree](https://github.com/data-goblin/claude-code-filetree) | Filetree IDE, Git status e indicação de leituras/escritas em tempo real | D | KEEP_EXTERNAL_REFERENCE. Pane e hooks do Claude Code, sem visibilidade automática do filesystem local do usuário no ChatGPT. |
| [cache-tax](https://github.com/karanb192/cache-tax) | Mantém cache de prompt aquecido por pings e alerta sobre custo estimado de rewrite | D | REJECT para importação ChatGPT. Supõe TTL, faturamento, clock e hooks específicos do Claude Code. Pings têm custo; métricas não equivalem à cobrança do plano. |
| [blast-radius](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius) | Intercepta comandos arriscados e estima arquivos, commits ou migrações afetados antes de aprovar | A/D | UPDATE_EXISTING: `agent-action-governance`. Preservar preflight, estimativa, incerteza, gate e vinculação da aprovação ao alvo. Não prometer interceptação automática de shell no ChatGPT. |
| [claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | Detecta correções, propõe regras, deduplica e descobre padrões de workflow com aprovação | A/D | UPDATE_EXISTING: `agent-memory-engineering`. Captura com provenance, escopo e aprovação; não assumir captura de todos os prompts nem escrita automática em AGENTS.md. |
| [terminal-browser](https://github.com/zenbu-labs/terminal-browser) | Chromium/Electron offscreen renderizado no terminal via protocolo kitty, com CLI e SSH | D | KEEP_EXTERNAL_REFERENCE para engenharia local. Ferramenta técnica, não skill metodológica. ChatGPT não controla esse binário no computador do usuário. |
| [replay-theater](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater) | Replay cronológico de diffs de edições por hooks de turnos | B/D | ABSORB_METHOD_ONLY em revisões futuras de `code-review`/`agent-choice-audit` quando histórico de commits/diffs existir; não criar nova skill nem afirmar replay ao vivo. |

## Incremento comprovado
1. `skills/agent-action-governance/SKILL.md`: preflight de operações destrutivas com escopo, dry-run seguro e aprovação vinculada ao efeito real.
2. `skills/agent-memory-engineering/SKILL.md`: aprendizagem supervisionada de correções, deduplicação, escopo e promoção auditável.
3. Sem novas skills ou stacks: owners existentes absorvem a metodologia portável; índice mantém rotas válidas.

## Segurança e portabilidade
- **CAUTION** para qualquer instalação externa: não foram auditados executáveis, scripts transitivos, todas as dependências ou binários. Não houve scanner nem runtime test.
- `terminal-browser` oferece instalador remoto `curl | bash`, rede/SSH, telemetria e captura de interação: requer análise completa do installer, bins, sessões e privacidade antes de uso local.
- `claude-reflect` pode inspecionar prompts/histórico e alterar arquivos de instrução persistentes: retenção, privacidade, escopo e aprovação precisam de gate.
- `cache-tax` pode consumir tokens e confunde-se facilmente com garantia de economia; sem compatibilidade ChatGPT.
- Mods de UI/progresso/filetree/replay usam APIs de hooks/panes e versões de Claude Code; não são plugins do ChatGPT.
- `blast-radius` mede impacto por comandos de leitura; sua lógica não substitui autorização, sandbox ou revisão dos scripts realmente executados.
- Nenhuma dependência foi executada, instalada ou habilitada. A avaliação é metodológica/estática de README, não certificação de segurança de supply chain.

## Critério de verificação
- Novos trechos de documentação publicados devem ser relidos do GitHub.
- Sem alteração de descrições das skills e sem novo recurso, o `ARSENAL INDEX.md` não precisa mudar.
