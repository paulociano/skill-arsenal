---
name: payment-billing-operations
description: "Projetar e analisar operações de pagamentos e billing com payment intents, routing, retries, idempotency, invoices, subscriptions, metering, reconciliation, refunds, dunning e controles antes de qualquer movimentação real de valor."
---

# Payment & Billing Operations

## Objetivo

Modelar o ciclo de cobrança e pagamento com estados explícitos, idempotência e reconciliação, separando cálculo de cobrança de movimentação de dinheiro.

## Quando usar

- payment orchestration;
- billing;
- invoices;
- subscriptions;
- usage-based billing;
- refunds;
- retries;
- reconciliation;
- dunning;
- payment-provider integration.

## Lifecycle

`usage/order → pricing → invoice/charge → payment attempt → processor → settlement → reconciliation → refund/dispute if any`

## Workflow

1. **Ground**
   - currencies;
   - merchant/entity;
   - providers;
   - payment methods;
   - settlement model;
   - billing cadence;
   - tax boundary;
   - source of truth.

2. **Pricing/billing**
   - usage/event definitions;
   - plan/version;
   - recurring vs usage vs hybrid;
   - credits/allowances;
   - proration;
   - invoice generation.

3. **Payment**
   - unique payment/payment-intent id;
   - amount/currency immutable after critical transition unless new version;
   - idempotency key;
   - state machine;
   - timeout/retry policy.

4. **Routing**
   - provider capability;
   - region/currency/payment method;
   - health/success rate;
   - cost only after hard constraints;
   - fallback must not double-charge.

5. **Webhooks**
   - authenticate;
   - deduplicate;
   - tolerate out-of-order delivery;
   - replay-safe handlers;
   - do not assume webhook arrival exactly once.

6. **Reconciliation**
   - internal invoice/payment state;
   - processor transactions;
   - settlement/payout;
   - fees;
   - bank/ledger;
   - breaks have owner and reason code.

7. **Refunds/disputes**
   - original payment reference;
   - partial/full;
   - balance/ledger effect;
   - status tracking;
   - manual review when policy requires.

8. **Dunning**
   - failed payment reason;
   - retry schedule;
   - customer notification;
   - entitlement/grace policy;
   - stop condition.

9. **Controls**
   - least privilege;
   - secrets outside prompts/repos/logs;
   - human approval for material live changes;
   - audit trail;
   - PCI/sensitive-data boundary.

## Regras

- retry sem idempotency pode cobrar duas vezes;
- invoice, payment e settlement são objetos diferentes;
- billing source of truth não precisa ser payment processor;
- amount/currency mismatch é blocker;
- live payment action exige autorização explícita.

## Integração

`accounting-financial-statements`, `banking-ledger-engineering`, `secure-code-privacy-review`, `system-design-engineering` e `verify-before-claim`.

## Provenance

Consolidada de Hyperswitch, Kill Bill, Lago e ecossistemas de invoicing/payments. Absorve orchestration, metering, idempotency, retries e reconciliation sem presumir acesso a gateways.
