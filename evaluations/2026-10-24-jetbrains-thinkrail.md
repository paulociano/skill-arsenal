# Avaliação — JetBrains/thinkrail (2026-10-24)

- **Origem:** https://github.com/JetBrains/thinkrail (branch main; README, goal-and-requirements.md, pi-compatibility.md e install.ps1).
- **Arsenal:** https://github.com/paulociano/skill-arsenal; router `ARSENAL INDEX.md`.
- **Classificação:** D (IDE/runtime especializado) + B (metodologia portátil de specs vivas, revisões e isolamento).
- **Decisão:** UPDATE_EXISTING em `skills/repository-evidence-docs/SKILL.md` para living specs rastreáveis, atualização seletiva, link entre spec, diff e testes. KEEP_EXTERNAL_REFERENCE para IDE, agent pi, `spec_*`, sessões paralelas visuais e extensões próprias. Sem nova skill ou stack.
- **Sobreposição:** `coding-agent-engineering` já aborda loop orient→edit→test→verify, contratos, Git e estado de sessão; `software-factory-operations` já aborda worktrees, verificador independente e PR. `repository-evidence-docs` já cobre evidência, grafo de documentação e sync incremental. Ganho incremental: a spec de intenção aprovada passa a ser mantida junto ao código e reconciliada explicitamente contra comportamento implementado com tríade spec→diff→teste.
- **Portabilidade:** processo Markdown independente de pi e ThinkRail; não declara ferramentas spec_*, IDE, shell, daemon nem git worktree local disponível no ChatGPT.
- **Segurança:** CAUTION para instalação/execução do produto. `install.ps1` sugere baixar script remoto via `irm | iex`, baixar releases e verificar SHA-256; modifica PATH do usuário. README documenta executáveis desktop e CLI, providers/auth, MCP e scripts de instalação. Código, binaries e cadeia completa de distribuição não foram auditados; nenhum instalador ou binário foi executado. Preferir artefato versionado com checksum confirmado e permissões limitadas. Conexão de repositórios e MCP tem superfície de prompt injection, execução e credenciais; aprovações humanas e trust boundary permanecem obrigatórios.
- **Critério should-trigger:** múltiplas sessões ou agentes com divergências entre intenção aprovada, documentação e código.
- **Near-miss:** mudança textual trivial não precisa criar SPEC.md ou grafo.
- **Verificação desejada:** rastrear requisito validado até diff e teste; inspeção pós-escrita da skill e avaliação.
- **Implementação:** `skills/repository-evidence-docs/SKILL.md`, commit `993b39cb4cc83c7f7510957289737719b9f98d86`. Índice permanece correto porque owner/description não mudaram.
