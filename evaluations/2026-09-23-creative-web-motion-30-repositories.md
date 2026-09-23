# Avaliação — 30 repositórios de creative web, motion, WebGL e UI contemporânea

Data: 2026-09-23

## Escopo

Segunda leva de pesquisa voltada a websites contemporâneos, motion graphics, scroll storytelling, microinterações, WebGL/3D, assets animados e design engineering. A avaliação foi comparada ao ARSENAL INDEX após a expansão anterior de web/social.

## Critérios

- **A** — metodologia/capacidade que muda comportamento do Arsenal.
- **B** — boa referência ou técnica para enriquecer owner existente.
- **C** — pouco ganho incremental ou catálogo visual sem método novo.
- **D** — valor técnico dependente de runtime/biblioteca/toolchain específica.

## Resultado

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 1 | pmndrs/react-three-fiber | A/D | Fonte principal para composição React + Three; incorporar routing de runtime, não criar wrapper de API. |
| 2 | pmndrs/drei | B/D | Catálogo técnico importante para R3F; usar sob demanda em creative effects/shader work. |
| 3 | pmndrs/postprocessing | A/D | Incorporar conceito de postprocessing com budgets e legibilidade. |
| 4 | pmndrs/react-postprocessing | B/D | Adapter React; sem skill separada. |
| 5 | oframe/ogl | A/D | Runtime WebGL enxuto; adicionar como opção quando Three seria excessivo. |
| 6 | martinlaxenaire/curtainsjs | A/D | Padrão DOM-to-WebGL útil para imagens/vídeos; incorporar metodologia. |
| 7 | shuding/cobe | B/D | Exemplo de efeito assinatura pequeno; referência, sem owner próprio. |
| 8 | 14islands/r3f-scroll-rig | A/D | Adotar progressive enhancement DOM/WebGL e sincronização por proxies/observers. |
| 9 | pmndrs/uikit | D | UI em cena 3D; nicho técnico, manter como referência. |
| 10 | akella/webGLImageTransitions | B/D | Repertório para image transitions/shaders; sem skill própria. |
| 11 | motiondivision/motion | A | Expandir ui-motion-design para gestures, springs, layout transitions e Motion. |
| 12 | pmndrs/react-spring | B/D | Referência de spring physics e motion interruptível. |
| 13 | theatre-js/theatre | A/D | Incorporar paradigma de timeline/choreography visual, sem exigir editor. |
| 14 | rive-app/rive-wasm | A/D | Criar routing para assets interativos/state machines. |
| 15 | airbnb/lottie-web | A/D | Routing para assets de timeline exportados; não importar toolchain After Effects. |
| 16 | tsparticles/tsparticles | B/D | Ambient/procedural effects; referência, não padrão visual. |
| 17 | darkroomengineering/lenis | A/D | Adotar distinção smooth scroll vs storytelling e sync de loops. |
| 18 | locomotivemtl/locomotive-scroll | B/D | Referência comparativa de scroll/parallax; não owner. |
| 19 | barbajs/barba | B/D | Page transition continuity útil; incorporar no raciocínio de navigation motion. |
| 20 | wagerfield/parallax | B | Referência de layered/pointer parallax com parcimônia. |
| 21 | ibelick/motion-primitives | A | Fonte forte para microinterações e padrões de polish. |
| 22 | imskyleen/animate-ui | A | Catálogo de primitives/effects animados; incorporar review de interaction polish. |
| 23 | DavidHDev/react-bits | A/D | Fonte para text/background/micro/texture effects; incorporar repertório e budgets. |
| 24 | magicuidesign/magicui | B | Catálogo contemporâneo de efeitos; usar como repertório, não identidade pronta. |
| 25 | kokonut-labs/kokonutui | B | Ponte entre product UI e creative UI; referência de composição. |
| 26 | shadcn/originui | B | Repertório de UI funcional contemporânea; sem nova skill. |
| 27 | shadcn-ui/ui | B | Owner shadcn já existe; manter atualização por versão real. |
| 28 | shadcn-ui/lint | A/B | Já incorporado em governance/shadcn; manter contratos verificáveis. |
| 29 | radix-ui/primitives | A/B | Base comportamental/acessível para interação; alimentar interaction-polish. |
| 30 | floating-ui/floating-ui | A/B | Padrões de positioning/collision/accessibility para contextual UI. |

## Mudanças adotadas

### Novas skills
- scroll-storytelling
- interaction-polish
- motion-asset-engineering
- creative-web-effects

### Nova stack
- creative-web-engineering

### Skills atualizadas
- ui-motion-design
- web-design-engineer
- shader-graphics-engineering

## Arquitetura resultante

### Creative web
design-direction → web-design-engineer → [scroll-storytelling] → ui-motion-design → [motion-asset-engineering | creative-web-effects] → interaction-polish → runtime/web-quality verification.

### Separações importantes

1. **Smooth scroll ≠ scroll storytelling.**
2. **Motion design ≠ biblioteca de animação.**
3. **Motion asset ≠ animação programática.**
4. **Creative effect ≠ shader obrigatório.**
5. **Polish ≠ redesign estrutural.**
6. **WebGL complementa DOM; não deve substituir conteúdo semântico por padrão.**

## Segurança, licença e portabilidade

- Nenhum installer ou exemplo externo foi executado.
- Repositórios de runtime foram tratados como fontes técnicas; dependências só devem ser usadas se já existirem ou forem justificadas no projeto.
- Toolchains autorais (After Effects plugins, editores visuais, CLIs) não foram importadas como requisito.
- Catálogos copy-paste continuam sujeitos às licenças individuais e não devem ser copiados em massa.
- React Bits declara MIT + Commons Clause; usar metodologia/repertório não implica redistribuir componentes.
- Efeitos GPU, smooth scroll e loops animados exigem fallback, reduced motion e verificação de performance.

## Fontes principais

- https://github.com/pmndrs/react-three-fiber
- https://github.com/pmndrs/drei
- https://github.com/pmndrs/postprocessing
- https://github.com/oframe/ogl
- https://github.com/martinlaxenaire/curtainsjs
- https://github.com/14islands/r3f-scroll-rig
- https://github.com/motiondivision/motion
- https://github.com/theatre-js/theatre
- https://github.com/rive-app/rive-wasm
- https://github.com/airbnb/lottie-web
- https://github.com/darkroomengineering/lenis
- https://github.com/barbajs/barba
- https://github.com/ibelick/motion-primitives
- https://github.com/imskyleen/animate-ui
- https://github.com/DavidHDev/react-bits
- https://github.com/magicuidesign/magicui
- https://github.com/kokonut-labs/kokonutui
- https://github.com/shadcn/originui
- https://github.com/radix-ui/primitives
- https://github.com/floating-ui/floating-ui

## Veredito

A segunda leva justificou 4 skills novas e 1 stack, porque as quatro capabilities têm contratos distintos. O restante foi mantido como referência técnica ou incorporado em owners existentes para evitar Arsenal inchado.
