---
name: experiment-design
description: "Desenhar experimentos falsificáveis com hipótese, métrica primária, guardrails e critérios de decisão anteriores aos resultados."
---

# experiment-design

## Objetivo

Desenhar experimentos falsificáveis com hipótese explícita, métrica primária, guardrails, magnitude relevante e critérios de decisão definidos antes dos resultados.

## Workflow

1. Formular hipótese com causa, efeito, magnitude e mecanismo.
2. Definir exatamente uma métrica primária e guardrails quando apropriado.
3. Definir antes do teste o que faria a equipe não adotar a mudança.
4. Separar significância estatística de relevância prática.
5. Calcular ou estimar amostra e duração quando os dados permitirem.
6. Evitar A/B test para bugs objetivos, compliance ou decisões não reducíveis a métrica operacional.
7. Registrar resultado e incerteza sem cherry-picking.

## Experimentos de otimização técnica

Para performance, memória ou throughput, definir baseline reproduzível e níveis de equivalência antes de medir velocidade.

Tiers úteis:
- off/stock: implementação original pinada;
- exact: mesmo resultado segundo critério definido, mais rápido;
- fast: diferença numérica aceita e documentada, com quality guardrail;
- big/memory: prioriza peak memory ou capacidade.

Regras:
- fixar versão, hardware, runtime, inputs e seeds quando relevantes;
- registrar qual modo e quais otimizações realmente ficaram ativos;
- se uma otimização não puder engajar, não fazer fallback silencioso e contar como tratamento;
- medir qualidade/correção junto com latency, throughput ou memory;
- separar unsupported hardware/cell de regressão;
- registrar coverage e fallback rate em dispatch por shape/device;
- declarar se o ganho é end-to-end ou apenas de uma etapa.

## Regras

Quando faltar dado, planejar e declarar o que precisa ser medido; não inventar baseline, power ou MDE.

## Fila de experimentos

- ligar experimento às assumptions/evidence;
- preferir ação reversível quando a confiança é baixa;
- não transformar score em decisão automática;
- explicitar o que falsificaria a recomendação.

## Referências

Adaptada de https://github.com/rampstackco/claude-skills/tree/main/skills/experiment-design.

Tiers de otimização, refusal contract e run accounting adaptados de https://github.com/anthropics/uplifting-biomolecular-modeling.

Origem local: [experiment-design.docx](../experiment-design.docx).
