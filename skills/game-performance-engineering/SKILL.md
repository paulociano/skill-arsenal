---
name: game-performance-engineering
description: "Diagnosticar e otimizar performance de jogos por frame budget, CPU/GPU profiling, memory/GC, rendering, physics, assets, streaming e entity scale, sempre com baseline e comparação antes/depois."
---

# Game Performance Engineering

## Objetivo

Tratar performance como orçamento mensurável por plataforma e cena, não como coleção de micro-otimizações.

## Quando usar

- FPS abaixo da meta;
- stutter/hitches;
- GC spikes;
- draw-call/render bottlenecks;
- physics cost;
- muitos entities/NPCs/projectiles;
- loading/streaming lento;
- mobile/web/VR constraints;
- DOTS/Jobs/Burst/parallelization.

## Workflow

1. Definir target platform/device, target FPS, frame budget, memory budget e worst-case scene.
2. Reproduzir cenário fixo e capturar CPU frame, GPU frame, memory/GC, rendering stats e physics.
3. Classificar bottleneck: main thread, GPU/render, scripts, physics, animation, UI, allocation/GC, asset IO, networking ou shader variants.
4. Corrigir o custo dominante primeiro: reduzir trabalho, frequência ou escopo antes de adicionar complexidade.
5. Escalar para Jobs/Burst/ECS/SIMD apenas quando workload grande e paralelizável justificar.
6. Revisar assets: textures, meshes, bones, audio, atlases, bundles/addressables e import settings por plataforma.
7. Revisar physics: collider complexity, fixed timestep, layers, sleeping, continuous collision e query frequency.
8. Repetir o mesmo cenário na mesma build/device e comparar antes/depois.
9. Verificar regressão visual e de gameplay antes de manter a otimização.

## Frame budgets

Referências matemáticas:
- 30 FPS ≈ 33.3 ms;
- 60 FPS ≈ 16.7 ms;
- 90 FPS ≈ 11.1 ms;
- 120 FPS ≈ 8.3 ms.

São budgets de referência, não metas universais. CPU e GPU podem sobrepor; usar profiler da engine/plataforma.

## Rendering

Investigar:
- overdraw;
- draw calls/state changes;
- material proliferation;
- shader complexity;
- lights/shadows;
- post-processing;
- transparency;
- LOD/culling;
- resolution;
- shader variant compilation.

## Memory

- separar asset memory, managed heap, resident memory e temporary allocations;
- encontrar a fonte de allocations antes de intervir no GC;
- pooling só quando churn e frequência justificarem;
- pool superdimensionado pode apenas trocar GC por memória ociosa.

## Platform-specific adaptation

Otimização por plataforma deve partir de sinais reais do device/runtime:
- thermal state;
- CPU/GPU bottleneck;
- battery/power state;
- memory pressure;
- refresh rate;
- resolution;
- available feature set.

Quando o runtime expuser adaptive-performance signals:
- definir quality tiers e knobs explícitos;
- reduzir custo gradualmente, não em saltos arbitrários;
- manter hysteresis para evitar quality thrashing;
- separar ajustes temporários por thermal/power de preferências persistentes do usuário;
- registrar qual knob mudou e por quê;
- testar recovery quando o device volta a condições normais.

Exemplos de knobs:
- render scale;
- shadow distance/quality;
- LOD bias;
- post-processing;
- particles;
- simulation frequency;
- streaming budget.

Mobile optimization deve considerar sustained performance, não apenas FPS frio nos primeiros minutos.

## Regras

- profile player/release quando possível;
- otimização sem baseline é hipótese;
- FPS médio pode esconder hitch;
- editor overhead pode distorcer;
- reduzir qualidade sem localizar bottleneck não é diagnóstico;
- a otimização fica somente se melhorar o budget sem quebrar gameplay/visual.

## Integração

Combina com `game-development-engineering`, `unity-game-engineering`, `game-networking-engineering`, `shader-graphics-engineering`, `diagnosing-bugs` e `verify-before-claim`.

## Provenance

Consolidada de Unity EntityComponentSystemSamples, ECS Network Racing, samples oficiais Unity e princípios data-oriented observados em Bevy/Fyrox. Não assume Profiler ou Frame Debugger específico disponível; exige medição real do projeto.
