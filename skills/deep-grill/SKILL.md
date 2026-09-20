---
name: deep-grill
description: "Conduzir entrevistas aprofundadas sobre planos ou decisões, resolvendo uma árvore de ambiguidades em rodadas sucessivas."
---

# deep-grill

## Objetivo

Entrevistar profundamente o usuário sobre um plano, decisão ou ideia até que todas as ramificações relevantes do design estejam resolvidas.

## Quando usar

Conduzir entrevistas aprofundadas sobre planos ou decisões, resolvendo uma árvore de ambiguidades em rodadas sucessivas.

## Diferença para `quick-grill`

`quick-grill` faz uma rodada curta de alinhamento. `deep-grill` trabalha uma árvore de decisões em várias rodadas até esgotar a fronteira de decisões relevantes.

## Workflow

1. Modelar o problema como uma árvore de decisões.
2. Identificar a **fronteira**: decisões cujos pré-requisitos já estão resolvidos.
3. Perguntar toda a fronteira em uma rodada, numerando as perguntas e oferecendo uma recomendação.
4. Recalcular a árvore após cada resposta.
5. Buscar fatos disponíveis em ferramentas/fontes, em vez de perguntar ao usuário.
6. Encerrar quando não restarem decisões silenciosamente assumidas.

## Registro de decisões abertas

Durante entrevistas longas:

- manter um ledger visível de ambiguidades, constraints, gates e decisões abertas;
- fatos recuperáveis do código/fontes devem ser pesquisados, não perguntados ao usuário;
- antes de cristalizar a especificação final, restatar goal + decisões centrais e pedir aprovação quando isso for uma verdadeira decisão do usuário;
- "parece claro" não encerra a entrevista se ainda houver assumptions silenciosas.

## Referências

[GitHub · mattpocock/skills · grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)

Origem local: [deep-grill.docx](../deep-grill.docx).
