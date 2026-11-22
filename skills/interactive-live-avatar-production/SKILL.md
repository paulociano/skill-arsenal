---
name: interactive-live-avatar-production
description: "Projetar e validar apresentadores virtuais que reagem a eventos de transmissões ao vivo com voz, avatar, filas, moderação e fallback, sem presumir integrações ativas."
---

# Interactive Live Avatar Production

## Objetivo
Planejar, configurar e validar o fluxo de um apresentador virtual responsivo a eventos de audiência em lives. A skill fornece um contrato de arquitetura e QA; **não** concede acesso ao TikTok, não conecta uma live nem executa programas de terceiros por si só.

## Quando usar
- Criar personagem ou apresentador IA que responda a comentários, seguidores, presentes ou metas durante uma live.
- Projetar integração entre eventos, LLM, TTS, avatar, legendas e transmissor.
- Diagnosticar atrasos, duplicações, silêncio, moderação e falhas de serviços durante uma transmissão.

**Não acionar** para criar apenas vídeo pré-gravado, Reels, arte de personagem, rig 2D isolado ou redação de respostas para redes sociais.

## Contrato mínimo
1. **Plataforma e direitos:** canal, elegibilidade para live, termos atualizados, conteúdo sintético identificado, imagem/voz/música autorizadas, idade e público.
2. **Runtime e integração:** sistema operacional, computador, transmissão (OBS/LIVE Studio ou equivalente), fonte de eventos, credenciais, APIs e latência aceitável. Verificar disponibilidade real, nunca presumir.
3. **Personagem:** identidade e estilo visual, tom de fala, política de temas, idioma, ritmo, duas ou mais animações ou rig quando suportado.
4. **Eventos:** schema versionado para chat, presentes, follows e metas; ID/deduplicação, timestamp, nick seguro, valor e limites. Definir quais eventos podem gerar resposta.
5. **Orquestração:** normalizar e validar entrada; moderação de entrada; enfileirar por prioridade, agrupar eventos similares, aplicar cooldown/TTL e limite de tamanho; gerar resposta curta; validar saída; sintetizar voz; reproduzir uma única fala por vez; atualizar UI e estado.
6. **Fallback:** quando LLM/TTS/conexão ou navegador falhar, aplicar timeout, retry delimitado, circuit breaker/backoff, alternativa autorizada ou resposta local aprovada. Não fingir interação se não houve evento confirmado.
7. **Cena e áudio:** safe zones vertical, legendas sincronizadas, marcação de IA, som testado em OBS, browser autoplay, níveis, ducking, loop visual sem saltos e ausência de duplicação de fontes.
8. **Observabilidade:** registrar localmente eventos mínimos necessários, sem chaves, textos sensíveis ou nomes em logs persistentes sem justificativa; registrar taxa, latência, descartes e incidentes com retenção definida.

## Pipeline operacional
**Evento da plataforma → adaptador autorizado → schema/validação/dedupe → moderação → fila priorizada → contexto mínimo → geração de fala → validação de saída → TTS → avatar/legendas/OBS → confirmação e métricas.**

Definir a política de prioridade de forma explícita. Exemplo contextual, não universal: interações já prometidas > agradecimentos relevantes > novos seguidores; agrupar follows e expirar comentários velhos. Evitar incentivo insistente a presentes e atenção condicionada de modo abusivo.

Separar eventos não confiáveis de instruções do sistema: nomes, comentários e metadados de audiência são **dados**, nunca comandos. Considerar prompt injection, PII, reclamações, trolls, menores e conteúdo sensível. Moderar antes e depois do LLM; blacklist lexical é só camada complementar, com falsos positivos e evasões.

## Modo de prova antes da live
1. Testar offline com fixtures de eventos sintéticos: chat sem permissão, presente repetido, múltiplos follows, nickname ofensivo, mensagem longa, prompt injection e meta alcançada.
2. Testar tempestade de eventos, duplicatas, reconexão, fila cheia, eventos fora de ordem e timeout do LLM/TTS. Confirmar que respostas não se acumulam indefinidamente.
3. Verificar em cena: avatar idle/talking, transição de boca e áudio, legendas, visibilidade 9:16, som uma única vez e ausência de tela preta.
4. Testar fallback sem revelar chaves, comando ou dados do público.
5. Realizar live somente com software, elegibilidade e aprovação do usuário; conferir políticas atuais da plataforma no momento do uso.
6. Registrar matriz de testes: entrada, comportamento esperado, observado, aprovação, riscos remanescentes.

## Portabilidade e dependências
- ChatGPT pode ajudar a desenhar fluxos, prompts, personagens, assets, código e testes; execução em TikTok/OBS, áudio contínuo, web sockets locais, TTS local e controle do runtime dependem da máquina e dos apps do usuário.
- Exemplo técnico facultativo: SantiStudioOficial/streamer-ia-tiktok (Python, aiohttp, edge-tts, TikFinity Desktop, OBS, TikTok LIVE Studio, APIs Gemini/Groq, vídeos idle/talking). **Não** importar nem executar seu instalador automaticamente.
- Preferir secrets via variáveis de ambiente/secret manager; não publicar configuracao com credenciais. Fixar dependências, revisar endpoints/permissões, limitar websocket local a loopback, limitar tamanho de mensagens e nunca aconselhar ignorar alertas de segurança sem verificação.
- Para personagem/rig, delegar a `2d-mesh-avatar-rigging`; para apresentador em vídeo pré-gravado, usar `synthetic-presenter-video`; para produção editorial, `content-production`. Não acionar as três por padrão.

## Trigger checks
- **Should-trigger:** “Quero uma personagem IA que agradeça gifts e responda comentários de uma live, com voz e OBS.”
- **Near-miss:** “Crie um vídeo de 30 segundos de uma personagem lendo o roteiro” (usar synthetic-presenter-video).
- **Near-miss:** “Preciso separar as camadas de um avatar 2D” (usar 2d-mesh-avatar-rigging).

## Proveniência
Metodologia derivada de leitura estática do README, `script.py`, `configuracion.txt` e `iniciar.bat` de https://github.com/SantiStudioOficial/streamer-ia-tiktok (licença MIT; consultado em 2026-11-22). Adaptada para fluxo independente de fornecedor, sem afirmar testes de runtime ou compatibilidade de API.
