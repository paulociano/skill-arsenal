---
name: model-routing-gateway
description: "Projetar ou configurar roteamento de modelos LLM com seleção por capacidade, retries, fallback, orçamento e observabilidade."
---

# model-routing-gateway

## Objetivo

Projetar uma camada de roteamento entre múltiplos modelos/providers com políticas explícitas de seleção, fallback, retry, cooldown, orçamento, limites e observabilidade.

## Quando usar

- mais de um modelo/provider;
- necessidade de failover;
- custo/latência/SLA;
- modelos com capacidades diferentes;
- rate limits;
- multi-region ou múltiplos deployments;
- centralização de credenciais/políticas de chamadas.

## Princípios

1. **Routing policy is product logic.** Tornar critérios explícitos, não espalhados em ifs.
2. **Retry ≠ fallback.** Retry tenta novamente a mesma classe de destino; fallback troca destino/capacidade.
3. **Circuit break / cooldown.** Deployment falhando deve sair temporariamente do pool.
4. **Budget is a routing constraint.** Custo deve participar da seleção quando isso importa.
5. **Context/capability checks before call.** Evitar enviar uma requisição a um modelo que claramente não suporta o input.
6. **Observability per hop.** Registrar provider/model escolhido, tentativa, latência, custo, erro e fallback usado.

## Workflow

1. Definir grupos de modelos por capacidade e finalidade.
2. Escolher estratégia:
   - simple/random;
   - least-busy;
   - latency-based;
   - cost-based;
   - load/usage-aware;
   - regra customizada baseada em capability/confidence.
3. Definir:
   - timeout;
   - retry count;
   - max fallbacks;
   - allowed failures;
   - cooldown;
   - retry-after;
   - budget/parallelism;
   - pre-call checks.
4. Separar fallbacks por causa quando necessário:
   - erro geral;
   - context window;
   - capability mismatch;
   - provider outage.
5. Definir circuit breaker/cooldown.
6. Instrumentar logs/metrics.
7. Testar falhas reais ou simuladas:
   - timeout;
   - 429/rate limit;
   - provider indisponível;
   - context overflow;
   - resposta inválida.
8. Verificar que o fallback preserva o contrato funcional esperado.

## Segurança

- centralizar credenciais aumenta blast radius; usar least privilege;
- nunca logar secrets ou payloads sensíveis por padrão;
- mascarar dados sensíveis antes de observability/export;
- fallback para outro provider pode mudar data residency e privacy;
- não habilitar provider externo automaticamente só porque o principal falhou;
- content-policy fallback nunca deve ser usado para contornar controles de segurança.

## Regras

- mais modelos não significa mais resiliência se todos dependem da mesma infraestrutura;
- fallback sem limite vira cascata cara;
- retry agressivo piora incidentes e rate limits;
- selecionar pelo menor custo sem medir qualidade pode degradar o produto;
- selecionar pela menor latência sem capability gate pode quebrar tarefas.

## Runtime local incorporado de Ollama

Quando houver requisito de execução local/on-device:

- tratar o runtime local como um deployment/provider distinto, com capacidade, memória, contexto e throughput próprios;
- fixar modelo + tag/versão quando reprodutibilidade importa;
- distinguir tempo de **load** de tempo de **generation**;
- usar keep-alive somente quando o ganho justificar memória ocupada;
- medir prompt eval e generation separadamente quando o runtime expuser essas métricas;
- structured output local deve obedecer ao mesmo contrato de `structured-output-contract`;
- embeddings locais são uma opção de deployment, não uma garantia de qualidade de retrieval;
- não expor a API local em rede sem autenticação/controle apropriado.

Ollama é uma implementação possível do lado local. A metodologia vale também para llama.cpp/vLLM e runtimes equivalentes.

## Ferramentas e dependências

Usar esta skill para desenhar arquitetura ou configurar gateways reais quando o usuário tiver LiteLLM, Vercel AI Gateway, provider APIs ou infraestrutura equivalente. Não presumir que o assistente desta conversa controla roteamento interno de modelos.

## Integração

Combina com `graph-engineering`, `loop-engineering`, `library-version-grounding`, `structured-output-contract` e `verify-before-claim`.

## Referências

Adaptada de BerriAI/litellm.

Origem local: [model-routing-gateway.docx](../model-routing-gateway.docx).
