---
name: structural-analysis-modeling
description: "Estruturar modelos de análise estrutural com geometry, materials, sections, supports, load cases/combinations, mesh, solver assumptions e result checks, exigindo revisão profissional antes de qualquer decisão construtiva."
---

# Structural Analysis Modeling

## Objetivo

Organizar modelos estruturais reproduzíveis para análise preliminar ou apoio técnico, mantendo separação clara entre modelo computacional, norma e responsabilidade profissional.

## Quando usar

- frames/trusses;
- beams/columns;
- FEM;
- load cases;
- structural model review;
- steel/concrete structural analysis;
- modal/seismic analysis setup.

## Princípio central

**Um solver resolve o modelo informado, não valida se o modelo representa a estrutura real.**

## Workflow

1. **Scope**
   - system;
   - material;
   - geometry;
   - analysis type;
   - code/jurisdiction;
   - required outputs.

2. **Geometry**
   - nodes;
   - members/elements;
   - connectivity;
   - offsets;
   - releases;
   - local axes.

3. **Properties**
   - material;
   - section;
   - stiffness;
   - density;
   - nonlinear behavior if used.

4. **Boundary conditions**
   - supports;
   - restraints;
   - springs;
   - diaphragm/contact assumptions.

5. **Loads**
   - self-weight;
   - dead/live;
   - wind;
   - seismic;
   - temperature;
   - equipment;
   - load path explicit.

6. **Combinations**
   - code-based factors only from current authoritative source;
   - serviceability vs strength separated.

7. **Mesh/model fidelity**
   - element type;
   - refinement;
   - convergence where meaningful;
   - shell/solid/frame choice justified.

8. **Solve**
   - linear/nonlinear;
   - static/dynamic;
   - modal;
   - stability/buckling as appropriate.

9. **Checks**
   - reaction balance;
   - deformed shape;
   - force diagrams;
   - displacement scale;
   - stress/result plausibility;
   - equilibrium;
   - mesh sensitivity;
   - known benchmark/simple hand check when possible.

10. **Report**
   - assumptions;
   - units;
   - load cases;
   - solver;
   - result envelopes;
   - limitations;
   - items for engineer review.

## Guardrails

- no construction approval from AI-only analysis;
- do not invent load factors or code limits;
- current structural code must be verified for jurisdiction;
- instability/singularity warnings are blockers, not cosmetic;
- pretty contour plots do not prove correctness;
- model changes affecting safety require qualified structural engineer review.

## Integração

`architectural-design-engineering`, `bim-ifc-engineering`, `cad-parametric-modeling`, `building-performance-analysis`, `verify-before-claim`.

## Provenance

Consolidada de OpenSees, Kratos Multiphysics, SfePy, pyNastran, OSDAG e IFC structural-analysis workflows. Não presume solver instalado ou professional sign-off.
