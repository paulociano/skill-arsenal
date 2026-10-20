---
name: software-factory-operations
description: "Operar uma software factory com agentes usando fila durável, charter de autonomia, triage, spec gates, implementação limitada, verificação independente, back-pressure de revisão e merge humano."
---

# Software Factory Operations

## Objetivo

Transformar entrega de software assistida por agentes em um loop operacional repetível, reiniciável e auditável, sem automatizar julgamento humano de alto impacto.

## Quando usar

- triage automatizado de issues;
- implementação agentic em fila;
- software factory;
- sessões independentes que precisam continuar o mesmo trabalho;
- review queue com back-pressure;
- implementação + verifier separado;
- automação recorrente de manutenção de código.

## Princípio central

**Autonomia deve acompanhar consequência, não dificuldade.**

Uma mudança longa e mecânica pode ser segura para automação; uma mudança pequena em auth, billing ou dados pode exigir gates humanos.

## Modelo

Separar:
- **Charter**: escopo permitido, risco, protected paths, stop conditions;
- **Queue**: trabalho durável e visível;
- **Handoff**: contrato entre runs;
- **Worker**: executor efêmero;
- **Gates**: checks determinísticos;
- **Verifier**: revisão independente;
- **Human review**: decisão final;
- **Monitor**: feedback do sistema em produção.

## Workflow

1. **Charter**
   - tipos de trabalho permitidos;
   - paths/sistemas protegidos;
   - tier de autonomia;
   - checks obrigatórios;
   - limite máximo de itens aguardando revisão;
   - condições de parada.

2. **Triage**
   - classificar issue em:
     - ready-to-implement;
     - ready-to-spec;
     - needs-info;
     - blocked;
   - registrar por que;
   - não converter ambiguidade de produto em código especulativo;
   - tarefas de triage podem usar um modelo mais barato ou regra determinística quando o objetivo é apenas filtrar/rotear, preservando o modelo mais capaz para decisões que exigem julgamento real.

3. **Claim e freshness**
   - uma unidade de trabalho por run;
   - claim determinístico e atômico;
   - primeiro claim válido vence;
   - colisão deve falhar fechada, não criar dois writers;
   - antes de publicar resposta ou ação derivada de contexto compartilhado, verificar se surgiram mensagens, commits ou decisões mais novas;
   - resposta baseada em cursor/estado stale deve ser retida e reavaliada contra o contexto novo, não publicada por inércia.

4. **Spec gate**
   Quando intenção ou design não forem triviais:
   - produto;
   - comportamento observável;
   - desenho técnico;
   - slice de implementação;
   - aprovação humana antes de avançar quando o risco justificar.

5. **Implement**
   - branch/worktree isolado;
   - escopo mínimo;
   - teste que reproduz a falha/contrato quando aplicável;
   - mudança;
   - checks definidos no charter.

6. **Deterministic gates**
   - typecheck;
   - lint;
   - tests;
   - build;
   - security/audit;
   - architecture checks quando definidos.

   Gate ausente que deveria existir é MISCONFIGURED, não PASS.

7. **Independent verifier**
   - lê diff e spec friamente;
   - ignora a narrativa do writer;
   - tenta refutar o claim;
   - quando possível, remover/reverter a fix e confirmar que o teste falha;
   - uncertainty suficiente deve bloquear promoção.

8. **Draft PR**
   - somente após gates e verifier;
   - inclui evidência;
   - não faz merge automático.

9. **Back-pressure**
   - review queue possui limite numérico;
   - quando cheio, parar de produzir novos itens;
   - o gargalo real é julgamento humano pendente, não número de agentes disponíveis.

10. **Human decision**
    - review;
    - request changes;
    - close;
    - merge.

11. **Monitor**
    - observar branch principal, regressões e factory health;
    - novos findings voltam para a fila como issues;
    - não reabrir automaticamente trabalho resolvido sem nova evidência.

## Durable state

A factory não depende de memória da sessão.

Preferir estado durável em:
- issues/labels;
- PRs;
- committed policy;
- handoff records;
- test artifacts;
- run receipts.

Sessões devem poder começar frescas e continuar a partir desse estado.

## Guardrails

- writer não aprova o próprio trabalho;
- agents não alteram silenciosamente o charter;
- merge permanece humano;
- hooks são guardrail, não boundary final;
- branch protection/ruleset é enforcement mais forte quando disponível;
- scheduled automation deve respeitar as mesmas policies de ações interativas;
- green infrastructure run não equivale a task success;
- queue cheia deve interromper produção, não esconder review debt.

## Integração

`software-engineering-cycle`, `agent-action-governance`, `multi-agent-orchestration`, `software-testing-engineering`, `code-review`, `behavior-contract-validation`, `production-go-live`.

## Provenance

Adaptada de addyosmani/factory e enriquecida por padrões de coordenação observados em yetone/cumora. Preserva charter humano, queue durável, autonomy-by-consequence, fail-closed gates, verifier independente, review back-pressure e merge humano. De Cumora foram absorvidos freshness gate antes de responder/agir, claims atômicos sobre unidades reais de trabalho e triage econômico; o runtime, chat, Kubernetes e infraestrutura específicos não são requisitos. Remove dependência de Claude routines, hooks e instaladores específicos; GitHub é uma implementação possível, não requisito conceitual.

## Isolamento, contratos e integração entre lanes

Inspirado na fábrica demonstrativa `PromtEngineer/software-factory`:

1. **Sandboxes por etapa**: quando houver runtime de execução isolada, cada lane de triage, worker e verifier recebe ambiente efêmero dedicado, criado de snapshot identificado (base commit e dependências pinadas). No ambiente ChatGPT/GitHub sem Upstash Box, usar branches e worktrees somente onde as ferramentas realmente permitirem; não prometer sandbox provisionada.
2. **Handoff tipado**: emitir por unidade `issue_id`, `base_sha`, `branch`, `status`, `summary`, `files_changed`, `tests_added`, `checks`, `artifacts`, `risk`, `next_action`; validar schema e transições entre etapas. Falha de schema deve bloquear promoção.
3. **Verifier em checkout limpo**: reexecutar testes fora do ambiente do writer e analisar diff contra issue e critérios; comparar evidência de testes declarada com saídas observadas. Manter casos ocultos/holdout fora do contexto do writer quando houver mecanismo legítimo para isso.
4. **Integração como gate distinto de PR**: PR isolado aprovado não prova compatibilidade com outros PRs. Integrar branches ordenadamente numa branch temporária, documentar conflitos, revisar resoluções, executar suíte completa após cada merge e preservar rastreabilidade por commit. Não fazer merge em branch protegida automaticamente.
5. **Métricas de factory**: registrar throughput, triaged-out, custo por issue, falhas de gate, conflitos de integração, regressões em holdout e review debt. Distinguir tempo de execução paralela de custo total de integração.
6. **Credenciais e rede**: preferir token mínimo por repo, injeção de secrets fora da visibilidade do agente, allowlist de egress e budget por lane; não carregar env completo no contexto do modelo. Testar política de acesso ao criar snapshots.
7. **Limites**: não equiparar relato de benchmark do projeto a garantia de qualidade; preservar independência do teste. Quando o usuário não dispõe de runtime isolado, executar apenas as etapas comprovadamente suportadas.

**Proveniência complementar:** https://github.com/PromtEngineer/software-factory (README, src/factory.ts, src/upstash.ts, src/integrate.ts, src/score.ts descritos no projeto; avaliação de 2026-10-15). Tecnologia de referência: Node 22+, Claude Code, Upstash Box, GitHub e Context7. Esses componentes não são pressupostos como instalados, e nenhum script do projeto foi executado na avaliação.

## Loop de melhoria por controle mensurável

Quando a fábrica automatizar manutenção **recorrente e incremental** de um codebase, desenhar explicitamente um feedback loop:

- **Set point:** propriedade e escopo a melhorar, com alvo observável, por exemplo reduzir ocorrências de uma regra legada.
- **Sensor:** medição repetível (lint, teste, AST, telemetria ou consulta), com versão, baseline e falhas detectáveis.
- **Controller:** seleção do menor incremento útil com prioridade, orçamento de mudança e back-pressure.
- **Actuator:** agente ou script executando a mudança sob charter de permissões, padrão exemplar e gates de teste.
- **Disturbances:** alterações concorrentes, mudanças de dependências e outros elementos que alteram a medição.
- **Dampener opcional:** quality gate que impede regressão em PRs mesmo antes do objetivo final.

Validar sensor e controller isolados antes de automatizar. Exigir PR/revisão humana para efeitos relevantes, controle de credenciais, idempotência e parada em caso de medição inconsistente. Uma automação agendada só existe se runner, credenciais, workflows e permissões estiverem realmente provisionados e testados.

Não instalar um agente headless ou escrever GitHub Actions apenas porque o padrão externo os sugere; adaptar ao runtime real e ao escopo do repositório.

**Origem adaptada:** https://github.com/humanlayer/skills/blob/main/plugins/design-control-loop/skills/design-control-loop/SKILL.md

## Ratchet de arquivos grandes sem automação cega

Quando o usuário pedir limitar complexidade por tamanho de arquivo, medir antes de impor um novo hook:

1. Identificar arquivos-fonte oversized usando o tokenizer real quando disponível; uma aproximação bytes/4 serve só para triagem, nunca para declarar tokenização exata.
2. Separar código autoral de vendored/gerado e ler o contrato de qualidade do repositório.
3. Para cada arquivo prioritário, encontrar limites semânticos (responsabilidade, módulo, estado, API), não dividir mecanicamente por linhas; confirmar que a extração preserva comportamento com testes existentes.
4. Estabelecer orçamento ou baseline por arquivo, com exceções justificadas e registradas, e priorizar evitar crescimento do débito enquanto a migração acontece.
5. Tratar pre-commit hooks, dependências e scripts como mudanças de infraestrutura sujeitas à aprovação explícita, especialmente quando bloqueiam commits de outros desenvolvedores.
6. Verificar que o controle realmente recusa uma regressão em ensaio seguro, desfazer os probes e registrar impacto sobre CI, contributors e arquivos legados.

**Origem (A/D, adaptado):** https://github.com/dzhng/skills/blob/main/skills/engineering/ratchet-files/SKILL.md. Não instalar por padrão Node, scripts ou hooks da origem.

## Back-pressure por loop e feedback persistente (HumanLayer, 2026-10)

Em automações recorrentes de coding agents, complementar o limite global da review queue com **limite por loop**:

1. Identificar cada loop por ID/label estável e definir teto de PRs abertos pendentes de revisão. **Um PR aberto por loop** é ponto de partida prudente, ajustável pelo charter e capacidade humana, não regra universal.
2. Antes da execução agendada, consultar **estado remoto atual**, inclusive PRs do mesmo loop; ao atingir o teto, registrar estado explícito de back-pressure e não criar novo branch/PR. Diferenciar de falha do sensor, falta de trabalho e sucesso do agente.
3. Reprocessar feedback no PR existente quando autorizado, em vez de criar PRs duplicados. Overrides manuais devem ser explícitos, auditáveis e sujeitos às mesmas políticas de permissão, escopo e validação.
4. Manter registro curto/versionado de **feedback permanente**: exclusões de escopo, falsos positivos conhecidos e critérios de reviewers. Não confundir com logs efêmeros, instrução de execução isolada, tokens ou regras já descritas na skill.
5. Se comentários em PR ou issues dispararem agentes, exigir autorização do autor/ator, validação do alvo e branch, proteção contra prompt injection e limites de segredos/escrita. Marcador em comentário ou label **não é** autorização suficiente.
6. Validar sensor, controller e actuator isoladamente, depois testar workflow e bloqueio de PRs pendentes. Agendamento, CI e GitHub Actions só existem operacionalmente quando configurados e verificados no repositório de destino.

**Origem metodológica:** [HumanLayer / build-iterated-agentic-loop](https://github.com/humanlayer/skills/blob/main/plugins/build-iterated-agentic-loop/skills/build-iterated-agentic-loop/SKILL.md) e [design-control-loop](https://github.com/humanlayer/skills/blob/main/plugins/design-control-loop/skills/design-control-loop/SKILL.md). Absorvidos back-pressure, feedback e verificação; sem instalar CLI, scripts, workflows, secrets ou handlers de comentários.
