---
name: statistical-data-analysis
description: "Analisar uma planilha ou base de dados com estatística: perfil dos dados primeiro, checagem de premissas, escolha do teste ou modelo, execução em código e saída em tabela, gráfico e parágrafo com tamanho de efeito e limites."
---

# statistical-data-analysis

## Objetivo

Responder perguntas sobre dados (comparar grupos, achar relação, explicar variação, testar diferença) escolhendo o método **depois** de olhar os dados, com cálculo em código e interpretação honesta.

## Quando usar

- "Analisa essa planilha", "tem diferença entre A e B?", "o que explica X?", "isso é significativo?", "faz uma regressão".
- Dados de clientes, vendas, pesquisas, treinamentos, finanças pessoais ou do time.

## Quando não usar

- Desenhar um teste A/B antes de coletar → `experiment-design`.
- Diagnóstico de métrica de produto e conferência de SQL → `product-metrics-diagnostics`.
- Previsão de cenários → `scenario-forecasting`.

## Workflow

1. **Pergunta.** Qual decisão a análise informa; variável resposta, variáveis explicativas, unidade de análise, período, população.
2. **Perfil dos dados (sempre antes de analisar), por código.** Tamanho da amostra; tipos (contínua, categórica, data); faltantes por variável; duplicatas; valores impossíveis; outliers; distribuição das variáveis-chave (média e desvio, mediana, assimetria). Emitir alertas: "variável X com 15% faltante", "Y muito assimétrica", "amostra pequena para o subgrupo Z".
3. **Premissas.** Normalidade (Shapiro-Wilk em amostra pequena; assimetria e curtose ou gráfico em amostra grande), homogeneidade de variâncias, independência das observações, linearidade e multicolinearidade em regressão, contagem esperada por célula em qui-quadrado.
4. **Escolha do método** pela pergunta × tipo de dado × premissas:
   - comparar 2 grupos: t de Student/Welch ou Mann-Whitney; pareado: t pareado ou Wilcoxon;
   - 3+ grupos: ANOVA/Welch ou Kruskal-Wallis, com comparações múltiplas corrigidas;
   - categórica × categórica: qui-quadrado ou exato de Fisher;
   - relação entre contínuas: Pearson ou Spearman;
   - explicar uma resposta: regressão linear, logística (sim/não) ou de contagem; checar resíduos;
   - dizer por que o método foi escolhido e qual seria o plano B.
5. **Execução** em Python (pandas, scipy, statsmodels) ou R, com código guardado para reproduzir.
6. **Saída em trio:** tabela de resultados; gráfico adequado (ver `dashboard-design`); parágrafo em linguagem simples com estatística, valor-p, **tamanho de efeito e intervalo de confiança**, e o que isso significa para a decisão.
7. **Limites.** Correlação não é causa; dados observacionais não provam efeito; muitas comparações inflacionam falso positivo; resultado "não significativo" não prova igualdade; amostra e período limitam a generalização.

## Guardrails

- Números só de código executado, nunca estimados no texto.
- Não remover outliers ou faltantes em silêncio: dizer a regra e mostrar o efeito.
- Não escolher o teste depois de ver qual dá "significativo".
- Dados pessoais: usar o mínimo, preferir agregados, não expor indivíduos.

## Integração

`product-metrics-diagnostics`, `experiment-design`, `dashboard-design`, `verify-before-claim`.

## Origem

Adaptado de [TerryFYL/claude-statistical-analysis-skill](https://github.com/TerryFYL/claude-statistical-analysis-skill) (MIT; "diagnóstico antes da análise": perfil dos dados, checagem de premissas, seleção do método e saída em tabela + figura + parágrafo), avaliado em 2026-11-10. Guia de escolha de testes reescrito a partir de prática estatística padrão. Garantia `static_only`.
