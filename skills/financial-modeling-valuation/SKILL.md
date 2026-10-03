---
name: financial-modeling-valuation
description: "Construir e auditar modelos financeiros integrados e valuation por DCF, múltiplos e cenários com fórmulas rastreáveis, histórico validado, assumptions explícitas e checks de integridade."
---

# Financial Modeling & Valuation

## Objetivo

Modelar empresas e ativos com relações financeiras reproduzíveis, separando históricos, assumptions, fórmulas e outputs.

## Quando usar

- 3-statement model;
- DCF;
- comps;
- scenario valuation;
- credit/leverage analysis;
- transaction/LBO-style returns analysis quando solicitado;
- template financeiro em Excel.

## Workflow

1. Mapear período, unidade, moeda, fiscal year e source documents.
2. Separar históricos hardcoded de assumptions e fórmulas.
3. Construir ou validar 3 statements integrados:
   - IS;
   - BS;
   - CF;
   - supporting schedules.
4. Confirmar checks:
   - Assets = L+E;
   - ending cash tie-out;
   - debt roll-forward;
   - retained earnings;
   - working capital;
   - no broken formulas.
5. Projetar por drivers, não por crescimento arbitrário de todos os line items.
6. Para DCF:
   - FCF definition explícita;
   - WACC/discount rate inputs rastreáveis;
   - terminal value;
   - EV → equity bridge;
   - diluted shares;
   - sensitivity around actual base assumptions.
7. Para comps:
   - peer set justificável;
   - metric definitions compatíveis;
   - calendarization/NTM/LTM consistentes;
   - outliers explicados.
8. Para scenarios:
   - assumptions block;
   - base/upside/downside;
   - same model logic across scenarios.
9. Source comments/provenance para hardcodes materiais.
10. Auditar formulas, units, signs, links and circularity before delivery.

## Regras

- formula > precomputed hardcode para derived cells em modelos editáveis;
- valuation é função de assumptions e não “preço verdadeiro”;
- não misturar market data de datas diferentes sem declarar;
- DCF sensitivity precisa conter o base case real;
- outputs para decisão de investimento devem informar incerteza e não substituir julgamento humano.

## Integração

`accounting-financial-statements`, `financial-planning-analysis`, `investment-portfolio-analysis`, `scenario-forecasting`, `evidence-claim-verification`.

## Provenance

Consolidada de open-financial-agents: 3-statement-model, dcf-model, comps-analysis e returns-analysis, com adaptação para ferramentas realmente disponíveis e sem depender de conectores financeiros proprietários.
