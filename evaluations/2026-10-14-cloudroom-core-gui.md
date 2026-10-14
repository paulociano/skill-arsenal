# Avaliação: Cloudroom Core + Cloudroom GUI (2026-10-14)

## Fontes
- https://github.com/davidondrej/cloudroom-core (branch main; README, docs/setup.md, docs/session-lifecycle.md, SECURITY.md)
- https://github.com/davidondrej/cloudroom-gui (branch main; README, gui/README.md, gui/package.json)
- Arsenal: ARSENAL INDEX.md; stacks/arsenal-autopilot/STACK.md; stacks/evaluate-and-import-skill/STACK.md; skills/skill-security-review/SKILL.md; skills/coding-agent-engineering/SKILL.md; skills/durable-workflow-engineering/SKILL.md.

## O que fazem
**Core**: runtime Rust auto-hospedável para executar agentes de programação em máquina Linux, gerenciar sessões e histórico por journal, fornecer API HTTP autenticada e recuperar conversas nativas após reinício. **GUI**: desktop Electron/TypeScript para macOS Apple Silicon (Linux x64 em alpha), com threads locais/remotas, transferência de contexto local-cloud (Teleport), workspaces/Git branches, acesso condicionado a recursos do Mac e computer use. Ambos são software executável, não skills portáveis.

## Classificação e decisão
- **cloudroom-core: D (ferramenta/infraestrutura técnica). KEEP_EXTERNAL_REFERENCE.** Contribui exemplo concreto de lifecycle durável (aceitação fsync, fila idempotente por request_id, receipts, recuperação explícita, outcome unknown), mas os princípios já estão cobertos por `durable-workflow-engineering`, `coding-agent-engineering` e governança de agentes. Não criar skill duplicada nem alegar que o runtime está integrado ao ChatGPT.
- **cloudroom-gui: D (aplicação externa). KEEP_EXTERNAL_REFERENCE.** Interessante como referência de UX e operações de agente local/cloud e níveis de acesso (Off / Read-only / Ask first / Full), já cobertos conceitualmente por `coding-agent-engineering`, `computer-use-agent-engineering` e `agent-action-governance`. Não há ganho incremental que justifique nova skill ou stack.
- **Padrão reutilizável (B, sem nova skill):** handoff de sessão com preservação de histórico, branch/workspace e explícita distinção entre aceitação, execução e conclusão, somente como referência de implementação futura. Não modificar owners existentes com conteúdo redundante nesta avaliação.

## Dependências e portabilidade
Core requer servidor Linux, usuários de sistema separados, Rust e CLIs dos agentes, configuração de rede/token, armazenamento local persistente e opcional backend remoto; a instalação documentada mira Ubuntu 24.04. GUI exige macOS 13+ Apple Silicon, Node/pnpm/Python/Xcode para build; Linux desktop ainda alpha. Uso de contas do usuário nos provedores/modelos. Nenhuma dessas ferramentas ou logins passa a ficar disponível por importar documentação para o Arsenal.

## Segurança (revisão documental estática): CAUTION
- Positivos: serviço com token, padrão de bind localhost, separação de usuário sem sudo, journal persistido e controle de histórico, recomendações Tailscale/HTTPS, versões testadas e checksums no instalador descrito.
- Riscos: agentes executam comandos sem prompts de aprovação no Core; instalação usa script remoto com sudo; acesso a arquivos/computador no GUI, inclusive modo Full; exposição de credenciais, rede, isolamento incompleto ou efeito externo requerem verificação rigorosa; uma máquina por usuário confiável é a recomendação do projeto.
- Atenção à documentação: README do Core menciona PostgreSQL, enquanto setup.md atualizado documenta self-hosted journal local sem banco. Para implementação, resolver a configuração conforme versão/commit efetivamente implantado; não pressupor equivalência de documentação.
- Nenhum instalador/binário foi executado, nem houve teste de ambiente, supply-chain scan integral, threat model independente ou auditoria de código completa. CAUTION não equivale a endosso de segurança para produção.

## Prova de valor incremental
**Should trigger**: usuário pergunta como operar agentes de programação em uma VM privada com sessões retomáveis, desktop local e migração para cloud. Consultar Cloudroom como opção técnica atual e comparar com alternativas, sem pressupor instalação.

**Near miss**: usuário pede para melhorar um prompt, escrever uma skill, criar um site ou automatizar tarefa nativa do ChatGPT. Não carregar Cloudroom nem fingir que sua infraestrutura existe.

## Resultado
Nenhuma nova skill, stack ou rota no índice. Manter ambos como referências técnicas externas. Só reavaliar adoção se houver demanda de integração ou operação efetiva do runtime, mediante validação de permissões, isolamento, identidade, storage, custos e recuperação.
