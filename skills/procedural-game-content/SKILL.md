---
name: procedural-game-content
description: "Projetar e validar geração procedural de níveis, mapas, cidades, dungeons, terrenos e spawns com seeds reproduzíveis, constraints explícitas, validação de jogabilidade e bounded regeneration."
---

# Procedural Game Content

## Objetivo

Gerar conteúdo de jogo a partir de regras e constraints verificáveis, mantendo variedade sem sacrificar jogabilidade, navegabilidade, performance ou reprodutibilidade.

## Quando usar

- dungeon/level generation;
- terrain/caves/cities/buildings;
- Wave Function Collapse;
- cellular automata;
- graph/layout generation;
- procedural spawning;
- runtime mesh/content generation.

## Princípio central

**Randomness propõe; constraints e validators decidem.**

Pipeline:

`seed → structure → constraints → decorate → validate → accept/regenerate`

## Workflow

1. **Generation contract**
   - output desejado;
   - dimensão/escala;
   - seed;
   - hard constraints;
   - soft preferences;
   - gameplay requirements;
   - perf/memory budget.

2. **Choose representation**
   - grid/tile;
   - graph/rooms/connections;
   - modules/connectors;
   - heightfield/voxel;
   - spline/road graph;
   - mesh/geometry.

3. **Choose generator**
   - cellular automata para caves/organic regions;
   - graph/grammar para layouts conectados;
   - BSP/room placement para dungeon structure;
   - noise para campos contínuos;
   - WFC/constraint propagation para module adjacency;
   - hybrid quando cada estágio tem responsabilidade distinta.

4. **Seedability**
   - seed explícita;
   - mesma versão + config + seed deve reproduzir quando o algoritmo promete determinismo;
   - versionar config/tileset/module rules;
   - não usar global random state de forma invisível.

5. **Hard validation**
   - conectividade;
   - spawn alcançável;
   - critical path;
   - room/door compatibility;
   - no overlaps impossíveis;
   - navigation pass;
   - bounds/minimum space;
   - required encounters/resources.

6. **Soft scoring**
   - pacing;
   - density;
   - branching;
   - sightlines;
   - exploration;
   - aesthetic repetition.

Hard failure rejeita. Soft score ajuda a escolher entre candidatos; não deve mascarar geração inválida.

7. **Bounded regeneration**
   - limite de attempts;
   - registrar failure reason;
   - não loopar indefinidamente esperando uma seed válida;
   - se failure rate for alto, corrigir constraints/generator.

8. **Decoration**
   - separar layout estrutural de props/detail;
   - decoration não pode bloquear critical path;
   - spawn tables com regras de distância, biome/zone e exclusão.

9. **Runtime generation**
   - chunk/stream quando mundo for grande;
   - generation budget por frame/tick;
   - cache/pooling somente quando medido;
   - persistir seed + player-authored changes em vez de mundo inteiro quando apropriado.

10. **Verify**
    - corpus de seeds;
    - edge seeds;
    - invariants automáticos;
    - playability sampling;
    - profiling;
    - visual review apenas como camada complementar.

## WFC

WFC é constraint propagation sobre compatibilidade local, não garantia de level design global.

Adicionar validators externos para:
- reachability;
- gameplay loops;
- critical structures;
- macro pacing.

Backtracking/restart precisa de budget e telemetry de contradições.

## Regras

- procedural não significa random sem contrato;
- uma seed bonita não prova robustez;
- sempre testar múltiplas seeds;
- geração válida geometricamente pode ser ruim de jogar;
- parâmetros precisam de ranges defensivos;
- conteúdo procedural não deve depender de ordem acidental de objetos quando determinismo importa.

## Integração

`game-development-engineering`, `game-ai-engineering`, `game-performance-engineering`, `shader-graphics-engineering`, `procedural-3d-reconstruction` quando o output for um objeto 3D específico, e `tdd` para invariants.

## Provenance

Consolidada de Syomus/ProceduralToolkit, OndrejNepozitek/Edgar-Unity, mxgmn/WaveFunctionCollapse e marian42/wavefunctioncollapse. Preserva seeds, constraint solving, modular generation, geometry e validation sem exigir Unity nem uma biblioteca específica.
