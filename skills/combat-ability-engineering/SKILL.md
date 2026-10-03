---
name: combat-ability-engineering
description: "Projetar e validar combate e abilities com attributes, costs, cooldowns, targeting, effects, hit windows, combos, status effects, cancellation, feedback e contratos de autoridade compatíveis com single e multiplayer."
---

# Combat & Ability Engineering

## Objetivo

Modelar combate como state transitions verificáveis entre intenção, targeting, activation, cost, effect, feedback e recovery, evitando lógica de dano espalhada por animações e scripts ad hoc.

## Quando usar

- melee/ranged combat;
- abilities/skills/spells;
- stats/attributes;
- cooldowns/costs;
- buffs/debuffs/status effects;
- combos;
- hitboxes/hurtboxes;
- target selection;
- combat multiplayer.

## Princípio central

**Uma ability é um contrato de ativação e efeitos, não apenas uma animação com dano.**

## Ability contract

Definir:
- owner/source;
- activation conditions;
- target rule;
- cost;
- cooldown;
- cast/startup;
- active window;
- recovery;
- effects;
- cancellation;
- tags/state requirements;
- replication/authority quando multiplayer.

## Workflow

1. **Attributes**
   - health/resource;
   - base versus modified value;
   - clamping;
   - temporary/permanent modifiers;
   - deterministic ordering quando múltiplos effects interagem.

2. **Activation**
   - canActivate;
   - reserve/pay cost;
   - enter state;
   - start timing;
   - fail sem consumir recurso quando contract disser.

3. **Targeting**
   - self;
   - point;
   - entity;
   - area;
   - cone/ray/projectile;
   - validate range, line of sight e team/faction.

4. **Hit resolution**
   - hitbox/hurtbox;
   - projectile;
   - raycast;
   - overlap;
   - contact deduplication;
   - invulnerability windows;
   - friendly-fire policy.

5. **Effects**
   - damage/heal;
   - stat modifier;
   - crowd control;
   - damage over time;
   - stack/refresh/replace rules;
   - dispel/expiry.

6. **Combos**
   - input buffer;
   - cancel window;
   - branch condition;
   - reset timeout;
   - animation sync;
   - não codificar combo exclusivamente por animation event.

7. **Feedback**
   - animation;
   - VFX;
   - SFX;
   - hit pause/shake;
   - damage numbers/UI;
   - feedback nunca deve alterar authority da simulação.

8. **Multiplayer**
   - client sends intent;
   - server validates activation/hit/effect quando competitivo;
   - prediction para responsiveness pode existir;
   - correction/reconciliation não deve duplicar efeitos.

9. **Balance**
   - separar tuning de rules;
   - registrar DPS, burst, time-to-kill, resource efficiency, uptime e counterplay;
   - comparar cenários, não um número isolado.

10. **Test**
    - insufficient resource;
    - cooldown;
    - cancel/interruption;
    - simultaneous hits;
    - invulnerability;
    - stacking;
    - target loss;
    - network retry/reconciliation quando aplicável.

## Regras

- damage não deve nascer de múltiplos owners sem contract;
- animation state não é combat state;
- cooldown visual não é cooldown autoritativo;
- stacking precisa de regra explícita;
- ability graph/editor é ferramenta, não substituto do domínio;
- tuning deve permanecer data-driven quando designers iteram frequentemente.

## Integração

`game-development-engineering`, `game-animation-engineering`, `game-networking-engineering`, `game-ai-engineering`, `game-audio-engineering`, `game-camera-cinematics-engineering` e `game-testing-quality-engineering`.

## Provenance

Consolidada de Unity FPSSample, PhysaliaStudio/Flexi e UnityGameplayAbilitySystem como referências de attributes, modifiers, abilities, targeting e combat flow. Repositórios antigos/arquivados são usados como metodologia, não como API atual.
