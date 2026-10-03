---
name: game-development-cycle
description: "Conduzir jogos 2D/3D da ideia ao vertical slice, implementação por engine, validação jogável, multiplayer/performance quando necessários e build verificável sem escolher tecnologia antes do requisito."
---

# Game Development Cycle

## Objetivo

Orquestrar criação e evolução de jogos com o menor conjunto de skills necessário, mantendo gameplay verificável no centro.

## Router

Sempre considerar:
- `game-development-engineering`

Unity:
- `unity-game-engineering`

Multiplayer:
- `game-networking-engineering`

Performance:
- `game-performance-engineering`

AI/NPCs:
- `game-ai-engineering`

Geração procedural de levels/worlds:
- `procedural-game-content`

LiveOps/economia/backend mutável:
- `live-game-operations-engineering`

XR/VR/AR/MR:
- `xr-game-engineering`

Especializações existentes:
- shaders/VFX → `shader-graphics-engineering`
- sprite sheets → `sprite-sheet-pipeline`
- asset 3D de referência → `concept-to-3d-asset`
- procedural 3D web/Three.js → `procedural-3d-reconstruction`
- bugs → `debug-and-fix`
- versões de libs/packages → `library-version-grounding`

## Fluxo

1. **Concept contract**
   - gênero/core loop;
   - 2D/3D;
   - plataforma;
   - single/multiplayer;
   - visual direction;
   - performance constraints;
   - scope do primeiro vertical slice.

2. **Engine grounding**
   - engine/version;
   - packages/plugins;
   - render pipeline;
   - source control;
   - target build.

3. **Vertical slice**
   - uma cena/arena;
   - input;
   - movimento/interação principal;
   - game state;
   - feedback;
   - win/fail/reset.

4. **Runtime verify**
   - jogar o slice;
   - logs;
   - state transitions;
   - reload/retry;
   - build quando o requisito depende da plataforma.

5. **Expand only after proof**
   - conteúdo;
   - systems;
   - AI/navigation → `game-ai-engineering`;
   - geração procedural → `procedural-game-content`;
   - multiplayer → `game-networking-engineering`;
   - persistence/live ops/economy → `live-game-operations-engineering`;
   - XR interaction/runtime → `xr-game-engineering`;
   - polish.

6. **Performance gate**
   - quando o slice já representa workload real, medir no target;
   - otimizar bottleneck dominante;
   - repetir baseline.

7. **Build/release**
   - build real;
   - smoke test;
   - version/package record;
   - regressions conhecidas;
   - rollback/version control.

## Regra de seleção

Não carregar todas as skills. Um jogo single-player 2D simples pode usar apenas `game-development-engineering` + skill da engine. Multiplayer, performance, AI, procedural, LiveOps e XR entram somente quando o requisito existe.

## Critério de conclusão

- loop jogável observável;
- comportamento central verificado;
- engine/version registradas;
- erros relevantes resolvidos;
- build/player testado quando possível;
- limites não testados explicitamente reportados.

## Provenance

Stack construída a partir dos lotes 2026-10-02 de game development. O primeiro lote usou Unity-Technologies/skills, samples oficiais Unity, Godot demos, Bevy, Mirror e PurrNet; o segundo expandiu AI/NPCs, procedural content, LiveOps e XR com libgdx/gdx-ai, crashkonijn/GOAP, ProceduralToolkit, Edgar-Unity, WaveFunctionCollapse, Unity Gaming Services samples, Nakama, PlayFab, XR Interaction Toolkit Examples, AR Foundation e OpenXR.
