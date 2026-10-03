---
name: vertical-video-reframing
description: "Converter e validar vídeos horizontais/quadrados para 9:16 usando subject detection/tracking, safe crop, smoothing, multi-subject policy e composition-aware reframing sem câmera virtual nervosa."
---

# Vertical Video Reframing

## Objetivo

Converter conteúdo para formato vertical preservando o sujeito e a composição ao longo do tempo.

## Quando usar

- 16:9 → 9:16;
- auto-reframe;
- face tracking crop;
- speaker tracking;
- multi-person podcast;
- repurpose para Reels/Shorts/TikTok.

## Workflow

1. **Target**
   - output aspect ratio;
   - resolution;
   - UI safe areas;
   - caption/overlay zones.

2. **Detect**
   - face/person/object;
   - confidence;
   - primary subject;
   - secondary subject.

3. **Track**
   - identity continuity;
   - position over time;
   - occlusion/re-entry;
   - speaker/activity signal when useful.

4. **Composition**
   - headroom;
   - gaze/lead room;
   - torso framing;
   - relevant object;
   - text/slide visibility.

5. **Crop window**
   - constrain to source bounds;
   - minimum subject coverage;
   - prevent abrupt zoom;
   - preserve resolution where possible.

6. **Smoothing**
   - low-pass/interpolation/hysteresis;
   - dead zone before moving virtual camera;
   - cap velocity/acceleration;
   - avoid frame-by-frame bounding-box chase.

7. **Multiple subjects**
   - wide crop if both matter;
   - active-speaker switching only with transition hysteresis;
   - split layout when crop cannot preserve both;
   - do not oscillate on rapid speaker alternation.

8. **Fallback**
   - center crop;
   - manual keyframe;
   - letterbox/background extension;
   - static composition when confidence is low.

9. **QA**
   - scrub whole clip;
   - face/head not cut;
   - gestures/props preserved;
   - camera motion comfortable;
   - no jitter at occlusion;
   - captions remain inside safe region.

## Regras

- tracking accuracy does not equal good composition;
- face center is not always visual center;
- virtual-camera movement needs temporal smoothing;
- active speaker is a cue, not an automatic crop command;
- do not upscale beyond useful source resolution without declaring it.

## Integração

`short-form-video-engineering`, `cinematic-visual-direction`, `computer-use-agent-engineering`.

## Provenance

Consolidada de MediaPipe/AutoFlip concepts, Ultralytics tracking, OpenCV and face-detection pipelines. Não presume specific detector/model installed.
