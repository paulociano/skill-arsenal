# Avaliação — cathrynlavery/diagram-design + zazencodes/zazencodes-season-3

Data: 2026-10-02

## Fontes

- https://github.com/cathrynlavery/diagram-design
- https://github.com/zazencodes/zazencodes-season-3

## Escopo

Lote avaliado pelo fluxo `arsenal-autopilot`, comparando capabilities com owners canônicos existentes no Skill Arsenal. Nenhum installer, setup, script ou binário das fontes externas foi executado.

---

## 1. cathrynlavery/diagram-design

### O que faz de verdade

Fornece uma skill de geração de diagramas editoriais em HTML/SVG, com grande catálogo de gramáticas visuais, seleção por significado, regras de densidade, static-first, brand matching por tokens semânticos, import/redraw de formatos como Mermaid/draw.io/Excalidraw e referências específicas por tipo.

### Capabilities úteis

- selecionar padrão semântico antes da gramática visual;
- escolher o menor artefato visual que realmente melhora a compreensão;
- reduzir nodes/edges e tratar complexidade excessiva como sinal para dividir overview + detalhe;
- reservar accent color para poucos focos;
- mapear identidade visual para papéis semânticos;
- preservar topologia/semântica ao redesenhar diagramas de outros formatos;
- manter significado essencial no frame estático e usar motion apenas quando necessário.

### Overlap no Arsenal

Owner principal: `architecture-visualization`.

Owners adjacentes:
- `interactive-system-diagram`;
- `visual-composition-fundamentals`;
- `editable-visual-design`;
- `ui-motion-design`.

A fonte é mais ampla que `architecture-visualization`, mas criar uma nova skill geral `diagram-design` geraria forte sobreposição de routing. O ganho incremental mais seguro é absorver a disciplina editorial no owner técnico já existente.

### Classificação

**A/D** — metodologia forte e claramente útil; implementação original inclui plugins, scripts, onboarding por rede e comandos específicos de vários hosts.

### Decisão

**UPDATE_EXISTING** em `skills/architecture-visualization/SKILL.md`.

Absorvido:
- semantic pattern before layout;
- orçamento de complexidade;
- deletion-first;
- static-first;
- brand tokens por papéis semânticos;
- preservação semântica ao redesenhar fontes externas.

Não absorvido:
- installers/marketplaces;
- scripts auxiliares;
- comandos específicos de Claude Code, Codex, Pi, Kiro, OpenCode etc.;
- persistência própria de profiles;
- catálogo completo de 42 tipos como contrato obrigatório.

### Segurança e portabilidade

Riscos principais da fonte:
- instalação de plugins/marketplaces;
- scripts locais;
- fetch de websites para onboarding;
- persistência de profiles e arquivos de configuração;
- integrações específicas de harness.

Adaptação no Arsenal mantém apenas metodologia textual e usa ferramentas reais disponíveis no ambiente. Nenhuma execução da fonte foi necessária.

---

## 2. zazencodes/zazencodes-season-3

### O que faz de verdade

É um repositório de código-fonte para vídeos e demos. Não é uma coleção homogênea de skills. Inclui agentes, apps, MCP UI, infraestrutura, exemplos cross-platform e experimentos de criação de skills.

### Triagem

Foram aprofundados os candidatos com novidade plausível para o Arsenal:

1. `src/dry-run-workflow-for-agent-skills`
2. `src/cross-platform-agent-skills`
3. `src/agent-md-effectiveness`

Os demais diretórios são majoritariamente demos de aplicações, integrações, modelos ou infraestrutura e não justificam importação automática como skills.

### 2.1 Dry-run workflow for agent skills

Capability útil:
- observar uma execução controlada antes de formalizar a skill;
- capturar passos, decisões, falhas e approvals reais;
- separar detalhes incidentais de invariantes;
- reexecutar com a candidate skill para comparar comportamento.

Overlap:
- `skill-builder` já cobre extração, portabilidade, testes e prova incremental, mas não explicitava com clareza a etapa de dry-run anterior à codificação.

Classificação: **B**.

Decisão: **UPDATE_EXISTING** em `skills/skill-builder/SKILL.md`.

### 2.2 Cross-platform agent skills

Capability:
- uma skill canônica com adapters/paths específicos por harness;
- scopes de projeto vs usuário;
- invocação explícita vs implícita.

Overlap:
- `project-skill-architecture` já possui owner canônico, adapters, distribuições derivadas, audiências e separação por harness.

Classificação: **B/C**.

Decisão: **KEEP_EXTERNAL_REFERENCE**. Nenhuma nova skill ou mudança necessária.

### 2.3 AGENTS.md / CLAUDE.md effectiveness

O material presente no repositório é pequeno e aponta para discussão/pesquisa, mas não contém evidência suficiente no próprio diretório para justificar uma nova capability operacional.

Classificação: **C** no estado atual da fonte inspecionada.

Decisão: **REJECT como nova skill**. O Arsenal já trata arquivos de contexto como shells/adapters em `project-skill-architecture`.

### Segurança e portabilidade

O repositório contém múltiplas demos com:
- serviços externos;
- SDKs;
- agentes;
- possíveis credenciais;
- deploys;
- scripts e aplicações executáveis.

Nenhum código foi executado. Foram absorvidas apenas metodologias textuais portáveis.

---

## Mudanças publicadas

- `architecture-visualization`: adicionada disciplina editorial de seleção semântica, complexidade, deletion-first, static-first, brand roles e redraw semântico.
- `skill-builder`: adicionado fluxo de dry-run antes de codificar workflows.

Nenhuma nova skill foi criada.

`ARSENAL INDEX.md` não precisou de mudança porque nomes e descriptions roteáveis permanecem válidos.

## Limites da validação

- avaliação baseada no estado atual das branches default em 2026-10-02;
- não houve execução de scripts, installers ou demos externas;
- não foi feita validação visual completa de todos os templates do `diagram-design`;
- o repositório Zazen foi tratado como ecossistema/radar e apenas candidatos com novidade plausível foram aprofundados.
