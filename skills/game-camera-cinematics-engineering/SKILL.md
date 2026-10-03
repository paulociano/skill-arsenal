---
name: game-camera-cinematics-engineering
description: "Projetar e validar câmeras de gameplay e sequências cinematográficas com framing, follow/aim, blends, damping, collision, camera states, shake e transições dirigidas por gameplay sem acoplar lógica de jogo à câmera."
---

# Game Camera & Cinematics Engineering

## Objetivo

Tratar câmera como sistema de percepção e composição, não como transform solto. O owner cobre gameplay camera, shot selection, blending, camera collision e sequências cinematográficas.

## Quando usar

- third/first-person camera;
- follow/aim/lock-on;
- top-down/isometric;
- camera zones;
- cinematic shots;
- cutscenes;
- blends/transitions;
- shake/impulse;
- camera collision/occlusion.

## Princípio central

**Gameplay produz alvos e intenção; a câmera decide enquadramento e transição.**

## Workflow

1. **Camera contract**
   - target(s);
   - framing goal;
   - player control;
   - allowed movement;
   - obstruction policy;
   - transition policy;
   - failure/recovery.

2. **State model**
   - gameplay;
   - aim;
   - lock-on;
   - traversal;
   - vehicle;
   - dialogue;
   - cinematic;
   - death/respawn.

3. **Composition**
   - follow target;
   - look-at target;
   - screen-space framing;
   - dead/soft zones;
   - field of view;
   - shoulder/offset;
   - damping.

4. **Transitions**
   - cut quando continuidade temporal não importa;
   - blend quando orientação espacial deve ser preservada;
   - duração e easing definidos por função;
   - interruptibility explícita.

5. **Collision/occlusion**
   - evitar câmera atravessar geometria;
   - não permitir clipping persistente;
   - shoulder swap/zoom-in/fade são estratégias possíveis;
   - priorizar legibilidade do alvo.

6. **Input**
   - separar look input de camera transform;
   - sensitivity por device;
   - invert axes;
   - dead zones;
   - recenter policy.

7. **Camera effects**
   - shake/impulse com amplitude/frequency/duration limitadas;
   - stacking controlado;
   - reduzir/desativar camera shake deve ser opção de acessibilidade.

8. **Cinematics**
   - shots e bindings versionáveis;
   - gameplay pause/ownership explícito;
   - skip precisa levar a state final válido;
   - subtitle/audio state deve permanecer coerente após skip.

9. **Verify**
   - edge geometry;
   - narrow spaces;
   - multiple targets;
   - target loss;
   - rapid state switches;
   - different aspect ratios;
   - high/low sensitivity;
   - skip/resume de cinematic.

## Regras

- câmera não deve possuir regra de gameplay crítica;
- damping não corrige camera state mal definido;
- shake não substitui feedback;
- cinematic skip deve aplicar consequências narrativas/gameplay necessárias;
- FOV e motion effects precisam considerar conforto/acessibilidade.

## Integração

`game-development-engineering`, `game-input-engineering`, `game-ui-accessibility-engineering`, `game-animation-engineering`, `xr-game-engineering` e `cinematic-visual-direction`.

## Provenance

Consolidada de Unity Cinemachine e padrões de camera systems em engines modernas. Preserva tracking, composition, blending, damping, shot/state separation e collision sem exigir Cinemachine.
