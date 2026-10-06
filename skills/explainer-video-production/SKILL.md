---
name: explainer-video-production
description: "Produzir vídeos explicativos narrados sincronizando roteiro, voz e mudanças visuais por beats ou palavras, com inspeção de frames, legibilidade, áudio e render verificáveis."
---

# Explainer Video Production

## Objetivo
Produzir vídeos explicativos em que a narração define o relógio e o visual responde a beats verificáveis, preservando factualidade, legibilidade, sincronização e revisão antes do render final.

## Quando usar
- vídeo educativo ou técnico narrado;
- product demo explicativo;
- motion explainer com cenas/diagramas;
- vídeo em que texto, ícones ou UI precisam aparecer no momento exato da fala.

Para Reel puramente short-form use `ai-reels-production`. Para direção de shots use `cinematic-visual-direction`. Para edição de footage use `video-editing-pipeline`.

## Workflow
1. Ground facts: pesquisar somente o necessário; não inventar números, features ou claims.
2. Narration first: escrever roteiro para o ouvido, com cenas curtas e uma ideia por beat.
3. Voice/timing: obter voz e medir duração real e, quando possível, timestamps por palavra.
4. Visual plan: mapear mudanças para palavra, marker ou beat explícito.
5. Scene build: manter poucos elementos, texto curto e continuidade espacial.
6. Inspect: gerar stills/contact sheets e revisar clipping, sobreposição, vazios e progressão.
7. Small-player check: testar legibilidade em escala reduzida e safe areas.
8. Render/verify: verificar loudness, silêncio anômalo, black frames, inteligibilidade e sincronização.
9. Delivery: reportar duração, artefato, checks e limites.

## Princípios
- A narração determina o relógio; o visual responde ao relógio.
- Mudança visual acompanha significado, não preenche tempo.
- Product demos usam labels/features reais; dados fictícios precisam parecer exemplos.
- Imagens geradas exigem inspeção própria; texto deve permanecer editável quando possível.

## Integração
`cinematic-visual-direction`, `short-form-video-engineering`, `synthetic-presenter-video`, `character-continuity`, `verify-before-claim`.

## Provenance
Adaptada de https://github.com/vincentsch/explainroo, preservando narration-first timing, word/marker synchronization, still/contact-sheet review e audiovisual verification sem exigir Kokoro, Whisper, Chrome, FFmpeg ou o runtime original.
