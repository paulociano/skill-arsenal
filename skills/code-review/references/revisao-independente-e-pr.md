# Revisao independente e pr

## Revisão independente

Quando a mudança for material e houver acesso real a revisores independentes:

- separar builder de reviewer;
- enviar aos revisores o mesmo pack factual: task/spec, diff relevante, testes, arquitetura e constraints;
- preferir diversidade de modelos/famílias quando isso estiver realmente disponível, porque revisores idênticos podem compartilhar blind spots;
- convergir por **findings e evidência**, não por votação cega;
- um quorum só é útil se cada reviewer puder discordar e citar problemas concretos;
- testes continuam sendo evidência mais forte que consenso de modelos;
- merge/publicação permanece atrás de aprovação humana quando aplicável.

Não depender de tmux, Codex CLI, Gemini CLI, OpenCode ou scripts do GodModeSkill. Se revisores externos não estiverem conectados, usar revisão independente dentro das capacidades reais do ambiente e não fingir diversidade de lineage.

## Handoff de revisão

Quando findings precisam voltar para um builder/agente:

- ancorar cada comentário em arquivo e linha/range quando disponível;
- numerar findings;
- separar comentário inline de resumo geral;
- preservar contexto suficiente para o destinatário corrigir sem reler toda a revisão;
- após correção, revalidar os anchors/linhas afetados e remover findings resolvidos em vez de copiar a lista inteira adiante.

Formato conceitual:

1. `path/file.ext:42` — finding acionável.
2. `path/file.ext:50-55` — finding acionável.
Resumo: riscos sistêmicos ou decisão de merge/review.

## Correção de feedback de PR

Ao corrigir feedback de PR:

1. ler comments/reviews/checks/mergeability e worktree state;
2. isolar mudanças não relacionadas;
3. aplicar a menor correção segura preservando o invariant original;
4. rodar validação estreita e depois gates obrigatórios;
5. fazer cross-review read-only do diff proposto antes de commit/push quando a mudança for material;
6. aceitar somente findings grounded no diff/spec/repo rules/evidence;
7. registrar por que findings foram aceitos ou rejeitados;
8. revalidar após cada blocker corrigido.

Cross-review é evidência, não autoridade. Commit/push/merge continuam ações separadas.
