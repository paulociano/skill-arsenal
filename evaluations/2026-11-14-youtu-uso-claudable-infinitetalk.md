# Avaliação em lote — Youtu-Agent, USO, Claudable e InfiniteTalk

- Data: 2026-11-14
- Procedimento: `arsenal-autopilot` (índice/router GitHub consultado primeiro) + revisão de portabilidade/segurança por leitura de README, manifests e owners existentes.
- Nível de evidência: `static_only`; sem download de pesos, execução, scanner automatizado, instalação ou benchmarks reproduzidos.
- Não executar scripts encontrados nos repositórios como parte desta avaliação.

## Matriz de decisões

| Fonte | Classe | Capacidade distinta | Owner/ação | Decisão |
| --- | --- | --- | --- | --- |
| https://github.com/TencentCloudADP/youtu-agent | B/D | Separar geração de workflow/meta-agente, validação de tool code e configs, aprendizado por experiência com regressão | `skills/coding-agent-engineering/SKILL.md` | UPDATE_EXISTING |
| https://github.com/bytedance/USO | B/D | Desacoplar sujeito/identidade, estilo e layout; QA por dimensão | `skills/character-continuity/SKILL.md` | UPDATE_EXISTING |
| https://github.com/anymorph-ai/Claudable | D | CLI agents + preview + deploy como produto local | nenhuma | KEEP_EXTERNAL_REFERENCE |
| https://github.com/MeiGen-AI/InfiniteTalk | B/D | Segmentação de talking-head longo, drift de cor/identidade e sincronização nas junções | `skills/synthetic-presenter-video/SKILL.md` | UPDATE_EXISTING |

### 1. Youtu-Agent

Framework Python baseado em OpenAI Agents SDK e bibliotecas adicionais; README descreve geração de workflows e meta-agentes, síntese de ferramentas e configurações, prática baseada em experiência/GRPO e treinamento RL distribuído. Benchmarks são alegações dos autores, não reproduzidos. O documento LICENSE lido contém texto MIT, embora metadados de licença GitHub retornem NOASSERTION; em uso externo verificar ainda dependências e assets.

**Ganho:** contrato para sintetizar ferramentas de forma governada e separar qualidade da síntese, execução e resultado. **Limite:** não instalamos framework, modelo, CUDA, RL nem workers. **Riscos:** tool code gerado pode executar operações, ler secrets, atingir rede; exigir staging, least privilege, testes adversariais, approval gate e holdout para regressão.

### 2. USO

Pesquisa/implementação ByteDance de geração por sujeito e estilo, com treino de disentanglement e recompensa; inferência baseada em difusão/FLUX, PyTorch e pesos externos. LICENSE Apache-2.0 do repo; licenças de checkpoints/base models devem ser verificadas separadamente. O README indica ~16 GB VRAM com fp8/offload para uma referência, ~18 GB para múltiplas.

**Ganho:** QA independente de identidade, estilo e composição para produção seriada. **Limite:** não prometer que o ChatGPT oferece pesos, ControlNet, fp8 ou VRAM. **Riscos:** direitos e consentimento da referência, execução de dependências e downloads de checkpoints; não se realizou inferência.

### 3. Claudable

Construtor web baseado em Next.js/React, Prisma/SQLite, Electron, agentes CLI externos e integrações GitHub/Vercel/Supabase. LICENSE MIT. README traz instruções de npm install, script postinstall de setup de ambiente e comandos que podem resetar banco; package.json indica `postinstall`, `prisma:reset` e `setup` com alterações de estado. Não executar automaticamente. A documentação ainda contém referências à antiga URL opactorai/Claudable, distinta do repo informado.

**Decisão:** KEEP_EXTERNAL_REFERENCE, pois `functional-web-app-builder` e `coding-agent-engineering` já cobrem os contratos sem requerer aplicação específica. **Riscos:** CLI com acesso a workspace, tokens de implantação e credenciais de banco; permissões para deploy e mudanças de schema; segurança e supply chain dependem de deployment real.

### 4. InfiniteTalk

Projeto MeiGen-AI para geração de vídeo com fala a partir de imagem ou vídeo, incluindo modos clip/streaming, dependências Wan2.1-I2V-14B e wav2vec2 e pesos InfiniteTalk, execução GPU e opções quantização/offload. LICENSE Apache-2.0 no repositório, com licenças de pesos/base modelos a verificar separadamente. README diferencia V2V para maior extensão de vídeo de I2V, onde avisa sobre desvio de cor após ~1 minuto. Vídeo 'unlimited-length' é objetivo do projeto, não garantia de consistência ilimitada.

**Ganho:** gate de continuidade audiovisual em segmentos, limites de drift e QA nas junções. **Limite:** nenhum render ou medição realizado. **Riscos:** heavy GPU, licenciamento de assets/pesos, consentimento de voz/imagem e falsificação de fala.

## Segurança / portabilidade

Veredito de triagem: **CAUTION**, não por malware demonstrado, mas por código executável não executado, instalação de dependências, acesso a credenciais e serviços externos, e modelos pesados com licenças próprias. Segredos nunca devem ser incluídos em prompts e logs por padrão. Não se alegou scanner completo ou `behavior_verified`.

## Ganho incremental, ownership e aceitação

- `coding-agent-engineering`: should-trigger = projetar agente que gera ferramentas a partir de requisitos e precisa testar schema/permissões; near-miss = patch de código simples.
- `character-continuity`: should-trigger = personagem recorrente com estilo alternável; near-miss = imagem única sem continuidade.
- `synthetic-presenter-video`: should-trigger = avatar falante contínuo por vários minutos; near-miss = legendagem de vídeo convencional.
- `Claudable`: nenhuma skill nova, pois a experiência de preview/deploy é um runtime alternativo, não processo incremental para ChatGPT.

## Materialização

Arquivos de owners atualizados:
- `skills/coding-agent-engineering/SKILL.md` — commit `5b27c7ce64fe2a13ed2bd2657ab816cb70b06218`.
- `skills/character-continuity/SKILL.md` — commit `9bac0ff47a36b518d4ffa412db97c23d5c2ed385`.
- `skills/synthetic-presenter-video/SKILL.md` — commit `f41f84d4f2cff549552347334d7a59edbad5443b`.

O índice permanece inalterado porque não surgiu owner ou alteração do roteamento. Todas as melhorias foram incorporadas como adendos nos owners existentes; nenhum script, aplicativo, agente, peso ou serviço foi instalado.

## Fontes

- https://github.com/TencentCloudADP/youtu-agent (README, LICENSE e raiz)
- https://github.com/bytedance/USO (README, configuração e licença do repositório)
- https://github.com/anymorph-ai/Claudable (README, package.json, licença do repositório)
- https://github.com/MeiGen-AI/InfiniteTalk (README e licença)
- https://github.com/paulociano/skill-arsenal/blob/master/stacks/arsenal-autopilot/STACK.md
