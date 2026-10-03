---
name: financial-planning-analysis
description: "Conduzir FP&A com actuals, budget, forecast, variance, drivers, cash/runway, cenários e management reporting, distinguindo plano, previsão, meta e realizado."
---

# Financial Planning & Analysis

## Objetivo

Conectar desempenho financeiro a decisões operacionais por meio de actuals confiáveis, budgets explícitos, forecasts atualizáveis e análise de drivers.

## Quando usar

- FP&A;
- budget anual;
- rolling forecast;
- budget vs actual;
- forecast vs actual;
- DRE gerencial;
- cash-flow forecast;
- runway;
- variance commentary;
- planejamento por cenário.

## Workflow

1. **Ground**
   - entidade/perímetro;
   - moeda;
   - calendário fiscal;
   - actual/budget/forecast versions;
   - grain: month/quarter/year;
   - owner de cada driver.

2. **Actuals**
   - partir de dados reconciliados;
   - normalizar one-offs quando a análise exigir, sem apagá-los;
   - manter mapping para contas de origem.

3. **Driver tree**
   - receita = volume × price/mix quando aplicável;
   - custos variáveis vs fixos;
   - headcount/compensation;
   - working capital;
   - CapEx;
   - debt/interest;
   - taxes.

4. **Budget**
   - plano aprovado/target;
   - versionar assumptions;
   - não confundir budget com previsão mais provável.

5. **Forecast**
   - atualizar a partir de latest actuals;
   - usar driver-based forecast quando possível;
   - usar `scenario-forecasting` para modelos temporais/intervalos.

6. **Variance**
   - Actual vs Budget;
   - Actual vs Prior Forecast;
   - Forecast vs Budget;
   - separar price/volume/mix/timing quando houver dados;
   - distinguir permanent vs timing variance.

7. **Cash**
   - EBITDA/resultado não substitui caixa;
   - modelar receivables, payables, payroll, taxes, debt, CapEx e financing;
   - runway = liquidity / net burn somente quando net burn positivo e estável o suficiente.

8. **Scenario**
   - base/upside/downside ou cenários nomeados;
   - drivers explícitos;
   - liquidity/covenant implications;
   - triggers que mudariam o cenário.

9. **Management output**
   - headline;
   - principais desvios;
   - drivers;
   - impacto futuro;
   - ações/owners;
   - forecast revision;
   - riscos/uncertainties.

10. **Review**
    - comparar forecast vintage vs actual;
    - medir bias/accuracy;
    - corrigir drivers ruins.

## Regras

- actual, budget, forecast e target são tipos diferentes;
- commentary deve explicar driver, não repetir número;
- não tratar forecast como compromisso;
- evitar plug numbers sem owner;
- um bom modelo precisa fechar contabilidade/cash quando afirma ser integrado.

## Integração

`accounting-financial-statements`, `scenario-forecasting`, `dashboard-design`, `financial-modeling-valuation` e `business-decision-intelligence`.

## Provenance

Consolidada de Open Accountant, OpenFP&A como referência de arquitetura, workflows de variance/accrual/roll-forward de open-financial-agents e práticas de ERP/reporting. OpenFP&A não é tratado como implementação completa de budgeting/forecasting quando esses módulos estiverem em roadmap.
