# GitHub por estrelas, posições 401–500: triagem (2026-11-10)

## Fonte e método
GitHub Search API, `stars:>1000 sort:stars order:desc`, páginas 9–10 de 50, consultada em 2026-11-10 via `gh api`. Continuação de `2026-11-10-github-stars-301-400-triage.md`. Estrelas medem popularidade, não qualidade. Nível de garantia de todas as decisões: `static_only`.

Fluxo: `arsenal-autopilot` → `evaluate-and-import-skill` + `skill-security-review`. Nada instalado ou executado.

### Níveis de evidência
- **100/100 triados** por identidade, descrição e cruzamento com o Arsenal (18 já tinham registro).
- **7 inspecionados** por clone sem blobs, README, LICENSE e listagem de `SKILL.md`: academic-research-skills, BMAD-METHOD, chrome-devtools-mcp, nature-skills, CLI-Anything, maybe, multica.
- **2 lidos em profundidade**: `bmad-code-org/BMAD-METHOD/skills/bmad-advanced-elicitation/SKILL.md` (MIT) e `ChromeDevTools/chrome-devtools-mcp/skills/debug-optimize-lcp/SKILL.md` (Apache-2.0).

## Atualizações aplicadas
- **BMAD-METHOD → `skills/decision-analysis/SKILL.md`** (seção de lentes adversariais): o brief de cada crítico inclui o que já está decidido, pede no máximo cinco achados localizados, cada leitor lê o alvo do zero; a fusão vira uma lista numerada de mudanças com descartes visíveis e premissas rejeitadas como decisão do usuário. Vale também para criticar rascunhos e planos.
- **chrome-devtools-mcp → `skills/web-quality-audit/SKILL.md`**: decompor o LCP em TTFB, atraso de carga, duração de carga e atraso de render antes de otimizar; atacar a parte desproporcional.

## Recursos para instalar
- **Chrome DevTools MCP** (Apache-2.0, Google): servidor MCP local para Claude Code com traces de performance, rede e console. Útil para depurar desempenho dos seus apps. No Claude chat, o Claude in Chrome já cobre navegação; o DevTools MCP acrescenta traces de performance.
- Nenhuma skill nova: `emilkowalski/skills` já instaladas; `academic-research-skills` tem licença **CC BY-NC 4.0** (não comercial) e foge do seu trabalho.

## Rejeitados
Proxy/contorno (`shadowsocks-windows`, `fanqiang`), torrent e download de mídia (`trackerslist`, `you-get`), deepfake (`faceswap`), reconhecimento facial (`face_recognition`), prompts vazados (`CL4R1T4S`), revenda/exposição de assinaturas de agentes como API (`CLIProxyAPI`, `new-api`), modificação de dispositivos (`cleanyourtv`, `AnyPS5`).

## Tabela
| # | Repositório | Estrelas | Último push | Classe | Decisão | Owner | Fundamentação |
|---:|---|---:|---|---|---|---|---|
| 401 | [FiloSottile/mkcert](https://github.com/FiloSottile/mkcert) | 59860 | 2024-08-13 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 402 | [jquery/jquery](https://github.com/jquery/jquery) | 59858 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 403 | [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch) | 59834 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 404 | [meta-llama/llama](https://github.com/meta-llama/llama) | 59623 | 2025-01-26 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Modelo/pesos ou app de geração local. |
| 405 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 59584 | 2026-11-10 | A | ALREADY_EVALUATED | `go-to-market-strategy` | Já avaliado (7 registros); skill `copywriting` instalada no Claude. |
| 406 | [shadowsocks/shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows) | 59486 | 2025-01-01 | D | REJECT | `—` | Proxy/contorno de censura, torrent ou download de mídia; fora da finalidade. |
| 407 | [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | 59194 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 408 | [rails/rails](https://github.com/rails/rails) | 59094 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 409 | [go-gitea/gitea](https://github.com/go-gitea/gitea) | 59010 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 410 | [FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus) | 58947 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, plataforma ou app de IA; sem método novo. |
| 411 | [pmndrs/zustand](https://github.com/pmndrs/zustand) | 58914 | 2026-11-06 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 412 | [pathwaycom/serviette](https://github.com/pathwaycom/serviette) | 58716 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, plataforma ou app de IA; sem método novo. |
| 413 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 58554 | 2026-09-22 | D | KEEP_EXTERNAL_REFERENCE | `ai-workflow-automation-engineering` | Gera CLIs + SKILL.md para ~150 apps (Blender, QGIS…); cada harness precisa de revisão própria. |
| 414 | [angular/angular.js](https://github.com/angular/angular.js) | 58434 | 2024-04-12 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 415 | [wasabeef/awesome-android-ui](https://github.com/wasabeef/awesome-android-ui) | 58390 | 2026-06-05 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 416 | [ultralytics/yolov5](https://github.com/ultralytics/yolov5) | 58260 | 2026-11-07 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 417 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | 58189 | 2026-11-10 | D | REJECT | `—` | Expõem assinaturas de agentes (Claude Code etc.) como API ou revendem acesso; termos de uso e credenciais. |
| 418 | [agalwood/Motrix](https://github.com/agalwood/Motrix) | 58110 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 419 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 57968 | 2026-11-07 | D | KEEP_EXTERNAL_REFERENCE | `teach` | Tutor personalizado; método de ensino já em teach. |
| 420 | [appwrite/appwrite](https://github.com/appwrite/appwrite) | 57931 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 421 | [Textualize/rich](https://github.com/Textualize/rich) | 57784 | 2026-11-07 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 422 | [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57713 | 2024-06-26 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |
| 423 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 57709 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 424 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | 57667 | 2026-10-08 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |
| 425 | [h5bp/html5-boilerplate](https://github.com/h5bp/html5-boilerplate) | 57666 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 426 | [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt) | 57634 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, plataforma ou app de IA; sem método novo. |
| 427 | [deepfakes/faceswap](https://github.com/deepfakes/faceswap) | 57606 | 2026-08-05 | D | REJECT | `—` | Deepfake facial; risco de abuso. |
| 428 | [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | 57212 | 2026-06-24 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 429 | [laurent22/joplin](https://github.com/laurent22/joplin) | 57129 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 430 | [typst/typst](https://github.com/typst/typst) | 57111 | 2026-11-06 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 431 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 56965 | 2026-10-08 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Modelo/pesos ou app de geração local. |
| 432 | [ageitgey/face_recognition](https://github.com/ageitgey/face_recognition) | 56893 | 2026-06-25 | D | REJECT | `—` | Reconhecimento facial; risco de vigilância de pessoas. |
| 433 | [soimort/you-get](https://github.com/soimort/you-get) | 56860 | 2026-10-06 | D | REJECT | `—` | Proxy/contorno de censura, torrent ou download de mídia; fora da finalidade. |
| 434 | [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions) | 56785 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |
| 435 | [FuelLabs/fuel-core](https://github.com/FuelLabs/fuel-core) | 56762 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 436 | [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | 56744 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `investment-portfolio-analysis` | Bot de trade de cripto com execução real; não instalar; backtest exige as regras de ponto no tempo. |
| 437 | [golang-standards/project-layout](https://github.com/golang-standards/project-layout) | 56740 | 2026-04-28 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |
| 438 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 56729 | 2026-11-09 | A/D | ALREADY_EVALUATED | `academic-paper-orchestration` | Já citado (2 registros). |
| 439 | [remix-run/react-router](https://github.com/remix-run/react-router) | 56635 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 440 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | 56578 | 2026-11-10 | D | REJECT | `—` | Proxy/contorno de censura, torrent ou download de mídia; fora da finalidade. |
| 441 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | 56434 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, plataforma ou app de IA; sem método novo. |
| 442 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 56353 | 2026-11-10 | A | KEEP_EXTERNAL_REFERENCE | `academic-paper-orchestration` | Pipeline acadêmico pesquisa→escrita→revisão; licença CC BY-NC 4.0 (não comercial); sobrepõe owners acadêmicos. |
| 443 | [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | 56095 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 444 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | 55978 | 2026-11-10 | D | REJECT | `—` | Modificação de dispositivos/consoles; fora da finalidade. |
| 445 | [gatsbyjs/gatsby](https://github.com/gatsbyjs/gatsby) | 55918 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 446 | [WerWolv/ImHex](https://github.com/WerWolv/ImHex) | 55818 | 2026-10-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 447 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | 55803 | 2026-11-09 | A | ALREADY_ADOPTED | `web-design-engineer` | Instaladas no Claude (emil-design-eng, animation-vocabulary, apple-design etc.). |
| 448 | [TryGhost/Ghost](https://github.com/TryGhost/Ghost) | 55736 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 449 | [azl397985856/leetcode](https://github.com/azl397985856/leetcode) | 55705 | 2025-07-16 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |
| 450 | [odoo/odoo](https://github.com/odoo/odoo) | 55699 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 451 | [ngosang/trackerslist](https://github.com/ngosang/trackerslist) | 55650 | 2026-11-10 | D | REJECT | `—` | Proxy/contorno de censura, torrent ou download de mídia; fora da finalidade. |
| 452 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 55648 | 2026-11-10 | D | ALREADY_EVALUATED | `coding-agent-engineering` | Avaliado hoje. |
| 453 | [multica-ai/multica](https://github.com/multica-ai/multica) | 55581 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, plataforma ou app de IA; sem método novo. |
| 454 | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 55566 | 2026-08-13 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, plataforma ou app de IA; sem método novo. |
| 455 | [romkatv/powerlevel10k](https://github.com/romkatv/powerlevel10k) | 55354 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 456 | [lyswhut/lx-music-desktop](https://github.com/lyswhut/lx-music-desktop) | 55238 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 457 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 55230 | 2026-11-08 | A/D | UPDATE_EXISTING | `decision-analysis` | Brief com 'o que já está decidido', ≤5 achados, fusão numerada com descartes visíveis. |
| 458 | [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 55121 | 2024-09-18 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 459 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 55074 | 2026-11-10 | A/D | UPDATE_EXISTING | `web-quality-audit` | Decomposição do LCP em quatro partes antes de otimizar; MCP local para Claude Code. |
| 460 | [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | 55073 | 2026-11-10 | D | ALREADY_EVALUATED | `meeting-knowledge-capture` | Já referenciado. |
| 461 | [AntonOsika/gpt-engineer](https://github.com/AntonOsika/gpt-engineer) | 54964 | 2025-05-14 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, plataforma ou app de IA; sem método novo. |
| 462 | [vuejs/core](https://github.com/vuejs/core) | 54908 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 463 | [psf/requests](https://github.com/psf/requests) | 54763 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 464 | [wagoodman/dive](https://github.com/wagoodman/dive) | 54717 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 465 | [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54670 | 2024-08-29 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, plataforma ou app de IA; sem método novo. |
| 466 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | 54497 | 2026-11-04 | B | KEEP_EXTERNAL_REFERENCE | `ai-workflow-automation-engineering` | Receitas oficiais da API do Claude; consultar quando construir com a API. |
| 467 | [google/material-design-icons](https://github.com/google/material-design-icons) | 54273 | 2026-10-23 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 468 | [chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) | 54239 | 2026-06-17 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |
| 469 | [maybe-finance/maybe](https://github.com/maybe-finance/maybe) | 54195 | 2025-07-24 | D | KEEP_EXTERNAL_REFERENCE | `personal-financial-planning` | App de finanças pessoais (AGPL, sem push desde 2025-07); referência de produto, não skill. |
| 470 | [dockur/windows](https://github.com/dockur/windows) | 54150 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 471 | [mozilla/pdf.js](https://github.com/mozilla/pdf.js) | 54122 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 472 | [ElemeFE/element](https://github.com/ElemeFE/element) | 53978 | 2024-08-20 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 473 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 53935 | 2026-08-27 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 474 | [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus) | 53873 | 2025-12-01 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Modelo/pesos ou app de geração local. |
| 475 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | 53677 | 2026-10-30 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 476 | [JetBrains/kotlin](https://github.com/JetBrains/kotlin) | 53562 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 477 | [necolas/normalize.css](https://github.com/necolas/normalize.css) | 53482 | 2024-06-12 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 478 | [expo/expo](https://github.com/expo/expo) | 53451 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 479 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | 53402 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, plataforma ou app de IA; sem método novo. |
| 480 | [jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker) | 53310 | 2026-04-19 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 481 | [dkhamsing/open-source-ios-apps](https://github.com/dkhamsing/open-source-ios-apps) | 53169 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |
| 482 | [poteto/hiring-without-whiteboards](https://github.com/poteto/hiring-without-whiteboards) | 53169 | 2026-09-24 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |
| 483 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 53060 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `academic-paper-orchestration` | 24 skills de escrita/figuras no padrão Nature; fora do seu trabalho; owners acadêmicos já existem. |
| 484 | [sickcodes/Docker-OSX](https://github.com/sickcodes/Docker-OSX) | 53003 | 2025-11-11 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 485 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 52959 | 2026-11-10 | D | REJECT | `—` | Modificação de dispositivos/consoles; fora da finalidade. |
| 486 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | 52868 | 2026-11-10 | D | ALREADY_EVALUATED | `agent-memory-engineering` | Já referenciado. |
| 487 | [ionic-team/ionic-framework](https://github.com/ionic-team/ionic-framework) | 52750 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 488 | [etcd-io/etcd](https://github.com/etcd-io/etcd) | 52688 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 489 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 52538 | 2026-11-10 | A/D | ALREADY_EVALUATED | `web-design-engineer` | Reavaliado hoje (v2). |
| 490 | [prettier/prettier](https://github.com/prettier/prettier) | 52412 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 491 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | 52388 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 492 | [xai-org/grok-1](https://github.com/xai-org/grok-1) | 52221 | 2024-08-30 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Modelo/pesos ou app de geração local. |
| 493 | [upscayl/upscayl](https://github.com/upscayl/upscayl) | 52180 | 2026-10-05 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 494 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | 52093 | 2026-11-09 | C | REJECT | `—` | Prompts de sistema vazados. |
| 495 | [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) | 52060 | 2023-12-29 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |
| 496 | [google/guava](https://github.com/google/guava) | 51922 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 497 | [jekyll/jekyll](https://github.com/jekyll/jekyll) | 51762 | 2026-10-13 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 498 | [skylot/jadx](https://github.com/skylot/jadx) | 51745 | 2026-11-08 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 499 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 51703 | 2026-11-10 | D | REJECT | `—` | Expõem assinaturas de agentes (Claude Code etc.) como API ou revendem acesso; termos de uso e credenciais. |
| 500 | [charlax/professional-programming](https://github.com/charlax/professional-programming) | 51671 | 2026-10-27 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional, guia ou dataset de referência. |

## Limites da validação
Triagem documental; só os SKILL.md citados foram lidos. Código, dependências e scripts não auditados.
