# Treze repositórios — agentes de computador, navegador, automação, frameworks e integrações (2026-11-09)

## Fontes
- https://github.com/simular-ai/Agent-S
- https://github.com/automatisch/automatisch
- https://github.com/camel-ai/owl
- https://github.com/Skyvern-AI/skyvern
- https://github.com/letta-ai/letta (código ativo: https://github.com/letta-ai/letta-code)
- https://github.com/activepieces/activepieces
- https://github.com/browserbase/stagehand
- https://github.com/huggingface/smolagents
- https://github.com/ComposioHQ/composio
- https://github.com/bytedance/UI-TARS-desktop
- https://github.com/agno-agi/agno
- https://github.com/huginn/huginn
- https://github.com/crewAIInc/crewAI
- Stack de avaliação: stacks/evaluate-and-import-skill/STACK.md

## Contexto de decisão
Avaliados um a um em conversa no Claude (claude.ai), com a pergunta "avaliar para o arsenal ou instalar". O ambiente do usuário já tem: computer use nativo do Claude, Claude in Chrome, conector Zapier, tarefas agendadas, memória persistente com Projects, subagentes e as skills `multi-agent-orchestration` e `signal-intelligence-digest`. Nenhum dos treze é Agent Skill; todos são runtimes, frameworks ou serviços.

Nove já tinham passagem anterior no Arsenal (2026-09-23, 2026-09-30, 2026-10-02, 2026-10-06). Esta é uma reavaliação com o estado atual dos repositórios mais quatro fontes novas (OWL, Composio, Huginn e o arquivamento do UI-TARS-desktop).

## Decisões

| Repositório | Licença | Classe | Decisão | Owner / motivo |
|---|---|---|---|---|
| simular-ai/Agent-S | Apache-2.0 | D | NÃO ADOTAR (referência) | `computer-use-agent-engineering` já consolidado. Exige grounding model separado (UI-TARS-1.5 em endpoint pago) + API de modelo principal; executa código Python para controlar a máquina. Redundante com computer use nativo |
| automatisch/automatisch | AGPL-3.0 + EE | D | SUPERADO por Activepieces | Self-hosted, sem MCP, menos integrações. Se surgir exigência de automação self-hosted, comparar Activepieces e n8n |
| camel-ai/owl | Apache-2.0 | D | NÃO ADOTAR (referência) | Framework multiagente sobre CAMEL; recomenda modelos OpenAI; última novidade no README em 2025-09. Padrão "workforce" já coberto por `multi-agent-orchestration` |
| Skyvern-AI/skyvern | AGPL-3.0 | B/D | WATCHLIST FORTE | `computer-use-agent-engineering`. Melhor opção para rotina web recorrente sem código (formulários, login com 2FA, download, workflows). Suporta Claude e MCP; tem skill própria em `skills/skyvern` (não inspecionada). Telemetria ligada por padrão (`SKYVERN_TELEMETRY=false`). Gatilho: rotina recorrente em vários portais (ex.: extratos de previdência/seguradoras) |
| letta-ai/letta | Apache-2.0 | B/D | ABSORB_METHOD_ONLY | Repositório virou ponteiro para `letta-code`; API V1 aposentada (branch `archive`). Conceito de blocos de memória nomeados absorvido em `agent-memory-engineering` |
| activepieces/activepieces | MIT (CE) + comercial (EE) | A/D | WATCHLIST | `ai-workflow-automation-engineering`. 280+ pieces expostas como MCP, human-in-the-loop, fluxos versionados. Supera Automatisch. Gatilho: exigência de LGPD/self-hosted ou integração com sistema interno |
| browserbase/stagehand | MIT | B/D | WATCHLIST (dev) | `runtime-ui-verification` e `computer-use-agent-engineering` já absorveram observe/act/extract e isolamento de credenciais (2026-09-23). v4 em TS/Python/Go; MCP hospedado depende da Browserbase (paga). Gatilho: projeto de código que precise de scraping ou teste E2E web |
| huggingface/smolagents | Apache-2.0 | B/D | ABSORB_METHOD_ONLY | Padrão "ações em código" absorvido em `ai-workflow-automation-engineering`. Biblioteca não adotada; exige sandbox (E2B/Modal/Docker) para execução segura |
| ComposioHQ/composio | MIT (SDK) + serviço em nuvem obrigatório | B/D | WATCHLIST FORTE | `ai-workflow-automation-engineering`. Concorrente direto do conector Zapier: 1000+ toolkits, OAuth gerenciado, MCP hospedado por sessão, adaptadores para Anthropic e Claude Agent SDK. Tokens ficam na nuvem do Composio; sem self-host. Não encontrado no diretório de conectores do claude.ai (conexão manual por URL MCP). Gatilho: app não coberto pelo Zapier/conectores nativos, ou produto próprio com autenticação por usuário |
| bytedance/UI-TARS-desktop | Apache-2.0 | D | DESCARTADO | **Arquivado em 2026-11-09** (read-only). Redundante com computer use nativo e Claude in Chrome; operadores remotos rodam na infraestrutura da ByteDance. Modelo UI-TARS (repo separado `bytedance/UI-TARS`) não afetado |
| agno-agi/agno | Apache-2.0 | A/D | WATCHLIST (produto) | Plataforma para rodar agentes como serviço (SDK + AgentOS + Control Plane); aceita Claude Agent SDK, expõe agentes via API e MCP, aprovação humana, agendamento, RBAC, self-host na própria nuvem. Telemetria ligada (`AGNO_TELEMETRY=false`). Gatilho: agente para a equipe (ex.: bot de gestão comercial no Slack) com controle de acesso e dados próprios |
| huginn/huginn | MIT | D | NÃO ADOTAR (método absorvido) | Monitoramento e digests já cobertos por tarefas agendadas + `signal-intelligence-digest`; sem MCP; mantido por uma pessoa; exige servidor Rails + worker + banco. Padrão sentinela absorvido em `ai-workflow-automation-engineering` |
| crewAIInc/crewAI | MIT | B/D | ABSORB_METHOD_ONLY | Orquestração coberta por `multi-agent-orchestration`; padrão OpenAI; telemetria ligada (`OTEL_SDK_DISABLED=true`). Se precisar de multiagente em produção, preferir Agno. Contrato `expected_output`/`context` por tarefa absorvido nas regras de stacks |

## Mapa de escolha resultante

| Necessidade | Escolha |
|---|---|
| Tarefa pontual no computador ou navegador | Computer use nativo / Claude in Chrome |
| Rotina web recorrente sem código, com 2FA | Skyvern (watchlist) |
| Automação web dentro de projeto de código | Stagehand (watchlist) |
| Integração entre apps | Zapier (ativo); Composio como plano B |
| Automação self-hosted por LGPD | Activepieces (comparar com n8n) |
| Agente servido à equipe/produto | Agno |
| Framework para construir agente embutido | Claude Agent SDK; smolagents só com modelos abertos |

## Valor incremental implementado
- `skills/computer-use-agent-engineering/SKILL.md`: seção "Escolha de runtime e higiene de fontes" (nativo primeiro, roteamento Skyvern × Stagehand × nativo, manutenção, onde a sessão roda, telemetria, credenciais fora do modelo) e nota de reavaliação (UI-TARS-desktop arquivado).
- `skills/agent-memory-engineering/SKILL.md`: seção "Blocos de memória nomeados" e nota de que o código ativo do Letta está em letta-code.
- `skills/ai-workflow-automation-engineering/SKILL.md`: subseções "Ações em código" (smolagents) e "Sentinela de mudança" (Huginn); parágrafo "Gateways de integração gerenciados" (Composio) no gate de wrappers MCP.
- `AGENTS.md`: regra de stacks passa a pedir entrega esperada e dependências por etapa (CrewAI).
- `stacks/research-to-presentation/STACK.md`: primeira stack com o contrato de entregas por etapa.

## Segurança e portabilidade
Nenhum instalador, container ou script foi executado. Riscos observados: execução de código arbitrário (Agent S, smolagents, OWL); telemetria ligada por padrão (Skyvern, Agno, CrewAI); tokens OAuth em nuvem de terceiro (Composio); operadores remotos em infraestrutura do fornecedor (UI-TARS-desktop); repositório arquivado (UI-TARS-desktop); licenças AGPL (Automatisch, Skyvern) que restringem incorporação de código.

## Aceite futuro
- Skyvern, Stagehand, Activepieces, Composio e Agno: promover para avaliação completa quando o gatilho listado ocorrer; ler a skill própria do projeto (Skyvern, Composio) e passar por `skill-security-review` antes de qualquer adoção.
- Aplicar o contrato de entregas por etapa às demais stacks à medida que forem editadas.

## Limites da avaliação
Pesquisa documental nos READMEs públicos dos repositórios na data. As skills internas de Skyvern (`skills/skyvern`) e Composio (`skills/composio`) não foram abertas. Sem execução de código nem teste de runtime.

## Arquivos atualizados
- evaluations/2026-11-09-thirteen-agent-automation-repositories.md (novo)
- skills/computer-use-agent-engineering/SKILL.md
- skills/agent-memory-engineering/SKILL.md
- skills/ai-workflow-automation-engineering/SKILL.md
- AGENTS.md
- stacks/research-to-presentation/STACK.md
