---
name: insurance-actuarial-modeling
description: "Modelar seguros por exposure, frequência/severidade, pricing, credibility, reserving, experience studies, Monte Carlo e capital/risk metrics com assumptions e validação explícitas."
---

# Insurance & Actuarial Modeling

## Objetivo

Estruturar análise atuarial reproduzível para pricing, reserving e risco, distinguindo dados observados, assumptions, modelo e decisão atuarial.

## Quando usar

- insurance pricing;
- reserving/IBNR;
- loss triangles;
- loss ratio;
- frequency/severity;
- credibility;
- experience studies;
- actuarial risk simulation.

## Workflow

1. **Data contract**
   - exposure grain;
   - policy/claim dates;
   - earned premium;
   - paid/incurred;
   - limits/deductibles;
   - development period;
   - source and snapshot date.

2. **Experience**
   - loss ratio;
   - frequency;
   - severity;
   - expense ratio;
   - actual vs expected;
   - concentration/large claims.

3. **Trend**
   - claim frequency/severity trend;
   - seasonality;
   - inflation/social inflation;
   - exposure mix;
   - explicit projection horizon.

4. **Pricing**
   - indicated loss cost;
   - expenses;
   - profit/risk margin;
   - credibility;
   - rating relativities/GLM when applicable;
   - constraints/regulatory limits external to model.

5. **Reserving**
   - triangles;
   - chain ladder;
   - Bornhuetter-Ferguson/Cape Cod when justified;
   - Mack standard error;
   - bootstrap/predictive distribution;
   - residual/calendar-year diagnostics.

6. **Risk simulation**
   - frequency-severity;
   - dependence;
   - reinsurance;
   - VaR/TVaR;
   - scenario/stress;
   - reproducible random seeds.

7. **Validation**
   - holdout/rolling valuation where possible;
   - backtest reserve development;
   - stability;
   - model assumptions;
   - compare methods;
   - explain material overrides.

8. **Governance**
   - versioned assumptions;
   - source provenance;
   - sign-off;
   - statutory/accounting regime handled separately.

## Regras

- point reserve sem uncertainty pode ser incompleto;
- chain ladder exige development assumptions, não funciona por magia;
- past loss development may break under structural change;
- actuarial estimates are estimates, not booked truth;
- insurance regulation/accounting varies by jurisdiction and date.

## Integração

`credit-risk-underwriting`, `scenario-forecasting`, `financial-planning-analysis`, `retirement-income-planning`, `evidence-claim-verification`.

## Provenance

Consolidada do ecossistema OpenActuarial, ChainLadder e actuarialpy: experience, trend, credibility, pricing, reserving, bootstrap e risk simulation. Não exige packages externos.
