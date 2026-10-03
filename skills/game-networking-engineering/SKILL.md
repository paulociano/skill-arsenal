---
name: game-networking-engineering
description: "Projetar e validar multiplayer em jogos com autoridade, replication, RPC/events, interpolation, prediction, reconciliation, rollback, interest management e testes sob latência/perda."
---

# Game Networking Engineering

## Objetivo

Projetar netcode a partir do modelo de autoridade e do comportamento observável do jogo, antes de escolher RPCs, SyncVars ou framework.

## Quando usar

- multiplayer realtime;
- co-op, competitive, racing, shooter, social hub;
- sincronização de physics/animation/state;
- client/server, host, distributed authority ou dedicated server;
- prediction, lag compensation ou rollback;
- reconnect e persistence de identidade.

## Workflow

1. **Network contract**
   - topologia;
   - quem é autoridade de cada state;
   - tick rate;
   - player count;
   - latency/jitter/packet-loss assumptions;
   - cheat/threat boundary;
   - reconnect/session requirements.

2. **Classify state**
   - authoritative game state;
   - player input;
   - cosmetic state;
   - ephemeral events;
   - large/rare assets;
   - persistent profile/economy.

3. **Choose replication**
   - snapshot/state replication para estado contínuo;
   - RPC/event para eventos;
   - delta/compression quando medido;
   - reliable somente onde perda é inaceitável;
   - unreliable para streams frequentes tolerantes a perda.

4. **Authority**
   - server authority como default para estado competitivo;
   - client authority só com boundary explícito;
   - ownership não equivale a confiança;
   - spawn/despawn e mutation permissions precisam ser deliberados.

5. **Movement**
   - remote entities: interpolation/extrapolation;
   - local controlled entity: client-side prediction quando responsividade exigir;
   - server correction + reconciliation;
   - physics prediction só com estratégia de determinismo/tolerância a divergence.

6. **Lag-sensitive interactions**
   - hit validation/lag compensation quando necessário;
   - guardar histórico limitado e verificável;
   - nunca aceitar timestamp/client claim sem policy.

7. **Interest management**
   - não replicar tudo para todos;
   - usar spatial/visibility/team/relevance rules;
   - medir bandwidth por player e por tick.

8. **Reconnect**
   - separar connection identity de player/game identity;
   - definir grace window e ownership recovery;
   - reconnect não pode duplicar entidades ou resetar state silenciosamente.

9. **Test hostile network**
   - latency;
   - jitter;
   - packet loss;
   - reorder quando transport permitir;
   - disconnect/reconnect;
   - late join;
   - host migration apenas se suportada pelo design.

10. **Measure**
    - bytes/sec;
    - messages/sec;
    - server frame/tick time;
    - client correction frequency;
    - prediction error;
    - bandwidth spikes;
    - GC/allocations causadas por serialization.

## Framework mapping

APIs como Netcode for GameObjects, Netcode for Entities, Mirror ou PurrNet são implementações. Mapear sempre:
- NetworkObject/Identity → networked entity identity;
- SyncVar/NetworkVariable → replicated state;
- RPC/Command → remote event;
- ownership/rules → authority policy;
- NetworkTransform/Rigidbody → movement replication strategy.

Não deixar nomes de API substituírem o desenho do protocolo.

## Multiplayer + physics

Definir explicitamente:
- simulation authority;
- physics tick;
- prediction model;
- collision ownership;
- correction threshold;
- interpolation buffer;
- determinism expectations.

## Segurança e integridade

- cliente é input não confiável;
- validar rate, range, ownership e state transitions;
- servidor não deve executar payload arbitrário;
- serialization bounds;
- limitar spawn/RPC abuse;
- não logar secrets/session tokens.

### Anti-cheat defensivo

Tratar anti-cheat primeiro como **integridade de protocolo e simulação**, não como corrida armamentista no cliente:

- servidor valida movimentos, cooldowns, fire rate, inventory/economy changes e transições impossíveis;
- usar invariants e envelopes físicos/temporais explícitos;
- comparar claims do cliente com state autoritativo;
- distinguir prevenção, detecção e resposta;
- coletar sinais suficientes para investigação sem capturar dados desnecessários;
- usar thresholds tolerantes a jitter/lag para evitar falso positivo;
- ações punitivas irreversíveis exigem evidência e policy humana/operacional apropriada;
- client anti-tamper pode ser uma camada adicional, mas nunca substitui server authority.

Não documentar bypass de anti-cheat, técnicas de evasão, ocultação de cheats, injeção em processos ou formas de derrotar mecanismos de detecção.

## Regras

- “sincroniza automaticamente” não elimina authority design;
- RPC em excesso é smell de state model mal definido;
- smooth remote movement não prova correção;
- LAN test não prova internet behavior;
- multiplayer deve ser testado sob rede degradada antes de conclusão.

## Integração

`game-development-engineering`, `unity-game-engineering`, `game-performance-engineering`, `system-design-engineering`, `secure-code-privacy-review` e `behavior-contract-validation`.

## Provenance

Consolidada de Unity Netcode for GameObjects, Unity Multiplayer Bitesize Samples, ECS Network Racing/Netcode for Entities, Mirror e PurrNet. Preserva authority, state replication, interpolation, prediction/reconciliation, lag compensation, interest management e network simulation sem fixar um framework.
