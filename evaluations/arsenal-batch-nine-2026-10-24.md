# Avaliação: nove repositórios (2026-10-24)

Fonte: ARSENAL INDEX.md, stacks/arsenal-autopilot/STACK.md e README público da branch main das origens. Revisão documental; não foram executados binários, testes ou scanners. Não confundir claims dos autores com benchmarks validados.

| Projeto | Classe | Decisão | Justificativa |
|---|---|---|---|
| https://github.com/dedicatedcode/reitti | D | KEEP_EXTERNAL_REFERENCE | Rastreamento GPS com dados pessoais sensíveis, hardware/federação; nenhuma necessidade geral de skill comprovada. |
| https://github.com/alexpasmantier/television | B/D | UPDATE_EXISTING skills/kb-retriever/SKILL.md | Canais de busca incremental, preview e ações seguras. |
| https://github.com/opengeos/RustGIS | D | KEEP_EXTERNAL_REFERENCE | GIS desktop/web scriptável; precisa motor, datasets, projeções e validação espacial, não disponíveis por default. |
| https://github.com/langfuse/langfuse | A/D | UPDATE_EXISTING skills/llm-observability-evaluation/SKILL.md | Ciclo trace-dataset-prompt-eval e comparação reprodutível. |
| https://github.com/marclou/mailcheap | B/D | UPDATE_EXISTING skills/email-campaign-engineering/SKILL.md | Consentimento, pré-envio, rollout e deliverability por evidência. |
| https://github.com/vectorize-io/hindsight | A/D | UPDATE_EXISTING skills/agent-memory-engineering/SKILL.md | Contratos retain/recall/reflect e proteção contra promoção não supervisionada. |
| https://github.com/onecli/onecli | B/D | UPDATE_EXISTING skills/agent-action-governance/SKILL.md | Gateway corporativo de credenciais, IdP, isolamento e approvals. |
| https://github.com/crivion/laranode | D | KEEP_EXTERNAL_REFERENCE | Painel de hospedagem privilegiado: backups/restores e demo já cobertos em técnicas do Arsenal; instalação shell requer auditoria específica. |
| https://github.com/MakazhanAlpamys/Soup | D | KEEP_EXTERNAL_REFERENCE | Fine-tuning de LLM específico de runtime GPU/RAM; não confundir com skill existente de difusão nem importar claim de VRAM sem benchmark independente. |

## Critérios e riscos
Should-trigger: pipeline de tracing real, memória reflexiva ou gateway multiusuário, ou trabalho explícito de newsletter/retrieval. Near-miss: mera consulta pontual sem runtime nem estado. Prova futura: regressão pareada com fonte/versionamento, autorização e controle de efeitos. Classificação CAUTION para instalação: Docker/serviços, credenciais, scripts privilegiados e modelos exigem threat model, pinning, testes e revisão de licença. Fonte externa continua opcional; nenhum código importado. ARSENAL INDEX.md inalterado porque não surgiram novos owners/rotas.
