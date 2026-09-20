---
name: sprite-sheet-pipeline
description: "Converter animações ou frames em sprite sheets com registro, escala, transparência e timing verificados."
---

# sprite-sheet-pipeline

## Objetivo

Transformar animação 2D em sprite sheets revisáveis, preservando registro, escala, transparência e validação antes da promoção final.

## Quando usar

Converter animações ou frames em sprite sheets com registro, escala, transparência e timing verificados.

## Workflow

1. Partir de vídeo de animação ou frames ordenados; uma still isolada precisa primeiro virar movimento quando esse for o objetivo.
2. Para geração de fonte, manter personagem completo, margens seguras, câmera travada e registro do core corporal estável.
3. Extrair frames, remover background quando necessário e empacotar células consistentes.
4. Validar ordem, timing, clipping, escala aparente, transparência e equivalência entre sheet e frames individuais.
5. Revisar visualmente antes de promover qualquer output final.
6. Manter source/raw, work-in-progress e final approved separados.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Verificar FFmpeg ou outro extrator antes de processar vídeo. Para criação ou edição raster, usar a ferramenta de imagem disponível conforme suas regras. Conferir frames e sheet; não presumir geração de vídeo ou movimento a partir de uma still.

## Referências

Adaptada de [LayrKits/Sprite-Pipeline](https://github.com/LayrKits/Sprite-Pipeline).

Origem local: [sprite-sheet-pipeline.docx](../sprite-sheet-pipeline.docx).
