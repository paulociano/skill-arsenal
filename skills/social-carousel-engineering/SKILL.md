---
name: social-carousel-engineering
description: "Projetar carrosséis sociais como narrativa slide a slide, do hook ao CTA, preservando marca, densidade legível, continuidade visual, editabilidade e QA de exportação sem prometer engajamento."
---

# social-carousel-engineering

## Objetivo

Transformar uma ideia, fonte ou campanha em um carrossel social coerente e editável, tratando o conjunto como uma sequência narrativa e não como uma pilha de cards independentes.

## Quando usar

- Instagram, LinkedIn, TikTok slideshow ou formatos equivalentes;
- carrossel educativo, teardown, case, lista, opinião, storytelling ou campanha;
- converter artigo, roteiro, pesquisa ou post longo em sequência visual;
- criar variações de carrossel para teste editorial ou de campanha.

Não usar quando o pedido é apenas um social card isolado; nesse caso, usar `editable-visual-design`.

## Contrato de entrada

Definir somente o necessário:
- objetivo: ensinar, gerar descoberta, consideração, clique, lead, prova ou conversa;
- audiência;
- ideia/claim central;
- fonte/prova disponível;
- plataforma e formato;
- voz/brand system;
- CTA;
- número aproximado de slides quando houver restrição.

Não assumir que "viral" é um objetivo mensurável nem prometer performance.

## Arquitetura narrativa

Escolher uma estrutura coerente com o material, não um template universal.

Padrões úteis:
- **Hook → tension → explanation → proof → implication → CTA**
- **Problem → mistakes → better model → steps → CTA**
- **Before → turning point → after → lesson**
- **Claim → evidence → counterpoint → synthesis**
- **List → progression → synthesis**
- **Teardown → observation → why → fix → example**

Cada slide deve ter uma função. Se dois slides fazem o mesmo trabalho, comprimir ou diferenciar.

## Workflow

1. **Distill** — extrair ideia central, proof points, tensões, objeções, exemplos e possíveis visuais.
2. **Choose arc** — selecionar a arquitetura narrativa adequada ao objetivo.
3. **Hook variants** — criar poucas aberturas estruturalmente diferentes. Hook deve criar curiosidade que o próprio carrossel consegue satisfazer.
4. **Slide map** — definir função de cada slide antes do acabamento visual.
5. **One dominant idea** — manter uma ideia dominante por slide; detalhes secundários entram apenas se aumentarem compreensão.
6. **Progressive disclosure** — cada swipe deve avançar a história, não apenas reformular o slide anterior.
7. **Visual grammar** — fixar palette, type roles, grid, safe zones, logo/handle e padrões de imagem/diagrama.
8. **Continuity** — variar composição sem quebrar reconhecimento da série.
9. **CTA fit** — CTA deve corresponder ao estágio: salvar/compartilhar, comentar, seguir, clicar, responder ou converter. Não forçar CTA comercial em conteúdo de descoberta quando ele quebra a narrativa.
10. **Per-slide revision** — permitir revisar/regenerar um slide sem destruir o restante da sequência quando a ferramenta real permitir.
11. **Spec grounding** — antes do export, verificar dimensões, aspect ratio, formato, duração/tamanho quando aplicável e safe zones em fonte atual da plataforma. [Media Cheat Sheet](https://mediacheatsheet.com/) pode acelerar a consulta porque agrega specs com links de origem, mas a plataforma oficial continua sendo a autoridade final quando houver conflito.
12. **Render/export** — produzir no aspect ratio correto e revisar o render final. LinkedIn document carousel normalmente exige documento/PDF; Instagram/TikTok slideshow normalmente exige imagens individuais conforme o canal e fluxo real.
13. **Learn** — após publicação, comparar o carrossel com outros conteúdos do mesmo autor/campanha usando métricas realmente disponíveis. Aprendizado histórico orienta a próxima hipótese, não vira regra universal.

## Hook discipline

Hooks podem explorar:
- tensão específica;
- resultado/prova;
- pergunta concreta;
- contraste;
- erro comum;
- observação;
- confissão/story;
- teardown;
- open loop.

Evitar:
- fake contrarianism;
- promessa que o conteúdo não entrega;
- "você não vai acreditar";
- urgência inventada;
- score de viralidade;
- copiar fórmulas literalmente quando a voz pede outra construção.

## Visual system

Combinar com `editable-visual-design` e `typographic-composition`.

Regras:
- texto factual permanece texto controlável quando possível;
- não gerar lettering crítico dentro de imagem;
- preservar safe zones e legibilidade móvel;
- imagem é evidência/apoio, não preenchimento automático;
- brand config deve separar identidade visual de provider/modelo quando houver automação;
- preview e export devem compartilhar a mesma fonte de layout quando o runtime permitir, reduzindo divergência WYSIWYG;
- preservar editabilidade até a etapa de exportação quando possível.

## Organic vs paid

### Orgânico
O carrossel pode otimizar para descoberta, saves, shares, comentários, profile visits ou cliques, conforme o objetivo. Não tratar likes como métrica universal.

### Pago
Quando o carrossel for creative de campanha:
- preservar hipótese criativa explícita;
- variar uma dimensão relevante por vez quando o objetivo for aprender;
- registrar audience, offer, hook, proof, CTA e visual concept;
- usar `experiment-design` para A/B tests e critérios de decisão;
- usar dados reais de campanha para análise; não declarar vencedor por gosto editorial.

## Feedback loop

Registrar quando houver superfície persistente:
- hipótese;
- hook/arc;
- formato;
- data;
- audiência/campanha;
- métricas disponíveis;
- observação qualitativa;
- próximo teste.

Separar:
- **qualidade editorial**;
- **performance observada**;
- **causalidade testada**.

Um post vencedor não prova sozinho que seu hook, horário ou layout causou o resultado.

## QA

Antes de finalizar:
- hook entrega promessa?
- sequência tem progressão?
- existe slide redundante?
- proof points estão sustentados?
- leitura funciona em tela pequena?
- contraste e safe zones estão corretos?
- brand/voice permanecem consistentes?
- CTA corresponde ao objetivo?
- formato de exportação corresponde à plataforma?
- claims de performance estão apresentados como hipótese quando não testados?

## Integração

`content-matrix`, `niche-research`, `editable-visual-design`, `typographic-composition`, `social-post-review`, `social-analytics`, `instagram-growth-diagnostics`, `experiment-design`, `content-production` e `social-growth-engine`.

## Origem metodológica

Síntese adaptada de padrões observados em projetos open source de carousel/content automation, especialmente:
- https://github.com/wasimjalali/swipekit
- https://github.com/tomaskub292929/open-carrusel
- https://github.com/kenkirito/carousel
- https://github.com/Simonstorms/slidelot
- https://github.com/Thaynabarreiro/social-content-automation
- https://github.com/agentreacher/skills

A adaptação preserva narrativa slide a slide, brand config, revisão granular, human approval e feedback loop, removendo dependências de Claude Code, Postiz, APIs/modelos específicos, MCPs, schedulers e claims de performance não verificados.
