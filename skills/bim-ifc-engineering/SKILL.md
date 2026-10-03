---
name: bim-ifc-engineering
description: "Criar, consultar, validar e coordenar modelos BIM/IFC com entidades semânticas, propriedades, relações espaciais, classifications, IDS/BCF, clash/change workflows e exports preservando modelo de informação."
---

# BIM & IFC Engineering

## Objetivo

Tratar edifícios como modelos semânticos e interoperáveis, não apenas geometria 3D.

## Quando usar

- IFC;
- BIM;
- Bonsai/Blender BIM;
- IFC viewer/editor;
- BIM coordination;
- model validation;
- IDS;
- BCF;
- clash/change review.

## Princípio central

**Geometria representa; IFC também descreve o que o elemento é e como se relaciona.**

## Workflow

1. **Schema/version**
   - IFC2x3/IFC4/IFC4x3 explicit;
   - authoring/target tool compatibility.

2. **Spatial structure**
   - project;
   - site;
   - building;
   - storeys;
   - spaces;
   - containment.

3. **Elements**
   - walls/slabs/doors/windows/columns/beams/etc;
   - type vs occurrence;
   - geometry;
   - placement;
   - material;
   - property sets.

4. **Classification/metadata**
   - stable IDs;
   - classifications;
   - quantities;
   - naming conventions;
   - custom properties only when necessary.

5. **Requirements**
   - IDS/other information requirements;
   - required properties;
   - cardinality;
   - allowed values.

6. **Coordination**
   - model federation;
   - clash detection;
   - issue creation;
   - BCF topics/viewpoints;
   - owner/status/resolution.

7. **Change**
   - diff models;
   - additions/deletions/modified properties;
   - provenance/revision;
   - never silently overwrite baseline.

8. **Interop**
   - IFC read/write;
   - geometry conversion only when needed;
   - preserve semantic source of truth;
   - visualization formats are derivatives.

9. **QA**
   - schema validity;
   - spatial containment;
   - required properties;
   - orphan elements;
   - duplicate GUIDs;
   - geometry/placement;
   - export/readback in another compatible viewer when possible.

## Security / actions

IFC editing via MCP/API is an external mutation:
- inspect first;
- scope changes;
- approval before consequential model writes;
- retain original/revision;
- verify changed model after write.

## Regras

- a 3D mesh alone is not BIM;
- valid IFC syntax does not prove model quality;
- IFC version and MVD/exchange requirement matter;
- custom properties should not replace standard semantics without reason;
- BCF issue is coordination record, not geometry mutation.

## Integração

`architectural-design-engineering`, `floor-plan-technical-drawing`, `cad-parametric-modeling`, `building-performance-analysis`, `structural-analysis-modeling`.

## Provenance

Consolidada de IfcOpenShell/Bonsai, BIMserver, web-ifc, xeokit, Speckle, buildingSMART IDS/BCF e COMPAS IFC. Não presume IFC runtime ou MCP instalado.
