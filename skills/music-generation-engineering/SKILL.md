---
name: music-generation-engineering
description: "Projetar workflows de música generativa por IA com blueprint musical, letra, BPM/key/meter, referência, variações, stems, edição localizada e QA sem depender de um modelo específico."
---

# Music Generation Engineering

## Objetivo
Transformar intenção criativa em música generativa controlável e revisável, separando planejamento musical, síntese, edição e avaliação.

## Workflow
1. Creative contract: finalidade, duração, gênero/mood, vocal/instrumental, idioma, referências e direitos.
2. Song blueprint: seções, energia, instrumentação e evolução.
3. Musical metadata: BPM, key/scale, meter, duração e constraints quando controláveis.
4. Lyrics: escrever para canto, considerando prosódia, repetição, fonética, métrica e estrutura.
5. Generation strategy: text-to-music, reference-guided, cover, completion, repaint, layer/stem ou vocal-to-BGM.
6. Variants: mudar poucas dimensões por vez.
7. Editing: preferir regeneração localizada quando o problema é local.
8. QA: continuidade, clipping/headroom, inteligibilidade, tempo/tonalidade, artefatos, repetição e estrutura.
9. Delivery: master e, quando disponíveis, instrumental/stems/lyric timestamps + settings/provenance.

## Planner antes do sintetizador
Preferir intent → blueprint → musical metadata/lyrics → synthesis para trabalhos estruturados.

## Personalização
Fine-tuning/LoRA só deve ser promovido com dados/direitos adequados, holdout separado e ganho comprovado contra baseline. Número de faixas, tempo e VRAM são propriedades do backend.

## Direitos e limites
- referências orientam características gerais autorizadas; não prometer cópia exata da identidade sonora de artista vivo ou obra protegida;
- covers/remixes exigem direitos adequados para distribuição;
- não afirmar backend, weights ou GPU disponíveis sem grounding.

## Provenance
Adaptada principalmente de https://github.com/ACE-Step/ACE-Step-1.5, preservando planner→synthesis, controles musicais, reference audio, editing/repaint, stems/layers e personalização avaliada sem exigir ACE-Step, seus pesos, Gradio, CUDA ou hardware específico.
