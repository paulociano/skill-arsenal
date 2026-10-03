# Avaliação — Game Development Expansion III: Animation, Audio, Narrative, Save, Modding e Integridade

Data: 2026-10-02

## Objetivo

Expandir o Arsenal nas lacunas restantes do ciclo de game development: animação, áudio/música, narrativa/diálogo, save/persistência, modding/tooling e anti-cheat defensivo.

## Fontes avaliadas

| Repositório | Domínio | Classe | Decisão |
|---|---|---|---|
| KybernetikGames/animancer | Runtime animation | B/D | ABSORB_METHOD_ONLY |
| needle-mirror/com.unity.animation.rigging | Rigging/IK | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| Unity-Technologies/Unity.Animation.Samples | Animation systems | B/D | ABSORB_METHOD_ONLY |
| FMOD/fmod-for-unity | Game audio integration | A/D | CREATE_NEW / KEEP_EXTERNAL_REFERENCE |
| Unity-Technologies/NativeAudioPlugins | DSP/native audio | B/D | ABSORB_METHOD_ONLY |
| YarnSpinnerTool/YarnSpinner-Unity | Dialogue | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| inkle/ink | Interactive narrative | A/D | ABSORB_METHOD_ONLY |
| inkle/ink-unity-integration | Unity narrative integration | B/D | KEEP_EXTERNAL_REFERENCE |
| mnicolas94/unity-save-system | Save/load | B/D | ABSORB_METHOD_ONLY |
| BayatGames/SaveGameFree | Save/load | B/D | ABSORB_METHOD_ONLY |
| BepInEx/BepInEx | Mod/plugin loading | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| pardeike/Harmony | Runtime patching | A/D | KEEP_EXTERNAL_REFERENCE + bounded use |
| NeighTools/UnityDoorstop | Loader/bootstrap | D | KEEP_EXTERNAL_REFERENCE |
| MirrorNetworking/Mirror | Multiplayer/integrity context | A/D | UPDATE_EXISTING |
| Unity live-service/backend sources from prior lot | Integrity/authority | A/D | UPDATE_EXISTING |

## Resultado executivo

Cinco novos owners foram materializados:

1. `game-animation-engineering`
2. `game-audio-engineering`
3. `narrative-dialogue-engineering`
4. `save-game-persistence-engineering`
5. `game-modding-tooling-engineering`

Anti-cheat **não** virou skill independente. O valor defensivo foi incorporado a `game-networking-engineering`, que já é o owner correto para autoridade, validation e integrity checks em multiplayer.

## 1. Game Animation Engineering

### Lacuna

O Arsenal já cobria motion visual, 3D assets e gameplay, mas não o contrato entre animation state, gameplay state, physics, root motion e rigging.

### Métodos absorvidos

- state/blend graph;
- root motion ownership;
- rig constraints e IK como layers sobre pose;
- ordem de avaliação;
- interruption/cancel states;
- animation events como sinais delimitados;
- animation LOD/performance.

### Decisão

Criar `game-animation-engineering`.

## 2. Game Audio Engineering

### Lacuna

Não havia owner para buses/mixers, concurrency, spatialization, adaptive music, ducking e DSP budget.

### Métodos absorvidos

De FMOD/Unity audio sources:
- event-oriented playback;
- routing por buses;
- lifecycle explícito;
- streaming versus preload;
- spatialization;
- profiling de voices/DSP;
- plugin/backend desacoplado do gameplay.

### Decisão

Criar `game-audio-engineering`.

## 3. Narrative & Dialogue Engineering

### Lacuna

O Arsenal tinha escrita, conteúdo e localization, mas não runtime narrative state nem branching/choices/commands integrados ao jogo.

### Métodos absorvidos

De Yarn Spinner:
- lines;
- options;
- commands;
- writer-friendly authoring.

De Ink:
- branching story;
- story state;
- compiled/runtime separation;
- preview/play while authoring;
- save/story format versioning.

### Decisão

Criar `narrative-dialogue-engineering`.

## 4. Save Game Persistence Engineering

### Lacuna

Persistência geral/memória de agentes não cobre save-game, schema evolution, cloud conflicts ou atomic local writes.

### Métodos absorvidos

- DTO/state explícito;
- async I/O;
- custom serialization;
- save/load events;
- schema/version;
- corruption handling;
- backup;
- migration;
- cloud revision/conflict policy.

### Rejeição importante

Um dos samples oferece DES encryption. Isso **não foi adotado**. O Arsenal registra explicitamente que criptografia local não cria autoridade e que algoritmos legados não devem ser usados por inércia de sample.

### Decisão

Criar `save-game-persistence-engineering`.

## 5. Game Modding & Tooling Engineering

### Lacuna

O Arsenal não tinha owner para mod APIs, manifests, compatibility, plugin loading e permission boundaries.

### Métodos absorvidos

De BepInEx:
- plugin discovery/loading;
- config;
- logging;
- compatibility por runtime;
- loader architecture.

De Harmony:
- runtime patching;
- multiple patch coexistence;
- patch ordering/conflict considerations.

### Adaptação

Para um jogo próprio, o owner **prioriza extension points oficiais** e APIs estáveis. Runtime patching fica como último recurso em ambiente autorizado.

A skill não deve ser usada para:
- burlar anti-cheat;
- contornar DRM/licença;
- injetar código em software sem autorização;
- evasão de controles.

### Decisão

Criar `game-modding-tooling-engineering`.

## 6. Anti-cheat / Game Integrity

### Decisão de ownership

Não criar uma skill `anti-cheat-engineering`.

Motivo:
- a maior parte do comportamento robusto já pertence a server authority/netcode;
- uma skill ampla demais corre risco de misturar defesa com conhecimento operacional de evasão;
- prevenção útil nasce de invariants de protocolo, simulação autoritativa, rate/range/state validation e observabilidade.

### Atualização

`game-networking-engineering` agora inclui:
- validation de movement/cooldown/fire rate/state;
- envelopes físicos/temporais;
- comparação entre client claims e authoritative state;
- prevenção/detecção/resposta separadas;
- cuidado com falso positivo sob lag/jitter;
- anti-tamper cliente como camada complementar, não substituto de autoridade;
- proibição de documentação de bypass/evasion/injection.

## Segurança e portabilidade

Nenhum installer, plugin, binary, Unity package, mod loader ou native audio plugin foi executado.

Superfícies relevantes:
- runtime code loading;
- method patching;
- arbitrary assemblies;
- filesystem save data;
- cloud save;
- native audio;
- mod scripts;
- multiplayer integrity;
- encryption;
- telemetry.

Guardrails:
- mods são input/código não confiável;
- runtime patching só em contexto autorizado;
- save local não é autoridade;
- encryption local não protege economy competitiva;
- secrets nunca no client;
- anti-cheat permanece defensivo;
- plugin/backend APIs exigem grounding de versão.

## Materialização

Criados:
- `skills/game-animation-engineering/SKILL.md`
- `skills/game-audio-engineering/SKILL.md`
- `skills/narrative-dialogue-engineering/SKILL.md`
- `skills/save-game-persistence-engineering/SKILL.md`
- `skills/game-modding-tooling-engineering/SKILL.md`

Atualizados:
- `skills/game-networking-engineering/SKILL.md`
- `stacks/game-development-cycle/STACK.md`
- `ARSENAL INDEX.md`

## Limites

- Avaliação por README/documentação e código representativo, sem execução dos projetos.
- FMOD source repo não inclui todos os binaries/plataformas.
- Animancer repo usado aqui é documentação, não o source completo do produto.
- Modding de jogos de terceiros possui implicações de autorização/licença; o owner criado é orientado a suporte autorizado/first-party.
- Anti-cheat foi mantido em escopo defensivo.
