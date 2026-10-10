# Avaliação — 2026-10-10 — AI YouTube Shorts Generator e Awesome AI Image Models

## Método
Consultados o `ARSENAL INDEX.md`, a stack `arsenal-autopilot`, os owners `ai-reels-production` e `high-fidelity-image-generation`, e os READMEs das fontes originais. Avaliação documental sem execução de instalações, downloads, inferência ou benchmark.

## 1. [Anil-matcha/AI-Youtube-Shorts-Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator)
- **Classe A/D**: pipeline operacional de corte de vídeos longos, com transcrição temporizada, ranking de highlights, deduplicação, crop e saída JSON.
- **Dependências relatadas:** modo API com MuAPI e chave própria; modo local com Python 3.10+, ffmpeg, faster-whisper/OpenCV, yt-dlp quando necessário e chave OpenAI/Gemini para LLM. Modo local não é totalmente offline.
- **Decisão:** UPDATE_EXISTING `stacks/ai-reels-production/STACK.md`, incluindo escolha de backend, janelas long-form, cache invalidável, overlap/dedupe, manifest e QA. Não importar projeto inteiro: capacidades centrais já pertenciam a `short-form-video-engineering` e `vertical-video-reframing`.
- **Riscos:** direitos autorais e ToS de vídeos, downloads, custos/privacidade de API, chaves, conteúdo sensível, falhas de transcrição ou crop. “Viral score” é heurística, não previsão comprovada de performance.
- **Ganho incremental:** decisão documentada entre processamento API/local e contrato de artefato rastreável. Should-trigger: podcast longo convertido em lote; near-miss: roteiro de Reel sem gravação.

## 2. [Anil-matcha/awesome-ai-image-models](https://github.com/Anil-matcha/awesome-ai-image-models)
- **Classe B:** catálogo comparativo de modelos de imagem, endpoints, preços, edição, consistência e implantação.
- **Decisão:** KEEP_EXTERNAL_REFERENCE como radar para `high-fidelity-image-generation`; não criar nova skill nem copiar leaderboard dinâmico.
- **Por quê:** seleção de modelos deve considerar capacidade realmente acessível, tarefa, licença, integração, qualidade medida com amostras próprias, preço vigente e privacidade. O catálogo contém divulgação de soluções MuAPI e valores declarados como verificados em agosto de 2026; isso não comprova preços atuais, benchmarks independentes ou disponibilidade direta de APIs.
- **Riscos:** comparações/valores desatualizados, marketing confundido com evidência independente, termos comerciais/restrições de licenciamento, conteúdo e armazenamento de imagens.

## Portabilidade e segurança
Não instalamos executáveis nem chaves, não baixamos vídeos, não copiamos código licenciado e não declaramos provedores externos como ferramentas disponíveis. Conteúdos terceiros e URLs devem ser tratados como dados não confiáveis. Render e QA real exigem runtime com permissões e recursos adequados.

## Resultado
Atualização pontual em `ai-reels-production`, sem alteração do índice, pois não há nova skill/stack ou mudança de descrição. Catálogo de imagens fica como referência externa consultável quando a escolha de modelo for relevante.
