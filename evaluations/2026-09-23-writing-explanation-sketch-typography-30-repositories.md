# Avaliação — 30 repositórios de escrita, explicação, esboço e tipografia

Data: 2026-09-23

## Escopo

Terceira leva de pesquisa do Arsenal, focada em melhoria de escrita, clareza, explicação, outline, documentação, sketching visual e composição tipográfica/lettering. A avaliação foi comparada ao ARSENAL INDEX atual, especialmente writing-quality, eli5, teach, beautiful-web-article, architecture-visualization e editable-visual-design.

## Critérios

- **A** — metodologia/capacidade que muda comportamento do Arsenal.
- **B** — boa referência para enriquecer owner existente.
- **C** — pouco ganho incremental sobre owners atuais.
- **D** — valor técnico dependente de ferramenta/runtime/toolchain específica.

## Resultado

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 1 | amperser/proselint | A | Incorporar filosofia de prose lint configurável em prose-lint. |
| 2 | errata-ai/vale | A/D | Referência forte para contratos editoriais verificáveis; não exigir CLI. |
| 3 | btford/write-good | A/B | Absorver checks como sinais, sem tratar passiva/hedging como erro universal. |
| 4 | get-alex/alex | A | Incorporar revisão de linguagem potencialmente excludente/condescendente com contexto. |
| 5 | textlint/textlint | A/D | Framework útil para regras customizáveis; owner conceitual prose-lint. |
| 6 | remarkjs/remark-lint | B/D | Consistência estrutural de Markdown; não criar skill própria. |
| 7 | retextjs/retext | A/D | Base NLP modular; usar como referência de checks. |
| 8 | retextjs/retext-equality | A/B | Complementar linguagem inclusiva; absorver metodologia. |
| 9 | wooorm/readability | B | Readability como sinal, nunca como objetivo isolado. |
| 10 | languagetool-org/languagetool | A/D | Gramática/style multilíngue; ferramenta opcional, não dependência. |
| 11 | 18F/content-guide | A | Plain language e content design incorporados em writing-quality/explanation. |
| 12 | vale-cli/Google | A/B | Regras de style guide como lint; incorporar ideia de contratos editoriais. |
| 13 | tech-writing-lab/google-tech-writing | A | Reforça audiência, clareza, estrutura e exemplos em explanation-architecture. |
| 14 | tech-writing-lab/style-guide | B | Boa referência de escrita técnica; sem owner novo. |
| 15 | davegomez/gemini-documentation-skills | A/B | Diátaxis como router de documentação; adaptar sem dependência de Gemini. |
| 16 | mermaid-js/mermaid | A/B | Diagramas complementam explicação; owner architecture-visualization. |
| 17 | excalidraw/excalidraw | A/D | Fonte principal para sketch visual informal; criar visual-explanation-sketch. |
| 18 | tldraw/tldraw | A/D | Whiteboard/canvas e pensamento espacial; incorporar metodologia, não SDK. |
| 19 | rough-stuff/rough | B/D | Estética hand-drawn como linguagem opcional, não padrão. |
| 20 | rough-stuff/rough-notation | A/B | Anotação visual de foco; incorporar vocabulário de destaque. |
| 21 | steveruizok/perfect-freehand | A/D | Stroke natural/pressão; referência técnica para sketching. |
| 22 | szimek/signature_pad | B/D | Captura/smoothing de escrita manual; nicho, sem skill própria. |
| 23 | opentypejs/opentype.js | A/D | Letterforms, kerning, paths e glyphs; informar typographic-composition. |
| 24 | fonttools/fonttools | A/D | Engenharia de fontes ampla; manter como tooling especializado. |
| 25 | fonttools/fontbakery | A/D | QA sistemático de fontes; inspirar validação tipográfica. |
| 26 | googlefonts/glyphsLib | D | Conversão/manipulação Glyphs; técnico, sem owner próprio. |
| 27 | googlefonts/ufo2ft | D | Build de fontes; referência técnica apenas. |
| 28 | googlefonts/fontmake | D | Compilação de fontes; usar somente em demanda real. |
| 29 | google/fonts | B/D | Fonte/licenciamento e repertório; não criar skill separada. |
| 30 | foliojs/fontkit | A/D | Métricas/shaping de fontes; complemento técnico a opentype.js. |

## Mudanças adotadas

### Novas skills
- explanation-architecture
- prose-lint
- visual-explanation-sketch
- typographic-composition

### Skills atualizadas
- writing-quality
- eli5
- teach
- beautiful-web-article
- editable-visual-design

## Decisões de arquitetura

1. **Outline pertence à escrita/explicação**, não exige uma skill separada.
2. **Lint não é reescrita**: prose-lint encontra candidatos e writing-quality decide edição.
3. **Tutorial, how-to, explanation e reference têm contratos diferentes** e não devem ser misturados por padrão.
4. **Visual sketch é diferente de diagrama técnico**: sketch comunica ideia; architecture-visualization documenta topologia/fluxo técnico.
5. **Composição tipográfica é diferente de type design**: o Arsenal ganhou owner para hierarquia e lettering aplicado, não uma fundição digital.
6. **Readability score e regras de estilo são sinais**, não leis universais.
7. **Plain language preserva precisão**, não autoriza remover termos necessários ou ressalvas.

## Segurança, portabilidade e licença

- Nenhum linter, CLI, editor ou pipeline de fontes foi instalado ou executado apenas para avaliação.
- Tools externas são opcionais quando já disponíveis no projeto.
- Regras específicas de inglês não foram importadas como regras de português.
- Linguagem inclusiva é tratada com contexto e sem sobrescrever citações/termos definidos.
- Excalidraw/tldraw/Rough/Perfect Freehand foram usados como referência metodológica, não como dependência obrigatória.
- FontTools, FontBakery, GlyphsLib, ufo2ft, fontmake, opentype.js e fontkit permanecem fontes técnicas; engenharia de font files só deve ser acionada em demanda real.

## Fontes principais

- https://github.com/amperser/proselint
- https://github.com/errata-ai/vale
- https://github.com/btford/write-good
- https://github.com/get-alex/alex
- https://github.com/textlint/textlint
- https://github.com/remarkjs/remark-lint
- https://github.com/retextjs/retext
- https://github.com/retextjs/retext-equality
- https://github.com/wooorm/readability
- https://github.com/languagetool-org/languagetool
- https://github.com/18F/content-guide
- https://github.com/vale-cli/Google
- https://github.com/tech-writing-lab/google-tech-writing
- https://github.com/tech-writing-lab/style-guide
- https://github.com/davegomez/gemini-documentation-skills
- https://github.com/mermaid-js/mermaid
- https://github.com/excalidraw/excalidraw
- https://github.com/tldraw/tldraw
- https://github.com/rough-stuff/rough
- https://github.com/rough-stuff/rough-notation
- https://github.com/steveruizok/perfect-freehand
- https://github.com/szimek/signature_pad
- https://github.com/opentypejs/opentype.js
- https://github.com/fonttools/fonttools
- https://github.com/fonttools/fontbakery
- https://github.com/googlefonts/glyphsLib
- https://github.com/googlefonts/ufo2ft
- https://github.com/googlefonts/fontmake
- https://github.com/google/fonts
- https://github.com/foliojs/fontkit

## Veredito

A leva justificou 4 skills novas e 5 upgrades de owners existentes. As demais fontes foram incorporadas como metodologia/referência técnica sem ampliar desnecessariamente o Arsenal.
