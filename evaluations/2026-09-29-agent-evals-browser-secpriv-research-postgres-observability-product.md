# Avaliação em lote — evals, browser reliability, security/privacy, research, PostgreSQL, observability e product

Data: 2026-09-29

## Escopo
Shortlist priorizada após discovery de 30 fontes. Fluxo: `arsenal-autopilot`.

Nenhum installer, benchmark runtime, browser extension, scanner, MCP externo ou CLI das fontes foi executado.

## Fontes resolvidas e decisões

| Fonte | Classe | Decisão | Owner |
|---|---|---|---|
| frontier-harness-eval/eval | A/B/D | UPDATE_EXISTING | `empirical-prompt-tuning`: controles de comparabilidade para harness eval |
| uiuing/browser-agent | A/B/D | UPDATE_EXISTING | `runtime-ui-verification`: postconditions expected/actual/evidence e replay verificado |
| facebookresearch/secpriv-skill | A/B | CREATE_NEW | `secure-code-privacy-review` |
| ngtiendong/Academic-Research-Agent-Skill | A/B/D | ABSORB_METHOD_ONLY | research-question-design + academic-paper-orchestration já cobrem reality/novelty/feasibility/claim gates; sem novo owner |
| Clear-Capabilities/agentic-security · privacy-data-flow | A/B/D | CREATE_NEW / MERGE | combinado com SecPriv em `secure-code-privacy-review` |
| timescale/pg-aiguide · postgres-database-migration | A/B/D | CREATE_NEW | `postgres-migration-safety` |
| datadog-labs/agent-skills · agent-observability-eval-pipeline | A/B/D | KEEP_EXTERNAL_REFERENCE | `llm-observability-evaluation` já cobre traces→datasets→evals→experiments→feedback |
| rajann44/pm-skills | A/B | CREATE_STACK | `product-management-cycle`, compondo owners existentes |

## Fontes da shortlist não resolvidas no GitHub canônico
- tmusser/agent-workflow-bench
- adityasankranthi/AI-research-agent
- VisualOps-AI/agent-eval-harness
- skillmds/skillmd

A busca GitHub disponível não confirmou os repositórios/path canônicos. Não foram classificados nem substituídos silenciosamente por resultados parecidos. Precisam de URL válida/fonte canônica antes de avaliação.

## Valor incremental

### secure-code-privacy-review
Novo owner justificado porque `code-review` é generalista, `skill-security-review` avalia extensões externas e `llm-red-team-evaluation` cobre GenAI adversarial. Faltava revisão de **código de aplicação** com detector→validator, trust boundaries e privacy data-flow.

### postgres-migration-safety
Novo owner justificado porque análise operacional de DDL depende de versão, lock, table rewrite/scan, rollout compatibility, backfill e rollback. Isso não cabe adequadamente em debugging genérico ou library grounding.

### product-management-cycle
Stack, não skill: o Arsenal já possui owners para discovery, JTBD, specs, priorização, métricas, experimentos e decisões. O ganho está em manter essas fases coerentes ao longo de uma decisão de produto e preservar context/evidence gates.

## Segurança e portabilidade
- FrontierHarness depende de Runta, Harbor/Pier, secrets, runtimes e custos externos; somente metodologia de comparabilidade foi absorvida.
- Browser Agent é extensão Chrome com execução de página e permissões; somente postcondition/replay methodology foi absorvida.
- SecPriv é metodologia portátil; não importamos taxonomia como scanner automático nem threshold de confiança como prova.
- agentic-security possui scanners/MCP/comandos e licença PolyForm Internal Use; somente metodologia abstrata de data flow foi incorporada, sem copiar runtime/assets.
- pg-aiguide depende de MCP/CLI e conhecimento versionado; a nova skill exige grounding na versão/documentação em vez de congelar a tabela externa como verdade eterna.
- Datadog skill depende de Datadog MCP/pup e credenciais; owner existente permanece vendor-neutral.
- pm-skills possui workspace conventions e thresholds rígidos; stack adaptada remove números universais e arquivos obrigatórios.

## Mudanças publicadas
- CREATE `skills/secure-code-privacy-review/SKILL.md`
- CREATE `skills/postgres-migration-safety/SKILL.md`
- CREATE `stacks/product-management-cycle/STACK.md`
- UPDATE `skills/runtime-ui-verification/SKILL.md`
- UPDATE `skills/empirical-prompt-tuning/SKILL.md`
- UPDATE `ARSENAL INDEX.md`

## Limites
Benchmarks e claims das fontes não foram reproduzidos. Não foi feita análise jurídica de compliance. As quatro fontes não resolvidas permanecem pendentes, não rejeitadas.
