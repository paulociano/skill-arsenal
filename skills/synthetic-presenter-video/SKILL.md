---
name: synthetic-presenter-video
description: "Criar ou avaliar vídeos com voz sintética, voice cloning, talking-head/lip-sync e portrait animation com consentimento, identity boundaries, timing, expression, artifact QA e provenance explícita."
---

# Synthetic Presenter Video

## Objetivo

Produzir apresentação sintética controlável sem perder sincronização, identidade, consentimento ou transparência.

## Quando usar

- TTS presenter;
- voice cloning;
- lip-sync;
- talking head;
- animated portrait;
- avatar video;
- dubbing;
- multilingual presenter.

## Workflow

1. **Identity/consent gate**
   - confirmar direitos/consentimento para voz/rosto;
   - identificar se é pessoa real, personagem ou synthetic identity;
   - não assumir autorização por disponibilidade pública do material.

2. **Script**
   - pronunciation notes;
   - pacing;
   - pauses;
   - emotion/register;
   - language.

3. **Voice**
   - TTS or authorized voice reference;
   - loudness;
   - breathing/pauses;
   - pronunciation;
   - consistent speaker identity;
   - keep original/reference provenance.

4. **Portrait/talking head**
   - source image/video quality;
   - frontal/usable face;
   - expression/pose range;
   - background/occlusions.

5. **Lip-sync**
   - audio/video alignment;
   - phoneme timing;
   - mouth region stability;
   - teeth/tongue artifacts;
   - facial boundary consistency.

6. **Portrait animation**
   - pose;
   - expression;
   - eye/blink;
   - head motion;
   - retargeting intensity;
   - avoid uncanny over-animation.

7. **Compositing**
   - crop;
   - background;
   - captions;
   - B-roll;
   - lighting/color consistency.

8. **QA**
   - identity consistency;
   - sync drift;
   - pronunciation;
   - expression appropriateness;
   - frame artifacts;
   - disclosure/provenance needs.

## Safety and integrity

- do not impersonate a person without permission;
- do not fabricate statements and present them as authentic recordings;
- preserve source/consent records when workflow supports it;
- generated voice/video should not be used to deceive viewers about origin;
- cloning a public figure is not automatically authorized;
- sensitive or consequential contexts require stronger disclosure and review.

## Regras

- lip-sync quality and portrait animation are separate problems;
- good audio does not fix uncanny face motion;
- cloning similarity is not proof of consent;
- model/provider capabilities and licenses must be checked at runtime;
- do not promise exact identity preservation without output inspection.

## Integração

`short-form-video-engineering`, `cinematic-visual-direction`, `voice-builder`, `character-continuity`.

## Provenance

Consolidada de Wav2Lip, MuseTalk, LivePortrait, OpenVoice, F5-TTS, Fish Speech, CosyVoice and related TTS runtimes. Methodology only; no model weights or runtime are assumed available.
