---
name: credit-risk-underwriting
description: "Analisar risco de crédito e underwriting com definição de default, PD/scorecards, affordability, collateral, policy rules, calibration, stability, fairness e decisão humana, sem automatizar aprovação apenas pelo modelo."
---

# Credit Risk & Underwriting

## Objetivo

Avaliar capacidade e risco de crédito separando dados, modelo estatístico, política de crédito e decisão operacional.

## Quando usar

- credit scoring;
- underwriting;
- probability of default;
- scorecards;
- borrower risk bands;
- affordability;
- loan policy;
- portfolio credit monitoring.

## Princípio central

**Modelo estima risco; política transforma risco em ação; decisão final precisa de governança.**

## Workflow

1. **Define outcome**
   - default definition;
   - performance window;
   - observation window;
   - cure/restructure policy;
   - portfolio/product scope.

2. **Data contract**
   - application data;
   - bureau/transactional data quando autorizado;
   - existing relationship;
   - collateral/guarantees;
   - income/debt;
   - missingness and provenance.

3. **Data split**
   - respeitar tempo quando possível;
   - train/validation/out-of-time;
   - impedir leakage;
   - registrar population shifts.

4. **Feature preparation**
   - missing treatment;
   - WOE/binning quando scorecard;
   - monotonicity quando fizer sentido;
   - IV/selection como ferramenta, não verdade;
   - evitar variáveis que funcionem como proxies inadequados para atributos protegidos.

5. **Model**
   - logistic scorecard como baseline interpretável;
   - boosted/ML models só quando ganho é mensurável e explicável o suficiente para o uso;
   - output principal: PD ou ranking coerente.

6. **Validation**
   - discrimination: AUC/Gini/KS;
   - calibration;
   - Brier/log-loss quando útil;
   - confusion metrics apenas no threshold definido;
   - out-of-time stability;
   - PSI/drift;
   - backtesting de default rates por band.

7. **Underwriting policy**
   - hard eligibility rules;
   - affordability/DTI;
   - minimum documentation;
   - collateral/LTV quando aplicável;
   - score/PD bands;
   - pricing/limit policy;
   - manual-review band;
   - decline reasons rastreáveis.

8. **Fairness/governance**
   - protected attributes and proxies review;
   - disparate-impact testing quando exigido;
   - explainability/adverse-action requirements conforme jurisdição;
   - overrides registrados.

9. **Monitoring**
   - approval rate;
   - bad rate/default rate;
   - vintage curves;
   - roll rates;
   - calibration drift;
   - PSI;
   - override performance;
   - concentration.

10. **Decision output**
    - risk estimate;
    - evidence;
    - policy outcome;
    - uncertainties;
    - manual-review conditions.

## Regras

- accuracy não é métrica suficiente para crédito desbalanceado;
- AUC alto não prova calibração;
- scorecard de dataset sintético não valida política real;
- reject inference é hipótese sensível, não ajuste automático;
- underwriting não deve depender de atributo protegido ou proxy ilegal;
- modelo nunca deve ser o único fundamento de ação adversa sem controles aplicáveis.

## Integração

`banking-ledger-engineering`, `financial-planning-analysis`, `scenario-forecasting`, `secure-code-privacy-review`, `experiment-design` e `verify-before-claim`.

## Provenance

Consolidada de scorecardpy, OptBinning e pipelines de credit-risk scorecards com WOE/IV, calibration, AUC/Gini/KS e stability monitoring. O Arsenal absorve metodologia e governance, não modelos treinados nem políticas de concessão específicas.
