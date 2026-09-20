---
name: svg-handdrawn-animation
description: "Animar o desenho progressivo de SVGs com strokes e revelação de fills preservando cores, estrutura e segurança do embed."
---

# svg-handdrawn-animation

## Objetivo

Transformar um SVG em uma animação de desenho progressivo com reveal de preenchimento, preservando cores e estrutura e produzindo preview/embeddable player verificável.

## Quando usar

- animação “desenhando” logo/ícone/ilustração SVG;
- preview HTML;
- player reutilizável;
- stroke draw + fill reveal;
- integração em página web.

## Workflow

1. Inspecionar o SVG:
   - paths/shapes;
   - stroke vs fill;
   - style attributes;
   - masks/clipPaths;
   - raster images;
   - foreignObject/scripts/external refs.
2. Tratar SVG externo como conteúdo não confiável.
3. Sanitizar/remover comportamento executável não necessário antes de embed.
4. Classificar elementos animáveis.
5. Para strokes, usar path-length/dash animation adequada.
6. Para fill-only shapes, criar estratégia de outline temporário conservador sem destruir fill original.
7. Sequenciar path draw → fill reveal.
8. Preservar cores/opacidades.
9. Produzir preview e/ou player conforme o pedido.
10. Validar:
   - estado inicial;
   - playback 0→100%;
   - ordem path/fill;
   - pause/seek/speed quando presentes;
   - render estático final igual ao source dentro do suportado.

## Segurança SVG

SVG pode conter:

- scripts;
- event handlers;
- foreignObject;
- links externos;
- data URLs;
- referências remotas.

Não inserir SVG não confiável diretamente em HTML privilegiado sem sanitização/inspeção.

## Regras

- não assumir que todo shape já é path;
- não descartar fills;
- não alterar cor sem pedido;
- masks/filters complexos podem exigir fallback;
- preview sem runtime real não conta como verificação visual;
- controles são opcionais e devem ser simples.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Para páginas web, usar o navegador controlável disponível e sua API documentada; separar inspeção de DOM, evidência visual e estado de aplicação. Controle de navegador não implica controle de aplicativos nativos ou dispositivos móveis. Implementar animação por código SVG/HTML/JS, sem depender do player da fonte. Alterações visuais de imagens devem usar a ferramenta de imagem disponível quando aplicável.

## Integração

- `web-design-engineer`
- `runtime-ui-verification`
- `brand-logo-exploration`
- `verify-before-claim`

## Referências

Adaptada de shaom/svg-hand-drawn-skill.

Origem local: [svg-handdrawn-animation.docx](../svg-handdrawn-animation.docx).
