---
name: financial-analysis-cycle
description: "Conduzir análises financeiras pessoais, empresariais e de investimentos do grounding dos dados à reconciliação, planejamento, cenários, valuation e revisão humana, roteando somente os owners necessários."
---

# Financial Analysis Cycle

## Objetivo

Orquestrar trabalho financeiro com rastreabilidade, separando dados, contabilidade, análise, previsão e decisão.

## Router

Planejamento financeiro pessoal:
- `personal-financial-planning`

Contabilidade, DRE, balanço, fluxo de caixa e close:
- `accounting-financial-statements`

FP&A, budget, forecast e variance:
- `financial-planning-analysis`

3-statement model, DCF e valuation:
- `financial-modeling-valuation`

Portfólio e rebalanceamento:
- `investment-portfolio-analysis`

Pagamentos, billing e reconciliação:
- `payment-billing-operations`

Core banking/ledger:
- `banking-ledger-engineering`

Tax modeling:
- `tax-financial-modeling`

Filings/XBRL:
- `financial-filings-analysis`

Crédito/underwriting:
- `credit-risk-underwriting`

Aposentadoria/decumulação:
- `retirement-income-planning`

Seguros/atuarial:
- `insurance-actuarial-modeling`

Renda fixa:
- `fixed-income-analysis`

Treasury corporativa:
- `corporate-treasury-management`

Imobiliário:
- `real-estate-investment-analysis`

Brasil:
- `brazil-financial-system-grounding`

Complementares:
- cenários → `scenario-forecasting`
- dashboards → `dashboard-design`
- pesquisa verificável → `evidence-claim-verification`
- documentos → `document-extraction-pipeline`
- segurança → `secure-code-privacy-review`
- ações externas → `agent-action-governance`

## Fluxo

1. **Ground**
   - pessoa/empresa/entidade;
   - jurisdição;
   - período;
   - moeda;
   - objetivo da análise;
   - fontes;
   - dados faltantes.

2. **Establish source of truth**
   - statements/ledger;
   - bank/processor exports;
   - filings;
   - portfolio statements;
   - tax rules;
   - user-provided assumptions.

3. **Reconcile before analyze**
   - contas e saldos;
   - periods;
   - units;
   - duplicated/missing transactions;
   - source discrepancies.

4. **Analyze**
   - cash flow;
   - profitability;
   - balance sheet;
   - portfolio;
   - payment/billing;
   - tax;
   - drivers.

5. **Model**
   - budget;
   - forecast;
   - scenarios;
   - valuation;
   - debt/payoff;
   - liquidity;
   - retirement/decumulation;
   - credit/underwriting;
   - insurance/reserving;
   - fixed income;
   - treasury;
   - real estate.

6. **Verify**
   - accounting identities;
   - cash tie-outs;
   - formula checks;
   - source provenance;
   - current rules/data when time-sensitive.

7. **Decision support**
   - show options and trade-offs;
   - distinguish fact, assumption and judgment;
   - preserve human choice for financial decisions.

8. **External actions**
   - no transfer, payment, trade, filing or ledger mutation without explicit authorization;
   - re-check amount, currency, destination, environment and approval before acting.

## High-stakes guardrails

- personalized investment, tax, legal, insurance or regulated advice may require licensed professional review;
- use current authoritative rules/data when the answer depends on them;
- para Brasil, usar `brazil-financial-system-grounding` antes de aplicar normas, APIs ou valores correntes;
- avoid false precision;
- do not infer hidden balances or liabilities;
- do not turn model output into automatic recommendation;
- protect account, banking and payment data.

## Critério de conclusão

- source and period are explicit;
- material numbers reconcile or unresolved differences are disclosed;
- assumptions are visible;
- calculations are reproducible;
- limitations are clear;
- next decision remains with the user unless an explicitly authorized action is requested.

## Provenance

Stack construída a partir dos lotes financeiros de 2026-10-03. O primeiro lote de 100 repositórios cobriu planejamento pessoal, contabilidade, FP&A, valuation, portfolio, payments, banking/ledger, tax e filings. O segundo adicionou crédito/underwriting, retirement income, atuarial/seguros, renda fixa, treasury, imobiliário e grounding do sistema financeiro brasileiro.
