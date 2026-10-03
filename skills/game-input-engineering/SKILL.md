---
name: game-input-engineering
description: "Projetar e validar input de jogos por actions semânticas, device abstraction, rebinding, control schemes, dead zones, local multiplayer, UI/game focus e persistência de bindings."
---

# Game Input Engineering

## Objetivo

Desacoplar intenção do jogador de teclas, botões ou dispositivos concretos, permitindo múltiplos control schemes, rebinding e comportamento consistente entre gameplay e UI.

## Quando usar

- keyboard/mouse;
- gamepad;
- touch/on-screen controls;
- input actions;
- rebinding;
- local multiplayer;
- device switching;
- input recording;
- accessibility de controles.

## Princípio central

**Gameplay consome actions; devices produzem bindings.**

## Workflow

1. **Action map**
   - mover;
   - olhar;
   - interagir;
   - atacar;
   - navegar UI;
   - pause;
   - actions contextuais.

2. **Control schemes**
   - keyboard/mouse;
   - gamepad;
   - touch;
   - XR;
   - custom devices quando realmente suportados.

3. **Binding**
   - primary/secondary bindings;
   - chords/composites quando necessários;
   - dead zones;
   - sensitivity;
   - inversion;
   - hold/tap/press semantics.

4. **Rebinding**
   - detectar conflito;
   - permitir cancelar/resetar;
   - impedir binding impossível;
   - persistir por profile;
   - restaurar defaults;
   - UI deve mostrar glyph/text do binding atual.

5. **Context/focus**
   - gameplay versus UI;
   - modal/pause;
   - text entry;
   - prevent double-consumption;
   - device hot-swap.

6. **Local multiplayer**
   - device ownership por player;
   - join/leave;
   - split-screen assignment quando aplicável;
   - reconnect sem trocar player silenciosamente.

7. **Accessibility**
   - remapping completo sempre que possível;
   - toggle versus hold;
   - sensitivity ranges;
   - stick dead-zone tuning;
   - one-handed alternatives quando o design permitir;
   - não exigir input simultâneo desnecessário.

8. **Recording/testing**
   - input trace/replay quando runtime suportar;
   - testar device disconnect/reconnect;
   - alt-tab/focus loss;
   - multiple devices;
   - rapid input;
   - UI/game overlap.

## Regras

- hardcoded keycode não é action contract;
- binding default não é binding obrigatório;
- device detection não deve reconfigurar controles sem feedback;
- UI prompts precisam acompanhar o scheme atual;
- não persistir binding por índice instável quando existe ID estável.

## Integração

`game-development-engineering`, `game-ui-accessibility-engineering`, `xr-game-engineering`, `save-game-persistence-engineering` e `unity-game-engineering`.

## Provenance

Consolidada do Unity Input System, incluindo actions, control schemes, rebinding, UI/game input, on-screen controls, local multiplayer e input tracing. Não exige Unity Input System.
