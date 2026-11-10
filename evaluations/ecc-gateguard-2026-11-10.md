# Reavaliação: affaan-m/ECC (GateGuard)

- Data: 2026-11-10
- Fonte: https://github.com/affaan-m/ECC, commit `d2ef268` (2026-11-06), VERSION 2.2.3 + seção Unreleased do CHANGELOG
- Fluxo: `evaluate-and-import-skill` + `skill-security-review` (inspeção estática; nada instalado ou executado)
- Avaliações anteriores: 2026-09-26 (batch ECC/Ruflo), 2026-10-03 (top 20), 2026-10-06 (ECC + Rive; memória, aprendizado, revisão independente, orçamento de contexto, falhas silenciosas), 2026-10-22 (top 100)
- Classificação: **A/D** (inalterada)
- Decisão: **UPDATE_EXISTING** em dois owners

## Escopo desta reavaliação
Só o que mudou depois de 2026-10-06. O repositório hoje tem 314 skills, dezenas de agents, hooks, rules, adaptadores para vários harnesses, `ecc2/`, dashboard e instalador; a quase totalidade já foi triada ou é coberta por owners existentes. A mudança relevante é o **GateGuard**: hook PreToolUse que nega o primeiro Edit/Write/Bash/MultiEdit/NotebookEdit em cada arquivo até o agente apresentar fatos concretos, com perguntas por classe de alvo, crédito para buscas já feitas, regras mais duras para arquivos sensíveis e um harness de avaliação de efetividade.

## Delta incorporado
1. `skills/coding-agent-engineering/SKILL.md` — checklist "fatos antes do primeiro toque" por tipo de mudança (importadores vs chamadas locais, amostra real do formato de dados, helper duplicado, testes que fixam o comportamento antigo, segredos como referência, instrução literal), com lista de arquivos sensíveis. Aplicado como checklist proporcional ao risco, não como bloqueio em toda edição.
2. `skills/empirical-prompt-tuning/SKILL.md` — desenho para avaliar gates/hooks: hipóteses antes, armadilha por cenário com avaliador oculto, referência e solução ingênua, braços sem regra / com regra / placebo / sem a pergunta-alvo, custo reportado junto com efeito.

## Achado de evidência
O `SKILL.md` do GateGuard anuncia "+2,25 pontos" a partir de dois A/B em duas tarefas. O próprio relatório posterior (`docs/gateguard/question-effectiveness.md`) rodou 72 sessões (6 cenários × 4 braços × 3) e todos os braços passaram em tudo: mediu só o custo (cerca de 45% mais turnos), não o efeito. A pergunta de "contrato externo" virou opt-in porque os testes de intenção oculta não mostraram ganho. Conclusão: o método de perguntas é útil, mas o ganho de qualidade não está demonstrado; o Arsenal registra isso em vez de repetir o número do README.

## Não incorporado
Hooks, instalador (`install.sh`, `install.ps1`, plugin `ecc@ecc`), variáveis `GATEGUARD_*`, métricas, harness Docker, as demais 313 skills e agents.

## Segurança: CAUTION
- Instalação completa adiciona hooks em vários eventos do Claude Code, rules, agents, MCP configs e escreve em `CLAUDE_CONFIG_DIR`/`~/.claude`.
- O próprio README alerta para cópias maliciosas fora dos canais oficiais.
- GateGuard é conservador (só remove negações exceto em arquivos sensíveis), mas custa turnos em toda primeira edição.

## Instalar no Claude?
- Claude chat: não se aplica.
- Claude Code: não instalar o ECC completo; sobrepõe superpowers, mattpocock e as skills já instaladas e consome contexto. Se quiser só o GateGuard, instalar isoladamente num projeto de código com risco real (dados, pagamentos) e medir se compensa os turnos extras.

## Limites da validação
Leitura de README, CHANGELOG (Unreleased e 2.2.3), `skills/gateguard/SKILL.md` e `docs/gateguard/question-effectiveness.md` (início). Hooks, scripts e demais skills não auditados nem executados.
