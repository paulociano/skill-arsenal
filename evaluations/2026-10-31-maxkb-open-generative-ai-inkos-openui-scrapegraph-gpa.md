# Seis repositórios — MaxKB, Open-Generative-AI, InkOS, OpenUI, ScrapeGraphAI e GPA (2026-10-31)

## Fontes
- https://github.com/1Panel-dev/maxkb
- https://github.com/anil-matcha/open-generative-ai
- https://github.com/Narcooo/inkos
- https://github.com/thesysdev/openui
- https://github.com/ScrapeGraphAI/Scrapegraph-ai
- https://github.com/AutoArk/GPA
- Stack de avaliação: stacks/evaluate-and-import-skill/STACK.md
- Router: ARSENAL INDEX.md (catálogo real: 274 diretórios em skills/ e 32 em stacks/; o README do repositório está desatualizado em 162/21)

## Resultado
Nenhuma skill nova, nenhuma skill alterada e nenhuma mudança em ARSENAL INDEX.md. Todos os seis têm owner existente ou são ferramentas externas sem método portável adicional. O README e a estrutura pública foram a única fonte consultada.

## Decisões

| Repositório | Licença | Classe | Decisão | Owner canônico / motivo |
|---|---|---|---|---|
| 1Panel-dev/MaxKB | GPL-3.0 | D | KEEP_EXTERNAL_REFERENCE | Plataforma de agentes e RAG (Django, Vue, pgvector) para hospedar em Docker. Owners: `kb-retriever`, `retrieval-quality-engineering`. Credenciais de administrador padrão documentadas no README: nunca usar sem trocar |
| anil-matcha/Open-Generative-AI | MIT | D | KEEP_EXTERNAL_REFERENCE (CAUTION) | Estúdio de imagem e vídeo que depende da API paga da Muapi. README promocional (revenda white label, posicionamento "sem filtros de conteúdo"). Owners: `high-fidelity-image-generation`, `synthetic-presenter-video`, stack `ai-reels-production`. Não adotar nem recomendar |
| Narcooo/inkos | AGPL-3.0 | B/D | KEEP_EXTERNAL_REFERENCE (watchlist) | Agente de criação de histórias longas (CLI Node 22.16+, Studio, TUI). README informa 19 skills internas em SKILL.md padrão, não inspecionadas. Sobreposição parcial com `narrative-dialogue-engineering`, `set-continuity` e `writing-quality`. Lacuna real: ficção longa com memória de continuidade, mas sem demanda registrada. Revisitar se houver projeto de ficção, lendo o SKILL.md e passando por `skill-security-review`. AGPL exige cuidado ao adaptar |
| thesysdev/openui | MIT | A/D | ALREADY_ABSORBED | Já avaliado em 2026-10-02 (item 3 do ledger) e 2026-10-10. Owner: `generative-ui-engineering`. Nenhuma mudança. O skill oficial em thesysdev/skills não foi inspecionado nesta passagem (acesso bloqueado por robots) |
| ScrapeGraphAI/Scrapegraph-ai | MIT | D | KEEP_EXTERNAL_REFERENCE | Biblioteca Python de scraping com LLM e Playwright. Owner: `web-extraction-pipeline`. Já aparecia no inventário ComposioHQ (item 656). Telemetria anônima ligada por padrão (opt-out por SCRAPEGRAPHAI_TELEMETRY_ENABLED=false); API gerenciada é paga |
| AutoArk/GPA | Apache-2.0 | D | KEEP_EXTERNAL_REFERENCE | Modelo único de ASR e TTS (GPA-v1.5), voice conversion ainda no roadmap. Exige GPU/ONNX. Owners: `realtime-voice-agent-engineering`, `synthetic-presenter-video`. Clonagem de voz exige as regras de consentimento já presentes em `synthetic-presenter-video` |

## Valor incremental
Nenhum método novo suficiente para justificar edição. Os pontos mais próximos de valor (continuidade de estado em ficção longa no InkOS; schema-prompt extraction no ScrapeGraphAI) ou dependem de runtime externo ou carecem de demanda; seguem como referência.

## Segurança e portabilidade
Nenhum instalador, script ou container foi executado. Riscos observados nos READMEs: credenciais padrão (MaxKB), dependência de API paga e posicionamento promocional (Open-Generative-AI), telemetria por padrão (ScrapeGraphAI), licenças copyleft fortes (MaxKB GPL-3.0, InkOS AGPL-3.0) que restringem incorporação de código.

## Aceite futuro
- InkOS: promover para avaliação completa se o usuário iniciar projeto de romance, roteiro ou série longa.
- GPA: reavaliar quando voice conversion nativo for lançado e se houver caso de uso de transcrição/TTS local.
- Verificação futura: ler SKILL.md e referências dos itens promovidos antes de qualquer adoção.

## Limites da avaliação
Pesquisa documental em READMEs públicos. As páginas `Narcooo/inkos/tree/master/skills` e `thesysdev/skills/tree/main/skills/openui` retornaram bloqueio de acesso automatizado e não foram contornadas. Sem execução de código.

## Arquivos atualizados
- evaluations/2026-10-31-maxkb-open-generative-ai-inkos-openui-scrapegraph-gpa.md (novo)
