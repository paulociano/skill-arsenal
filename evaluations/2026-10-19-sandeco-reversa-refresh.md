# Reavaliação: sandeco/reversa (2026-10-19)

- Fonte: https://github.com/sandeco/reversa e README da branch main consultado em 2026-10-19.
- **Classe A (metodologia operacional com mudança clara de comportamento), D para execução integral do framework externo.**
- Decisão: **ADAPT_EXISTING_OWNER**, sem instalar Reversa e sem duplicar skill. Owner: `skills/legacy-system-reconstruction/SKILL.md`.
- Evidência de implementação: commit https://github.com/paulociano/skill-arsenal/commit/0a17b0790ca130ec3b1446795636a12192996660
- A origem já constava no owner canônico. Atualização incremental: rastreabilidade bidirecional SOURCE ↔ RULE ↔ SPEC ↔ ACTION ↔ CODE ↔ TEST ↔ BUG, gates de caracterização antes da implementação, fase de documentação/descoberta somente leitura, escrita controlada em forward, addenda/sync pós-entrega e checkpoints para continuidade.
- Pipeline upstream: reconnaissance/Scout, excavation/Archaeologist, business interpretation/Detective, architecture/Architect, spec/Writer, reviewer/gaps. Oferece também migração, debugging causal, refatoração, greenfield e geração de documentação. Não replicar equipes de agentes onde não agregam valor.
- Dependências externas: Node.js 18+, `npx reversa install`, agentes Claude Code/Codex/Cursor e comandos de sessão `/reversa*`. Não foram instalados/executados nem devem ser tratados como comandos nativos ChatGPT.
- Segurança: **CAUTION** para instalação/execução externa, revisão de documentação somente. O README declara fase de descoberta imutável e recomenda backup; o modo `/reversa-forward-autonomous` explicitamente modifica código, roda comandos e exige política de escrita. Não considerar garantias de README como testes concluídos. Sem revisão integral do installer, subagentes ou supply chain.
- Overlap: `legacy-system-reconstruction`, `repository-evidence-docs`, `behavior-contract-validation`; manter uma fonte canônica para a reconstrução e usar demais skills apenas quando escopo exigir.
- Resultado: reforço do owner existente; sem novo nome no índice, porque descrição/roteamento não mudaram; sem benchmark de aplicação real.
