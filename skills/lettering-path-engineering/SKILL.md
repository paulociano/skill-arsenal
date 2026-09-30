---
name: lettering-path-engineering
description: "Construir lettering customizado, glyphs e texto vetorial por paths editáveis, métricas e relações tipográficas, incluindo single-stroke para plotter/CNC, sem confundir composição tipográfica com desenho de fonte."
---

# Lettering Path Engineering

## Objetivo
Projetar letras como geometria editável quando a entrega exige paths, glyphs customizados, single-stroke, gravação, plotter, CNC ou uma expressão que uma fonte existente não resolve.

## Quando usar
- lettering customizado real;
- logotipo baseado em letras desenhadas;
- glyph/path editing;
- single-line/single-stroke fonts;
- texto para plotter, gravação, CNC ou laser;
- converter letterforms em SVG paths controlados;
- prototipar pequena família/glyph set.

Para apenas compor texto com fontes existentes, usar typographic-composition.

## Modelo
Separar:
- skeleton/stroke;
- outline;
- anchors/control handles;
- baseline/x-height/cap-height/ascender/descender;
- advance width;
- sidebearings;
- kerning;
- contours;
- glyph identity/unicode;
- interpolation axes quando houver sistema multi-master.

## Workflow
1. Definir destino: display, logo, plotter, engraving, font ou SVG isolado.
2. Definir métricas e guias.
3. Escolher skeleton-first ou outline-first.
4. Construir curvas com poucos pontos úteis e tangência controlada.
5. Reutilizar componentes quando formas realmente compartilham estrutura.
6. Ajustar spacing antes de micro-kerning.
7. Testar glyph isolado e palavras reais.
8. Para single-stroke, manter contornos abertos quando o processo exige uma passada e evitar outline duplicado.
9. Preservar paths editáveis e provenance/licença das referências.
10. Validar export/import e aparência no destino real.

## Lettering, type design e plotter
- lettering pode otimizar uma expressão única;
- type design precisa funcionar como sistema;
- outline font descreve áreas preenchidas;
- stroke font descreve trajetórias;
- converter outline em centerline automaticamente pode perder intenção e exigir correção.

## Sketch → path
Quando partir de desenho manual:
1. preservar gesture/silhouette;
2. remover ruído que não pertence ao traço;
3. inferir strokes/curves;
4. simplificar nós sem apagar personalidade;
5. comparar vetor sobre o sketch;
6. manter a imagem original como referência, não como verdade geométrica perfeita.

## QA
Verificar ritmo, consistência de curvas, joins, overshoot quando relevante, spacing, kerning, legibilidade, nós excessivos, self-intersections, direção/abertura de paths e fidelidade de exportação.

## Ferramentas
opentype.js, fontmake, FontTools, Paper.js, Maker.js, vpype, Hershey/stroke-font tooling são referências. Não presumir runtime instalado.

## Integração
typographic-composition, brand-logo-exploration, editable-visual-design, svg-handdrawn-animation, verify-before-claim.

## Origem metodológica
Generalizada de opentype.js, fontmake, Maker.js, vpype, Hershey Text JS, Stroke Font Studio e sketch-vectorization.
