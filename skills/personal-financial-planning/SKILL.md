---
name: personal-financial-planning
description: "Estruturar planejamento financeiro pessoal por fluxo de caixa, reserva, dívidas, patrimônio, metas e cenários, separando fatos, premissas e decisões do usuário sem transformar heurísticas em regras universais."
---

# Personal Financial Planning

## Objetivo

Transformar dados financeiros pessoais em um plano coerente, verificável e atualizável, conectando fluxo de caixa, liquidez, dívidas, patrimônio e metas.

## Quando usar

- orçamento pessoal;
- reserva de emergência;
- plano de quitação de dívidas;
- patrimônio líquido;
- metas financeiras;
- revisão mensal/anual;
- decisões entre poupar, amortizar ou investir.

## Workflow

1. **Ground**
   - moeda e jurisdição;
   - horizonte;
   - renda recorrente/variável;
   - despesas essenciais e discricionárias;
   - dívidas;
   - ativos e liquidez;
   - metas e datas.

2. **Cash flow**
   - usar períodos comparáveis;
   - separar transferências internas de receita/despesa;
   - calcular renda, despesas, resultado e taxa de poupança;
   - marcar dados incompletos.

3. **Liquidity**
   - estimar despesas essenciais;
   - construir cenários de meses de cobertura;
   - adequar target à estabilidade de renda, dependentes e risco;
   - não impor um número universal.

4. **Debt**
   - registrar saldo, taxa, prazo e pagamento mínimo;
   - comparar avalanche, snowball e outras restrições;
   - simular juros e tempo de quitação;
   - taxas variáveis exigem cenários.

5. **Net worth**
   - ativos menos passivos;
   - separar ativos líquidos, ilíquidos e de uso;
   - registrar valuation date e fonte;
   - acompanhar delta no tempo.

6. **Goals**
   - target amount;
   - target date;
   - current funding;
   - required contribution;
   - prioridade e flexibilidade;
   - detectar competição entre metas pela mesma capacidade mensal.

7. **Scenario**
   - base, stress e upside quando material;
   - explicitar premissas;
   - usar `scenario-forecasting` para horizontes incertos.

8. **Protection and succession inventory**
   - beneficiaries/designations;
   - dependents;
   - ownership of key assets;
   - insurance coverage;
   - liquidity for taxes/debts/final expenses;
   - wills/trusts/estate documents as existence/status only unless qualified legal review is available;
   - identify concentration, missing beneficiary, illiquid-estate and succession continuity risks;
   - do not draft legal instruments or infer legal effectiveness from a checklist.

9. **Plan**
   - transformar análise em opções;
   - mostrar trade-offs;
   - usuário escolhe prioridade;
   - registrar assumptions que mudariam a decisão.

10. **Review cadence**
   - monthly: cash flow/budget;
   - quarterly: goals/debt;
   - annual or event-driven: insurance, tax, estate, allocation and long-term plan.

## Guardrails

- não inferir saldo atual apenas de transações;
- não tratar 50/30/20, 3-6 meses ou qualquer outra heurística como obrigação;
- separar conselho educacional de decisão regulada/profissional;
- regras tributárias, previdenciárias, sucessórias e de seguros dependem de jurisdição e data;
- não recomendar produto financeiro específico sem dados atuais e escopo apropriado;
- preservar autonomia do usuário em prioridades entre liquidez, dívida, consumo e investimento.

## Integração

`scenario-forecasting`, `investment-portfolio-analysis`, `retirement-income-planning`, `insurance-actuarial-modeling`, `tax-financial-modeling`, `brazil-financial-system-grounding`, `dashboard-design` e `verify-before-claim`.

## Provenance

Consolidada de openaccountant/skills, Actual Budget, Firefly III e práticas de budgeting/net-worth/debt planning. Adapta workflows, não herda integrações bancárias nem heurísticas prescritivas.
