# Pesquisa de ecossistema — design, criação, produtividade e alternativas open-source

Data: 2026-09-30

## Objetivo

Pesquisar 30 repositórios inovadores em design, criação, produtividade, automação, knowledge work e alternativas abertas/self-hosted a grandes sistemas pagos.

Fluxo aplicado: `arsenal-autopilot`.

Nenhum installer, Docker image, script, CLI, MCP, plugin ou aplicação externa foi executado.

## 30 repositórios pesquisados

### Design, canvas e criação visual
1. `penpot/penpot` — plataforma open-source de design colaborativo; SVG/CSS/HTML/JSON, design tokens, components/variants, flex/grid, API/plugins.
2. `open-pencil/open-pencil` — editor open-source compatível com .fig/.pen; árvore estruturada, queries, lint, token extraction, design-to-code e import HTML/CSS.
3. `excalidraw/excalidraw` — whiteboard infinito, formato aberto JSON, colaboração, local-first e E2EE.
4. `tldraw/tldraw` — canvas/whiteboard SDK e editor extensível.
5. `AFFiNE/affine` — workspace/canvas/docs orientado a conhecimento.
6. `kdenlive/kdenlive` — editor de vídeo open-source.
7. `mltframework/shotcut` — editor de vídeo gratuito/open-source/cross-platform.

### Knowledge work e produtividade
8. `AppFlowy-IO/AppFlowy` — alternativa open-source ao Notion, workspace com dados sob controle do usuário.
9. `docmost/docmost` — wiki/documentação colaborativa, histórico, permissões e diagramas.
10. `logseq/logseq` — knowledge management privacy-first, graphs e colaboração.
11. `silverbulletmd/silverbullet` — knowledge database programável: Markdown + links + objetos + queries + scripting.
12. `usememos/memos` — captura rápida, timeline Markdown, organização leve, self-host e zero telemetry.
13. `makeplane/plane` — project management open-source, cycles/modules/views/pages/analytics.
14. `twentyhq/twenty` — CRM open-source extensível como código.
15. `actualbudget/actual` — personal finance local-first, free/open-source e sync.
16. `maybe-finance/maybe` — personal finance self-hostable; repositório atualmente não mantido.
17. `immich-app/immich` — photo/video management self-hosted com busca, backup e compartilhamento.

### Database, no-code e internal tools
18. `nocodb/nocodb` — database/no-code sobre dados relacionais.
19. `baserow/baserow` — alternativa aberta ao Airtable; databases, apps, automations e dashboards.
20. `apitable/apitable` — spreadsheet/database colaborativo API-first.
21. `ToolJet/ToolJet` — internal tools builder com componentes, data sources, self-host e extensibilidade.
22. `appsmithorg/appsmith` — low-code open-source para dashboards/admin/internal apps.
23. `Budibase/budibase` — low-code/internal apps e automação.

### Workflow automation e agentes
24. `activepieces/activepieces` — automação visual, loops, branches, retries, versioning e integrações.
25. `automatisch/automatisch` — alternativa self-hosted ao Zapier com foco em controle de dados.
26. `bytechefhq/bytechef` — workflows + agentes como passos duráveis; human pause/resume e structured output.
27. `n8n-io/n8n` — visual workflow automation + code + agents + approvals/observability; fair-code/source-available.
28. `FlotHQ/flot` — alternativa de workflow automation.
29. `healer-125/activepieces` — fork/variante encontrada na busca; sem novidade canônica sobre a fonte original.
30. `pypestream/pro-studio` — builder/no-code encontrado na busca; usado somente como triagem de ecossistema.

## Principais capabilities encontradas

### 1. Design como estrutura, não só pixels
Penpot e OpenPencil reforçam que design pode ser inspecionado como:
- node tree;
- parent/child relations;
- components/variants;
- layout constraints;
- design tokens;
- semantic structure;
- machine-readable exports.

Isso é incremental para `design-system-extraction`: quando estrutura real existir, ela deve complementar screenshots e computed styles.

### 2. Interoperabilidade design ↔ code
Formatos abertos e exportáveis reduzem perda na passagem design→implementação:
- SVG;
- CSS;
- HTML;
- JSON;
- token formats;
- component-oriented code.

A metodologia não exige uma ferramenta específica. O princípio adotado é preferir representação estruturada e portátil quando disponível.

### 3. Design lint como diagnóstico
OpenPencil demonstra lint sobre naming/layout/accessibility/structure. O Arsenal absorve o princípio, não a CLI:
- lint ajuda a encontrar inconsistência;
- lint não prova qualidade visual;
- regras objetivas podem virar checks;
- julgamento estético continua separado.

### 4. Canvas como spatial workspace
Excalidraw/tldraw/AFFiNE mostram o valor de:
- infinite canvas;
- spatial grouping;
- zoomable context;
- local visual neighborhoods;
- open/serializable scene state.

O Arsenal já cobre o método em `visual-explanation-sketch` e `interactive-system-diagram`; não foi criada skill duplicada.

### 5. Local-first / ownership
AppFlowy, Actual, Excalidraw e outros reforçam:
- trabalho local/offline quando possível;
- sincronização como camada separada;
- formatos exportáveis;
- propriedade de dados;
- redução de lock-in.

É um princípio de arquitetura/produto, não uma nova capability operacional por si só.

### 6. Progressive capture
Memos é interessante pela redução de friction:
`capture first → organize lightly → retrieve later`.
Isso é referência útil para sistemas de conhecimento, mas não exige novo owner.

### 7. Programmable knowledge base
SilverBullet combina documento, objetos, queries e scripting. O padrão relevante é:
`human-readable canonical content + structured query layer + optional programmable views`.
Isso converge com `session-learn`, `kb-retriever` e memória/index derivado já existente.

### 8. Apps sobre dados existentes
ToolJet/Appsmith/Budibase/Baserow/NocoDB convergem em:
`data source → governed components → queries/actions → interface → permissions/deployment`.
Útil como referência técnica para protótipos/internal tools, mas depende de runtime externo.

### 9. Workflow visual + code escape hatch
Activepieces, n8n, ByteChef e Automatisch reforçam:
- workflow explícito;
- branches/loops;
- retries;
- versioning;
- human approval;
- custom code quando necessário;
- self-host/data control.

O Arsenal já possui `loop-engineering`, `graph-engineering`, `multi-agent-orchestration` e automations reais. Nenhuma nova skill foi necessária.

### 10. Durable agent as workflow step
ByteChef traz uma distinção útil: agente pode ser apenas um passo dentro de um workflow durável, com pause/resume, em vez de ser o orquestrador de tudo.
Esse princípio já é compatível com `graph-engineering` e `loop-engineering`; manter como referência externa por depender de runtime.

## Mapa de alternativas úteis

| Categoria | Sistema pago conhecido | Alternativas pesquisadas |
| --- | --- | --- |
| Product design | Figma | Penpot, OpenPencil |
| Whiteboard | Miro | Excalidraw, tldraw |
| Workspace/wiki | Notion | AppFlowy, AFFiNE, Docmost, Logseq, SilverBullet |
| Airtable/database | Airtable | Baserow, NocoDB, APITable |
| Internal tools | Retool | ToolJet, Appsmith, Budibase |
| Automation | Zapier/Make | Activepieces, Automatisch, ByteChef, n8n |
| Project management | Linear/Jira/Asana | Plane |
| CRM | Salesforce/HubSpot | Twenty |
| Photo cloud | Google Photos/iCloud Photos | Immich |
| Personal finance | YNAB/Monarch-style category | Actual Budget, Maybe |
| Video editing | Premiere-style category | Kdenlive, Shotcut |

"Alternativa" aqui significa sobreposição funcional relevante, não equivalência completa de features, suporte, segurança, maturidade ou UX.

## Classificação

- **Penpot** — A/B/D — UPDATE_EXISTING — `design-system-extraction`, referência para `design-system-governance`.
- **OpenPencil** — A/B/D — UPDATE_EXISTING — inspeção estrutural, lint, token extraction e interoperability.
- **Excalidraw** — A/B/D — ALREADY_ABSORBED — `visual-explanation-sketch`.
- **tldraw** — B/D — KEEP_EXTERNAL_REFERENCE.
- **AFFiNE** — B/D — KEEP_EXTERNAL_REFERENCE.
- **AppFlowy** — B/D — KEEP_EXTERNAL_REFERENCE.
- **Docmost** — B/D — KEEP_EXTERNAL_REFERENCE.
- **Logseq** — B/D — KEEP_EXTERNAL_REFERENCE.
- **SilverBullet** — A/B/D — KEEP_EXTERNAL_REFERENCE; programação de knowledge base.
- **Memos** — B/D — ABSORB_AS_REFERENCE; low-friction capture.
- **Plane** — B/D — KEEP_EXTERNAL_REFERENCE.
- **Twenty** — A/B/D — KEEP_EXTERNAL_REFERENCE; programmable CRM.
- **Baserow/NocoDB/APITable** — A/B/D — KEEP_EXTERNAL_REFERENCE; no-code data/app patterns.
- **ToolJet/Appsmith/Budibase** — A/B/D — KEEP_EXTERNAL_REFERENCE; internal-tool runtimes.
- **Activepieces/Automatisch/ByteChef/n8n** — A/B/D — KEEP_EXTERNAL_REFERENCE; workflow runtimes overlap metodologicamente com existing owners.
- **Actual Budget** — B/D — KEEP_EXTERNAL_REFERENCE; local-first product reference.
- **Maybe** — D — REFERENCE_WITH_STATUS_WARNING; upstream not actively maintained.
- **Immich** — A/B/D — KEEP_EXTERNAL_REFERENCE; self-hosted media product reference.
- **Kdenlive/Shotcut** — D — KEEP_EXTERNAL_REFERENCE; mature creative applications, not ChatGPT-native capabilities.
- **Flot/forks/long-tail search hits** — C/D — discovery only.

## Mudança canônica

### UPDATE — `design-system-extraction`

Adicionados princípios:
- inspecionar node tree e relações estruturais quando o formato permitir;
- extrair components/variants e constraints/layout de estrutura legível por máquina;
- preferir formatos interoperáveis e legíveis para design↔code;
- usar lint de naming/layout/contraste/estrutura como diagnóstico, não prova de qualidade;
- não presumir Penpot/OpenPencil/Figma/MCP/CLI disponíveis sem conexão real.

Nenhuma nova skill ou stack foi criada.

## Segurança, licença e portabilidade

- Não executamos comandos de instalação das fontes.
- Não executamos Docker/curl/npm/CLI.
- Não ativamos MCPs ou plugins.
- Self-hostable não significa automaticamente seguro ou simples de operar.
- Open-source, open-core, fair-code e source-available não são sinônimos; a licença precisa ser conferida para o uso concreto.
- Forks e projetos abandonados foram diferenciados de upstreams canônicos.
- Claims de compliance dos READMEs não foram tratados como auditoria independente.
- Alternativa gratuita não significa equivalência total ao produto comercial.

## Conclusão

O maior valor deste lote é duplo:

1. **Radar operacional de alternativas abertas** para design, produtividade, dados, automação e criação.
2. **Melhoria metodológica do Arsenal** para tratar artefatos de design como estruturas interrogáveis e portáveis, não apenas imagens.

A pesquisa não justificou criar uma "skill de ferramentas gratuitas". A escolha de software depende de necessidade atual, maturidade, licença, integração, hosting e risco; isso deve permanecer uma decisão contextual.
