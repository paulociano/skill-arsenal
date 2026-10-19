# Avaliação de cinco fontes externas (2026-10-19)

## Escopo, autoridade e política
- Arsenal canônico: https://github.com/paulociano/skill-arsenal, branch `master`; consulta inicial a `ARSENAL INDEX.md`, `AGENTS.md`, `stacks/arsenal-autopilot/STACK.md` e `stacks/evaluate-and-import-skill/STACK.md`.
- Fontes originais na branch `main`, descobertas por README, árvore de arquivos e arquivos candidatos concretos.
- Método: avaliação por capability, não por nome de repositório; importação seletiva. Não foram executados installers, scripts de terceiros ou automações com credenciais.
- A revisão é seletiva e **não** corresponde à auditoria integral de todas as 177 skills científicas ou de todos os links do catálogo de personas.

## Decisões por fonte

### 1. K-Dense-AI/scientific-agent-skills — A/D, adotar método específico
Origem: https://github.com/K-Dense-AI/scientific-agent-skills; README e `skills/experimental-design/SKILL.md`.
- Valor: projeto de estudos antes da coleta com unidade experimental, randomização, blocking, factorial DOE, crossover, pseudorreplicação e plano reproduzível.
- Overlap: `experiment-design` do Arsenal tratava mais diretamente de experiências A/B em produto; complementar sem duplicar owner.
- Decisão: **UPDATE_EXISTING** em `skills/experiment-design/SKILL.md` com ramo de experimento científico. Não copiar `pydoe`, scripts ou as 177 skills.
- Dependências: Python, bibliotecas e bases especializadas não presumidas; análises clínicas, biomédicas e laboratoriais requerem domínio, validação e supervisão próprios.
- Não adotado: coleção integral e workflows científicos sem demanda/ambiente comprovado. Referência externa para futuras tarefas especializadas.

### 2. humanlayer/skills — A/B/D, adotar seletivamente
Origem: https://github.com/humanlayer/skills; README; `plugins/rpi/skills/rpi/SKILL.md`, `plugins/design-control-loop/skills/design-control-loop/SKILL.md`, `plugins/show-me/skills/show-me/SKILL.md`, `plugins/visual-pr/skills/visual-pr/SKILL.md`.
- Valor: RPI persistente, separação discovery/design/implementation, documentos por fase e feedback loops set point/sensor/controller/actuator, dampeners e revisão humana.
- Decisão: **UPDATE_EXISTING** `skills/project-planning/SKILL.md` e `skills/software-factory-operations/SKILL.md`.
- `show-me` e `visual-pr`: **KEEP_EXTERNAL_REFERENCE**; formas de explicação/diff/PR já cabem em handoff e tooling atual, sem evidência para skill separada.
- `improve-claude-md`: específico do Claude; `narrow-react-prop-types`: tarefa estreita; iterated loop: sobreposto à software factory e dependente de runner. Não instalados.
- Risco: CI agendado, token de GitHub e CLI headless não são presumidos.

### 3. agentskills/agentskills — A/B, norma incorporada
Origem: https://github.com/agentskills/agentskills; `docs/specification.mdx`.
- Valor: contrato aberto de SKILL.md, metadata, comprimento/slug, compatibilidade, ferramentas opcionais experimentais e progressive disclosure.
- Decisão: **UPDATE_EXISTING** `skills/skill-builder/SKILL.md` com gate de portabilidade e conformidade; **não** criar um novo owner.
- Limites: esquema é formato, não garantia de suporte do host; stacks permanecem convenção local.

### 4. tmstack/awesome-persona-skills — B/C/D, referência externa
Origem: https://github.com/tmstack/awesome-persona-skills; README.
- É um diretório de links externos e simulações de pessoas, não uma skill operacional unificada; exemplos incluem figuras públicas, escritores, colegas, familiares e pessoas falecidas.
- Decisão: **KEEP_EXTERNAL_REFERENCE** como radar de metodologias, não importar personas nem scripts. Catálogo sozinho não demonstra valor incremental.
- Riscos: privacidade, consentimento, direitos de personalidade, material sensível e falsas atribuições de opiniões a pessoas reais. Avaliar repositório de origem individualmente antes de futura adoção.

### 5. ibelick/ui-skills — A/B/D, adotar métodos de QA
Origem: https://github.com/ibelick/ui-skills; README; `skills/baseline-ui/SKILL.md`, `skills/improve-ui/SKILL.md`, `skills/create-design-md/SKILL.md`, `skills/fixing-motion-performance/SKILL.md`, `skills/component-canvas/SKILL.md`.
- Valor: finding com prova de contrato/runtime/fix e contraevidência, reconstrução de design existente sem inventar direção, diagnóstico de jank por layout/paint/composite.
- Decisão: **UPDATE_EXISTING** em `skills/design-principles-audit/SKILL.md`, `skills/design-system-extraction/SKILL.md` e `skills/ui-motion-design/SKILL.md`.
- Não adotado: `baseline-ui` como proibição universal de gradientes, motion ou libs; prescrições absolutas podem conflitar com marca, UX ou implementação. `component-canvas` fica como **KEEP_EXTERNAL_REFERENCE** para futura demanda real, sem duplicar stack de web-app.
- Risco: npm CLI, MCP remoto, OAuth e Cloudflare runtime não necessários para absorção do método, por isso não foram instalados/conectados.

## Ledger resumido de ownership
| Capability | Owner canônico | Ação |
| --- | --- | --- |
| DOE, pseudorreplicação e randomização antes da coleta | experiment-design | UPDATE_EXISTING |
| RPI por fases e handoffs versionados | project-planning | UPDATE_EXISTING |
| Controle incremental mensurável da software factory | software-factory-operations | UPDATE_EXISTING |
| Conformidade open Agent Skills | skill-builder | UPDATE_EXISTING |
| Contrato e verificação de design visual | design-system-extraction; design-principles-audit | UPDATE_EXISTING |
| Diagnóstico técnico de motion/jank | ui-motion-design | UPDATE_EXISTING |
| Personas derivadas de pessoas reais | sem owner novo | KEEP_EXTERNAL_REFERENCE |
| Canvas de componentes e PR visual | owners existentes suficientes para o escopo | KEEP_EXTERNAL_REFERENCE |

## Alterações publicadas e verificação
Arquivos alterados na branch canônica:
- `skills/ui-motion-design/SKILL.md`
- `skills/design-system-extraction/SKILL.md`
- `skills/design-principles-audit/SKILL.md`
- `skills/experiment-design/SKILL.md`
- `skills/skill-builder/SKILL.md`
- `skills/project-planning/SKILL.md`
- `skills/software-factory-operations/SKILL.md`
- Este arquivo de avaliação.

Nenhum owner novo ou description de frontmatter alterada; `ARSENAL INDEX.md` não exigiu atualização. Escritas realizadas via GitHub Contents API na branch canônica, com SHA original de cada arquivo, sem force-push.

## Segurança, portabilidade e limites da validação
- Nenhuma dependência de terceiros executada; nenhuma instalação em projetos consumidores; nenhuma credencial coletada; nenhuma importação em massa.
- Conteúdo de repositórios externos tratado como documentação não confiável, não como autorização para executar ações.
- A absorção foi metodológica; não certifica compatibilidade das ferramentas originais ou valida a precisão de experimentos específicos.
- Confirmar em leituras pós-escrita o conteúdo remoto e a avaliação. Os commits pertencem à sequência de commits de alteração, sem squashing.
