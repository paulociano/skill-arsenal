# GitHub Top 100 por estrelas: atualização (2026-11-10)

## Fonte e método
GitHub Search API, `stars:>1000 sort:stars order:desc`, páginas 1–2 de 50, consultada em 2026-11-10 via `gh api`. "Mais bem avaliados" foi interpretado como **mais estrelas**: o GitHub não tem nota de avaliação. Estrelas medem popularidade, não qualidade nem utilidade como skill.

Base de comparação: `evaluations/2026-10-22-github-top100-stars-triage.md` (100 triados, 96 READMEs lidos, 5 aprofundados). Esta atualização **não refaz** a triagem dos 97 repositórios que continuam no ranking; reaproveita a classe e a decisão de outubro e aprofunda apenas o que é novo.

Fluxo: `arsenal-autopilot` → `evaluate-and-import-skill` + `skill-security-review`. Nada instalado ou executado.

## O que mudou desde 2026-10-22
- **Entraram (3):** `TauricResearch/TradingAgents`, `earendil-works/pi`, `stablyai/orca`.
- **Saíram (3):** `2dust/v2rayN`, `godotengine/godot`, `justjavac/free-programming-books-zh_CN`.
- Distribuição atual: 40 D (software/runtime), 35 B (referência/catálogo), 24 A/D (método + runtime), 1 C.

## Repositórios novos

### TauricResearch/TradingAgents — A/D, UPDATE_EXISTING
- Evidência: README (framework, "Fundamentals as filed", "Current holdings", "Persistence", "Evaluating decisions over time", "Reproducibility"), `tradingagents/agents/` (analistas, bull/bear researchers, trader, debatedores de risco agressivo/neutro/conservador, portfolio manager), `dataflows/date_window.py`. Licença Apache-2.0. Não confundir com `TradingAgents-AI/TradingAgents`, triado em 2026-10-03.
- Delta: disciplina de dados no ponto do tempo (demonstrações como arquivadas, sem restatement posterior, sem cadastro atual em análise histórica, entrada no fechamento seguinte), identidade do ativo resolvida antes da análise, debate bull/bear seguido de três leituras de risco, distinção carteira vazia × não informada, liquidação de decisões por retorno realizado e alfa, e variação esperada entre execuções.
- Owner: `skills/investment-portfolio-analysis/SKILL.md`, seção "Dados no ponto do tempo, debate e checagem de decisões".
- Segurança: **CAUTION**. Chaves de vários provedores de LLM e dados de mercado; envia User-Agent ao SEC EDGAR; memória em `~/.tradingagents`. O próprio projeto declara uso de pesquisa, não recomendação. Não executar ordens.
- Instalar no Claude: não é skill. Para o seu trabalho, o método já está no Arsenal; o framework só se justificaria para pesquisa quantitativa com dados pagos.

### earendil-works/pi — D, KEEP_EXTERNAL_REFERENCE
- Evidência: README, `packages/` (agent, ai, coding-agent, codemode, durable…). Harness de agente de código mínimo e extensível (CLI, SDK, RPC), com skills, extensões e templates; sem subagentes nem plan mode por padrão. Já citado em avaliações anteriores (ECC tem adaptador `pi/`).
- Delta: nenhum método novo além de `coding-agent-engineering`. Alternativa ao Claude Code.
- Segurança: **CAUTION** (instalação `curl | sh`; npm sem pin transitivo).

### stablyai/orca — D, KEEP_EXTERNAL_REFERENCE
- Evidência: README. App desktop/mobile que orquestra vários agentes de código em paralelo, cada um em seu worktree, com coordenador, diffs, navegador e CLI.
- Delta: padrões já cobertos por `multi-agent-orchestration` e `git-worktree-lifecycle` (avaliação do sandcastle em 2026-10-23).
- Segurança: **CAUTION** (controla sessões autenticadas de vários agentes, acesso remoto).

## Instalar como skill no Claude
Entre os 100, os que são realmente skills/plugins instaláveis no Claude já estão instalados nesta conta ou absorvidos no Arsenal:
- `anthropics/skills` (docx, xlsx, pptx, pdf, skill-creator…), `obra/superpowers`, `mattpocock/skills`, `garrytan/gstack` (revisões CEO/eng, office hours), `DietrichGebert/ponytail` — **já instalados**.
- `multica-ai/andrej-karpathy-skills` — absorvido como `surgical-engineering`.
- `github/spec-kit`, `affaan-m/ECC` — reavaliados hoje; método absorvido, instalação não recomendada.
- `msitarzewski/agency-agents` — subagentes-persona para Claude Code; sobrepõem skills existentes.
Nenhuma instalação nova recomendada nesta rodada.

## Ranking atual com decisão vigente
Classe e decisão vêm da triagem de 2026-10-22 para os repositórios mantidos (`mantido`) e desta avaliação para os novos (`novo`). Decisões posteriores a outubro que alteram a tabela: `mattpocock/skills` (UPDATE_EXISTING, 2026-10-22), `github/spec-kit` e `affaan-m/ECC` (UPDATE_EXISTING, 2026-11-10).

| # | Repositório | Estrelas | Último push | Classe | Decisão | Owner | Status |
|---:|---|---:|---|---|---|---|---|
| 1 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 561594 | 2026-11-08 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 2 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 534826 | 2026-09-02 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | mantido |
| 3 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 497921 | 2026-11-07 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 4 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 458948 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 5 | [morluto/rea](https://github.com/morluto/rea) | 449750 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 6 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 401457 | 2026-11-07 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 7 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 394300 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 8 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | 377581 | 2026-09-15 | B | KEEP_EXTERNAL_REFERENCE | `system-design-engineering` | mantido |
| 9 | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 371756 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 10 | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | 364193 | 2026-11-07 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 11 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 335799 | 2026-11-07 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 12 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 333839 | 2026-11-08 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 13 | [mattpocock/skills](https://github.com/mattpocock/skills) | 320818 | 2026-11-09 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 14 | [obra/superpowers](https://github.com/obra/superpowers) | 315713 | 2026-11-03 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 15 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 300751 | 2026-11-09 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 16 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 289488 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 17 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 278157 | 2026-11-04 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 18 | [996icu/996.ICU](https://github.com/996icu/996.ICU) | 277233 | 2025-08-22 | C | KEEP_EXTERNAL_REFERENCE | `research-and-synthesize` | mantido |
| 19 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 262419 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 20 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | 257430 | 2024-11-19 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 21 | [torvalds/linux](https://github.com/torvalds/linux) | 255169 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 22 | [react/react](https://github.com/react/react) | 252492 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 23 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 231839 | 2026-04-20 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 24 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225996 | 2026-11-02 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 25 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 225889 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 26 | [vuejs/vue](https://github.com/vuejs/vue) | 212625 | 2024-10-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 27 | [ossu/computer-science](https://github.com/ossu/computer-science) | 211080 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 28 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 210016 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 29 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | 207765 | 2026-08-12 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 30 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 206709 | 2026-11-04 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 31 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 201444 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 200492 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 33 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | 198428 | 2026-10-17 | D | REJECT | `skill-security-review` | mantido |
| 34 | [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 196727 | 2026-07-26 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 35 | [microsoft/vscode](https://github.com/microsoft/vscode) | 195270 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 36 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 194797 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 37 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 194793 | 2026-11-07 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 38 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 193156 | 2026-11-06 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 39 | [anthropics/skills](https://github.com/anthropics/skills) | 192223 | 2026-11-06 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 40 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190435 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 41 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 188344 | 2026-10-29 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 42 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 188014 | 2026-10-31 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 43 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 187985 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 44 | [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) | 187790 | 2026-07-29 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 45 | [ollama/ollama](https://github.com/ollama/ollama) | 186566 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | mantido |
| 46 | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186477 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 47 | [getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS) | 184846 | 2026-10-31 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 48 | [flutter/flutter](https://github.com/flutter/flutter) | 181111 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 49 | [f/prompts.chat](https://github.com/f/prompts.chat) | 176840 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 50 | [github/gitignore](https://github.com/github/gitignore) | 176440 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 51 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 175038 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 52 | [huggingface/transformers](https://github.com/huggingface/transformers) | 168749 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 53 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 167650 | 2026-11-09 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 54 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 165287 | 2026-03-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 55 | [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) | 162735 | 2024-06-25 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 56 | [langgenius/dify](https://github.com/langgenius/dify) | 160880 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 57 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 159514 | 2026-10-25 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 58 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 158320 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 59 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 157629 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 60 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 156512 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 61 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 155201 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 62 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 154509 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 63 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 153329 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 64 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 149323 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 65 | [github/spec-kit](https://github.com/github/spec-kit) | 149195 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 66 | [airbnb/javascript](https://github.com/airbnb/javascript) | 148012 | 2026-04-16 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 67 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 147774 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `ui-ux-catalog` | mantido |
| 68 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 146173 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 69 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 145606 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 70 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 144602 | 2026-10-12 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 71 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 144367 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 72 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 143751 | 2026-11-10 | D | REJECT | `skill-security-review` | mantido |
| 73 | [vercel/next.js](https://github.com/vercel/next.js) | 143455 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 74 | [yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 143249 | 2026-08-07 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 75 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 142491 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 76 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 141963 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 77 | [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl) | 141526 | 2026-11-06 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 78 | [garrytan/gstack](https://github.com/garrytan/gstack) | 141097 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 79 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 140836 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 80 | [golang/go](https://github.com/golang/go) | 139837 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 81 | [labuladong/fucking-algorithm](https://github.com/labuladong/fucking-algorithm) | 136047 | 2026-10-18 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 82 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 135456 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 83 | [openai/codex](https://github.com/openai/codex) | 134763 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | mantido |
| 84 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 133949 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | mantido |
| 85 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 132154 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 86 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129481 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 87 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128983 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 88 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 128920 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 89 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 127843 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `ui-ux-catalog` | mantido |
| 90 | [react/react-native](https://github.com/react/react-native) | 126894 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 91 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 126477 | 2026-10-28 | B | KEEP_EXTERNAL_REFERENCE | `ui-ux-catalog` | mantido |
| 92 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | 125185 | 2026-10-27 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 93 | [electron/electron](https://github.com/electron/electron) | 123842 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 94 | [nodejs/node](https://github.com/nodejs/node) | 123464 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 95 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 123313 | 2026-11-05 | B | KEEP_EXTERNAL_REFERENCE | `teach` | mantido |
| 96 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 121869 | 2026-11-04 | A/D | UPDATE_EXISTING | `investment-portfolio-analysis` | novo |
| 97 | [rust-lang/rust](https://github.com/rust-lang/rust) | 121743 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | mantido |
| 98 | [stablyai/orca](https://github.com/stablyai/orca) | 121365 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `multi-agent-orchestration` | novo |
| 99 | [earendil-works/pi](https://github.com/earendil-works/pi) | 121241 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | novo |
| 100 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | 120586 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `computer-use-agent-engineering` | mantido |

## Limites da validação
Os três novos foram lidos em README, manifestos e arquivos citados; os demais 97 mantêm a evidência de outubro (README, sem auditoria de código). Nada instalado ou executado; dependências e código-fonte não auditados.
