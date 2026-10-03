# Avaliação — Game Development Expansion IV: Camera, Input, UI/Accessibility, QA e Build/Release

Data: 2026-10-03

## Objetivo

Expandir a stack de game development para fechar lacunas operacionais de produção: câmera/cinematics, input/controls, UI/acessibilidade, testing/QA, build/release e editor tooling.

## Fontes avaliadas

| Repositório | Domínio | Classe | Decisão |
|---|---|---|---|
| Unity-Technologies/com.unity.cinemachine | Camera/cinematics | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| Unity-Technologies/InputSystem | Input/controls | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| Unity-Technologies/uGUI | Runtime UI | D | KEEP_EXTERNAL_REFERENCE |
| Unity-Technologies/ui-toolkit-manual-code-examples | UI/editor tooling | B/D | ABSORB_METHOD_ONLY |
| game-ci/unity-actions | CI/build | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| game-ci/unity-test-runner | Automated testing | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| needle-mirror/com.unity.test-framework | Test framework | D | KEEP_EXTERNAL_REFERENCE |
| Unity-Technologies/Addressables-Sample | Content packaging | A/D | ABSORB_METHOD_ONLY |
| Unity-Technologies/ProjectAuditor | Editor/static auditing | B/D | UPDATE_EXISTING |
| Unity-Technologies/UnityCsReference | Editor/API reference | D | KEEP_EXTERNAL_REFERENCE / UPDATE_EXISTING |
| Unity-Technologies/game-programming-patterns-demo | Architecture examples | B/D | KEEP_EXTERNAL_REFERENCE |
| Unity-Technologies/Graphics | Rendering internals | D | ROUTE_EXISTING |
| Unity-Technologies/UnityRenderStreaming | Streaming | D | KEEP_EXTERNAL_REFERENCE |

## Resultado executivo

Cinco novos owners foram materializados:

1. `game-camera-cinematics-engineering`
2. `game-input-engineering`
3. `game-ui-accessibility-engineering`
4. `game-testing-quality-engineering`
5. `game-build-release-engineering`

Além disso, `unity-game-engineering` recebeu uma seção de editor tooling em vez de criar um owner separado.

## 1. Camera & Cinematics

### Valor incremental

O owner geral de game development não cobria framing, follow/aim, camera state, blending, damping, collision/occlusion nem transições cinematográficas.

### Métodos absorvidos

De Cinemachine:
- target tracking;
- composition;
- blending/cutting;
- modular camera behavior;
- versão/package grounding.

### Decisão

Criar `game-camera-cinematics-engineering`.

## 2. Game Input

### Valor incremental

Input não é apenas ler teclado/gamepad. O domínio exige action abstraction, control schemes, rebinding, hot-swap, UI/game focus e local multiplayer.

### Métodos absorvidos

Do Unity Input System:
- actions;
- control schemes;
- custom devices;
- rebinding UI;
- on-screen controls;
- local multiplayer;
- UI versus gameplay input;
- input traces/recording.

### Decisão

Criar `game-input-engineering`.

## 3. Game UI & Accessibility

### Valor incremental

O Arsenal tinha design/UI genérico, mas game UI possui particularidades de HUD, gamepad focus, viewing distance, safe areas, subtitles, audio alternatives, camera motion e persistent accessibility preferences.

### Métodos absorvidos

De UI Toolkit/uGUI e Input System:
- runtime controls;
- binding;
- focus/navigation;
- gamepad UI;
- scalable runtime UI.

De referências metodológicas de acessibilidade em games:
- informação crítica não depender apenas de cor/som;
- remapping;
- subtitles/captions;
- reduced motion/shake;
- independent audio controls;
- motor, visual e hearing alternatives.

### Decisão

Criar `game-ui-accessibility-engineering`.

Guidelines externas são referência de design e não declaração automática de compliance.

## 4. Game Testing & Quality

### Valor incremental

`tdd` é owner de ciclos red-green, mas game QA precisa de camadas específicas: Edit/Play/runtime/device, saves antigos, procedural seeds, network simulation, performance e soak.

### Métodos absorvidos

De Unity Test Framework/GameCI:
- edit mode/play mode;
- automated test execution;
- CI artifacts;
- focused versus full suite;
- build-target validation.

### Decisão

Criar `game-testing-quality-engineering`.

## 5. Game Build & Release

### Valor incremental

`production-go-live` cobre produção de apps/infra, porém games exigem build artifacts por plataforma, signing, store packaging, asset/content catalogs e compatibilidade player/content/save.

### Métodos absorvidos

De GameCI:
- checkout/configure/license/test/build/artifact pipeline;
- platform-specific builds.

De Addressables Sample:
- asset reference ownership;
- load/release lifecycle;
- catalog/content separation;
- remote/update content concerns.

De práticas de release dos packages Unity:
- release branches/tags;
- version grounding;
- shippable release artifacts.

### Decisão

Criar `game-build-release-engineering`, integrando com `production-go-live` quando backend/infra externa também existir.

## 6. Unity Editor Tooling

### Decisão de ownership

Não criar `unity-editor-tooling-engineering` separado.

`unity-game-engineering` já é owner canônico do ambiente Unity. Ele foi atualizado com:
- custom inspectors/windows apenas quando reduzem custo recorrente;
- serialized properties/data binding;
- validation antes de mutar assets/scenes;
- preview/dry-run para batch destructivo;
- diagnostics separados de recommendation;
- editor-only code não pode vazar ao player.

Fontes:
- UI Toolkit manual examples;
- ProjectAuditor;
- UnityCsReference.

## Segurança e portabilidade

Nenhum package, runner, Unity Editor, CI workflow, build, signing key ou external binary foi executado.

Superfícies relevantes:
- Unity licensing em CI;
- signing certificates/keystores;
- store credentials;
- build secrets;
- native platform SDKs;
- remote content;
- package version drift;
- editor scripts que alteram assets;
- accessibility claims sem device testing.

Guardrails:
- secrets fora do repo/log;
- clean builds periódicos;
- artifact imutável após aprovação quando possível;
- simulator/editor não substitui device build;
- console SDKs/NDA não são inferidos de repos públicos;
- cache não é source of truth.

## Materialização

Criados:
- `skills/game-camera-cinematics-engineering/SKILL.md`
- `skills/game-input-engineering/SKILL.md`
- `skills/game-ui-accessibility-engineering/SKILL.md`
- `skills/game-testing-quality-engineering/SKILL.md`
- `skills/game-build-release-engineering/SKILL.md`

Atualizados:
- `skills/unity-game-engineering/SKILL.md`
- `stacks/game-development-cycle/STACK.md`
- `ARSENAL INDEX.md`

## Limites

- Avaliação por metadata, README, documentação e exemplos representativos.
- Nenhum build/test foi executado.
- O repo público de Addressables contém exemplos antigos e deve ser usado como metodologia, não como API atual.
- uGUI/UI Toolkit e Input System dependem da versão real do projeto.
- console release continua dependente de SDKs e documentação sob NDA.
