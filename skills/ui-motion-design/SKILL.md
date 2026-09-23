---
name: ui-motion-design
description: "Projetar e auditar motion de interface por função, timing, acessibilidade e custo antes de escolher a tecnologia de animação."
---

# ui-motion-design

## Objetivo

Decidir o que deve se mover, por quê e com qual intensidade antes de escolher CSS, GSAP, Framer Motion, Web Animations ou outra implementação.

## Quando usar

- microinterações, transições, scroll effects, parallax e motion systems;
- revisão de interface que parece parada, excessiva ou inconsistente;
- quando várias tecnologias de animação seriam possíveis;
- quando o problema é de linguagem de movimento, não apenas de API GSAP.

## Funções de motion

Classifique cada animação por uma função principal:
- feedback;
- orientation;
- continuity;
- hierarchy;
- progress;
- narrative.

Se não houver função clara, a animação é candidata a remoção.

## Workflow

1. Inventariar estados, gatilhos e animações existentes.
2. Separar motion iniciado pelo usuário de motion automático.
3. Definir prioridades: ações críticas e navegação antes de decoração.
4. Escolher timing/easing coerentes com a função, sem transformar heurísticas em standards universais.
5. Preferir propriedades de composição como transform/opacity quando servirem ao efeito e reduzir layout thrash.
6. Planejar interrupção, reversão, resize e unmount quando aplicável.
7. Garantir prefers-reduced-motion e alternativa funcional sem animação.
8. Escolher tecnologia pelo requisito:
   - CSS/WAAPI para transições simples;
   - gsap-animation para timelines, scroll e coordenação complexa;
   - biblioteca já instalada quando ela atende sem migração.
9. Verificar em runtime fluidez, foco, input por teclado/toque e ausência de bloqueio de conteúdo.
10. Remover loops decorativos ou efeitos que aumentam custo sem ajudar a tarefa.

## Regras

- Não migrar biblioteca sem necessidade explícita.
- Não adotar números rígidos de duration/stagger como verdade universal; contexto e plataforma importam.
- Scroll-linked motion não pode ser pré-requisito para compreender ou acessar conteúdo.
- Reduced motion deve preservar informação e ações.
- Motion deve ser testado no artefato real; código isolado não prova sensação ou performance.

## Integração

web-design-engineer, landing-craft, gsap-animation, runtime-ui-verification e web-quality-audit.

## Origem metodológica

Adaptada de rbaumier/skills, greensock/gsap-skills, MengTo/Skills e podo/design-agent-skills, preservando princípios portáveis e removendo regras estéticas rígidas ou dependências específicas.
