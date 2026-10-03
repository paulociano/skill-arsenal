---
name: banking-ledger-engineering
description: "Projetar e revisar ledgers e fluxos bancários com contas, postings, pending/posted balances, atomicidade, idempotência, reconciliação, multi-moeda e APIs de banking sem confundir ledger operacional com contabilidade gerencial."
---

# Banking & Ledger Engineering

## Objetivo

Modelar movimento de valor como postings atômicos e auditáveis, preservando invariantes financeiras mesmo sob retries, concorrência e falhas.

## Quando usar

- core banking;
- wallet/balance systems;
- internal financial ledger;
- payment ledger;
- loans/savings account systems;
- Open Banking APIs;
- reconciliation architecture.

## Princípio central

**Saldo é derivado de postings válidos, não um número mutável isolado.**

## Workflow

1. Definir asset/currency e precision.
2. Definir accounts e ownership.
3. Definir transaction/posting contract:
   - source/debit;
   - destination/credit;
   - amount;
   - asset;
   - idempotency/reference;
   - metadata;
   - timestamp/state.
4. Separar pending/reserved de posted/settled quando necessário.
5. Garantir atomicidade entre postings da mesma transação.
6. Definir invariant de conservação de valor por ledger/asset.
7. Idempotency para retries.
8. Reversals/adjustments como novos eventos, não edição destrutiva do histórico.
9. Reconcile ledger com processors/banks/subledgers.
10. Expor APIs com auth, scopes e views mínimos necessários.

## Multi-currency

- nunca somar currencies sem conversão explícita;
- FX rate tem source/date;
- rounding policy;
- realized/unrealized effects ficam fora do ledger base quando apropriado;
- asset precision não pode ser implícita.

## Loans/savings/core banking

Quando aplicável:
- product terms versionados;
- accrual/interest schedules;
- disbursement;
- repayment allocation;
- fees;
- delinquency state;
- schedule changes como eventos rastreáveis.

## Open banking

- consent/scopes;
- account/transaction views;
- data minimization;
- token lifecycle;
- connector/core abstraction;
- no credential sharing beyond necessary boundary.

## Regras

- nunca corrigir ledger apagando histórico;
- pending e posted não são o mesmo saldo;
- retries devem ser deterministicamente deduplicáveis;
- ledger operacional e GL podem ter granularidades diferentes e precisam de mapping/reconciliation;
- movimento real de valor exige authorization/controls externos ao modelo.

## Integração

`payment-billing-operations`, `accounting-financial-statements`, `secure-code-privacy-review`, `system-design-engineering` e `agent-action-governance`.

## Provenance

Consolidada de TigerBeetle, Formance Ledger, Apache Fineract, Mifos e Open Bank Project. Não presume esses runtimes ou qualquer credencial bancária disponível.
