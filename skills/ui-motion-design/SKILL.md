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
- **interactive state machine** — componente visual cujo estado, transições, inputs e dados fazem parte do comportamento da interface;
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
   - Em morphs interruptíveis, retomar da forma atualmente renderizada em vez de reiniciar da origem quando isso preserva continuidade.
   - Em transições dependentes de assets/fontes, preservar layout e função com fallback estático quando o morph não puder ser resolvido.
9. Para componentes interativos ricos, explicitar primeiro o contrato de estados e dados (ex.: ready → active → success/error → next) antes de decidir se ele vive em React/CSS, Motion/GSAP ou em uma state machine autorada como Rive.
10. Escolher tecnologia pelo requisito:
   - CSS/WAAPI para transições simples;
   - Motion quando layout transitions, gestures, springs e animação React declarativa forem a melhor aderência;
   - gsap-animation para timelines, scroll e coordenação complexa;
   - motion-asset-engineering para Rive/Lottie/SVG/video;
   - shader-graphics-engineering para motion procedural de GPU;
   - biblioteca já instalada quando atende sem migração.
11. Para experiências dirigidas por scroll, usar scroll-storytelling para arquitetura narrativa antes da implementação.
12. Verificar em runtime fluidez, foco, input por teclado/toque e ausência de bloqueio de conteúdo.
13. Remover loops decorativos ou efeitos que aumentam custo sem ajudar a tarefa.

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

Adaptada de rbaumier/skills, greensock/gsap-skills, Motion, react-spring, Theatre.js, MengTo/Skills, podo/design-agent-skills e LottieFiles/motion-design-skill. Continuidade de morph interruptível e fallback funcional refinados a partir de KickNext/morphnext. Preserva função, personalidade e coreografia portáveis, removendo presets rígidos e dependências específicas.

## Motion semântico e orçamento de renderização

Para efeitos ricos inspirados em motion/Three.js, preservar intenção antes de aparência:
1. Vincular estados animados a estados reais de produto (loading, selected, processing, focus, success, failure), sem glow/loop permanente que simule atividade inexistente.
2. Escolher CSS/SVG antes de canvas/WebGL quando isso atingir o efeito; explicitar custo de camadas, draw calls, memória, DPR, frame-time e fallback.
3. Pausar simulações fora do viewport, ao ocultar a página e quando reduced-motion exigir, limpando rAF/listeners/observers na desmontagem.
4. Para scroll, manter um único controlador do progresso, sem disputa entre biblioteca de smooth scroll e scroll nativo; garantir navegação por teclado e restauração.
5. Para emissores de cursor/partículas, basear espaçamento em distância percorrida e reciclar pool em vez de alocação sem limite.
6. Verificar o resultado no dispositivo-alvo e separar captura visual de evidência de performance; não alegar medição que não ocorreu.

Origem: metodologias analisadas individualmente em `MengTo/Skills/agent-skills/web-design` (2026-10-15). Componentes terceiros e efeitos WebGL não são dependências obrigatórias.

## Vocabulário de movimento ancorado em demonstração (motion-prompt)

Quando o pedido de animação for vago, identificar um efeito por nome, amostra visual e função antes de selecionar código. Descrever sujeito, câmera versus zoom, eixo, direção, amplitude, duração, easing, stagger e interrupção. Usar demonstração apenas como referência, não equivalência garantida. Adaptar ao projeto e verificar acessibilidade, reduced motion, layout, responsividade e mudanças de estado. Escolher poucos efeitos com propósito. Fonte: https://github.com/showheyohtaki/motion-prompt (2026-10-18); galeria e skill Node permanecem externas.

## React View Transitions: continuidade espacial (Vercel, 2026-10-19)

Em projetos React/Next.js que suportem a API na versão realmente instalada, considerar View Transitions nativas antes de introduzir uma nova biblioteca de animação. Usar somente para comunicar continuidade, não como padrão decorativo de toda navegação:

1. Inventariar relações list→detail, mudanças de posição em listas, enter/exit e revelações assíncronas; escolher transitions por propósito.
2. Para shared elements, exigir identidade estável e nome único por elemento; verificar que origem e destino participam da mesma transição. Não usar o mesmo identificador em duas instâncias simultaneamente montadas.
3. Separar animação de navegação da revelação posterior por Suspense; tipos de direção usados na rota não necessariamente persistem para o conteúdo carregado depois.
4. Utilizar `default="none"` deliberadamente em boundaries cujo background update não deveria animar; checar também `share` e `update` para evitar desabilitar acidentalmente a transição desejada.
5. Reservar slide direcional para hierarquia e sequências ordenadas; tabs e transições laterais não devem simular profundidade inexistente.
6. Validar compatibilidade exata entre React, Next.js e browser antes de recomendar `<ViewTransition>`, `addTransitionType` ou `transitionTypes`. APIs experimentais/canary não são defaults portáveis.
7. Respeitar reduced-motion, navegação por teclado, history/back-forward, estados de erro, fallback sem animação e interrupções.

**Fonte:** https://github.com/vercel-labs/agent-skills/tree/main/skills/react-view-transitions . Adaptada como decisão de motion independente do runtime Vercel ou de uma versão presumida do React.
