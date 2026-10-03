---
name: financial-filings-analysis
description: "Pesquisar e analisar demonstrações e filings públicos com hierarquia de fontes, XBRL quando disponível, períodos comparáveis, provenance por line item e separação entre dados reportados, normalizações e interpretação."
---

# Financial Filings Analysis

## Objetivo

Transformar filings e demonstrações públicas em dados e análises rastreáveis, preservando fonte, período, unidade, taxonomy e diferenças entre reportado e ajustado.

## Quando usar

- 10-K/10-Q/8-K;
- XBRL/iXBRL;
- annual reports;
- public-company financial statements;
- earnings analysis;
- peer comparisons;
- historical financial extraction.

## Source hierarchy

Preferir:
1. filing regulatório original;
2. demonstração/earnings release da companhia;
3. investor presentation/supplement;
4. data provider estruturado;
5. agregador/secondary source.

Quando fontes divergirem, registrar a diferença e não escolher silenciosamente.

## Workflow

1. **Ground**
   - companhia/entity;
   - ticker/identifier;
   - filing type;
   - filing date;
   - fiscal period;
   - currency/units;
   - source URL.

2. **Extract**
   - statement line items;
   - periods;
   - XBRL concepts/dimensions quando disponíveis;
   - reported vs derived values.

3. **Normalize**
   - units;
   - sign convention;
   - fiscal calendar;
   - continuing/discontinued operations;
   - restatements;
   - taxonomy synonyms.

4. **Validate**
   - statement totals;
   - comparative periods;
   - cash consistency;
   - basic accounting identities;
   - filing amendments/restatements.

5. **Interpret**
   - growth;
   - margins;
   - working capital;
   - leverage/liquidity;
   - cash conversion;
   - one-offs;
   - management adjustments, claramente separados de GAAP/IFRS/reportado.

6. **Cross-company**
   - ensure same period basis;
   - align definitions;
   - note accounting-policy differences;
   - avoid false comparability from similar labels.

7. **Provenance**
   - every material hardcode/model input should point to source, date, statement/section and period;
   - derived values should expose formula.

8. **Update**
   - latest filing supersedes older assumptions only where applicable;
   - amendments/restatements require explicit version change.

## XBRL

XBRL is structured reporting, not automatic truth.

Validate:
- concept;
- context;
- period type;
- unit;
- dimensions;
- sign;
- duplicate facts;
- custom taxonomy extensions.

Use filing validation tools when available, but distinguish parser/validator success from accounting correctness.

## Guardrails

- never invent missing line items;
- do not mix quarterly and annual values without normalization;
- LTM/NTM are derived constructs and must be labeled;
- adjusted/non-GAAP metrics require reconciliation or explicit source;
- current filings require fresh retrieval;
- regulatory interpretation may require qualified professional review.

## Integração

`accounting-financial-statements`, `financial-modeling-valuation`, `financial-planning-analysis`, `evidence-claim-verification`, `document-extraction-pipeline`.

## Provenance

Consolidada de EdgarTools, Arelle e SEC/XBRL workflows observados em open-financial-agents. Não presume acesso a EDGAR APIs, MCPs ou data vendors sem ferramenta disponível.
