---
name: game-testing-quality-engineering
description: "Projetar QA de jogos com testes de lógica, Edit/Play/runtime/device, deterministic fixtures, seed corpora, soak, save migration, input/network simulation e release gates baseados em comportamento observável."
---

# Game Testing & Quality Engineering

## Objetivo

Testar jogos nas camadas onde falhas realmente aparecem: lógica determinística, integração da engine, runtime, plataforma, persistência, rede e performance.

## Quando usar

- QA strategy;
- automated game tests;
- EditMode/PlayMode;
- regression;
- soak;
- compatibility;
- release candidate validation;
- test automation em CI.

## Test matrix

1. **Pure logic**
   - rules;
   - economy;
   - combat math;
   - generators/invariants.

2. **Engine integration**
   - scenes;
   - prefabs/resources;
   - animation/input/physics integration.

3. **Runtime/play**
   - vertical slices;
   - state transitions;
   - reload/retry.

4. **Platform/device**
   - actual build;
   - input devices;
   - permissions;
   - suspend/resume.

5. **Persistence**
   - old saves;
   - corruption;
   - migration;
   - cloud conflict.

6. **Networking**
   - lag/loss/jitter;
   - reconnect;
   - late join;
   - authority validation.

7. **Performance**
   - representative workload;
   - hitches;
   - memory growth;
   - thermal/device constraints.

## Workflow

1. Definir risco e regressões críticas.
2. Mapear comportamento para a camada mínima que consegue prová-lo.
3. Preferir testes puros para rules determinísticas.
4. Usar Play/runtime somente onde engine lifecycle importa.
5. Criar fixtures/seeds reproduzíveis.
6. Capturar logs/artifacts quando teste falhar.
7. Evitar flaky waits por tempo fixo quando uma condição observável existe.
8. Rodar focused suite antes da full suite.
9. Release candidate exige build real + smoke na plataforma alvo quando possível.
10. Falha conhecida permanece blocker explícito; não baixar threshold para “ficar verde”.

## Game-specific regression suites

Manter quando relevantes:
- save fixtures de versões anteriores;
- procedural seed corpus;
- replay/input traces;
- network simulation presets;
- benchmark scenes;
- controller/device matrix;
- localization overflow scenes.

## Soak

Para jogos long-running/live:
- hours-long session quando risco justificar;
- memory growth;
- handle/resource leaks;
- disconnect cycles;
- scene/level churn;
- server tick degradation.

## Flakiness

- seed fixa para reprodução;
- random test pode existir, mas precisa registrar seed ao falhar;
- distinguir nondeterminism legítimo de oracle fraco;
- retry não converte falha em pass sem diagnóstico.

## Regras

- compile green não prova Play Mode;
- Play Mode não prova player build;
- screenshot não prova state;
- coverage percentual não substitui risk coverage;
- teste automatizado pode complementar, não eliminar playtesting humano para feel/usability.

## Integração

`tdd`, `behavior-contract-validation`, `game-development-engineering`, `game-networking-engineering`, `game-performance-engineering`, `save-game-persistence-engineering` e `game-build-release-engineering`.

## Provenance

Consolidada do Unity Test Framework, GameCI Unity Test Runner e padrões de tests/samples do Unity Input System. Preserva Edit/Play separation, CI artifacts e target-build validation sem exigir GameCI ou Unity.
