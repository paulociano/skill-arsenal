# Avaliação — listmonk, Postiz, Docling, Browser Use e LangChain Agent Evaluation System

Data: 2026-10-19

## Processo
Stack: `arsenal-autopilot` + `evaluate-and-import-skill`, com revisão proporcional `skill-security-review`.
Fonte canônica: `ARSENAL INDEX.md` do GitHub.
Foram lidos README atuais dos cinco repositórios, owners canônicos específicos e avaliação anterior de listmonk. Nenhum script, binário, servidor, container ou installer externo foi executado. A revisão de segurança foi documental e parcial, não auditoria de código completa.

## Matriz e decisão

| Fonte | Classe | Capability | Owner | Decisão |
| --- | --- | --- | --- | --- |
| [knadh/listmonk](https://github.com/knadh/listmonk) | B/D | Mailing lists, opt-in, estados de campanha, bounces, SMTP, self-host | `skills/email-campaign-engineering/SKILL.md` | KEEP_EXTERNAL_REFERENCE: já incorporado na avaliação de 2026-09-20; não duplicar |
| [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | B/D | Scheduler multiplataforma, variantes por canal, publicação, API, analytics | `stacks/social-growth-engine/STACK.md` | UPDATE_EXISTING: adicionar contrato de ciclo operacional, comprovante de publicação, dedupe e credenciais |
| [docling-project/docling](https://github.com/docling-project/docling) | B/D | Parsing multimodal, layout/tabelas, DoclingDocument, provenance, OCR seletivo | `skills/document-extraction-pipeline/SKILL.md` | KEEP_EXTERNAL_REFERENCE: princípios de representação estruturada e locators já incorporados |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | A/D | Agente browser observe-ground-act-verify, trajectories e browser local/cloud | `skills/computer-use-agent-engineering/SKILL.md` | KEEP_EXTERNAL_REFERENCE: fundamentos já incorporados; runtime não é automaticamente disponível |
| [Mohamad-Hachem/LangChain_Agent_Evaluation_System](https://github.com/Mohamad-Hachem/LangChain_Agent_Evaluation_System) | B/D | Evals com casos, tool calls, argumentos, trace e sete métricas | `skills/llm-observability-evaluation/SKILL.md` | UPDATE_EXISTING: fortalecer contrato de regras de negócio, reutilização do mesmo run, oráculos, relógio congelado e guards de ação |

## Novidade e evidência
- **Postiz**: separa calendário editorial de execução real; preflight por rede, contas/canais autorizados, registro de status/URL remota, retries e idempotência. Caso should-trigger: gerir publicação automatizada com scheduler. Near-miss: apenas escrever legenda de um post.
- **Lab LangChain**: demonstra que resposta final correta não prova escolha/argumentos/ordem de ferramentas corretas. Caso should-trigger: avaliar agente com ferramentas e regras de negócio. Near-miss: avaliar somente estilo de um texto sem tool use.
- **listmonk**: metodologia já adaptada em `email-campaign-engineering` segundo `evaluations/2026-09-20-twenty-listmonk.md`.
- **Docling**: owner existente já menciona Docling, preservação de layout/reading order/locators e OCR seletivo.
- **Browser Use**: owner existente já cita Browser Use e define observe/ground/plan/act/verify, isolamento e human takeover.

## Portabilidade e segurança
- **listmonk**: CAUTION. SMTP, importações, PII, reputação de domínio e PostgreSQL. Não enviar nem importar contatos sem autorização legítima. AGPLv3.
- **Postiz**: CAUTION. Tokens OAuth, publicação outward-facing, apps de provedor, armazenamento, Temporal/Redis/Postgres em self-hosting, API e integrações. Não inferir conexão com ChatGPT. AGPLv3.
- **Docling**: CAUTION. Arquivos não confiáveis, OCR/VLM pesados, dependências/modelos e eventual API remota; processar documentos sensíveis conforme política; MIT no repositório, licenças de modelos/serviços separadas.
- **Browser Use**: CAUTION. Navegador com contas, credenciais, cookies, CAPTCHAs, proxy, custos cloud e ações externas; exigir controle de escopo e revisão humana em ações sensíveis. Dependências Python/browser/cloud não instaladas automaticamente.
- **Agent Evaluation System**: CAUTION. API key OpenAI, dados de testes, traces potencialmente sensíveis, judge pago; repositório didático usa dados simulados, relógio dinâmico e regras no prompt, não no serviço. Não copiar modelo/threshold da demo cegamente.

## Implementação
- Atualizado `skills/llm-observability-evaluation/SKILL.md`: sete eixos, cenário+estado+invariantes, mesmo run, validade temporal e bloqueio de efeitos externos.
- Atualizado `stacks/social-growth-engine/STACK.md`: status de publicação, per-channel QA, prova de publicação, retry/dedupe, segurança de credenciais e limites de integração.
- Sem novos owners e sem mudança de descriptions, portanto `ARSENAL INDEX.md` não precisa de alteração.
- Nenhum dos cinco sistemas foi instalado, conectado ou executado.
- Commits: `3cedb8aca13ac26f3dba19394e6e6dbd20a23cf5` e `abaf4484455431e72d65e053f51c2b12c93be599`.

## Limites de validação
Avaliação baseada em documentação e comparação de owners. Não foram executados testes integrados, auditadas dependências profundas, nem verificadas condições reais de publicação/social providers. Claims sobre comportamento esperado são regras metodológicas, não resultados medidos.
