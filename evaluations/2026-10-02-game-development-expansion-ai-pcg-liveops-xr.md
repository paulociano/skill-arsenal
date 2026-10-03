# Avaliação — Game Development Expansion II: AI, PCG, LiveOps e XR

Data: 2026-10-02

## Objetivo

Expandir a stack de game development do Skill Arsenal nos quatro domínios que ficaram deliberadamente fora do primeiro lote: AI/NPCs, procedural content, live-game operations e XR.

## Fontes avaliadas

| Repositório | Domínio | Classe | Decisão |
|---|---|---|---|
| Unity-Technologies/ml-agents | AI/ML gameplay | A/D | KEEP_EXTERNAL_REFERENCE + method boundary |
| libgdx/gdx-ai | Game AI clássica | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| crashkonijn/GOAP | GOAP Unity | A/D | ABSORB_METHOD_ONLY |
| Syomus/ProceduralToolkit | Procedural generation | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| OndrejNepozitek/Edgar-Unity | Procedural levels | A/D | ABSORB_METHOD_ONLY |
| mxgmn/WaveFunctionCollapse | Constraint generation | A/D | ABSORB_METHOD_ONLY |
| marian42/wavefunctioncollapse | WFC world generation | B/D | ABSORB_METHOD_ONLY |
| Unity-Technologies/com.unity.services.samples.use-cases | LiveOps/economy | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| heroiclabs/nakama | Game backend/live services | A/D | ABSORB_METHOD_ONLY |
| heroiclabs/nakama-unity | Unity backend integration | D | KEEP_EXTERNAL_REFERENCE |
| PlayFab/UnitySDK | Live services SDK | D | ABSORB_METHOD_ONLY / security contrast |
| Unity-Technologies/arfoundation-samples | AR/XR | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| Unity-Technologies/XR-Interaction-Toolkit-Examples | XR interaction | A/D | ABSORB_METHOD_ONLY |
| KhronosGroup/OpenXR-SDK-Source | OpenXR runtime/spec implementation | A/D | ABSORB_METHOD_ONLY |
| De-Panther/unity-webxr-export | WebXR Unity | B/D | KEEP_EXTERNAL_REFERENCE + cross-runtime contrast |

## Resultado executivo

Quatro lacunas reais foram confirmadas e materializadas como owners novos:

1. `game-ai-engineering`
2. `procedural-game-content`
3. `live-game-operations-engineering`
4. `xr-game-engineering`

A stack `game-development-cycle` foi atualizada para rotear essas capacidades sob demanda.

## 1. Game AI Engineering

### Valor incremental

O owner geral de game development não tinha contrato suficiente para percepção, decision models, pathfinding, steering, planners e escalabilidade de NPCs.

### Padrões absorvidos

De `libgdx/gdx-ai`:
- steering behaviors;
- formation movement;
- A* e hierarchical pathfinding;
- path smoothing;
- FSM;
- behavior trees;
- message handling e scheduling.

De `crashkonijn/GOAP`:
- goals/actions com preconditions/effects;
- planning separado de action execution;
- visualização/diagnóstico como parte da operabilidade;
- escalabilidade por jobs como opção, não default.

De `Unity-Technologies/ml-agents`:
- ML para gameplay é uma ferramenta específica, não substituto automático de FSM/BT/GOAP;
- training/evaluation precisa de artifact e métricas reais.

### Decisão

Criar `game-ai-engineering` engine-agnostic. `ml-production-engineering` continua owner de ML lifecycle quando treinamento/deploy real existir.

## 2. Procedural Game Content

### Valor incremental

`procedural-3d-reconstruction` reconstrói um objeto 3D a partir de referência. Não cobre geração de levels/worlds por seed e constraints.

### Padrões absorvidos

De `ProceduralToolkit`:
- random helpers, geometry, mesh generation, cellular automata e building strategies.

De `Edgar-Unity`:
- level generation configurável com rooms/templates/graph constraints.

De `mxgmn/WaveFunctionCollapse` e `marian42/wavefunctioncollapse`:
- constraint propagation;
- module adjacency;
- entropy/selection;
- backtracking/restart;
- separação entre compatibilidade local e validade global.

### Decisão

Criar `procedural-game-content` com seedability, hard validators, soft scoring, bounded regeneration e corpus de seeds.

## 3. Live Game Operations Engineering

### Valor incremental

O Arsenal tinha product analytics, experimentação, system design e production go-live, mas não um owner para operação mutável de economia/eventos/config de jogos já lançados.

### Padrões absorvidos

De Unity Gaming Services Use Cases:
- A/B difficulty;
- battle pass;
- daily rewards;
- seasonal events;
- mailbox/gifts;
- loot/reward cooldown;
- virtual shop;
- server-authoritative economy;
- remote/scheduled content.

De Nakama:
- auth;
- storage;
- social;
- leaderboards/tournaments;
- multiplayer;
- purchase validation;
- server runtime logic;
- operational console/metrics.

De PlayFab:
- contraste entre client APIs e server APIs;
- server secrets nunca devem ser tratados como configuração cliente;
- transporte/configuração precisa ser version-aware.

### Guardrails importantes

- cliente não é autoridade sobre currency, item, reward, price ou eligibility;
- clock do device não governa reward crítico;
- retry de grant/purchase exige idempotency;
- remote config precisa de schema/default/rollback;
- experiments precisam de assignment estável e métricas definidas.

### Decisão

Criar `live-game-operations-engineering`.

## 4. XR Game Engineering

### Valor incremental

O Arsenal possuía mobile, 3D, shaders e runtime validation, mas não tracking spaces, spatial interaction, locomotion, comfort ou device-runtime abstraction.

### Padrões absorvidos

De XR Interaction Toolkit Examples:
- XR Origin;
- locomotion;
- grab/activate/socket;
- gaze/focus;
- 2D/3D spatial UI;
- physics interactables;
- climb interactions.

De AR Foundation Samples:
- runtime/platform plugins;
- session lifecycle;
- plane/anchor/hit-test tracking;
- device build como fluxo real;
- branches/version compatibility.

De OpenXR:
- loader/runtime abstraction;
- feature/extensions;
- portable core versus vendor-specific paths.

De WebXR Export:
- diferença entre engine interaction semantics e runtime/browser source de poses/input;
- capability detection;
- cross-device/browser fallback.

### Decisão

Criar `xr-game-engineering`.

## Segurança e portabilidade

Nenhum installer, package, Docker image, Unity project, model training, SDK, XR runtime ou executable externo foi executado.

Superfícies relevantes:
- ML training/runtime;
- package managers;
- cloud credentials;
- developer/server secret keys;
- purchase validation;
- player data;
- economy mutation;
- sockets/realtime networking;
- device cameras/sensors;
- XR permissions;
- vendor SDKs;
- browser/device compatibility.

Adaptações:
- nenhuma engine/tool é presumida disponível;
- SDK/server snippets das fontes não foram copiados como dependência;
- secrets permanecem server-side;
- APIs específicas exigem grounding na versão instalada;
- simulator não conta como validação de XR material;
- ML fica subordinado a avaliação reproduzível;
- procedural generation tem bounded retries.

## Materialização

Criados:
- `skills/game-ai-engineering/SKILL.md`
- `skills/procedural-game-content/SKILL.md`
- `skills/live-game-operations-engineering/SKILL.md`
- `skills/xr-game-engineering/SKILL.md`

Atualizados:
- `stacks/game-development-cycle/STACK.md`
- `ARSENAL INDEX.md`

## Próxima fronteira

Não foram criados owners específicos para:
- dialogue/narrative systems;
- animation engineering;
- audio/game music systems;
- save-game/persistence engineering;
- modding/tooling;
- anti-cheat.

Esses temas podem ser um terceiro lote se houver necessidade real.

## Limites

- Repositórios foram avaliados por metadata, README/documentação central e exemplos representativos.
- Não foi feita execução funcional dos projetos.
- Adoção é metodológica; compatibilidade concreta deve ser revalidada contra engine/package/runtime do projeto real.
