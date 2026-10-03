---
name: game-ui-accessibility-engineering
description: "Projetar e validar HUDs, menus e opções de acessibilidade em jogos com focus/navigation, legibilidade por distância, safe areas, subtitles/captions, color-safe cues, scalable UI, input remapping e feedback multimodal."
---

# Game UI & Accessibility Engineering

## Objetivo

Construir interface de jogo para legibilidade, navegação e feedback sob diferentes dispositivos, distâncias, limitações sensoriais/motoras e contextos de gameplay.

## Quando usar

- HUD;
- menus/settings;
- inventory/map/quest UI;
- gamepad navigation;
- subtitles/captions;
- colorblind/high contrast;
- UI scale/text scale;
- visual alternatives to audio;
- accessibility settings.

## Princípio central

**Informação crítica não deve depender de um único canal sensorial ou de um único modo de input.**

## Workflow

1. **UI contract**
   - task;
   - state;
   - action;
   - feedback;
   - error/recovery.

2. **HUD**
   - mostrar informação acionável;
   - esconder ruído quando irrelevante;
   - prioridades visuais;
   - contextual HUD apenas quando não prejudica descoberta.

3. **Menu navigation**
   - focus visível;
   - ordem previsível;
   - keyboard/gamepad/touch;
   - focus recovery após modal;
   - wrap apenas quando coerente.

4. **Legibility**
   - text scale;
   - contrast;
   - viewing distance;
   - TV/console safe areas;
   - handheld pass;
   - não codificar estado apenas por cor.

5. **Subtitles/captions**
   - speaker identification quando necessário;
   - tamanho configurável;
   - background/contrast;
   - non-dialogue cues quando informação crítica;
   - sincronização com skip/pause.

6. **Audio alternatives**
   - cue visual/haptic para evento essencial;
   - directional indicator quando direção sonora é gameplay-critical;
   - volume separado por music/SFX/voice/UI.

7. **Motor/input accessibility**
   - rebinding;
   - toggle/hold options;
   - sensitivity/dead zones;
   - timing windows ajustáveis quando apropriado;
   - evitar mash/hold simultâneo como default quando não é parte essencial do desafio.

8. **Motion/photosensitivity**
   - reduce camera shake;
   - reduce flashes;
   - reduce motion;
   - warning quando conteúdo inevitável exigir;
   - não esconder critical information em efeitos transitórios.

9. **Persistence**
   - accessibility/settings fora do save de campanha quando são preferências do jogador;
   - defaults seguros;
   - primeiras telas críticas não devem exigir navegar por UI inacessível para ativar acessibilidade.

10. **Verify**
    - mouse/keyboard;
    - controller-only;
    - text/UI scale;
    - grayscale/color simulation quando útil;
    - muted audio;
    - reduced motion;
    - subtitle-only comprehension;
    - common aspect ratios e safe areas.

## Regras

- acessibilidade não é preset de dificuldade;
- colorblind mode não é apenas trocar vermelho por verde;
- screen-reader support depende de APIs de plataforma e precisa ser testado onde existir;
- WCAG pode informar UI, mas game UI também exige regras específicas de dispositivo e gameplay;
- opções devem preservar feedback sobre mudanças.

## Integração

`game-input-engineering`, `game-audio-engineering`, `game-camera-cinematics-engineering`, `design-principles-audit`, `runtime-ui-verification`, `save-game-persistence-engineering` e `xr-game-engineering`.

## Provenance

Consolidada de Unity UI Toolkit/uGUI, Unity Input System e práticas de Game Accessibility Guidelines/Xbox Accessibility Guidelines usadas apenas como referência metodológica. Não trata guidelines como compliance automático.
