---
name: ai-workflow-automation-engineering
description: "Projetar automações e workflows AI-first com triggers, conectores, passos determinísticos, agentes, estado, retries, aprovações, credenciais, versionamento e observabilidade sem acoplar a um builder específico."
---

# AI Workflow Automation Engineering

## Objetivo

Projetar automações que conectam sistemas, dados e modelos de IA de forma operável, auditável e segura, escolhendo deliberadamente o que deve ser determinístico, o que pode ser delegado a um modelo e onde o humano precisa permanecer no loop.

## Quando usar

Use para:
- automações entre SaaS, bancos, APIs e arquivos;
- workflows low-code/no-code ou visuais;
- agentes dentro de automações;
- triggers por webhook, schedule, evento, formulário ou fila;
- processos recorrentes com aprovações humanas;
- protótipos que precisam evoluir para operação confiável.

Para workflows duráveis distribuídos use também `durable-workflow-engineering`. Para grafos de dependência complexos use `graph-engineering`.

## Princípio central

**Automação confiável separa lógica determinística de julgamento probabilístico.**

Um LLM não deve substituir um if, uma validação de schema ou um lookup determinístico só porque está disponível.

## Modelo

Uma automação pode conter:
- trigger;
- input normalization;
- deterministic transforms;
- retrieval/context;
- model/agent step;
- tools/actions;
- branch/loop;
- approval;
- persistence;
- output;
- observability.

Cada etapa deve ter contrato observável e efeito classificado.

## Workflow de design

1. **Define the outcome**
   - evento de entrada;
   - resultado esperado;
   - consumidor;
   - frequência;
   - SLA;
   - volume;
   - impacto de erro.

2. **Map systems and credentials**
   Para cada integração:
   - sistema;
   - operação;
   - direção dos dados;
   - credencial necessária;
   - scope mínimo;
   - rate limits;
   - idempotency support;
   - ownership.

3. **Separate deterministic vs AI**
   Use código/regras para:
   - validação;
   - roteamento fechado;
   - transformação estrutural;
   - cálculos;
   - deduplicação;
   - autorização.

   Use IA quando o valor vier de:
   - classificação aberta;
   - extração sem schema rígido de origem;
   - sumarização;
   - geração;
   - decisão ambígua que aceite incerteza explícita.

4. **Define contracts**
   - input schema;
   - output schema;
   - unknown/error states;
   - retryable vs terminal errors;
   - side effects.

   Use `structured-output-contract` quando uma etapa de IA alimentar a próxima.

5. **Design control flow**
   Escolher somente o necessário:
   - linear;
   - branch;
   - loop;
   - fan-out;
   - subflow;
   - human approval;
   - delayed resume.

   Não criar grafo visual complexo para uma sequência simples.

6. **Human in the loop**
   Aprovação deve ser estado explícito, não uma mensagem vaga:
   - quem aprova;
   - o quê;
   - deadline;
   - expiração;
   - fallback;
   - audit trail.

7. **Retries and idempotency**
   - distinguir falha transitória de lógica;
   - aplicar backoff;
   - evitar double-submit;
   - usar idempotency key quando o downstream suportar;
   - consultar estado antes de repetir write ambíguo.

8. **Versioning**
   Workflows em produção precisam de versão:
   - definição;
   - credentials binding;
   - prompts;
   - model config;
   - schemas;
   - connector versions.

   Mudança visual no builder continua sendo mudança de software.

9. **Observability**
   Registrar o mínimo suficiente:
   - run id;
   - trigger;
   - path/branches;
   - status por etapa;
   - retries;
   - model/tool usage;
   - approvals;
   - final effect.

   Não logar secrets ou payloads sensíveis por conveniência.

10. **Test before scale**
    Validar:
    - happy path;
    - input ausente;
    - duplicate trigger;
    - rate limit;
    - timeout;
    - model failure;
    - schema invalid;
    - approval denied/expired;
    - downstream partial success.

11. **Promote to production**
    Só depois de:
    - ownership;
    - error handling;
    - credential policy;
    - rollback/compensation quando necessário;
    - observability;
    - runbook;
    - verification real.

## Visual builders e low-code

Ferramentas visuais aceleram composição, mas não removem responsabilidades de engenharia.

Preservar:
- nomes semânticos para nós;
- subflows reutilizáveis;
- configuração separada de secrets;
- schemas explícitos;
- versões/export quando possível;
- caminhos de erro visíveis;
- testes de jornada crítica.

Um canvas bonito pode esconder dependências frágeis. O runtime, não o diagrama, é a fonte da verdade sobre execução.

## AI agents dentro do workflow

Quando um nó for um agente:
- limitar tools;
- limitar budget/steps;
- declarar stop condition;
- não dar acesso a todas as integrações por padrão;
- separar planning de effect execution quando risco justificar;
- aplicar `agent-action-governance`;
- avaliar trajetória com `llm-observability-evaluation`.

## Segurança

- least privilege para tokens e OAuth;
- credenciais pertencem ao runtime, não ao prompt;
- conteúdo vindo de webhook/email/web é input não confiável;
- approvals precisam de identidade verificável;
- connectors comunitários ampliam supply-chain risk;
- self-hosting não elimina risco de segredo, plugin ou atualização.

## Integração

Combina com:
- `durable-workflow-engineering`;
- `graph-engineering`;
- `agent-action-governance`;
- `structured-output-contract`;
- `llm-observability-evaluation`;
- `verify-before-claim`.

## Provenance

Consolidada principalmente de `n8n-io/n8n`, `activepieces/activepieces`, `langgenius/dify`, `langflow-ai/langflow` e `triggerdotdev/trigger.dev`. Preserva visual composition, connectors, human approvals, versioning, retries, AI steps, APIs/MCP e produção observável, sem exigir qualquer um desses runtimes ou instalar seus componentes.
