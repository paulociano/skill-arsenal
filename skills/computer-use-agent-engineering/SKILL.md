---
name: computer-use-agent-engineering
description: "Projetar, avaliar e endurecer agentes que operam browser ou desktop por visão, DOM/accessibility tree ou abordagem híbrida, com grounding, action space observada, stale guards, isolamento, trajetória, human takeover e benchmarks reproduzíveis."
---

# Computer Use Agent Engineering

## Objetivo

Projetar computer-use agents capazes de perceber uma interface, escolher uma ação suportada, executá-la e verificar o novo estado sem depender de coordenadas frágeis ou loops cegos.

## Quando usar

Use para:
- agentes de browser/desktop;
- GUI automation baseada em visão;
- hybrid DOM + vision agents;
- sandboxes/VMs para execução;
- criação de datasets/trajectories;
- avaliação de computer-use.

Para verificar uma mudança de UI específica, use `runtime-ui-verification`.
Para operar um dispositivo somente quando controle real estiver disponível, siga a ferramenta/runtime correspondente.

## Loop

`observe → ground → plan → act → verify → reobserve`

### Observe
Capturar somente o necessário:
- screenshot;
- DOM/accessibility tree;
- janela/app/URL;
- estado de controles;
- cursor/viewport quando relevante.

### Ground
Transformar percepção em targets acionáveis:
- elemento;
- role/label;
- bounding box;
- stable node id;
- ação permitida.

Parsers visuais podem produzir ícones/regiões/labels, mas detecção não prova semanticamente a função.

### Plan
Escolher próximo passo pequeno.
Não gerar uma sequência longa quando o estado intermediário pode mudar.

### Act
- usar action space real;
- preferir semantic target a coordenada absoluta;
- revalidar target/fingerprint;
- consumir decisão uma vez para evitar double-submit.

### Verify
Declarar postcondition antes da ação.
Depois conferir estado, DOM, screenshot, output ou efeito externo.

## Estratégias de percepção

### DOM/accessibility
Melhor quando a interface expõe semântica confiável.

### Vision
Necessária quando:
- canvas;
- remote desktop;
- app nativo;
- elemento sem DOM útil;
- visual state é parte da decisão.

### Hybrid
Preferível quando uma modalidade pode corrigir a outra:
- DOM para target;
- vision para estado visual;
- screenshot parser para elementos não semânticos.

## Isolation

Para tarefas arriscadas ou treinamento:
- VM/container/profile separado;
- credenciais de teste quando possível;
- filesystem/workspace dedicado;
- network e clipboard limitados;
- reset entre episódios;
- snapshot/checkpoint quando útil.

Isolamento não substitui `agent-action-governance`.

## Human takeover

Defina estados:
- agent_control;
- help_requested;
- human_control;
- released.

Enquanto humano controla, não deixar o agente continuar clicando em paralelo.

## Trajectory

Uma trajectory útil registra:
- observação;
- action candidate;
- ação escolhida;
- target;
- resultado;
- postcondition;
- erro/recovery;
- timestamp/model/runtime version.

Evitar armazenar secrets em screenshots/traces quando puderem ser mascarados.

## Evaluation

Medir mais que task success:
- completion;
- steps;
- retries;
- stale-target rate;
- invalid-action rate;
- recoveries;
- latency/cost;
- safety violations;
- human interventions.

Benchmarks precisam:
- ambiente pinado;
- reset reproduzível;
- oracle verificável;
- tasks sem leakage da resposta;
- trajetória disponível para diagnóstico.

## Regras

- screenshot bonito não é grounding.
- coordinate-only automation é último recurso quando target semântico não existe.
- loop sem mudança útil precisa de budget/stop.
- toast de sucesso não substitui postcondition.
- um parser de UI não cria permissão para clicar.
- remote computer é uma superfície de alto impacto mesmo quando descartável.

## Integração

Combina com:
- `agent-action-governance`;
- `runtime-ui-verification`;
- `llm-observability-evaluation`;
- `behavior-contract-validation`;
- `multi-agent-orchestration`;
- `verify-before-claim`.

## Provenance

Consolidada de [trycua/cua](https://github.com/trycua/cua), [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S), [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop), [microsoft/OmniParser](https://github.com/microsoft/OmniParser), [browser-use/browser-use](https://github.com/browser-use/browser-use) e [browserbase/stagehand](https://github.com/browserbase/stagehand). Preserva grounding, action-space, isolation, trajectories e evaluation sem exigir seus drivers, modelos, sandboxes ou clouds.
