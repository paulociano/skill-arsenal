# Avaliação de obra/superpowers (2026-10-21)

## Fonte
https://github.com/obra/superpowers (README e skills `brainstorming`, `subagent-driven-development`, `finishing-a-development-branch`, catálogo de `skills/`). Stack de avaliação: `arsenal-autopilot` e `evaluate-and-import-skill`; comparação com índice canônico `ARSENAL INDEX.md`.

## Classificação
**A/B/D**: metodologia de engenharia coerente com ganhos claros em qualidade, porém com hooks, subagentes e workflows dependentes de ferramentas externas. Não é uma única skill portátil.

## Inventário e decisão
- Discovery/brainstorm e aprovação de design: **KEEP_EXTERNAL_REFERENCE**; o Arsenal já dispõe de design, scoping, `project-planning` e `software-engineering-cycle`. O uso obrigatório em toda tarefa prejudicaria requests pequenos; não importar trigger universal.
- Planejamento em fatias, critérios de aceitação, RED-GREEN-REFACTOR, revisão e verificação: **KEEP_EXTERNAL_REFERENCE**; owners `to-tickets`, `tdd`, `code-review`, `verify-before-claim`, `git-worktree-lifecycle`, `software-engineering-cycle` já cobrem o fluxo essencial.
- Desenvolvimento por subagentes: **KEEP_EXTERNAL_REFERENCE** para runtime específico; Arsenal já tem `multi-agent-orchestration` e `coding-agent-engineering`; execução só com delegação realmente disponível.
- Diagnóstico de falha do próprio harness/skills (`diagnosing-superpowers`): **UPDATE_EXISTING** em `skills/coding-agent-engineering/SKILL.md`; novidade útil é triagem por fases, primeira divergência observável e regressões should-trigger/near-miss.
- Encerramento de branch: **KEEP_EXTERNAL_REFERENCE**; decisão humana sobre merge/push e worktree já representada por guardrails do Arsenal.

## Segurança e portabilidade
Revisão estática documental; nenhum installer, hook, script ou agente foi executado. Versões, capacidades e semântica de hooks são específicas da origem, e não podem ser prometidas dentro do ChatGPT. Skills externas contêm instruções de ampla obrigatoriedade e delegação; não transformar comandos externos em permissões. Reconhecimento e uso de transcrições exigem disponibilidade real e limpeza de segredos. Gates humanos são mantidos para ações irreversíveis, acesso sensível e push/merge fora do escopo.

## Valor incremental e teste esperado
- Should-trigger: sessão de coding agent não seleciona skill elegível ou continua sem review e pede análise do motivo; construir timeline observável, primeiro ponto de divergência e correção do owner.
- Near-miss: ajuste direto e simples em arquivo sem fluxo agentic; não disparar diagnóstico ou descoberta longa.
- Validação feita: publicação do texto metodológico e leitura posterior, sem benchmark runtime de agentes.

## Implementação
- `skills/coding-agent-engineering/SKILL.md` atualizado no commit `ee2c21e4ca1c0886c5573e4eab314cb16d8a1078`.
- Este registro em `evaluations/2026-10-21-obra-superpowers.md`.
- `ARSENAL INDEX.md` preservado: nenhuma skill criada nem description alterada materialmente.
