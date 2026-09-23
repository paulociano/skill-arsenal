---
name: typographic-composition
description: "Projetar tipografia expressiva e legível em layouts, títulos e peças visuais usando hierarquia, ritmo, line breaks, spacing e forma das palavras sem confundir composição com engenharia de fontes."
---

# typographic-composition

## Objetivo

Tratar texto como conteúdo e forma visual ao mesmo tempo. A skill cuida de composição tipográfica em interfaces, pôsteres, capas, posts, slides e peças editoriais sem entrar automaticamente em desenho/compilação de arquivos de fonte.

## Quando usar

- lettering tipográfico, display type e hero typography;
- capas, social cards, pôsteres e apresentações;
- páginas editoriais;
- títulos com alto peso visual;
- revisão de hierarquia, line breaks, tracking e densidade.

## Dimensões

- type role: display, heading, body, label, caption;
- contrast: tamanho, peso, largura, cor, caixa;
- line length e measure;
- leading;
- tracking/kerning percebido;
- line breaks;
- alinhamento e eixo;
- optical balance;
- relationship entre texto e imagem;
- repetição e ritmo;
- forma da palavra/bloco.

## Workflow

1. Preservar o texto exato quando factual.
2. Definir função de cada bloco textual.
3. Escolher família/estilo conforme direção visual e licença.
4. Construir hierarquia com poucos contrastes fortes.
5. Ajustar line breaks manualmente quando título/display justificar.
6. Revisar palavras problemáticas, órfãs, viúvas e linhas desequilibradas.
7. Ajustar tracking/leading por escala e função, não com valores universais.
8. Verificar contraste, responsividade e zoom.
9. Para lettering customizado real, decidir se a entrega será:
   - texto com fonte;
   - SVG/path desenhado;
   - ilustração gerada;
   - fonte/glyph customizado.
10. Se houver edição de glyph/font file, encaminhar para tooling tipográfico especializado e validar licença/qualidade.

## Lettering vs fonte

- **composição tipográfica** organiza letras existentes;
- **lettering** desenha uma expressão específica;
- **type design** cria um sistema reutilizável de glyphs/fonte.

Não misturar esses escopos.

## Regras

- Não distorcer fonte arbitrariamente para "parecer única".
- Não usar texto rasterizado quando ele precisa permanecer editável/acessível.
- Não confiar em kerning automático para display crítico sem inspeção visual.
- Não usar fonte proprietária sem direito de uso.
- Em web, preservar fallback, loading e métricas para reduzir layout shift.

## Integração

editable-visual-design, beautiful-web-article, web-design-engineer, design-direction e brand-logo-exploration.

## Origem metodológica

Adaptada de práticas observadas em opentype.js, FontTools/FontBakery, Google Fonts tooling e sistemas paramétricos como Iosevka, mantendo o foco em composição e QA tipográfico em vez de exigir uma toolchain de fundição.
