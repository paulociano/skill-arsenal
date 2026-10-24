# Avaliação: marmottajr (6 repositórios)

Data: 2026-10-24. Fonte: https://github.com/marmottajr?tab=repositories . Avaliação guiada pelo `ARSENAL INDEX.md` e `stacks/arsenal-autopilot/STACK.md`. Análise estática de READMEs/contratos publicados; sem execução de scripts, testes, instalações ou auditoria exaustiva de código.

| Fonte | Capacidade observada | Classe | Decisão | Owner / motivo |
| --- | --- | --- | --- | --- |
| [dontpanic](https://github.com/marmottajr/dontpanic) | Boilerplate SaaS NestJS/Next, Postgres RLS, RBAC, auth/2FA, filas, teste e observabilidade | A/D | ABSORB_METHOD_ONLY + KEEP_EXTERNAL_REFERENCE | `developer-platform-engineering`: os padrões de baseline de segurança e projeto gerado compõem golden paths existentes; dependências e código externo não foram importados. |
| [dontpanic-create](https://github.com/marmottajr/dontpanic-create) | CLI configurável que remove features, renomeia, gera segredos e valida presets por matriz de conformidade | A/D | UPDATE_EXISTING | `developer-platform-engineering`: acrescentada seção de conformidade de geradores parametrizados, sem adotar CLI. |
| [habblaud](https://github.com/marmottajr/habblaud) | Visualização pixel-art local da atividade e aprovações de sessões Claude Code/Codex | D | KEEP_EXTERNAL_REFERENCE | Observabilidade e interação dependem de runtime/mod de terceiros; `software-observability-engineering` / `coding-agent-engineering` cobrem objetivos portáveis, sem necessidade comprovada de nova skill. |
| [path-adder](https://github.com/marmottajr/path-adder) | Inserção massiva de comentário com caminho em JS/TS | D | REJECT | Reescrita indiscriminada de arquivos, ruído em diffs e pouca utilidade transversal; ferramenta pontual, não uma competência. |
| [ExemploPOSTCallback](https://github.com/marmottajr/ExemploPOSTCallback) | Exemplo de callback HTTP POST em PHP para Monetizze | B/D | KEEP_EXTERNAL_REFERENCE | Exemplo específico de fornecedor; `ai-workflow-automation-engineering` já cobre webhooks, contracts, validação e idempotência. Não assumir autenticação ou assinatura sem auditar código. |
| [marmottajr](https://github.com/marmottajr/marmottajr) | Perfil público/README de portfólio | C | REJECT | Não apresenta processo reutilizável como skill. |

## Ganho aplicado

Arquivo: `skills/developer-platform-engineering/SKILL.md`.

Adicionado gate de conformidade: template versionado e fonte limpa, feature manifest e remoção consistente, detecção de nomes residuais, rotação de segredos, matriz de build/test de projetos **gerados** por preset, validação e2e seletiva de isolamento RLS, migrations e checks de export estático. Trigger: gerador de projetos com presets e feature pruning. Near-miss: clone único sem parametrização e sem necessidade de matriz, para o qual bastam verificações proporcionais.

## Segurança e portabilidade

Não executar instaladores, mods, hooks ou scripts publicados por terceiros para importar metodologia. Habblaud requer integração com sessões e arquivos locais de outro agente; não inferir disponibilidade no ChatGPT. DontPanic depende de Node, banco, containers, migrations, segredos e configuração de deploy; comportamento de segurança documentado não substitui teste independente. O gerador deve emitir segredos aleatórios, isolar tenants e exigir validação real. Nenhum runtime externo foi instalado, nenhum código copiado.

## Verificação

O owner foi alterado no GitHub no commit `61abe4706d804aff33500d69eecc73e3cebb311d`. Nenhuma nova skill/stack criada; o índice permanece adequado, pois o owner já estava listado. A avaliação se limita ao conteúdo inspecionado; não certifica funcionamento nem segurança de execução dos repositórios de origem.
