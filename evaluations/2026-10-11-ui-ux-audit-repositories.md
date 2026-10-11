# Avaliação de repositórios para auditoria UI/UX — 2026-10-11

## Objetivo
Melhorar a auditoria existente sem duplicar owners canônicos. Fonte de autoridade: `ARSENAL INDEX.md` e `skills/design-principles-audit/SKILL.md` do GitHub oficial. Decisão operacional: `UPDATE_EXISTING` + ajustar integração em `improve-existing-web-app`, não criar skill nova.

## Critérios
Valor incremental; metodologia demonstrável; tipo de evidência; dependências; riscos de instaladores/scripts/credenciais; portabilidade para ChatGPT; manutenção. Classes: A = skill com mudança concreta de comportamento; B = método absorvível; C = prompt com baixa novidade; D = mecanismo técnico condicionado a runtime.

## Fontes e decisões

| Fonte externa | Classe | Ganho incremental | Decisão |
| --- | --- | --- | --- |
| https://github.com/paulunemoon/ux-audit-skill | A | 16 dimensões, severidade versus confiança, limites por modalidade de evidência | UPDATE_EXISTING: matriz de cobertura e confiança |
| https://github.com/EnchStyle/ui-ux-audit-skill | A/D | Medição/checagem visual em viewports distintos, com script Playwright | ABSORB_METHOD_ONLY: viewport/estado reproduzíveis; não instalar scripts |
| https://github.com/scottkw/ui-audit-skill | A/D | Diagnosticar, corrigir, reauditar; relatório persistente | UPDATE_EXISTING: gate de reteste e baseline |
| https://github.com/meshcode-ai/skills-design | B | Hierarquia visual, consistência e tokens | ABSORB_METHOD_ONLY: critérios contextuais; rejeitar nota arbitrária A–F como conformidade |
| https://github.com/openai/plugins | B (referência a aprofundar) | Abordagem de auditoria de produto baseada em evidências; não confirmado nesta rodada arquivo específico da skill | KEEP_EXTERNAL_REFERENCE: não atribuir capabilities não verificadas |
| https://github.com/microsoft/playwright | D | Testes de browser | KEEP_EXTERNAL_REFERENCE: somente quando browser/runtime autorizado e disponível |
| https://github.com/dequelabs/axe-core | D | Verificações automatizadas de acessibilidade | KEEP_EXTERNAL_REFERENCE: complementar a testes manuais e WCAG |
| https://github.com/GoogleChrome/lighthouse-ci | D | Quality budgets e regressões | KEEP_EXTERNAL_REFERENCE: depende de CI/instrumentação |
| https://github.com/storybookjs/test-runner | D | Testes de estados de componente | KEEP_EXTERNAL_REFERENCE: somente quando projeto suportar |

Outras fontes levantadas anteriormente (brumley-agents/claude-ui-ux-audit-skill, borghei/Claude-Skills, carlsz/ux-agent-skills, WomenDefiningAI/claude-code-skills, otherland/prompts-and-skills e curiositech/some_claude_skills) permanecem radar de descoberta, **sem adoção nesta rodada** por não ter sido realizada validação específica de seus arquivos canônicos.

## Capability ledger

| Capability | Owner | Novo comportamento |
| --- | --- | --- |
| Jornadas, estados e cobertura | design-principles-audit | Inventário priorizado por risco, lacunas explicitadas |
| Evidência e confiança | design-principles-audit | Finding com esperado/observado, condição e confiança |
| Consistência visual | design-principles-audit | Critérios situados sem score cosmético obrigatório |
| Verificação comportamental | runtime-ui-verification (já existente) | Teste real, distinguindo aparência de consequência |
| WCAG e performance | web-quality-audit (já existente) | Gate normativo/mensurável, sem reivindicar WCAG via scanner |
| Correção e reauditoria | improve-existing-web-app | Preservação de IDs, baseline e testes de regressão |

## Portabilidade, segurança e limites
Não instalar scripts, hooks, extensões, MCP, browser frameworks ou comandos Claude/Codex de terceiros para aplicar as instruções. Usar somente ferramentas conectadas e disponíveis, com autorização e escopo. Não presumir acesso a estado de rede, DOM, screenshots, execução de scripts ou CI. Captura única não valida keyboard, performance, privacidade ou conclusão funcional. Resultados agregados não demonstram qualidade sem cobertura e evidência.

## Testes de aceite do método
- **Should trigger:** "audite UI/UX do app, encontre problemas no fluxo mobile e priorize correções" → protocolo por jornada, evidência, confiança e cobertura.
- **Should trigger:** "corrija todos os findings UX" → baseline, implementação proporcional, reauditoria com mesmo critério e estado de cada finding.
- **Near miss:** "crie um site novo" → não acionar auditoria integral sem interface existente.
- **Near miss:** "analise uma única screenshot" → não afirmar funcionamento, rede, teclado ou conformidade total.
- **Falha de evidência:** URL inacessível → achados sustentados por outros materiais e `UNKNOWN` nos testes pendentes.

## Publicação
Integração registrada em `skills/design-principles-audit/SKILL.md` e `stacks/improve-existing-web-app/STACK.md`. O índice existente já lista esses recursos; não criar alias ou nova entrada para um owner inalterado. Repositórios externos são fontes de método, não autoridade do Arsenal.
