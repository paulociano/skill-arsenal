# Avaliação: SantiStudioOficial/streamer-ia-tiktok

- **Data:** 2026-11-22
- **Origem:** https://github.com/SantiStudioOficial/streamer-ia-tiktok
- **Arquivos examinados:** README.md, script.py, configuracion.txt, iniciar.bat, metadata/licença MIT.
- **Método:** evaluate-and-import-skill, skill-security-review, skill-builder e verify-before-claim; inspeção estática, sem execução de código ou instalador.
- **Categoria:** **D — skill técnica**; valor metodológico concreto e runtime externo obrigatório.
- **Decisão:** **ADOPT_ADAPTED**: extrair workflow de apresentador virtual para lives em `skills/interactive-live-avatar-production/SKILL.md`. Não instalar/copiar o software original nem garantir live em ambiente ChatGPT.

## O que realmente implementa
Python + aiohttp lê eventos gift/chat/follow de TikFinity Desktop em websocket local; normaliza e filtra usernames/comentários; agrega gifts e seguidores; controla respostas a comentários de quem enviou presente; monta prompts de persona; alterna modelos de texto em APIs externas com pausa por erro/limite; sintetiza voz por edge-tts; entrega eventos para visor HTML via WebSocket em loopback; usa vídeos de repouso e fala, legendas e metas na cena OBS/LIVE Studio. O README também contém roteiro e prompts para produzir o personagem.

## Incremento e overlap
- `2d-mesh-avatar-rigging`: rig e deformação de ilustração, não eventos/LLM/TTS de live.
- `synthetic-presenter-video` e `ai-reels-production`: produção assíncrona de vídeo gravado, não orquestração de respostas de audiência.
- `content-production`/`social-growth-engine`: estratégia/editorial, não operação técnica de live.
- **Novo owner justificado:** eventos da plataforma, filas, deduplicação, moderação, prioridades, latência, fallback e QA de transmissão em tempo real.

## Análise de segurança
**Veredito: CAUTION / static_only.**
- `iniciar.bat` executa `pip install aiohttp edge-tts` sem versões pinadas. A instalação não foi executada nem a cadeia de pacotes auditada.
- `configuracion.txt` guarda chaves de Gemini/Groq em texto claro; o README alerta para não compartilhar. Preferir secrets manager/env e .gitignore.
- Há chamadas remotas para modelos e voz; textos de espectadores podem ser enviados a serviços terceiros. Exigir revisão de privacidade e política de dados.
- `script.py` limita HTTP local ao loopback e usa whitelist de extensões/paths no servidor de arquivos; evento WebSocket do TikFinity é tratado como fonte externa e pede limites robustos de payload e autenticação quando cabível.
- Os filtros lexicais e normalização diminuem algumas ofensas, mas têm falso positivo, evasão e não cobrem a segurança semântica nem prompt injection.
- A conexão upstream usa `max_msg_size=0` (sem limite interno de mensagem); risco de consumo de recursos em payloads malformados. Revisar antes de produção.
- Integrações e elegibilidade TikTok não são garantidas pelo repositório. Não recomendar contornar avisos do Windows sem validação da origem.

**Ausência de prova:** não houve teste com live, teste de carga, lint, scanner estático especializado ou auditoria de transitivos, nem confirmação da disponibilidade dos modelos configurados. A licença MIT foi declarada na metadata do repositório, sem auditoria de assets incorporados.

## Adaptação e QA exigidos
Foi preservado o fluxo fonte→evento→validação→fila→LLM→moderação→TTS→UI, além de modo offline, política de prioridade, fallback e testes. Removidos como requisitos: TikFinity, Gemini, Groq, Edge TTS, Windows, Flow/DeepSeek e OBS. Dependências específicas são exemplos condicionais.

**Critérios de aceitação da skill:** YAML com name/description; trigger e near-miss; integração opcional; fronteira de credenciais e segurança; testes sintéticos; referência a owners adjacentes; indexação no Arsenal; read-after-write. **Runtime real não testado.**

## Arquivos e publicação
- `skills/interactive-live-avatar-production/SKILL.md`
- `ARSENAL INDEX.md`
- `evaluations/santistudio-streamer-ia-tiktok.md`

Publicação: commits registrados pela operação de escrita no GitHub; consultar o histórico para o SHA final.
