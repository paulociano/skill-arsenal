---
name: discovery-research-synthesis
description: "Sintetizar entrevistas, tickets e pesquisas em padrões, contradições e decisões com evidência rastreável."
---

# discovery-research-synthesis

## Objetivo

Transformar entrevistas, tickets, calls, pesquisas e outros artefatos de descoberta em padrões, implicações e decisões sem fabricar insight.

## Quando usar

Sintetizar entrevistas, tickets e pesquisas em padrões, contradições e decisões com evidência rastreável.

## Workflow

1. Preparar os artefatos em formato analisável.
2. Taggear cada artefato de forma descritiva, sem impor taxonomia prematura.
3. Agrupar observações entre artefatos.
4. Nomear padrões somente depois do agrupamento.
5. Registrar contradições e segmentos divergentes, não escondê-los.
6. Derivar implicações de produto distinguindo claramente evidência de interpretação.
7. Para cada implicação, explicitar o `so what`: qual decisão concreta ela informa.
8. Quando possível, validar padrões qualitativos com dados quantitativos ou outras fontes independentes.

## Guardrails

- Não saltar de quote para conclusão sem cadeia de evidência.
- Não transformar volume aparente em frequência populacional sem base quantitativa.
- Não produzir deck bonito como substituto de decisão.
- Manter evidência rastreável para cada padrão relevante.

## Registro de evidências

Quando o volume de pesquisa justificar, normalizar sinais em um ledger rastreável:

- id estável;
- source type;
- segment;
- observation/signal;
- quote ou metric real;
- strength;
- limitations.

Themes precisam listar os evidence ids que os sustentam e registrar contradições/segment differences. Uma opportunity matrix pode usar scores como apoio visual, mas score nunca substitui julgamento.

Para decisões, fechar com um memo curto:

- recommended move;
- evidência;
- o que pode estar errado;
- reversible next step;
- o que medir em seguida.

## Integração

Combina com `kb-retriever` para localizar evidências, `jtbd-framing` para uma lente específica e `experiment-design` para validação posterior.

## Referências

Adaptada de [rampstackco/claude-skills · discovery-research-synthesis](https://github.com/rampstackco/claude-skills/tree/main/skills/discovery-research-synthesis).

Origem local: [discovery-research-synthesis.docx](../discovery-research-synthesis.docx).
