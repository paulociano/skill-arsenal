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
- para múltiplos browser workers/subagentes, preferir perfis de navegador separados e domain allowlists por worker quando o escopo permitir;
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

Perfis separados por browser worker, domain allowlists e composição de subagentes especializados refinados a partir de `PrettyPrinted/youtube_video_code` (2026-09-30, Pydantic AI Harness + browser-use), sem assumir proxies, Pydantic AI Harness ou browser-use como runtimes disponíveis.

Consolidada de [trycua/cua](https://github.com/trycua/cua), [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S), [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop), [microsoft/OmniParser](https://github.com/microsoft/OmniParser), [browser-use/browser-use](https://github.com/browser-use/browser-use) e [browserbase/stagehand](https://github.com/browserbase/stagehand). Preserva grounding, action-space, isolation, trajectories e evaluation sem exigir seus drivers, modelos, sandboxes ou clouds.

## Superfícies virtuais para agentes visuais (yomado)

Em desktop nativo, display virtual só deve ser considerado após verificar SO, permissões, ferramenta de screenshot/input real e janelas selecionadas. Dar nome ao workspace, registrar estado/geometria original e demonstrar screenshot fresco mais ação concreta antes de avançar. Display na mesma sessão não isola foco, teclado, mouse, clipboard, filesystem nem contas. Coordenar interferência com humano/outros agentes e restaurar janelas ao terminar, inclusive falhas. Testar separadamente fechamento, múltiplos displays e monitor desligado; uma demo limitada não prova estabilidade desassistida. Fonte: https://github.com/chekusu/yomado (2026-10-18), protótipo macOS com APIs privadas, não presente neste runtime.

## Diagnóstico por trace em automações de navegador (Browserbase, 2026-10-19)

Quando houver um navegador realmente controlável e captura autorizada de eventos, usar traces como evidência complementar à trajetória de ações:

1. **Capture**: isolar run id, URL/origin e janela temporal; observar eventos de network, console, runtime, navegação, DOM e screenshot sem instalar automaticamente CDP listeners ou abrir portas de depuração.
2. **Correlate**: associar ação, target, request/response, mudança DOM, screenshot, falha, retry e postcondition por timestamp e identificador de sessão.
3. **Bisect**: segmentar o trace por páginas/estados, buscar primeiro eventos pertinentes à falha e diferenciar erro de interface, erro de rede, auth e target desatualizado.
4. **Hypothesis**: ancorar causa provável em evidências, separar observação e inferência, reproduzir no mesmo estado e verificar depois da correção. Ausência de evento não demonstra ausência de bug quando trace é parcial.
5. **Derived API**: só em sistemas autorizados, extrair endpoints observados em traces, com path templating e esquema amostral; toda OpenAPI gerada é **observacional/incompleta**, não contrato oficial nem permissão de invocar interfaces não documentadas.
6. **Privacy**: mascarar cookies, auth headers, request/response bodies, dados pessoais e tokens antes de persistir/exportar; traces e dumps podem conter credenciais mesmo quando o script não pretende coletá-las.
7. **Portabilidade**: não presumir Node, `browse`, Browserbase, Stagehand, CDP, browser remoto, proxies ou capacidade de interceptar tráfego no ChatGPT. Sem observação real, entregar plano de instrumentação e marcar execução como não verificada.

Fontes: https://github.com/browserbase/skills/tree/main/skills/browser-trace e https://github.com/browserbase/skills/tree/main/skills/browser-to-api . Princípios adaptados, sem copiar scripts ou instalar serviços.
