---
name: scenario-forecasting
description: "Construir forecasts e cenários com baseline, backtesting, intervalos, premissas e gatilhos de atualização sem transformar projeção em certeza."
---

# scenario-forecasting

## Objetivo

Projetar previsões úteis para decisão combinando forecast quantitativo quando há série histórica com cenários explícitos quando o futuro depende de premissas, intervenções ou incerteza estrutural.

## Quando usar

- demanda, receita, pipeline ou capacidade;
- planejamento mensal/trimestral/anual;
- cenários base/upside/downside;
- projeções com sazonalidade;
- necessidades de staffing/estoque/orçamento.

## Workflow

1. Definir variável, horizonte, frequência e decisão suportada.
2. Estabelecer baseline ingênuo antes de modelos sofisticados.
3. Inspecionar:
   - tendência;
   - sazonalidade;
   - rupturas;
   - missing/outliers;
   - regressoras externas.
4. Separar treino/validação respeitando ordem temporal.
5. Usar backtesting/rolling validation quando houver dados suficientes.
6. Comparar modelos contra baseline por métricas adequadas.
7. Produzir intervalo/probabilidade quando possível, não apenas ponto.
8. Para incertezas não capturáveis pela série, construir cenários com premissas explícitas.
9. Definir gatilhos que invalidam ou atualizam o cenário.
10. Registrar forecast vintage e comparar previsto vs realizado.

## Cenário vs forecast

- **forecast** estima distribuição futura a partir de dados/modelo;
- **scenario** explora futuros condicionais a premissas;
- **target** é objetivo;
- **budget** é plano;
- nenhum deles deve ser apresentado como fato futuro.

## Regras

- Não escolher modelo pelo ajuste in-sample.
- Não extrapolar além do horizonte defensável sem alerta.
- Mudança estrutural pode tornar histórico pouco representativo.
- Intervalos muito estreitos sem base são falsa precisão.
- Sempre comparar com um baseline simples.
- Modelos avançados só entram se melhorarem validação ou resolverem requisitos específicos.

## Integração

decision-analysis, product-metrics-diagnostics, financial/business analysis, experiment-design e dashboard-design.

## Origem metodológica

Adaptada de StatsForecast, MLForecast, Darts, sktime, GluonTS e Prophet, preservando baseline, backtesting, probabilistic forecasting e covariates sem exigir uma biblioteca específica.
