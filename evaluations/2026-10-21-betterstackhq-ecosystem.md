# BetterStackHQ, avaliação de ecossistema (2026-10-21)

## Fontes e escopo
- Organização: https://github.com/orgs/BetterStackHQ/repositories
- Busca de repositórios GitHub retornou 33 projetos visíveis na organização nesta consulta; não representa inventário imutável nem garante inspeção de cada projeto.
- Fontes aprofundadas: https://github.com/BetterStackHQ/codex-plugin (README e skills `investigate-incident`, `logs-query`, `health-check`, `uptime-monitors`); https://github.com/BetterStackHQ/claude-plugin; https://github.com/BetterStackHQ/cursor-plugin; https://github.com/BetterStackHQ/collector; https://github.com/BetterStackHQ/opentelemetry-demo; https://github.com/BetterStackHQ/beyla; https://github.com/BetterStackHQ/clickhouse-analyzer.
- Stack aplicada: `arsenal-autopilot`, com segurança via `skill-security-review`.
- Base canônica consultada: `ARSENAL INDEX.md`, `software-observability-engineering`, `llm-observability-evaluation`. Sem executar scripts ou instalar binários.

## Capabilities e decisões

| Fonte/capacidade | Classificação | Owner/decisão |
| --- | --- | --- |
| Plugin Better Stack para Codex, Claude, Cursor (MCP, investigação, queries, charts, alertas, monitores) | D/B | UPDATE_EXISTING em `skills/software-observability-engineering/SKILL.md` para workflow portátil; não copiar tools/SQL vendor-specific. Plugins permanecem referência técnica de operação Better Stack. |
| Better Stack Collector (coleta e auto-instrumentação eBPF em Docker/Kubernetes) | D/B | UPDATE_EXISTING na mesma skill com preflight de eBPF, recursos, privacidade, custo e validação; não instalar runtime. |
| OpenTelemetry Demo (fork de Astronomy Shop, exemplos e testes) | D | KEEP_EXTERNAL_REFERENCE; serve de laboratório, não é método separado. README inclui script remoto `curl | bash`, não executado. |
| Beyla (fork, com desenvolvimento dirigido a OpenTelemetry eBPF Instrumentation) | D | KEEP_EXTERNAL_REFERENCE; upstream deve ser preferido para acompanhamento técnico. |
| clickhouse-analyzer (parser/LSP de SQL ClickHouse, autodeclarado experimental) | D | KEEP_EXTERNAL_REFERENCE; instalação Rust/WASM/LSP não agrega skill portátil ao uso geral de observabilidade. |
| Helm charts, terraform providers, SDKs e cloud integrations | D | KEEP_EXTERNAL_REFERENCE; dependem de provider/infra e devem ser selecionados apenas em projetos concretos, sem importação em massa. |
| Repositórios auxiliares/forks/libs genéricas | D/C conforme finalidade | Não promovidos ao Arsenal nesta triagem; exigir avaliação pontual antes de adoção. |

## Segurança e portabilidade
Veredito documental: CAUTION para runtimes/MCP e coletores por credenciais, rede, shell, Kubernetes, Docker, eBPF, efeitos externos de incidentes/monitores; nenhum achado malicioso confirmado nesta leitura parcial, que não é auditoria de código-fonte ou dependências. OAuth/token e permissões devem ser avaliados no ambiente real. Criar monitor pode gerar verificações/alertas; ack, alteração, escalonamento, criação de dashboard e publicação exigem autorização efetiva. Não confundir leitura do README com disponibilidade de ferramentas na sessão ChatGPT.

## Resultado materializado
- Atualizado `skills/software-observability-engineering/SKILL.md` com playbook de incidente e validação de auto-instrumentação/eBPF, commit `89f1e579e42ba7c09df9a96b063ea9e7a0bd12b1`.
- Sem novas skills, stacks ou mudanças de descriptions; índice inalterado justificadamente.
- Registrar este arquivo na branch canônica e reler os arquivos publicados. A cobertura foi amostral por capability, não uma auditoria profunda dos 33 repositórios.
