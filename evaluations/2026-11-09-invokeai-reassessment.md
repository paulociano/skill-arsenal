# InvokeAI — reavaliação (2026-11-09)

## Fonte
- https://github.com/invoke-ai/InvokeAI — Apache-2.0 (+ licenças de componentes de modelos), ~28k estrelas
- Avaliações anteriores: `2026-09-30-creative-ai-open-source-radar.md` (B/D, referência externa) e `2026-10-08-zapier-agent-workspaces-creative-tools.md` (A/D, KEEP_EXTERNAL_REFERENCE; "avaliar mais a fundo quando houver trabalho concreto em geração visual")
- Lido nesta passagem: README público

## Estado atual
Motor criativo de geração de imagens com interface web e instalação por Launcher. Unified Canvas (inpainting/outpainting, pincéis), workflows por nós, gerenciador de modelos, upscaling, segmentação SAM/SAM2 e galeria com metadados para reproduzir prompt e parâmetros. A lista de modelos cresceu bastante: SD 1.5/2/XL/3.5, FLUX (Dev, Schnell, Kontext, Krea, Redux, Fill e FLUX.2), CogView 4, Z-Image, Qwen Image, ERNIE-Image, Ideogram 4 e modelos só por API (Nano Banana, GPT Image, Wan). Sem MCP nem integração com agentes no README.

## Decisão
**KEEP_EXTERNAL_REFERENCE (mantida). Sem mudança em skills.** Continua sendo aplicação de desktop/servidor local que exige GPU, não uma capacidade que o agente execute. Os métodos portáveis (controle espacial, pipelines por nós, metadados para reprodutibilidade) já estão em `high-fidelity-image-generation`, e a organização de workspace em `stacks/ai-workspace-operating-cycle`.

## Gatilho registrado
O usuário mantém projetos de jogos com assets gerados em ferramentas externas (city builders em miniatura e em massinha, com sprites via Blender). Se esses projetos precisarem de geração local em lote com consistência de estilo (mesmo checkpoint, LoRA, seed e pipeline reaproveitável) e houver GPU disponível, InvokeAI passa a ser candidato real como ferramenta de produção de assets, junto com ComfyUI. Nesse caso, fazer avaliação prática (instalação no computador do usuário, teste de um pipeline de sprite) antes de adotar.

## Segurança
Nada executado. Modelos de terceiros carregados no gerenciador têm licenças próprias (algumas não comerciais); conferir antes de usar assets em produto. Checkpoints em formato pickle podem executar código: preferir safetensors.
