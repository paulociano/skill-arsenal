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

## Gate de necessidade e frequência

Antes de implementar ou sugerir motion:

1. **Frequência** — quanto mais recorrente a ação, menor deve ser o motion. Atalhos de teclado, command palettes e navegação central podem exigir resposta instantânea sem transição.
2. **Propósito** — nomear a função: feedback, orientação espacial, indicação de estado, continuidade, explicação ou narrativa. Se não houver função clara, não animar.
3. **Função da superfície** — dados que o usuário precisa ler ou operar não devem se mover apenas por decoração.
4. **Custo temporal** — motion não deve fazer UI frequente parecer atrasada. Entradas ocasionais toleram mais tempo; delight fica reservado a momentos raros.
5. **Interrupção** — interações rápidas devem poder retarget/reverter sem reiniciar de forma brusca.

Ao procurar oportunidades em uma interface, registrar também candidatos deliberadamente rejeitados e o motivo. Um bom audit pode concluir que nenhuma animação nova é necessária.

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

Princípios de gate por frequência, propósito, função e rejeição explícita de candidatos adaptados de https://github.com/emilkowalski/skills, sem importar presets rígidos como verdade universal.

## Origem metodológica

Adaptada de rbaumier/skills, greensock/gsap-skills, Motion, react-spring, Theatre.js, MengTo/Skills e podo/design-agent-skills, preservando princípios portáveis e removendo regras estéticas rígidas ou dependências específicas.
