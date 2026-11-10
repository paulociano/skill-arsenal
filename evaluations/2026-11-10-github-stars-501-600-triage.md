# GitHub por estrelas, posições 501–600: triagem (2026-11-10)

## Fonte e método
GitHub Search API, `stars:>1000 sort:stars order:desc`, páginas 11–12 de 50, consultada em 2026-11-10 via `gh api`. Continuação de `2026-11-10-github-stars-401-500-triage.md`. Estrelas medem popularidade, não qualidade. Nível de garantia de todas as decisões: `static_only`.

Fluxo: `arsenal-autopilot` → `evaluate-and-import-skill` + `skill-security-review`. Nada instalado ou executado.

### Níveis de evidência
- **100/100 triados** por identidade, descrição e cruzamento com o Arsenal (27 já tinham registro).
- **6 inspecionados** por clone sem blobs, README e LICENSE: shannon, Kronos, GitNexus, claude-howto, big-list-of-naughty-strings, qlib.
- **1 lido em profundidade**: `minimaxir/big-list-of-naughty-strings/blns.txt` (categorias; MIT).

## Atualização aplicada
- **big-list-of-naughty-strings → `skills/synthetic-test-data-engineering/SKILL.md`**: categorias de strings problemáticas para campos de texto livre (palavras reservadas, strings que parecem número, controles invisíveis, aspas, emoji e bandeiras, texto RTL, mudança de tamanho ao virar minúscula, strings longas, trechos que parecem SQL/script); devem ser tratadas como texto, nunca interpretadas.

## Rodada de baixo rendimento
Esta faixa é dominada por bibliotecas, ferramentas de desenvolvedor e apps (82 referências). Os repositórios em forma de skill ou já estavam no Arsenal (`obsidian-skills`, `open-code-review`, `codebase-memory-mcp`, `agentic-awesome-skills`) ou repetem métodos já absorvidos (`shannon` repete o que veio do Strix; `qlib` e `Kronos` repetem o que veio do TradingAgents). Licenças restritivas: `GitNexus` (PolyForm Noncommercial), `shannon` (AGPL).

## Rejeitados
`NARKOZ/hacker-scripts` (piada), `MHSanaei/3x-ui` e `v2ray/v2ray-core` (proxy), `moeru-ai/airi` (companheira virtual "waifu": contrária às regras do Arsenal sobre dependência emocional).

## Instalar como skill no Claude
Nada novo recomendado.

## Tabela
| # | Repositório | Estrelas | Último push | Classe | Decisão | Owner | Fundamentação |
|---:|---|---:|---|---|---|---|---|
| 501 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | 51653 | 2026-11-10 | D | ALREADY_EVALUATED | `creative-web-effects` | Já referenciado. |
| 502 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | 51648 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `web-application-security-audit` | Pentester autônomo que executa exploits ('no exploit, no report'); AGPL; mesma regra já absorvida do Strix; só em sandbox com permissão. |
| 503 | [roboflow/supervision](https://github.com/roboflow/supervision) | 51585 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 504 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 51564 | 2026-09-15 | A | ALREADY_EVALUATED | `obsidian-vault-authoring` | Já absorvido. |
| 505 | [ethereum/go-ethereum](https://github.com/ethereum/go-ethereum) | 51472 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 506 | [DefinitelyTyped/DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) | 51469 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 507 | [tldraw/tldraw](https://github.com/tldraw/tldraw) | 51450 | 2026-11-10 | D | ALREADY_EVALUATED | `architecture-visualization` | Já referenciado. |
| 508 | [serhii-londar/open-source-mac-os-apps](https://github.com/serhii-londar/open-source-mac-os-apps) | 51311 | 2026-10-31 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 509 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | 51263 | 2026-11-10 | D | REJECT | `—` | Companheira virtual 'waifu'; contrário à política de memória/dependência emocional do Arsenal. |
| 510 | [justjavac/wechat-miniapp-radar](https://github.com/justjavac/wechat-miniapp-radar) | 51167 | 2026-10-02 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 511 | [astral-sh/ruff](https://github.com/astral-sh/ruff) | 51162 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 512 | [apple/container](https://github.com/apple/container) | 51136 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 513 | [chenglou/pretext](https://github.com/chenglou/pretext) | 51025 | 2026-10-15 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 514 | [cypress-io/cypress](https://github.com/cypress-io/cypress) | 51024 | 2026-11-10 | D | ALREADY_EVALUATED | `runtime-ui-verification` | Já referenciado. |
| 515 | [Semantic-Org/Semantic-UI](https://github.com/Semantic-Org/Semantic-UI) | 50996 | 2024-11-27 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 516 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse) | 50866 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 517 | [nlohmann/json](https://github.com/nlohmann/json) | 50865 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 518 | [team-spotube/spotube](https://github.com/team-spotube/spotube) | 50713 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 519 | [kelseyhightower/kubernetes-the-hard-way](https://github.com/kelseyhightower/kubernetes-the-hard-way) | 50652 | 2025-04-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 520 | [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | 50574 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 521 | [TanStack/query](https://github.com/TanStack/query) | 50557 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 522 | [lukasz-madon/awesome-remote-job](https://github.com/lukasz-madon/awesome-remote-job) | 50525 | 2026-09-21 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 523 | [mastodon/mastodon](https://github.com/mastodon/mastodon) | 50505 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 524 | [huginn/huginn](https://github.com/huginn/huginn) | 50483 | 2026-11-09 | D | ALREADY_EVALUATED | `ai-workflow-automation-engineering` | Já referenciado. |
| 525 | [AlistGo/alist](https://github.com/AlistGo/alist) | 50442 | 2026-10-21 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 526 | [jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) | 50415 | 2024-06-26 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 527 | [Homebrew/brew](https://github.com/Homebrew/brew) | 50384 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 528 | [mudler/LocalAI](https://github.com/mudler/LocalAI) | 50296 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Inferência local; depende de hardware. |
| 529 | [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg) | 50268 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 530 | [metabase/metabase](https://github.com/metabase/metabase) | 50267 | 2026-11-10 | D | ALREADY_EVALUATED | `dashboard-design` | BI já referenciado. |
| 531 | [tmux/tmux](https://github.com/tmux/tmux) | 50239 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 532 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | 50236 | 2026-11-10 | D | ALREADY_EVALUATED | `—` | Já avaliado (2026-09-26). |
| 533 | [microsoft/qlib](https://github.com/microsoft/qlib) | 50202 | 2026-11-04 | D | KEEP_EXTERNAL_REFERENCE | `investment-portfolio-analysis` | Plataforma quant com banco point-in-time; método já absorvido via TradingAgents. |
| 534 | [hashicorp/terraform](https://github.com/hashicorp/terraform) | 50200 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 535 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | 50055 | 2026-05-22 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente/harness/app; aider e herdr já citados. |
| 536 | [jgthms/bulma](https://github.com/jgthms/bulma) | 50033 | 2026-09-21 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 537 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | 50000 | 2026-11-07 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente/harness/app; aider e herdr já citados. |
| 538 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 49996 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente/harness/app; aider e herdr já citados. |
| 539 | [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) | 49986 | 2026-03-04 | B | ALREADY_EVALUATED | `teach` | Já referenciado. |
| 540 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | 49899 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 541 | [NARKOZ/hacker-scripts](https://github.com/NARKOZ/hacker-scripts) | 49869 | 2023-10-23 | C | REJECT | `—` | Scripts-piada de automação pessoal; sem método. |
| 542 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 49788 | 2026-11-10 | A/D | ALREADY_EVALUATED | `code-review` | Já citado (3 registros). |
| 543 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 49745 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Inferência local; depende de hardware. |
| 544 | [DovAmir/awesome-design-patterns](https://github.com/DovAmir/awesome-design-patterns) | 49692 | 2024-10-25 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 545 | [bevyengine/bevy](https://github.com/bevyengine/bevy) | 49677 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `game-development-cycle` | Engine de jogos em Rust. |
| 546 | [MHSanaei/3x-ui](https://github.com/MHSanaei/3x-ui) | 49674 | 2026-11-06 | D | REJECT | `—` | Painel/núcleo de proxy; fora da finalidade. |
| 547 | [bigskysoftware/htmx](https://github.com/bigskysoftware/htmx) | 49628 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 548 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 49493 | 2026-11-10 | B | ALREADY_EVALUATED | `arsenal-autopilot` | Catálogo de ~3 mil skills já usado como radar. |
| 549 | [akullpp/awesome-java](https://github.com/akullpp/awesome-java) | 49491 | 2026-09-23 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 550 | [algorithm-visualizer/algorithm-visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer) | 49462 | 2024-06-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 551 | [slidevjs/slidev](https://github.com/slidevjs/slidev) | 49428 | 2026-11-05 | D | ALREADY_EVALUATED | `architecture-visualization` | Já referenciado. |
| 552 | [JuliaLang/julia](https://github.com/JuliaLang/julia) | 49256 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 553 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 49149 | 2026-11-10 | D | ALREADY_EVALUATED | `runtime-ui-verification` | Já referenciado. |
| 554 | [nilbuild/design-patterns-for-humans](https://github.com/nilbuild/design-patterns-for-humans) | 48944 | 2024-12-02 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 555 | [brillout/awesome-react-components](https://github.com/brillout/awesome-react-components) | 48845 | 2026-01-26 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 556 | [pixijs/pixijs](https://github.com/pixijs/pixijs) | 48664 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 557 | [iamkun/dayjs](https://github.com/iamkun/dayjs) | 48654 | 2026-11-06 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 558 | [hiroi-sora/Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) | 48567 | 2025-11-20 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 559 | [type-challenges/type-challenges](https://github.com/type-challenges/type-challenges) | 48562 | 2026-10-26 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 560 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 48458 | 2026-11-10 | D | ALREADY_EVALUATED | `code-understanding-audit` | Já citado. |
| 561 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | 48421 | 2026-11-05 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 562 | [GitHubDaily/GitHubDaily](https://github.com/GitHubDaily/GitHubDaily) | 48417 | 2025-12-31 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 563 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | 48400 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `code-understanding-audit` | Grafo de código com 34 skills; licença PolyForm Noncommercial; métodos já cobertos. |
| 564 | [SimplifyJobs/Summer2027-Internships](https://github.com/SimplifyJobs/Summer2027-Internships) | 48382 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 565 | [usebruno/bruno](https://github.com/usebruno/bruno) | 48325 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 566 | [exo-explore/exo](https://github.com/exo-explore/exo) | 48284 | 2026-11-06 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Inferência local; depende de hardware. |
| 567 | [nvm-windows/nvm](https://github.com/nvm-windows/nvm) | 48175 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 568 | [ReactiveX/RxJava](https://github.com/ReactiveX/RxJava) | 48154 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 569 | [karan/Projects](https://github.com/karan/Projects) | 48103 | 2024-08-14 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 570 | [discourse/discourse](https://github.com/discourse/discourse) | 48074 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 571 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | 47988 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 572 | [acmesh-official/acme.sh](https://github.com/acmesh-official/acme.sh) | 47939 | 2026-11-07 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 573 | [gogs/gogs](https://github.com/gogs/gogs) | 47929 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 574 | [moment/moment](https://github.com/moment/moment) | 47873 | 2026-10-08 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 575 | [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) | 47870 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente/harness/app; aider e herdr já citados. |
| 576 | [dypsilon/frontend-dev-bookmarks](https://github.com/dypsilon/frontend-dev-bookmarks) | 47737 | 2024-05-21 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 577 | [oobabooga/textgen](https://github.com/oobabooga/textgen) | 47734 | 2026-08-17 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Inferência local; depende de hardware. |
| 578 | [minimaxir/big-list-of-naughty-strings](https://github.com/minimaxir/big-list-of-naughty-strings) | 47716 | 2024-04-18 | B | UPDATE_EXISTING | `synthetic-test-data-engineering` | Categorias de strings problemáticas para testar campos de texto. |
| 579 | [prisma/orm](https://github.com/prisma/orm) | 47663 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 580 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 47564 | 2026-04-13 | D | KEEP_EXTERNAL_REFERENCE | `scenario-forecasting` | Modelo de fundação para candles (OHLCV); previsão de preço de curto prazo, sem uso no seu trabalho; não tratar previsão como recomendação. |
| 581 | [apache/airflow](https://github.com/apache/airflow) | 47440 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 582 | [slab/quill](https://github.com/slab/quill) | 47368 | 2025-07-25 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 583 | [9001/copyparty](https://github.com/9001/copyparty) | 47318 | 2026-10-21 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 584 | [gedoor/legado](https://github.com/gedoor/legado) | 47242 | 2026-05-27 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 585 | [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | 47165 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 586 | [lysine-dev/okhttp](https://github.com/lysine-dev/okhttp) | 47110 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 587 | [typescript-cheatsheets/react](https://github.com/typescript-cheatsheets/react) | 47088 | 2026-09-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 588 | [iina/iina](https://github.com/iina/iina) | 47082 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 589 | [Asabeneh/30-Days-Of-JavaScript](https://github.com/Asabeneh/30-Days-Of-JavaScript) | 47002 | 2026-08-27 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 590 | [microsoft/monaco-editor](https://github.com/microsoft/monaco-editor) | 46961 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 591 | [cli/cli](https://github.com/cli/cli) | 46956 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 592 | [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat) | 46944 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente/harness/app; aider e herdr já citados. |
| 593 | [helix-editor/helix](https://github.com/helix-editor/helix) | 46942 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 594 | [serverless/serverless](https://github.com/serverless/serverless) | 46930 | 2026-11-06 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 595 | [DIYgod/RSSHub](https://github.com/DIYgod/RSSHub) | 46914 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 596 | [v2ray/v2ray-core](https://github.com/v2ray/v2ray-core) | 46908 | 2026-08-31 | D | REJECT | `—` | Painel/núcleo de proxy; fora da finalidade. |
| 597 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | 46900 | 2026-11-03 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |
| 598 | [jgm/pandoc](https://github.com/jgm/pandoc) | 46885 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 599 | [zhongyang219/TrafficMonitor](https://github.com/zhongyang219/TrafficMonitor) | 46882 | 2026-09-27 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 600 | [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) | 46862 | 2026-10-18 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou lista de referência. |

## Limites da validação
Triagem documental. Código, dependências e scripts não auditados.
