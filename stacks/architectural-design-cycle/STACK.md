---
name: architectural-design-cycle
description: "Conduzir projetos arquitetônicos e de interiores do briefing à planta técnica, CAD paramétrico, maquete 3D, BIM/IFC, desempenho ambiental e análise estrutural preliminar, carregando somente os owners necessários."
---

# Architectural Design Cycle

## Objetivo

Orquestrar tarefas AEC do estudo inicial à documentação e coordenação, sem confundir visualização, cálculo e aprovação profissional.

## Router

Programa/layout:
- `architectural-design-engineering`

Planta/esboço técnico:
- `floor-plan-technical-drawing`

CAD paramétrico:
- `cad-parametric-modeling`

Interiores/reformas:
- `interior-spatial-design`

BIM/IFC:
- `bim-ifc-engineering`

Desempenho ambiental:
- `building-performance-analysis`

Estruturas:
- `structural-analysis-modeling`

Assets/maquete/render:
- `concept-to-3d-asset`
- `procedural-3d-reconstruction`
- `high-fidelity-image-generation`

Complementares:
- `design-direction`
- `editable-visual-design`
- `verify-before-claim`

## Fluxo

1. **Ground**
   - objetivo;
   - tipo de imóvel/projeto;
   - existing/new/renovation;
   - medidas/fontes;
   - localização/jurisdição quando norma importar;
   - nível de entrega: estudo, anteprojeto, coordenação ou documentação.

2. **Program**
   - necessidades;
   - ambientes;
   - áreas;
   - adjacências;
   - circulação;
   - constraints.

3. **Existing conditions**
   - levantamento;
   - estrutura;
   - shafts;
   - aberturas;
   - níveis;
   - elementos incertos marcados para verificação.

4. **Concept/layout**
   - zoning;
   - alternativas;
   - furniture footprints;
   - area control;
   - human selection of direction.

5. **Technical plan**
   - scale;
   - walls/openings;
   - dimensions;
   - annotations;
   - existing/demolition/new;
   - print/export QA.

6. **Parametric/CAD**
   - stable units/origin;
   - constraints;
   - reusable parameters;
   - derived views/sections.

7. **3D/interiors**
   - 2D/3D parity;
   - furniture/materials;
   - walkthrough/render only as communication layer.

8. **BIM**
   - spatial structure;
   - semantic elements;
   - properties;
   - IFC;
   - IDS/BCF/coordination where required.

9. **Analysis**
   - daylight/solar/energy when relevant;
   - structural model only when required;
   - current standards/code grounded separately.

10. **QA**
    - dimensional consistency;
    - model/readback;
    - floor-to-floor continuity;
    - BIM validation;
    - simulation assumptions;
    - structural warning checks.

11. **Handoff**
    - distinguish study vs executable documentation;
    - unresolved issues;
    - professional review required;
    - editable/source artifacts when produced.

## Selection rule

Não carregar todas as skills.

Exemplos:
- reorganizar sala: `interior-spatial-design`;
- criar planta: + `floor-plan-technical-drawing`;
- modelo editável/dimensional: + `cad-parametric-modeling`;
- entrega IFC: + `bim-ifc-engineering`;
- estudo solar/energia: + `building-performance-analysis`;
- modificação estrutural: + `structural-analysis-modeling` e revisão profissional.

## Safety / professional boundary

- não afirmar viabilidade construtiva somente a partir de render/planta conceitual;
- legislação e normas dependem de local/data;
- paredes/elementos existentes precisam de levantamento e verificação;
- alteração estrutural exige engenheiro habilitado;
- instalações elétricas, hidráulicas, incêndio e acessibilidade exigem disciplina e norma próprias;
- nenhuma simulação substitui ART/RRT, aprovação ou responsabilidade profissional quando aplicáveis.

## Provenance

Stack construída do lote AEC de 30 repositórios de 2026-10-03, com maior peso em FreeCAD, IfcOpenShell/Bonsai, web-ifc, BIMserver, xeokit, Speckle, Architect3D, Blueprint.js, Archilyse, COMPAS, Ladybug/Honeybee, OpenStudio, OpenSees, Kratos, SfePy e OSDAG.
