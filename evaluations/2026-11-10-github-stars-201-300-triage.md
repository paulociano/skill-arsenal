# GitHub por estrelas, posições 201–300: triagem (2026-11-10)

## Fonte e método
GitHub Search API, `stars:>1000 sort:stars order:desc`, páginas 5–6 de 50, consultada em 2026-11-10 via `gh api` (a página 5 retornou HTTP 502 na primeira tentativa e foi repetida). Continuação de `2026-11-10-github-stars-101-200-triage.md`. Estrelas medem popularidade, não qualidade.

Fluxo: `arsenal-autopilot` → `evaluate-and-import-skill` + `skill-security-review`. Nada instalado ou executado. Nível de garantia de todas as decisões: `static_only`.

### Níveis de evidência
- **100/100 triados** por identidade, descrição e cruzamento com o Arsenal (16 já tinham registro).
- **9 inspecionados** por clone sem blobs e listagem de `SKILL.md`: ppt-master, OpenBB, strix, OpenSpec, career-ops, learn-claude-code, OpenMontage, codegraph, oh-my-openagent.
- **2 lidos em profundidade**: `usestrix/strix/skills/find-security-vulnerabilities-in-code` (Apache-2.0) e `Fission-AI/OpenSpec/skills/openspec-archive-change` + lista das 12 skills (MIT).
- Demais: classe provisória por descrição.

## Atualizações aplicadas
- **Fission-AI/OpenSpec → `skills/to-spec/SKILL.md`**: specs vigentes por capacidade e cada mudança numa pasta com proposta, tarefas e só o delta (adicionado/modificado/removido); ao concluir, mesclar e arquivar. Complementa o que veio do spec-kit (que cria uma spec por feature nova, não deltas sobre sistema existente).
- **usestrix/strix → `skills/web-application-security-audit/SKILL.md`**: declarar modelo de tenancy, fronteiras de confiança e entradas do atacante antes de auditar; varredura sem achados ≠ código limpo (registrar orçamento e caminhos não revisados); corrigir na causa compartilhada e repetir a exploração.

## Rejeitados
`Z4nzu/hackingtool` (coleção de ferramentas de ataque sem método), `asgeirtj/system_prompts_leaks` (prompts vazados de terceiros), `NanmiCoder/MediaCrawler` (raspagem de redes sociais contornando proteções).

## Instalar como skill no Claude
Nada novo recomendado:
- `ppt-master`: gera PPTX nativo, mas você já tem o tipo Slides (exporta .pptx) e a skill `pptx`.
- `OpenBB`: só se você quiser um provedor de dados de mercado via MCP no Claude Code; as skills ensinam a operar o OpenBB, não análise.
- `strix`: exige Docker, chave de LLM e roda exploração real; só em projeto próprio com sandbox.
- `OpenSpec`: método absorvido; o CLI só se valer para um projeto de código específico.
- Já instalados/conectados: Remotion (skills) e HyperFrames (MCP).

## Tabela
| # | Repositório | Estrelas | Último push | Classe | Decisão | Owner | Fundamentação |
|---:|---|---:|---|---|---|---|---|
| 201 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | 84802 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 202 | [fighting41love/funNLP](https://github.com/fighting41love/funNLP) | 84505 | 2024-05-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Coletânea de recursos de NLP em chinês; parada desde 2024. |
| 203 | [realworld-apps/realworld](https://github.com/realworld-apps/realworld) | 84376 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 204 | [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 84335 | 2026-10-26 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 205 | [junegunn/fzf](https://github.com/junegunn/fzf) | 84137 | 2026-11-07 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 206 | [vitejs/vite](https://github.com/vitejs/vite) | 83925 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 207 | [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit) | 83805 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 208 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | 83452 | 2026-11-10 | D | ALREADY_EVALUATED | `document-extraction-pipeline` | Conversão de documentos para LLM já avaliada. |
| 209 | [animate-css/animate.css](https://github.com/animate-css/animate.css) | 82978 | 2024-07-29 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 210 | [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | 82566 | 2026-10-30 | B | KEEP_EXTERNAL_REFERENCE | `web-application-security-audit` | Listas de payloads para teste autorizado; uso só com escopo e permissão. |
| 211 | [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh) | 82443 | 2024-07-30 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 212 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 82266 | 2026-11-10 | D | ALREADY_EVALUATED | `ai-reels-production` | Já avaliado; MCP HyperFrames conectado. |
| 213 | [tonsky/FiraCode](https://github.com/tonsky/FiraCode) | 82180 | 2026-07-28 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 214 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | 81845 | 2026-10-31 | D | REJECT | `—` | Coleção 'all in one' de ferramentas de ataque; sem método e com alto risco. |
| 215 | [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) | 81797 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 216 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | 81722 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `—` | Agentes de busca de emprego; fora do seu trabalho atual. |
| 217 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 81430 | 2026-11-10 | A/D | ALREADY_EVALUATED | `multi-agent-orchestration` | Já avaliado (2026-09-26, ecossistema ruvnet 2026-10-24). |
| 218 | [netdata/netdata](https://github.com/netdata/netdata) | 81351 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 219 | [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | 81134 | 2026-11-05 | D | KEEP_EXTERNAL_REFERENCE | `web-design-engineer` | App screenshot → código; o Claude já faz isso. |
| 220 | [hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch) | 80773 | 2026-11-05 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 221 | [ventoy/Ventoy](https://github.com/ventoy/Ventoy) | 80709 | 2026-10-22 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 222 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | 80218 | 2026-10-27 | B | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Tutorial de harness tipo Claude Code do zero; skills de exemplo genéricas. |
| 223 | [awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) | 80019 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 224 | [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 79970 | 2026-03-11 | B | ALREADY_EVALUATED | `empirical-prompt-tuning` | Já referenciado. |
| 225 | [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats) | 79841 | 2026-10-01 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 226 | [coder/code-server](https://github.com/coder/code-server) | 79827 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 227 | [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | 79408 | 2026-11-09 | A/D | KEEP_EXTERNAL_REFERENCE | `ai-reels-production` | ~140 skills de produção de vídeo acopladas ao pipeline e a APIs pagas; sobrepõe a stack de Reels. |
| 228 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 79367 | 2026-11-07 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 229 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 79311 | 2026-11-10 | D | ALREADY_EVALUATED | `codex-cost-efficiency` | Já avaliado (2026-09-21). |
| 230 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | 79295 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `diffusion-finetuning-planning` | Fine-tuning de LLM; depende de GPU. |
| 231 | [obsproject/obs-studio](https://github.com/obsproject/obs-studio) | 79268 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 232 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 79220 | 2026-09-18 | B | ALREADY_EVALUATED | `arsenal-autopilot` | Catálogo de Claude Skills já usado como radar (12 registros). |
| 233 | [doocs/advanced-java](https://github.com/doocs/advanced-java) | 79167 | 2026-10-19 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 234 | [caddyserver/caddy](https://github.com/caddyserver/caddy) | 78952 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 235 | [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | 78660 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 236 | [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | 78553 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 237 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | 78543 | 2026-09-30 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 238 | [storytold/photocraft](https://github.com/storytold/photocraft) | 78482 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 239 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 78294 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 240 | [python/cpython](https://github.com/python/cpython) | 78164 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 241 | [grafana/grafana](https://github.com/grafana/grafana) | 77819 | 2026-11-10 | D | ALREADY_EVALUATED | `dashboard-design` | Já referenciado. |
| 242 | [tensorflow/models](https://github.com/tensorflow/models) | 77636 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 243 | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | 77448 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 244 | [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 77354 | 2025-05-27 | D | KEEP_EXTERNAL_REFERENCE | `local-llm-inference-engineering` | Inferência local; sem push desde 2025-05. |
| 245 | [redis/redis](https://github.com/redis/redis) | 77352 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 246 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 77299 | 2026-11-01 | D | KEEP_EXTERNAL_REFERENCE | `code-understanding-audit` | Índice de grafo de código via MCP; skills são de manutenção interna. |
| 247 | [ocornut/imgui](https://github.com/ocornut/imgui) | 77046 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 248 | [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 77033 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 249 | [FortAwesome/Font-Awesome](https://github.com/FortAwesome/Font-Awesome) | 77028 | 2026-07-15 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 250 | [nestjs/nest](https://github.com/nestjs/nest) | 76994 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 251 | [MisterBooo/LeetCodeAnimation](https://github.com/MisterBooo/LeetCodeAnimation) | 76714 | 2026-06-12 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 252 | [PKUFlyingPig/cs-self-learning](https://github.com/PKUFlyingPig/cs-self-learning) | 76697 | 2026-09-17 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 253 | [chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11) | 76574 | 2026-10-29 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 254 | [sdmg15/Best-websites-a-programmer-should-visit](https://github.com/sdmg15/Best-websites-a-programmer-should-visit) | 76171 | 2025-09-16 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 255 | [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | 75980 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `diffusion-finetuning-planning` | Fine-tuning de LLM; depende de GPU. |
| 256 | [typicode/json-server](https://github.com/typicode/json-server) | 75733 | 2026-03-23 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 257 | [binhnguyennus/awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) | 75628 | 2026-01-04 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 258 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 75627 | 2026-11-09 | A/D | KEEP_EXTERNAL_REFERENCE | `research-to-presentation` | Skill de PPTX nativo; sobrepõe o tipo Slides e a skill pptx já instalada. |
| 259 | [apache/superset](https://github.com/apache/superset) | 75466 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 260 | [Eugeny/tabby](https://github.com/Eugeny/tabby) | 75372 | 2026-11-06 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 261 | [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) | 75306 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `financial-analysis-cycle` | Plataforma de dados financeiros com MCP; as 5 skills ensinam a operar o próprio OpenBB. Útil se você quiser um provedor de dados de mercado. |
| 262 | [enaqx/awesome-react](https://github.com/enaqx/awesome-react) | 75235 | 2026-09-04 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 263 | [pallets/flask](https://github.com/pallets/flask) | 75092 | 2026-10-30 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 264 | [usestrix/strix](https://github.com/usestrix/strix) | 74863 | 2026-11-10 | A/D | UPDATE_EXISTING | `web-application-security-audit` | Modelo de confiança declarado antes, varredura vazia ≠ limpo, correção na causa compartilhada com reexploração. |
| 265 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 74791 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 266 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 74788 | 2026-11-09 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 267 | [thedaviddias/Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist) | 74698 | 2026-10-31 | B | ALREADY_EVALUATED | `web-quality-audit` | Já referenciado. |
| 268 | [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) | 74681 | 2026-11-10 | B | KEEP_EXTERNAL_REFERENCE | `web-application-security-audit` | Listas de payloads para teste autorizado; uso só com escopo e permissão. |
| 269 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 74544 | 2026-11-10 | A/D | UPDATE_EXISTING | `to-spec` | Spec por capacidade + mudança como delta arquivada. |
| 270 | [tw93/Mole](https://github.com/tw93/Mole) | 74536 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 271 | [juliangarnier/anime](https://github.com/juliangarnier/anime) | 74496 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 272 | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 74427 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 273 | [fffaraz/awesome-cpp](https://github.com/fffaraz/awesome-cpp) | 74351 | 2026-11-06 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 274 | [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | 74059 | 2025-09-08 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Código de referência/protocolo/modelo; sem método de skill. |
| 275 | [unionlabs/union](https://github.com/unionlabs/union) | 73717 | 2026-07-25 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Código de referência/protocolo/modelo; sem método de skill. |
| 276 | [CompVis/stable-diffusion](https://github.com/CompVis/stable-diffusion) | 73573 | 2024-06-18 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Código de referência/protocolo/modelo; sem método de skill. |
| 277 | [vuejs/awesome-vue](https://github.com/vuejs/awesome-vue) | 73480 | 2026-11-03 | B | KEEP_EXTERNAL_REFERENCE | `arsenal-autopilot` | Metacatálogo; cada item exige avaliação própria. |
| 278 | [strapi/strapi](https://github.com/strapi/strapi) | 73458 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 279 | [prakhar1989/awesome-courses](https://github.com/prakhar1989/awesome-courses) | 72744 | 2023-05-04 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 280 | [nektos/act](https://github.com/nektos/act) | 72634 | 2026-11-04 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 281 | [hakimel/reveal.js](https://github.com/hakimel/reveal.js) | 72552 | 2026-09-30 | D | ALREADY_EVALUATED | `cinematic-presentation` | Já referenciado. |
| 282 | [moby/moby](https://github.com/moby/moby) | 72365 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 283 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 72232 | 2026-11-10 | D | ALREADY_ADOPTED | `ai-reels-production` | Skills Remotion instaladas no Claude. |
| 284 | [protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf) | 72161 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 285 | [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 71640 | 2026-01-25 | D | KEEP_EXTERNAL_REFERENCE | `multi-agent-orchestration` | Framework/app de agentes; sem método novo. |
| 286 | [cline/cline](https://github.com/cline/cline) | 71508 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `coding-agent-engineering` | Agente de código; alternativa ao Claude Code. |
| 287 | [ansible/ansible](https://github.com/ansible/ansible) | 71335 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 288 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | 71333 | 2026-07-24 | D | KEEP_EXTERNAL_REFERENCE | `multi-agent-orchestration` | Sandbox para código gerado por IA; padrões já cobertos. |
| 289 | [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 71242 | 2026-01-21 | D | KEEP_EXTERNAL_REFERENCE | `multi-agent-orchestration` | Framework/app de agentes; sem método novo. |
| 290 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 71151 | 2026-11-10 | C | REJECT | `—` | Prompts vazados de terceiros; procedência e licença problemáticas. |
| 291 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | 71090 | 2026-11-10 | A/D | KEEP_EXTERNAL_REFERENCE | `—` | Agentes de busca de emprego; fora do seu trabalho atual. |
| 292 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 70829 | 2026-11-10 | A/D | ALREADY_EVALUATED | `multi-agent-orchestration` | Já citado (2 registros); harness para OpenCode. |
| 293 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 70809 | 2026-11-09 | D | REJECT | `—` | Raspagem de redes sociais chinesas contornando proteções; risco legal e de termos de uso. |
| 294 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 70699 | 2026-11-04 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 295 | [swiftlang/swift](https://github.com/swiftlang/swift) | 70548 | 2026-11-10 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 296 | [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) | 70537 | 2026-11-04 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 297 | [docling-project/docling](https://github.com/docling-project/docling) | 70394 | 2026-11-10 | D | ALREADY_EVALUATED | `document-extraction-pipeline` | Conversão de documentos para LLM já avaliada. |
| 298 | [byoungd/up](https://github.com/byoungd/up) | 70378 | 2026-11-04 | B | KEEP_EXTERNAL_REFERENCE | `teach` | Material educacional ou guia; consultar na fonte quando pertinente. |
| 299 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | 69974 | 2026-11-09 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |
| 300 | [expressjs/express](https://github.com/expressjs/express) | 69575 | 2026-11-02 | D | KEEP_EXTERNAL_REFERENCE | `software-engineering-cycle` | Software, framework ou app; não é skill portátil. |

## Limites da validação
Triagem documental; só os SKILL.md citados foram lidos. Código, dependências e scripts não auditados.
