---
name: unity-game-engineering
description: "Implementar e revisar jogos Unity com grounding de versão, render pipeline, packages, scenes/prefabs, MonoBehaviour/ScriptableObject/ECS, física, 2D/3D e validação no Editor/runtime."
---

# Unity Game Engineering

## Objetivo

Operar projetos Unity com decisões ancoradas na versão real do Editor, render pipeline e packages instalados, evitando receitas de outra geração da engine.

## Trigger

Use quando o projeto é Unity e a tarefa envolve gameplay, scenes, prefabs, ScriptableObjects, 2D/3D, physics, navigation, UI, packages, build ou runtime behavior.

## Grounding obrigatório

Antes de alterar código ou assets relevantes, determinar quando possível:
- Unity Editor version;
- URP / HDRP / Built-in;
- package versions;
- target platform;
- old/new Input System;
- GameObject/MonoBehaviour versus Entities/DOTS;
- scene(s) afetadas.

Se a versão estiver ausente e a decisão depender dela, consultar projeto/docs atuais via `library-version-grounding`.

## Workflow

1. **Inspect project**
   - `ProjectSettings/ProjectVersion.txt`;
   - `Packages/manifest.json` e lock equivalente;
   - render pipeline assets;
   - assembly definitions quando relevantes;
   - scene/prefab ownership.

2. **Choose Unity representation**
   - MonoBehaviour/Component para comportamento local e authoring convencional;
   - ScriptableObject para dados/configuração e, com cautela, channels/delegate objects/runtime sets;
   - Entities/DOTS somente quando escala/performance/data-oriented architecture justificarem.

3. **Scenes and prefabs**
   - cenas coordenam composição, não devem virar depósitos de lógica;
   - prefab variants apenas quando representam variação real;
   - alterações a prefab/scene precisam respeitar serialized references;
   - assets e seus `.meta` pertencem juntos ao source control.

4. **ScriptableObject patterns**
   - separar dados estáticos de runtime state;
   - event channels reduzem coupling quando há produtores/consumidores independentes;
   - runtime sets podem substituir buscas globais/singletons em alguns casos;
   - não usar ScriptableObject só para evitar uma classe comum.

5. **Update loops**
   - `Update` para input/presentation;
   - `FixedUpdate` para physics-driven operations quando aplicável;
   - `LateUpdate` para follow/camera quando a ordem justificar;
   - coroutines/async/jobs não substituem entendimento do lifecycle.

6. **Physics**
   - detectar 2D versus 3D;
   - não misturar APIs Physics2D/Physics;
   - declarar Rigidbody ownership;
   - layers/masks;
   - continuous/discrete collision conforme velocidade/risco;
   - validar behavior em Play Mode.

7. **2D**
   - pipeline correto;
   - PPU consistente;
   - point filtering apenas para pixel art;
   - Pixel Perfect Camera depende do pipeline;
   - tilemap/palette/atlas devem refletir o workflow de level authoring e build.

8. **3D**
   - escala física coerente;
   - character controller versus Rigidbody explícito;
   - NavMesh/AI navigation configurados por package/version;
   - materiais/shaders coerentes com URP/HDRP/Built-in.

9. **Packages**
   - não adivinhar package id/version;
   - preferir Package Manager/API oficial;
   - não editar manifest manualmente quando o workflow oficial resolver;
   - verificar compatibilidade com Editor version.

10. **Editor tooling**
    - custom inspectors/windows somente quando reduzem erro ou custo recorrente de authoring;
    - preferir serialized properties/data binding a duplicar estado;
    - tooling deve validar input antes de modificar assets/scenes;
    - operações em lote precisam de preview/dry-run quando destrutivas;
    - diagnostics/auditors devem separar finding observado de recomendação;
    - editor-only code não pode vazar para player build.

11. **Validate**
    - compile;
    - Editor Console;
    - Play Mode behavior;
    - scene reload;
    - prefab/serialized references;
    - screenshot/frame apenas como evidência visual complementar;
    - build/player quando a mudança depender da plataforma.

## Render pipeline guardrail

URP, HDRP e Built-in não são variantes cosméticas. Components, shader names, renderer features e post-processing diferem.

Antes de escrever material/shader/camera code:
1. detectar pipeline;
2. confirmar package/version;
3. usar API daquele pipeline;
4. tratar shader/component ausente como erro, não como fallback silencioso.

## DOTS/ECS

Quando Entities for escolhido:
- separar components como dados;
- systems operam queries explícitas;
- jobs/Burst entram por ganho mensurável;
- baking/conversion fazem parte do authoring contract;
- medir antes/depois;
- não portar arquitetura GameObject para ECS apenas trocando nomes.

## Source control

- nunca versionar Library/Temp/obj/build caches;
- incluir `.meta`;
- Git LFS ou VCS adequado quando assets binários grandes justificarem;
- migrations de project/package devem ser commits identificáveis e reversíveis.

## Regras

- branch/sample de outra versão não é documentação da versão do projeto;
- tutorial antigo é evidência histórica, não API atual;
- não usar `OnGUI` como default para HUD moderno;
- não assumir que Editor success equivale a player build success;
- não instalar package/render pipeline redundante sobre template sem verificar.

## Integração

Combina com `game-development-engineering`, `game-networking-engineering`, `game-performance-engineering`, `game-input-engineering`, `game-ui-accessibility-engineering`, `game-testing-quality-engineering`, `game-build-release-engineering`, `shader-graphics-engineering`, `sprite-sheet-pipeline`, `library-version-grounding`, `diagnosing-bugs` e `tdd`.

## Provenance

Adaptada principalmente de `Unity-Technologies/skills`, `PhysicsExamples2D`, `PaddleGameSO`, `EntityComponentSystemSamples`, `ECS-Network-Racing-Sample`, `2d-animation-samples`, `UnityPlayground`, `open-project-1`, `UI Toolkit Manual Code Examples`, `ProjectAuditor` e `UnityCsReference`. O Arsenal absorve metodologia e guardrails, não presume Unity CLI, Editor automation ou packages externos disponíveis nesta conversa.
