# Avaliação em lote — Zapier, FreeLLMAPI, OpenManus, Odysseus, Vane, InvokeAI, ACE-Step 1.5 e Dyad

Data: 2026-10-08. Método: stacks/arsenal-autopilot/STACK.md, ARSENAL INDEX canônico e skill-security-review. Triagem estática de README/documentação, sem instalar ou executar software externo.

## Decisões por fonte

| Fonte | Classe | Decisão | Owner / justificativa |
|---|---|---|---|
| https://github.com/zapier | B/D | UPDATE_EXISTING | Em especial zapier/wade-skills e zapier/agent-skills: meeting-to-actions, weekly-review-planning, decision-analysis e ai-workflow-automation-engineering. Skills específicas de Zapier SDK não são portáveis automaticamente. |
| https://github.com/tashfeenahmed/freellmapi | A/D | ALREADY_ABSORBED | model-routing-gateway já referencia a origem e registra avaliação anterior (2026-09-26). |
| https://github.com/FoundationAgents/OpenManus | B/D | KEEP_EXTERNAL_REFERENCE | Runtime Python, browser-use MCP e provider keys exigidos; loops agente/browser já cobertos por computer-use-agent-engineering e agent-action-governance. |
| https://github.com/odysseus-dev/odysseus | A/D | UPDATE_EXISTING | ai-workspace-operating-cycle: status de integração, instalação limpa, context budget para modelos locais, segurança de tools. A branch default é dev, não um release garantido. |
| https://github.com/ItzCrazyKns/Vane | B/D | KEEP_EXTERNAL_REFERENCE | Motor de respostas com SearxNG, pesquisa citada, busca privada, seleção de fontes; potencialmente útil para pesquisa, mas sem ganho metodológico exclusivo confirmado. |
| https://github.com/invoke-ai/InvokeAI | A/D | KEEP_EXTERNAL_REFERENCE | Canvas, nós de workflows, metadados, galeria e remix; padrões já amplamente previstos em ai-workspace-operating-cycle e design/canvas. Considerar avaliação mais profunda quando houver trabalho concreto em geração visual. |
| https://github.com/ace-step/ACE-Step-1.5 | A/D | ALREADY_ABSORBED | music-generation-engineering já tem provenance explícita ACE-Step. |
| https://github.com/dyad-sh/dyad | B/D | KEEP_EXTERNAL_REFERENCE | App builder local BYOK; coding-agent-engineering, software-engineering-cycle e web-design-engineer já cobrem metodologia. Atenção às licenças distintas no diretório src/pro. |

## Capability ledger: ganho incremental

- Zapier Wade — painel adversarial como **lentes simuladas** sem fingir especialistas consultados: UPDATE_EXISTING decision-analysis.
- Zapier Wade — agenda semanal com fontes, carry-forwards, filtro cross-functional e tratamento: UPDATE_EXISTING weekly-review-planning.
- Zapier Wade — níveis de profundidade de reuniões e write-back proposto: UPDATE_EXISTING meeting-to-actions.
- Zapier agent-skills — compatibilidade SDK/min tested, command-surface, optimistic concurrency: UPDATE_EXISTING ai-workflow-automation-engineering. Não executar freshness script automaticamente.
- Odysseus — degraded state por integração e testes de fresh-install, contexto mínimo e auth: UPDATE_EXISTING ai-workspace-operating-cycle.
- InvokeAI — node canvas, galeria e provenance: KEEP_EXTERNAL_REFERENCE, owner de workspace já abrange arquitetura; sem runtime/gráficos importados.
- FreeLLMAPI e ACE-Step — nenhuma escrita adicional porque já absorvidos.
- OpenManus, Vane, Dyad — referências externas sem nova skill.

## Revisão de segurança e portabilidade

Veredito: CAUTION para importar/executar os runtimes; APPROVE somente para incorporar as metodologias revisadas como instruções.

Riscos: instaladores curl-pipe-shell, Docker :latest, extensão de permissões de agente/browser/shell, exposição de credenciais e serviços locais, plugins/tools externos, prompt injection por material recuperado, licenças e modelos/weights, licença AGPL no Odysseus e licença de código misto no Dyad. Nenhum installer, pacote ou script foi executado. Não houve auditoria exaustiva de código-fonte, SBOM ou dependências, logo esta avaliação não certifica segurança dos produtos. Hardware, keys, modelos e serviços continuam dependências externas, não capacidades nativas deste ChatGPT.

## Arquivos alterados

- skills/decision-analysis/SKILL.md
- skills/weekly-review-planning/SKILL.md
- stacks/meeting-to-actions/STACK.md
- stacks/ai-workspace-operating-cycle/STACK.md
- skills/ai-workflow-automation-engineering/SKILL.md

Nenhuma skill ou stack nova; descriptions do índice não mudaram, portanto ARSENAL INDEX não exige atualização. Preservado menor conjunto útil.

## Verificação de comportamento sugerida

1. Decisão estratégica: lentes apontam riscos diferentes e não fingem entrevistas reais.
2. Semana com apenas dois temas reais: agenda não inventa tópicos extras.
3. Reunião rotineira sem compromissos: não gera tickets nem e-mails artificiais.
4. Workflow com SDK incompatível: bloqueia publicação sem atualizar automaticamente toolchain.
5. Workspace com integração ausente: relata indisponibilidade, em vez de alegar dados lidos.

A validação foi estática/documental; não houve execução de runtimes externos nem teste end-to-end desses cenários.
