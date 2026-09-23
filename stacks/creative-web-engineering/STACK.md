---
name: creative-web-engineering
description: Orquestra direção, estrutura, scroll, motion, microinterações e gráficos criativos para websites contemporâneos de alta expressão com verificação de acessibilidade e performance.
---

# Creative Web Engineering

## Objetivo

Criar experiências web expressivas sem confundir "moderno" com excesso de efeitos. A stack organiza o caminho da ideia ao runtime e aciona apenas as especializações necessárias.

## Skills candidatas

- design-direction
- web-design-engineer
- landing-craft
- scroll-storytelling
- ui-motion-design
- interaction-polish
- motion-asset-engineering
- creative-web-effects
- shader-graphics-engineering
- gsap-animation
- runtime-ui-verification
- web-quality-audit

## Workflow

1. **Direction** — resolver visual thesis e signature elements com design-direction.
2. **Structure** — web-design-engineer define macroestrutura/greybox; landing-craft entra quando a superfície é conversão.
3. **Narrative movement** — scroll-storytelling somente quando scroll participa da narrativa.
4. **Motion language** — ui-motion-design define funções e tecnologia.
5. **Creative layer** — escolher motion-asset-engineering ou creative-web-effects conforme o efeito seja asset ou runtime gráfico.
6. **Implementation** — shader-graphics-engineering/gsap-animation apenas quando necessários.
7. **Polish** — interaction-polish após estrutura e conteúdo estarem estáveis.
8. **Verify** — runtime-ui-verification e web-quality-audit com desktop/mobile, keyboard, touch, reduced motion e budget de performance.
9. **Cut** — remover efeitos cujo custo ou competição visual não justifique benefício.

## Budgets de complexidade

Antes de adicionar cada camada expressiva, responder:
- qual função ela cumpre?
- qual fallback existe?
- qual custo de JS/GPU/runtime?
- como se comporta em mobile e reduced motion?
- o site ainda funciona se essa camada falhar?

## Regra de parcimônia

Um site contemporâneo pode usar zero WebGL e zero smooth scroll. Não ativar especializações porque estão na stack. A menor composição que entrega a direção é a correta.

## Origem metodológica

Stack sintetizada da segunda avaliação de creative web, incluindo Motion, Lenis, r3f-scroll-rig, Theatre.js, Rive/Lottie, React Bits, Animate UI, Magic UI, Radix/Floating UI e ecossistema pmndrs.
