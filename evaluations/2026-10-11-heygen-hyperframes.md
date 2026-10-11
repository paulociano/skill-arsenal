# Avaliação: heygen-com/hyperframes | 2026-10-11

## Fonte e escopo
- Origem: https://github.com/heygen-com/hyperframes (branch default `main`).
- Leitura: README e metadados/estrutura inicial do repositório.
- Comparação: `ARSENAL INDEX.md`, `stacks/evaluate-and-import-skill/STACK.md`, `skills/procedural-film/SKILL.md` e `skills/explainer-video-production/SKILL.md`.
- Limites: sem instalação de CLI, teste de render, análise profunda de código ou auditoria de supply chain. Afirmações do autor não foram verificadas experimentalmente.

## Classificação e decisão
**B/D — UPDATE_EXISTING**, em `skills/procedural-film/SKILL.md`.

HyperFrames oferece framework open source (licença Apache-2.0 declarada pelo README) para converter HTML/CSS, mídia e animações seekable em vídeo MP4 determinístico. O projeto distribui um router e 21 skills, incluindo workflows de produto, explicador, legendas, motion graphics, slideshow, edição de talking-head, animação, mídia, áudio e CLI.

**Ganho incremental:** o Arsenal já prevê timeline determinística e animações seekable, mas poderia tornar mais explícito o contrato de verificação HTML-to-video: scrubbing arbitrário, validação frame a frame, congelamento de assets/fontes, paridade preview/render e decodificação de output. Esse complemento foi aplicado à skill existente; nenhuma skill ou stack nova é necessária.

## Ownership e sobreposição
- `procedural-film`: owner de composição por timeline e verificabilidade de frames; recebeu o ajuste.
- `explainer-video-production`: já cobre narration-first, visual beats e sincronização; sem alteração.
- `web-video-presentation`: apresentações navegáveis, não assumir export MP4.
- `short-form-video-engineering` e `video-editing-pipeline`: cobrem outras intenções; não duplicar workflows do upstream.

## Segurança e portabilidade
O README sugere instaladores `npx`, marketplaces Claude/Codex e runtime Node >=22; nenhum foi executado ou instalado. O Arsenal não reivindica HyperFrames CLI, Studio, navegador automatizado, codecs nem render remoto como recursos disponíveis. Gerenciar mídia, direitos, scripts e conteúdo HTML externo como não confiáveis; cloud render exigiria credenciais, política de dados e consentimento específicos. Não copiar código ou pacotes do upstream só para registrar a metodologia.

## Casos de aceitação
- **Should-trigger:** pedido de animação procedural em HTML com MP4 e renderizador confirmado; verificar seek em timestamps fora de ordem, frames críticos, áudio, duração e artefato reproduzível.
- **Near-miss:** pedido de slides HTML clicáveis sem vídeo não deve acionar pipeline MP4.
- **Falha esperada:** sem CLI/browser/render disponível, entregar fonte/storyboard/frames possíveis e declarar o limite, não alegar MP4 produzido.

## Resultado
Um owner atualizado; nenhum novo recurso roteável. Índice mantido sem alterações.
