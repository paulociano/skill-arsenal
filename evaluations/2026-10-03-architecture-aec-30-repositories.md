# Avaliação — 30 repositórios AEC: arquitetura, interiores, CAD, BIM, engenharia e maquetes virtuais

Data: 2026-10-03

## Objetivo

Expandir o Skill Arsenal para arquitetura, interiores, CAD, BIM/IFC, plantas baixas, reformas, desempenho ambiental e análise estrutural, com foco em criação de esboços técnicos, documentação, maquetes virtuais e workflows interoperáveis.

A unidade de adoção foi capability, não repositório.

## Resultado executivo

Criados sete owners:
- `architectural-design-engineering`
- `floor-plan-technical-drawing`
- `cad-parametric-modeling`
- `bim-ifc-engineering`
- `interior-spatial-design`
- `building-performance-analysis`
- `structural-analysis-modeling`

Criada:
- stack `architectural-design-cycle`

Atualizado:
- `ARSENAL INDEX.md`

## Triage dos 30 repositórios

### A. CAD, desenho técnico e kernels geométricos

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 1 | FreeCAD/FreeCAD | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 2 | LibreCAD/LibreCAD | A/D | ABSORB_METHOD_ONLY |
| 3 | BRL-CAD/brlcad | A/D | KEEP_EXTERNAL_REFERENCE |
| 4 | openscad/openscad | A/D | ABSORB_METHOD_ONLY |
| 5 | Open-Cascade-SAS/OCCT | A/D | ABSORB_METHOD_ONLY |

Capabilities adotadas:
- sketch 2D com constraints;
- parametric history;
- B-Rep/CSG;
- feature modeling;
- technical drawings;
- 2D↔3D interoperability;
- export/readback.

Owner:
- `cad-parametric-modeling`.

### B. BIM, IFC e interoperabilidade

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 6 | IfcOpenShell/IfcOpenShell | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 7 | opensourceBIM/BIMserver | A/D | ABSORB_METHOD_ONLY |
| 8 | ThatOpen/engine_web-ifc | A/D | ABSORB_METHOD_ONLY |
| 9 | ThatOpen/engine_components | A/D | KEEP_EXTERNAL_REFERENCE |
| 10 | xeokit/xeokit-sdk | A/D | ABSORB_METHOD_ONLY |
| 11 | specklesystems/speckle-server | A/D | ABSORB_METHOD_ONLY |
| 12 | compas-dev/compas_ifc | A/D | ABSORB_METHOD_ONLY |
| 13 | buildingSMART/IDS | A/D | ABSORB_METHOD_ONLY |
| 14 | buildingSMART/BCF-API | A/D | ABSORB_METHOD_ONLY |
| 15 | xeokit/xeokit-bim-viewer | B/D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- IFC schema/version grounding;
- spatial structure;
- semantic elements;
- type vs occurrence;
- properties/classification/quantities;
- IDS;
- BCF;
- clash/coordination;
- model diff/revisions;
- IFC as semantic source of truth.

Owner:
- `bim-ifc-engineering`.

IfcOpenShell/Bonsai teve o maior peso metodológico do lote porque combina parsing, authoring, conversion, clash, BCF, IDS, cost/FM extensions e workflows de edição IFC.

### C. Planta baixa e interiores

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 16 | cvdlab/react-planner | B/D | ABSORB_METHOD_ONLY |
| 17 | aalavandhaann/blueprint-js | A/D | ABSORB_METHOD_ONLY |
| 18 | sztepen/Archilyse | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 19 | amitukind/architect3d | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 20 | Vanuan/sweethome3d | B/D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- 2D floor planning;
- room closure;
- walls/openings/stairs;
- furniture footprints;
- scale/dimensions;
- multi-storey;
- 2D/3D parity;
- plan export/print;
- digitization of existing plans;
- DXF/IFC/PNG/PDF outputs;
- renovation layers.

Owners:
- `floor-plan-technical-drawing`
- `interior-spatial-design`
- `architectural-design-engineering`.

### D. Computational/parametric architecture and building performance

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 21 | compas-dev/compas | A/D | ABSORB_METHOD_ONLY |
| 22 | Sverchok/Sverchok | A/D | KEEP_EXTERNAL_REFERENCE |
| 23 | blender/blender | D | ROUTE_EXISTING / KEEP_EXTERNAL_REFERENCE |
| 24 | ladybug-tools/ladybug | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 25 | ladybug-tools/honeybee-core | A/D | ABSORB_METHOD_ONLY |
| 26 | ladybug-tools/honeybee-energy | A/D | ABSORB_METHOD_ONLY |
| 27 | openstudiocoalition/OpenStudio | A/D | ABSORB_METHOD_ONLY |

Capabilities adotadas:
- computational geometry;
- climate grounding;
- sun/solar;
- daylight;
- envelope;
- thermal/energy assumptions;
- scenario analysis;
- distinction between early-design simulation and compliance.

Owner:
- `building-performance-analysis`.

Blender stays routed through existing 3D capabilities; it does not justify a new architecture-specific modeling owner by itself.

### E. Structural/civil engineering

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 28 | OpenSees/OpenSees | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 29 | KratosMultiphysics/Kratos | A/D | ABSORB_METHOD_ONLY |
| 30 | FOSSEE/OSDAG | A/D | ABSORB_METHOD_ONLY |

Additional references examined during validation:
- sfepy/sfepy
- SteveDoyle2/pyNastran

Capabilities adotadas:
- structural nodes/elements;
- material/section properties;
- boundary conditions;
- load cases;
- combinations;
- mesh fidelity;
- static/dynamic/nonlinear/modal analysis;
- result plausibility/equilibrium;
- convergence/model checks;
- professional review gate.

Owner:
- `structural-analysis-modeling`.

## Architectural Design Engineering

### Lacuna

Existing 3D skills reconstruct/model assets, but they do not own the design problem:
- users;
- program;
- area targets;
- adjacencies;
- zoning;
- circulation;
- existing conditions;
- layout alternatives.

### Decisão

Criar `architectural-design-engineering`.

Study/planning is kept separate from technical drawing and buildability.

## Floor Plan & Technical Drawing

### Lacuna

The Arsenal had diagramming, not architectural plan production.

New capability:
- scale;
- walls/openings;
- dimension hierarchy;
- annotations;
- north/title/revision;
- furniture clearance;
- storey continuity;
- existing/demolition/new graphics;
- export/readback.

### Decisão

Criar `floor-plan-technical-drawing`.

## CAD Parametric Modeling

### Lacuna

`procedural-3d-reconstruction` creates procedural Three.js assets, but does not own dimensional CAD, sketches, feature history, B-Rep or production drawings.

### Decisão

Criar `cad-parametric-modeling`.

Key distinction:
- mesh/render geometry for visualization;
- B-Rep/parametric geometry for editable technical intent.

## BIM & IFC Engineering

### Lacuna

No owner existed for semantic building models or IFC coordination.

### Decisão

Criar `bim-ifc-engineering`.

Key distinction:
- mesh says how something looks;
- BIM also says what it is, where it belongs, how it relates and which properties it owns.

## Interior Spatial Design

### Lacuna

The Arsenal can create visual direction and assets, but did not own furniture layout, ergonomic clearances, renovation layers or 2D/3D parity.

### Decisão

Criar `interior-spatial-design`.

## Building Performance Analysis

### Lacuna

No owner covered sun/daylight/climate/energy at building scale.

### Decisão

Criar `building-performance-analysis`.

Simulation outputs are explicitly directional unless inputs, solver and applicable standards support stronger claims.

## Structural Analysis Modeling

### Lacuna

No owner covered structural-analysis model definition.

### Decisão

Criar `structural-analysis-modeling` with high professional boundary.

The skill supports setup, interpretation and checks. It does not authorize construction or replace structural engineer sign-off.

## Stack

Created `architectural-design-cycle`:

`brief → program → existing conditions → layout → technical plan → CAD → 3D/interiors → BIM → environmental/structural analysis → QA → handoff`

Skills load only when required.

## Safety and professional boundary

Verdict geral: **CAUTION / HIGH for structural/buildability claims**.

Risk surfaces:
- inaccurate site/as-built measurements;
- structural wall removal;
- code/fire/accessibility assumptions;
- electrical/plumbing/MEP conflicts;
- structural analysis;
- construction documents;
- automated IFC mutations;
- false confidence from rendered visuals or simulation heatmaps.

Adaptations:
- study ≠ executive design;
- render ≠ technical validation;
- IFC syntax validity ≠ BIM quality;
- solver success ≠ structural correctness;
- current local standards must be grounded when material;
- professional review/sign-off remains required where applicable;
- destructive edits to live BIM/project files need approval and version preservation.

No CAD/BIM/solver installation or external binary was executed during evaluation.

## Materialização

Criados:
- `skills/architectural-design-engineering/SKILL.md`
- `skills/floor-plan-technical-drawing/SKILL.md`
- `skills/cad-parametric-modeling/SKILL.md`
- `skills/bim-ifc-engineering/SKILL.md`
- `skills/interior-spatial-design/SKILL.md`
- `skills/building-performance-analysis/SKILL.md`
- `skills/structural-analysis-modeling/SKILL.md`
- `stacks/architectural-design-cycle/STACK.md`

Atualizado:
- `ARSENAL INDEX.md`

## Limites

- The 30 repositories were triaged by capability; the strongest candidates were read more deeply.
- No repository was executed.
- CAD/BIM APIs and schemas can be version-sensitive.
- building codes, accessibility, fire and structural standards are jurisdiction/date specific.
- rendering and virtual renovation remain visualization, not proof of construction feasibility.
