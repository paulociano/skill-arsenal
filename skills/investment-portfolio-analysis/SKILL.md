---
name: investment-portfolio-analysis
description: "Analisar carteiras de investimento por retorno, risco, drawdown, alocação, concentração, benchmark, contribuição de risco e rebalanceamento, evitando transformar otimização matemática em recomendação automática."
---

# Investment & Portfolio Analysis

## Objetivo

Avaliar portfólios como sistemas de exposição, risco e objetivos, distinguindo performance histórica, risco estimado e decisões futuras.

## Quando usar

- portfolio review;
- allocation;
- rebalance;
- benchmark;
- risk contribution;
- diversification;
- drawdown;
- optimization;
- client investment review.

## Workflow

1. **Ground**
   - objetivo;
   - horizonte;
   - moeda base;
   - liquidity needs;
   - constraints;
   - benchmark;
   - tax/account wrappers quando relevantes.

2. **Positions**
   - weights por asset/security;
   - cash;
   - duplicated exposures;
   - concentration;
   - look-through quando possível.

3. **Performance**
   - TWR quando medir estratégia/gestão;
   - MWR/IRR quando fluxos do investidor importam;
   - periods comparáveis;
   - benchmark na mesma moeda/período.

4. **Risk**
   - volatility;
   - max drawdown;
   - downside metrics;
   - VaR/CVaR somente com assumptions declaradas;
   - factor/asset-class exposure;
   - concentration;
   - liquidity.

5. **Contribution**
   - retorno por posição/asset class;
   - contribuição de risco;
   - winners não são automaticamente melhores holdings.

6. **Rebalancing**
   - current vs target;
   - drift;
   - transaction costs;
   - taxes;
   - liquidity;
   - cash flows;
   - user/IPS constraints.
   - não executar trades sem autorização explícita.

7. **Optimization**
   - inputs: expected returns, covariance/risk model, constraints;
   - compare com equal-weight/reference portfolio;
   - testar sensitivity/estimation error;
   - incluir turnover/weight bounds;
   - não tratar optimizer output como decisão final.

8. **Scenario/stress**
   - rates;
   - equity shock;
   - FX;
   - inflation;
   - credit spread;
   - custom historical/hypothetical scenarios.

9. **Review output**
   - current state;
   - key concentrations/risks;
   - drift;
   - alternative actions;
   - consequences/trade-offs;
   - missing information.

## Guardrails

- retorno passado não é previsão;
- volatilidade não captura todo risco;
- correlação pode mudar;
- expected returns são assumptions;
- otimização é altamente sensível a inputs;
- recomendações reguladas/personalizadas exigem contexto e regras aplicáveis;
- preservar decisão humana.

## Dados no ponto do tempo, debate e checagem de decisões

Para analisar um ativo numa data passada, testar uma regra ou revisar decisões já tomadas:

1. **Ponto do tempo.** Usar só o que era público na data da análise: demonstrações **como foram arquivadas** naquela data (não a versão reapresentada depois), sem exercício encerrado mas ainda não publicado, e sem cadastro atual da empresa (nome, setor, classificação mudam). Fonte que data pelo período coberto e não pela publicação, ou operação de insider datada pela execução e não pelo registro, fica fora de análise histórica. A decisão entra no primeiro fechamento **depois** da data, se a análise leu notícias do próprio dia.
2. **Identidade antes da análise.** Resolver ticker → empresa de forma determinística e ancorar preços e indicadores citados num snapshot verificado, para não analisar a empresa errada nem inventar cotação.
3. **Debate estruturado.** Para tese de compra/venda, construir o melhor caso a favor e o melhor caso contra a partir dos mesmos relatórios, cada um respondendo diretamente aos pontos do outro, com julgamento explícito; depois, a mesma proposta passa por leituras de risco agressiva, neutra e conservadora antes da decisão. Relatório ausente é declarado ausente, não preenchido.
4. **Carteira real ou genérica.** Sem a posição atual do cliente, escrever a orientação para um leitor genérico; "carteira vazia" é diferente de "carteira não informada".
5. **Liquidar decisões.** Registrar cada decisão com data, horizonte e nota; quando o horizonte vencer, medir retorno realizado e alfa contra o benchmark do ativo, agrupar por nota e só então avaliar se o processo decide bem. Uma decisão isolada não diz nada sobre a qualidade do processo.
6. **Variação esperada.** Análise com LLM varia entre execuções (amostragem, notícias que mudam); não apresentar um resultado como reprodutível nem como recomendação.

Adaptado de [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) (Apache-2.0; seções "Fundamentals as filed", "Evaluating decisions over time", "Reproducibility", `dataflows/date_window.py`, `agents/researchers` e `agents/risk_mgmt`), avaliado em 2026-11-10. Não instala o framework nem executa ordens; o próprio projeto declara uso para pesquisa, não recomendação.

## Integração

`personal-financial-planning`, `financial-modeling-valuation`, `scenario-forecasting`, `evidence-claim-verification` e `dashboard-design`.

## Provenance

Consolidada de Riskfolio-Lib, PyPortfolioOpt, QuantStats, backtesting/portfolio libraries e workflows de wealth-management/portfolio-rebalance de open-financial-agents.

## Revisão longitudinal de tese e evidência

Quando o usuário fornecer duas fotografias temporais de pesquisa ou carteira, comparar apenas observações realmente comparáveis:

1. Identificar ativo, fonte, revisão, data/hora, moeda, janela, metodologia de score e premissas de cada snapshot.
2. Classificar alterações em fatos verificáveis, opinião de analistas, inferências, tese, riscos e lacunas de dados; não confundir mudança de preço com validação de uma tese.
3. Tornar explícitas alterações de metodologia, cobertura, versão ou universo que impeçam comparação direta; nesses casos, registrar `não comparável` em vez de fabricar deltas.
4. Para notícia ou relatório, separar evento reportado, ativo afetado, mecanismo causal hipotético, evidência contrária e próximos checkpoints.
5. Informar o que mudou, o que continua incerto, qual premissa da tese precisa ser revisitada e qual evidência futura discriminaria as hipóteses.
6. Não tratar scores proprietários como equivalentes e não trocar chamadas pagas por dados de demonstração. Um provider como AlphaGBM depende de acesso real, autorização de consumo e backend disponível. Nunca executar trades a partir da revisão.

**Origem adaptada:** https://github.com/AlphaGBM/skills/blob/main/skills/core/alphagbm-investment-review/SKILL.md e https://github.com/AlphaGBM/skills/blob/main/skills/core/alphagbm-news-impact/SKILL.md.
