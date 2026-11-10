# Avaliação: OpenMausBot, Scrapling, NVIDIA Auto Ontology e T3 Code

- Data: 2026-11-10
- Fluxo: `evaluate-and-import-skill` + `skill-security-review` (inspeção estática; nada instalado ou executado)

| Fonte | Classe | Decisão | Owner atualizado |
|---|---|---|---|
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | D (com método B) | ABSORB_METHOD_ONLY | `skills/behavior-contract-validation/SKILL.md` |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) v0.5.1 | D | UPDATE_EXISTING (reavaliação) | `skills/web-extraction-pipeline/SKILL.md` |
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | D (com método A) | ABSORB_METHOD_ONLY | `skills/product-metrics-diagnostics/SKILL.md` |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | D | KEEP_EXTERNAL_REFERENCE | nenhum |

## 1. OpenMausBot

- Evidência: README, `package.json`, LICENSE (Apache-2.0), `skills/` (create-verification-skill, data-dashboards, phone-harness, social-posts).
- Função real: app desktop Electron + servidor/relay + Cloudflare que roda vários bots (Claude/Codex locais) como contatos num chat, cada um com "computador em nuvem" e apps conectados. Alternativa aberta ao Grok Bot / Meta Muse.
- Delta: `create-verification-skill` define uma receita de verificação por projeto (Launch, Doctor, Drive, Evidence, Cleanup, Feature map, Maintenance), escrita só depois de provar um fluxo real. Incorporado em `behavior-contract-validation`. As outras três skills dependem de ferramentas internas do app (`skill_manage`, phone relay) ou sobrepõem `dashboard-design`/`content-production`.
- Segurança: **CAUTION**. Agentes com controle de computador remoto, relay de celular, conectores de apps, deploy em Cloudflare e versão enterprise; CLA para contribuições. Não auditado.
- Instalar no Claude: não é skill; é um app concorrente do próprio Claude desktop. Não recomendado.

## 2. Scrapling (reavaliação)

- Evidência: README, `pyproject.toml` (0.5.1, commit de 2026-11-09), `agent-skill/Scrapling-Skill/SKILL.md`, LICENSE (BSD-3).
- Já adaptado antes em `web-extraction-pipeline`. Novo: skill oficial do autor com flag `--ai-targeted`, que extrai só o conteúdo principal e filtra elementos ocultos antes de entregar ao modelo, como defesa contra prompt injection.
- Incorporado: regra de reduzir HTML ao conteúdo principal e remover elementos ocultos antes de passar ao modelo; regra explícita de que bypass anti-bot (Turnstile, stealth, proxy) exige autorização e não é default.
- Segurança: **CAUTION**. Ferramentas de contorno de anti-bot podem violar termos de uso; instala navegadores via `scrapling install`.
- Instalar no Claude: a skill oficial é instalável no Claude Code (precisa Python 3.10+ e pip). Útil só se você raspar sites com frequência; para leitura pontual, WebFetch/Firecrawl já conectados bastam.

## 3. NVIDIA Auto Ontology

- Evidência: README, `skills/` (setup, query, management), `skills/nvidia-ontology-query/references/query-validation.md`, `mcp/`.
- Função real: plataforma (Next.js + FastAPI + Postgres/pgvector + NVIDIA NIM, Helm/Docker) que gera ontologia/camada semântica a partir de metadados corporativos e responde perguntas em linguagem natural via SQL, exposta por MCP/CLI/API.
- Delta: protocolo de validação de resposta text-to-SQL (pergunta material, inspeção da consulta, fanout de join, checagem independente das linhas, truncamento, estados de evidência, recibo). Nenhum owner do Arsenal tinha isso; incorporado em `product-metrics-diagnostics`, útil também para planilhas e CRM.
- Não incorporado: a plataforma, NIM, MCP, RBAC, ingestão. `knowledge-graph-engineering` já cobre a modelagem de ontologia.
- Segurança: **CAUTION**. Conecta a bancos corporativos com credenciais (Vault opcional), envia dados a endpoints NIM hospedados por padrão (`integrate.api.nvidia.com`) com API key. Não aceita contribuições externas.
- Instalar no Claude: só faz sentido com um deployment rodando e bancos para consultar. Não é o caso hoje.

## 4. T3 Code

- Evidência: README, LICENSE (MIT), listagem de `apps/` e `packages/`.
- Função real: "control surface" para agentes de código (Claude Code, Codex, Cursor, Grok, OpenCode, Antigravity) com apps desktop, web e celular, controle remoto via SSH/Tailscale e integração com GitHub/GitLab/Bitbucket etc.
- Delta: nenhuma metodologia de skill; é produto/runtime. Manter como referência para `coding-agent-engineering` e `software-factory-operations` se um dia for preciso comandar agentes pelo celular.
- Segurança: **CAUTION**. Instalação por `curl | sh` / `irm | iex`; servidor local com acesso às sessões autenticadas dos CLIs; acesso remoto.
- Instalar no Claude: não é skill. É alternativa ao Claude Code desktop/remote que você já usa.

## Limites da validação
Leitura de README, manifestos, LICENSE e dos SKILL.md citados. Código-fonte, dependências e comportamento em runtime não auditados.
