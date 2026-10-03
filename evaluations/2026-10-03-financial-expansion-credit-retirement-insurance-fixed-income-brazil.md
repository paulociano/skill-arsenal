# Avaliação — Financial Expansion II: Credit, Retirement, Insurance, Fixed Income, Treasury, Real Estate e Brasil

Data: 2026-10-03

## Objetivo

Expandir o núcleo financeiro do Arsenal nas áreas deliberadamente deixadas para um segundo lote: crédito/underwriting, aposentadoria/decumulação, seguros/atuarial, sucessão, renda fixa, treasury corporativa, imobiliário e sistema financeiro brasileiro.

## Resultado executivo

Criados:
- `credit-risk-underwriting`
- `retirement-income-planning`
- `insurance-actuarial-modeling`
- `fixed-income-analysis`
- `corporate-treasury-management`
- `real-estate-investment-analysis`
- `brazil-financial-system-grounding`

Atualizados:
- `personal-financial-planning` com protection/succession inventory;
- `financial-analysis-cycle`;
- `ARSENAL INDEX.md`.

Não foi criada uma skill isolada de estate/succession porque a parte operacional depende fortemente de direito sucessório, documentos jurídicos e jurisdição. O Arsenal cobre inventário, liquidez, beneficiários e riscos, mas não presume validade jurídica.

## Fontes principais

| Repositório/fonte | Domínio | Classe | Decisão |
|---|---|---|---|
| shichenxie/scorecardpy | Credit scorecards | A/D | ABSORB_METHOD_ONLY |
| guillermo-navas-palencia/optbinning | Binning/scorecards | A/D | ABSORB_METHOD_ONLY |
| KelsonLam/credit-risk-analysis | Explainable PD/score pipeline | B/D | ABSORB_METHOD_ONLY |
| imjoebond/driftcurve | Retirement household simulation | A/D | ABSORB_METHOD_ONLY |
| itsdfish/RetirementPlanners.jl | Retirement stress testing | A/D | ABSORB_METHOD_ONLY |
| OpenActuarial/actuarialpy | Actuarial primitives | A/D | ABSORB_METHOD_ONLY |
| OpenActuarial/reservingmodels | Reserving/uncertainty | A/D | ABSORB_METHOD_ONLY |
| mages/ChainLadder | Claims reserving | A/D | KEEP_EXTERNAL_REFERENCE + ABSORB_METHOD_ONLY |
| bbkfe/rateslib_all | Fixed income | A/D | ABSORB_METHOD_ONLY |
| QuantLib/QuantLib | Pricing/fixed income reference | A/D | KEEP_EXTERNAL_REFERENCE |
| Shavkats/Treasury-Management-System | Treasury domain model | B/D | ABSORB_METHOD_ONLY |
| DaveVoyles/Cash-forecasting | Treasury forecast reference | C/D | REFERENCE_ONLY |
| Andorta/LiquidityForecasting | Liquidity analytics | B/D | KEEP_EXTERNAL_REFERENCE |
| daniel-fink/rangekeeper | Real-estate financial modeling | A/D | ABSORB_METHOD_ONLY |
| bacen/pix-api | Pix specification | A/D | CANONICAL_EXTERNAL_REFERENCE |
| OpenBanking-Brasil/openapi | Open Finance Brasil APIs | A/D | CANONICAL_EXTERNAL_REFERENCE |
| OpenBanking-Brasil/all-services-repo | Current OFB service specs | A/D | CANONICAL_EXTERNAL_REFERENCE |
| StrategicProjects/tesouropy | Tesouro open-data adapter | B/D | KEEP_EXTERNAL_REFERENCE |
| CVM open-data adapters / filings-cvm ecosystem | Brazilian filings data | B/D | KEEP_EXTERNAL_REFERENCE |

## 1. Credit Risk & Underwriting

O primeiro lote havia recusado criar owner de crédito por excesso de projetos acadêmicos. O segundo lote adicionou evidência suficiente com scorecardpy, OptBinning e pipelines explicáveis.

Capabilities adotadas:
- default/performance-window definition;
- WOE/IV/binning;
- logistic scorecards as interpretable baseline;
- AUC/Gini/KS;
- calibration;
- PSI/stability;
- out-of-time validation;
- affordability/policy layer;
- fairness/proxy review;
- override governance.

Regra central: modelo estima risco; policy e governance determinam ação.

## 2. Retirement Income Planning

Capabilities adotadas:
- household-level modeling;
- múltiplas retirement dates;
- pensions/income streams;
- deterministic baseline + historical stress + Monte Carlo;
- sequence-of-returns risk;
- inflation/longevity;
- withdrawal strategies;
- spending guardrails;
- stress tests.

Rejeitado:
- regras tributárias e previdenciárias específicas dos EUA como defaults universais;
- tratar probability of success como garantia.

## 3. Insurance & Actuarial Modeling

OpenActuarial forneceu uma arquitetura especialmente útil: primitives separados de workflows.

Capabilities adotadas:
- exposure model;
- frequency/severity;
- loss/expense ratio;
- trend;
- credibility;
- pricing;
- claims triangles;
- chain ladder;
- BF/Cape Cod;
- Mack errors;
- bootstrap predictive reserve;
- VaR/TVaR e simulation.

## 4. Fixed Income Analysis

Capabilities adotadas:
- instrument/cash-flow contract;
- clean/dirty price;
- YTM;
- zero/discount curves;
- duration/DV01/convexity;
- key-rate/spread risk;
- inflation/FX exposure;
- carry/roll-down;
- rate/spread scenarios.

Rateslib foi absorvido como metodologia, não runtime. QuantLib permanece referência técnica externa.

## 5. Corporate Treasury

O domínio mostrou incremento real além de FP&A:
- cash position por entity/bank/currency;
- restricted cash;
- 13-week forecasting;
- liquidity buffer;
- facilities/debt;
- treasury investments;
- FX/rate exposure;
- maker-checker payments;
- bank reconciliation;
- stress liquidity.

Cash forecast continua integrado com FP&A, mas treasury possui ownership distinto sobre liquidez, funding e controles.

## 6. Real Estate

Rangekeeper justificou owner próprio.

Capabilities:
- rent/occupancy;
- NOI;
- cap rate;
- DCF/pro forma;
- terminal/exit cap;
- debt service/DSCR;
- levered/unlevered IRR;
- equity multiple;
- cash-on-cash;
- construction/CapEx/refi scenarios.

## 7. Sucessão / Estate

Decisão: UPDATE_EXISTING em `personal-financial-planning`.

Adicionado:
- beneficiaries;
- dependents;
- asset ownership;
- insurance;
- estate liquidity;
- wills/trusts/documents como inventário/status;
- risks de concentração, iliquidez e continuidade.

Guardrail:
- não criar instrumento jurídico;
- não inferir validade/efeito sucessório sem lei e revisão profissional atuais.

## 8. Brazil Financial System Grounding

Novo owner de grounding, não de regra estática.

Fontes canônicas:
- BCB;
- CVM;
- Tesouro Nacional;
- Receita Federal;
- Open Finance Brasil;
- legislação/Diário Oficial quando necessário;
- B3 conforme o tema.

Padrões absorvidos:
- Pix OpenAPI version/release grounding;
- consent/permissions/token contracts do Open Finance;
- distinguir draft/stable;
- dados CVM/Tesouro com período/revision;
- adapters comunitários são conveniência, nunca autoridade.

Regra crítica:
- não hardcodar Selic, alíquotas, limites ou regras correntes em skill permanente.

## Segurança

Verdict: CAUTION.

Domínios de alto impacto:
- aprovação/recusa de crédito;
- protected data;
- insurance pricing/reserving;
- retirement/tax decisions;
- payment/Pix;
- Open Finance consent/tokens;
- treasury payments;
- real-estate transactions.

Adaptação:
- analysis/modeling by default;
- no live financial action without explicit authorization;
- no bank/payment credentials assumed;
- no automatic adverse credit decision;
- current law/rule lookup when material;
- professional review gates preserved.

## Materialização

Criados:
- `skills/credit-risk-underwriting/SKILL.md`
- `skills/retirement-income-planning/SKILL.md`
- `skills/insurance-actuarial-modeling/SKILL.md`
- `skills/fixed-income-analysis/SKILL.md`
- `skills/corporate-treasury-management/SKILL.md`
- `skills/real-estate-investment-analysis/SKILL.md`
- `skills/brazil-financial-system-grounding/SKILL.md`

Atualizados:
- `skills/personal-financial-planning/SKILL.md`
- `stacks/financial-analysis-cycle/STACK.md`
- `ARSENAL INDEX.md`

## Limites

- As fontes brasileiras comunitárias não substituem BCB/CVM/Tesouro/Receita.
- Regras previdenciárias, tributárias e sucessórias mudam e precisam de verificação atual.
- Credit underwriting real exige dados representativos, fairness/compliance review e policy governance.
- OpenActuarial packages estavam pre-1.0 na avaliação; metodologia foi absorvida, APIs não.
- Rateslib consultado estava beta/pre-release; não foi tratado como API estável.
