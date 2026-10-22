# GitHub Top 100 por estrelas: triagem de oportunidades para skills (2026-10-22)

## Fonte e método
Consulta ao GitHub Search de repositórios: `stars:>10000 sort:stars-desc`, página 1, tamanho 100, em 2026-10-22. A ordem é **a ordem retornada pela consulta**, não uma avaliação qualitativa. O conector não forneceu números de estrelas neste resultado; portanto, nenhum número foi inventado. A busca é dinâmica e rankings podem mudar. Repositórios arquivados, forks, critérios de popularidade e flutuações da busca podem afetar o conjunto. URLs são as fontes originais.

Fonte canônica do Arsenal: `ARSENAL INDEX.md`; stack: `stacks/arsenal-autopilot/STACK.md`.

### Dois níveis de evidência
- **100/100 triados** por identidade do repositório, tipo de recurso e encaixe preliminar com owners do Arsenal.
- **15/100 inspecionados pelo README** para testar candidatos prioritários: openclaw/openclaw, obra/superpowers, mattpocock/skills, affaan-m/ECC, deepseek-ai/deepseek-harness, NousResearch/hermes-agent, multica-ai/andrej-karpathy-skills, firecrawl/firecrawl, msitarzewski/agency-agents, Shubhamsaboo/awesome-llm-apps, github/spec-kit, nextlevelbuilder/ui-ux-pro-max-skill, garrytan/gstack, ggml-org/llama.cpp e browser-use/browser-use. Para os demais, a classe é **provisória** e não é análise do código ou manifesto.

**Classes:** A (comportamento de skill potencial), B (metodologia/referência), C (pouco incremento de skill), D (sistema técnico/runtime). A/D significa método potencial + execução dependente de ferramentas.

**Atenção:** A classificação preliminar NÃO indica aprovação de segurança, compatibilidade, licença ou qualidade de produção. Não executar scripts, instalar pacotes, conceder permissões, copiar código ou afirmar disponibilidade de runtime a partir desta tabela.

## Ranking e triagem individual

| # | Repositório | Classe | Decisão preliminar | Owner proposto | Fundamentação |
|---:|---|---|---|---|---|
| 1 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Referência já avaliada/incorporada no Arsenal; evitar duplicação. |
| 2 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo: radar de descoberta; exige resolver cada fonte primária antes de avaliar. |
| 3 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 4 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 5 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 6 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 7 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | B | KEEP_EXTERNAL_REFERENCE | `system-design-engineering` | Referência já avaliada/incorporada no Arsenal; evitar duplicação. |
| 8 | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 9 | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 10 | [morluto/rea](https://github.com/morluto/rea) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 11 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Referência já avaliada/incorporada no Arsenal; evitar duplicação. |
| 12 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 13 | [obra/superpowers](https://github.com/obra/superpowers) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Biblioteca composicional de skills para coding agents; comparar com fluxos existentes e não executar instaladores. |
| 14 | [mattpocock/skills](https://github.com/mattpocock/skills) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 15 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Referência já avaliada/incorporada no Arsenal; evitar duplicação. |
| 16 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Harness/kit de agente; integração depende do ambiente, permissões e controles do agente. |
| 17 | [996icu/996.ICU](https://github.com/996icu/996.ICU) | C | KEEP_EXTERNAL_REFERENCE | `research-and-synthesize` | Iniciativa de conscientização, não metodologia de skill operacional. |
| 18 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 19 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 20 | [torvalds/linux](https://github.com/torvalds/linux) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 21 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 22 | [react/react](https://github.com/react/react) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 23 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 24 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 25 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 26 | [vuejs/vue](https://github.com/vuejs/vue) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 27 | [ossu/computer-science](https://github.com/ossu/computer-science) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 28 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 29 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 30 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 31 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 32 | [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 33 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | D | REJECT | `skill-security-review` | Fora da finalidade do Arsenal como metodologia reutilizável; conteúdo/execução requer cautela legal e de segurança. |
| 34 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 35 | [microsoft/vscode](https://github.com/microsoft/vscode) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 36 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 37 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 38 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 39 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 40 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 41 | [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 42 | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 43 | [getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 44 | [ollama/ollama](https://github.com/ollama/ollama) | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Infraestrutura de inferência local, dependente de hardware, desempenho e runtime. |
| 45 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 46 | [anthropics/skills](https://github.com/anthropics/skills) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 47 | [flutter/flutter](https://github.com/flutter/flutter) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 48 | [github/gitignore](https://github.com/github/gitignore) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 49 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 50 | [f/prompts.chat](https://github.com/f/prompts.chat) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 51 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 52 | [huggingface/transformers](https://github.com/huggingface/transformers) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 53 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 54 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 55 | [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 56 | [langgenius/dify](https://github.com/langgenius/dify) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 57 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 58 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 59 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 60 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 61 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 62 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 63 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 64 | [airbnb/javascript](https://github.com/airbnb/javascript) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 65 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 66 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 67 | [vercel/next.js](https://github.com/vercel/next.js) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 68 | [yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 69 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 70 | [github/spec-kit](https://github.com/github/spec-kit) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Fluxo de desenvolvimento guiado por especificação; metodologia potencial, mas exigir ganho comprovado sobre task contracts existentes. |
| 71 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | D | REJECT | `skill-security-review` | Fora da finalidade do Arsenal como metodologia reutilizável; conteúdo/execução requer cautela legal e de segurança. |
| 72 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 73 | [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 74 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 75 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 76 | [golang/go](https://github.com/golang/go) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 77 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | B | KEEP_EXTERNAL_REFERENCE | `ui-ux-catalog` | Catálogo/componentes UI; a curadoria já possui owner; não confundir com skill autônoma. |
| 78 | [garrytan/gstack](https://github.com/garrytan/gstack) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 79 | [labuladong/fucking-algorithm](https://github.com/labuladong/fucking-algorithm) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 80 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 81 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 82 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 83 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Infraestrutura de inferência local, dependente de hardware, desempenho e runtime. |
| 84 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 85 | [openai/codex](https://github.com/openai/codex) | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente, harness ou instruções operacionais; potencial metodológico, mas requer revisão de permissões, sobreposição e runtime. |
| 86 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 87 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 88 | [react/react-native](https://github.com/react/react-native) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 89 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 90 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | D | KEEP_EXTERNAL_REFERENCE | `ui-ux-catalog` | Catálogo/componentes UI; a curadoria já possui owner; não confundir com skill autônoma. |
| 91 | [electron/electron](https://github.com/electron/electron) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 92 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 93 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | B | KEEP_EXTERNAL_REFERENCE | `ui-ux-catalog` | Catálogo/componentes UI; a curadoria já possui owner; não confundir com skill autônoma. |
| 94 | [nodejs/node](https://github.com/nodejs/node) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 95 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 96 | [rust-lang/rust](https://github.com/rust-lang/rust) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 97 | [justjavac/free-programming-books-zh_CN](https://github.com/justjavac/free-programming-books-zh_CN) | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material ou catálogo educacional/de referência; usar na fonte primária quando pertinente, sem importar em massa. |
| 98 | [godotengine/godot](https://github.com/godotengine/godot) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |
| 99 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | A/D | KEEP_EXTERNAL_REFERENCE | `computer-use-agent-engineering` | Automação do navegador exige runtime, isolamento, autorização e avaliação observável. |
| 100 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software/runtime completo; não é uma skill portátil nem deve ser instalado automaticamente. |

## Shortlist para aprofundamento
1. `obra/superpowers`: comparar sequência brainstorm/plan/test/review com `software-engineering-cycle` e `coding-agent-engineering`; provar diferença em casos com/sem necessidade de planejamento. Sem instalar extensões.
2. `mattpocock/skills`: identificar skills individuais úteis e contrastar seus contratos com owners existentes; o repositório como um todo não é uma skill.
3. `github/spec-kit`: buscar etapa de especificação verificável que não esteja já no `task contract` de `coding-agent-engineering`.
4. `browser-use/browser-use`: inspeção técnica orientada a computer-use, autorização, proteção contra prompt injection e recuperação de execução.
5. `deepseek-ai/deepseek-harness`: README declara developer preview e mudanças incompatíveis; apenas referência de arquitetura de plugins até validar maturidade.
6. `ggml-org/llama.cpp`: referência técnica para inferência local; não instalar e não supor disponibilidade de CPU/GPU.
7. `affaan-m/ECC`, `openclaw/openclaw`, `NousResearch/hermes-agent` e `garrytan/gstack`: comparar agentes e workflows com owner de coding agents e limites de autonomia.

## Compatibilidade, sobreposição e segurança
- O índice já contém `coding-agent-engineering`, `computer-use-agent-engineering`, `local-llm-inference-engineering`, `system-design-engineering`, `teach` e `ui-ux-catalog`. Evitar criar uma skill por repositório.
- Os recursos de `build-your-own-x`, `system-design-primer`, `awesome-python` e `project-based-learning` já tinham sido avaliados em 2026-10-22; esta triagem não os reinstala.
- A maior parte do ranking é código/produto/ecossistema ou coletânea, não uma skill invocável. Tratar dependências, APIs externas, credenciais e instaladores como não avaliados.
- Apenas após abrir fonte primária mais específica (`SKILL.md`, workflow, licença e scripts) pode-se transformar uma hipótese em UPDATE_EXISTING/CREATE_NEW. Avaliação não equivale a aprovação automática.

## Resultado e limite de execução
Esta entrega implementa uma **triagem completa dos 100 nomes**, não 100 auditorias profundas. Nesta etapa não foi identificado um delta comprovado que justifique alterar owners canônicos com segurança, especialmente porque os principais candidatos já têm owners de função no Arsenal. Por isso a decisão conservadora é **KEEP_EXTERNAL_REFERENCE**, até aprofundamento, salvo rejeições explícitas. Não criar skill artificial para satisfazer quantidade.

Arquivos afetados: apenas este registro em `evaluations/`. Nenhuma instalação de terceiros. Validação: conferir que há exatamente 100 linhas classificadas e que a branch alvo contém o documento publicado.


## Aprofundamento 1: 2026-10-22

Fontes consultadas diretamente:
- `mattpocock/skills`: README e `skills/engineering/grill-with-docs/SKILL.md`, que delega a skills internas `grilling` e `domain-modeling`. O método de vocabulário comum e ADR foi extraído do README; não foi executada a cadeia de skills ou instalador.
- `obra/superpowers`: README; execução de conjunto de skills permanece dependente de instalação e tools de cada agente.
- `github/spec-kit`: README; fluxos de especificação, bug assessment/fix/test e ideia go/clarify/stop com extensões CLI. Sobreposição significativa com owners existentes, sem delta comprovado.
- `browser-use/browser-use`: README; execução depende de Python, browser/CDP/cloud/API keys, já coberta como referência por `computer-use-agent-engineering`.
- `deepseek-ai/deepseek-harness`: README; declara preview, incompatibilidades futuras e arquitetura por plugins. Mantido como referência arquitetural, sem instalar.

### Decisões finais deste aprofundamento
| Fonte | Classificação | Decisão | Evidência/owner |
| --- | --- | --- | --- |
| mattpocock/skills (glossário/ADR) | B | UPDATE_EXISTING | `skills/coding-agent-engineering/SKILL.md`: seção vocabulário e decisões duráveis, com should-trigger e near-miss; absorção metodológica efetiva |
| obra/superpowers | B/D | KEEP_EXTERNAL_REFERENCE | Workflow composicional já amplamente representado por `software-engineering-cycle`, `tdd`, `code-review` |
| github/spec-kit | B/D | KEEP_EXTERNAL_REFERENCE | Contracts, diagnóstico/bugfix e check de comportamento já roteados pelo Arsenal; CLI não portátil por pressuposição |
| browser-use/browser-use | D | KEEP_EXTERNAL_REFERENCE | Owner `computer-use-agent-engineering` já inclui a fonte; sem nova lacuna identificada |
| deepseek-ai/deepseek-harness | D | KEEP_EXTERNAL_REFERENCE | Preview com breaking changes; não adotar runtime em avaliação estática |

### Revisão de segurança e portabilidade
Somente leituras documentais; nenhum `npx`, `uv`, extensão, script, CLI ou conexão externa executados. `mattpocock` declara comandos de instalação e habilidades específicas de agente que não foram transportadas; absorvida apenas metodologia de nomenclatura/documentação. Browser agents envolvem credenciais, sessões, navegação e efeitos externos; harnesses de plugins têm superfície extensível privilegiada. **Veredito:** APPROVE para metodologia absorvida; CAUTION para execução de sistemas terceiros. Não é auditoria de supply chain, código nem de todos os 100 repos.

### Evidência da implementação
- Arquivo alterado: `skills/coding-agent-engineering/SKILL.md`.
- Branch: `eval/github-top100-stars-20261022`.
- Sem nova skill ou mudança material de description: índice preservado.
- Critérios de aceitação: seção de glossário/ADR presente, includes should-trigger e near-miss, sem dependência externa obrigatória; read-after-write, diff contra master e 100 entradas da triagem preservadas.


## Aprofundamento 2: fechamento da leitura do Top 100 (2026-10-22)

Foram solicitados os 100 READMEs da captura original. **96 retornaram conteúdo e 4 falharam**: `sindresorhus/awesome`, `nilbuild/developer-roadmap`, `torvalds/linux` e `vercel/next.js`. Trata-se de avaliação documental em nível README, não auditoria de 100 codebases, dependências, licenças ou scripts. A/B/C/D da tabela inicial permanece classificação operacional preliminar quando não houve análise de subarquivos.

| Rank | Repositório | README | Decisão pós-triagem | Owner sugerido |
|---:|---|---|---|---|
| 1 | `codecrafters-io/build-your-own-x` | Lido | ALREADY_COVERED | `teach` |
| 2 | `sindresorhus/awesome` | Falhou | LIMITED_NO_README | `arsenal-autopilot` |
| 3 | `public-apis/public-apis` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 4 | `freeCodeCamp/freeCodeCamp` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 5 | `EbookFoundation/free-programming-books` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 6 | `openclaw/openclaw` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 7 | `donnemartin/system-design-primer` | Lido | ALREADY_COVERED | `system-design-engineering` |
| 8 | `nilbuild/developer-roadmap` | Falhou | LIMITED_NO_README | `teach` |
| 9 | `jwasham/coding-interview-university` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 10 | `morluto/rea` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 11 | `vinta/awesome-python` | Lido | ALREADY_COVERED | `teach` |
| 12 | `awesome-selfhosted/awesome-selfhosted` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 13 | `obra/superpowers` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 14 | `mattpocock/skills` | Lido | UPDATE_EXISTING | `coding-agent-engineering` |
| 15 | `practical-tutorials/project-based-learning` | Lido | ALREADY_COVERED | `teach` |
| 16 | `affaan-m/ECC` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 17 | `996icu/996.ICU` | Lido | KEEP_EXTERNAL_REFERENCE | `research-and-synthesize` |
| 18 | `deepseek-ai/deepseek-harness` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 19 | `NousResearch/hermes-agent` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 20 | `torvalds/linux` | Falhou | LIMITED_NO_README | `software-engineering-cycle` |
| 21 | `trimstray/the-book-of-secret-knowledge` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 22 | `react/react` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 23 | `TheAlgorithms/Python` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 24 | `multica-ai/andrej-karpathy-skills` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 25 | `anomalyco/opencode` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 26 | `vuejs/vue` | Lido | LEGACY_REFERENCE | `software-engineering-cycle` |
| 27 | `ossu/computer-science` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 28 | `n8n-io/n8n` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 29 | `DigitalPlatDev/FreeDomain` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 30 | `tensorflow/tensorflow` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 31 | `yt-dlp/yt-dlp` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 32 | `trekhleb/javascript-algorithms` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 33 | `massgravel/Microsoft-Activation-Scripts` | Lido | DO_NOT_IMPORT | `skill-security-review` |
| 34 | `ultraworkers/claw-code` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 35 | `microsoft/vscode` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 36 | `firecrawl/firecrawl` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 37 | `microsoft/markitdown` | Lido | UPDATE_EXISTING | `software-engineering-cycle` |
| 38 | `ohmyzsh/ohmyzsh` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 39 | `avelino/awesome-go` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 40 | `Significant-Gravitas/AutoGPT` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 41 | `jackfrued/Python-100-Days` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 42 | `CyC2018/CS-Notes` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 43 | `getify/You-Dont-Know-JS` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 44 | `ollama/ollama` | Lido | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` |
| 45 | `521xueweihan/HelloGitHub` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 46 | `anthropics/skills` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 47 | `flutter/flutter` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 48 | `github/gitignore` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 49 | `twbs/bootstrap` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 50 | `f/prompts.chat` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 51 | `DietrichGebert/ponytail` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 52 | `huggingface/transformers` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 53 | `AUTOMATIC1111/stable-diffusion-webui` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 54 | `msitarzewski/agency-agents` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 55 | `jlevy/the-art-of-command-line` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 56 | `langgenius/dify` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 57 | `Snailclimb/JavaGuide` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 58 | `open-webui/open-webui` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 59 | `langflow-ai/langflow` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 60 | `clash-verge-rev/clash-verge-rev` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 61 | `Genymobile/scrcpy` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 62 | `anthropics/claude-code` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 63 | `langchain-ai/langchain` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 64 | `airbnb/javascript` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 65 | `farion1231/cc-switch` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 66 | `x1xhlol/system-prompts-and-models-of-ai-tools` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 67 | `vercel/next.js` | Falhou | LIMITED_NO_README | `software-engineering-cycle` |
| 68 | `yangshun/tech-interview-handbook` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 69 | `Shubhamsaboo/awesome-llm-apps` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 70 | `github/spec-kit` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 71 | `iptv-org/iptv` | Lido | DO_NOT_IMPORT | `skill-security-review` |
| 72 | `Comfy-Org/ComfyUI` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 73 | `ytdl-org/youtube-dl` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 74 | `ripienaar/free-for-dev` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 75 | `microsoft/PowerToys` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 76 | `golang/go` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 77 | `nextlevelbuilder/ui-ux-pro-max-skill` | Lido | ALREADY_COVERED | `ui-ux-catalog` |
| 78 | `garrytan/gstack` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 79 | `labuladong/fucking-algorithm` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 80 | `excalidraw/excalidraw` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 81 | `harry0703/MoneyPrinterTurbo` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 82 | `Graphify-Labs/graphify` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 83 | `ggml-org/llama.cpp` | Lido | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` |
| 84 | `krahets/hello-algo` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 85 | `openai/codex` | Lido | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` |
| 86 | `Chalarangelo/30-seconds-of-code` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 87 | `kubernetes/kubernetes` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 88 | `react/react-native` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 89 | `rustdesk/rustdesk` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 90 | `shadcn-ui/ui` | Lido | KEEP_EXTERNAL_REFERENCE | `ui-ux-catalog` |
| 91 | `electron/electron` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 92 | `Hack-with-Github/Awesome-Hacking` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 93 | `VoltAgent/awesome-design-md` | Lido | KEEP_EXTERNAL_REFERENCE | `ui-ux-catalog` |
| 94 | `nodejs/node` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 95 | `microsoft/generative-ai-for-beginners` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 96 | `rust-lang/rust` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 97 | `justjavac/free-programming-books-zh_CN` | Lido | KEEP_EXTERNAL_REFERENCE | `teach` |
| 98 | `godotengine/godot` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |
| 99 | `browser-use/browser-use` | Lido | ALREADY_COVERED | `computer-use-agent-engineering` |
| 100 | `2dust/v2rayN` | Lido | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` |

### Resultados concretos

- `microsoft/markitdown`: o README ressalta que opera I/O com privilégios do processo. **UPDATE_EXISTING** em `skills/document-extraction-pipeline/SKILL.md`, adicionando limites de execução, rede, plugins, pastas e tratamento de fontes não confiáveis. Sem instalar MarkItDown.
- `mattpocock/skills`: incorporado anteriormente nesta branch, com glossário de domínio e ADR em `skills/coding-agent-engineering/SKILL.md`.
- `vuejs/vue`: o README declara o Vue 2 em fim de vida e aponta `vuejs/core` como versão corrente; popularidade não serve para recomendar runtime legado.
- `github/spec-kit`, `obra/superpowers`, `browser-use/browser-use`, `deepseek-ai/deepseek-harness`: referências aprofundadas anteriormente, com sobreposição em owners existentes e/ou runtime externo.
- Os quatro casos sem README mantêm somente classificação inicial fundamentada no ranking e identidade; **não foram avaliados profundamente**.

### Segurança e validade

Nenhum instalador, pacote, script, CLI, agente, plugin ou extensão da lista foi executado. A leitura documental não prova segurança, atualidade de cada dependência, licença redistribuível ou desempenho. Catálogos são radar; código e runtimes precisam de avaliação na fonte específica antes de serem executados. `KEEP_EXTERNAL_REFERENCE` não significa aprovação de segurança.

**Resultado deste lote:** 100/100 identificados e classificados, 96/100 READMEs efetivamente consultados, 4 leituras indisponíveis e dois owners enriquecidos com métodos portáveis e concretos. Não houve criação de skills artificiais. Arquivos alterados na branch: esta avaliação, `skills/coding-agent-engineering/SKILL.md` e `skills/document-extraction-pipeline/SKILL.md`. Índice preservado pois owners e descriptions não mudaram. Validação documental posterior verificará a contagem, a presença dos métodos e o diff da branch.
