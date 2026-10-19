# Avaliação: Anthropic frontend-design (2026-10-19)

## Fonte e escopo
- Fonte: https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md
- Consultado em: 2026-10-19; documento upstream informa modificação em 2026-09-02.
- Conteúdo revisado: metodologia textual do SKILL.md. Sem execução de scripts ou instalação de Claude Code.
- Owners consultados: `skills/design-direction/SKILL.md`, `skills/web-design-engineer/SKILL.md`, `skills/design-principles-audit/SKILL.md`, `skills/skill-security-review/SKILL.md` e `stacks/evaluate-and-import-skill/STACK.md`.

## O que faz de fato
Define direção visual específica a briefing e domínio antes de implementação; sugere escolha deliberada de hero, paleta, tipografia, alinhamento, wireframe e elemento de assinatura. Exige crítica dos padrões visuais frequentemente produzidos por IA. Inclui microcopy, moderação de motion e piso de responsividade/acessibilidade, mas não contém engine, testes automáticos ou ferramenta de render.

## Classificação e decisão
- **B — Boa metodologia.** O diferencial é o gate explícito de especificidade visual, revisão em dois passes e crítica de clichês por contexto, não uma capacidade técnica independente.
- **Decisão: ABSORB_IN_EXISTING_OWNER.** Não criar `skills/frontend-design`: `design-direction` já define tese visual, tokens, gramática de layout e assinatura; `web-design-engineer` já implementa e verifica. Importar somente a revisão incremental de hero, anti-default, parcimônia de motion, intenção da estrutura e microcopy.
- Ganho real sobre instrução genérica: checkpoint reproduzível para evitar UI de template e exigir racional vinculado ao produto.
- Limite: originalidade estética é avaliação qualitativa, não métrica objetiva.

## Dependências, segurança e portabilidade
- A skill upstream é texto declarativo. Não apresenta dependências executáveis nem necessidade de CLI, scripts, credenciais, instalação, browser ou runtime Claude Code para aproveitar a metodologia.
- Revisão manual do SKILL.md: sem comandos para exfiltração, persistência, auto-instalação ou elevação de privilégio. **APPROVE** para absorção metodológica; não equivale a auditoria integral de todo repositório upstream.
- A checagem visual por screenshots só é feita se o runtime realmente estiver disponível. Respeitar a marca aprovada e exigências explícitas antes de qualquer preferência estética da fonte.
- Regras anticlíchê são diagnósticas, não banimentos universais de fonte, cores, cards ou gradientes.

## Implementação e verificação
- Alterado: `skills/design-direction/SKILL.md`, seção `Gate de especificidade visual e autocritica`.
- Commit de implementação: `b3589fcb131de405008f573dd090fa75cc7012a7`.
- `ARSENAL INDEX.md` não precisa mudar: nenhuma skill/stack nova e description preservada.
- Verificação: releitura do arquivo remoto após escrita e confirmação do registro publicado. Sem teste visual de app, pois esta tarefa avalia metodologia, não um frontend em runtime.

## Aplicação
Acionar apenas para novas interfaces ou redesigns substanciais em que a identidade visual importa. Na execução: proposta breve de direção, crítica de genericidade, implementação e QA. Para modificações triviais, dispensar o gate.
