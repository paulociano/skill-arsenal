---
name: floor-plan-technical-drawing
description: "Criar e revisar plantas baixas e esboços técnicos com escala, paredes, aberturas, níveis, cotas, eixos, mobiliário, símbolos, áreas e exports legíveis, separando estudo, documentação e desenho executivo."
---

# Floor Plan & Technical Drawing

## Objetivo

Transformar layout espacial em planta legível, dimensionada e rastreável, adequada a estudo, coordenação ou documentação conforme o nível de detalhe pedido.

## Quando usar

- planta baixa;
- sketch técnico;
- reforma existente/demolição/nova;
- cotas;
- layout de mobiliário;
- plantas para apresentação;
- export SVG/PDF/DXF.

## Workflow

1. **Set contract**
   - purpose;
   - scale;
   - units;
   - sheet size;
   - north;
   - level/storey;
   - existing/new/demolition state.

2. **Geometry**
   - walls;
   - columns;
   - doors/windows;
   - stairs;
   - shafts;
   - fixed equipment;
   - room boundaries.

3. **Dimensions**
   - overall;
   - internal;
   - openings;
   - clearances;
   - levels where relevant;
   - avoid duplicate/contradictory dimensions.

4. **Annotations**
   - room names;
   - area;
   - door/window tags;
   - section/elevation markers;
   - notes;
   - title block;
   - revision/date.

5. **Furniture/equipment**
   - use real dimensions where material;
   - check circulation;
   - door swing;
   - appliance/service clearances.

6. **Graphics**
   - hierarchy lineweight;
   - cut elements stronger than projected;
   - existing/demolition/new differentiated;
   - hatches/symbols consistent;
   - text size readable at output scale.

7. **Multi-storey**
   - floor-to-floor height;
   - stair opening continuity;
   - vertical alignment;
   - shafts/columns continuity;
   - level references.

8. **Export**
   - scale preserved;
   - SVG/PDF/PNG for presentation;
   - DXF/DWG/IFC only when toolchain supports it;
   - print/readback test.

9. **QA**
   - closed rooms;
   - no wall gaps;
   - duplicate intersections;
   - doors collide?;
   - circulation usable?;
   - dimensions sum?;
   - scale bar/title/north present when required.

## Regras

- image-based floor plan sem scale calibration não é dimensionally authoritative;
- furniture icon size must represent actual footprint when used for clearance;
- exported PDF/image needs readback at target scale;
- floor plan is not structural or MEP approval.

## Integração

`architectural-design-engineering`, `cad-parametric-modeling`, `interior-spatial-design`, `bim-ifc-engineering`.

## Provenance

Consolidada de Architect3D, Blueprint.js, React Planner, Archilyse e FreeCAD technical drawing workflows.
