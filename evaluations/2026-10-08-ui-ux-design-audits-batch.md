# UI/UX design audits: avaliação comparativa (2026-10-08)

## Escopo, autoridade e procedimento

Fonte canônica: [ARSENAL INDEX](../ARSENAL%20INDEX.md), stack `arsenal-autopilot`, `evaluate-and-import-skill` e owners atuais `design-principles-audit`, `web-quality-audit`, `design-system-governance`, `runtime-ui-verification` e `web-design-engineer`.

Triagem realizada por metadados, árvores de arquivos e leitura de SKILL.md/README.md e documentação selecionada de cada fonte. Não foram executados instaladores, CLIs, MCP servers, código de terceiros ou testes de produtos reais. Tópicos GitHub são catálogos voláteis, não skills. A segurança é revisão estática parcial, não atestado integral do código.

## Decisão por fonte

| Fonte | Classe | Capacidade incremental | Decisão e owner | Limite / risco |
|---|---|---|---|---|
| [mistyhx/frontend-design-audit](https://github.com/mistyhx/frontend-design-audit) | A | Checklist de 15 heurísticas, severidade 0–4, análise de estados ocultos, finding acionável, revisão pós-fix | **UPDATE_EXISTING:** `design-principles-audit` | Específico a Claude; evitar obrigação artificial de encontrar 10+ problemas e assumir HTML estático como runtime |
| [Aboudjem/ui-ux-suite](https://github.com/Aboudjem/ui-ux-suite) | A/D | Localização arquivo/linha/seletor, valores medidos vs recomendados, dimensões de score, gates por regressão/baseline | **UPDATE_EXISTING:** `web-quality-audit` e `design-principles-audit`. CLI/MCP ficam referência técnica opcional | Installers, parsing/execução e integrações demandariam review separado; score e pesos são convencionais, não normas; APCA não substitui WCAG |
| [tommygeoco/ui-audit](https://github.com/tommygeoco/ui-audit) | B | Scaffolding → decisioning → crafting, macro bets, JTBD, precedência entre contexto interno, convenção e pesquisa | **ABSORB_METHOD_ONLY:** `design-principles-audit` | Framework conceitual e sem licença indicada no metadado, sem replicar texto longo |
| [narenkatakam/ux-audit](https://github.com/narenkatakam/ux-audit) | A/B | Router por superfície: forms, tables, modals, cards, dashboards, buttons, navigation; revisão de estados | **UPDATE_EXISTING:** `design-principles-audit` | Números fixos, "one CTA" e estilo minimalista não são regras universais; scripts/gerador HTML não importados |
| [thedaviddias/Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist) | B/D | Corpus versionável de regras de lançamento, severidade, instruções de verificação e remediação; documentação declara 386 regras em 11 categorias | **UPDATE_EXISTING:** `web-quality-audit`; manter catálogo original como referência | Não duplicar 386 regras; MCP/site/CLI exigem acesso e verificação; conferir vigência de cada regra; não confundir boas práticas com requisitos |
| [GitHub topic: design-audit](https://github.com/topics/design-audit) | B (radar) | Descoberta de outras candidatas | **KEEP_EXTERNAL_REFERENCE** | Lista dinâmica; cada repo descoberto exige avaliação original |
| [GitHub topic: ui-optimization](https://github.com/topics/ui-optimization) | B (radar) | Descoberta de otimização de interfaces | **KEEP_EXTERNAL_REFERENCE** | Não é método validado nem fonte normativa |
| [sm3dev UI UX Front-End Resources](https://gist.github.com/sm3dev/be972ae57ff94d5086a2bb403e995530) | B (curadoria) | Mapa de livros, ferramentas, design systems e referências | **KEEP_EXTERNAL_REFERENCE** | Links variados, alguns históricos/afiliados; não é skill nem valida ferramenta por si |

## Capability ledger e ownership

| Capability | Owner canônico | Evidência de ganho | Near-miss / não fazer |
|---|---|---|---|
| Audit por evidência localizada | `design-principles-audit` | Finding aponta sintoma, causa provável, local observável, severidade e teste | Não inventar linha nem detectar erro só por conjectura |
| Checklists de componente/estado sob demanda | `design-principles-audit` + `runtime-ui-verification` | Cobertura de menu, modal, forms, tables, dashboard e estados relevantes | Não auditar tudo com todos os checklists |
| Quality gate de release baseado em regressão | `web-quality-audit` | Baseline e comparação em condições equivalentes; UNKNOWN explícito | Não perseguir nota arbitrária ou declarar conformidade WCAG por score |
| Decisão contextual em UX | `design-principles-audit` | Rastreabilidade entre tarefa, risco, convenção, negócio e evidência | Não transformar filosofia de uma fonte em dogma visual |
| Sistemas/tokens/contratos de design | `design-system-governance` | Já coberto | Não criar novo owner duplicado |

## Segurança, licença e portabilidade

- Leitura de documentos e metadados somente, sem instalar/executar nada de terceiros. **CAUTION** para executar CLIs/MCP/install.sh externos: inspecionar cadeia de scripts, rede, logs, dados enviados, permissões, dependências e pin antes de habilitar.
- Fontes com licença identificada em metadados: mistyhx MIT; Aboudjem MIT; narenkatakam Apache-2.0; Front-End-Checklist MIT. Tommy Geoco sem license identificada no metadado consultado. Gist e topics tratados apenas como referências; não copiar conteúdo integral.
- Adaptação é editorial/metodológica, não redistribuição de arquivos/scripts dos projetos.
- Não foi comprovado funcionamento de qualquer sistema externo em aplicação-alvo nem desempenho comparativo das auditorias.

## Mudanças adotadas

1. `skills/design-principles-audit/SKILL.md`: gravidade 0–4 vinculada a evidência, findings localizados, checklists por superfície, estados ocultos, separação de norma/heurística e teste de aceitação.
2. `skills/web-quality-audit/SKILL.md`: achado medido, thresholds/baseline e gate de regressão, regra aplicável ao escopo, WCAG x APCA, unknown explícito.
3. Sem novas skills ou stacks: owners existentes já cobrem o trabalho; `ARSENAL INDEX.md` mantém descrições válidas, sem alteração necessária.

## Casos de aceitação

- **Should trigger:** "Audite o fluxo de criação de um projeto, encontre problemas em formulários e modais, priorize e indique arquivo/linha e como testar" → `design-principles-audit` + verificação se runtime disponível.
- **Should trigger:** "Faça QA de frontend antes do release e bloqueie regressões de acessibilidade" → `web-quality-audit` com métricas e baseline.
- **Near miss:** "Crie uma landing page bonita do zero" → `web-design-engineer`, não auditoria extensa como gate inicial.
- **Condição de parada:** avaliação registrada; owners atualizados; sem instaladores, sem promessa de score real em produção; read-after-write realizado.

## Fontes

- https://github.com/mistyhx/frontend-design-audit/blob/main/.claude/skills/frontend-design-audit/SKILL.md
- https://github.com/Aboudjem/ui-ux-suite/blob/main/docs/scoring.md
- https://github.com/tommygeoco/ui-audit/blob/main/SKILL.md
- https://github.com/narenkatakam/ux-audit/blob/main/skills/ux-audit/SKILL.md
- https://github.com/thedaviddias/Front-End-Checklist/blob/main/README.md
- https://github.com/topics/design-audit
- https://github.com/topics/ui-optimization
- https://gist.github.com/sm3dev/be972ae57ff94d5086a2bb403e995530
