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

## Motion personality

Antes de escolher curvas e durações, descreva a personalidade do movimento em poucas propriedades observáveis, por exemplo: precisa ou elástica, contida ou energética, direta ou teatral, contínua ou em beats.

Use essa personalidade para manter coerência entre entradas, hover, feedback, transições e cenas. Ela deriva da marca, tarefa e frequência de uso; não é um preset estético.

Para sequências com vários elementos, planeje coreografia por:
1. elemento líder;
2. ordem de atenção;
3. overlap ou pausa intencional;
4. chegada/settling;
5. possibilidade de interrupção.

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
4. Definir função e, quando houver sistema de motion, uma personalidade coerente.
5. Escolher paradigma e timing/easing coerentes com função, personalidade e plataforma.
6. Preferir propriedades de composição como transform/opacity quando servirem ao efeito e reduzir layout thrash.
7. Planejar interrupção, reversão, resize, route change e unmount.
8. Garantir prefers-reduced-motion e alternativa funcional.
9. Escolher tecnologia pelo requisito:
   - CSS/WAAPI para transições simples;
   - Motion quando layout transitions, gestures, springs e animação React declarativa forem a melhor aderência;
   - gsap-animation para timelines, scroll e coordenação complexa;
   - motion-asset-engineering para Rive/Lottie/SVG/video;
   - shader-graphics-engineering para motion procedural de GPU;
   - biblioteca já instalada quando atende sem migração.
10. Para experiências dirigidas por scroll, usar scroll-storytelling para arquitetura narrativa antes da implementação.
11. Verificar em runtime fluidez, foco, input por teclado/toque e ausência de bloqueio de conteúdo.
12. Remover loops decorativos ou efeitos que aumentam custo sem ajudar a tarefa.

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
- Timeline autorada visualmente ainda precisa de ownership, fallback e verificação no runtime.
- Princípios de animação clássicos podem orientar peso, antecipação, continuidade e staging, mas não justificam teatralidade em UI frequente.

## Referências de componentes

Para exemplos concretos de motion e efeitos por stack, consultar [bibliotecas de componentes animados e efeitos](../creative-web-effects/references/animated-component-libraries.md). Escolher pelo comportamento e custo, não pela quantidade de demos.

## Integração

web-design-engineer, scroll-storytelling, interaction-polish, motion-asset-engineering, creative-web-effects, gsap-animation, runtime-ui-verification e web-quality-audit.

## Origem metodológica

Adaptada de rbaumier/skills, greensock/gsap-skills, Motion, react-spring, Theatre.js, MengTo/Skills, podo/design-agent-skills e LottieFiles/motion-design-skill. Preserva função, personalidade e coreografia portáveis, removendo presets rígidos e dependências específicas.
