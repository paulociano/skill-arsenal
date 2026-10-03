---
name: retirement-income-planning
description: "Modelar aposentadoria e decumulação com household cash flows, longevidade, inflação, sequence risk, pensions, spending guardrails, Monte Carlo/historical stress tests e withdrawal strategies sem tratar probabilidade de sucesso como garantia."
---

# Retirement Income Planning

## Objetivo

Planejar transição da acumulação para decumulação com múltiplas fontes de renda, ativos, despesas e incerteza de longevidade/mercado.

## Quando usar

- retirement plan;
- previdência/aposentadoria;
- FIRE;
- withdrawal planning;
- pension income;
- longevity;
- sequence-of-returns risk;
- Monte Carlo retirement analysis.

## Workflow

1. **Household**
   - pessoas/idades;
   - retirement dates;
   - life expectancy horizon assumptions;
   - dependents;
   - household expenses.

2. **Assets/liabilities**
   - taxable/tax-advantaged/pension accounts;
   - cash;
   - real estate;
   - debts;
   - concentration.

3. **Income streams**
   - salary;
   - pension;
   - social-security/public pension;
   - annuity;
   - rental;
   - other recurring income.
   - start/end dates explicit.

4. **Spending**
   - essential;
   - discretionary;
   - health/long-term-care reserve when material;
   - one-offs;
   - inflation basis.

5. **Simulation**
   - deterministic baseline;
   - historical stress/backtest;
   - Monte Carlo/bootstrap when useful;
   - sequence risk;
   - inflation;
   - correlation assumptions;
   - document return model and horizon.

6. **Withdrawal strategy**
   - fixed real;
   - percentage;
   - guardrails;
   - bucket/segmentation;
   - account sequencing;
   - tax interactions only with current jurisdictional rules.

7. **Guardrails**
   - spending adjustment triggers;
   - floor/ceiling;
   - probability/risk trigger is model-dependent;
   - avoid mechanical action without household judgment.

8. **Stress tests**
   - early bear market;
   - high inflation;
   - lower returns;
   - longevity extension;
   - healthcare shock;
   - pension delay/reduction;
   - property/liquidity event.

9. **Outputs**
   - projected cash flows;
   - depletion distribution;
   - probability/risk ranges;
   - spending bands;
   - key failure modes;
   - actions that improve resilience.

## Regras

- Monte Carlo não é previsão;
- “probabilidade de sucesso” depende integralmente das assumptions;
- regra fixa de retirada não é universal;
- não usar historical average sem stress;
- contas/previdência/tax wrappers variam por jurisdição;
- decisões previdenciárias legais/fiscais precisam de regra atual.

## Integração

`personal-financial-planning`, `investment-portfolio-analysis`, `tax-financial-modeling`, `scenario-forecasting`, `insurance-actuarial-modeling`.

## Provenance

Consolidada de driftcurve, RetirementPlanners.jl e outros retirement simulators com household modeling, Monte Carlo, historical bootstrap e spending guardrails. Preserva a incerteza do modelo e não adota regras tributárias específicas dos EUA.
