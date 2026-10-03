---
name: fixed-income-analysis
description: "Analisar instrumentos de renda fixa por cash flows, yield/curve, duration, convexity, spread, inflation/FX exposure, scenario P&L e reinvestment/liquidity risk com convenções e datas explícitas."
---

# Fixed Income Analysis

## Objetivo

Avaliar títulos e exposições de juros usando cash flows e curvas coerentes, separando preço, yield, risco de taxa, spread e cenários.

## Quando usar

- bonds;
- government bonds;
- corporate debt;
- duration/convexity;
- yield curve;
- spread analysis;
- inflation-linked bonds;
- fixed income portfolios.

## Workflow

1. **Instrument contract**
   - currency;
   - face/notional;
   - coupon;
   - frequency;
   - day-count;
   - settlement;
   - maturity;
   - indexation;
   - call/put/prepayment features.

2. **Cash flows**
   - schedule;
   - coupon/principal;
   - accrued interest;
   - clean vs dirty price;
   - business-day conventions.

3. **Yield/discounting**
   - yield-to-maturity when appropriate;
   - spot/zero curve for consistent valuation;
   - curve date/source explicit;
   - interpolation convention.

4. **Risk**
   - Macaulay/modified duration;
   - DV01/PV01;
   - convexity;
   - key-rate duration when useful;
   - spread duration;
   - inflation/FX basis if relevant.

5. **Credit**
   - government vs credit spread;
   - default/recovery assumptions if modeling risky debt;
   - avoid equating spread solely with default risk.

6. **Scenario**
   - parallel shifts;
   - steepener/flattener;
   - key-rate shock;
   - spread widening;
   - inflation/FX shock;
   - carry and roll-down separately from mark-to-market.

7. **Portfolio**
   - weighted duration;
   - cash-flow buckets;
   - concentration;
   - liquidity;
   - laddering;
   - reinvestment risk;
   - benchmark comparison.

8. **Output**
   - valuation date;
   - price/yield;
   - risk measures;
   - scenario P&L;
   - assumptions and missing risks.

## Regras

- yield and price move inversely only ceteris paribus;
- YTM is an IRR-like construct, not guaranteed realized return;
- duration is local approximation;
- convexity and optionality matter for larger moves;
- curve/instrument conventions are part of the calculation, not decoration.

## Integração

`investment-portfolio-analysis`, `financial-modeling-valuation`, `corporate-treasury-management`, `scenario-forecasting`, `brazil-financial-system-grounding`.

## Provenance

Consolidada de Rateslib, QuantLib, fixed-income portfolio workflows de open-financial-agents/LSEG e bond analytics references. Metodologia é engine-agnostic e exige grounding de convenções.
