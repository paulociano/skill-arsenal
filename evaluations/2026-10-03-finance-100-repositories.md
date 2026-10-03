# Avaliação — 100 repositórios financeiros

Data: 2026-10-03

## Objetivo

Expandir o Skill Arsenal para finanças pessoais, planejamento financeiro, FP&A, contabilidade/DRE, pagamentos, banking/ledgers, investimentos, tax/reporting e workflows financeiros para agentes.

A unidade de adoção foi **capability**, não repositório.

## Resultado executivo

O lote confirmou nove owners novos e uma stack:

- `personal-financial-planning`
- `accounting-financial-statements`
- `financial-planning-analysis`
- `financial-modeling-valuation`
- `investment-portfolio-analysis`
- `payment-billing-operations`
- `banking-ledger-engineering`
- `tax-financial-modeling`
- `financial-filings-analysis`
- stack `financial-analysis-cycle`

Crédito/score foi deliberadamente mantido fora deste primeiro corte: o radar encontrou muitos projetos acadêmicos/portfólio, mas nenhuma fonte do lote justificou ainda um owner canônico com a mesma maturidade das demais famílias.

## Triage dos 100 candidatos

### A. Planejamento financeiro pessoal

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 1 | actualbudget/actual | A/D | ABSORB_METHOD_ONLY |
| 2 | firefly-iii/firefly-iii | A/D | KEEP_EXTERNAL_REFERENCE |
| 3 | finlynq/finlynq | B/D | KEEP_EXTERNAL_REFERENCE |
| 4 | DeseretSaint/open-finance | B/D | KEEP_EXTERNAL_REFERENCE |
| 5 | UMwai/moneta | B/D | KEEP_EXTERNAL_REFERENCE |
| 6 | treeline-money/treeline | B/D | KEEP_EXTERNAL_REFERENCE |
| 7 | securo-finance/securo | B/D | KEEP_EXTERNAL_REFERENCE |
| 8 | fsousac/Dragg | B/D | KEEP_EXTERNAL_REFERENCE |
| 9 | tombadilo-bombadilo/budgero | B/D | KEEP_EXTERNAL_REFERENCE |
| 10 | ellite/Wallos | B/D | KEEP_EXTERNAL_REFERENCE |

Capability adotada: budgeting, cash flow, goals, debt, net worth e revisão periódica.  
Owner: `personal-financial-planning`.

### B. Contabilidade, DRE e ledger contábil

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 11 | frappe/erpnext | A/D | ABSORB_METHOD_ONLY |
| 12 | odoo/odoo | A/D | KEEP_EXTERNAL_REFERENCE |
| 13 | akaunting/akaunting | A/D | KEEP_EXTERNAL_REFERENCE |
| 14 | bigcapitalhq/bigcapital | A/D | KEEP_EXTERNAL_REFERENCE |
| 15 | frappe/books | A/D | ABSORB_METHOD_ONLY |
| 16 | Dolibarr/dolibarr | B/D | KEEP_EXTERNAL_REFERENCE |
| 17 | ledgersmb/LedgerSMB | A/D | KEEP_EXTERNAL_REFERENCE |
| 18 | beancount/beancount | A/D | ABSORB_METHOD_ONLY |
| 19 | simonmichael/hledger | A/D | ABSORB_METHOD_ONLY |
| 20 | ledger/ledger | A/D | ABSORB_METHOD_ONLY |

Capability adotada: double-entry, journal → ledger → trial balance → DRE/balanço/fluxo de caixa, reconciliation e close.  
Owner: `accounting-financial-statements`.

### C. FP&A, budget, forecast e variance

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 21 | Finasis/OpenFPA | B/D | KEEP_EXTERNAL_REFERENCE |
| 22 | openaccountant/skills | A/D | ABSORB_METHOD_ONLY |
| 23 | The-Financial-Fox/Copilot-Excel-Finance | B/D | KEEP_EXTERNAL_REFERENCE |
| 24 | M-0024/Finance-FP-A-Analysis-Explained | B/C | KEEP_EXTERNAL_REFERENCE |
| 25 | dhruvbisht33/finance-sql-variance-analysis | B/D | KEEP_EXTERNAL_REFERENCE |
| 26 | hkmehul3/fpna-ops-dashboard | B/D | KEEP_EXTERNAL_REFERENCE |
| 27 | Neriah2021/fpa-variance-pipeline | B/D | KEEP_EXTERNAL_REFERENCE |
| 28 | srushtipawar-finance/ai-enabled-fpa-command-center | B/D | KEEP_EXTERNAL_REFERENCE |
| 29 | JWANDAYA/Financial-Modelling-and-Analytics-Project | B/D | KEEP_EXTERNAL_REFERENCE |
| 30 | Wammiri/ai-spend-cfo | B/D | KEEP_EXTERNAL_REFERENCE |

OpenFPA foi rebaixado de fonte metodológica principal porque budgeting/forecasting estão declarados como roadmap e vários endpoints são TODO.

Capabilities adotadas:
- actual/budget/forecast/target como tipos distintos;
- driver-based planning;
- variance;
- cash/runway;
- forecast vintage;
- scenario/management reporting.

Owner: `financial-planning-analysis`.

### D. Pagamentos, billing e invoices

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 31 | juspay/hyperswitch | A/D | ABSORB_METHOD_ONLY |
| 32 | killbill/killbill | A/D | ABSORB_METHOD_ONLY |
| 33 | getlago/lago | A/D | ABSORB_METHOD_ONLY |
| 34 | InvoicePlane/InvoicePlane | B/D | KEEP_EXTERNAL_REFERENCE |
| 35 | vteams/open-source-billing | B/D | KEEP_EXTERNAL_REFERENCE |
| 36 | meteroid-oss/meteroid | A/D | KEEP_EXTERNAL_REFERENCE |
| 37 | kdeldycke/awesome-billing | B | KEEP_EXTERNAL_REFERENCE (radar) |
| 38 | invoiceninja/invoiceninja | A/D | KEEP_EXTERNAL_REFERENCE |
| 39 | pretix/pretix | A/D | KEEP_EXTERNAL_REFERENCE |
| 40 | stripe/stripe-python | D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- payment state machine;
- routing/fallback;
- idempotency;
- retries;
- usage metering/pricing;
- invoicing;
- settlement/reconciliation;
- refund/dispute/dunning.

Owner: `payment-billing-operations`.

### E. Core banking, Open Banking e operational ledgers

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 41 | apache/fineract | A/D | ABSORB_METHOD_ONLY |
| 42 | openMF/mifos-x | A/D | KEEP_EXTERNAL_REFERENCE |
| 43 | mojaloop/mojaloop | A/D | KEEP_EXTERNAL_REFERENCE |
| 44 | mojaloop/central-ledger | A/D | KEEP_EXTERNAL_REFERENCE |
| 45 | mojaloop/sdk-scheme-adapter | D | KEEP_EXTERNAL_REFERENCE |
| 46 | OpenBankProject/OBP-API | A/D | ABSORB_METHOD_ONLY |
| 47 | tigerbeetle/tigerbeetle | A/D | ABSORB_METHOD_ONLY |
| 48 | formancehq/ledger | A/D | ABSORB_METHOD_ONLY |
| 49 | plaid/plaid-python | D | KEEP_EXTERNAL_REFERENCE |
| 50 | apache/fineract-backoffice-ui | D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- account/posting model;
- debit/credit invariants;
- pending vs posted;
- atomicity;
- idempotency;
- reversals;
- multi-currency;
- loan/savings product state;
- Open Banking consent/scopes.

Owner: `banking-ledger-engineering`.

### F. Investments, portfolio e quantitative finance

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 51 | QuantConnect/Lean | A/D | KEEP_EXTERNAL_REFERENCE |
| 52 | mementum/backtrader | A/D | KEEP_EXTERNAL_REFERENCE |
| 53 | polakowo/vectorbt | A/D | KEEP_EXTERNAL_REFERENCE |
| 54 | robertmartin8/PyPortfolioOpt | A/D | ABSORB_METHOD_ONLY |
| 55 | dcajasn/Riskfolio-Lib | A/D | ABSORB_METHOD_ONLY |
| 56 | QuantLib/QuantLib | A/D | KEEP_EXTERNAL_REFERENCE |
| 57 | microsoft/qlib | A/D | KEEP_EXTERNAL_REFERENCE |
| 58 | OpenBB-finance/OpenBB | A/D | KEEP_EXTERNAL_REFERENCE |
| 59 | ranaroussi/quantstats | B/D | ABSORB_METHOD_ONLY |
| 60 | ranaroussi/yfinance | D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- return measurement;
- benchmark;
- allocation/drift;
- concentration;
- drawdown/downside;
- risk contribution;
- portfolio optimization with constraints;
- sensitivity to input estimation;
- rebalance as decision support, never automatic execution.

Owner: `investment-portfolio-analysis`.

### G. Crédito e risco

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 61 | shichenxie/scorecardpy | A/D | KEEP_EXTERNAL_REFERENCE |
| 62 | guillermo-navas-palencia/optbinning | A/D | KEEP_EXTERNAL_REFERENCE |
| 63 | bashtage/arch | A/D | KEEP_EXTERNAL_REFERENCE |
| 64 | domokane/FinancePy | A/D | KEEP_EXTERNAL_REFERENCE |
| 65 | attack68/rateslib | A/D | KEEP_EXTERNAL_REFERENCE |
| 66 | google/tf-quant-finance | A/D | KEEP_EXTERNAL_REFERENCE |
| 67 | OpenGamma/Strata | A/D | KEEP_EXTERNAL_REFERENCE |
| 68 | Tech-with-Vidhya/credit-risk-assessment-fintech-framework-using-deep-learning-and-transfer-learning | C/D | REFERENCE_ONLY |
| 69 | xlifp/credit-scoring | B/D | REFERENCE_ONLY |
| 70 | mappy92/credit-risk-pipeline | B/D | REFERENCE_ONLY |

Decisão: não criar owner de crédito neste lote. Scorecards, binning, time-series risk e pricing são áreas diferentes e exigem avaliação dedicada para evitar uma skill superficial.

### H. Tax, reporting e XBRL

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 71 | PSLmodels/Tax-Calculator | A/D | ABSORB_METHOD_ONLY |
| 72 | PolicyEngine/policyengine-us | A/D | KEEP_EXTERNAL_REFERENCE |
| 73 | PolicyEngine/policyengine-core | A/D | KEEP_EXTERNAL_REFERENCE |
| 74 | openfisca/openfisca-core | A/D | ABSORB_METHOD_ONLY |
| 75 | openfisca/openfisca-france | A/D | KEEP_EXTERNAL_REFERENCE |
| 76 | Arelle/Arelle | A/D | ABSORB_METHOD_ONLY |
| 77 | dgunning/edgartools | A/D | ABSORB_METHOD_ONLY |
| 78 | sec-edgar-downloader/sec-edgar-downloader | B/D | KEEP_EXTERNAL_REFERENCE |
| 79 | voulkon/secdata | B/D | KEEP_EXTERNAL_REFERENCE |
| 80 | PSLmodels/Tax-Brain | B/D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- tax rule versioning/jurisdiction/year;
- tax-benefit microsimulation;
- filing/XBRL parsing;
- taxonomy/context/unit validation;
- source provenance.

Owners:
- `tax-financial-modeling`
- `financial-filings-analysis`.

### I. Dados financeiros e research infrastructure

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 81 | daniel3303/Equibles | A/D | KEEP_EXTERNAL_REFERENCE |
| 82 | OctagonAI/octagon-mcp-server | B/D | KEEP_EXTERNAL_REFERENCE |
| 83 | daniel3303/stock-market-mcp-server | B/D | KEEP_EXTERNAL_REFERENCE |
| 84 | pydata/pandas-datareader | D | KEEP_EXTERNAL_REFERENCE |
| 85 | FinanceData/FinanceDataReader | D | KEEP_EXTERNAL_REFERENCE |
| 86 | akfamily/akshare | D | KEEP_EXTERNAL_REFERENCE |
| 87 | ccxt/ccxt | D | KEEP_EXTERNAL_REFERENCE |
| 88 | stefan-jansen/zipline-reloaded | A/D | KEEP_EXTERNAL_REFERENCE |
| 89 | PatrykW7/Financial-data-lakehouse-GCP | B/D | REFERENCE_ONLY |
| 90 | financial-datasets/mcp-server | B/D | KEEP_EXTERNAL_REFERENCE |

Decisão: conectores/data libraries continuam referências. O Arsenal deve usar a fonte atual disponível no runtime e não prometer vendor/MCP específico.

### J. Agentes e skills financeiras

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 91 | chainstart/open-financial-agents | A/D | ABSORB_METHOD_ONLY |
| 92 | anthropics/financial-services | A/D | KEEP_EXTERNAL_REFERENCE |
| 93 | virattt/ai-hedge-fund | B/D | KEEP_EXTERNAL_REFERENCE |
| 94 | AI4Finance-Foundation/FinGPT | A/D | KEEP_EXTERNAL_REFERENCE |
| 95 | AI4Finance-Foundation/FinRL | A/D | KEEP_EXTERNAL_REFERENCE |
| 96 | TradingAgents-AI/TradingAgents | B/D | KEEP_EXTERNAL_REFERENCE |
| 97 | EodHistoricalData/eodhd-claude-skills | B/D | KEEP_EXTERNAL_REFERENCE |
| 98 | cjpatten/canadian-finance-planner-skill | B/D | KEEP_EXTERNAL_REFERENCE |
| 99 | zavora-ai/skill-finance-accounting | B/D | KEEP_EXTERNAL_REFERENCE |
| 100 | KameronKales/planfi-skills | B/D | KEEP_EXTERNAL_REFERENCE |

`open-financial-agents` teve peso alto porque contém 117 SKILL.md no tree observado, incluindo 3-statement model, DCF, comps, GL reconciliation, accrual schedules, variance commentary, portfolio rebalance, financial plan, returns analysis, unit economics e earnings analysis.

## Owners criados

### personal-financial-planning
Capability: fluxo de caixa pessoal, liquidez, dívida, patrimônio e metas, com heurísticas tratadas como opções e não regras universais.

### accounting-financial-statements
Capability: double-entry, ledger, trial balance, DRE, balanço, cash flow, close e reconciliation.

### financial-planning-analysis
Capability: FP&A, actual/budget/forecast, driver tree, variance, cash/runway e management reporting.

### financial-modeling-valuation
Capability: 3-statement model, DCF, comps, scenarios e formula/provenance discipline.

### investment-portfolio-analysis
Capability: performance, allocation, benchmark, concentration, drawdown, risk contribution, optimization e rebalance.

### payment-billing-operations
Capability: billing lifecycle, payment state, routing, idempotency, webhooks, settlement, reconciliation, refunds e dunning.

### banking-ledger-engineering
Capability: operational ledger, postings, pending/posted state, atomicity, reversals, multi-currency, banking products e Open Banking boundaries.

### tax-financial-modeling
Capability: tax rules por jurisdiction/year, calculation/simulation, boundary testing e professional-review guardrails.

### financial-filings-analysis
Capability: filings, XBRL, source hierarchy, normalization, statement validation e provenance.

## Stack criada

`financial-analysis-cycle` roteia o menor subconjunto necessário de owners financeiros e mantém actions externas atrás de autorização explícita.

## Segurança e portabilidade

Verdict geral do lote: **CAUTION**.

Não indica fonte maliciosa; indica domínio e tooling de alto impacto.

Superfícies identificadas:
- credenciais bancárias;
- payment gateway keys;
- tax data;
- personal financial data;
- brokerage/investment data;
- MCP/data-provider credentials;
- live payment/write APIs;
- bank/core-ledger mutation;
- transaction execution;
- cloud databases;
- Docker/install scripts;
- external paid data entitlements.

Adaptação do Arsenal:
- nenhum installer ou runtime externo foi executado;
- nenhuma credencial é presumida disponível;
- read/analyze antes de mutate;
- pagamentos, transfers, trades, filings ou ledger writes exigem autorização explícita;
- tax/investment outputs preservam incerteza e revisão humana;
- vendor-specific commands foram removidos do core methodology.

## Achados metodológicos

1. **Reconciliação precede análise financeira.**
2. **DRE/balanço/fluxo são visões ligadas por um ledger e schedules, não relatórios independentes.**
3. **Actual, budget, forecast e target são semanticamente diferentes.**
4. **Modelos editáveis devem preservar formulas e assumptions, não hardcodes derivados.**
5. **Payment retry sem idempotency é risco financeiro real.**
6. **Operational ledger e general ledger contábil são diferentes, mas precisam reconciliar.**
7. **Portfolio optimizer output não é recomendação automática.**
8. **Tax modeling precisa fixar jurisdição, período e versão de regra.**
9. **XBRL estruturado reduz fricção, mas não elimina validação de context/unit/taxonomy.**
10. **Financial agents úteis mantêm human sign-off e não executam recomendações por conta própria.**

## Materialização

Criados:
- `skills/personal-financial-planning/SKILL.md`
- `skills/accounting-financial-statements/SKILL.md`
- `skills/financial-planning-analysis/SKILL.md`
- `skills/financial-modeling-valuation/SKILL.md`
- `skills/investment-portfolio-analysis/SKILL.md`
- `skills/payment-billing-operations/SKILL.md`
- `skills/banking-ledger-engineering/SKILL.md`
- `skills/tax-financial-modeling/SKILL.md`
- `skills/financial-filings-analysis/SKILL.md`
- `stacks/financial-analysis-cycle/STACK.md`

Atualizado:
- `ARSENAL INDEX.md`

## Limites

- Os 100 foram triados como capability radar; o aprofundamento foi concentrado nas fontes com novidade plausível.
- Nem todos os 100 foram auditados arquivo a arquivo.
- OpenFPA está incompleto em áreas centrais declaradas no próprio roadmap.
- Alguns repositórios acadêmicos ou portfolio projects de credit risk foram mantidos apenas como referência.
- APIs, impostos, regulações, mercados e preços precisam de grounding atual quando usados numa tarefa real.
