# Avaliação — Game Development Expansion V: Level Design, Combat, Matchmaking, Localization, Economy Balance e Platform Performance

Data: 2026-10-03

## Objetivo

Expandir o Arsenal nas especializações finais de alto valor para game development: level design, combat/abilities, matchmaking/social systems, localization pipeline, economy balance e otimização adaptativa por plataforma.

## Fontes avaliadas

| Repositório | Domínio | Classe | Decisão |
|---|---|---|---|
| TrenchBroom/TrenchBroom | Level authoring/greybox | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| Unity-Technologies/FPSSample | Combat + level preview | B/D | ABSORB_METHOD_ONLY |
| PhysaliaStudio/Flexi | Ability systems | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| sjai013/UnityGameplayAbilitySystem | Ability systems | B/D | KEEP_EXTERNAL_REFERENCE |
| googleforgames/open-match | Matchmaking | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| googleforgames/agones | Game server allocation | A/D | ABSORB_METHOD_ONLY |
| needle-mirror/com.unity.localization | Localization | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| needle-mirror/com.unity.adaptiveperformance | Mobile/platform performance | A/D | UPDATE_EXISTING |
| Unity-Technologies/BoatAttack | Mobile/URP optimization | B/D | UPDATE_EXISTING |
| Unity live-service/economy sources from prior lot | Economy balance | A/D | UPDATE_EXISTING |

## Resultado executivo

Criados quatro novos owners:

1. `level-design-engineering`
2. `combat-ability-engineering`
3. `game-matchmaking-social-engineering`
4. `game-localization-engineering`

Atualizados:
- `live-game-operations-engineering` com economy balance;
- `game-performance-engineering` com adaptive/platform-specific performance;
- `game-development-cycle` e `ARSENAL INDEX.md`.

## 1. Level Design Engineering

### Lacuna

`procedural-game-content` gera estruturas e `game-development-engineering` cobre gameplay geral, mas nenhum owner cuidava do espaço como experiência: greybox, critical path, traversal metrics, sightlines, encounter spaces e pacing.

### Métodos absorvidos

De TrenchBroom:
- brush/blockout-first authoring;
- 2D/3D views;
- entity placement;
- issue browser;
- undo/iteration;
- geometria simples antes do polish.

Do FPSSample:
- preview mode;
- testar level, traversal e weapons antes de standalone;
- levels compostos por múltiplas scenes;
- ferramenta/editor workflow para iteração rápida.

### Decisão

Criar `level-design-engineering`.

## 2. Combat & Ability Engineering

### Lacuna

O Arsenal possuía gameplay, animation e networking, porém faltava um contrato para activation, attributes, costs, cooldowns, effects, targeting, hit resolution e combos.

### Métodos absorvidos

De Flexi:
- low-level ability runner;
- stats/modifiers;
- ability chain;
- designer-facing graph como authoring tool.

De UnityGameplayAbilitySystem e referências GAS:
- attributes;
- gameplay tags/state requirements;
- effects/modifiers;
- ability activation contract.

Do FPSSample:
- weapon/combat validation integrada a multiplayer e level preview.

### Decisão

Criar `combat-ability-engineering`.

O repo `sjai013/UnityGameplayAbilitySystem` está arquivado e portanto foi tratado somente como referência metodológica.

## 3. Game Matchmaking & Social Engineering

### Lacuna

`game-networking-engineering` cuida da partida já formada, mas não de ticketing, pools, quality-vs-wait tradeoff, parties, lobbies, backfill ou server allocation.

### Métodos absorvidos

De Open Match:
- tickets;
- pools;
- match functions;
- evaluator/assignment separation;
- extensibilidade de regras sem acoplar à infraestrutura.

De Agones:
- alocação/orquestração de game servers;
- region/build/capacity como parte do contract operacional.

### Decisão

Criar `game-matchmaking-social-engineering`.

## 4. Game Localization Engineering

### Lacuna

`locale-adapter` e narrative/UI cobriam partes do problema, mas não pipeline completo de localization de jogos.

### Métodos absorvidos

Do Unity Localization package:
- string localization;
- localized assets;
- Smart Strings;
- pseudo-localization;
- locale variants;
- XLIFF/CSV/Google Sheets import/export.

### Decisão

Criar `game-localization-engineering` engine-agnostic.

## 5. Economy Balance

### Decisão de ownership

Não criar `game-economy-design` separado neste lote.

O owner `live-game-operations-engineering` já controla currency, rewards, stores, progression e server-authoritative economy. Foi ampliado com:
- sources/sinks;
- currency creation/destruction;
- balance por cohort;
- sink/source ratio;
- time-to-afford;
- inventory saturation;
- inflation/hoarding/exploit scenarios;
- versionamento de mudanças de preço/reward.

Isso evita separar design de economia da operação que realmente modifica o estado de valor.

## 6. Platform-Specific Performance

### Decisão de ownership

Não criar owner separado.

`game-performance-engineering` foi ampliado com:
- thermal state;
- battery/power state;
- memory pressure;
- adaptive quality tiers;
- render scale;
- shadow/LOD/post-processing/particle knobs;
- hysteresis;
- recovery;
- sustained performance.

Adaptive Performance mostrou que FPS frio no início da sessão não representa necessariamente a performance sustentada em mobile.

## Segurança e portabilidade

Nenhuma engine, package, game server, Kubernetes cluster, localization pipeline, SDK, Unity project ou binary foi executado.

Superfícies relevantes:
- matchmaker/player identifiers;
- multiplayer service infrastructure;
- Kubernetes/server orchestration;
- remote economy state;
- localization provider data;
- mobile thermal/power APIs;
- archived/outdated Unity samples.

Guardrails:
- matchmaking metadata limitado ao necessário;
- server allocation não presume Agones/Kubernetes disponível;
- archived combat examples não viram API atual;
- economy state continua server-authoritative;
- localization imports precisam de diff/merge seguro;
- platform tuning depende do device/runtime real.

## Materialização

Criados:
- `skills/level-design-engineering/SKILL.md`
- `skills/combat-ability-engineering/SKILL.md`
- `skills/game-matchmaking-social-engineering/SKILL.md`
- `skills/game-localization-engineering/SKILL.md`

Atualizados:
- `skills/live-game-operations-engineering/SKILL.md`
- `skills/game-performance-engineering/SKILL.md`
- `stacks/game-development-cycle/STACK.md`
- `ARSENAL INDEX.md`

## Limites

- TrenchBroom é editor orientado a jogos Quake-like, usado aqui como fonte de metodologia de blockout/iteration, não como requisito técnico.
- FPSSample é antigo e explicitamente não mantido; somente padrões conceituais foram absorvidos.
- Adaptive Performance mirror inclui detalhes internos/provider-specific; apenas o contrato de feedback thermal/power foi incorporado.
- Matchmaking real exige métricas e população do jogo; nenhuma política universal de skill/latency foi imposta.
