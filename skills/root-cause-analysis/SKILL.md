---
name: root-cause-analysis
description: "Investigar causas de problemas operacionais, comerciais ou de produto separando sintomas, mecanismos, fatores contribuintes e evidência causal."
---

# root-cause-analysis

## Objetivo

Investigar por que um resultado ocorreu sem parar na primeira explicação plausível. A skill distingue correlação, mecanismo causal, fator contribuinte, gatilho e condição de fundo.

## Quando usar

- queda de conversão, receita, retenção ou produtividade;
- falha operacional;
- problemas recorrentes;
- incidentes não estritamente técnicos;
- quando há múltiplas explicações concorrentes.

## Workflow

1. Definir o desvio observado: métrica, período, população e baseline.
2. Separar sintoma de resultado intermediário.
3. Construir uma árvore de hipóteses causal mínima.
4. Para cada hipótese, registrar:
   - mecanismo esperado;
   - evidência que a suporta;
   - evidência que a enfraqueceria;
   - dados necessários.
5. Procurar mudanças temporais, segmentação e pontos de ruptura.
6. Testar explicações alternativas antes de aceitar a primeira narrativa.
7. Distinguir:
   - causa necessária;
   - causa suficiente;
   - fator contribuinte;
   - confounder;
   - coincidência.
8. Quando houver dados observacionais, não declarar causalidade sem desenho adequado.
9. Definir correção/intervenção e sinal esperado se a hipótese estiver correta.
10. Verificar depois da intervenção.

## Ferramentas conceituais

- 5 Whys para exploração inicial, não como prova;
- fault tree / issue tree;
- causal graph;
- before/after segmentado;
- experiment-design quando intervenção controlada for possível;
- métodos causais formais somente quando dados/assunções sustentarem.

## Regras

- Correlação temporal não prova causa.
- Uma causa raiz pode ser sistêmica e ter múltiplos fatores contribuintes.
- Não escolher culpado humano como atalho para mecanismo.
- Resultados de causal inference dependem de assumptions; explicitar confounders e limitações.

## Integração

experiment-design, discovery-research-synthesis, product-metrics-diagnostics, social-analytics, web-analytics-ga4 e after-action-review.

## Origem metodológica

Adaptada de práticas de causal inference representadas por DoWhy, EconML e causal-learn, convertidas para investigação operacional sem exigir bibliotecas estatísticas.
