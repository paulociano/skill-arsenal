# Avaliação: mattpocock/sandcastle

- Data: 2026-10-23
- Fonte: https://github.com/mattpocock/sandcastle
- Evidência: README.md, package.json (versão 0.12.0), lista de arquivos em src/, metadados do GitHub.
- Categoria: **D — ferramenta técnica**, com padrões metodológicos úteis.
- Decisão: **ADAPT_EXISTING_OWNER** em `skills/multi-agent-orchestration/SKILL.md`. Não criar skill duplicada nem instalar runtime.
- Status: revisão documental/estática parcial, sem execução ou scanner de dependências.

## Função real
Biblioteca TypeScript `@ai-hero/sandcastle` para orquestração de coding agents. Inclui `run()`, `createSandbox()`, `interactive()`, worktrees/branches, providers Docker/Podman/Vercel, provider customizado, hooks, timeouts, logs e coleta de commits. Também aceita `noSandbox()`, que deliberadamente remove o isolamento. Providers bind-mount e isolated têm superfícies distintas.

## Valor incremental
Implementação concreta do lifecycle de sandbox, distinção operacional das estratégias Git (`head`, `merge-to-head`, `branch`), ambiente reutilizável implement-test-review, hooks em host e sandbox, `copyToWorktree`, observabilidade e timeouts. O Arsenal ganha um checklist independente do SDK, útil para desenhar e auditar runtimes de agentes.

## Sobreposição
- `multi-agent-orchestration`: ownership, branches/worktrees, resultados, integração e reviewer.
- `coding-agent-engineering`: loop edit-test-review, contexto e Git boundary.
- `software-factory-operations`: fila, gates e merges supervisionados.
- `agent-action-governance`: permissões e aprovações.
- `skill-security-review`: auditoria de scripts e execução externa.
Não criar nova skill de orquestração: ampliar owner existente.

## Segurança: CAUTION
- `noSandbox()` executa no host, sem isolamento.
- `head` escreve diretamente no working directory, em vez de branch isolada.
- Bind mounts, devices, network e grupos podem ampliar acesso ao host.
- Hooks executam comandos; `copyToWorktree` e ambientes remotos podem expor arquivos, tokens e `.env`.
- Auto-merge e sincronização podem produzir efeitos externos ou conflitar com trabalho existente.
- Logs verbose podem conter informações sensíveis.
- Dependências, scripts e source completo não passaram por auditoria integral; não afirmar ausência de vulnerabilidades.

Mitigação: branch separada, mounts mínimos, política de secrets/egress, limites de iteração/timeout, revisão de diff, testes, aprovação humana para merge/push/deploy, preservação de estado quando falhar.

## Portabilidade
A biblioteca requer Node/TypeScript, Git, CLI de agente e provider de sandbox real; não é ferramenta nativa do ChatGPT. GitHub conectado permite revisar e alterar repositórios, mas não fornece automaticamente sandbox Docker/Podman/agent CLI. Incorporar a metodologia sem simular runtime.

## Mudança publicada
- Owner: `skills/multi-agent-orchestration/SKILL.md`
- Commit: https://github.com/paulociano/skill-arsenal/commit/94fb963680fa5bfddb3ccd286f6f35e85947fe71
- Sem alteração no INDEX: nome, propósito e rota da skill existente permanecem válidos.
- Critério de validação: verificar conteúdo remoto publicado e presença desta avaliação.

## Não validado
Não houve npm install, execução de código do Sandcastle, testes dinâmicos, SAST, revisão profunda das dependências ou comprovação de isolamento por experimento.