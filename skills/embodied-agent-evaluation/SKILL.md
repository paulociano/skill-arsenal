---
name: embodied-agent-evaluation
description: "Avaliar e evoluir agentes embodied/robóticos por rollouts reproduzíveis, failure clustering, diagnóstico causal, critic/recovery separados, shadow replay, same-seed gates e held-out evaluation antes de promover novas políticas."
---

# Embodied Agent Evaluation

## Objetivo

Melhorar agentes que atuam em simuladores ou robôs sem transformar falhas observadas em patches improvisados que quebram generalização.

## Quando usar

- embodied AI;
- robotics agents;
- VLA policy evaluation;
- simulator rollouts;
- recovery skills;
- online adaptation;
- manipulation benchmarks;
- failure-driven agent improvement.

## Princípio central

**Diagnóstico, proposta, decisão e ação precisam de papéis separados.**

## Evolution protocol

1. **Freeze campaign**
   - task contract;
   - environment;
   - model/policy version;
   - tool/action schema;
   - development seeds;
   - held-out seeds;
   - metrics;
   - promotion criteria.

2. **Collect rollouts**
   - complete trajectories;
   - synchronized observations/video when available;
   - bounded telemetry;
   - environment outcome;
   - infra failures tagged separately.

3. **Failure clustering**
   - group by observable failure mechanism;
   - preserve representative segments;
   - do not mix infra failures with task failures.

4. **Causal diagnose**
   - explain one concrete mechanism;
   - diagnosis role cannot execute a recovery;
   - avoid vague labels like “bad reasoning” when temporal evidence supports a specific failure.

5. **Candidate**
   - create one bounded critic/recovery bundle;
   - exact input/output/action schemas;
   - frozen candidate for evaluation.

6. **Shadow replay**
   - run critic/recovery logic against recorded trajectories where possible;
   - measure trigger precision/false positives before live action.

7. **Same-seed paired gate**
   - baseline and candidate on identical seeds/conditions;
   - compare success and regressions;
   - reject if improvement is not attributable.

8. **Held-out gate**
   - use seeds/tasks not used for candidate creation;
   - held-out set must be frozen before evaluation;
   - do not inspect and tune repeatedly on the test set.

9. **Promotion**
   - promote only passing bundle;
   - content hash/version;
   - immutable campaign artifacts;
   - preserve baseline for rollback/comparison.

10. **Runtime boundaries**
    - critic proposes;
    - policy/decision role accepts or rejects;
    - recovery actor executes only bounded accepted action;
    - environment actor owns simulator/robot writes.

## Evaluation dimensions

- success rate;
- recovery trigger precision;
- false positives;
- intervention frequency;
- task latency;
- recovery cost;
- regressions by task slice;
- robustness across held-out seeds;
- safety violations;
- infra-failure rate.

## Guardrails

- privileged simulator state cannot silently leak into task policy;
- infra failure is not a zero task score unless protocol defines it;
- development and held-out seeds must remain disjoint;
- a successful replay does not prove live safety;
- simulation success does not prove real-robot safety;
- physical deployment requires hardware-specific safety boundary and human oversight;
- never let critic directly bypass the action authority.

## Integração

`llm-observability-evaluation`, `empirical-prompt-tuning`, `agent-action-governance`, `multi-agent-orchestration`, `experiment-design`, `verify-before-claim`.

## Provenance

Adaptada de air-embodied-brain/Zetta-Embodiment. Preserva failure cluster → diagnose → candidate → shadow replay → paired same-seed gate → held-out promotion, com role separation e immutable campaign evidence. Não presume LIBERO, RoboCasa, Isaac, Ray, VLA checkpoints ou hardware robótico disponível.
