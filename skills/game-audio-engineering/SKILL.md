---
name: game-audio-engineering
description: "Projetar e validar áudio de jogos com eventos, buses/mixers, spatialization, concurrency, adaptive music, ducking, pooling, DSP budget e integração observável com gameplay."
---

# Game Audio Engineering

## Objetivo

Tratar áudio como sistema de feedback e mix em tempo real, com roteamento, prioridade, espacialização e orçamento, não como chamadas soltas de PlaySound.

## Quando usar

- SFX e ambience;
- audio mixer/buses;
- spatial/3D audio;
- adaptive music;
- voice/dialogue playback;
- ducking;
- audio pooling/concurrency;
- DSP/native audio;
- mix e performance.

## Workflow

1. **Audio contract**
   - evento de gameplay;
   - asset/event de áudio;
   - bus;
   - priority;
   - spatial/non-spatial;
   - concurrency;
   - lifecycle/stop behavior.

2. **Routing**
   - Master;
   - Music;
   - SFX;
   - Voice;
   - UI;
   - Ambience;
   - sub-buses quando realmente necessários.

3. **Concurrency**
   - limite por event/family;
   - steal policy;
   - cooldown/random variation;
   - evitar centenas de instâncias idênticas.

4. **Spatial audio**
   - attenuation curve;
   - min/max distance;
   - listener model;
   - occlusion/obstruction apenas onde o custo justificar;
   - HRTF/vendor spatializer atrás de capability/config explícita.

5. **Adaptive music**
   - separar musical state de gameplay signal;
   - transitions em beat/bar quando necessário;
   - layers/stems ou sections;
   - hysteresis para evitar troca nervosa.

6. **Ducking**
   - sidechain ou snapshot/state;
   - voice/dialogue pode reduzir music/SFX de forma controlada;
   - attack/release coerentes;
   - accessibility options preservadas.

7. **Asset policy**
   - compression/streaming por duração e plataforma;
   - mono/stereo coerentes;
   - loudness/peak QA;
   - loop points verificados;
   - sample rate sem exagero sem benefício audível.

8. **Runtime**
   - preload versus stream;
   - pool somente quando churn justificar;
   - release/stop handles corretamente;
   - pause/resume e scene transitions.

9. **Profile**
   - voices ativas;
   - DSP/CPU;
   - memory;
   - streaming stalls;
   - clipping;
   - mixer headroom.

10. **Verify**
    - headphones/speakers relevantes;
    - low/high volume;
    - overlapping events;
    - pause/resume;
    - scene reload;
    - target device quando áudio/platform backend importar.

## Regras

- aumentar volume não corrige mix;
- compressor/limiter não substitui headroom;
- audio event precisa de lifecycle;
- spatialize tudo é caro e desnecessário;
- música adaptativa sem hysteresis tende a oscilar;
- plugin/backend específico não deve contaminar gameplay code.

## Integração

`game-development-engineering`, `game-animation-engineering`, `game-performance-engineering`, `xr-game-engineering` e `library-version-grounding`.

## Provenance

Consolidada de FMOD for Unity, Unity Native Audio Plugin SDK e práticas de mixers/event systems. O Arsenal absorve routing, event lifecycle, spatialization e profiling sem presumir FMOD, Wwise ou plugin nativo disponível.
