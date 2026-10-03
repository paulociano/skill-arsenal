---
name: accounting-financial-statements
description: "Estruturar, reconciliar e analisar contabilidade de dupla entrada e demonstrações financeiras, incluindo razão, trial balance, DRE, balanço e fluxo de caixa, preservando rastreabilidade entre lançamentos e relatórios."
---

# Accounting & Financial Statements

## Objetivo

Tratar demonstrações financeiras como visões derivadas de lançamentos e saldos reconciliados, não como tabelas independentes.

## Quando usar

- DRE/P&L;
- balanço patrimonial;
- fluxo de caixa;
- razão geral;
- trial balance;
- journal entries;
- month-end close;
- reconciliação;
- análise de margens e contas.

## Princípio central

`source transaction → journal entry → ledger → trial balance → statements → analysis`

## Workflow

1. Definir período, entidade, moeda, regime e plano de contas.
2. Confirmar opening balances e source systems.
3. Mapear transações a contas com débito/crédito.
4. Validar que cada lançamento fecha.
5. Reconciliar bancos, cartões, subledgers e contas críticas.
6. Produzir trial balance.
7. Derivar:
   - DRE: receitas, custos, despesas, resultado;
   - balanço: ativos, passivos e patrimônio;
   - fluxo de caixa: operacional, investimento e financiamento.
8. Rodar checks:
   - debits = credits;
   - Assets = Liabilities + Equity;
   - cash-flow ending cash = balance-sheet cash;
   - net income roll-forward consistente;
   - opening + movements = closing para contas roll-forward.
9. Fazer variance e ratio analysis somente após reconciliação.
10. Registrar ajustes, accruals, reversals e evidência.

## DRE

Separar quando aplicável:
- receita bruta;
- deduções/contra-revenue;
- receita líquida;
- COGS/custos diretos;
- gross profit;
- opex;
- EBITDA/EBIT quando definidos;
- resultado financeiro;
- impostos;
- net income.

Não inventar EBITDA ou classificação gerencial se a fonte não suportar.

## Close

Checklist mínimo:
- completeness;
- uncategorized items;
- duplicates;
- accruals/prepayments;
- bank reconciliation;
- intercompany;
- fixed assets/depreciation;
- payroll/taxes quando aplicável;
- trial balance;
- management adjustments;
- statement checks;
- lock/archive.

## Regras

- relatório não reconciliado deve ser marcado como provisório;
- classificação contábil depende de política/jurisdição;
- não sobrescrever histórico sem trilha de ajuste;
- não usar sinal positivo/negativo sem declarar convenção;
- gestão e contabilidade estatutária podem ter mappings diferentes.

## Integração

`financial-planning-analysis`, `financial-modeling-valuation`, `tax-financial-modeling`, `document-extraction-pipeline`, `dashboard-design` e `verify-before-claim`.

## Provenance

Consolidada de Frappe Books, ERPNext, LedgerSMB, Beancount/hledger/Ledger e workflows de GL reconciliation/month-end close de open-financial-agents.
