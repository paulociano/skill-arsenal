---
name: building-performance-analysis
description: "Analisar desempenho ambiental de edifícios por clima, orientação, insolação, daylight, envelope, energia e cenários com modelos explícitos e validação de assumptions antes de tratar simulação como decisão."
---

# Building Performance Analysis

## Objetivo

Avaliar como geometria, orientação, clima, envelope e uso afetam conforto ambiental e energia.

## Quando usar

- insolação;
- daylight;
- shading;
- orientação;
- envelope;
- energy model;
- thermal loads;
- early-stage environmental design.

## Workflow

1. **Ground**
   - location/weather file;
   - north/orientation;
   - model geometry;
   - zones/spaces;
   - usage/schedules;
   - analysis period.

2. **Climate**
   - temperature;
   - solar;
   - humidity;
   - wind;
   - sky condition.

3. **Geometry**
   - envelope;
   - apertures;
   - shading;
   - surrounding context;
   - adjacency.

4. **Daylight/solar**
   - sun path;
   - radiation;
   - direct sun hours;
   - illuminance/daylight metrics as appropriate;
   - glare risk where modeled.

5. **Energy**
   - constructions/U-values;
   - infiltration/ventilation;
   - internal loads;
   - schedules;
   - HVAC assumptions;
   - ideal loads vs explicit systems distinguished.

6. **Scenario**
   - glazing;
   - shading;
   - orientation;
   - insulation;
   - occupancy;
   - system efficiency.

7. **Validation**
   - units;
   - weather source;
   - geometry sanity;
   - schedules;
   - energy balance/plausibility;
   - sensitivity.

8. **Output**
   - assumptions;
   - metrics;
   - comparisons;
   - uncertainty;
   - design implication.

## Regras

- simulation accuracy cannot exceed input quality;
- early-stage models are directional, not compliance proof;
- energy/daylight standards depend on jurisdiction/version;
- visual heatmaps need numeric interpretation.

## Integração

`architectural-design-engineering`, `bim-ifc-engineering`, `interior-spatial-design`, `scenario-forecasting`.

## Provenance

Consolidada de Ladybug Tools, Honeybee, Dragonfly and OpenStudio workflows. Não presume EnergyPlus/Radiance/OpenStudio instalados.
