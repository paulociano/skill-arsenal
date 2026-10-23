# Reavaliação — mattpocock/skills (2026-10-23)

Fonte: https://github.com/mattpocock/skills (branch main)
Baseline: evaluations/2026-09-26-mattpocock-skills.md
Motivo: SOURCE_CHANGED; lançamento 1.3.0/1.3.1 com graduação de retro, pr, implement-spec, mudança de convenção para GLOSSARY.md e remoção de resolving-merge-conflicts.

## Escopo e evidência
Consultados README, CHANGELOG, lista de skills e SKILL.md de retro, pr e implement-spec. Não foram executados instaladores, scripts ou testes do repositório externo. Este é um parecer estático/documental, não benchmark.

## Ledger de capacidades
| Capacidade | Classe | Owner canônico | Decisão | Evidência / razão |
|---|---|---|---|---|
| Auditoria retrospectiva do **ambiente** de coding agent | A (método portátil) | skills/retrospective-codify/SKILL.md | UPDATE_EXISTING | Distinção entre check mecânico já existente mas desconectado vs ausência de check; navegação, contexto, tool economy e instruções ineficazes. |
| Corpo de PR com resumo visual mínimo, before/after e merge danger | B | skills/code-review e skills/software-factory-operations | KEEP_EXTERNAL_REFERENCE | Boa estrutura, mas fluxo de revisão já exige evidência e blast radius; não misturar autoria de descrição com revisão do diff sem demanda real. |
| Execução de task graph com worktrees, frontier, branch de integração e subagentes | A/D | skills/software-factory-operations, graph-engineering | KEEP_EXTERNAL_REFERENCE | Processo tem valor; runtime local de worktrees/subagentes background não é garantido no ChatGPT; owners existentes já exigem integração e gates. |
| Atualização para GLOSSARY.md | B | skills/domain-modeling | RETAIN | Convenção de arquivo, não capacidade nova; não impor renomeação a projetos existentes. |
| TDD, debugging, code review, interviewing | A/B | owners existentes no Arsenal | RETAIN | Baseline de 2026-09-26 já identificou overlap. |
| claude-handoff e skills beta | D | handoff (quando cabível) | REJECT como importação | Dependem de comando local Claude e background agent não garantido, ou estão instáveis. |
| resolving-merge-conflicts removida na origem | — | merge-conflict-resolution | RETAIN owner local | Remoção na origem não prova falta de valor no Arsenal. |

## Mudança publicada

UPDATE_EXISTING: skills/retrospective-codify/SKILL.md
Commit: a42fbba25a92e34f614dd84ba2085aefb8630d66
A adição delimita trigger para retrospectiva de sessões com agentes, exige checagem dos gates reais, prioriza verificação determinística para falhas mecânicas, limita acesso a logs inexistentes e preserva gates de aprovação. Não altera índice, pois o owner já existe e sua descrição continua apropriada.

**Should-trigger:** revisão de uma sessão de coding agent com falha que um typecheck existente teria detectado, mas não está conectado ao CI.
**Near-miss:** revisão apenas de código em um PR; permanecer em code-review.
**Failure-path:** logs ou scripts inacessíveis; registrar falta de evidência em vez de alegar verificação de runtime.

## Segurança e portabilidade

Não foram importados instaladores, hooks, skills do Claude/Codex, worktrees, subprocessos ou subagentes. Nenhum acesso a credenciais ou ao ambiente local foi presumido. Propostas de alteração em CI, hooks ou regras globais exigem aprovação/escopo. Não há resultados de testes de execução.

## Próxima condição de reabertura

Reavaliar implement-spec somente se houver runtime operacional confirmado com isolamento de branches e execução/revisão independentes, ou um caso real em que os owners atuais falhem. Reavaliar PR body quando houver recorrência de PRs cujo corpo não reporte evidência/risco.
