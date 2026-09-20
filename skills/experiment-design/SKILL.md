---
name: experiment-design
description: "Desenhar experimentos falsificáveis com hipótese, métrica primária, guardrails e critérios de decisão anteriores aos resultados."
---

# experiment-design

## Objetivo

Desenhar experimentos falsificáveis com hipótese explícita, métrica primária, guardrails, magnitude relevante e critérios de decisão definidos antes dos resultados.

## Quando usar

Desenhar experimentos falsificáveis com hipótese, métrica primária, guardrails e critérios de decisão anteriores aos resultados.

## Workflow

1. Formular hipótese com causa, efeito, magnitude e mecanismo.
2. Definir exatamente uma métrica primária e 3–5 guardrails quando apropriado.
3. Definir antes do teste o que faria a equipe **não** adotar a mudança.
4. Separar significância estatística de relevância prática.
5. Calcular/estimar amostra e duração a partir de baseline, MDE, poder e sazonalidade quando os dados permitirem.
6. Evitar A/B test para bugs objetivos, obrigações legais/compliance ou decisões estratégicas que não são reducíveis a uma métrica operacional.
7. Registrar resultado, incerteza e decisão sem cherry-picking pós-hoc.

## Regras

Quando faltar dado para cálculo estatístico, planejar o experimento e declarar o que ainda precisa ser medido; não inventar poder, baseline ou MDE.

## Fila de experimentos

Quando a síntese gerar várias oportunidades:

- converter apenas as mais importantes em experimentos;
- ligar cada experimento aos evidence ids/assumptions que pretende testar;
- usar uma próxima ação reversível quando a confiança ainda for baixa;
- não transformar score de oportunidade em decisão automática;
- explicitar o que poderia falsificar a recomendação.

## Referências

Adaptada de [rampstackco/claude-skills · experiment-design](https://github.com/rampstackco/claude-skills/tree/main/skills/experiment-design).

Origem local: [experiment-design.docx](../experiment-design.docx).
