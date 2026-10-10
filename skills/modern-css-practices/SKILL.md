---
name: modern-css-practices
description: "Aplicar CSS moderno adaptativo em páginas e componentes com progressive enhancement, layout intrínseco, estados acessíveis e redução de JavaScript/breakpoints desnecessários."
---

# Modern CSS Practices

## Origem
Adaptado de https://github.com/vojtaholik/good-css (MIT). Consultar a fonte original para exemplos e compatibilidade atualizada.

## Quando usar
Escrita, revisão ou modernização de CSS em interfaces web, quando o alvo de browsers e o sistema de estilos do projeto forem conhecidos. Não acionar para UI exclusivamente nativa.

## Método
1. Verifique browsers suportados, tokens de design e sistema de estilos existente. Não imponha recursos recentes sem fallback.
2. Prefira layout intrínseco: grid com `minmax()`, `auto-fit`, `min()`, `max()` e `clamp()`; use container queries quando dimensões do componente importarem mais que viewport.
3. Prefira propriedades lógicas (`margin-inline`, `padding-block`) respeitando direção de texto; não proíba propriedades físicas quando semântica exigir direção física.
4. Reutilize tokens de cor, espaço e tipografia. Considere `oklch()` e `color-mix()` com compatibilidade testada e fallback de cor quando necessário.
5. Deixe hover restrito a dispositivos que o oferecem, use `:focus-visible` com outline observável, estado `:active` e alvo de toque adequado.
6. Use transições de propriedades explícitas e respeite `prefers-reduced-motion`; não esconda interatividade essencial em animação.
7. Considere scroll snapping, popover, dialog e recursos CSS nativos antes de adicionar JavaScript; preserve semântica e teclado.
8. Para conteúdo externo, trate wrapping, truncamento, imagens, overflow e idioma sem pressupor dimensão fixa.
9. Teste desktop, mobile, zoom, teclado, redução de movimento, navegadores-alvo e contraste. Meça regressão visual e de performance.

## Guardrails
- CSS-first não significa CSS-only: estado, dados e operações continuam na camada adequada.
- Não substituir breakpoints úteis dogmaticamente; usar quando o layout ou o conteúdo justificarem.
- Não instalar `npx skills`, Bun ou scripts do projeto externo para executar esta metodologia.
- Não afirmar verificação em browser quando só houve revisão estática.

## Resultado
Diff mínimo de estilos, justificativa de responsividade, fallbacks e evidências de teste quando disponíveis.
