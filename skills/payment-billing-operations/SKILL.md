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

## Ownership boundary

Para decidir value metric, packaging, tiers, price point, willingness-to-pay ou rollout de preço, use `saas-pricing-monetization`.

Esta skill começa quando a estratégia precisa virar contrato operacional de billing e pagamento.

## Lifecycle

`usage/order → pricing rule → invoice/charge → payment attempt → processor → settlement → reconciliation → refund/dispute if any`

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

## Integrações Stripe: roteamento específico do provedor

Quando o processador escolhido for Stripe, usar o catálogo oficial de skills como **referência externa atualizável**, não como runtime instalado: https://github.com/stripe/ai/tree/main/skills/ (sincronizado pela Stripe a partir da documentação oficial).

1. Antes de implementar, verificar a documentação atual do produto, SDK e versão da API, sem congelar números do snapshot da skill externa.
2. Para pagamentos únicos e checkout customizado, comparar Checkout Sessions e Payment Element com as alternativas atuais conforme necessidade; justificar qualquer PaymentIntent direto.
3. Para marketplaces, verificar modelo Stripe Connect (account ownership, encargos, saldo negativo, charge pattern), onboarding, exigências regulatórias e fluxo de repasses por país.
4. Para assinaturas, faturamento por uso e tributos, separar contrato comercial, eventos de medição, entitlement, invoice, cobrança e obrigações fiscais. Não presumir que ativar cálculo automático de tributos substitui registros exigidos.
5. Tratar webhooks como parte do contrato de consistência: assinatura/autenticidade, replay, idempotência, eventos assíncronos e fulfillment pós-confirmação. Nunca confiar só na página de sucesso.
6. Usar ambiente isolado de teste/sandbox quando disponível e validar ciclo completo antes de produção. Chaves restritas, segredo fora do repositório e privilégio mínimo.
7. Migrações: comparar versões efetivamente fixadas no backend, SDKs e destinos de eventos; consultar changelog oficial e testar regressões. Não afirmar que a versão apontada pelo catálogo continua sendo a mais recente.
8. Transferências de fundos, provisionamento de serviços, movimentações reais e alterações de configuração live requerem capacidades efetivamente conectadas e aprovação humana específica. Não executar comandos da CLI mencionados na fonte se a CLI não estiver disponível.

**Referências específicas para consulta seletiva:** `stripe-best-practices`, `connect-recommend`, `connect-required-verification-information`, `metronome`, `upgrade-stripe` e `stripe-docs`. `stripe-pay`, `stripe-directory` e `stripe-projects` dependem de CLI/plugins e operações externas; não são automaticamente capacidades deste ambiente.

**Should-trigger:** implementar marketplace com split de pagamentos Stripe e contas conectadas. Verificar responsabilidade, fluxo do dinheiro, KYC e webhook antes do código. **Near-miss:** sistema interno de cobranças sem Stripe selecionada não deve receber recomendação obrigatória de APIs Stripe.

## Integração

`saas-pricing-monetization`, `accounting-financial-statements`, `banking-ledger-engineering`, `secure-code-privacy-review`, `system-design-engineering` e `verify-before-claim`.

## Provenance

Consolidada de Hyperswitch, Kill Bill, Lago e ecossistemas de invoicing/payments. Roteamento Stripe enriquecido a partir de https://github.com/stripe/ai/tree/main/skills/ (consulta de 2026-10-12), sem instalar CLI ou importar ações financeiras. Absorve orchestration, metering, idempotency, retries e reconciliation sem presumir acesso a gateways.
