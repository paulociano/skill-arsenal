# GitHub por estrelas, posições 301–400: triagem (2026-11-10)

## Fonte e método
GitHub Search API, `stars:>1000 sort:stars order:desc`, páginas 7–8 de 50, consultada em 2026-11-10 via `gh api`. Continuação de `2026-11-10-github-stars-201-300-triage.md`. Estrelas medem popularidade, não qualidade. Nível de garantia de todas as decisões: `static_only`.

Fluxo: `arsenal-autopilot` → `evaluate-and-import-skill` + `skill-security-review`. Nada instalado ou executado.

### Níveis de evidência
- **100/100 triados** por identidade, descrição e cruzamento com o Arsenal (24 já tinham registro).
- **8 inspecionados** por clone sem blobs, README, LICENSE e listagem de `SKILL.md`: daily_stock_analysis, claude-code-best-practice, ai-hedge-fund, context7, TrendRadar, mempalace, humanizer, free-claude-code.
- **2 lidos em profundidade**: `upstash/context7/plugins/agent-plugins/context7/skills/context7-mcp/SKILL.md` (MIT) e `ZhuLinsen/daily_stock_analysis/SKILL.md` (MIT).

## Atualização aplicada
- **upstash/context7 → `skills/library-version-grounding/SKILL.md`**: como usar um MCP de documentação por versão (resolver o ID, preferir a versão citada, uma consulta por conceito, ler o código-fonte indexado para fatos exatos e citar arquivo/linha, limite de chamadas) e o aviso de que backend/parser são privados e não se deve mandar código proprietário nas consultas.

## Recurso indicado para instalar
- **Conector Context7** — existe no diretório de conectores do Claude (não instalado nesta conta; exige autenticação). Útil quando você estiver programando (jogos, apps, Arsenal) e precisar da documentação atual de uma biblioteca.

## Rejeitados
`kelseyhightower/nocode` (piada), `2dust/v2rayNG` e `chen08209/FlClash` (proxy), `ChrisTitusTech/winutil`, `Raphire/Win11Debloat` e `topjohnwu/Magisk` (alteram o sistema com privilégio), `xtekky/gpt4free`, `Alishahryar1/free-claude-code` e `Ebony-Vinyl/dsh-our-free-model` (acesso "grátis" a modelos pagos por terceiros: termos de uso, credenciais e roteamento de dados).

## Lidos e não incorporados
- `daily_stock_analysis`: o SKILL.md só documenta funções Python do próprio projeto; saída com "pontos de compra/venda" para mercado chinês. Fora do método do Arsenal, que não emite sinais de trade.
- `ai-hedge-fund`: agentes que imitam investidores famosos com paper trading; educacional; owners de valuation e carteira já cobrem o método, e o TradingAgents (absorvido hoje) é mais rigoroso em dados no ponto do tempo.
- `mempalace`: memória com alegação de "melhor benchmark" não verificada; `agent-memory-engineering` já cobre o método.
- Clonagem de voz (`GPT-SoVITS`, `voicebox`, `Real-Time-Voice-Cloning`): só com consentimento de quem é clonado.

## Tabela
| # | Repositório | Estrelas | Último push | Classe | Decisão | Owner | Fundamentação |
|---:|---|---:|---|---|---|---|---|
| 301 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 69539 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `investment-portfolio-analysis` | Analisador de ações com SKILL.md que só documenta o próprio código Python; foco em mercado chinês, sinais de compra/venda. |
| 302 | [gorhill/uBlock](https://github.com/gorhill/uBlock) | 69234 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 303 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 69203 | 2026-09-14 | A | ALREADY_EVALUATED | `web-application-security-audit` | Já absorvida. |
| 304 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 68946 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Catálogo de práticas de Claude Code com skills de exemplo; sobrepõe owners e skills já instaladas. |
| 305 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 68853 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente/framework; autogen já citado. |
| 306 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | 68767 | 2026-11-06 | D | ALREADY_EVALUATED | `agent-memory-engineering` | Já avaliado. |
| 307 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | 68671 | 2026-11-10 | D | REJECT | `—` | Acesso 'gratuito' a modelos pagos por proxies/terceiros; risco de termos de uso, credenciais e roteamento de dados. |
| 308 | [base/node](https://github.com/base/node) | 68295 | 2026-09-08 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 309 | [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 68153 | 2026-11-10 | D | ALREADY_EVALUATED | `agent-memory-engineering` | Já referenciado. |
| 310 | [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68137 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 311 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | 68133 | 2026-11-10 | D | REJECT | `—` | Acesso 'gratuito' a modelos pagos por proxies/terceiros; risco de termos de uso, credenciais e roteamento de dados. |
| 312 | [chartjs/Chart.js](https://github.com/chartjs/Chart.js) | 67789 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 313 | [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | 67744 | 2026-11-02 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 314 | [apache/echarts](https://github.com/apache/echarts) | 67703 | 2026-10-13 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 315 | [prometheus/prometheus](https://github.com/prometheus/prometheus) | 67618 | 2026-11-10 | D | ALREADY_EVALUATED | `software-engineering-cycle` | Já referenciado. |
| 316 | [blader/humanizer](https://github.com/blader/humanizer) | 67538 | 2026-11-10 | A | ALREADY_ADOPTED | `writing-quality` | Instalada no Claude como `humanizer`. |
| 317 | [sindresorhus/awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs) | 67442 | 2026-09-02 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 318 | [bradtraversy/design-resources-for-developers](https://github.com/bradtraversy/design-resources-for-developers) | 67372 | 2026-10-18 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 319 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 67231 | 2026-11-10 | A/D | ALREADY_ADOPTED | `signal-intelligence-digest` | Instalada no Claude como `last30days`. |
| 320 | [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | 67037 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 321 | [xtekky/gpt4free](https://github.com/xtekky/gpt4free) | 67024 | 2026-11-03 | D | REJECT | `—` | Acesso 'gratuito' a modelos pagos por proxies/terceiros; risco de termos de uso, credenciais e roteamento de dados. |
| 322 | [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | 66899 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 323 | [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) | 66823 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 324 | [meta/docusaurus](https://github.com/meta/docusaurus) | 66700 | 2026-11-06 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 325 | [leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts) | 66524 | 2026-10-21 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 326 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 66309 | 2026-11-09 | A | ALREADY_EVALUATED | `architecture-visualization` | Já avaliado. |
| 327 | [alacritty/alacritty](https://github.com/alacritty/alacritty) | 66162 | 2026-11-06 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 328 | [kelseyhightower/nocode](https://github.com/kelseyhightower/nocode) | 66041 | 2024-08-07 | C | REJECT | `—` | Repositório-piada; sem conteúdo. |
| 329 | [webpack/webpack](https://github.com/webpack/webpack) | 65997 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 330 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | 65966 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 331 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | 65902 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 332 | [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) | 65824 | 2026-11-04 | D | REJECT | `—` | Alteram o sistema operacional com privilégio; fora da finalidade e de risco. |
| 333 | [2dust/v2rayNG](https://github.com/2dust/v2rayNG) | 65675 | 2026-11-10 | D | REJECT | `—` | Cliente de proxy; fora da finalidade. |
| 334 | [kdn251/interviews](https://github.com/kdn251/interviews) | 65559 | 2025-05-12 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 335 | [traefik/traefik](https://github.com/traefik/traefik) | 65516 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 336 | [nocodb/nocodb](https://github.com/nocodb/nocodb) | 65483 | 2026-11-09 | D | ALREADY_EVALUATED | `software-engineering-cycle` | Já referenciado. |
| 337 | [scrapy/scrapy](https://github.com/scrapy/scrapy) | 65316 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 338 | [lydiahallie/javascript-questions](https://github.com/lydiahallie/javascript-questions) | 65277 | 2024-08-04 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 339 | [ryanoasis/nerd-fonts](https://github.com/ryanoasis/nerd-fonts) | 65187 | 2026-10-17 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 340 | [localstack/localstack](https://github.com/localstack/localstack) | 65121 | 2026-03-23 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 341 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 65098 | 2026-10-27 | D | ALREADY_EVALUATED | `software-engineering-cycle` | Já referenciado. |
| 342 | [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 64721 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `—` | Clonagem de voz; só com consentimento da pessoa clonada. |
| 343 | [rust-lang/rustlings](https://github.com/rust-lang/rustlings) | 64630 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 344 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | 64625 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `value-investing-company-analysis` | Agentes-persona de investidores famosos com paper trading; educacional, sem SKILL.md; já há owners de valuation. |
| 345 | [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | 64608 | 2025-11-12 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 346 | [termux/termux-app](https://github.com/termux/termux-app) | 64564 | 2026-11-05 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 347 | [upstash/context7](https://github.com/upstash/context7) | 64522 | 2026-11-10 | A/D | UPDATE_EXISTING | `library-version-grounding` | Método de consulta de docs por versão absorvido; conector disponível no Claude. |
| 348 | [keras-team/keras](https://github.com/keras-team/keras) | 64420 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 349 | [usememos/memos](https://github.com/usememos/memos) | 64385 | 2026-11-10 | D | ALREADY_EVALUATED | `software-engineering-cycle` | Já referenciado. |
| 350 | [git/git](https://github.com/git/git) | 64249 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 351 | [tldr-pages/tldr](https://github.com/tldr-pages/tldr) | 64189 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 352 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | 64160 | 2026-05-31 | A/D | ALREADY_EVALUATED | `software-engineering-cycle` | Já citado. |
| 353 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 64127 | 2026-11-10 | D | ALREADY_EVALUATED | `—` | Já citado. |
| 354 | [commaai/openpilot](https://github.com/commaai/openpilot) | 64100 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 355 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | 63967 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 356 | [jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop) | 63926 | 2026-11-05 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 357 | [topjohnwu/Magisk](https://github.com/topjohnwu/Magisk) | 63919 | 2026-11-10 | D | REJECT | `—` | Alteram o sistema operacional com privilégio; fora da finalidade e de risco. |
| 358 | [withastro/astro](https://github.com/withastro/astro) | 63875 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 359 | [marktext/marktext](https://github.com/marktext/marktext) | 63835 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 360 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 63572 | 2026-11-05 | D | KEEP_EXTERNAL_REFERENCE | `signal-intelligence-digest` | Monitor de tendências em plataformas chinesas; GPL; método de radar já coberto. |
| 361 | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | 63283 | 2026-11-10 | D | ALREADY_EVALUATED | `software-engineering-cycle` | Já referenciado. |
| 362 | [socketio/socket.io](https://github.com/socketio/socket.io) | 63243 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 363 | [tw93/Pake](https://github.com/tw93/Pake) | 63113 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 364 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 63064 | 2026-11-10 | D | ALREADY_EVALUATED | `ai-workflow-automation-engineering` | Gateway de LLM já referenciado. |
| 365 | [resume/resume.github.com](https://github.com/resume/resume.github.com) | 62899 | 2023-02-15 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 366 | [youngyangyang04/leetcode-master](https://github.com/youngyangyang04/leetcode-master) | 62810 | 2026-10-24 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 367 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | 62459 | 2026-11-04 | D | REJECT | `—` | Cliente de proxy; fora da finalidade. |
| 368 | [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | 62316 | 2026-11-08 | D | REJECT | `—` | Alteram o sistema operacional com privilégio; fora da finalidade e de risco. |
| 369 | [makeplane/plane](https://github.com/makeplane/plane) | 62270 | 2026-11-10 | D | ALREADY_EVALUATED | `software-engineering-cycle` | Já referenciado. |
| 370 | [penpot/penpot](https://github.com/penpot/penpot) | 62262 | 2026-11-10 | D | ALREADY_EVALUATED | `software-engineering-cycle` | Já referenciado. |
| 371 | [1c7/chinese-independent-developer](https://github.com/1c7/chinese-independent-developer) | 62032 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 372 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | 62004 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 373 | [Solido/awesome-flutter](https://github.com/Solido/awesome-flutter) | 61860 | 2026-09-03 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 374 | [pi-hole/pi-hole](https://github.com/pi-hole/pi-hole) | 61779 | 2026-11-07 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 375 | [microsoft/autogen](https://github.com/microsoft/autogen) | 61778 | 2026-10-28 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente/framework; autogen já citado. |
| 376 | [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) | 61599 | 2026-10-26 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 377 | [reduxjs/redux](https://github.com/reduxjs/redux) | 61440 | 2026-10-20 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 378 | [FuelLabs/sway](https://github.com/FuelLabs/sway) | 61344 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 379 | [sharkdp/bat](https://github.com/sharkdp/bat) | 61286 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 380 | [lodash/lodash](https://github.com/lodash/lodash) | 61267 | 2026-10-01 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 381 | [minio/minio](https://github.com/minio/minio) | 61262 | 2026-04-24 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 382 | [nuxt/nuxt](https://github.com/nuxt/nuxt) | 61061 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 383 | [rclone/rclone](https://github.com/rclone/rclone) | 60924 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 384 | [xingshaocheng/architect-awesome](https://github.com/xingshaocheng/architect-awesome) | 60852 | 2024-04-11 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 385 | [h5bp/Front-end-Developer-Interview-Questions](https://github.com/h5bp/Front-end-Developer-Interview-Questions) | 60847 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 386 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 60767 | 2026-10-19 | A | ALREADY_EVALUATED | `plain-writing` | Já avaliado (2026-09-21). |
| 387 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | 60743 | 2026-11-10 | D | ALREADY_EVALUATED | `crm-data-quality` | Já avaliado (2026-09-20). |
| 388 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 60740 | 2026-11-10 | A/D | ALREADY_EVALUATED | `multi-agent-orchestration` | Contrato expected_output já absorvido (AGENTS.md). |
| 389 | [atom/atom](https://github.com/atom/atom) | 60692 | 2023-01-03 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 390 | [starship/starship](https://github.com/starship/starship) | 60684 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 391 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | 60509 | 2026-11-09 | A/D | KEEP_EXTERNAL_REFERENCE | `agent-memory-engineering` | Memória com plugin Claude e alegação de benchmark; métodos já cobertos; benchmark não verificado. |
| 392 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 60445 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 393 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 60429 | 2026-09-07 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 394 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 60388 | 2026-10-07 | D | KEEP_EXTERNAL_REFERENCE | `—` | Clonagem de voz; só com consentimento da pessoa clonada. |
| 395 | [spring-projects/spring-framework](https://github.com/spring-projects/spring-framework) | 60313 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 396 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 60292 | 2026-11-10 | D | ALREADY_EVALUATED | `agent-memory-engineering` | Já avaliado. |
| 397 | [tiimgreen/github-cheat-sheet](https://github.com/tiimgreen/github-cheat-sheet) | 60276 | 2024-04-15 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |
| 398 | [adam-p/markdown-here](https://github.com/adam-p/markdown-here) | 60251 | 2025-08-22 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 399 | [CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) | 60237 | 2026-03-09 | D | KEEP_EXTERNAL_REFERENCE | `—` | Clonagem de voz; só com consentimento da pessoa clonada. |
| 400 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | 59975 | 2025-10-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou de referência. |

## Limites da validação
Triagem documental; só os SKILL.md citados foram lidos. Código, dependências e scripts não auditados.
