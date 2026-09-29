# Referências para projetos HTML e CSS

Pesquisa documental: 2026-09-29. Fontes oficiais nas linhas abaixo. Complemento ao catálogo de componentes animados, com foco em documentos HTML, páginas estáticas e JavaScript nativo quando necessário.

| Recurso | Tipo | Aplicação e limite |
|---|---|---|
| [Uiverse](https://uiverse.io/) | Catálogo | Componentes e efeitos; selecionar HTML/CSS, pois há variantes Tailwind/React. |
| [Animista](https://animista.net/) | Gerador CSS | Ajustar keyframes, duração e easing; exportar somente o necessário. |
| [Animate.css](https://animate.style/) | Animação CSS | Entradas, saídas e atenção por classes; gatilhos de estado podem exigir JS. |
| [Hover.css](https://ianlunn.github.io/Hover/) | Efeitos CSS | Hover em links, botões e imagens; oferecer foco/toque equivalentes. |
| [CSS Loaders](https://css-loaders.com/) | Snippets CSS | Indicadores de carregamento; estado e anúncio acessível pertencem à aplicação. |
| [Magic Animations](https://www.minimamente.com/project/magic/) | Animação CSS | Perspectiva, rotação e transições expressivas; uso pontual. |
| [Transition.css](https://www.transition.style/) | Animação CSS | Revelações por clip-path; conferir suporte e fallback. |
| [Imagehover.css](https://imagehover.io/) | Efeitos CSS | Overlays e legendas de imagens; não esconder informação essencial no hover. |
| [Hamburgers](https://jonsuh.com/hamburgers/) | Componente CSS | Ícone de menu animado; conectar estado, aria-expanded e painel real. |
| [CSS Buttons](https://cssbuttons.io/) | Catálogo | Botões HTML/CSS; revisar estilos globais e licença do item. |
| [Hint.css](https://kushagra.dev/lab/hint/) | Componente CSS | Tooltip visual; verificar teclado/leitor de tela, não usar para informação indispensável. |
| [CSS Pattern](https://css-pattern.com/) | Snippets CSS | Texturas e fundos com gradientes; conferir contraste. |
| [Pico CSS](https://picocss.com/) | Base CSS | HTML semântico, formulários e poucas classes; avaliar efeitos globais nos elementos. |
| [Bulma](https://bulma.io/) | Base CSS | Grid, cards, navegação e forms; lógica interativa deve ser implementada. |
| [Pure CSS](https://purecss.io/) | Base CSS modular | Grids, tabelas, botões e formulários; importar módulos necessários. |
| [Open Props](https://open-props.style/) | Tokens CSS | Variáveis de cor, sombras, espaçamento e motion; não é catálogo de widgets. |
| [Open Props UI](https://open-props-ui.netlify.app/html/) | Componentes HTML/CSS | Recursos modernos de HTML/CSS; conferir suporte por componente. |
| [Beer CSS](https://www.beercss.com/) | CSS + JS opcional | Material Design; JS opcional na base, necessário em alguns comportamentos. |
| [daisyUI](https://daisyui.com/) | Ecossistema Tailwind | Componentes e temas; distinguir setup de build de CSS compilado no navegador. |
| [Bulmaswatch](https://jenil.github.io/bulmaswatch/) | Temas Bulma | Alternativa visual para Bulma; conferir compatibilidade de versões. |

## Seleção por necessidade

- Página simples ou formulário: avaliar Pico CSS; para layout com classes, Bulma ou módulos Pure CSS.
- Interface própria: Open Props fornece tokens; Open Props UI oferece padrões de componentes.
- Efeito isolado: Uiverse, Animista, CSS Loaders ou CSS Pattern permitem extrair um trecho.
- Animações reutilizadas: Animate.css, Hover.css, Magic Animations ou Transition.css.
- Projeto já em Tailwind: avaliar daisyUI; projeto já em Bulma: avaliar Bulmaswatch.
- Material Design: Beer CSS, distinguindo aparência de comportamento.

## Integração

1. Preservar a arquitetura existente. Evitar combinar resets/frameworks globais como Pico, Bulma e Beer CSS na mesma página sem isolamento.
2. Separar HTML/CSS puro, gerador, tokens, temas e dependências de build. Ausência de React não significa ausência de JavaScript ou compilação.
3. Registrar licença da versão e do item usado, incluindo assets. Código copiável não implica licença irrestrita. Conferir condições comerciais onde existirem.
4. Em documento HTML único, considerar CSS local/inlined e funcionamento offline; não introduzir CDNs como requisito implícito.
5. Usar motion somente quando servir ao comportamento ou à direção visual; respeitar prefers-reduced-motion e manter conteúdo disponível.
6. Hover não pode ser o único acesso. Implementar foco, teclado, toque, estados e semântica reais.
7. Conferir responsividade, conflitos de seletores, contraste, custo de blur/shadows/paint e suporte do navegador no projeto consumidor.

## Limite da avaliação

Sites e documentação foram consultados; não houve instalação nem teste de execução dessas bibliotecas. As recomendações são pontos de partida para protótipos, não aprovação de produção ou auditoria completa de acessibilidade/segurança.
