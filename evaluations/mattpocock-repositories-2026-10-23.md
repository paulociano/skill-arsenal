# Avaliação: mattpocock GitHub repositories (2026-10-23)

## Escopo e fontes
- Fonte: https://github.com/mattpocock?tab=repositories
- Fonte aprofundada: https://github.com/mattpocock/skills
- Documentos examinados: `skills/engineering/tdd/SKILL.md`, `tests.md`, `mocking.md`, `to-spec/SKILL.md`, `implement-spec/SKILL.md`, `domain-modeling/SKILL.md`, `wayfinder/SKILL.md`.
- Fonte complementar: `mattpocock/agent-rules-books` (README).
- Radar de repositórios: `evalite`, `ts-reset`, `ai-sdk-tips`. Não houve leitura técnica dos conteúdos; nenhuma adoção ou veredito de segurança específico.
- Autoridade interna: `ARSENAL INDEX.md`, `stacks/arsenal-autopilot/STACK.md`, `stacks/evaluate-and-import-skill/STACK.md`, `skills/tdd/SKILL.md`, `skills/domain-modeling/SKILL.md`, `skills/software-testing-engineering/SKILL.md`, `skills/coding-agent-engineering/SKILL.md`, `skills/skill-security-review/SKILL.md`.

## Capability ledger e decisões
| Candidata | Classe | Owner no Arsenal | Decisão | Justificativa |
| --- | --- | --- | --- | --- |
| TDD / tests / mocking | A/B | `skills/tdd` | UPDATE_EXISTING | Complementar seams públicos, riscos fora de cobertura e oráculos independentes; não duplicar a skill. |
| Domain modeling | A/B | `skills/domain-modeling` | KEEP_EXTERNAL_REFERENCE | Linguagem canônica, casos-limite e ADRs já incorporados explicitamente. |
| to-spec | B/D | `coding-agent-engineering`, ciclo de software | KEEP_EXTERNAL_REFERENCE | Template/spec e fronteiras de teste são úteis, mas publicar no tracker e labels dependem de configuração não demonstrada; sem novo owner. |
| implement-spec | B/D | `coding-agent-engineering`, software engineering cycle | KEEP_EXTERNAL_REFERENCE | Task graph e integration branch são padrões úteis; subagentes paralelos, worktrees e tracker não estão garantidos pelo runtime. |
| wayfinder | B/D | ciclo de produto/software | KEEP_EXTERNAL_REFERENCE | Mapa de decisões dependente de issue tracker é próximo de métodos existentes; sem novidade suficiente demonstrada. |
| agent-rules-books | B | `codebase-design`, `domain-modeling` e arquitetura | KEEP_EXTERNAL_REFERENCE | README mostra regras editoriais baseadas em livros; sem importar pacotes ou reproduzir texto protegido. |
| evalite / ts-reset / ai-sdk-tips | não classificada | por definir | DEFER | Apenas descoberta; exigir leitura do código/README canônico antes de decisão. |

## Revisão de segurança e portabilidade
- Avaliação **estática** dos documentos citados, sem executar scripts, instaladores, plugins ou binários.
- `tdd`/metodologia documental: **APPROVE** para adaptação textual limitada; não é aprovação de toda a supply chain do repositório.
- `implement-spec`, `wayfinder` e `to-spec`: **CAUTION** quanto a comandos, subagentes, worktrees, issue tracker, labels, merge e publicação automática; não transportar pressupostos de permissões ou execução.
- Sem scanner automatizado. Não foram auditados instaladores, dependências ou árvore completa.
- Licenças de terceiros e trechos de livro devem ser verificados antes de redistribuição ou inclusão substancial.

## Implementação e verificação
- Alterado: `skills/tdd/SKILL.md` (contrato de seams, limitações de cobertura, oráculos independentes, RED/GREEN realmente observado e critérios should-trigger/near-miss).
- Commit da skill: https://github.com/paulociano/skill-arsenal/commit/a44a405ee2027c5aeab3674b69f7c4d957a33833
- `ARSENAL INDEX.md` não exige alteração: `tdd` já está roteada e descrição permanece correta.
- Validação pretendida: leitura do arquivo publicado, confirmação do cabeçalho/frontmatter e do registro em `evaluations/`. Não executamos testes de aplicação, portanto melhoria metodológica não implica ganho empírico medido.
