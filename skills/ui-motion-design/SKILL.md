---
name: ui-motion-design
description: "Projetar e auditar motion de interface por função, timing, acessibilidade e custo antes de escolher CSS, Motion, GSAP, Rive ou outra tecnologia."
---

# ui-motion-design

## Objetivo

Decidir o que deve se mover, por quê, com qual intensidade e com qual paradigma antes de escolher a tecnologia de animação.

## Quando usar

- microinterações, transições, scroll effects, parallax e motion systems;
- revisão de interface que parece parada, excessiva ou inconsistente;
- quando várias tecnologias de animação seriam possíveis;
- quando o problema é de linguagem de movimento, não apenas de API.

## Funções de motion

Classifique cada animação por uma função principal:
- feedback;
- orientation;
- continuity;
- hierarchy;
- progress;
- narrative.

Se não houver função clara, a animação é candidata a remoção.

## Paradigmas

- **state transition** — mudança discreta de UI;
- **spring/gesture** — interação interruptível e física;
- **timeline** — sequência coreografada;
- **scroll-linked** — progresso dirigido por scroll;
- **asset playback** — animação autorada externamente;
- **procedural** — Canvas/WebGL/shader.

Escolha paradigma antes de biblioteca.

## Workflow

1. Inventariar estados, gatilhos e animações existentes.
2. Separar motion iniciado pelo usuário de motion automático.
3. Definir prioridades: ações críticas e navegação antes de decoração.
4. Escolher paradigma e timing/easing coerentes com a função.
5. Preferir propriedades de composição como transform/opacity quando servirem ao efeito e reduzir layout thrash.
6. Planejar interrupção, reversão, resize, route change e unmount.
7. Garantir prefers-reduced-motion e alternativa funcional.
8. Escolher tecnologia pelo requisito:
   - CSS/WAAPI para transições simples;
   - Motion quando layout transitions, gestures, springs e animação React declarativa forem a melhor aderência;
   - gsap-animation para timelines, scroll e coordenação complexa;
   - motion-asset-engineering para Rive/Lottie/SVG/video;
   - shader-graphics-engineering para motion procedural de GPU;
   - biblioteca já instalada quando atende sem migração.
9. Para experiências dirigidas por scroll, usar scroll-storytelling para arquitetura narrativa antes da implementação.
10. Verificar em runtime fluidez, foco, input por teclado/toque e ausência de bloqueio de conteúdo.
11. Remover loops decorativos ou efeitos que aumentam custo sem ajudar a tarefa.

## Regras

- Não migrar biblioteca sem necessidade explícita.
- Não adotar números rígidos de duration/stagger como verdade universal; contexto e plataforma importam.
- Scroll-linked motion não pode ser pré-requisito para compreender ou acessar conteúdo.
- Reduced motion deve preservar informação e ações.
- Motion deve ser testado no artefato real; código isolado não prova sensação ou performance.
- Spring não é automaticamente melhor que easing; use física quando interruptibilidade/continuidade justificar.
- Timeline autorada visualmente (por exemplo Theatre-like workflows) ainda precisa de ownership, fallback e verificação no runtime.

## Integração

web-design-engineer, scroll-storytelling, interaction-polish, motion-asset-engineering, creative-web-effects, gsap-animation, runtime-ui-verification e web-quality-audit.

## Origem metodológica

Adaptada de rbaumier/skills, greensock/gsap-skills, Motion, react-spring, Theatre.js, MengTo/Skills e podo/design-agent-skills, preservando princípios portáveis e removendo regras estéticas rígidas ou dependências específicas.
