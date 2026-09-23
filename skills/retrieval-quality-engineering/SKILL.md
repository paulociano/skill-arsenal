---
name: retrieval-quality-engineering
description: "Diagnosticar e melhorar retrieval/RAG com conjunto de consultas, baseline e avaliação de chunking, busca híbrida e reranking."
---

# retrieval-quality-engineering

## Objetivo

Diagnosticar e melhorar sistemas de retrieval/RAG medindo qualidade real antes de trocar índices, embeddings ou arquitetura, e escolhendo entre dense, sparse, hybrid, filters, reranking e feedback com base no problema observado.

## Princípio central

**Antes de tunar o banco vetorial, descubra se o problema é dado, embedding, chunking, query ou retrieval strategy.**

## Quando usar

- resultados irrelevantes;
- baixa precision/recall;
- resultados esperados ausentes;
- RAG recupera contexto ruim;
- dúvida entre dense/sparse/hybrid;
- migração de embedding model;
- reranking/diversidade;
- filtros/multitenancy;
- performance de search degradou.

## Workflow

1. Construir um golden set pequeno com queries reais e resultados esperados.
2. Medir baseline com métricas adequadas: recall@k, precision@k, MRR/nDCG ou outra métrica útil.
3. Testar exact/lexical clues para separar problema de dados/chunking de problema vetorial.
4. Inspecionar:
   - chunk boundaries;
   - metadata/filter correctness;
   - embedding model e dimensionalidade;
   - query formulation;
   - language/domain mismatch;
   - index/quantization effects.
5. Só depois alterar a estratégia.

## Estratégias

- **Dense**: semântica ampla.
- **Sparse/lexical**: termos exatos, entidades, códigos, nomes.
- **Hybrid**: combinar representações quando semantic + keyword importam.
- **Reranking**: custo extra para refinar top candidates.
- **MMR/diversity**: evitar resultados quase duplicados quando diversidade importa.
- **Relevance feedback**: incorporar sinais explícitos/implícitos quando disponíveis.
- **Filters**: limitar corpus por tenant, período, tipo, ACL ou metadado.

## Hybrid search

Ao combinar buscas:

1. executar representações de forma independente;
2. fundir com método explícito;
3. medir ganho versus baseline;
4. registrar trade-off de latência/CPU/RAM;
5. não escolher RRF/DBSF/fusion “por vibes”.

## RAG end-to-end

Retrieval bom não garante resposta boa. Quando o objetivo for avaliar RAG completo, separar:

- **retriever quality**: recall/precision/MRR/nDCG e presença do evidence necessário;
- **context quality**: relevância, redundância, ordem e contamination;
- **answer grounding**: se a resposta é sustentada pelo contexto recuperado;
- **answer relevance/completeness**: se responde ao pedido sem extrapolar;
- **citation correctness** quando houver citações.

RAGAS e frameworks semelhantes podem acelerar essas métricas, mas não são autoridade automática. Definir dataset e oracle antes de otimizar, combinar checks determinísticos/human labels quando possível e não mascarar falha de retrieval com um gerador mais eloquente.

## Multitenancy e isolamento

- payload filters não implicam automaticamente isolamento estatístico de todos os mecanismos;
- revisar escopo de IDF, shards e indexes no produto/versão real;
- privacy/ACL deve ser enforced antes ou durante retrieval, nunca apenas após retornar resultados.

## Performance

Separar:

- search latency;
- throughput/QPS;
- indexing time;
- memory footprint.

Otimização para uma pode piorar outra. Não copiar parâmetros de outro workload sem medir.

## Version grounding

Para recomendações específicas de Qdrant, usar `library-version-grounding` e guidance oficial atual. As skills oficiais da Qdrant são symptom-routed e mudam com o produto; preferir fonte fresca a snapshots antigos.

## Ferramentas e dependências

A metodologia vale para qualquer vector/search stack. Não presumir Qdrant instalado. Se houver Qdrant, usar docs/skills atuais; se houver outro motor, traduzir os princípios para suas APIs e limitações.

## Integração

Combina com `kb-retriever`, `discovery-research-synthesis`, `experiment-design`, `library-version-grounding` e `verify-before-claim`.

## Referências

Adaptada de qdrant/qdrant e qdrant/skills.

Separação retriever/context/answer e métricas end-to-end refinadas a partir de https://github.com/explodinggradients/ragas e suites de avaliação RAG de DeepEval/Opik.

Origem local: [retrieval-quality-engineering.docx](../retrieval-quality-engineering.docx).
