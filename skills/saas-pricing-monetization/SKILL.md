---
name: saas-pricing-monetization
description: "Projetar e revisar pricing e monetização de SaaS, APIs e produtos de IA conectando valor, packaging, value metric, usage/credits, entitlements, willingness-to-pay, economics, rollout e aprendizado sem confundir billing infrastructure com estratégia."
---

# SaaS Pricing & Monetization

## Objetivo

Transformar pricing em um sistema de decisão que conecta valor percebido, forma de cobrança, packaging, economics e aprendizado de mercado. A skill cobre estratégia de monetização; implementação de billing é tratada apenas como consequência técnica quando necessária.

## Quando usar

- definir preço inicial;
- revisar pricing tiers;
- escolher entre seat, usage, credit, flat, outcome ou modelo híbrido;
- estruturar free tier, trial, allowance, overage ou minimum commitment;
- redesenhar packaging;
- avaliar willingness-to-pay;
- planejar aumento de preço;
- monetização de APIs, SaaS ou produtos de IA;
- revisar incoerência entre custo de servir e modelo de receita.

Não usar apenas para implementar cobrança, invoices ou integração com gateway.

## Princípio central

**Value metric, packaging e price point são decisões diferentes e devem ser avaliadas separadamente.**

## Workflow

1. **Business context**
   - quem usa;
   - quem paga;
   - motion: self-serve, sales-led ou híbrido;
   - estágio;
   - objetivo: learning, growth, revenue, margin ou expansion.

2. **Value model**
   - outcome entregue;
   - alternativa atual;
   - frequência/criticality;
   - unidade pela qual o valor cresce;
   - evidência real de willingness-to-pay.

3. **Value metric**
   - testar se a unidade de cobrança cresce com valor recebido;
   - verificar previsibilidade, simplicidade e resistência a gaming;
   - separar usage observável de value metric econômico.

4. **Pricing model**
   Considerar apenas quando fizer sentido:
   - flat;
   - per seat;
   - usage;
   - tiered/volume;
   - feature/entitlement;
   - credits/prepaid;
   - transaction/outcome;
   - hybrid.

5. **Packaging**
   - definir quem é cada package;
   - benefícios e limites;
   - upgrade trigger;
   - entitlements;
   - support/service level;
   - evitar tiers que diferem apenas por ornamentação.

6. **Price point**
   - usar concorrentes como contexto, não target automático;
   - custo de servir é floor/constraint, não fonte principal de valor;
   - separar preço de lista, desconto, commitment e custom enterprise terms;
   - no estágio inicial, escolher um preço que gere aprendizado em vez de fabricar precisão.

7. **Economics**
   - gross/contribution margin;
   - cost to serve;
   - infra/AI/API variable cost;
   - support/success burden;
   - payment fees;
   - discount leakage;
   - expansion/contraction dynamics.

8. **Usage and credits**
   Para modelos usage/credit:
   - definir evento faturável;
   - aggregation;
   - idempotência/reconciliation;
   - allowance;
   - prepaid/promotional credits;
   - top-up/overage;
   - expiration;
   - customer visibility;
   - disputes/adjustments.

   O desenho econômico deve existir antes da infraestrutura.

9. **Research**
   Usar proporcionalmente:
   - customer/pricing interviews;
   - historical conversion/churn;
   - deal-loss reasons;
   - competitor anchors;
   - Van Westendorp/MaxDiff ou métodos equivalentes quando adequados;
   - preço pago/compromisso real vale mais que opinião hipotética.

10. **Experiment and rollout**
    - definir hipótese e guardrails;
    - testar primeiro onde blast radius é menor quando apropriado;
    - separar novos clientes de migração da base;
    - planejar grandfathering/grace period explicitamente;
    - acompanhar conversion, churn, expansion, support e margin;
    - rollback ou pause quando o custo do erro justificar.

11. **Billing architecture handoff**
    Quando execução técnica for necessária, traduzir a estratégia em:
    - product catalog;
    - plan/version;
    - metric/event;
    - entitlement;
    - credit;
    - invoice rule;
    - payment/revenue integration.

    Não escolher fornecedor de billing antes de estabilizar o contrato econômico relevante.

12. **Review**
    - o modelo continua alinhado ao valor?
    - a receita cresce junto com valor e custo?
    - clientes entendem a cobrança?
    - pricing está impedindo adoção ou monetização?
    - qual evidência justificaria nova mudança?

## Guardrails

- não afirmar willingness-to-pay sem evidência;
- não copiar competitor pricing mecanicamente;
- não usar custo como única base de preço;
- não tratar um survey como validação suficiente;
- não otimizar para conversão ignorando margin/retention;
- não transformar usage-based em surpresa de fatura;
- não esconder assumptions atrás de forecast preciso;
- mudanças de preço em base existente exigem análise de confiança, comunicação e reversibilidade.

## Entregável

Conforme a tarefa:
- pricing diagnosis;
- value metric;
- packaging/tier proposal;
- pricing model;
- price hypotheses;
- economics;
- research plan;
- rollout/experiment;
- risks;
- verification metrics.

## Integração

Combina com:
- `venture-building-cycle`;
- `customer-interview`;
- `experiment-design`;
- `financial-modeling-valuation`;
- `financial-planning-analysis`;
- `product-metrics-diagnostics`;
- `go-to-market-strategy`;
- `decision-analysis`.

## Provenance

Adaptada de práticas encontradas em:
- https://github.com/coreyhaines31/marketingskills
- https://github.com/getlago/lago
- https://github.com/flexprice/flexprice
- https://github.com/uselotus/lotus
- https://github.com/kdeldycke/awesome-billing
- https://github.com/AIDevGTM/gtm-cofounder

Preserva separação entre value metric, packaging e price point; pricing por valor; usage/credits/entitlements; rollout e economics. Ferramentas de billing, CLIs e serviços externos não são requisitos.
