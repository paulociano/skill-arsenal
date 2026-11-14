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

## Vídeo longo com fala: continuidade por segmentos (InfiniteTalk)

Para talking-head, avatar ou personagem que fala por períodos extensos, planejar **segmentos encadeados**, em vez de considerar duração ilimitada como garantia de continuidade perfeita.

1. Separar áudio-fonte autorizado e transcrição/timestamps de identidade, imagem/vídeo de referência, configuração de movimento, duração e idioma. Registrar versão de todas as fontes.
2. Para cada segmento, conservar fotogramas/estado de movimento adequados à continuidade e auditar junções (posição facial, escala, boca, olhos, luz, cor, fundo, áudio, prosódia).
3. Medir drift de identidade e cor ao longo da duração, sobretudo após muitos segmentos. O projeto InfiniteTalk relata diferenças entre image-to-video e video-to-video: I2V pode acumular mudança de cor depois de cerca de um minuto; V2V é a rota declarada para sequências mais longas, mas não garante câmera idêntica.
4. Testar amostra curta antes de renderizar vídeo extenso; comparar sincronização labial, estabilização facial, fluidez, costuras e erro acumulado. Fallback: cortes editoriais, reancoragem por referência, B-roll e trechos curtos.
5. Escolher entre API disponível e runtime local conforme qualidade, VRAM, custo e direitos sobre pesos/modelos. Quantização, offload, TeaCache e LoRA são mecanismos específicos de implementação: nunca prometer que estão disponíveis no ChatGPT ou que eliminam requisitos de GPU.
6. Preservar consentimento de identidade e voz, proveniência e sinalização adequada para conteúdo sintético, especialmente quando puder ser confundido com fala autêntica de uma pessoa.

**Should-trigger:** gerar avatar falante por vários minutos com continuidade. **Near-miss:** legenda de um Reel gravado, sem sintetizar fala ou rosto.

**Fonte metodológica:** https://github.com/MeiGen-AI/InfiniteTalk (README de uso e modos de inferência, 2026-11-14). Não foram importados modelos, scripts ou pesos.
