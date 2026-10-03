---
name: narrative-dialogue-engineering
description: "Projetar e integrar narrativa interativa e diálogos com nodes/choices, variables, conditions, commands, localization, save-state, validation de branches e separação entre conteúdo narrativo e gameplay code."
---

# Narrative & Dialogue Engineering

## Objetivo

Modelar narrativa interativa como conteúdo versionável e executável, separando escrita, state narrativo, presentation e efeitos no gameplay.

## Quando usar

- diálogos;
- branching narrative;
- quests conversacionais;
- choices/consequences;
- Ink/Yarn Spinner ou formato equivalente;
- narrative variables;
- localization;
- dialogue UI;
- narrative testing.

## Princípio central

**A narrativa emite lines, choices e commands; o jogo decide como apresentar e executar efeitos.**

## Workflow

1. Definir escopo: conversa local, quest, capítulo ou narrativa global.
2. Separar:
   - content/text;
   - narrative state;
   - conditions;
   - choices;
   - commands/events;
   - gameplay integration.
3. Usar identificadores estáveis para nodes/lines relevantes.
4. Variáveis narrativas precisam de owner e default explícitos.
5. Commands para gameplay devem passar por adapter/allowlist, não executar texto arbitrário.
6. Branches precisam convergir ou permanecer deliberadamente abertas; dead ends devem ser detectáveis.
7. Choices registram consequência e, quando necessário, persistência.
8. Save/load inclui narrative runtime state/version compatível.
9. Localization deve preservar ids/commands/tags, alterando apenas conteúdo traduzível.
10. Testar caminhos críticos e combinações de flags.

## Authoring

- texto legível por escritores;
- lógica complexa demais para o formato narrativo deve migrar para gameplay code;
- evitar duplicar a mesma regra em script narrativo e código;
- tags/metadata têm schema pequeno e documentado;
- preview/play-as-you-write é útil, mas não substitui integração real.

## Validation

Checar:
- missing target;
- unreachable node;
- choice sem destino;
- variable não inicializada;
- command desconhecido;
- localization missing;
- branch crítica sem exit;
- save format incompatível.

## Regras

- diálogo não deve conhecer scene object concreto quando um command adapter resolver;
- não usar index ordinal de choice como identidade persistente se conteúdo pode mudar;
- story state precisa de versão;
- conteúdo de usuário/mod não pode ganhar execução arbitrária via command;
- branching massivo precisa de ferramentas/telemetry de coverage.

## Integração

`game-development-engineering`, `save-game-persistence-engineering`, `game-audio-engineering`, `locale-adapter`, `domain-modeling` e `behavior-contract-validation`.

## Provenance

Consolidada de Yarn Spinner e ink/ink-unity-integration: lines, choices, commands, story state, compilação/preview e integração desacoplada. Não exige Yarn ou Ink.
