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
- typographic-composition
- scroll-storytelling
- ui-motion-design
- interaction-polish
- motion-asset-engineering
- cinematic-visual-direction
- creative-web-effects
- shader-graphics-engineering
- gsap-animation
- runtime-ui-verification
- web-quality-audit

## Workflow

1. **Direction** — resolver visual thesis e signature elements com design-direction.
2. **Structure** — web-design-engineer define macroestrutura/greybox; landing-craft entra quando a superfície é conversão.
3. **Typography** — quando tipo tiver papel identitário, editorial ou cinético, typographic-composition define hierarquia e pode consultar seu radar de fontes modernas.
4. **Narrative movement** — scroll-storytelling somente quando scroll participa da narrativa.
5. **Motion language** — ui-motion-design define função, personalidade e tecnologia antes da implementação.
6. **Creative layer** — quando a experiência pedir linguagem de câmera, vídeo ou continuidade entre cenas, cinematic-visual-direction define os shots; depois escolher motion-asset-engineering ou creative-web-effects conforme o efeito seja asset ou runtime gráfico.
7. **Physics/procedural gate** — springs, partículas, forças, Canvas/WebGL ou simulações entram apenas quando o comportamento exige física/procedural real. Definir parâmetros observáveis e uma forma de verificar o efeito, evitando movimento aleatório usado como substituto de direção.
8. **Implementation** — shader-graphics-engineering/gsap-animation apenas quando necessários.
9. **Polish** — interaction-polish após estrutura e conteúdo estarem estáveis.
10. **Verify** — runtime-ui-verification e web-quality-audit com desktop/mobile, keyboard, touch, reduced motion e budget de performance.
11. **Cut** — remover efeitos cujo custo ou competição visual não justifique benefício.

## Budgets de complexidade

Antes de adicionar cada camada expressiva, responder:
- qual função ela cumpre?
- qual fallback existe?
- qual custo de JS/GPU/runtime?
- como se comporta em mobile e reduced motion?
- o site ainda funciona se essa camada falhar?
- se usa física/procedural, qual comportamento observável prova que não é drift sintético?

## Regra de parcimônia

Um site contemporâneo pode usar zero WebGL e zero smooth scroll. Não ativar especializações porque estão na stack. A menor composição que entrega a direção é a correta.

## Origem metodológica

Stack sintetizada da segunda avaliação de creative web, incluindo Motion, Lenis, r3f-scroll-rig, Theatre.js, Rive/Lottie, React Bits, Animate UI, Magic UI, Radix/Floating UI e ecossistema pmndrs. Enriquecida com princípios portáveis de LottieFiles/motion-design-skill e feitangyuan/motion-web, sem importar seus scripts, verificadores ou runtimes como dependências.
