# Avaliação — mattpocock/skills

Data: 2026-09-26  
Fonte: https://github.com/mattpocock/skills  
Branch avaliada: `main`

## Escopo

O repositório é um ecossistema de skills de engenharia e produtividade, não uma skill isolada. A avaliação foi conduzida via `arsenal-autopilot`, com triagem ampla pelo README e aprofundamento seletivo em capacidades com novidade plausível.

## Capacidades observadas

Principais famílias:
- grilling e refinamento de decisões;
- modelagem de domínio e ADRs;
- TDD e seams;
- debugging e code review;
- design de módulos profundos;
- prototipagem descartável orientada a perguntas;
- transformação de conversa em specs/tickets;
- wayfinding para trabalho longo;
- handoff;
- questionários assíncronos;
- escrita de documentos consumidos por agentes.

## Overlap com o Arsenal

### Já coberto materialmente
- `grilling` ↔ `deep-grill`, `quick-grill`, `idea-refine`;
- `domain-modeling` ↔ `domain-modeling`;
- `diagnosing-bugs` ↔ `diagnosing-bugs` e stack `debug-and-fix`;
- `code-review` ↔ `code-review`;
- `codebase-design` ↔ `codebase-design`;
- `handoff` ↔ `handoff`;
- `research` ↔ `research-and-synthesize` e skills de research;
- `resolving-merge-conflicts` ↔ `merge-conflict-resolution`;
- `wayfinder` tem grande overlap com `project-planning`, `graph-engineering`, `project-complexity-management` e `loop-engineering`.

Decisão: não duplicar owners.

## Valor incremental identificado

### 1. Questionário de decisão para conhecimento externo
A skill `to-questionnaire` contém um mecanismo nítido que não estava representado como owner dedicado: entrevistar o usuário apenas sobre o envio e a lacuna, e produzir perguntas para a pessoa que detém o conhecimento ausente.

**Classificação: A**  
**Ação: CREATE_NEW** como `decision-questionnaire`.

Ganho demonstrável:
- deveria ativar quando uma decisão depende do conhecimento de um terceiro;
- não deveria ativar para pesquisa pública ou para decisões que o próprio usuário consegue responder;
- sucesso é mensurável pela cobertura entre outputs necessários e perguntas.

### 2. Protótipo descartável como instrumento de decisão
A skill `prototype` separa explicitamente perguntas de lógica/estado e perguntas de UI e trata o protótipo como artefato descartável que responde uma pergunta.

**Classificação: B/A parcial**  
**Ação: KEEP_EXTERNAL_REFERENCE / futura absorção no owner adequado**.

O Arsenal já possui várias capacidades de prototipagem e web engineering. Criar um novo owner agora aumentaria overlap. O padrão "question-first prototype" deve ser considerado em futuras revisões de skills de prototipagem.

### 3. Escrita para agentes
`writing-for-agents` traz bons conceitos de context pointers, progressive disclosure, completion criteria e redução de duplicação.

**Classificação: B**  
**Ação: ABSORB_METHOD_ONLY**.

Há overlap forte com `directional-prompting`, `functional-skill-architecture`, `project-skill-architecture`, `skill-builder` e o próprio Autopilot. Não justifica owner novo neste lote.

### 4. TDD orientado a seams e tracer bullets
`tdd` reforça teste por interface pública, seams pré-acordados e ciclos verticais pequenos.

**Classificação: B**  
**Ação: KEEP_EXTERNAL_REFERENCE**.

O Arsenal já possui `experiment-design`, `behavior-contract-validation`, debugging e revisão, mas não foi encontrada evidência suficiente neste lote para alterar um owner sem abrir e reconciliar toda a skill canônica de TDD/implementação existente. Evitado update especulativo.

## Segurança e portabilidade

Revisão estática proporcional:
- o repositório inclui instaladores/integração para Claude Code/Codex e scripts de manutenção;
- nenhuma dessas rotas foi executada;
- comandos específicos como Skill tool, background agents, slash commands, `.claude/` e instalação via npm/plugin não foram tratados como capacidades disponíveis;
- a metodologia adotada foi reescrita em termos portáveis;
- o novo owner não exige shell, credenciais, rede, persistência ou integração externa por padrão.

Verdict: **APPROVE para absorção metodológica seletiva; CAUTION para infraestrutura/instalação original, que não foi importada.**

## Classificação global

**A/B/D misto**.

- A: alguns workflows produzem mudança real de comportamento;
- B: boa parte da novidade é metodológica e deve enriquecer owners existentes;
- D: empacotamento, plugins, scripts e convenções dependem de runtimes externos.

## Decisão

Adotar apenas `decision-questionnaire` como nova skill neste lote. Não importar o catálogo completo. Registrar prototipagem orientada a pergunta e escrita para agentes como referências úteis para futuras evoluções de owners existentes.

## Limites da avaliação

A triagem não abriu cada `SKILL.md` do repositório. Seguindo a política de lote do Arsenal, foram aprofundadas somente candidatas com novidade plausível após leitura do README e dos buckets principais.
