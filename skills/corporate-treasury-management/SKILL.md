---
name: corporate-treasury-management
description: "Gerir análise de treasury corporativa por cash positioning, 13-week forecast, liquidity buffers, funding, debt, investments, FX/interest-rate exposure, bank reconciliation e payment controls."
---

# Corporate Treasury Management

## Objetivo

Conectar disponibilidade de caixa, previsões, funding e riscos financeiros a decisões operacionais seguras.

## Quando usar

- cash positioning;
- 13-week cash forecast;
- liquidity management;
- corporate treasury;
- debt facilities;
- cash pooling;
- FX exposure;
- treasury investments;
- bank reconciliation.

## Workflow

1. **Cash position**
   - entity;
   - bank;
   - account;
   - currency;
   - available/blocked/restricted cash;
   - timestamp and source.

2. **Forecast**
   - short-term daily/weekly;
   - 13-week when useful;
   - receipts/payments/payroll/tax/debt;
   - confidence/forecast category;
   - base/stress scenarios.

3. **Liquidity**
   - minimum buffer;
   - committed facilities;
   - undrawn capacity;
   - covenant/availability constraints;
   - maturity wall.

4. **Funding**
   - debt draw/repayment;
   - intercompany;
   - equity/other;
   - cost and term;
   - refinancing risk.

5. **Investments**
   - capital preservation;
   - liquidity;
   - yield third;
   - counterparty/issuer limits;
   - maturity alignment.

6. **FX/rates**
   - exposures by currency;
   - natural hedges;
   - forecast confidence;
   - hedge objective/instrument;
   - effectiveness and accounting handled separately.

7. **Payments**
   - batches;
   - maker-checker/dual approval;
   - beneficiary controls;
   - cutoff;
   - settlement;
   - segregation of duties.

8. **Reconciliation**
   - bank statement;
   - ledger;
   - payments;
   - fees;
   - unmatched breaks.

9. **Stress**
   - delayed receipts;
   - revenue shock;
   - FX/rate move;
   - margin/collateral call;
   - facility unavailable;
   - concentrated bank failure.

## Regras

- forecasted cash is not available cash;
- restricted cash must not fund operations silently;
- yield is subordinate to liquidity and capital preservation for operating cash;
- treasury payment execution requires explicit authorization and controls;
- forecast error should be measured by horizon/category.

## Integração

`financial-planning-analysis`, `accounting-financial-statements`, `payment-billing-operations`, `banking-ledger-engineering`, `fixed-income-analysis`, `scenario-forecasting`.

## Provenance

Consolidada de TreasuryFlow, cash/liquidity forecasting references, ERPNext/Odoo treasury building blocks e banking/payment owners já adotados. Não presume SWIFT, EBICS, bank APIs ou payment rails disponíveis.
