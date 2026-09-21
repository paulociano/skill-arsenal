---
name: sprite-sheet-pipeline
description: "Converter animações ou frames em sprite sheets com registro, escala, transparência e timing verificados."
---

# sprite-sheet-pipeline

## Objetivo

Transformar animação 2D em sprite sheets revisáveis, preservando registro, escala, transparência e validação antes da promoção final.

## Workflow

1. Partir de vídeo ou frames ordenados.
2. Manter personagem completo, margens seguras, câmera travada e registro do core estável.
3. Extrair frames, remover background quando necessário e empacotar células.
4. Validar ordem, timing, clipping, escala, transparência e equivalência.
5. Revisar visualmente antes de promover.
6. Separar source/raw, work-in-progress e final approved.

## Sheets direcionais e de reação

Para mascotes ou personagens dirigidos por cursor/estado:

- separar directions e reactions quando simplificar runtime;
- manter identidade, framing, scale e core body entre sheets;
- usar grid fixo e semântica por célula;
- verificar esquerda/direita manualmente, pois uma sheet espelhada pode passar checks geométricos;
- evitar cabelo solto, props ou silhuetas largas quando quebram registro;
- usar a primeira sheet como referência de identidade para a segunda quando a ferramenta suportar.

## Transparência

Transparência é capacidade da ferramenta, não uma frase no prompt.

- se a ferramenta gera alpha real, habilitar a opção explicitamente;
- se não gera, usar chroma key sólido que não colida com o personagem e remover depois;
- checkerboard pintado não é transparência;
- fundo branco/cinza achatado pode ser irrecuperável;
- validar o canal alpha do arquivo final.

## Ferramentas e dependências

Verificar FFmpeg ou extrator antes de usar. Para criação/edição raster, usar a ferramenta de imagem disponível. Não presumir geração de movimento a partir de still.

## Referências

Adaptada de https://github.com/LayrKits/Sprite-Pipeline.

Directional/reaction sheets e alpha validation adaptados de https://github.com/nilbuild/page-mascot.

Origem local: [sprite-sheet-pipeline.docx](../sprite-sheet-pipeline.docx).
