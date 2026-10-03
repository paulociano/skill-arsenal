---
name: interactive-world-simulation
description: "Projetar mundos interativos persistentes gerados ou mediados por IA com world state, scenes, interactions, branches, history, replay e provider boundaries, preservando continuidade causal e estado verificável ao longo do tempo."
---

# Interactive World Simulation

## Objetivo

Construir mundos que continuam evoluindo entre cenas e interações sem perder identidade, causalidade ou estado.

## Quando usar

- persistent AI worlds;
- interactive generated environments;
- multimodal world simulation;
- branching scenes;
- AI-native games;
- replayable generated experiences;
- text/voice/image interaction with persistent state.

## Princípio central

**Cena é uma projeção do mundo; não é o mundo inteiro.**

## Modelo

Separar:
- **World**: regras, contexto e estado persistente;
- **Scene**: momento gerado a partir do estado atual;
- **Interaction**: input humano/agente/evento;
- **Branch**: continuação alternativa;
- **History**: estados, escolhas e transições registradas;
- **Output**: preview/live/render;
- **Replay**: reconstrução de um caminho anterior.

## Workflow

1. **World contract**
   - identity;
   - invariant rules;
   - mutable state;
   - actors/entities;
   - time model;
   - allowed interactions.

2. **State schema**
   - separar fatos duráveis de conteúdo visual efêmero;
   - IDs estáveis;
   - versionamento;
   - explicit defaults;
   - branch lineage.

3. **Understand**
   - prompt;
   - image;
   - voice;
   - selected region/object;
   - prior scene context;
   - map each input to candidate state effects.

4. **Simulate**
   - update state;
   - enforce invariants;
   - derive possible actions/events;
   - preserve causal continuity;
   - record uncertainty when the model invents missing detail.

5. **Generate scene**
   - scene brief from current state;
   - renderer/model replaceable;
   - continuity requirements explicit;
   - generated media is derivative, not canonical state.

6. **Interaction**
   - classify input;
   - resolve target/referent;
   - validate against allowed actions;
   - apply transition;
   - record actor, timestamp and resulting state.

7. **Branching**
   - fork state deliberately;
   - branch IDs;
   - parent pointer;
   - no silent cross-branch state bleed;
   - compare/merge only by explicit rule.

8. **History and replay**
   - preserve transition log;
   - replay should reconstruct state/path without relying on hidden model memory;
   - cached media can accelerate preview but does not replace state/history.

9. **Provider boundaries**
   - understanding model;
   - simulation/reasoning;
   - image/video renderer;
   - speech;
   - live output;
   - each is replaceable behind a contract.

10. **Continuity evaluation**
   - entity identity;
   - spatial consistency;
   - inventory/state consistency;
   - causal consistency;
   - branch isolation;
   - replay consistency;
   - temporal drift.

## Regras

- generated scene must not silently overwrite canonical world state;
- visual continuity is not enough if logical state contradicts;
- branch history must be inspectable;
- provider output needs normalization before entering world state;
- persistent state should remain user-controlled/exportable where possible;
- roadmap features are not current capabilities;
- live output requires separate latency, moderation and safety gates.

## Integração

`game-development-engineering`, `procedural-game-content`, `narrative-dialogue-engineering`, `game-ai-engineering`, `save-game-persistence-engineering`, `embodied-agent-evaluation`.

## Provenance

Adaptada de BuzzPlay/infinite-world. Preserva world → scene → interaction → branch → history → replay, multimodal interaction e provider replaceability, sem presumir Whisper, FFmpeg, live streaming ou um gerador específico.
