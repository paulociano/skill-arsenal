# Avaliação: skills de graph engineering (2026-11-09)

## Pedido
Procurar skills de graph engineering para o Arsenal e para instalação no Claude.

## Estado anterior do Arsenal
- `skills/graph-engineering` cobre apenas grafos de **tarefas** (DAG limitado, fan-out/fan-in, joins, verificação por nó, coordenação multiworker).
- Grafos de **conhecimento** (ontologia, extração, resolução de entidades, GraphRAG) não tinham owner; havia apenas menções em `agent-memory-engineering` e `code-understanding-audit` (Graphify, REAgraph — ver `2026-10-21-graphify-reagraph.md`).

## Fontes analisadas
Leitura de páginas de registro (tessl.io, skills.cat, claudeskills.info, claudemarketplaces.com) e clone parcial de repositórios públicos. Nenhum instalador externo executado.

| Fonte | Classe | Decisão |
|---|---|---|
| Jamie-BitFlight/claude_skills · `graph-engineering` | A | ADAPT — ramo de knowledge graph (9 etapas) vira base da nova skill; ramo de task graph descartado por overlap |
| lyndonkl/claude · `graphrag-system-design` | A/B | ABSORB — escolha entre 3 padrões GraphRAG incorporada; skill externa pode ser instalada no Claude se houver projeto GraphRAG |
| omer-metin/skills-for-antigravity · `graph-engineer` | B | ABSORB — princípios (grafo esparso, limite de cardinalidade, validade temporal, ER primeiro, EXPLAIN); o resto é persona |
| neo4j-contrib/neo4j-skills (30+ skills) | D | KEEP_EXTERNAL_REFERENCE — específicas de Neo4j, dependem de drivers/pacotes; instalar apenas se Neo4j for usado |
| oakoss/agent-skills · `knowledge-graph-builder` | C/B | DISCARD — sobreposição com Jamie-BitFlight, menos rigor, viés para stack fixa |
| asiaostrich/universal-dev-standards · `knowledge-graph` | C | DISCARD — impacto entre specs/decisões; acoplado ao padrão EngramGraph do autor |

## Materialização
- NEW: `skills/knowledge-graph-engineering/SKILL.md`.
- Índice atualizado com a nova entrada.
- `graph-engineering` recebeu apenas ponteiro para a nova skill (divisão task graph × knowledge graph).

## Segurança e portabilidade
- Metodologia sem scripts; funciona por leitura e raciocínio.
- Extração por LLM pode enviar dados a terceiros: exigir autorização para dados sensíveis.
- Registro do skills.cat sinaliza menção a credenciais em `references/fusion-and-llm.md` da Jamie-BitFlight; arquivo não importado.

## Limitações
- O repositório Jamie-BitFlight/claude_skills não pôde ser clonado nesta sessão (exigiu autenticação); a adaptação usou o resumo publicado nos registros, não o SKILL.md integral. Revisar contra a fonte se ela ficar acessível.
- Nenhum benchmark executado.

## Acceptance cases
- Deve disparar: GraphRAG sobre base normativa; grafo de clientes/produtos/contratos para exposição.
- Near-miss: resumo de PDFs (`kb-retriever`); paralelizar relatórios (`graph-engineering`).
