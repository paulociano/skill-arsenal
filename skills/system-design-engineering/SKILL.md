---
name: system-design-engineering
description: "Projetar sistemas escaláveis a partir de requisitos, estimativas, trade-offs, componentes, dados, falhas e evolução operacional."
---

# system-design-engineering

## Objetivo

Projetar ou revisar sistemas distribuídos e aplicações de escala não trivial de forma rastreável, partindo de requisitos e restrições antes de escolher arquitetura.

## Quando usar

- system design de um produto ou serviço;
- arquitetura para alto volume, disponibilidade ou crescimento;
- escolha entre cache, filas, bancos, replicação, sharding ou CDN;
- revisão de arquitetura com gargalos e failure modes;
- preparação prática para entrevistas de system design.

Não usar apenas para desenhar um diagrama. Para visualização de uma arquitetura já definida, preferir architecture-visualization.

## Princípio central

Tudo é trade-off. Uma arquitetura só é boa em relação a workload, constraints, SLOs e custos explícitos.

## Workflow

1. **Scope**
   - listar casos de uso essenciais;
   - separar requisitos funcionais e não funcionais;
   - explicitar usuários, regiões, compliance e limites.

2. **Workload**
   - estimar ordem de grandeza de usuários, requests, read/write ratio, payload, storage e crescimento;
   - marcar estimativas como assumptions;
   - não criar precisão falsa quando faltam dados.

3. **SLOs e constraints**
   - disponibilidade;
   - latency;
   - durability;
   - consistency;
   - throughput;
   - RPO/RTO quando aplicável;
   - budget/operational complexity.

4. **High-level design**
   - definir clients, edge/CDN, gateways, services, data stores, queues, caches e external dependencies apenas quando necessários;
   - mostrar dataflow e ownership.

5. **Core components**
   - definir APIs e principais entidades;
   - modelar storage/access patterns;
   - justificar SQL, key-value, document, search ou outros stores pelo acesso real;
   - definir partition key, indexing e consistency onde isso importar.

6. **Scale**
   - identificar primeiro bottleneck provável;
   - avaliar horizontal scaling, replication, sharding, caching, batching e async processing;
   - não introduzir cada padrão de escala por checklist.

7. **Failure modes**
   - dependency outage;
   - retries e retry storms;
   - partial failure;
   - stale cache;
   - duplicate delivery;
   - hot partitions;
   - backpressure;
   - regional failure;
   - data corruption ou inconsistency.

8. **Operational design**
   - metrics, logs, traces e alerts;
   - capacity signals;
   - deploy/rollback;
   - migrations;
   - runbooks e ownership quando necessário.

9. **Trade-off review**
   - registrar alternativas consideradas;
   - explicar o que o design ganha e sacrifica;
   - distinguir requisito presente de possibilidade futura.

10. **Evolution**
    - propor a arquitetura mínima suficiente para o estágio atual;
    - indicar quais sinais justificariam o próximo salto arquitetural.

## Heurísticas úteis

### Latency versus throughput
Otimizar uma não implica otimizar a outra. Definir qual é o objetivo real e onde existe queueing.

### Availability versus consistency
Não usar CAP como slogan. Declarar qual falha de rede ou partition está sendo considerada e qual comportamento a aplicação precisa durante ela.

### Cache
Definir:
- key;
- owner;
- TTL/invalidation;
- cold start;
- stale behavior;
- stampede protection;
- source of truth.

### Assíncrono
Fila só agrega valor quando desacoplamento, absorção de burst, retry ou processamento demorado justificarem complexidade adicional.

### Dados
Sharding é uma resposta a escala/acesso, não ponto de partida. Primeiro entender growth, query patterns, skew e migration cost.

## Entregável

Uma análise de system design deve deixar claro:

- requisitos e assumptions;
- estimativas relevantes;
- diagrama ou descrição high-level;
- componentes e contratos principais;
- estratégia de dados;
- bottlenecks;
- failure modes;
- observabilidade;
- trade-offs;
- caminho de evolução.

## Ferramentas e dependências

Usar documentação atual das tecnologias específicas quando a decisão depender de limites, versões ou guarantees de produto. Não tratar diagramas ou números clássicos de entrevistas como specs atuais de providers.

## Integração

Combina com architecture-visualization, project-complexity-management, graph-engineering, model-routing-gateway, retrieval-quality-engineering e verify-before-claim.

## Referências

Adaptada de https://github.com/donnemartin/system-design-primer, especialmente o fluxo requirements → high-level design → core components → scale, atualizado para enfatizar SLOs, operações e evidência atual de tecnologia.
