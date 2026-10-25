# Avaliação Arsenal — cinco repositórios (2026-10-24)

## Grounding
Fonte canônica: `ARSENAL INDEX.md`. Router: `stacks/arsenal-autopilot/STACK.md`. Avaliação por README atual e comparação com owners específicos. Sem execução de código externo nem scanner completo.

| Origem | Categoria | Decisão | Justificativa / owner |
|---|---|---|---|
| [lovisdotio/motion2code](https://github.com/lovisdotio/motion2code) | A/D | UPDATE_EXISTING | Pipeline vídeo → observação por timestamps → SVG/GSAP seekable → diff por frame e QA de loop. Atualizado `skills/gsap-animation/SKILL.md`. Depende de Python, ffmpeg, Playwright e GSAP para prova em runtime, não importados. |
| [omnara-ai/omnara](https://github.com/omnara-ai/omnara) | B/D | UPDATE_EXISTING | Arquitetura de plataforma com event log durável, workers intercambiáveis, máquinas e aprovações. Atualizado `skills/durable-workflow-engineering/SKILL.md`; controles de ação remetidos a `agent-action-governance`. Não equivale a implantar Omnara. |
| [AbdullahAlhariri/penmentor](https://github.com/AbdullahAlhariri/penmentor) | A/D | UPDATE_EXISTING | Correção no primeiro erro, avaliação linha a linha, pistas graduais e recuperação ativa. Atualizado `skills/teach/SKILL.md`. Xournal++/X11/Manim e modelos CLI não instalados. |
| [tombkeeper/BitKindle](https://github.com/tombkeeper/BitKindle) | D | KEEP_EXTERNAL_REFERENCE | Compilador C auto-hospedado a partir de seed binária de 3.584 bytes, específico Windows x64; metodologia de bootstrap e reproducibilidade já coberta por `build-system-engineering`, sem ganho suficientemente novo para mudança. |
| [rolottr/bambu-bar](https://github.com/rolottr/bambu-bar) | D | KEEP_EXTERNAL_REFERENCE | App SwiftUI para monitorar/controlar impressoras Bambu Lab na LAN, requer macOS 26 e equipamento; sem caso de uso novo e portátil para uma skill geral. |

## Segurança e portabilidade
- **Motion2Code — CAUTION:** scripts Python/Playwright, browser, CDN e vídeos de origem; tratar páginas/clipes como dados não confiáveis e não executar installers da fonte. Renderização e comparação só são prova se realizadas.
- **Omnara — CAUTION:** runners com shell, provedores, rede, secrets, daemon e infraestrutura Docker/DB; local defaults declaradamente inseguros pelo README. Requer isolamento, política e controle de credenciais, aprovações e observabilidade. Não foi implantado.
- **Penmentor — CAUTION:** captura de páginas manuscritas, CLIs de agentes, screenshots e possíveis dados pessoais; evitar upload implícito e armazenamento excessivo. Não foi executado.
- **BitKindle — CAUTION:** seed binária, PowerShell ExecutionPolicy Bypass e execução de binários gerados. Identidade entre builds não demonstra ausência de malware/erros. Não executado.
- **Bambu Bar — CAUTION:** descoberta LAN, leitura de código de acesso, controle físico pause/stop e Keychain. Hardware, rede e autorização antes de uso; não executado.
- Revisão estática limitada a documentação inicial; sem análise integral de dependências, instrumentação, pentest ou scanner.

## Publicações efetivas
- `skills/gsap-animation/SKILL.md` — commit `17ea3951ea3654b99c9f638da3069a3cb57288d2`.
- `skills/durable-workflow-engineering/SKILL.md` — commit `be055142019ca9fa74b23e7f8b52e290e90d6fc6`.
- `skills/teach/SKILL.md` — commit `c2594a3812ae352f0e5dd2060fb200869163c43c`.

Sem novos owners ou descrições materialmente alteradas: `ARSENAL INDEX.md` não demanda atualização. Verificação pós-escrita: reler os três arquivos e este registro do GitHub.

## Limites de conclusão
Metodologias incorporadas e rastreáveis. Nenhum app, biblioteca, agente, processo permanente ou simulação externa foi instalado, testado ou ativado.
