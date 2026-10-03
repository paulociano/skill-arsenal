# Avaliação — 30 repositórios para geração de Reels com IA

Data: 2026-10-03

## Objetivo

Expandir o Skill Arsenal para produção de Reels/Shorts/TikToks com IA, cobrindo transcrição temporizada, seleção de clipes, scene detection, auto-edit, reframing 9:16, captions, motion graphics, TTS, lip-sync, portrait animation e B-roll generativo.

A unidade de adoção foi capability, não repositório.

## Resultado executivo

Criados:
- `short-form-video-engineering`
- `vertical-video-reframing`
- `synthetic-presenter-video`
- stack `ai-reels-production`

Atualizados:
- `reels-scripting` com seleção semântica de clips;
- `cinematic-visual-direction` com generative B-roll;
- `ARSENAL INDEX.md`.

## Triage dos 30 repositórios

### A. ASR, timing e diarização

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 1 | m-bain/whisperX | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 2 | SYSTRAN/faster-whisper | A/D | ABSORB_METHOD_ONLY |
| 3 | ggml-org/whisper.cpp | A/D | KEEP_EXTERNAL_REFERENCE |
| 4 | openai/whisper | A/D | KEEP_EXTERNAL_REFERENCE |
| 5 | pyannote/pyannote-audio | A/D | ABSORB_METHOD_ONLY |

Capabilities adotadas:
- word-level timestamps;
- forced alignment;
- VAD;
- diarization;
- long-form context;
- transcript as timing backbone.

Owner: `short-form-video-engineering`.

### B. Scene detection, auto-edit e composição

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 6 | Breakthrough/PySceneDetect | A/D | ABSORB_METHOD_ONLY |
| 7 | WyattBlue/auto-editor | A/D | ABSORB_METHOD_ONLY |
| 8 | Zulko/moviepy | D | KEEP_EXTERNAL_REFERENCE |
| 9 | kkroening/ffmpeg-python | D | KEEP_EXTERNAL_REFERENCE |
| 10 | remotion-dev/remotion | A/D | ABSORB_METHOD_ONLY |
| 11 | motion-canvas/motion-canvas | A/D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- content-aware scene boundaries;
- silence/motion activity;
- dead-space removal;
- temporal padding;
- programmatic video composition;
- captions, transitions and overlays;
- reusable design systems for video.

Owner: `short-form-video-engineering`.

Remotion also reinforced `cinematic-visual-direction`, but a renderer-specific owner was not created.

### C. Auto-reframe, tracking e visual focus

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 12 | google-ai-edge/mediapipe | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 13 | ultralytics/ultralytics | A/D | ABSORB_METHOD_ONLY |
| 14 | opencv/opencv | A/D | KEEP_EXTERNAL_REFERENCE |
| 15 | deepinsight/insightface | A/D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- person/face/object detection;
- tracking across frames;
- virtual-camera crop;
- temporal smoothing;
- multi-subject policy;
- safe framing.

Owner: `vertical-video-reframing`.

A principal adaptação veio do conceito AutoFlip/MediaPipe: subject salience e tracking ajudam o crop, mas a composição final precisa de smoothing e rules de enquadramento.

### D. Lip-sync, portrait animation e presenter sintético

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 16 | Rudrabha/Wav2Lip | A/D | ABSORB_METHOD_ONLY |
| 17 | TMElyralab/MuseTalk | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 18 | KlingAIResearch/LivePortrait | A/D | ABSORB_METHOD_ONLY |

Capabilities adotadas:
- lip-sync;
- mouth-region temporal consistency;
- portrait retargeting;
- pose/expression control;
- identity consistency;
- artifact QA.

Owner: `synthetic-presenter-video`.

### E. TTS e voice generation

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 19 | myshell-ai/OpenVoice | A/D | ABSORB_METHOD_ONLY |
| 20 | SWivid/F5-TTS | A/D | ABSORB_METHOD_ONLY |
| 21 | fishaudio/fish-speech | A/D | KEEP_EXTERNAL_REFERENCE |
| 22 | QwenAudio/CosyVoice | A/D | ABSORB_METHOD_ONLY |
| 23 | hexgrad/kokoro | A/D | KEEP_EXTERNAL_REFERENCE |
| 24 | resemble-ai/chatterbox | A/D | KEEP_EXTERNAL_REFERENCE |
| 25 | myshell-ai/MeloTTS | A/D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- TTS;
- multi-speaker/style;
- pronunciation/pacing;
- authorized voice reference;
- voice consistency;
- consent/provenance gate.

Owner: `synthetic-presenter-video`.

No model/provider is assumed available in runtime.

### F. Generative video / B-roll

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 26 | zai-org/CogVideo | A/D | KEEP_EXTERNAL_REFERENCE |
| 27 | Wan-Video/Wan2.1 | A/D | UPDATE_EXISTING / ABSORB_METHOD_ONLY |
| 28 | Lightricks/LTX-Video | A/D | UPDATE_EXISTING / ABSORB_METHOD_ONLY |
| 29 | Tencent-Hunyuan/HunyuanVideo | A/D | KEEP_EXTERNAL_REFERENCE |
| 30 | Stability-AI/generative-models | A/D | KEEP_EXTERNAL_REFERENCE |

Capabilities adotadas:
- text-to-video;
- image-to-video;
- video editing;
- keyframe/multi-keyframe control;
- short independent generated shots;
- generation as B-roll layer, not default full-Reel replacement.

Owner: `cinematic-visual-direction`.

## 1. Short-Form Video Engineering

### Lacuna

`reels-scripting` cuidava de narrativa, mas não da execução audiovisual.

### Decisão

Criar `short-form-video-engineering` com:
- transcript + timing;
- segmentation;
- clip selection;
- dead-space edit;
- captions;
- enrichment;
- audio;
- variants;
- mobile QA.

Regra central:

`transcript semantics + scene boundaries + speaker/activity timing`

é melhor que cortar por um único sinal.

## 2. Vertical Video Reframing

### Lacuna

Nenhum owner cuidava de conversão temporalmente estável de 16:9 para 9:16.

### Decisão

Criar `vertical-video-reframing`.

A skill separa:
- detection;
- tracking;
- composition;
- crop window;
- smoothing;
- multi-subject behavior;
- fallback.

Bounding box frame a frame foi rejeitada como câmera final por gerar jitter.

## 3. Synthetic Presenter Video

### Lacuna

TTS, lip-sync e portrait animation têm risco e QA próprios e não pertencem apenas a direction/copy.

### Decisão

Criar `synthetic-presenter-video`.

O owner exige:
- identity/consent gate;
- source provenance;
- voice QA;
- lip-sync QA;
- portrait animation QA;
- disclosure/integrity review.

## 4. Reels Scripting

UPDATE_EXISTING.

Adicionado:
- semantic clip candidates para fontes longas;
- mini edit brief por candidato;
- first-frame text;
- removable sections;
- B-roll opportunities;
- CTA compatibility.

Continua proibido tratar score editorial como previsão de viralidade.

## 5. Cinematic Visual Direction

UPDATE_EXISTING.

Adicionado generative B-roll:
- gerar por beat específico;
- shot contract;
- escolher T2V/I2V/keyframe/V2V pela necessidade;
- clips curtos;
- output QA;
- fallback quando geração falha.

## Stack

Criada `ai-reels-production`:

`goal → narrative → transcript/segments → clip selection → edit → 9:16 reframe → captions → enrichment → synthetic presenter if requested → audio → variants → QA → learn from real metrics`

## Segurança e portabilidade

Verdict geral: **CAUTION**.

Nenhum model weight, installer, CUDA package, FFmpeg binary, Docker image ou inference server foi executado.

Superfícies relevantes:
- GPU/CUDA/runtime downloads;
- model weights;
- Hugging Face tokens;
- biometric/face data;
- voice samples;
- voice/face cloning;
- public-figure impersonation risk;
- video/media licensing;
- commercial model licenses;
- generated synthetic media.

Adaptação:
- methodology only;
- no runtime presumed;
- explicit consent for real-person voice/face use;
- no fabricated authentic-looking statement presented as genuine recording;
- model/version/license grounding before implementation;
- publication remains an external action requiring authorization.

## Materialização

Criados:
- `skills/short-form-video-engineering/SKILL.md`
- `skills/vertical-video-reframing/SKILL.md`
- `skills/synthetic-presenter-video/SKILL.md`
- `stacks/ai-reels-production/STACK.md`

Atualizados:
- `skills/reels-scripting/SKILL.md`
- `skills/cinematic-visual-direction/SKILL.md`
- `ARSENAL INDEX.md`

## Limites

- O lote avaliou capacidade e documentação, não executou os pipelines.
- Requisitos de GPU e qualidade mudam por modelo.
- Model licenses differ and must be checked for commercial use.
- Nenhum método de “viral score” foi adotado.
- Performance de Reel continua sendo medida pós-publicação com dados reais.
