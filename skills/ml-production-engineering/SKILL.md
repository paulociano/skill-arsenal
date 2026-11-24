---
name: ml-production-engineering
description: "Projetar e operar sistemas de machine learning do dado à produção com testes, avaliação, serving, monitoramento e ciclos seguros de melhoria."
---

# ml-production-engineering

## Objetivo

Levar workloads de machine learning de experimentos para sistemas operacionais reproduzíveis, testáveis e observáveis, sem confundir qualidade offline do modelo com valor ou confiabilidade em produção.

## Quando usar

- projeto de ML que precisa sair de notebook para produção;
- pipeline de data/train/evaluate/serve;
- MLOps, CI/CD ou continual training;
- validação de dados e modelos;
- monitoramento de drift, performance ou qualidade;
- revisão de arquitetura de sistemas de ML.

Para aplicações puramente LLM, combinar ou preferir llm-observability-evaluation nas partes específicas de prompts, traces e judges.

## Princípio central

O modelo é um componente. O sistema inclui dados, features, training code, artifacts, serving, monitoring, feedback e operação.

## Lifecycle

1. Design
2. Data
3. Train
4. Evaluate
5. Package
6. Deploy
7. Observe
8. Learn
9. Retrain ou rollback

Cada transição deve ter artefato, versão e critério de promoção quando o risco justificar.

## Workflow

### 1. Definir tarefa e valor

- usuário e decisão suportada;
- target e prediction horizon;
- custo de false positive/false negative;
- baseline simples;
- métrica offline;
- métrica de produto/negócio;
- latency/cost/availability constraints.

### 2. Data contract

- schema;
- ranges/categories;
- nullability;
- uniqueness;
- leakage checks;
- train/validation/test split;
- freshness e provenance.

Qualidade do dataset precisa ser testada como código quando possível. Um pipeline verde com schema quebrado não é válido.

### 3. Experiment tracking

Registrar:
- dataset/version;
- code commit;
- features/config;
- seed;
- environment;
- model artifact;
- metrics;
- evaluation slices.

Sem esses vínculos, resultado não é reproduzível.

### 4. Training

- separar data loading, transforms, model e training loop;
- tornar configuração explícita;
- guardar artifacts e metadata;
- medir recursos e duração quando relevantes;
- não promover apenas pelo training metric.

### 5. Evaluation

Avaliar:
- holdout realmente não usado no tuning;
- baseline versus candidate;
- métricas globais e slices;
- calibration quando probability é usada;
- robustness/edge cases;
- latency e resource cost;
- thresholds ligados à decisão de produto.

### 6. Testing

Separar:
- unit tests de transforms/lógica;
- data quality tests;
- integration tests do pipeline;
- artifact/serialization tests;
- serving contract tests;
- regression tests com fixtures representativas.

### 7. Serving

Definir:
- batch, async ou online;
- input/output schema;
- preprocessing parity;
- model/version loading;
- timeout;
- fallback;
- concurrency;
- resource limits;
- rollback.

Training-serving skew deve ser tratado como risco explícito.

### 7.1. Serving de modelos e decision engines

Para inferência GPU com concorrência, definir antes do deploy:
- política de batching e espera adaptativa;
- prefix/KV cache e seu limite de memória;
- warmup de kernels e buckets de comprimento;
- admission control, backpressure e respostas de overload;
- limites de tokens por linha, request e fila;
- cancelamento de requests e limpeza de trabalho em andamento;
- separação entre tempo de load, prefill, inferência aquecida e p95/p99.

Comparar pelo mesmo workload, número de perguntas, comprimento, concorrência, dtype, quantização e hardware. Um número de latência isolado não demonstra throughput nem qualidade. Para outputs probabilísticos, medir accuracy, NLL/ECE e calibração por tipo de pergunta e slice, além de erro de serviço.

### 8. Deployment gate

Promover somente artifact/version avaliado. Registrar qual código, dados e config produziram o modelo servido.

Canary, shadow ou staged rollout podem ser usados quando o impacto justificar.

### 9. Monitoring

Monitorar dimensões diferentes:

- service health: latency, errors, saturation;
- data health: schema, missingness, ranges, drift;
- prediction health: distribution, confidence/calibration;
- model quality: quando labels/outcomes chegam;
- business outcome;
- cost e resource utilization.

Drift sozinho não prova degradação. Degradação sem drift também é possível.

### 10. Continual learning

Novo training deve ser um experimento comparável ao modelo atual:

- trigger definido;
- dataset versionado;
- mesmas gates ou gates atualizadas explicitamente;
- champion/challenger ou baseline/candidate;
- rollback;
- não promover automaticamente apenas porque o treino terminou.

## CI/CD para ML

Separar code CI de model promotion.

Uma PR pode:
- rodar testes;
- construir artifact;
- treinar candidate;
- avaliar;
- publicar resultados comparáveis.

A produção só muda quando o gate de promoção autorizado é satisfeito.

## Segurança e governança

- secrets fora de notebooks e artifacts;
- PII minimizada e com acesso controlado;
- dataset e model artifacts com provenance;
- dependências pinadas onde reprodutibilidade importa;
- registrar limitações, slices frágeis e known failure modes;
- não afirmar monitoramento de quality quando labels ainda não existem.

## Ferramentas e dependências

Adaptar ao stack real. Ray, MLflow, Great Expectations, Kubernetes, cloud services e frameworks específicos são opções, não requisitos. Confirmar versões e APIs antes de propor comandos concretos.

## Integração

Combina com experiment-design, llm-observability-evaluation, tdd, model-routing-gateway, structured-output-contract, system-design-engineering e verify-before-claim.

## Referências

Adaptada de https://github.com/GokuMohandas/Made-With-ML, preservando o ciclo design → develop → deploy → iterate, testes de dados/modelos, evaluation, serving e continual learning sem exigir Ray/Anyscale ou a stack da fonte.

## Serving de visão temporal e múltiplos streams (Tamserve, 2026-11-24)

Para pipelines autorizados de segmentação/tracking de objetos em vídeo ao vivo, estender o contrato de serving com estado temporal explícito:
- Separar pesos compartilháveis, encoding por frame/stream e estado por objeto/stream; limitar histórico às dependências reais do modelo. Nunca compartilhar memória temporal entre streams por acidente.
- Batch dinâmico com limites de memória e latência, agrupando entradas de shape/estado compatível; medir encoding, tracking e latência ponta a ponta. Diferenciar throughput agregado de FPS efetivo por stream e idade do frame.
- Definir política de backpressure e descarte: latest-frame para aplicações que toleram perda, processamento integral quando cada frame é necessário. Medir impacto sobre drift, oclusão e recuperação, não apenas velocidade.
- Dar identidade a stream/frame/objeto; prever start, stop, correção/reset, entrada tardia, desconexão e reentrada. Adicionar objeto ao frame corrente não pode avançar duas vezes o estado dos demais.
- Comparar com implementação de referência em mesmo modelo, hardware, resolução e workload; medir qualidade de máscara/tracking, memória com duração e concorrência crescentes, p95 de latência, isolamento e soak. Precisão offline semelhante não prova qualidade ao vivo.
- Exigir finalidade autorizada, minimização/retenção e proteção de imagens; não usar como autorização para vigilância de pessoas. Confirmar GPU/runtime, licença e origem dos pesos antes de execução.

Should-trigger: desenhar serving de segmentação de objetos em vários fluxos de vídeo. Near-miss: recortar uma imagem estática ou editar um clipe simples. Fonte: https://github.com/aryamandarda/tamserve (README e docs/how-it-works.md). SAM, PyTorch, pesos, câmeras e GPUs não foram executados/importados; resultados publicados são dos autores.
