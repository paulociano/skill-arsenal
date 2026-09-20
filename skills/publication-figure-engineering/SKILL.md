---
name: publication-figure-engineering
description: "Produzir figuras científicas alinhadas aos claims de papers, separando diagramas conceituais de gráficos quantitativos exatos."
---

# publication-figure-engineering

## Objetivo

Projetar e produzir figuras técnicas/científicas para papers separando diagramas conceituais de plots quantitativos exatos, com um figure brief explícito e verificação contra o claim e os dados.

## Quando usar

- graphical abstract;
- system architecture em paper;
- algorithm workflow;
- hardware schematic;
- benchmark chart;
- ablation plot;
- heatmap/scatter/trend;
- figura multi-panel;
- redesenho de figura com evidência.

## Princípio central

**Conceito pode ser gerado visualmente; número exato deve ser plotado a partir dos dados.**

## Figure brief

Antes de renderizar, definir:

- figure_goal;
- paper_claim;
- figure_type;
- mode: image | plot | mixed;
- panels e ordem de leitura;
- must_keep_labels;
- data/provenance;
- style/venue constraints;
- output formats;
- verification checklist.

## Router de modo

### Image
Para:

- arquitetura conceitual;
- workflow;
- graphical abstract;
- schematic;
- mecanismo sem geometria numérica exata.

### Plot
Para:

- barras;
- curvas;
- scatter;
- heatmap;
- error bars;
- benchmark/ablation;
- qualquer eixo/geometria que represente valor real.

### Mixed
Renderizar painéis quantitativos deterministicamente e tratar painéis conceituais separadamente.

## Workflow

1. Ground claim e dados.
2. Criar/normalizar figure brief.
3. Escolher modo.
4. Produzir layout/prompt ou plot spec.
5. Renderizar no runtime disponível.
6. Verificar:
   - labels;
   - arrows/reading order;
   - números;
   - eixos/legend;
   - panel consistency;
   - claim alignment;
   - readability no tamanho final do paper.
7. Corrigir somente o problema observado.
8. Exportar em formato adequado e manter versão editável quando possível.

## Regras

- nunca usar image generation para inventar valores, barras ou curvas exatas;
- nunca inventar hardware specs, benchmark gains ou experimental values;
- figure bonita não corrige claim ruim;
- short labels, hierarchy e reading order importam mais que ornamentação;
- plot precisa apontar para dataset/tabela fonte;
- incluir uncertainty/error bars somente quando existirem;
- verificar legibilidade no tamanho de publicação, não apenas fullscreen.

## Relação com architecture-visualization

- `architecture-visualization`: verdade/topologia de sistemas em geral.
- `publication-figure-engineering`: figura orientada ao claim de paper, incluindo plots quantitativos.
Quando ambas se aplicarem, architecture-visualization pode gerar a spec topológica e esta skill cuida da composição/publicação.

## Segurança

- arquivos/dados de pesquisa podem ser confidenciais;
- provider externo de imagem exige autorização;
- não enviar draft/dataset sensível a relay de terceiros por padrão;
- chaves/API ficam fora do artefato.

## Ferramentas e dependências

Usar geração de imagem para painéis conceituais e Python/bibliotecas gráficas disponíveis para números exatos. Verificar labels e exportações. Não exigir scripts/providers da fonte nem enviar material a outro serviço sem autorização adequada.

## Integração

- `academic-paper-orchestration`
- `architecture-visualization`
- `structured-output-contract`
- `verify-before-claim`

## Referências

Adaptada de heyu-233/engineering-figure-agent.

Origem local: [publication-figure-engineering.docx](../publication-figure-engineering.docx).
