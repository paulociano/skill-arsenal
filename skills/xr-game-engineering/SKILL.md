---
name: xr-game-engineering
description: "Projetar e validar experiências VR/AR/MR com OpenXR quando possível, tracking spaces, locomotion, grab/gaze/UI espacial, hands/controllers, conforto, performance e testes em dispositivo real."
---

# XR Game Engineering

## Objetivo

Construir interação espacial robusta separando tracking/runtime da lógica de interação e validando no dispositivo real, com conforto e performance como requisitos funcionais.

## Quando usar

- VR;
- AR;
- MR/passthrough;
- OpenXR;
- XR Interaction Toolkit;
- AR Foundation;
- WebXR;
- controllers/hands/gaze;
- locomotion e spatial UI.

## Princípio central

**Pose/input source e interaction semantics são camadas diferentes.**

Um grab não deveria precisar saber se a pose veio de OpenXR, hand tracking, controller ou simulator.

## Workflow

1. **Ground**
   - device/runtime;
   - OpenXR/vendor plugin/WebXR;
   - engine/package versions;
   - VR, AR ou MR;
   - controllers/hands/gaze;
   - room-scale/seated;
   - target refresh rate.

2. **Tracking spaces**
   - origin/reference space explícito;
   - local/floor/stage behavior;
   - recenter;
   - tracking loss/recovery;
   - não assumir world origin estável entre runtimes.

3. **Input abstraction**
   - actions semânticas;
   - poses;
   - select/activate;
   - haptics;
   - hand joints quando disponíveis;
   - vendor-specific extension isolada atrás de capability check.

4. **Interaction**
   - hover/focus;
   - select/grab;
   - sockets;
   - two-hand manipulation;
   - gaze;
   - world-space UI;
   - physics interactions.

5. **Locomotion**
   - teleport;
   - continuous move;
   - snap/smooth turn;
   - climb;
   - seated/room-scale;
   - comfort settings expostos quando possível.

6. **AR**
   - session lifecycle;
   - plane/mesh/anchor tracking;
   - hit test/raycast;
   - light/environment data;
   - permission flow;
   - tracking state precisa aparecer na UX.

7. **Comfort**
   - evitar aceleração/câmera artificial agressiva por default;
   - horizonte estável quando aplicável;
   - scale consistente;
   - snap turn/teleport como opções;
   - não mover câmera independentemente da cabeça sem justificativa forte.

8. **Performance**
   - target refresh rate define frame budget;
   - stereo rendering cost;
   - overdraw/transparency;
   - dynamic resolution/foveation quando runtime suportar;
   - thermal/mobile headset constraints.

9. **Simulator versus device**
   - simulator valida lógica básica;
   - não prova tracking, optics, comfort, controller pose, permissions nem performance;
   - device build é gate para conclusão de XR material.

10. **Cross-runtime**
    - preferir OpenXR/capabilities quando a feature existir de forma padronizada;
    - vendor extensions somente quando requisito exigir;
    - feature detection + fallback explícito;
    - não presumir hand/eye tracking em todo headset.

## Spatial UI

- tamanho físico e distância legível;
- targets maiores que desktop;
- ray/gaze/direct interaction podem exigir layouts diferentes;
- feedback de hover/select;
- evitar UI crítica fora do comfortable field of view;
- world-locked versus head-locked precisa ser decisão consciente.

## Testing matrix

- first launch/permissions;
- seated/standing;
- tracking loss;
- controllers disconnected;
- left/right handed;
- hands unavailable;
- boundary/guardian events quando expostos;
- pause/resume;
- device sleep;
- low performance/thermal condition;
- AR low-feature environment.

## Regras

- Editor preview não prova XR;
- simulator não substitui headset/device;
- OpenXR reduz coupling, não garante feature parity;
- interaction toolkit é implementação, não design de interação;
- frame drops em XR são também problema de conforto;
- tracking state deve ser tratado como state de produto, não exceção escondida.

## Integração

`game-development-engineering`, `unity-game-engineering`, `game-performance-engineering`, `crossplatform-mobile-engineering`, `shader-graphics-engineering`, `behavior-contract-validation` e `library-version-grounding`.

## Provenance

Consolidada de Unity XR Interaction Toolkit Examples, Unity AR Foundation Samples, Khronos OpenXR SDK e De-Panther/unity-webxr-export. Preserva abstraction de runtime, interaction semantics, tracking recovery e device validation sem exigir Unity, OpenXR loader ou WebXR runtime disponíveis.
