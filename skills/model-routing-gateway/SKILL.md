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

## Decision engines versus modelos gerativos

Nem toda decisão precisa de geração de texto. Classificadores, rerankers e **decision engines tipados** podem responder `choice`, score ordinal ou probabilidade binária sem produzir prosa.

Tratar esses motores como uma classe de deployment própria quando houver benefício mensurável de latência/custo:

- verificar se os critérios/opções podem ser definidos no runtime ou se o modelo exige labels fixas;
- medir qualidade no **domínio real**, não apenas benchmark do autor;
- validar idioma/script antes de rotear para checkpoints especializados;
- testar cardinalidade de labels: muitos options podem degradar modelos com budget compartilhado;
- calibrar probabilidades no domínio quando confidence aciona automação; confidence não é prova de correção;
- preferir fallback para modelo gerativo quando a decisão exige raciocínio aberto, explicação ou contexto além da capacidade do decision engine;
- registrar versão/checkpoint e parâmetros de calibração para reprodutibilidade;
- quando o engine só se torna competitivo após fine-tuning, tratar o dataset e a avaliação de holdout como parte da dependência operacional.

Modelos como SemIf ou Laya são implementações possíveis dessa arquitetura. Não presumir que estão instalados nem que benchmarks publicados transferem para o workload atual.

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
- selecionar pela menor latência sem capability gate pode quebrar tarefas;
- probabilidade calibrada em um benchmark não autoriza ação consequencial em outro domínio sem validação.

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

## Agregação de free tiers e cotas compartilhadas

Quando o pool combinar free tiers ou múltiplas chaves, aplicar estes checks adicionais:

1. **Orçamento efetivo.** Registrar limite, unidade, janela, reset, origem e validade por modelo, chave e pool de conta/projeto. Não somar cotas de modelos ou chaves que compartilham o mesmo pool. Limite desconhecido não significa ilimitado; números de catálogo não garantem capacidade disponível para a conta.
2. **Concorrência.** Reservar requisição e tokens estimados antes do dispatch, reconciliar com consumo observado e liberar reservas de forma idempotente também em erro/cancelamento. Definir expiração e recuperação após falha. Em múltiplos workers, usar coordenação compartilhada/atômica: leases somente em memória de um processo não protegem o pool global.
3. **Pressão versus bloqueio.** Usar headroom em cache para ordenar destinos, mas manter a admissão baseada em contadores e reservas atuais. Considerar a janela mais restritiva e confirmar o reset do provedor; não generalizar meia-noite UTC para todos.
4. **Origem do cooldown.** Separar indisponibilidade estimada, Retry-After/reset explícito, falta de crédito, autenticação inválida e restrição de plano. Usar probes com orçamento e jitter apenas para hipóteses de recuperação; uma chave autenticada não prova reposição de crédito nem acesso ao modelo. Nunca antecipar retry antes do prazo explícito, mesmo que ultrapasse o teto do backoff local.
5. **Limites aprendidos.** Ajustar limites com evidência inequívoca de unidade e escopo em headers/erros; registrar data e confiança. Não aumentar capacidade automaticamente por interpretação ambígua nem sobrescrever ajustes locais silenciosamente.
6. **Contrato por rota.** Testar endpoint, streaming, tools, JSON/schema, contexto e modalidade usados pelo cliente. Compatibilidade OpenAI não implica paridade de todas as APIs. Fixar grupo equivalente para pedido de modelo específico; degradar para outro modelo somente quando a política permitir, expondo o destino efetivo.
7. **Qualidade e privacidade.** Medir qualidade conforme os melhores destinos esgotam suas cotas. Impedir fallback para destinos fora da política de dados. Rotação de chaves não cria direito a cotas adicionais; respeitar os limites de conta e termos aplicáveis.

### Catálogo remoto e operação

- Tratar atualização de catálogo como mudança de configuração: verificar assinatura, schema, versão e frescor; manter estado anterior em falha.
- Preservar overrides, modelos desativados/excluídos pelo usuário e endpoints próprios. Separar disponibilidade anunciada, capacidade validada e permissão de uso.
- Assinatura comprova procedência/integridade, não exatidão de cotas, confiança em qualquer novo destino ou disponibilidade atual. Validar também a política local antes de ativar rotas.
- Separar credencial do gateway das chaves upstream; proteger chave mestra, backups, exportações e logs. Criptografia em repouso não protege contra comprometimento do processo que descriptografa.
- Fixar versão/digest antes de uma implantação reproduzível. Distinguir ferramenta pessoal em rede confiável de gateway público ou multi-tenant.
- Tratar síntese em painel de modelos e compressão de prompts como opções separadas: exigir benefício medido, orçamento e política de dados; não ativar só porque o gateway oferece.

### Verificação mínima deste cenário

| Cenário | Resultado exigido |
| --- | --- |
| Dois modelos/chaves compartilham cota de conta | Uso agregado respeita um único pool |
| Duas chamadas disputam a última vaga | Reserva atômica admite somente a capacidade restante |
| Provedor informa Retry-After maior que o teto local | Nenhuma tentativa antecipada |
| Chave válida, mas crédito/plano bloqueado | Probe de autenticação não reabilita a rota |
| Catálogo sem assinatura ou com modelo desativado localmente | Rejeitar atualização inválida e preservar decisão local |
| Pool gratuito só tem destinos sem tools/privacidade exigida | Retornar indisponibilidade explícita, sem degradar o contrato |

FreeLLMAPI é uma referência de implementação para esses padrões, não uma dependência instalada. Seu uso exige servidor real, credenciais próprias e validação do cliente. Um MCP exposto pelo produto não altera o modelo interno desta conversa nem está disponível sem conexão efetiva.

## Ferramentas e dependências

Usar esta skill para desenhar arquitetura ou configurar gateways reais quando o usuário tiver LiteLLM, Vercel AI Gateway, provider APIs ou infraestrutura equivalente. Não presumir que o assistente desta conversa controla roteamento interno de modelos. Decision engines especializados exigem runtime real e avaliação própria antes de entrar no pool.

## Integração

Combina com `graph-engineering`, `loop-engineering`, `library-version-grounding`, `structured-output-contract` e `verify-before-claim`.

## Referências

Adaptada de BerriAI/litellm.

Cotas, leases, origem de cooldown e catálogo: [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi/tree/a0befbc6718bbbf2d856c9cf08d01a92aefbe1e4). Ver [avaliação e limites da adaptação](../../evaluations/2026-09-26-freellmapi.md).

Decision engines tipados: [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) e [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya), usados como referências arquiteturais, não dependências do Arsenal.

Origem local: [model-routing-gateway.docx](../model-routing-gateway.docx).
