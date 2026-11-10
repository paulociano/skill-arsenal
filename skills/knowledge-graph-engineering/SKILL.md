---
name: knowledge-graph-engineering
description: "Projetar, construir e avaliar grafos de conhecimento e GraphRAG a partir de perguntas de competência, com ontologia mínima, extração restrita, resolução de entidades, proveniência e subgrafos com evidência. Use quando relações, caminhos multi-hop ou identidade recorrente forem centrais; não para workflows de tarefas (graph-engineering)."
---

# knowledge-graph-engineering

## Objetivo

Construir grafos de conhecimento que respondam perguntas reais com evidência rastreável, em vez de grafos densos e ruidosos que só parecem sofisticados.

## Quando usar

- Perguntas dependem de relações, caminhos multi-hop, identidade recorrente de entidades ou mudança no tempo (ex.: "quem está ligado a quem", "qual a cadeia de impacto de X", "o que mudou desde a versão anterior").
- Projetar ou revisar GraphRAG, memória em grafo, ontologia, extração de entidades/relações/eventos ou deduplicação de entidades.
- Avaliar se um grafo existente está entregando valor.

## Quando não usar

- Dados tabulares simples → tabela/banco relacional.
- Busca em documentos sem relações relevantes → `retrieval-quality-engineering` ou `kb-retriever`.
- Workflow de tarefas com dependências e paralelismo → `graph-engineering`.
- Memória de agente sem necessidade de travessia → `agent-memory-engineering`.
- Entender estrutura de código/repositório → `code-understanding-audit`.

Gate inicial obrigatório: declarar por que tabela, índice de documentos, busca vetorial ou workflow serial não bastam. Se não houver resposta concreta, não construir grafo.

## Workflow

1. **Perguntas de competência.** Listar 5–15 perguntas que o grafo precisa responder, com exemplos de resposta esperada. Tudo que não serve a uma pergunta fica fora do escopo inicial.
2. **Representação.** Escolher property graph, RDF/OWL ou arestas tipadas simples conforme consultas, interoperabilidade e equipe. Definir desde o início: identidade (chave canônica por tipo), tempo (validade das arestas: `valid_from`/`valid_to` ou equivalente) e proveniência (fonte, trecho, data, extrator, confiança).
3. **Ontologia mínima.** Só os tipos de nó, tipos de relação e restrições exigidos pelas perguntas. Reutilizar vocabulário existente quando houver. Registrar cardinalidades e domínio/alcance de cada relação.
4. **Ingestão.** Dados estruturados entram por mapeamento determinístico. Texto aberto entra por extração restrita à ontologia (entidades, relações, eventos), com schema de saída, evidência por asserção e rejeição do que não se encaixa — não deixar o modelo inventar tipos novos silenciosamente.
5. **Avaliação da extração.** Amostra rotulada por tipo de relação; medir precisão e recall separadamente. Limiar definido pelo custo do erro a jusante, não por número fixo. Relações de alto impacto exigem precisão maior ou revisão humana.
6. **Resolução de entidades e fusão.** Resolver identidade antes de densificar o grafo ("João Silva", "J. Silva" e "João S." não podem virar três nós). Fundir asserções preservando conflitos com fonte e confiança; nunca sobrescrever silenciosamente. Casos ambíguos ficam marcados, não fundidos.
7. **Armazenamento e operação.** Escolher store pelo volume, padrão de consulta e operação (embutido, Neo4j, RDF store, Postgres com tabelas de aresta etc.). Definir constraints/índices antes da carga, rotina de ingestão incremental, deleção/retratação por fonte e checagens de integridade.
8. **Serviço (GraphRAG/memória).** Entregar ao modelo o menor subgrafo com evidência que responde à pergunta, com limite de hops e de tamanho. Escolher o padrão:
   - **híbrido símbolo + vetor** — consultas mistas estruturadas e semânticas;
   - **subgrafo sob demanda** — perguntas multi-hop focadas, quando custo e frescor importam;
   - **sumarização por comunidades** — perguntas amplas sobre o corpus inteiro.
   Respostas citam nós/arestas e as fontes que os sustentam.
9. **Avaliação ponta a ponta.** Testar com as perguntas de competência e medir cada etapa separadamente (extração, resolução, recuperação, resposta), para saber onde está a falha. Comparar com baseline sem grafo; se o grafo não superar, simplificar.

## Princípios de modelagem

- Grafo esparso escala; conectar demais é pior que conectar de menos.
- Limitar cardinalidade de arestas por nó; "god nodes" com dezenas de milhares de arestas degradam travessia e relevância.
- Validade temporal nas arestas desde o primeiro dia; adicionar depois é caro.
- Resolução de entidades é a maior parte do trabalho e vem antes da estrutura.
- Relações inferidas não provam causalidade; marcar EXTRACTED / INFERRED / AMBIGUOUS quando relevante.
- Perfilar consultas (EXPLAIN/PROFILE ou equivalente) antes de declarar performance aceitável.
- Grafo, índices e embeddings são derivados reconstruíveis das fontes; a fonte e a proveniência são o record.

## Entregas

Conforme o pedido, entregar uma ou mais:

- especificação: perguntas de competência, ontologia, regras de identidade/tempo/proveniência, pipeline, padrão de serviço, plano de avaliação;
- schema/constraints e exemplos de consulta para o store escolhido;
- prompt e schema de extração restrita, com casos de teste;
- relatório de avaliação por etapa com limites declarados.

## Ferramentas e dependências

A metodologia funciona só com leitura e raciocínio. Construir ou consultar um grafo real exige store, drivers e acesso aos dados; sem isso, entregar o desenho e declarar que nada foi executado. Não presumir Neo4j, neo4j-graphrag, LangChain, LlamaIndex, Graphify ou MCPs instalados. Extração por LLM pode enviar dados a provedores externos — confirmar autorização para dados sensíveis.

Se o projeto usar Neo4j de fato, as skills oficiais `neo4j-contrib/neo4j-skills` (modelagem, Cypher, import, GraphRAG, query tuning) são referência técnica complementar.

## Aceite

- **Deve disparar:** "montar um grafo de clientes, produtos e contratos para responder quem está exposto a X"; "projetar GraphRAG sobre a base de normas internas".
- **Near-miss:** "resumir estes 10 PDFs" → `kb-retriever`; "paralelizar a geração de 5 relatórios" → `graph-engineering`.
- **Falha a evitar:** grafo sem perguntas de competência, com tipos criados livremente pelo extrator e entidades duplicadas.

## Referências

Adaptada de:
- [Jamie-BitFlight/claude_skills · graph-engineering](https://github.com/Jamie-BitFlight/claude_skills) (ramo de knowledge graph; derivado do curso de grafos de conhecimento da Southeast University). Ramo de task graph não importado: já coberto por `graph-engineering`.
- [omer-metin/skills-for-antigravity · graph-engineer](https://github.com/omer-metin/skills-for-antigravity/tree/HEAD/skills/graph-engineer) — princípios de modelagem.
- [lyndonkl/claude · graphrag-system-design](https://github.com/lyndonkl/claude) — escolha de padrão GraphRAG.

Avaliação: `evaluations/2026-11-09-graph-engineering-skills.md`.
