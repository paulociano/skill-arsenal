---
name: game-development-engineering
description: "Projetar, implementar e validar jogos 2D/3D por loops jogáveis pequenos, separando gameplay state, simulation, presentation, assets e runtime verification sem assumir uma engine específica."
---

# Game Development Engineering

## Objetivo

Construir jogos como sistemas iterativos verificáveis, não como uma coleção de scripts isolados. O owner é engine-agnostic e cobre o ciclo de gameplay, cenas/entidades, input, simulação, apresentação, assets, testes e builds.

Use `unity-game-engineering` quando o projeto for Unity. Para shaders, assets 3D e sprites especializados, rotear para os owners existentes.

## Quando usar

- criar ou evoluir um jogo 2D/3D;
- implementar um vertical slice;
- definir arquitetura de gameplay;
- integrar input, câmera, movimento, combate, interação, inventário, spawning ou checkpoints;
- diagnosticar comportamento de jogo que atravessa múltiplos sistemas;
- escolher entre object/component, scene graph, ECS/data-oriented ou mistura proporcional.

## Princípio central

**Fechar um loop jogável antes de ampliar o sistema.**

Sequência preferida:

`player intent → simulation → state transition → presentation → observable feedback → verify`

Uma feature não está pronta só porque compila. Precisa existir uma ação do jogador ou evento de simulação que possa ser observado e verificado no runtime.

## Workflow

1. **Ground**
   - engine e versão;
   - plataformas alvo;
   - 2D/3D;
   - single/multiplayer;
   - target frame rate;
   - input devices;
   - constraints de arte, física e build.

2. **Playable contract**
   - definir o que o jogador faz;
   - condição inicial;
   - ação/input;
   - resultado observável;
   - fail/recovery state;
   - critério de conclusão.

3. **Choose representation**
   - scene/object/component para lógica local e authoring;
   - ECS/data-oriented quando escala, paralelismo ou grande volume de entidades justificarem;
   - não introduzir ECS por moda;
   - manter dados configuráveis fora de lógica quando designers precisam iterar sem recompilar.

4. **Separate clocks**
   - input e presentation no frame loop;
   - física/simulação determinística no fixed timestep quando aplicável;
   - lógica de rede em tick próprio quando multiplayer exigir;
   - nunca acoplar comportamento crítico a frame rate variável sem intenção explícita.

5. **Build one vertical slice**
   - input;
   - state;
   - simulation;
   - feedback visual/sonoro;
   - reset/retry;
   - telemetry/debug visibility mínima.

6. **Gameplay state**
   - distinguir state durável de objetos de cena temporários;
   - evitar singletons globais como default;
   - eventos/channels/runtime sets/data assets são opções quando desacoplamento real existir;
   - preferir contracts pequenos entre sistemas.

7. **Physics**
   - declarar quem move: physics engine, character controller ou transform;
   - collision layers/masks explícitos;
   - triggers separados de colisões físicas;
   - não misturar teleporte por transform com rigidbody dinâmico sem resolver ownership do movimento.

8. **2D**
   - definir pixels-per-unit/escala antes da produção de assets;
   - câmera, sprite filtering, atlas/tilemap e sorting precisam ser coerentes;
   - pixel-perfect só quando a direção de arte exige.

9. **3D**
   - declarar escala/unidades;
   - câmera e controller antes de polish;
   - colisores simples antes de mesh collision detalhada;
   - animation root motion e physics precisam de owner claro sobre deslocamento.

10. **Verify in runtime**
    - reproduzir o loop;
    - observar estado antes/depois;
    - conferir console/logs;
    - testar reset/reload;
    - testar input alternativo e boundary cases relevantes;
    - screenshot bonito não prova gameplay correto.

11. **Profile only after observable loop exists**
    - usar `game-performance-engineering` quando frame time, memória, GC, draw calls, streaming ou entidades virarem restrição.

12. **Build**
    - validar build real na plataforma alvo quando possível;
    - editor/play mode não substitui player/device build;
    - registrar versão da engine, packages/plugins e build target.

## Gameplay systems

Para sistemas recorrentes, separar:
- **data/config**;
- **runtime state**;
- **rules/simulation**;
- **presentation**;
- **persistence**;
- **network replication**, se houver.

Aplicável a health/damage, abilities, inventory, quests, dialogue, checkpoints, progression, spawning e economy.

## Testes

Preferir uma pirâmide adaptada a jogos:
- testes puros para regras determinísticas;
- integration/play-mode para interação entre engine systems;
- runtime smoke para cena/vertical slice;
- build/device para plataforma;
- perf/regression quando budgets forem críticos.

## Regras

- não confundir engine feature com requisito de jogo;
- não começar por arquitetura máxima;
- evitar abstrações antes de existir repetição/comportamento real;
- não misturar simulation state com presentation state sem necessidade;
- não esconder dependência temporal em callbacks implícitos;
- uma cena que abre não prova que o jogo funciona;
- toda feature jogável precisa de um caminho de reset/reprodução para teste.

## Integração

- `unity-game-engineering` para Unity;
- `game-networking-engineering` para multiplayer;
- `game-performance-engineering` para frame/memory budgets;
- `shader-graphics-engineering` para shaders;
- `sprite-sheet-pipeline` para spritesheets;
- `procedural-3d-reconstruction` / `concept-to-3d-asset` para assets 3D;
- `tdd`, `diagnosing-bugs`, `runtime-ui-verification` e `library-version-grounding` conforme o caso.

## Provenance

Consolidada de padrões recorrentes em Unity Technologies samples, Godot demo projects, Bevy, Fyrox, Stride, Flax e Defold. Preserva vertical slices, version grounding, separação de clocks, scene/component/ECS trade-offs e runtime validation sem assumir uma engine específica.

## Contratos de conteúdo jogável e integridade transacional

Para jogos orientados a dados e inventários, incluindo Three.js:

1. Definir item, inimigo, nível, encontro e ação de combate como **conteúdo versionado** separado do estado de execução. IDs estáveis, transições explícitas e migração de saves evitam duplicações e referências órfãs.
2. Tratar transferência, equipar, dividir pilha, coletar e descartar inventário como **transações atômicas**: checar origem, capacidade, compatibilidade e persistência antes de aplicar; sob erro, nenhuma cópia ou perda silenciosa.
3. Fazer movesets declararem startup, active window, recovery, interruptibilidade, hitbox/contact, cooldown, custo e telegraph. A animação apresenta o resultado; a simulação determina acertos.
4. Para inimigos, manter percepção, decisão, movimento, combate e render separados. Fixtures reproduzíveis devem cobrir aggro, leash, interrupção, rota bloqueada e retorno.
5. Para editores de fase, separar rascunho reversível de dado publicado, com schema versionado, import/export validado, undo e proteção de rotas de edição. Nunca deixar uma edição visual mutar a sessão de produção implicitamente.
6. Demonstrar o caminho do jogador com evidência runtime quando disponível: entrar, agir, receber feedback, ganhar recompensa, modificar inventário, salvar e continuar. Uma compilação verde não substitui o percurso jogável.

**Proveniência:** metodologias de `MengTo/Skills` (`build-game-inventory`, `build-threejs-enemy-systems`, `design-action-combat`, `build-game-map-editor`, `test-playable-web-games`), avaliadas em 2026-10-15. Não presume Three.js, navegador, sessões de teste ou ferramentas instaladas.
