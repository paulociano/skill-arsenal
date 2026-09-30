---
name: content-matrix
description: "Gerar e priorizar ideias específicas de conteúdo cruzando pilares, ângulos, formatos, hooks, prova e objetivo do funil sem confundir potencial editorial com previsão de performance."
---

# content-matrix

## Objetivo

Transformar pilares editoriais, tensões da audiência, provas disponíveis e objetivo de negócio em um portfólio de ideias específicas de conteúdo, com ângulos e formatos suficientemente distintos para produzir e testar.

## Quando usar

- brainstorm estruturado de posts;
- calendário editorial;
- campanha orgânica ou paga;
- explorar ângulos para uma mesma pauta;
- escolher entre post, carrossel, Reel/vídeo, thread, social card ou outro formato;
- gerar variantes de hook antes da produção.

## Entradas

Usar somente o contexto necessário:
- audiência;
- objetivo: descoberta, educação, autoridade, conversa, clique, lead, conversão ou retenção;
- 3–5 pilares ou temas;
- oferta/proposta quando relevante;
- provas, dados, histórias, exemplos ou assets disponíveis;
- canais;
- voz/brand context.

Se faltarem provas, gerar ideias que não dependam de claims inventados.

## Matriz de oportunidades

Cruzar pilares com famílias de ângulo, escolhendo apenas as pertinentes:
- actionable/how-to;
- análise/explicação;
- observação;
- erro comum;
- contraste/X vs Y;
- before/after;
- teardown;
- história/confissão;
- objeção;
- proof/case;
- presente vs futuro;
- lista/framework;
- contrarian apenas quando houver argumento real;
- pergunta concreta;
- bastidores/processo.

Cada célula deve virar uma **ideia específica**, não um tema genérico.

## Hook families

Para ideias promissoras, explorar 2–4 famílias estruturalmente diferentes:
- tensão específica;
- resultado/prova;
- pergunta;
- contraste;
- erro;
- observação;
- story/confissão;
- warning;
- teardown;
- open loop.

O hook deve criar uma promessa que a peça consegue cumprir.

Evitar:
- clickbait sem entrega;
- urgência inventada;
- fake contrarianism;
- engagement bait;
- score de viralidade apresentado como previsão;
- copiar fórmulas prontas sem adaptar à voz e ao canal.

## Idea card

Para cada candidata final, registrar de forma compacta:
- **idea/claim**;
- **audience tension**;
- **angle**;
- **hook direction**;
- **proof/source**;
- **format**;
- **CTA**;
- **funnel role**;
- **visual opportunity**, quando houver.

Não é necessário preencher todos os campos para pedidos pequenos.

## Priorização

Selecionar ideias por:
1. aderência ao objetivo;
2. relevância para a audiência;
3. especificidade/novidade do ângulo;
4. força da prova disponível;
5. adequação ao canal/formato;
6. capacidade real de produção.

Não converter esses critérios em score preditivo de alcance ou conversão.

Quando houver histórico real, usar `social-post-review` ou `social-analytics` para comparação, mantendo julgamento editorial separado de performance observada.

## Organic vs paid

### Orgânico
Balancear funções ao longo do calendário: descoberta, valor salvável/compartilhável, autoridade/prova, conversa e conversão. Não exigir que toda peça venda.

### Paid creative
Gerar ideias como hipóteses explícitas:
`audience × offer × angle × hook × proof × CTA × visual concept`.

Se a intenção for aprender causalmente, combinar com `experiment-design` e variar deliberadamente as dimensões escolhidas.

## Workflow

1. Reutilizar perfil/voz e contexto já disponíveis.
2. Definir objetivo e audiência.
3. Confirmar pilares e proof inventory.
4. Gerar matriz de ângulos.
5. Eliminar duplicatas semânticas.
6. Expandir hooks apenas das melhores candidatas.
7. Escolher formato pelo trabalho narrativo, não por hábito.
8. Montar idea cards.
9. Priorizar pelo objetivo e capacidade.
10. Rotear produção:
   - carrossel → `social-carousel-engineering`;
   - Reel/short video → `reels-scripting`;
   - peça visual fixa → `editable-visual-design`;
   - texto social → `writing-quality` + `social-post-review`.
11. Depois da publicação, usar dados reais para atualizar hipóteses do próximo ciclo.

## Repurposing

Quando a entrada for uma fonte existente, primeiro extrair:
- ideia central;
- 3–7 ideias atômicas;
- provas;
- histórias;
- objeções;
- frases/conceitos reutilizáveis;
- oportunidades visuais.

Depois reconstruir peças nativas por canal. Reutilizar **fatos e ideias**, não necessariamente o mesmo wording.

## Ferramentas e dependências

Entregar no chat ou em artefato apropriado conforme o pedido. Pesquisa atual usa `niche-research` quando tendências/notícias importarem. Não depender de scheduler, scraper, MCP ou plataforma externa específica.

## Referências

Base original: https://github.com/charlie947/social-media-skills/tree/main/skills/content-matrix

Metodologia de hooks e repurposing enriquecida a partir de:
- https://github.com/agentreacher/skills
- https://github.com/rediumvex/viral-hooks-skill

Adaptada para evitar scores preditivos, dependências específicas de agentes e fórmulas tratadas como garantias de performance.
