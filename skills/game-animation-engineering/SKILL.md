---
name: game-animation-engineering
description: "Projetar, integrar e validar animação de personagens e objetos em jogos com state graphs, blending, root motion, rigging/IK, events, procedural layers e ownership explícito entre gameplay, physics e animation."
---

# Game Animation Engineering

## Objetivo

Construir animação como sistema de estado e movimento integrado ao gameplay, evitando graphs opacos, transições frágeis e conflito entre Animator, physics e code-driven motion.

## Quando usar

- locomotion/idle/run/jump/combat;
- animation state machines;
- blend trees/layers;
- root motion;
- IK/rig constraints;
- procedural animation;
- animation events;
- retargeting;
- animation performance/debugging.

## Princípio central

**Gameplay decide intenção; animation apresenta e, quando explicitamente escolhido, contribui movimento.**

## Workflow

1. Definir contract por estado: trigger/condition, entrada, saída, interruptibility e observable result.
2. Declarar ownership do deslocamento: transform/controller, physics ou root motion.
3. Separar logical state de animation state quando não forem equivalentes.
4. Usar blend contínuo para parâmetros contínuos; usar transição explícita para mudanças semânticas.
5. Evitar transições globais que possam disparar de estados inesperados.
6. Rig/IK entra como camada sobre pose base, com weight e fallback claros.
7. Animation events servem como sinais de presentation/gameplay cuidadosamente delimitados; lógica crítica não deve depender de frame/evento impossível de reproduzir.
8. Sincronizar hit windows, VFX/SFX e movement windows por timeline/state verificável.
9. Tratar cancel/interruption, hit reaction, death e reload como estados reais, não exceções espalhadas.
10. Validar no runtime com slow motion/debug overlay quando útil.

## Root motion

Se root motion controla deslocamento:
- gameplay ainda valida colisão/authority;
- rede precisa de estratégia de replication/prediction compatível;
- clips precisam de velocidade/escala coerentes;
- transition blending não pode introduzir drift não intencional.

## Rigging e IK

- constraint hierarchy clara;
- world/local spaces explícitos;
- weights animáveis;
- chain limits;
- target loss fallback;
- ordem de avaliação importa;
- medir custo em personagens numerosos.

## Performance

- animation LOD/culling;
- reduzir rig constraints fora de relevância;
- limitar layers e masks;
- compression e sampling proporcionais ao asset;
- medir CPU por character e worst-case crowd.

## Regras

- Animator graph não substitui gameplay state;
- root motion e physics não podem disputar a mesma transformação sem contrato;
- animation event não é barramento global;
- visual blend correto não prova timing de gameplay correto;
- mudanças em skeleton/avatar/retargeting exigem revalidação de clips.

## Integração

`game-development-engineering`, `unity-game-engineering`, `game-ai-engineering`, `game-networking-engineering`, `game-performance-engineering` e `behavior-contract-validation`.

## Provenance

Consolidada de Unity Animation Rigging, Unity.Animation.Samples e padrões de runtime animation observados em Animancer. Preserva state/blending, rig constraints, ownership de movimento e validation sem exigir package específico.
