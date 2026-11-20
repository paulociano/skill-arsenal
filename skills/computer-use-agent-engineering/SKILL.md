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

Reavaliação 2026-11-09: `bytedance/UI-TARS-desktop` foi **arquivado** (read-only) em 2026-11-09 e segue apenas como referência de método; não adotar seu runtime. Agent S continua exigindo um grounding model separado (UI-TARS-1.5) e executa código Python para controlar a máquina. Detalhes em `evaluations/2026-11-09-thirteen-agent-automation-repositories.md`.

## Escolha de runtime e higiene de fontes (2026-11-09)

Antes de adotar um runtime externo de agente de computador ou navegador:

1. **Preferir o que já é nativo e supervisionado.** Computer use nativo e extensão de navegador com aprovação por ação cobrem tarefas pontuais; runtime externo só entra quando houver ganho comprovado (execução recorrente, desassistida ou em lote).
2. **Rotear pela natureza da tarefa.** Rotina web recorrente sem código, com login/2FA e download → workflow RPA visual (ex.: Skyvern). Automação dentro de um projeto de código, com extração tipada → SDK com `observe/act/extract` (ex.: Stagehand). Tarefa pontual → ferramenta nativa.
3. **Checar manutenção.** Repositório arquivado, sem release recente ou mantido por uma pessoa não deve controlar máquina com dados reais.
4. **Checar onde a sessão roda.** Operadores "remotos" ou "gratuitos" em infraestrutura do fornecedor expõem telas, cookies e dados exibidos; para dados de clientes, exigir execução local ou em ambiente controlado.
5. **Checar telemetria e custos ocultos.** Telemetria ligada por padrão, grounding model hospedado pago, proxies anti-bot só na versão cloud.
6. **Credenciais fora do modelo.** Usar observação para obter seletores e preencher segredos por código ou cofre; o modelo nunca recebe a senha.

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


## Separação de abas privadas e operadas por agentes (Yab, 2026-11-18)
Em desenho de browsers com agentes, tratar **perfil/aba privada** e **aba delegada** como limites de autorização: o agente não deve poder enumerar, ler, observar histórico, extrair cookies ou agir em abas privadas; implementar tal fronteira no browser, não apenas em prompt. Permitir que o agente use uma sessão autenticada somente com o escopo concedido, com confirmação para enviar, pagar, excluir ou alterar permissões. Registrar quais dados de página entram no contexto e são enviados ao provedor do modelo; histórico full-text, snippets e memórias são stores distintos com retenção e opt-out. Verificar separação entre armazenamento local, sync criptografado e telemetria. Não assumir que duas engines (WebKit/Chromium) isolam credenciais ou ferramentas por padrão. Proveniência: https://github.com/yetanotherbrowser/yab (README e `docs/privacy.md`); aplicativo macOS, não conectado ao ChatGPT.


## Captura e replay de fluxos determinísticos (Ui.Vision, WebBrain, BrowserKitten; 2026-11-19)

Quando uma tarefa browser/desktop for recorrente e a sequência puder ser reproduzida, avaliar a passagem **trajetória observada → macro parametrizada → replay controlado** em vez de exigir que um LLM redescubra cada clique:

1. Capturar uma execução autorizada e bem-sucedida com targets, condições prévias, parâmetros, postconditions e pontos onde a interface muda.
2. Separar valores voláteis (IDs, senhas, datas, dados de clientes) da definição da macro. Não gravar cookies, tokens, senhas, prompts sensíveis ou screenshots de clientes em exemplos compartilháveis.
3. Preferir API/DOM/alvos semânticos observados; usar OCR/matching visual apenas quando necessário, com resolução, escala e idioma como condições explícitas.
4. Introduzir checkpoints após mudanças de página, downloads, salvamentos e formulários. Em erro de target, pausar/reobservar; não repetir cegamente uma ação potencialmente não idempotente.
5. Exigir aprovação humana para submissão, compra, envio, exclusão, troca de permissões e outras ações consequenciais. Um plano aprovado não autoriza efeitos externos ilimitados.
6. Fazer replay em ambiente de teste com estado inicial definido; comparar outputs, quantidade de etapas, falhas, intervenções e efeitos externos. Diferenciar script gerado, macro salva e execução real verificada.
7. Para watches e follow-ups, definir gatilho, frequência, limite de tentativas, condição de parada, horário de operação e dependência de browser/computador ativo. Só prometer execução programada quando uma ferramenta conectada a suportar.

Referências: https://github.com/A9T9/RPA (macros e ponte MCP externa); https://github.com/webbrain-one/webbrain (modos read-only/act/dev, plano aprovado e workflows); https://github.com/Player-YN/BrowserKitten (execução em sessão local e follow-ups). As extensões, bridge MCP, OCR, controle de desktop e agendadores locais **não** são ferramentas presumidas disponíveis no ChatGPT. Revisão estática dos READMEs em 2026-11-19.


## Controle de sessão, pareamento e handover em browsers locais (BrowserSkill e Browser MCP, 2026-11-19)

Em arquiteturas onde agente/CLI/MCP controla uma **extensão no navegador já autenticado do usuário**, tratar transporte conectado, autorização de dispositivo, autorização de aba e autorização de ação como quatro estados separados:

1. **Identidade e pareamento:** para ponte extension↔daemon usar loopback ou WSS autenticado, confirmação explícita de identidade/código, segredo de pareamento curto e descartável, tokens em storage restrito, revogação e renovação verificáveis. Um socket aberto ou daemon respondendo não prova identidade; pareamento opcional sem verificação deixa risco de impersonação. Não instalar `npx ...@latest` nem `curl | sh` para fazer esta avaliação.
2. **Boundaries de sessão:** inventariar browser/profile, tab IDs scoped, task ID, URL/origin e dono de cada aba. Uma janela dedicada ajuda a distinguir a tarefa, mas **compartilhar perfil também compartilha logins**; janela dedicada não é sandbox. Para abas existentes, exigir empréstimo explícito, retorno e handover; não enumerar nem controlar abas privadas sem grants específicos.
3. **Human takeover:** exibir controle ativo, permitir Stop/hold, suspender comandos enquanto pessoa usa a aba, reobservar e reconciliar mudanças humanas antes de retomar. Movimento manual da aba, desconexão, troca de perfil ou perda de autorização invalidam a sessão; não reassociar um ID antigo a outra aba.
4. **Resultado desconhecido:** timeout de chamada, diálogo nativo ou desconexão após submissão gera `effect_unknown`; sincronizar e consultar estado atual antes de qualquer retry não idempotente. Não tratar retorno técnico como sucesso de negócio.
5. **Remote bridge:** diferenciar onde ficam o browser, daemon, agente e logs; verificar WSS, política de origem, grants por dispositivo e revogação de sockets vivos. Um servidor remoto pareado pode operar logins existentes e precisa de aprovação e minimização de dados, não apenas autenticação do canal.
6. **Auditoria mínima:** para cada operação autorizada, preservar task/session ID, horário, origem, alvo, ação, resultado confirmado/unknown e intervenção, com retenção e exclusão configuráveis. Redigir valores, secrets, URLs completas sensíveis, screenshots e corpos de resposta por padrão. Registro parcial não comprova conclusão da tarefa.
7. **Acceptance:** pareamento de navegador A não deve abrir aba no perfil B; Stop precisa impedir **novas** ações; após timeout em envio, o agente não deve reenviar até reconciliar; aba emprestada deve retornar ao proprietário após encerramento normal. Near-miss: consulta apenas textual, sem controle de browser, não exige daemon, pareamento nem sessão.

Fontes: https://github.com/Tencent/BrowserSkill (`crates/bsk-cli/skill/SKILL.md`, `docs/local-pairing.md`, `docs/remote-extension-connection.md`, `docs/operation-audit.md`) e https://github.com/BrowserMCP/mcp (`README.md`, `packages/mcp/README.md`). Metodologias adaptadas sem executar extensões, scripts, CLI, ponte CDP ou MCP; documentação consultada em 2026-11-19. Apenas usar runtime conectado e efetivamente autorizado no ambiente atual.
