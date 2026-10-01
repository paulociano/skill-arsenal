---
name: brand-logo-exploration
description: "Explorar conceitos de logo e identidade, testar escala e monocromia e refinar a direção escolhida."
---

# brand-logo-exploration

## Objetivo

Explorar direções de logo e identidade visual de forma estruturada, gerando conceitos distintos, verificando legibilidade/escala e refinando uma direção escolhida antes de produzir showcases.

## Quando usar

- logo para produto/marca;
- exploração inicial de identidade;
- ícone de app/serviço;
- variações SVG/conceituais;
- apresentação/showcase de uma direção escolhida.

## Context scan

Antes de perguntar, reutilize contexto real já disponível: nome, descrição, estratégia, cores, fonts, assets existentes, superfícies de uso e restrições. Em código/produto, procurar sinais em documentação, theme/tokens, manifest e assets sem presumir que tudo encontrado é aprovado.

Faça perguntas apenas para lacunas que mudem materialmente a direção.

## Workflow

1. **Brief mínimo** — nome, categoria, conceito central, personalidade, restrições e usos.
2. **Constraints** — monocromia/cor, wordmark/symbol, small-size use, background contexts.
3. **Direction set** — gerar 3–6 conceitos realmente diferentes, não só parâmetros. Variar símbolo, lógica formal ou tipográfica, composição e relação mark/wordmark; se duas propostas aceitam trocar o nome sem parecer conceitos diferentes, refazer uma.
4. **Rationale** — explicar a ideia sem inventar significado pós-hoc.
5. **Small-size test** — verificar leitura em favicon/app icon/tamanho pequeno.
6. **Monochrome test** — logo deve sobreviver sem efeitos.
7. **Select** — usuário escolhe 1–2 direções.
8. **Targeted refinement** — ajustar proporção, spacing, geometry e cor sem regenerar tudo. Quando já existe logo aprovado, registrar invariantes de símbolo, wordmark, silhueta e spelling antes de explorar colorways ou aplicações.
9. **Production pass** — produzir master vetorial quando adequado e passar derivados/exports para `brand-asset-production`; não misturar criação conceitual com uma explosão de formatos.
10. **Showcase** — mockups/backgrounds vêm depois da marca funcionar sozinha.

## Lentes modernistas

Quando a direção pedir linguagem modernista, internacional, suíça ou corporativa histórica, usar estas lentes como repertório, não como preset:

- redução formal e geometria clara;
- uso disciplinado de grids, proporções e módulos;
- símbolos capazes de funcionar em uma cor;
- relação controlada entre positivo e negativo;
- construção por formas básicas quando isso melhora reconhecimento;
- consistência de família entre marca principal, submarcas e aplicações;
- evitar ornamento que não contribui para identidade ou distinção;
- comparar a solução com precedentes históricos para reduzir clichê e semelhança involuntária.

## Princípios

- simplicidade e recognizability vencem showcase;
- negative space deve ser intencional;
- uma logo não precisa “explicar” todo o produto;
- efeitos, texturas e mockups não podem esconder fragilidade do símbolo;
- usar sistemas geométricos quando ajudam consistência, não por obrigação;
- evitar semelhança excessiva com marcas existentes;
- pesquisar conflitos/trademark apenas quando o usuário pedir ou o uso exigir.

## Variação

Quando a direção envolver mascote/IP simples ou ícone-personagem:
- apresente poucas direções conceituais antes da geração;
- mantenha o sujeito explícito quando o usuário já o definiu e varie tratamento, silhueta, região secundária de cor ou traço definidor;
- quando o sujeito estiver aberto, conecte cada proposta a uma promessa de produto ou atributo de marca, evitando variedade arbitrária;
- prefira formas grandes, arredondadas e legíveis em tamanho pequeno a detalhes anatômicos explicativos;
- valide leitura em 32×32 e fundo sólido sem depender de efeitos para sustentar a forma;
- gere variantes controladas que testem composição e crop sem trocar o conceito central.

As direções devem variar em conceito:

- geométrica;
- tipográfica;
- monograma;
- símbolo abstrato;
- sistema modular;
- organicidade, quando coerente.

Não aceitar seis variações quase iguais como exploração real.

## Segurança e propriedade

- não copiar logo de marca existente;
- referências visuais são inspiração, não templates para réplica;
- APIs externas de imagem só quando conectadas/autorizadas;
- não enviar materiais confidenciais a provider externo sem necessidade.

## Ferramentas e dependências

Usar a geração de imagem disponível para conceitos raster e ferramentas de design/código compatíveis para vetores. Não exigir Gemini, Nano Banana ou APIs externas. Inspecionar o resultado e declarar formatos que não puderam ser exportados.

## Integração

- `brand-identity-system`
- `brand-guidelines-authoring`
- `brand-asset-production`
- `design-system-governance`
- `design-system-extraction`
- `web-design-engineer`
- `verify-before-claim`

## Teste morfológico

Para conceitos geométricos ou modernistas, verificar separadamente:

1. **silhueta** — reconhecível sem detalhe interno;
2. **massa** — equilíbrio entre áreas cheias e vazias;
3. **estrutura** — lógica modular ou geométrica perceptível sem precisar ser explicada;
4. **redução** — sobrevive em escala pequena e reprodução imperfeita;
5. **distinção** — não parece apenas uma recombinação genérica de círculo, seta, globo ou monograma;
6. **sistema** — pode gerar aplicações coerentes sem depender de mockup ornamental.

## Referências

Adaptada de op7418/logo-generator-skill, refinada com context scan e asset-kit workflow de sacredvoid/logo-generator e separação base-logo/colorway/mascot observada em SanbaoAI/logo-generator-skill e enriquecida por repertório e princípios de redução formal observados em *Logo Modernism*, de Jens Müller e R. Roger Remington. O livro funciona como referência histórica e morfológica, não como catálogo para copiar marcas.

Mascote/IP simples: metodologia absorvida de s1dashu/ip-as-logo-skill, sem fixar modelo externo, número obrigatório de imagens ou convenções específicas de outro agente.

Origem local: [brand-logo-exploration.docx](../brand-logo-exploration.docx).
