# FluidVoice (2026-11-09)

## Fonte
- https://github.com/altic-dev/FluidVoice — GPL-3.0 desde 2026-02-23 (Apache-2.0 antes), ~12,9k estrelas, release 1.6.0
- Lido: README público

## O que é
Aplicativo de ditado (voz → texto) para **macOS 15+**, gratuito e open source, com transcrição no próprio computador: Nemotron Speech 3.5 (multilíngue), Parakeet TDT v2/v3, Cohere Transcribe, Apple Speech e Whisper (Tiny a Large). Português é suportado por Parakeet TDT v3, Cohere Transcribe e Whisper. Pós-processamento opcional por LLM (OpenAI, Groq, provedor próprio) ou pelo runtime local "Fluid Intelligence", que é fechado. "Command Mode" abre apps e roda atalhos por voz. Sem integração com agentes, skills ou MCP. Versões para iOS e Windows anunciadas, sem data.

## Decisão
| Item | Classe | Decisão |
|---|---|---|
| Aplicativo | D | **NÃO ADOTAR** — ferramenta de usuário final, não método nem skill; e **só roda em macOS**, enquanto o ambiente principal do usuário é Windows (`C:\Users\ph_gr\Skill-Arsenal`, conforme AGENTS.md) |
| Método | — | Nada novo: transcrição local, escolha de modelo por idioma e pós-processamento por LLM já estão em `realtime-voice-agent-engineering` |

## Gatilho
Reavaliar quando a versão para Windows for lançada, se o usuário quiser ditar prompts e textos em português com transcrição local.

## Segurança
Nada executado. Analytics **ligados por padrão** (ID anônimo de instalação, data, versão, SO e contagem de uso de recursos/modelos; o projeto afirma não coletar áudio nem texto) — desligar nas configurações. Pós-processamento em nuvem envia o texto ao provedor escolhido. O README alerta que fluidvoice.org não é oficial; os canais oficiais são altic.dev/fluid e as Releases do GitHub. GPL-3.0 restringe incorporação de código.
