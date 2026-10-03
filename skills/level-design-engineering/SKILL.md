---
name: level-design-engineering
description: "Projetar, greyboxar, validar e iterar níveis de jogos por objetivos, rotas, affordances, pacing, encounter spaces, traversal, sightlines e métricas de navegação antes de substituir blockout por arte final."
---

# Level Design Engineering

## Objetivo

Transformar objetivos de gameplay em espaços jogáveis verificáveis, começando por greybox/blockout e só avançando para arte final após provar navegação, pacing, legibilidade e encounter flow.

## Quando usar

- criar ou revisar fases/mapas;
- greybox/blockout;
- FPS/TPS arenas;
- platformer traversal;
- dungeon/room layout;
- encounter spaces;
- checkpoints;
- objective placement;
- progression espacial.

## Princípio central

**Prove o espaço em geometria simples antes de investir em arte.**

## Workflow

1. **Level contract**
   - objetivo do jogador;
   - entry/exit;
   - critical path;
   - optional paths;
   - gameplay verbs exercitados;
   - target completion time;
   - fail/recovery.

2. **Greybox**
   - unidades/escala consistentes;
   - player dimensions;
   - jump/reach/move metrics;
   - cover/door/corridor widths;
   - elevation ranges;
   - navigation bounds.

3. **Flow**
   - critical path legível;
   - loops e shortcuts deliberados;
   - retorno/backtracking quando necessário;
   - gating por capability, key, encounter ou state;
   - evitar dead-end acidental.

4. **Sightlines**
   - revelar objetivo antes ou depois da ação conforme intenção;
   - landmarks;
   - occlusion;
   - combat range;
   - sniper/long-range dominance quando aplicável.

5. **Encounter spaces**
   - entradas/saídas;
   - cover/exposure;
   - flank routes;
   - spawn visibility;
   - retreat/recovery;
   - verticality;
   - AI navigation.

6. **Pacing**
   - tensão → resolução → exploração;
   - alternar intensidade;
   - checkpoints após esforço relevante;
   - não empilhar tutorial, combate e narrativa crítica no mesmo instante sem necessidade.

7. **Validation**
   - traversal sem noclip;
   - navmesh/pathing;
   - objective readability;
   - stuck points;
   - sequence breaks;
   - spawn safety;
   - timing real;
   - multiple play styles quando suportados.

8. **Art pass**
   - substituir greybox mantendo métricas e transforms canônicos;
   - arte não pode estreitar corredor, bloquear linha ou mudar cover silenciosamente;
   - validar colisão após cada substituição estrutural.

9. **Iteration**
   - registrar problema observado;
   - mudar uma hipótese por vez quando possível;
   - comparar heatmap/telemetry/playtest notes quando disponíveis;
   - não tratar preferência individual como regra universal.

## Metrics úteis

- tempo por segmento;
- deaths/fails;
- checkpoint retries;
- route choice;
- objective discovery delay;
- stuck/reversal points;
- encounter duration;
- combat distance distribution.

## Regras

- level bonito não prova level bom;
- navmesh válido não prova flow;
- landmark decorativo precisa ajudar orientação quando essa é sua função;
- esconder saída pode ser intencional, mas precisa ser testado;
- procedural layout deve passar pelos mesmos validators de level design.

## Integração

`game-development-engineering`, `procedural-game-content`, `game-ai-engineering`, `game-camera-cinematics-engineering`, `game-testing-quality-engineering` e `game-performance-engineering`.

## Provenance

Consolidada de TrenchBroom como referência de blockout/brush/entity authoring, Unity FPSSample para preview/traversal/weapon testing e práticas de greybox observadas em toolchains de Godot/Unity. Não exige editor específico.
