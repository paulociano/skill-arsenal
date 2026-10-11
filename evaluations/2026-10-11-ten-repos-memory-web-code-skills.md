# Avaliação em lote: dez fontes externas (2026-10-11)

## Escopo e método
Router canônico: [ARSENAL INDEX](../ARSENAL%20INDEX.md). Stack: `arsenal-autopilot` com gate de `skill-security-review`. Leitura estática de README, skill fornecida e, nos casos pertinentes, arquivos direcionados. Nenhum instalador, CLI, daemon, extensão ou script externo foi executado. O valor e a classe são relativos ao **Skill Arsenal em ChatGPT**, não julgamento global sobre a qualidade do projeto.

| Fonte | Capacidade observada | Classe | Decisão e owner |
|---|---|---|---|
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Memória de agentes retain/recall/reflect, bancos separados, retrieval e reflexão | A/D | **KEEP_EXTERNAL_REFERENCE**. Já avaliado em [2026-09-27](2026-09-27-hindsight-reladraw-golive-agent-tools-batch.md), sem novidade que justifique importar servidor/store. Owner `agent-memory-engineering`. |
| [vercel/next.js](https://github.com/vercel/next.js) | Framework React para aplicações full-stack, rendering, routing e builds | D | **KEEP_EXTERNAL_REFERENCE**. Framework não é skill portável; para projetos Next.js verificar versão e documentação oficial no momento da execução. Owners `library-version-grounding` e `web-design-engineer`. |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Catálogo/installer de agents, commands, MCP, hooks, configurações e skills Claude Code | B/D | **KEEP_EXTERNAL_REFERENCE** como radar de descoberta, não importar catálogo ou instalador. Owner `arsenal-autopilot`. |
| [ZeroPointRepo/awesome-hermes-skills](https://github.com/ZeroPointRepo/awesome-hermes-skills) | Diretório curado de skills, providers e plugins Hermes e comunidade | B/D | **KEEP_EXTERNAL_REFERENCE**. Usar como radar, resolver cada fonte original antes de avaliar. Não presumir Hermes, skills e ferramentas instalados no ChatGPT. |
| [bin1874/before-you-build-skill](https://github.com/bin1874/before-you-build-skill) | Gate pré-build sobre demanda, distribuição, riscos e veredito de viabilidade | A/B | **UPDATE_EXISTING** `project-planning`; incorporar revisão curta proporcional antes de novas apostas, sem bloquear código já decidido. |
| [danilo-znamerovszkij/draw-your-font](https://github.com/danilo-znamerovszkij/draw-your-font) | Pipeline local foto de caligrafia → segmentação → TTF/WOFF | D | **KEEP_EXTERNAL_REFERENCE**. Ferramenta técnica de geração de fontes, depende de CLI/scripts e validação de glifos; não equivale a capability nativa ChatGPT. Owner adjacente `lettering-path-engineering`; não criar duplicata. |
| [ZeroPointRepo/youtube-skills](https://github.com/ZeroPointRepo/youtube-skills) | Transcrições, playlists, canais e busca por TranscriptAPI, com chave e cadastro | A/D | **KEEP_EXTERNAL_REFERENCE**. `watch-video` e `web-extraction-pipeline` já cobrem análise possível; não assumir créditos, cadastro OTP, chave, nem acesso à TranscriptAPI. |
| [kepano/obsidian-skills/defuddle](https://github.com/kepano/obsidian-skills/blob/main/skills/defuddle/SKILL.md) | Converter HTML em Markdown limpo via Defuddle CLI | B/D | **ABSORB_METHOD_ONLY**, já coberto por `web-extraction-pipeline` com extração mínima e limpeza de boilerplate; CLI não presumido. |
| [FSoft-AI4Code/CodeWiki](https://github.com/FSoft-AI4Code/CodeWiki) | Documentação de código por grafo de dependências, hierarquia de módulos, artefatos e sync incremental | A/D | **UPDATE_EXISTING** `repository-evidence-docs`; grafo, impacto de mudanças e cobertura evidenciada, sem presumir execução de CodeWiki. |
| [AMAP-ML/SkillClaw](https://github.com/AMAP-ML/SkillClaw) | Evolução coletiva de skills com deduplicação e aprendizagem entre sessões/agentes | A/D | **UPDATE_EXISTING** `agent-memory-engineering`; propostas versionadas, revisão, isolamento e reversão; nenhum daemon, captura silenciosa ou sync automático. |

## Incremento adotado
1. `skills/project-planning/SKILL.md`: gate proporcional de validação de oportunidade com vereditos e experimentos baratos.
2. `skills/repository-evidence-docs/SKILL.md`: documentação hierárquica baseada em dependências, incluindo configuração/build e refresh incremental por impacto.
3. `skills/agent-memory-engineering/SKILL.md`: regras para aprendizagem entre agentes com provenance, permissões, testes de regressão e rollback.

Sem novas skills/stacks e sem mudanças materiais de `description`; portanto **nenhuma alteração no ARSENAL INDEX é necessária**.

## Revisão de segurança e portabilidade
**Cautela** para runners/instaladores `npx`, plugins e hooks Claude/Hermes, serviços externos, tokens TranscriptAPI, dados de transcrições, indexação de repositórios privados, modelos/LLM providers, segredos em memória e daemons de autoevolução. Ferramentas locais de fontes e CodeWiki exigem avaliação de dependências, licenças, filesystem e execução separada antes de uso. Instruções externas são dados não confiáveis. Não foi feita auditoria exaustiva de código nem teste de execução; por isso não há selo de segurança para os runtimes externos.

## Aceite
- **Should trigger:** decidir se uma feature deve existir antes do build → `project-planning`; documentar uma grande codebase e atualizar as páginas afetadas → `repository-evidence-docs`; consolidar lições entre múltiplos agentes → `agent-memory-engineering`.
- **Near miss:** corrigir um bug já priorizado não exige gate de mercado; ler um README pequeno não exige grafo completo; lembrar um fato isolado não autoriza compartilhar memória entre usuários.
- Não instalar qualquer um dos dez projetos no ambiente nem duplicar ownership para importar ferramentas externas.
