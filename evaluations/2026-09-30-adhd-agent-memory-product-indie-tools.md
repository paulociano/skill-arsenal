# Avaliação em lote — ADHD output, agent runtimes, product analytics, memory e indie tools

Data: 2026-09-30

## Escopo

Fontes:
- https://github.com/ayghri/i-have-adhd
- https://github.com/herdrdev/herdr
- https://github.com/PostHog/posthog
- https://github.com/akitaonrails/ai-memory
- https://github.com/iAmCorey/Wake
- https://github.com/iamcorey/kooky
- https://github.com/iamcorey/birth
- https://magicbox.tools/
- https://showmethe.codes/
- https://github.com/iAmCorey/awesome-indie-hacker-tools

Fluxo aplicado: `arsenal-autopilot`.

Nenhum installer, daemon, hook, MCP externo, binário, aplicativo desktop ou serviço de terceiros foi executado.

## Resumo

| Fonte | Classe | Decisão | Owner |
| --- | --- | --- | --- |
| ayghri/i-have-adhd | B | KEEP/ALREADY_ABSORBED | `writing-quality` + critérios em `llm-observability-evaluation` |
| herdrdev/herdr | B/D | KEEP_EXTERNAL_REFERENCE | `multi-agent-orchestration` / `graph-engineering` |
| PostHog/posthog | B/D | KEEP_EXTERNAL_REFERENCE | `product-metrics-diagnostics`, `experiment-design`, `llm-observability-evaluation` |
| akitaonrails/ai-memory | A/B/D | UPDATE_EXISTING | `session-learn` + `handoff` |
| iAmCorey/Wake | B/D | KEEP_EXTERNAL_REFERENCE | `handoff`, `repository-evidence-docs` |
| iAmCorey/kooky | D/B | KEEP_EXTERNAL_REFERENCE | `multi-agent-orchestration` / runtime tooling |
| iAmCorey/birth | D/B | KEEP_EXTERNAL_REFERENCE | security/runtime reference only |
| magicbox.tools | C/D | KEEP_EXTERNAL_REFERENCE | discovery catalog only |
| showmethe.codes | C/D | KEEP_EXTERNAL_REFERENCE | discovery/reference only |
| iAmCorey/awesome-indie-hacker-tools | C/B | KEEP_EXTERNAL_REFERENCE | discovery catalog only |

## Decisões

### i-have-adhd
Já havia avaliação canônica em 2026-09-21. A metodologia de ação primeiro, passos pequenos, estado visível e redução de tangentes já foi absorvida em owners existentes. Não criar modo clínico, não inferir diagnóstico e não ativar persistência global por interesse na fonte.

### Herdr
Já havia sido avaliado e reavaliado. Continua sendo runtime técnico útil como referência para sessões persistentes, panes, remote machines e status de agentes, mas não acrescenta owner novo ao Arsenal.

### PostHog
É plataforma de produto/analytics, não skill. O valor metodológico está em instrumentação, replay, experimentos, feature flags, error tracking e self-driving workflows, mas esses conceitos já têm owners no Arsenal. Não importar produto, SDKs ou infraestrutura como se fossem capacidades nativas.

### ai-memory
É a fonte com maior ganho incremental deste lote. O padrão mais útil é memória durável com:
- fonte de verdade humana e versionável;
- índices derivados/reconstruíveis;
- handoff explícito;
- provenance e temporalidade;
- compactação reversível;
- contradições sinalizadas;
- retenção influenciada por uso sem apagar a fonte.

Esse ganho foi incorporado em `session-learn` como contrato metodológico, sem importar o servidor, hooks, MCP, daemon, storage ou claims de benchmark.

### Wake
Boa referência para busca read-only sobre históricos de múltiplos agentes e retomada de sessões. A implementação depende de app desktop, filesystem local, SQLite/FTS, MCP e formatos específicos de agentes. O padrão de continuidade já está coberto por `handoff` e `session-learn`.

### Kooky
É terminal/IDE operacional para múltiplos agentes. Tem boas ideias de status unificado, resume, workspace state e command surface, mas depende de runtime macOS/terminal/socket. Mantido como referência técnica.

### Birth
Ferramenta macOS de auditoria de startup items. O valor é principalmente produto/runtime: least privilege, provenance por code signing, backup antes de remoção e graceful permission degradation. Não justifica skill genérica nova.

### Magicbox.tools e ShowMeThe.codes
As URLs fornecidas são sites, não repositórios GitHub canônicos resolvidos pelo conector nesta avaliação. Sem fonte canônica de código/documentação, ficam como referências externas apenas. Não foram usados para criar metodologia nova.

### awesome-indie-hacker-tools
Catálogo amplo de ferramentas. Útil como radar de discovery, mas rankings/listas não são evidência de qualidade nem substituem avaliação da fonte original. Não importar catálogo para o Arsenal.

## Mudança aplicada

- UPDATE `skills/session-learn/SKILL.md` com arquitetura de memória: fonte canônica humana/versionável, índices derivados, handoffs explícitos, compactação reversível, contradições e retenção orientada por uso.

## Segurança e portabilidade

- Nenhum installer ou runtime externo foi executado.
- Claims de benchmark/performance não foram reproduzidos.
- Apps desktop, hooks, MCPs, daemons, servidores e SDKs permanecem dependências externas.
- Catálogos são tratados como discovery, não autoridade.
- Interesse em i-have-adhd não implica qualquer atributo de saúde do usuário.

## Conclusão

Nenhuma nova skill foi criada. O lote produziu uma melhoria material em `session-learn`; o restante foi deduplicado contra owners existentes ou mantido como referência técnica/discovery.
