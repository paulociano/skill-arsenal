---
name: tax-financial-modeling
description: "Modelar impactos tributários com jurisdição, período, regras versionadas, base tributável, faixas/créditos/deduções e cenários, sem apresentar resultado como aconselhamento fiscal definitivo."
---

# Tax Financial Modeling

## Objetivo

Calcular e comparar cenários tributários de forma rastreável, separando fatos do contribuinte, parâmetros legais e regras dependentes de jurisdição/ano.

## Quando usar

- tax estimate;
- tax scenario;
- tax-benefit model;
- quarterly/annual planning;
- deduction/credit analysis;
- policy simulation;
- after-tax financial modeling.

## Workflow

1. **Ground**
   - jurisdição;
   - tax year;
   - filing/entity type;
   - currency;
   - source/version das regras.

2. **Inputs**
   - income categories;
   - deductions;
   - credits;
   - dependents/status;
   - withholding/prepayments;
   - capital gains/losses quando aplicável;
   - business items quando aplicável.

3. **Rule model**
   - thresholds;
   - brackets;
   - phase-ins;
   - phase-outs;
   - caps;
   - carryforwards;
   - interaction order.

4. **Calculation**
   - gross/adjusted/taxable base;
   - tax before credits;
   - credits;
   - other taxes;
   - prepayments;
   - estimated liability/refund.

5. **Scenario**
   - change one or more assumptions explicitly;
   - compare marginal and total impact;
   - identify cliffs/phase-outs;
   - do not extrapolate one jurisdiction to another.

6. **Validation**
   - compare with authoritative calculator/form when available;
   - test boundary values;
   - test zero/max/cap cases;
   - record rule version.

7. **Output**
   - assumptions;
   - calculation;
   - sensitivity;
   - uncertainty;
   - source/rule date;
   - items requiring tax professional review.

## Guardrails

- tax law is time- and jurisdiction-specific;
- web/source verification is required for current rules;
- do not invent deductions/credits;
- examples from US Schedule C or any other jurisdiction are not universal;
- tax result is estimate unless produced/validated under authoritative filing rules;
- filing/execution remains with user or qualified professional.

## Integração

`personal-financial-planning`, `financial-planning-analysis`, `accounting-financial-statements`, `scenario-forecasting`, `evidence-claim-verification`.

## Provenance

Consolidada de PSL Tax-Calculator, OpenFisca and tax workflows from Open Accountant. Adapta rule-engine/microsimulation patterns e rejeita hardcodes jurisdicionais fora de contexto.
