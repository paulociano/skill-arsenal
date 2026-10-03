# Avaliação — 30 repositórios para Game Development

Data: 2026-10-02

## Objetivo

Expandir o Skill Arsenal para desenvolvimento de jogos 2D/3D sem transformar cada engine, package ou sample em uma skill separada.

A unidade de adoção foi **capability**, não repositório.

## Fontes avaliadas

| # | Repositório | Classificação | Decisão |
|---|---|---|---|
| 1 | Unity-Technologies/skills | A/D | CREATE_NEW + ABSORB_METHOD_ONLY |
| 2 | Unity-Technologies/EntityComponentSystemSamples | A/D | UPDATE/FEED new game owners |
| 3 | Unity-Technologies/PhysicsExamples2D | B/D | ABSORB_METHOD_ONLY |
| 4 | UnityTechnologies/PaddleGameSO | B | ABSORB_METHOD_ONLY |
| 5 | UnityTechnologies/open-project-1 | B/D | KEEP_EXTERNAL_REFERENCE |
| 6 | Unity-Technologies/ECS-Network-Racing-Sample | A/D | ABSORB_METHOD_ONLY |
| 7 | Unity-Technologies/com.unity.multiplayer.samples.bitesize | A/D | ABSORB_METHOD_ONLY |
| 8 | Unity-Technologies/com.unity.netcode.gameobjects | D | KEEP_EXTERNAL_REFERENCE |
| 9 | Unity-Technologies/ml-agents | D | KEEP_EXTERNAL_REFERENCE |
| 10 | Unity-Technologies/FPSSample | B/D | KEEP_EXTERNAL_REFERENCE |
| 11 | UnityTechnologies/ShaderGraph_ExampleLibrary | B/D | ROUTE_EXISTING |
| 12 | FractalAsim/UnityShaderLib | B/D | ROUTE_EXISTING |
| 13 | TinyPlay/URPShadersCollection | B/D | ROUTE_EXISTING |
| 14 | Unity-Technologies/2d-animation-samples | B/D | KEEP_EXTERNAL_REFERENCE |
| 15 | Unity-Technologies/UnityPlayground | B/D | KEEP_EXTERNAL_REFERENCE |
| 16 | UnityTechnologies/GalacticKittens | B/D | KEEP_EXTERNAL_REFERENCE |
| 17 | Unity-Technologies/Unity.Animation.Samples | D | KEEP_EXTERNAL_REFERENCE |
| 18 | Unity-Technologies/ProjectTinySamples | C/D | REFERENCE_ONLY |
| 19 | MirrorNetworking/Mirror | A/D | ABSORB_METHOD_ONLY |
| 20 | PurrNet/PurrNet | A/D | ABSORB_METHOD_ONLY |
| 21 | unitycoder/Game-Networking-Resources | B | KEEP_EXTERNAL_REFERENCE (radar) |
| 22 | Unity-Technologies/com.unity.services.samples.use-cases | B/D | KEEP_EXTERNAL_REFERENCE |
| 23 | Unity-Technologies/arfoundation-samples | D | KEEP_EXTERNAL_REFERENCE |
| 24 | godotengine/godot-demo-projects | A/D | ABSORB_METHOD_ONLY |
| 25 | godotengine/godot | D | KEEP_EXTERNAL_REFERENCE |
| 26 | bevyengine/bevy | A/D | ABSORB_METHOD_ONLY |
| 27 | FyroxEngine/Fyrox | D | KEEP_EXTERNAL_REFERENCE |
| 28 | stride3d/stride | D | KEEP_EXTERNAL_REFERENCE |
| 29 | FlaxEngine/FlaxEngine | D | KEEP_EXTERNAL_REFERENCE |
| 30 | defold/defold | D | KEEP_EXTERNAL_REFERENCE |

## Capabilities adotadas

### 1. game-development-engineering

Novo owner engine-agnostic para:
- playable contract e vertical slice;
- player intent → simulation → state → presentation → feedback;
- clocks separados para frame, physics e network ticks;
- gameplay systems como data/config + runtime state + rules + presentation + persistence;
- trade-off scene/component/ECS;
- regras 2D e 3D;
- runtime validation e build validation.

Principais fontes:
- Godot demo projects;
- Bevy;
- Unity official samples;
- Fyrox/Stride como contraste de arquitetura.

### 2. unity-game-engineering

Novo owner Unity-specific para:
- grounding de Editor version, render pipeline e package versions;
- Scenes, Prefabs, MonoBehaviour, ScriptableObject e Entities/DOTS;
- Update/FixedUpdate/LateUpdate;
- Physics2D versus Physics3D;
- pixel-perfect e 2D import/pipeline;
- 3D controller/navigation/material pipeline;
- UPM/package discipline;
- source control com .meta;
- Play Mode + player/build verification.

Principais fontes:
- Unity-Technologies/skills;
- PhysicsExamples2D;
- PaddleGameSO;
- EntityComponentSystemSamples;
- ECS Network Racing;
- 2d-animation-samples;
- UnityPlayground.

### 3. game-networking-engineering

Novo owner de netcode engine-agnostic para:
- authority/topology;
- replicated state versus events/RPCs;
- interpolation;
- prediction/reconciliation;
- rollback/lag compensation;
- interest management;
- reconnect;
- network simulation;
- bandwidth/tick metrics.

Principais fontes:
- Unity Netcode for GameObjects;
- Multiplayer Bitesize;
- ECS Network Racing;
- Mirror;
- PurrNet.

### 4. game-performance-engineering

Novo owner para:
- target FPS/frame budget;
- CPU versus GPU bottleneck;
- memory/GC;
- rendering;
- physics;
- asset budgets;
- pooling baseado em churn real;
- Jobs/Burst/ECS apenas por ganho medido;
- comparação antes/depois no mesmo cenário/build/device.

Principais fontes:
- EntityComponentSystemSamples;
- ECS Network Racing;
- Bevy;
- Unity samples.

### 5. game-development-cycle

Nova stack que roteia:
- game core → game-development-engineering;
- Unity → unity-game-engineering;
- multiplayer → game-networking-engineering;
- performance → game-performance-engineering;
- shaders, sprite sheets e 3D assets → owners existentes.

## Capabilities que NÃO viraram novas skills

### Game shaders/VFX

Já existe `shader-graphics-engineering`. ShaderGraph ExampleLibrary, UnityShaderLib e URPShadersCollection permanecem referências técnicas/versionadas.

### Sprite sheets/assets 2D

Já existe `sprite-sheet-pipeline`. Unity-specific atlas/tilemap/pixel-perfect ficou dentro de `unity-game-engineering`, sem duplicar o pipeline de sprite.

### 3D assets/procedural

Já existem `concept-to-3d-asset`, `image-to-3d` e `procedural-3d-reconstruction`.

### ML-Agents / Game AI

`ml-agents` é tecnicamente forte, mas é runtime/framework-heavy e cobre reinforcement/imitation learning mais do que game AI geral. Não foi criada uma skill `game-ai-engineering` a partir de uma única família de evidência. Navigation convencional permanece parte do owner Unity quando necessário.

### LiveOps / monetização / backend

UGS Use Cases contém Battle Pass, Daily Rewards, Economy, Cloud Code, Remote Config, Lobby e outros padrões úteis, mas mistura arquitetura de jogo com serviços Unity específicos. Mantido como referência para futura avaliação dedicada de live-game engineering.

### AR/XR

AR Foundation Samples é uma fonte oficial valiosa, porém AR/XR é um domínio grande o suficiente para avaliação separada. Não foi comprimido dentro de game 3D genérico.

## Achados metodológicos importantes

1. **Version grounding é crítico em engines.** Godot demos mantêm branches por versão; PhysicsExamples2D também mantém versões específicas; Unity skills explicitam diferenças de render pipeline/API.
2. **Engine choice não substitui game architecture.** Unity, Godot, Bevy, Fyrox, Stride, Flax e Defold convergem em loops, state, asset lifecycle e runtime verification, apesar de modelos diferentes.
3. **ECS é ferramenta, não default.** Unity Entities e Bevy reforçam data-oriented design, mas o custo arquitetural só se justifica por workload/scale reais.
4. **Multiplayer começa por authority.** Mirror, PurrNet e Unity Netcode oferecem APIs diferentes para os mesmos problemas fundamentais.
5. **Samples isolados são melhores para aprender capability; jogos completos são melhores para integração.**
6. **Play Mode/editor success não prova build/device success.**
7. **Visual correctness não prova gameplay correctness.**

## Segurança e portabilidade

Nenhum repository, package, installer, build, Editor command, plugin, binary ou sample foi executado durante a avaliação.

Superfícies identificadas:
- package managers e install scripts;
- Unity Editor/CLI e build modules;
- native plugins;
- cloud services;
- authentication;
- ads/IAP/economy;
- multiplayer sockets/relay;
- telemetry;
- AR/XR device permissions;
- Git LFS e assets grandes.

Regras de adaptação:
- não assumir Unity Editor ou qualquer engine disponível na conversa;
- não executar package install apenas para descobrir comportamento;
- grounding por versão antes de API específica;
- cloud/live services exigem autorização/configuração próprias;
- samples antigos não são tratados como documentação atual;
- security/authority de multiplayer permanece explícita.

## Materialização

Criados:
- `skills/game-development-engineering/SKILL.md`
- `skills/unity-game-engineering/SKILL.md`
- `skills/game-networking-engineering/SKILL.md`
- `skills/game-performance-engineering/SKILL.md`
- `stacks/game-development-cycle/STACK.md`

Atualizado:
- `ARSENAL INDEX.md`

Não foram criadas skills para shaders, sprites, 3D assets, ML-Agents, AR/XR ou LiveOps porque o Arsenal já tem owner adequado ou a evidência justifica uma avaliação futura mais específica.

## Limites

- A avaliação foi feita por source tree, READMEs, skills oficiais e exemplos centrais; não houve build/execução dos 30 projetos.
- Repositórios de engine completa foram tratados como fontes arquiteturais, não auditados arquivo a arquivo.
- Compatibilidade de APIs deve sempre ser revalidada contra a versão real do projeto.
