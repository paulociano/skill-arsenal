# GitHub por estrelas, posições 101–200: triagem (2026-11-10)

## Fonte e método
GitHub Search API, `stars:>1000 sort:stars order:desc`, páginas 3–4 de 50, consultada em 2026-11-10 via `gh api`. Continuação de `evaluations/2026-11-10-github-top100-stars-update.md`. Estrelas medem popularidade, não qualidade. A ordem pode variar entre consultas.

Fluxo: `arsenal-autopilot` → `evaluate-and-import-skill` + `skill-security-review`. Nada instalado ou executado.

### Níveis de evidência
- **100/100 triados** por identidade, descrição, tipo de recurso e cruzamento com o Arsenal (21 já tinham registro em `evaluations/` ou `skills/`).
- **12 inspecionados** por clone sem blobs e contagem de `SKILL.md`: Understand-Anything, open-design, deer-flow, hello-agents, crawl4ai, worldmonitor, paperclip, OmniRoute, odysseus, MiroFish, modelcontextprotocol/servers, lobehub.
- **4 lidos em profundidade** (SKILL.md e licença): `deer-flow/skills/public/skill-reviewer` e `consulting-analysis`, `odysseus/resources/skills/agent/verified-state-change` e `communication/reviewable-external-draft`, `worldmonitor/claude-plugin/skills/world-brief`.
- Demais: classe provisória por descrição; não é análise de código.

## Achados
- **Distribuição:** 81 referência externa, 8 já avaliados antes, 3 já adotados (skills instaladas no Claude), 6 rejeitados, 1 com método já absorvido hoje (claude-mem), 1 atualização nova.
- A maioria dos `SKILL.md` encontrados é de **manutenção interna** do próprio repositório (`.agents/skills`, `.claude/skills`: triagem de issue, smoke test, PR) ou depende do runtime do produto (open-design, worldmonitor, Understand-Anything). Não são portáveis.

### Atualização aplicada
- **bytedance/deer-flow → `skills/skill-security-review/SKILL.md`** (MIT). O `skill-reviewer` separa *prontidão* (blocked / revise / publish_candidate) de *garantia* (static_only / trigger_checked / behavior_verified / regression_verified) e trata a skill revisada como dado não confiável. O Arsenal emitia APPROVE/CAUTION/REJECT sem declarar o nível de evidência; agora declara, e um APPROVE `static_only` não é tratado como prova de funcionamento.

### Lidos e não incorporados
- `deer-flow/consulting-analysis`: relatório de consultoria em duas fases (esqueleto + requisitos de dados por capítulo, depois relatório). Sobrepõe `research-and-synthesize`, `research-to-presentation` e `deep-research`; a regra "dado ausente = 'não disponível', nunca estimado" já está em `verify-before-claim`.
- `odysseus` (AGPL-3.0): `verified-state-change` (ler → mudar o mínimo → reler) e `reviewable-external-draft` (rascunho revisável, nunca enviar só porque a ferramenta permite) já estão cobertos por `agent-action-governance` e pelas regras de envio do Arsenal. Licença copyleft: não copiar texto.
- `worldmonitor` (AGPL-3.0): plugin Claude útil para briefing geopolítico, mas exige MCP do World Monitor (parte paga).

### Rejeitados
`2dust/v2rayN` e `fatedier/frp` (proxy/rede, fora de finalidade), `hacksider/Deep-Live-Cam` (deepfake), `sherlock-project/sherlock` (rastrear contas de pessoas por username), `cheaper-inference/OmniRoute` (gateway por centenas de provedores "free": credenciais e termos de uso), `nvbn/thefuck` (sem método, parado desde 2024).

## Instalar como skill no Claude
Nada novo recomendado. Os que são skills de fato já estão instalados (`caveman`, `impeccable`, `taste-skill` como `design-taste-frontend`) ou absorvidos (`addyosmani/agent-skills`, `archify`, `autoresearch`, `Scrapling`, `Agent-Reach`). Candidato condicional: o plugin `worldmonitor` no Claude Code, se você quiser briefing de geopolítica e mercado, aceitando a assinatura e a licença AGPL.

## Tabela
| # | Repositório | Estrelas | Último push | Classe | Decisão | Owner | Fundamentação |
|---:|---|---:|---|---|---|---|---|
| 101 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 120344 | 2026-11-10 | D | REJECT | `—` | Rede/proxy; fora da finalidade do Arsenal. |
| 102 | [godotengine/godot](https://github.com/godotengine/godot) | 119946 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `game-development-cycle` | Engine; já roteada pela stack de jogos. |
| 103 | [justjavac/free-programming-books-zh_CN](https://github.com/justjavac/free-programming-books-zh_CN) | 119559 | 2026-07-29 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 104 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 118872 | 2026-11-10 | A | ALREADY_ADOPTED | `caveman` | Já avaliado; skills caveman instaladas no Claude. |
| 105 | [immich-app/immich](https://github.com/immich-app/immich) | 118730 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 106 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 118212 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; radar de descoberta, cada item exige avaliação própria. |
| 107 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 118075 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 108 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 115784 | 2026-11-10 | D | ABSORB_METHOD_ONLY | `agent-memory-engineering` | Avaliado em 2026-11-10. |
| 109 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 115087 | 2026-11-01 | A | ALREADY_EVALUATED | `software-engineering-cycle` | Já citado em 3 registros do Arsenal. |
| 110 | [supabase/supabase](https://github.com/supabase/supabase) | 114755 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 111 | [d3/d3](https://github.com/d3/d3) | 113900 | 2026-11-03 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 112 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 112972 | 2026-11-08 | A | ALREADY_ADOPTED | `web-design-engineer` | design-taste-frontend instalada no Claude. |
| 113 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 112913 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `agent-action-governance` | Plataforma/workspace de agentes; SKILL.md internos de manutenção ou dependentes do runtime. Odysseus: AGPL-3.0, verified-state-change já coberto. |
| 114 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 112673 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 115 | [openai/whisper](https://github.com/openai/whisper) | 112368 | 2026-08-31 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 116 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111872 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 117 | [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | 111395 | 2026-10-28 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 118 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 110895 | 2026-11-08 | D | ALREADY_EVALUATED | `web-extraction-pipeline` | Método já absorvido. |
| 119 | [fatedier/frp](https://github.com/fatedier/frp) | 110516 | 2026-11-10 | D | REJECT | `—` | Rede/proxy; fora da finalidade do Arsenal. |
| 120 | [axios/axios](https://github.com/axios/axios) | 109301 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 121 | [denoland/deno](https://github.com/denoland/deno) | 108952 | 2026-10-29 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 122 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 108840 | 2026-11-10 | D | REJECT | `—` | OSINT de contas por username; risco de rastreamento de pessoa privada. |
| 123 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 108765 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente de código/harness; alternativa ao Claude Code. |
| 124 | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 108195 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 125 | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 107894 | 2026-11-08 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 126 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 107544 | 2026-11-10 | A | ALREADY_ADOPTED | `web-design-engineer` | Método já absorvido; skill instalada no Claude. |
| 127 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 107174 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 128 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 107021 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `web-design-engineer` | Workspace de design com ~560 templates SKILL.md acoplados ao app. |
| 129 | [goldbergyoni/nodebestpractices](https://github.com/goldbergyoni/nodebestpractices) | 105722 | 2026-06-15 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 130 | [microsoft/terminal](https://github.com/microsoft/terminal) | 105365 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 131 | [pytorch/pytorch](https://github.com/pytorch/pytorch) | 105330 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 132 | [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | 104794 | 2025-08-28 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Pesos/modelo. |
| 133 | [fastapi/fastapi](https://github.com/fastapi/fastapi) | 104625 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 134 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 103866 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 135 | [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 103825 | 2026-10-26 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 136 | [neovim/neovim](https://github.com/neovim/neovim) | 103558 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 137 | [react/create-react-app](https://github.com/react/create-react-app) | 103232 | 2025-02-15 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 138 | [angular/angular](https://github.com/angular/angular) | 101467 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 139 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 101088 | 2026-11-09 | D | ALREADY_EVALUATED | `web-extraction-pipeline` | Método já absorvido. |
| 140 | [mtdvio/every-programmer-should-know](https://github.com/mtdvio/every-programmer-should-know) | 100646 | 2025-12-29 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 141 | [ant-design/ant-design](https://github.com/ant-design/ant-design) | 100145 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 142 | [microsoft/playwright](https://github.com/microsoft/playwright) | 99794 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `runtime-ui-verification` | Ferramenta de automação de navegador já referenciada. |
| 143 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 99750 | 2026-03-26 | A/D | ALREADY_EVALUATED | `empirical-prompt-tuning` | Protocolo Autoresearch já absorvido. |
| 144 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 99338 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 145 | [mui/material-ui](https://github.com/mui/material-ui) | 99315 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 146 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 98673 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 147 | [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) | 98534 | 2025-10-11 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 148 | [localsend/localsend](https://github.com/localsend/localsend) | 98265 | 2026-11-08 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 149 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 98033 | 2026-09-24 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 150 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | 97960 | 2026-11-08 | D | REJECT | `—` | Deepfake facial em tempo real; risco de abuso. |
| 151 | [nvbn/thefuck](https://github.com/nvbn/thefuck) | 97951 | 2024-07-19 | C | REJECT | `—` | Utilitário de terminal sem método; sem push desde 2024. |
| 152 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 97576 | 2026-11-06 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; radar de descoberta, cada item exige avaliação própria. |
| 153 | [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 97120 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 154 | [oven-sh/bun](https://github.com/oven-sh/bun) | 96747 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 155 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 96688 | 2026-11-10 | D | ALREADY_EVALUATED | `local-llm-inference-engineering` | Já avaliado. |
| 156 | [3b1b/manim](https://github.com/3b1b/manim) | 96329 | 2026-09-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 157 | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 96217 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 158 | [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | 95821 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `runtime-ui-verification` | Ferramenta de automação de navegador já referenciada. |
| 159 | [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 95789 | 2026-11-04 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 160 | [odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus) | 95559 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `agent-action-governance` | Plataforma/workspace de agentes; SKILL.md internos de manutenção ou dependentes do runtime. Odysseus: AGPL-3.0, verified-state-change já coberto. |
| 161 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 95361 | 2026-11-10 | A | ALREADY_EVALUATED | `architecture-visualization` | Já citado em 3 registros. |
| 162 | [iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns) | 94856 | 2026-10-08 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 163 | [ryanmcdermott/clean-code-javascript](https://github.com/ryanmcdermott/clean-code-javascript) | 94689 | 2024-07-29 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 164 | [zed-industries/zed](https://github.com/zed-industries/zed) | 94673 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 165 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 93968 | 2026-11-10 | D | ALREADY_EVALUATED | `agent-memory-engineering` | RAG engine já referenciado. |
| 166 | [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) | 93466 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 167 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 93146 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente de código/harness; alternativa ao Claude Code. |
| 168 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 92535 | 2026-09-16 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 169 | [home-assistant/core](https://github.com/home-assistant/core) | 92128 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 170 | [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 92108 | 2026-11-07 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 171 | [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) | 92013 | 2025-06-27 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Pesos/modelo. |
| 172 | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 91914 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `ai-workflow-automation-engineering` | Servidores MCP de referência; instalar caso a caso. |
| 173 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 91871 | 2026-11-09 | A/D | KEEP_EXTERNAL_REFERENCE | `knowledge-graph-engineering` | Plugin com 9 skills que geram grafo do código; dependem do runtime; AGPL-3.0. |
| 174 | [astral-sh/uv](https://github.com/astral-sh/uv) | 91857 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 175 | [django/django](https://github.com/django/django) | 91704 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 176 | [opencv/opencv](https://github.com/opencv/opencv) | 91523 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 177 | [storybookjs/storybook](https://github.com/storybookjs/storybook) | 91520 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 178 | [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) | 91264 | 2026-10-01 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 179 | [ByteByteGoHq/system-design-101](https://github.com/ByteByteGoHq/system-design-101) | 91102 | 2025-04-04 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 180 | [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | 91070 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 181 | [bitcoin/bitcoin](https://github.com/bitcoin/bitcoin) | 90652 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 182 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | 90456 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `signal-intelligence-digest` | Plugin Claude depende de MCP pago do World Monitor; regras de corroboração já cobertas. |
| 183 | [gohugoio/hugo](https://github.com/gohugoio/hugo) | 90437 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 184 | [syncthing/syncthing](https://github.com/syncthing/syncthing) | 90324 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 185 | [PanJiaChen/vue-element-admin](https://github.com/PanJiaChen/vue-element-admin) | 90110 | 2024-10-24 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 186 | [gin-gonic/gin](https://github.com/gin-gonic/gin) | 89617 | 2026-10-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 187 | [ChatGPTNextWeb/NextChat](https://github.com/ChatGPTNextWeb/NextChat) | 88948 | 2026-10-20 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 188 | [sveltejs/svelte](https://github.com/sveltejs/svelte) | 88695 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 189 | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | 87191 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `web-extraction-pipeline` | Crawler/API; sem SKILL.md; padrões já cobertos. |
| 190 | [bregman-arie/devops-exercises](https://github.com/bregman-arie/devops-exercises) | 86704 | 2025-12-27 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 191 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 86622 | 2026-10-13 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 192 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 86273 | 2026-11-10 | D | REJECT | `—` | Gateway que roteia tráfego por centenas de provedores 'free'; risco de credenciais e termos de uso. |
| 193 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 86107 | 2026-11-10 | D | ALREADY_EVALUATED | `codex-cost-efficiency` | Já avaliado (2026-09-21). |
| 194 | [DopplerHQ/awesome-interview-questions](https://github.com/DopplerHQ/awesome-interview-questions) | 85494 | 2024-07-29 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 195 | [laravel/laravel](https://github.com/laravel/laravel) | 85398 | 2026-10-30 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 196 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 85222 | 2026-11-10 | A/D | UPDATE_EXISTING | `skill-security-review` | Harness de longo prazo; skill-reviewer trouxe separação prontidão × garantia. |
| 197 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | 85208 | 2026-10-16 | D | KEEP_EXTERNAL_REFERENCE | `scenario-forecasting` | Simulação por enxame de agentes para 'prever qualquer coisa'; alegação sem validação. |
| 198 | [macrozheng/mall](https://github.com/macrozheng/mall) | 85031 | 2026-09-15 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 199 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 85031 | 2026-02-05 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou catálogo; consultar na fonte quando pertinente. |
| 200 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | 84859 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `agent-action-governance` | Plataforma/workspace de agentes; SKILL.md internos de manutenção ou dependentes do runtime. Odysseus: AGPL-3.0, verified-state-change já coberto. |

## Limites da validação
Triagem documental. Só os 4 SKILL.md citados foram lidos inteiros; código, dependências e scripts não auditados.
