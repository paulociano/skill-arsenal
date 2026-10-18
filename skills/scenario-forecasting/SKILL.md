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

## Simulações de decisões com evidência aprovada (Scenario Lab, 2026-10-15)

Quando o problema exigir **ações e reações de múltiplos agentes ou organizações**, e não apenas extrapolação de séries, estruturar uma simulação condicional: (1) delimitar atores, horizonte, estados, opções e **resultados possíveis explicitamente excluídos** pelo modelo; (2) montar pacote de evidências com origem e data, separar fatos das hipóteses de comportamento e obter aprovação das premissas; (3) definir transições, utilidades e penalidades por consequências de segunda ordem, evitando recompensas que só favoreçam o benefício imediato; (4) explorar ramos com seeds/iterações e critérios documentados; (5) agrupar famílias de resultados sem tratar score interno ou frequência de ramos como probabilidade calibrada do mundo real; (6) testar replay histórico e cenários adversariais, discriminando regressão técnica de validade preditiva externa; (7) versionar evidence packet, domain rules, assumptions e resultados para revisão quando fatos mudarem.

Se um cenário terminal relevante (como escalada total) não estiver no espaço de estados, dizer que **a simulação não consegue encontrá-lo**, não que o considera improvável. Replays com evidências divergentes ou resultados muito concentrados devem reduzir confiança e motivar revisão. A implementação específica de MCTS/CLI não é requisito para aplicar essa metodologia. Referência: https://github.com/YSLAB-ai/scenario-lab (README e docs/limitations.md, versão experimental v0.1.0). Não apresentar simulação como previsão factual, aconselhamento de risco ou decisão profissional automatizada.

## Forecast multivariado e quantílico com modelos fundacionais (Timestral)

Quando séries e covariáveis justificarem modelo probabilístico multivariado: (1) definir targets, variates, frequência, horizonte e unidades; (2) distinguir covariáveis apenas históricas de conhecidas no futuro e categóricas, prevenindo leakage dos valores realizados em backtest; (3) comparar zero-shot com seasonal naive e métodos clássicos em rolling-origin backtesting idêntico; (4) avaliar quantis por pinball loss, cobertura e largura de intervalos, crossing e calibração por horizonte/série; (5) versionar pesos, preprocessing, splits e licenças; (6) só executar PyTorch/pesos quando realmente disponíveis. Benchmarks externos não demonstram superioridade nos dados do usuário. Fonte: https://github.com/mistralai/timestral (2026-10-18), código e pesos licenciados separadamente.
