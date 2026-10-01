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
- revisão de hierarquia, line breaks, tracking e densidade;
- escolha de famílias modernas ou variable fonts quando a tipografia participa da identidade ou do motion.

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
- forma da palavra/bloco;
- eixos variáveis úteis, como weight, width, optical size ou slant, quando a família realmente os oferece.

## Princípios editoriais adicionais

- tratar tipografia como sistema de proporções e ritmo, não como coleção de tamanhos isolados;
- preservar a textura da página: densidade, medida, entrelinha e contraste devem produzir leitura contínua;
- escolher largura de linha, leading e escala por contexto e tipo, evitando números universais;
- usar hierarquia tipográfica com economia: poucas relações fortes vencem muitas exceções;
- respeitar pontuação, caixa, espaços, hifens, aspas e sinais como parte da composição;
- considerar alinhamento óptico e margens aparentes quando a precisão visual justificar;
- em texto longo, legibilidade e ritmo têm precedência sobre efeitos de display.

## Workflow

1. Preservar o texto exato quando factual.
2. Definir função de cada bloco textual.
3. Escolher família/estilo conforme direção visual, legibilidade, cobertura de caracteres e licença.
4. Quando a direção pedir linguagem contemporânea, consultar `references/MODERN-FONT-RADAR.md` como radar, não como ranking automático.
5. Construir hierarquia com poucos contrastes fortes.
6. Ajustar line breaks manualmente quando título/display justificar.
7. Revisar palavras problemáticas, órfãs, viúvas e linhas desequilibradas.
8. Ajustar tracking/leading por escala e função, não com valores universais.
9. Em variable fonts, usar eixos para resolver composição ou interação; não animar eixos apenas por novidade.
10. Verificar contraste, responsividade, zoom e comportamento durante font loading.
11. Para lettering customizado real, decidir se a entrega será texto com fonte, SVG/path desenhado, ilustração gerada ou fonte/glyph customizado.
12. Se houver edição de glyph/font file, encaminhar para tooling tipográfico especializado e validar licença/qualidade.

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
- Repositório de fonte é fonte de assets e documentação, não uma skill executável.
- Preferir fonte variável somente quando seus eixos trouxerem ganho real de composição, responsividade ou motion.

## Integração

editable-visual-design, beautiful-web-article, web-design-engineer, design-direction, ui-motion-design e brand-logo-exploration.

## Checklist editorial

Antes de concluir uma composição de texto longo ou editorial, verificar:

- medida confortável e coerente com o suporte;
- leading suficiente para separar linhas sem dissolver o parágrafo;
- hierarquia reconhecível sem excesso de estilos;
- ritmo vertical previsível entre títulos, parágrafos, listas e notas;
- pontuação e sinais tipograficamente corretos quando o ambiente suportar;
- órfãs, viúvas, rivers e quebras problemáticas em entregas de alta fidelidade;
- consistência entre intenção editorial e comportamento responsivo.

## Origem metodológica

Enriquecida por princípios editoriais inspirados em *The Elements of Typographic Style*, de Robert Bringhurst, sem reproduzir a obra ou impor proporções como regras universais. Adaptada também de práticas observadas em opentype.js, FontTools/FontBakery, Google Fonts tooling e sistemas paramétricos como Iosevka, enriquecida por famílias open source contemporâneas como Geist, Inter, Recursive e IBM Plex, mantendo o foco em composição e QA tipográfico em vez de exigir uma toolchain de fundição.
