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
