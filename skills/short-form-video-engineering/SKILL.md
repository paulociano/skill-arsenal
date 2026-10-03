---
name: short-form-video-engineering
description: "Projetar e automatizar Reels/Shorts/TikToks a partir de vídeo, áudio ou roteiro usando transcrição temporizada, scene detection, seleção de clipes, cortes, captions, ritmo, overlays e QA sem tratar score editorial como previsão de viralidade."
---

# Short-Form Video Engineering

## Objetivo

Transformar uma fonte longa ou roteiro em vídeo curto vertical com narrativa clara, timing preciso e edição reproduzível.

## Quando usar

- Reels;
- Shorts;
- TikTok;
- recortes de podcast/entrevista;
- talking head;
- automatic clipping;
- captions animadas;
- cortes por silêncio/cena;
- produção de variantes.

## Princípio central

**Corte bom preserva sentido, ritmo e continuidade; não apenas duração.**

## Pipeline

1. **Source contract**
   - formato/orientação;
   - duração;
   - idioma;
   - speakers;
   - objetivo do Reel;
   - target length;
   - CTA;
   - brand/voice.

2. **Transcript**
   - speech-to-text;
   - word-level timestamps quando disponíveis;
   - speaker diarization quando necessário;
   - manter transcript bruto e versão limpa separadas.

3. **Segmentation**
   - sentence/semantic boundaries;
   - scene boundaries;
   - silence/activity regions;
   - speaker turns;
   - candidate visual discontinuities.

4. **Clip candidates**
   Cada candidato precisa:
   - começar com contexto suficiente;
   - conter ideia relativamente autônoma;
   - terminar em payoff/conclusão/abertura deliberada;
   - caber na duração;
   - evitar cortar palavra, gesto ou raciocínio ao meio.

5. **Selection**
   Avaliar:
   - hook clarity;
   - standalone meaning;
   - novelty/specificity;
   - proof/example density;
   - emotional or informational tension;
   - visual opportunity;
   - CTA compatibility.

   Não transformar isso em previsão de alcance.

6. **First-pass edit**
   - remover dead space;
   - preservar respiração/padding natural;
   - evitar jump cuts excessivamente nervosos;
   - usar scene boundary quando melhora continuidade;
   - speed-up apenas quando inteligibilidade permanece.

7. **Captions**
   - partir de timing por palavra;
   - agrupar por unidades semânticas;
   - manter linhas curtas;
   - destacar poucas palavras-chave;
   - safe areas para UI da plataforma;
   - contraste e legibilidade;
   - caption timing nunca deve antecipar significativamente a fala.

8. **Visual enrichment**
   - B-roll;
   - callouts;
   - charts;
   - images;
   - zoom/punch-in;
   - motion graphics;
   - usar apenas quando reforçam a fala.

9. **Audio**
   - dialogue intelligibility first;
   - loudness consistente;
   - music ducking;
   - remove noise only if voice quality does not degrade;
   - sound accents sparingly.

10. **Variants**
    - hook;
    - first-frame text;
    - caption style;
    - CTA;
    - B-roll intensity;
    - pacing.

11. **QA**
    - first 1–2 seconds understandable;
    - no clipped words;
    - captions sync;
    - subject remains visible;
    - text does not collide with platform UI;
    - audio intelligible on phone speaker;
    - no unsupported claims;
    - duration/export correct.

## Clip extraction from long-form

Prefer:
`transcript semantics + scene boundaries + speaker/activity timing`

instead of one signal alone.

Scene detection is evidence of visual structure, not proof of semantic boundary. Silence is evidence of pause, not proof of edit point.

## Regras

- não prometer viralidade;
- não classificar clip como “viral” sem dados comparativos reais;
- não remover pausas a ponto de tornar fala artificial;
- subtitles are derived from audio and must be rechecked after edit;
- source rights/permissions remain required;
- synthetic inserts must be disclosed when context or policy requires.

## Integração

`reels-scripting`, `vertical-video-reframing`, `synthetic-presenter-video`, `cinematic-visual-direction`, `social-post-review`, `social-analytics`, `experiment-design`.

## Provenance

Consolidada de WhisperX, faster-whisper/Whisper, PySceneDetect, Auto-Editor, MoviePy, FFmpeg wrappers e Remotion. O Arsenal absorve timing, segmentation, edit contracts e compositing sem presumir esses runtimes instalados.
