---
name: realtime-voice-agent-engineering
description: "Projetar e avaliar agentes de voz em tempo real por pipeline de áudio, turn-taking, interrupções, latência, ferramentas, estado conversacional, fallback e observabilidade sem assumir provider ou runtime específico."
---

# Realtime Voice Agent Engineering

## Objetivo

Projetar agentes conversacionais de voz que funcionem em tempo real como sistemas de streaming, não como chatbots que ocasionalmente recebem áudio.

## Quando usar

Use para:
- atendimento e suporte por voz;
- recepção, triagem ou intake;
- copilotos em chamadas;
- role-play e treinamento;
- meeting assistants;
- experiências multimodais com áudio/vídeo;
- agentes que chamam ferramentas durante uma conversa ao vivo.

Para voz sintética em vídeo use `synthetic-presenter-video`. Para gravações offline use pipelines de áudio/vídeo apropriados.

## Modelo

Uma arquitetura típica pode ser:

`transport → audio input → VAD/turn detection → STT ou realtime model → reasoning/tools → TTS/audio output → transport`

Nem todo sistema usa todos os blocos. Modelos speech-to-speech podem colapsar etapas, mas as responsabilidades continuam existindo.

## Workflow

1. **Define the conversation contract**
   - objetivo;
   - usuário;
   - canal;
   - idioma;
   - duração esperada;
   - ferramentas;
   - dados sensíveis;
   - ações permitidas;
   - critérios de handoff humano.

2. **Choose speech architecture**
   Compare:
   - STT → LLM → TTS;
   - realtime speech-to-speech;
   - arquitetura híbrida.

   Decidir por qualidade, latência, controle, observabilidade, custo e requisitos de compliance.

3. **Transport**
   Definir WebRTC, WebSocket, telefonia ou transporte equivalente.
   Medir latência end-to-end, não apenas tempo do modelo.

4. **Turn-taking**
   Projetar:
   - voice activity detection;
   - endpointing;
   - silêncio;
   - backchannel;
   - barge-in/interrupção;
   - cancelamento do áudio de saída.

   Um agente que continua falando sobre o usuário falhou mesmo que a resposta textual seja correta.

5. **Streaming pipeline**
   Trabalhar com frames/chunks e backpressure.
   Não bloquear o pipeline inteiro em uma etapa lenta sem política explícita.

6. **State and context**
   Separar:
   - transcript;
   - state machine/flow;
   - tool state;
   - memória durável;
   - facts temporários da chamada.

   Transcript completo não precisa entrar em toda inferência.

7. **Tools and external actions**
   Aplicar `agent-action-governance` quando houver efeitos externos.
   Durante fala/tool call:
   - deixar o estado perceptível;
   - evitar double-submit;
   - lidar com timeout;
   - confirmar ações consequenciais quando necessário.

8. **Structured conversations**
   Para fluxos regulados ou transacionais, combinar liberdade conversacional com estados explícitos:
   - current step;
   - required fields;
   - allowed transitions;
   - recovery;
   - completion criteria.

9. **Fallback and degradation**
   Preparar:
   - STT incerto;
   - ruído;
   - TTS failure;
   - model timeout;
   - tool failure;
   - network jitter;
   - reconnect;
   - handoff para humano/texto.

10. **Observability**
   Medir:
   - time-to-first-audio;
   - turn latency;
   - interruption success;
   - transcription error patterns;
   - tool latency/failure;
   - dropped audio;
   - task completion;
   - handoffs;
   - cost por sessão.

11. **Evaluation**
   Testar com áudio realista:
   - sotaques e idiomas relevantes;
   - ruído;
   - fala rápida/lenta;
   - interrupções;
   - silêncio;
   - nomes/números;
   - chamadas longas;
   - edge cases do domínio.

   Avaliar áudio, trajetória e resultado, não apenas transcript final.

## Segurança e privacidade

- voz pode conter PII e dados biométricos;
- definir consentimento, retenção e gravação;
- mascarar secrets em traces/transcripts;
- separar autorização de speaker recognition;
- não tratar voz semelhante como autenticação;
- ações financeiras, legais ou irreversíveis precisam de controles adicionais;
- provider externo pode alterar data residency e retenção.

## Guardrails

- baixa latência não compensa ação incorreta;
- VAD é heurística, não intenção do usuário;
- transcript parcial não deve disparar ação irreversível;
- retries não podem duplicar tool effects;
- voz sintetizada não deve ser usada para personificar pessoa real sem autorização;
- multi-agent por voz só vale quando papéis e handoffs reduzem complexidade real.

## Integração

Combina com:
- `agent-action-governance`;
- `llm-observability-evaluation`;
- `multi-agent-orchestration`;
- `durable-workflow-engineering`;
- `structured-output-contract`;
- `synthetic-presenter-video`.

## Provenance

Consolidada principalmente de `pipecat-ai/pipecat` e `pydantic/pydantic-ai`. Preserva pipelines de streaming, transports, turn-taking, flows/state, tool use, realtime speech e observabilidade, sem exigir Pipecat, Pydantic AI, WebRTC específico ou providers particulares.

## Voz full-duplex e modelos expressivos

Quando o requisito exigir fala expressiva, turn-taking nativo e interrupções, comparar arquiteturas streaming STT→LLM→TTS, speech-to-speech e híbrida; usar [adventists-ai/sophon-realtime](https://github.com/adventists-ai/sophon-realtime) apenas como **referência de implementação externa**, não como provider ativado por padrão.

- Medir do microfone até o primeiro áudio reproduzido, qualidade dos turnos, barge-in, backchannel e consistência entre **o que foi ouvido** e o histórico retido após interrupção. Rascunhos antecipados não podem produzir ações externas ou áudio irreversível antes da confirmação da intenção.
- Separar fala textual, marcas de expressividade e comandos para ferramentas. Tags como riso/suspiro só se tornam áudio por pipeline compatível; não devem aparecer literalmente na resposta.
- Ao avaliar voice cloning, exigir autorização demonstrável para a voz, controles contra personificação e política de retenção para clips de referência.
- Compatibilidade declarada com protocolo Realtime/OpenAI não garante equivalência de comportamento, autenticação, latência ou qualidade. Testar com o endpoint e versão reais.
- Requisitos de GPU/VRAM, downloads de weights e resultados de benchmark publicados pelo projeto são claims do fornecedor até replicação. Sem GPU compatível ou API conectada, desenhar o sistema, não afirmar que roda localmente.

Should-trigger: projeto de agente de suporte em voz full-duplex com interrupções e emoções. Near-miss: transcrição offline simples. Prova: corpus de áudio de teste com sotaques, silêncio, ruído, interrupções e métricas end-to-end.
