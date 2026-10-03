---
name: real-estate-investment-analysis
description: "Analisar ativos e projetos imobiliários por NOI, cap rate, DCF/pro forma, debt service, cash-on-cash, IRR, vacancy, rent growth, CapEx e cenários, separando valor do imóvel de assumptions de operação e financiamento."
---

# Real Estate Investment Analysis

## Objetivo

Modelar imóvel ou desenvolvimento como série de cash flows operacionais, financiamento e valor terminal, com assumptions explícitas.

## Quando usar

- rental property;
- commercial real estate;
- development feasibility;
- property valuation;
- cap rate;
- real-estate DCF;
- cash-on-cash;
- levered/unlevered returns.

## Workflow

1. **Asset**
   - property type;
   - units/area;
   - acquisition/development cost;
   - valuation date;
   - location/context;
   - hold period.

2. **Revenue**
   - rent;
   - occupancy/vacancy;
   - concessions;
   - other income;
   - lease expiry/escalation when relevant.

3. **Operating costs**
   - property tax;
   - insurance;
   - maintenance;
   - management;
   - utilities;
   - reserves;
   - CapEx separately from opex.

4. **NOI**
   - effective gross income minus operating expenses;
   - financing costs excluded from NOI.

5. **Valuation**
   - direct cap when appropriate;
   - DCF/pro forma;
   - terminal/reversion;
   - exit cap;
   - transaction costs;
   - assumptions benchmarked to evidence.

6. **Financing**
   - LTV;
   - rate;
   - amortization;
   - debt service;
   - DSCR;
   - balloon/refinance;
   - covenants.

7. **Returns**
   - unlevered IRR;
   - levered IRR;
   - equity multiple;
   - cash-on-cash;
   - NPV;
   - breakeven occupancy/rent when useful.

8. **Scenario**
   - rent growth;
   - vacancy;
   - CapEx;
   - exit cap;
   - interest rate/refi;
   - construction delay/cost overrun;
   - regulatory/tax shock.

## Regras

- cap rate não é desconto universal;
- NOI não inclui financing;
- appreciation não deve ser presumida sem cenário;
- leverage amplifica ganhos e perdas;
- property tax/legal/title/zoning/regulation dependem da jurisdição;
- valuation precisa declarar condition, date and assumptions.

## Integração

`financial-modeling-valuation`, `personal-financial-planning`, `corporate-treasury-management`, `scenario-forecasting`, `tax-financial-modeling`.

## Provenance

Consolidada de Rangekeeper e padrões de DCF/pro forma imobiliário. Não absorve scores proprietários ou heurísticas sem base verificável.
