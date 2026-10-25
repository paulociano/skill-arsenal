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

## Revisão contextual de micro-padrões CSS

Ao modernizar CSS legado, avaliar cada técnica no componente concreto, em vez de importar uma coleção de snippets como defaults:
1. Checar `box-sizing`, estilos base e herança antes de acrescentar novo reset, evitando sobrescrever componentes e estilos nativos de formulário.
2. Preferir `aspect-ratio` e `object-fit` para imagens quando preservarem geometria, além de `margin-inline` e outras propriedades lógicas para layout independente da direção.
3. Usar `:is()` com atenção à especificidade efetiva; escolher `:where()` quando intencionalmente se deseja zero especificidade.
4. Proteger foco visível: `all: unset`, remoção de `outline` ou controles construídos com CSS não podem apagar acessibilidade por teclado.
5. Verificar se conteúdo gerado por `::before`/`::after` precisa ser lido, copiado ou exposto a tecnologia assistiva. Nunca substituir texto semântico essencial por conteúdo CSS.
6. Tratar hacks como padding para aspect ratio, seletores globais de espaçamento ou expansão no `:hover` como alternativas históricas, não melhores práticas universais. Preferir APIs modernas, sem perder fallback para browsers-alvo.
7. Validar no navegador sempre que o comportamento de layout, cascata, hover/focus ou leitor de tela for determinante.

**Origem (B, método absorvido seletivamente):** https://github.com/AllThingsSmitty/css-protips. É um catálogo de dicas, não um runtime nem uma Agent Skill.


## Estratégia classless-first e cascata de baixa especificidade (Sumi.css, 2026-10-24)

Em sites editoriais, protótipos, ferramentas internas e páginas simples, considerar baseline de HTML semântico estilizado antes de introduzir componentes e classes utilitárias. Avaliar: (1) elemento nativo adequado para cada papel; (2) valores de design via custom properties; (3) seletores de zero especificidade com `:where()` para preservar overrides; (4) color scheme claro/escuro e estados ARIA visíveis; (5) foco por teclado, contraste e redução de movimento; (6) custo de CSS, dependências e build.

A opção classless não deve sobrescrever o design system existente nem forçar estilos globais em aplicações grandes ou componentes encapsulados. Escolher CSS próprio, framework leve ou biblioteca existente pelo custo real de manutenção. Só integrar Sumi.css quando o usuário/projeto pedir ou a validação no projeto justificar, após conferir licença e versão.

**Proveniência:** https://github.com/vladocar/Sumi.css. Metodologia de arquitetura visual absorvida; pacote não instalado nem copiado.
