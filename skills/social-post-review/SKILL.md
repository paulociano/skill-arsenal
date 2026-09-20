---
name: social-post-review
description: "Revisar posts separando qualidade editorial de comparação com o histórico real do autor, sem prever desempenho por score."
---

# social-post-review

## Objetivo

Revisar um post social usando duas camadas separadas: qualidade editorial e comparação com histórico real do próprio autor, quando disponível.

## Quando usar

Revisar posts separando qualidade editorial de comparação com o histórico real do autor, sem prever desempenho por score.

## Workflow

1. Ler o post e o perfil de voz, se houver.
2. Usar histórico do próprio autor apenas quando fornecido ou acessado por conexão autorizada.
3. Quando houver dados, identificar padrões dos posts de melhor e pior desempenho: hooks, temas, formato, comprimento, CTA, ritmo e distribuição de formatos.
4. Separar claramente **julgamento editorial** de **comparação histórica**.
5. Avaliar hook, voice match, densidade de valor, estrutura/formato e prontidão de publicação.
6. Nunca apresentar um score editorial como previsão de performance futura.

## Ferramentas e dependências

Não depender de Apify. Pode usar export enviado pelo usuário, planilha, dados de conector autorizado ou simplesmente fazer revisão editorial. Se não houver histórico, declarar que o componente comparativo está indisponível.

## Referências

Adaptada de [post-scorer](https://github.com/charlie947/social-media-skills/tree/main/skills/post-scorer)

Origem local: [social-post-review.docx](../social-post-review.docx).
