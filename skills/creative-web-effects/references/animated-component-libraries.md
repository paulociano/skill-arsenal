# Bibliotecas de componentes animados e efeitos

Catálogo curado em 2026-09-28 para ampliar o repertório do Arsenal. As entradas abaixo são referências de implementação e direção visual; não implicam instalar dependências, copiar identidade ou aceitar automaticamente a licença. Confirmar licença, versão, dependências e suporte de navegador antes de adotar.

## Prioridade de exploração

- **P1 — prototipar primeiro:** Animata, Aceternity UI, Cult UI, Fancy Components, SmoothUI, UI Layouts, Skiper UI, Hover.dev.
- **P2 — efeitos e superfícies:** ScrollX UI, ParticleUI, Marvelous UI, Canvas UI, Paper Shaders, Aurora.
- **P3 — stacks específicas ou comerciais:** Vue Bits, Svelte Bits, Svelte Animations, Inspira UI, Motion UI, Myndui.

## Catálogo

| Biblioteca | URL oficial | Stack / foco | Como usar como referência | Observações |
|---|---|---|---|---|
| **Animata** | [animata.design](https://animata.design/) · [codse/animata](https://github.com/codse/animata) | React + Tailwind; componentes copiados para o projeto, backgrounds, cards, scroll, texto, loaders e hero | Base para microinterações e blocos completos com código local | Site declara MIT; confirmar o arquivo de licença no commit usado |
| **Aceternity UI** | [ui.aceternity.com](https://ui.aceternity.com/) | React/Next + Tailwind; hero, bento, beams, aurora, canvas, parallax e cards | Repertório forte para landing pages e efeitos de destaque | Catálogo mistura componentes livres e blocos/acesso pago; validar item |
| **Cult UI** | [cult-ui.com](https://www.cult-ui.com/docs) · [nolly-studio/cult-ui](https://github.com/nolly-studio/cult-ui) | React/Tailwind/shadcn; componentes experimentais, shaders e microinterações | Referência para direções “art-directed” e efeitos de superfície | Repositório declara MIT; docs também têm seções/templates pagos |
| **Fancy Components** | [fancycomponents.dev](https://www.fancycomponents.dev/) · [danielpetho/fancy](https://github.com/danielpetho/fancy) | React + Tailwind; registry de componentes com motion e efeitos | Copiar a anatomia de um efeito sem acoplar uma biblioteca inteira | Conferir licença e dependências do componente escolhido |
| **SmoothUI** | [smoothui.dev](https://smoothui.dev/docs/components) | React + Tailwind; upload, tabs, botões magnéticos, kinetic text, shaders, glass, gooey, cursor e scroll | Catálogo amplo para selecionar uma assinatura visual por tela | Conteúdo e dependências variam por componente; testar custo e reduced motion |
| **UI Layouts** | [ui-layouts.com](https://ui-layouts.com/) · [ui-layouts/uilayouts](https://github.com/ui-layouts/uilayouts) | React/Tailwind; layouts, efeitos, blocos e ferramentas de design | Referência de composição de páginas, não só de widgets | Projeto ativo; revisar API e licença do commit atual |
| **Skiper UI** | [skiper-ui.com](https://skiper-ui.com/) | React + Tailwind/Motion; hero, showcase, drag, ícones e layouts animados | Estudar coreografia de seções inteiras e transições entre estados | Alguns demos e páginas têm distribuição própria; validar código antes de reutilizar |
| **Hover.dev** | [hover.dev](https://www.hover.dev/) | React/Tailwind; interações de hover, botões, cards e marketing | Fonte para estados hover/focus e feedback de ponteiro | Mistura exemplos gratuitos e conteúdo comercial; não tratar demo como API estável |
| **ScrollX UI** | [scrollxui.dev](https://scrollxui.dev/) · [Adityakishore0/ScrollX-UI](https://github.com/Adityakishore0/ScrollX-UI) | React/Tailwind/Motion; text motion, spotlight, reveal, dynamic backgrounds e scroll | Referência para reveal e sequenciamento scroll-linked | Alguns efeitos têm opção mobile explícita; manter conteúdo compreensível sem scroll |
| **ParticleUI** | [particleui.dev](https://www.particleui.dev/) | React, Vue e Svelte via registry; meteors, sparkles, marquee, skeleton, slider | Comparar o mesmo efeito entre frameworks e extrair versões menores | Suporte e implementação variam por componente; conferir licença e engine |
| **Marvelous UI** | [marvelous-ui.com](https://marvelous-ui.com/) | React/Vue/Svelte/Angular/Astro/HTML; backgrounds, texto, 3D e microinterações | Radar multi-framework para efeito de marketing e ambientação | A página anuncia vários frameworks; validar maturidade e licença por exemplo |
| **Canvas UI** | [canvasui.dev](https://canvasui.dev/docs) · [DavidHDev/canvas-ui](https://github.com/DavidHDev/canvas-ui) | HTML dentro de Canvas/WebGL/WebGPU; variantes React, Solid, Preact, Vue, Svelte e vanilla | Explorar superfícies imersivas quando HTML em canvas for requisito real | Docs indicam que a maioria usa Chrome Origin Trial; tratar como experimental e manter fallback HTML |
| **Paper Shaders** | [shaders.paper.design](https://shaders.paper.design/) · [paper-design/shaders](https://github.com/paper-design/shaders) | Canvas shaders sem dependências; backgrounds e texturas procedurais | Efeitos de fundo leves e controláveis sem puxar Three.js | Preservar o arquivo NOTICE/LICENSE do repositório ao redistribuir |
| **Aurora** | [auroralib.com](https://auroralib.com/) | Web components/CSS vars, GSAP opcional e Three.js opcional; componentes animados | Referência quando a stack precisa de elementos nativos e framework-neutral | Confirmar licença, browser support e custo dos componentes que usam Three.js |
| **Vue Bits** | [vue-bits.dev](https://vue-bits.dev/) | Vue; componentes animados, backgrounds, texto e interações copy-to-project | Portar ideias de React Bits para produtos Vue | É repertório de código copiado; conferir dependências e licença do componente |
| **Svelte Bits** | [svelte-bits.dev](https://svelte-bits.dev/) · [DavidHDev/svelte-bits](https://github.com/DavidHDev/svelte-bits) | Svelte; componentes interativos, shaders, física e efeitos portados | Referência Svelte quando preservação de comportamento importa | É um port oficial do ecossistema React Bits; verificar licença e dependências originais |
| **Svelte Animations** | [sv-animations.vercel.app](https://sv-animations.vercel.app/) · [github.com/SikandarJODD/animations](https://github.com/SikandarJODD/animations) | Svelte; componentes animados e efeitos | Fonte rápida para transições e efeitos prontos em Svelte | Tratar como catálogo comunitário; validar manutenção, licença e acessibilidade |
| **Inspira UI** | [inspira-ui.com](https://inspira-ui.com/) | Vue/Tailwind; componentes animados e efeitos de interface | Aumentar cobertura de Vue em cards, texto e backgrounds | Site deve ser usado como referência visual; confirmar fonte/licença de cada item |
| **Motion UI** | [motion.dev/ui](https://motion.dev/ui) | React/Tailwind + Motion; seções de marketing, transições e blocos | Estudar composição de seções e tuning pelo tema Motion | Parte do Motion+; conteúdo comercial e dependente do ecossistema Motion |
| **Myndui** | [myndui.vercel.app/docs](https://myndui.vercel.app/docs) | React/TypeScript/Tailwind/Motion/shadcn; componentes e efeitos | Opção rápida para prototipar UI React com motion | Confirmar estado do projeto, licença e dependências antes de produção |

## Critério de seleção para o Arsenal

1. Escolher pelo efeito e pela função da tela, não pela quantidade de demos.
2. Preferir copiar um componente pequeno quando isso reduz dependências e facilita ownership.
3. Registrar engine real (CSS, Motion, GSAP, Canvas, WebGL ou WebGPU) e o custo esperado.
4. Preservar semântica HTML, teclado, foco, prefers-reduced-motion, toque e fallback estático.
5. Medir CPU/GPU, memória, DPR e impacto em Core Web Vitals no artefato real.
6. Conferir licença do código, shaders, fontes e assets separadamente; páginas de demonstração não são prova de licença.
7. Para Canvas/WebGL/WebGPU, carregar sob demanda e não substituir conteúdo que precisa ser selecionável ou indexável.
