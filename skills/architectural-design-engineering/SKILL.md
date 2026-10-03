---
name: architectural-design-engineering
description: "Estruturar projetos arquitetônicos do briefing ao layout espacial, programa de necessidades, circulação, adjacências, áreas, níveis e critérios funcionais antes de detalhar CAD/BIM ou visualização."
---

# Architectural Design Engineering

## Objetivo

Transformar requisitos de uso e contexto em uma organização espacial coerente antes de avançar para documentação técnica ou maquete virtual.

## Quando usar

- programa de necessidades;
- estudos preliminares;
- layout residencial/comercial;
- reformas;
- distribuição de ambientes;
- adjacências;
- circulação;
- estudos de massa e implantação.

## Princípio central

**Forma segue um programa verificável, não apenas estética.**

## Workflow

1. **Brief**
   - usuários;
   - usos;
   - áreas-alvo;
   - relações entre ambientes;
   - acessibilidade;
   - iluminação/ventilação desejadas;
   - existing conditions;
   - constraints legais/estruturais conhecidos.

2. **Program**
   - lista de ambientes;
   - area target/min/max;
   - privacy/publicness;
   - adjacency;
   - acoustic/technical requirements;
   - furniture/equipment assumptions.

3. **Existing conditions**
   - dimensões medidas;
   - estrutura;
   - shafts/prumadas;
   - aberturas;
   - instalações;
   - orientação/norte;
   - níveis;
   - elementos a preservar/remover.

4. **Adjacency graph**
   - must-near;
   - should-near;
   - must-separate;
   - circulation links;
   - service/public/private zoning.

5. **Block layout**
   - zonas e envelopes primeiro;
   - circulação;
   - access/egress;
   - shafts/service cores;
   - furniture clearances;
   - daylight/orientation constraints.

6. **Area control**
   - gross vs net;
   - circulation percentage;
   - service area;
   - compare program vs layout;
   - flag overshoot/undershoot.

7. **Alternatives**
   - produzir poucas opções contrastantes;
   - comparar trade-offs;
   - preservar decisão humana de direção.

8. **Gate to technical design**
   - layout aprovado;
   - dimensions sufficiently grounded;
   - unresolved structural/code issues listed;
   - no claim of buildability before technical validation.

## Reforma

Para reformas:
- separar existing / demolish / new;
- não assumir que parede é removível;
- mapear interferência com estrutura/MEP;
- indicar elementos uncertain as verify-on-site;
- existing drawings are evidence, not guarantee of as-built condition.

## Guardrails

- não substituir arquiteto/engenheiro responsável;
- legislação, código de obras, acessibilidade e incêndio precisam de grounding local atual;
- medidas críticas exigem levantamento confiável;
- estudo preliminar não equivale a projeto executivo;
- layout bonito não prova viabilidade construtiva.

## Integração

`floor-plan-technical-drawing`, `cad-parametric-modeling`, `bim-ifc-engineering`, `building-performance-analysis`, `structural-analysis-modeling`, `interior-spatial-design`.

## Provenance

Consolidada de workflows observados em FreeCAD, Archilyse, Blueprint/Architect3D e ecossistemas AEC. Mantém programa→layout→validação antes de modelagem técnica.
