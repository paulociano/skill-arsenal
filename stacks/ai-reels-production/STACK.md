---
name: ai-reels-production
description: "Produzir Reels/Shorts com IA do roteiro ou long-form ao corte, reframing 9:16, captions, B-roll, voz/avatar, motion, variantes e QA, carregando apenas os owners necessários."
---

# AI Reels Production

## Objetivo

Orquestrar produção de vídeo curto vertical com IA sem depender de um único gerador e sem confundir automação de edição com previsão de performance.

## Router

Estrutura/hook/roteiro:
- `reels-scripting`
- `content-matrix`

Edição short-form:
- `short-form-video-engineering`

Reframe vertical:
- `vertical-video-reframing`

Presenter/voz/avatar:
- `synthetic-presenter-video`

B-roll e direção de shots:
- `cinematic-visual-direction`

Brand/voz:
- `voice-builder`
- `design-direction`

Revisão e analytics:
- `social-post-review`
- `social-analytics`
- `experiment-design`

## Fluxo

1. **Goal**
   - audience;
   - message;
   - source;
   - platform;
   - duration;
   - CTA;
   - production constraints.

2. **Narrative**
   - hook;
   - setup;
   - proof/example;
   - payoff;
   - CTA.

3. **If long-form**
   - transcript;
   - word timestamps;
   - speaker turns;
   - semantic segments;
   - scene boundaries;
   - clip candidates.

4. **Select**
   - standalone meaning;
   - hook clarity;
   - specificity;
   - proof;
   - visual opportunity;
   - target duration.

5. **Edit**
   - remove dead space;
   - preserve natural cadence;
   - scene-aware cuts;
   - audio cleanup;
   - rough timing.

6. **Vertical composition**
   - track primary subject;
   - smooth crop;
   - safe zones;
   - multi-subject fallback.

7. **Captions**
   - word timing;
   - semantic chunks;
   - visual hierarchy;
   - keyword emphasis;
   - mobile legibility.

8. **Enrichment**
   - original B-roll first when available;
   - generated B-roll for specific beats;
   - charts/callouts;
   - motion graphics;
   - punch-ins only when meaningful.

9. **Synthetic presenter when requested**
   - identity/consent gate;
   - TTS/voice;
   - lip-sync/portrait;
   - provenance/disclosure review.

10. **Sound**
    - dialogue priority;
    - leveling;
    - music ducking;
    - restrained accents.

11. **Variants**
    - first frame;
    - hook wording;
    - caption treatment;
    - pacing;
    - B-roll;
    - CTA.

12. **QA**
    - hook readable immediately;
    - no word/caption clipping;
    - crop stable;
    - face/subject preserved;
    - captions avoid platform chrome;
    - audio understandable on phone;
    - no synthetic identity deception;
    - export aspect/resolution/duration correct.

13. **Learn**
    - after publication, compare actual retention/engagement data;
    - do not infer “viral score” from editorial features alone.

## Local-first execution path

Quando o objetivo for custo baixo e houver máquina local adequada, um runtime self-hosted como OpenShorts pode executar partes do fluxo:
- transcript/word timing;
- moment selection;
- adaptive 9:16 layout;
- burned captions;
- hook overlays;
- optional publishing integrations.

Tratar isso como implementação possível, não dependência do Arsenal. APIs externas, publishing e AI actors continuam sujeitos a suas próprias chaves, custos, consentimento e approval gates.

## Selection rule

Não carregar todos os owners.

Exemplos:
- gravou talking head vertical pronto: `reels-scripting` + `short-form-video-engineering`;
- podcast horizontal: adicionar `vertical-video-reframing`;
- avatar/TTS: adicionar `synthetic-presenter-video`;
- Reel cinematográfico/B-roll IA: adicionar `cinematic-visual-direction`.

## Guardrails

- postagem externa exige autorização e ferramenta disponível;
- rights/licensing apply to source footage, music, models and generated assets;
- cloning voice/face requires permission;
- generated video should not be presented as authentic recording of a real person;
- model weights/installers are never assumed available;
- performance is measured after publishing, not predicted from a score.

## Provenance

Stack construída do lote de 30 repositórios de AI video/Reels de 2026-10-03, com maior peso em WhisperX, PySceneDetect, Auto-Editor, Remotion, MediaPipe, Ultralytics, MuseTalk, LivePortrait, F5-TTS/CosyVoice e Wan/LTX video-generation ecosystems. mutonby/openshorts acrescentou o caminho local-first/self-hosted e layouts adaptativos por cena.

## Pipeline de clipping com escolha explícita de execução

Inspiração metodológica: https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator. Não presumir que MuAPI, yt-dlp, faster-whisper, ffmpeg, OpenCV ou chaves LLM estejam instalados.

1. **Escolha API versus local:** discrimine custo, privacidade, residência dos dados, direitos sobre a fonte, requisitos de hardware e possibilidade de editar/verificar o MP4. Modo local não significa necessariamente offline: ranking por LLM pode chamar serviço remoto.
2. **Transcrição rastreável:** associe transcript e timestamps à versão identificável do vídeo-fonte. Cache somente com identidade/versão da fonte, parâmetros e idioma; nunca reutilize legenda obsoleta silenciosamente.
3. **Vídeos extensos:** faça segmentação com sobreposição delimitada, conservando timestamps globais; dedupe resultados de janelas e candidatos que apontem para o mesmo momento antes da seleção.
4. **Seleção editorial:** armazene para cada candidato início/fim, abertura, contexto necessário, razão editorial e evidência de fala. Use score somente como ranking heurístico interno, jamais como probabilidade calibrada de viralização.
5. **Reenquadramento:** compare detecção de rosto, subject tracking e crop estável; proteja mãos, gestos, demonstrações e falas com múltiplos participantes. Prefira layout adaptativo quando o crop destrói informação.
6. **Saída intercambiável:** mantenha manifest estruturado com referência de fonte, transcript, candidatos, timecodes, decisão de escolha, dimensões, arquivos/URLs, versão de workflow e status de revisão.
7. **QA e custo:** examine começo/fim de cada clipe, sincronização, clipping de áudio, legenda, permissões, duração, plataforma e custo de chamadas; amostre render real antes de produção em lote.
8. **Direitos e dados:** não baixar, redistribuir ou publicar vídeo de terceiros sem autorização aplicável; não enviar transcrição, áudio ou imagem sensíveis a API sem base de permissão.

**Should-trigger:** extrair vários Shorts de um podcast longo ou webinar com deduplicação e manifest. **Near-miss:** escrever roteiro de Reel original sem vídeo-fonte (continuar fluxo usual).

## Recriação de linguagem audiovisual a partir de referência (ReelMimic)

Quando a fonte for um vídeo de referência estética, antes de gerar cenas:
1. Decompor linguagem em duração de shots, ritmo e BPM quando mensurável, tipos de corte, transições, enquadramentos, paleta, movimento de câmera e densidade de informação. Indicar pontos inferidos, não fingir medições.
2. Escrever shot list e storyboard de **conteúdo original**, com style frames e assets próprios; requerer revisão de direção antes de produção em lote quando isso evitar retrabalho material.
3. Produzir cenas com IDs/timecodes; quando houver múltiplos executores disponíveis, separar produção e QA independente. Quando não houver, realizar uma segunda passagem de revisão explícita, sem inventar subagentes.
4. Em correções, comparar frame ou trecho antes/depois, registrar o defeito e comprovar o resultado; fazer revisão em timestamps, não feedback genérico como 'melhore'.
5. Inspecionar flicker, coerência de personagens/cenários, início/fim de corte, áudio, clipping e legibilidade antes do master. Não reaproveitar áudio, pessoas, frames ou assets protegidos da referência sem direitos. Estilo pode inspirar direção, não justifica réplica confundível.

Fonte: https://github.com/edenfunf/reelmimic. O aplicativo exige ferramentas e modelos locais específicos; não faz parte do runtime nativo do ChatGPT.

## Modo anúncio de lançamento de produto (Brag)

Quando a solicitação for um vídeo curto de lançamento de site/app, antes do roteiro localizar **produto real em uso**, sua promessa verificável, público, identidade e 2–3 momentos demonstráveis (entrada → ação central → resultado). Estruturar 15–25 segundos em hook curto, revelação, highlights e fechamento, com texto legível pelo tempo suficiente; evitar métricas, depoimentos e funcionalidades inventadas. Reutilizar screenshots ou assets autorizados e evitar `.env`, segredos, dados reais de clientes e áreas privadas. Planejar áudio/SFX licenciados e verificar frames estáveis e transições antes de renderizar. Se o runtime de vídeo/áudio não estiver conectado, entregar storyboard e copy com limitação declarada, não prometer MP4. `brag`, `brag-slim`, Hyperframes e FFmpeg são opcionais e não estão implícitos na stack. Fonte: https://github.com/latent-spaces/brag (2026-10-17).

## Referência de execução: ai-video-cut

O projeto https://github.com/adrianoz1/ai-video-cut fornece um exemplo de automação por etapas (`yt-dlp` → FFmpeg/audio → transcrição API → JSON/SRT → seleção LLM → legendas/crop 9:16 → clipes). **É implementação externa opcional, não runtime habilitado no ChatGPT.**

Para considerar essa implementação num projeto real:
- confirmar direito de baixar/processar/publicar o vídeo-fonte, inclusive Reels que exigem sessão/cookies;
- preferir chave API por variável de ambiente/secret manager, nunca argumentos de CLI que podem aparecer em histórico/process list;
- observar custo de API, limites de upload e segmentação, retries e versionamento de modelos;
- preservar timecodes globais, deduplicar highlights e usar contract JSON/SRT verificável;
- separar crop 9:16 estático de reframing inteligente: verificar manualmente cenas com pessoas, tela, gestos ou múltiplos sujeitos;
- verificar saída real e dependências (`yt-dlp`, FFmpeg, Python, jq); não executar scripts por simples avaliação;
- tratar palavras como 'viral' no README como heurística editorial não calibrada.

**Should-trigger:** usuário quer montar pipeline local para transformar vídeos autorizados do YouTube em vários Shorts com legendas. **Near-miss:** criação de roteiro de Reel inteiramente novo sem footage original.
