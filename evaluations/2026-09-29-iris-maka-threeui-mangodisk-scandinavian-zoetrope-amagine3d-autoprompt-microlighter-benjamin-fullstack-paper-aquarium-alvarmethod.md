# Avaliação em lote — agent runtimes, visual verification, 3D, design, teaching e efficiency

Data: 2026-09-29

## Fontes
- brijr/iris
- apache/maka
- MengTo/threeui
- harry0703/MangoDisk
- ericzakariasson/scandinavian-design
- furkankly/zoetrope
- amagine-ai/Amagine3D
- Spielewoy/autoprompt-skill
- davatron5000/microlighter
- JetBrains/benjamin-plus-skill
- jaredrhod/fullstack-agent
- MrMoT9I/paper-aquarium
- vasanthsreeram/Alvarmethod

Fluxo: `arsenal-autopilot`. Nenhum installer, binário, firmware, browser runtime ou script das fontes foi executado.

## Decisões

| Fonte | Classe | Decisão | Owner / razão |
|---|---|---|---|
| brijr/iris | A/B/D | UPDATE_EXISTING | `runtime-ui-verification`: captura visual reproduzível exige metadata de viewport/DPR/theme/selector/waits; runtime Rust/MCP não é importado |
| apache/maka | A/B/D | UPDATE_EXISTING | `graph-engineering`: append-only runtime event log como record e projections reconstruíveis |
| MengTo/threeui | B/D | KEEP_EXTERNAL_REFERENCE | catálogo/runtime de componentes 3D; capabilities já cobertas por creative-web-effects/shader/web-design |
| harry0703/MangoDisk | A/B/D | UPDATE_EXISTING | `verify-before-claim`: read-only discovery, preview/confirm, mutação, readback e operation history para mudanças destrutivas |
| ericzakariasson/scandinavian-design | A/B | UPDATE_EXISTING | `design-direction`: estilo nomeado é direção contextual, não preset; preservar densidade/semântica/identidade |
| furkankly/zoetrope | B/D | ABSORB_METHOD_ONLY | reforça event-log/replay/graph observability; owner `graph-engineering`, sem importar runtime |
| amagine-ai/Amagine3D | A/B/D | UPDATE_EXISTING | `procedural-3d-reconstruction`: intent vs semantic scene e checks físicos/fabricação |
| Spielewoy/autoprompt-skill | A/B/D | KEEP_EXTERNAL_REFERENCE | review/fix/recheck, routing e multi-agent já cobertos por verify/code-review/graph; benchmarks não reproduzidos |
| davatron5000/microlighter | D/B | KEEP_EXTERNAL_REFERENCE | biblioteca técnica; clean DOM + native Highlight API é referência de implementação, não capability genérica nova |
| JetBrains/benjamin-plus-skill | A/B | UPDATE_EXISTING | `codex-cost-efficiency`: one-pass recon, keyhole reads e polling como custo; claims percentuais não importados |
| jaredrhod/fullstack-agent | D/B | KEEP_EXTERNAL_REFERENCE | integração Claude-specific de memória/voz/face/hands; componentes e instalador não são capacidades nativas |
| MrMoT9I/paper-aquarium | D/B | KEEP_EXTERNAL_REFERENCE | sistema técnico criativo com CV/Three.js/security patterns; sem owner novo necessário |
| vasanthsreeram/Alvarmethod | A/B/D | UPDATE_EXISTING | `teach`: probe curto/adaptativo antes do plano; restante já coberto por teach + evidence verification |

## Segurança e portabilidade

- Iris: installer curl-pipe-shell, Rust binary e Chrome CDP/MCP. Metodologia apenas.
- Maka: Electron/Node/Rust, modelos externos e execução de ferramentas. Metodologia apenas.
- ThreeUI: package/CLI e assets com fronteiras de licença/entitlement. Não copiar Pro/assets.
- MangoDisk: operações destrutivas e privilégios de sistema; padrões de approval/readback são úteis, runtime não.
- Scandinavian Design: scripts/evals e presets estilísticos. Absorver princípios, não valores rígidos.
- Zoetrope: leitura de transcripts locais e binário Rust/WASM. Read-only é positivo; não necessário no Arsenal.
- Amagine3D: CAD/build123d/OCP, shell/tool runtime e possíveis buscas externas. Não importar execução.
- Autoprompt: installer, hooks/injeção e subagents. Não executar; claims de benchmark tratados como claims da fonte.
- MicroLighter: biblioteca JS, TextMate grammars. Sem necessidade de integração canônica.
- Benjamin+: hook/instrução global. Importar apenas hábitos medidos; não instalar/injetar globalmente.
- Fullstack-agent: wizard instala múltiplos repos, voz/webcam/memória e persistência. CAUTION alto.
- Paper Aquarium: uploads, rede local/internet, modelos comerciais e scripts de conversão. Referência apenas.
- Alvarmethod: installers multi-agent e arquivos persistentes de learner. Absorver pedagogia sem exigir picker específico.

## Mudanças publicadas

- `codex-cost-efficiency`: reconnaissance agrupado, keyhole reads e polling proporcional.
- `teach`: probe curto por strands quando o nível é incerto.
- `runtime-ui-verification`: metadata necessária para screenshot reproduzível.
- `graph-engineering`: event log append-only como record durável; projections/context podem ser compactados.
- `procedural-3d-reconstruction`: intent imutável vs semantic scene mutável; checks de fabricação.
- `design-direction`: estilos Scandinavian/Nordic/minimal como direção contextual.
- `verify-before-claim`: discovery read-only → preview/approval → mutation → readback para operações destrutivas.

## Não-criação

Nenhuma nova skill foi criada. Todas as capabilities úteis têm owner canônico adequado. ThreeUI, MicroLighter, Fullstack Agent e Paper Aquarium são principalmente implementações/repertório técnico; Autoprompt e Zoetrope reforçam owners já existentes.

## Limites

Benchmarks das fontes não foram reproduzidos. Nenhum runtime externo foi instalado/executado. Claims de performance, qualidade e hardware permanecem atribuídos às fontes. Licenças/assets devem ser rechecados no commit efetivamente reutilizado.
