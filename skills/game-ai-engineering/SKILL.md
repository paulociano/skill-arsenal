---
name: game-ai-engineering
description: "Projetar, implementar e validar AI de gameplay para NPCs com percepção, state machines, behavior trees, GOAP, steering, pathfinding/navigation e aprendizado quando realmente justificado."
---

# Game AI Engineering

## Objetivo

Projetar comportamento de NPCs como um loop observável de percepção, decisão, ação e feedback, escolhendo a técnica mais simples que sustente o comportamento desejado.

## Quando usar

- NPCs, inimigos, aliados, criaturas ou crowds;
- patrol/chase/flee/combat;
- state machines, behavior trees ou GOAP;
- navigation/pathfinding;
- steering e formation movement;
- utility/planning;
- ML/reinforcement/imitation learning aplicado a gameplay.

## Princípio central

**Comportamento bom é explicável e depurável antes de ser sofisticado.**

Loop:

`observe → update blackboard/state → decide → act → verify outcome → reconsider`

## Workflow

1. **Behavior contract**
   - estímulos observáveis;
   - estados/objetivos;
   - ações legais;
   - prioridades;
   - fail/recovery;
   - frequência de decisão;
   - critério observável de sucesso.

2. **Perception**
   - visão, distância, som, triggers ou game state;
   - separar sensor de decisão;
   - cachear/scheduler apenas quando custo medido justificar;
   - limitar queries físicas caras por frame.

3. **Choose decision model**
   - FSM: poucos estados e transições claras;
   - behavior tree: composição hierárquica de condições/ações;
   - GOAP/planner: objetivos e ações recombináveis com preconditions/effects;
   - utility: escolhas graduais entre alternativas;
   - ML: somente quando regra/planner explícito é insuficiente e existe dataset/reward/evaluation real.

4. **Navigation**
   - representação do mundo: graph, grid, navmesh, voxel ou outro;
   - A*/hierarchical pathfinding quando aplicável;
   - path smoothing separado do planejamento;
   - local avoidance/steering separado de global pathfinding;
   - recalcular caminho apenas quando estado relevante mudou.

5. **Action execution**
   - decisão não deve teletransportar state silenciosamente;
   - action possui start, running, success/failure/cancel;
   - animation/physics ownership explícito;
   - interrupção segura quando prioridade muda.

6. **Debuggability**
   - estado atual;
   - objetivo;
   - target;
   - último estímulo;
   - action/path;
   - motivo de transition;
   - visualizers/gizmos/traces quando runtime permitir.

7. **Scale**
   - reduzir decision frequency por LOD/relevance;
   - schedulers/budgets para crowds;
   - spatial partitioning;
   - Jobs/ECS apenas quando profiling mostrar necessidade.

8. **Verify**
   - cenários reproduzíveis;
   - success/fail/recovery;
   - target desaparece;
   - caminho bloqueado;
   - múltiplos agentes;
   - performance no pior caso.

## ML-based NPCs

Quando usar ML-Agents ou equivalente:
- definir reward sem shortcuts óbvios;
- baseline rule-based;
- train/eval split de cenários quando aplicável;
- medir generalização;
- política treinada é artifact versionado;
- não substituir regras críticas de segurança/game state por comportamento opaco sem guardrails.

Combinar com `ml-production-engineering` quando houver treino/deploy real.

## Regras

- behavior tree não é automaticamente melhor que FSM;
- pathfinding não é steering;
- navigation success não prova comportamento convincente;
- planner sem visualização de preconditions/effects fica difícil de depurar;
- não usar raycast/perception máxima para todos os NPCs a cada frame sem budget;
- randomness deve ser seedable quando reprodução/importância exigir.

## Integração

`game-development-engineering`, `unity-game-engineering`, `game-performance-engineering`, `ml-production-engineering`, `diagnosing-bugs` e `behavior-contract-validation`.

## Provenance

Consolidada de libgdx/gdx-ai (steering, pathfinding, FSM, behavior trees, scheduling), crashkonijn/GOAP (goal-oriented planning e visualização) e Unity-Technologies/ml-agents como referência para aprendizado. Não exige esses runtimes.
