---
name: cad-parametric-modeling
description: "Modelar geometria CAD 2D/3D com sketches restritos, parâmetros, features, B-Rep/CSG, referências estáveis e desenhos derivados, preservando editabilidade e intent geométrico."
---

# CAD Parametric Modeling

## Objetivo

Construir modelos técnicos editáveis em que dimensões e relações controlam geometria, em vez de depender de meshes ou transforms arbitrários.

## Quando usar

- sketch constraints;
- CAD 2D/3D;
- parametric geometry;
- product/architectural components;
- sections;
- technical drawing;
- dimensional variants.

## Workflow

1. **Units/origin**
   - units explicit;
   - local/world reference;
   - planes and axes stable.

2. **Sketch**
   - geometry minimal;
   - dimensional/geometric constraints;
   - avoid under/over-constrained state;
   - name critical parameters.

3. **Features**
   - extrude/pad;
   - pocket/cut;
   - revolve;
   - sweep/loft;
   - boolean;
   - pattern/mirror;
   - fillet/chamfer after primary topology when possible.

4. **References**
   - prefer semantic/datums over fragile topology indices;
   - avoid reference chains that collapse after upstream edits;
   - define design intent.

5. **Assemblies/components**
   - explicit placement constraints;
   - hierarchy;
   - reusable parametric families/components.

6. **Derived drawings**
   - views;
   - sections;
   - details;
   - dimensions sourced from model when possible.

7. **Interop**
   - STEP/IGES/BREP for CAD;
   - DXF/SVG for 2D;
   - IFC for building semantics;
   - GLTF/OBJ for visualization only when semantic loss acceptable.

8. **QA**
   - regeneration after parameter changes;
   - self-intersection;
   - manifold/solid validity;
   - dimensional checks;
   - export/readback.

## Regras

- mesh is not a substitute for editable B-Rep when downstream CAD editing matters;
- feature history should encode design intent, not incidental click order;
- parametric model must survive representative parameter changes;
- export format selection depends on whether geometry, semantics or appearance is authoritative.

## Integração

`floor-plan-technical-drawing`, `bim-ifc-engineering`, `procedural-3d-reconstruction`, `structural-analysis-modeling`.

## Provenance

Consolidada de FreeCAD, OpenSCAD, OpenCascade, BRL-CAD e LibreCAD. Não presume nenhum CAD instalado.
