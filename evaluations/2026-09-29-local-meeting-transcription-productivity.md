# Avaliação — transcrição local de reuniões e produtividade

Data: 2026-09-29

## Fontes aprofundadas
- elmoghany/meeting-scribe
- anshuman-pandey/open-granola
- igarrux/kuali
- Higangssh/ghostmeet
- Vexa-ai/vexa

## Decisões
| Fonte | Classe | Decisão |
|---|---|---|
| MeetingScribe | A/B/D | KEEP_EXTERNAL_REFERENCE + UPDATE_EXISTING |
| Open Granola | A/B/D | KEEP_EXTERNAL_REFERENCE + UPDATE_EXISTING |
| Kuali | A/B/D | KEEP_EXTERNAL_REFERENCE + UPDATE_EXISTING |
| ghostmeet | B/D | KEEP_EXTERNAL_REFERENCE |
| Vexa | A/B/D | KEEP_EXTERNAL_REFERENCE |

Nenhuma nova skill de transcrição foi criada: são runtimes externos, não uma capacidade nativa do ChatGPT. O owner correto continua sendo `meeting-knowledge-capture`, que recebe gravação/transcript quando uma ferramenta real o produz.

## Metodologia absorvida
`meeting-knowledge-capture` agora:
- prefere speaker identity fornecida pela plataforma/captura quando disponível;
- mantém diarização inferida corrigível e sem inventar nomes;
- exige rastreabilidade de decisões/action items ao trecho/timestamp quando a fonte permitir;
- distingue draft gerado por IA de fato aprovado;
- preserva transcript bruto quando auditoria exigir.

## Orientação de runtime
Para Windows e uso individual em Google Meet, Open Granola apresenta a menor fricção declarada: pacote MSI, WASAPI loopback, mic + system audio, Whisper local, diarização local e notas por LLM local, sem conta/cloud. Modelos iniciais somam cerca de 4 GB segundo o README.

MeetingScribe oferece controles e exports mais ricos e diarização/voice memory, mas exige ambiente Python e componentes ML; qualidade máxima local com large-v3 + pyannote + LLM pode ser pesada para laptop/CPU.

Kuali é especialmente interessante quando identidade real dos participantes no Meet é requisito, mas o README atual documenta Quick Start nativo principalmente para macOS; não foi escolhido como instalação Windows principal nesta rodada.

ghostmeet é simples para captura de aba no Chrome, porém speaker diarization ainda consta no roadmap; não é a melhor escolha quando "transcrição completa" inclui quem falou.

Vexa é a escolha quando um bot precisa entrar sozinho na reunião. Self-host completo tem alvo de produção Linux/Ubuntu + Docker e é mais infraestrutura do que desktop recorder; hosted oferece apenas crédito inicial limitado.

## Limites
Não instalamos nem executamos nenhum desses projetos no computador do usuário. Claims de precisão/performance são dos próprios repositórios e não foram reproduzidos. Consentimento/gravação deve respeitar participantes, política da organização e legislação aplicável.
