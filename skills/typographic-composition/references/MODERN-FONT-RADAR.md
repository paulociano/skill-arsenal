# Modern Font Radar

Radar curado para `typographic-composition`. Não é ranking nem catálogo exaustivo. Sempre verificar licença, cobertura de caracteres, formato disponível e adequação ao projeto antes do uso.

## Famílias principais

### Geist
Fonte: https://github.com/vercel/geist-font

- Papel: produto digital contemporâneo, SaaS, dashboards, interfaces e apresentações tech.
- Famílias: Sans, Mono e Pixel.
- Força: linguagem limpa e atual com boa legibilidade para UI.
- Uso no Arsenal: candidata forte para produto/interface quando a direção pede neutralidade moderna com caráter técnico.

### Inter
Fonte: https://github.com/rsms/inter

- Papel: workhorse para UI, marketing e sistemas densos.
- Força: variable font, optical size, ampla faixa de pesos e recursos OpenType.
- Uso no Arsenal: body/UI robusto; display pode explorar optical sizing quando suportado.
- Nota: preferir distribuição oficial atual quando fidelidade à versão importa.

### Recursive
Fonte: https://github.com/arrowtype/recursive

- Papel: UI, código e experiências tipográficas expressivas.
- Força: família variável Sans/Mono com eixos que permitem transformar personalidade e largura de forma contínua.
- Uso no Arsenal: excelente candidata quando tipografia participa do motion, transição de estados ou identidade procedural.

### IBM Plex
Fonte: https://github.com/IBM/plex

- Papel: produto, editorial, apresentações, dados e sistemas globais.
- Famílias: Sans, Serif, Mono, Sans Condensed e extensões de idiomas.
- Força: sistema tipográfico amplo e coerente, útil quando uma única identidade precisa cobrir múltiplos papéis.
- Uso no Arsenal: apresentações e interfaces com mistura de editorial, dados e código.

## Famílias secundárias

### Archivo
Fonte: https://github.com/Omnibus-Type/Archivo

Grotesca com grande amplitude de pesos/larguras. Útil quando a composição precisa de contraste de largura e densidade sem trocar de família.

### Work Sans
Fonte: https://github.com/weiweihuanghuang/Work-Sans

Sans grotesca versátil para interfaces e comunicação. Tratar como alternativa de linguagem mais humanista/menos "produto tech padrão" conforme a direção.

### Jost
Fonte: https://github.com/indestructible-type/Jost

Geométrica com variable font. Pode funcionar em identidades, títulos e landing pages quando a direção pede geometria mais marcada.

### JetBrains Mono
Fonte: https://github.com/JetBrains/JetBrainsMono

Mono open source com alta legibilidade e recursos OpenType. Usar para código, labels técnicas, números ou contraste editorial, não como decoração automática de interfaces tech.

### Iosevka
Fonte: https://github.com/be5invis/Iosevka

Sistema altamente paramétrico com variantes sans/slab, mono/quasi-proportional. É mais valioso como referência de customização e engenharia tipográfica do que como escolha padrão.

### Google Fonts
Fonte: https://github.com/google/fonts

Tratar como ecossistema/distribuição e radar amplo, não como direção estética. Resolver a família específica e sua fonte original quando versão, licença ou recursos variáveis forem críticos.

## Heurística de seleção

Escolher pela função antes da novidade:

1. confirmar caracteres e idiomas necessários;
2. definir papéis: display, heading, body, UI, mono/data;
3. comparar legibilidade e personalidade com a direção visual;
4. verificar pesos, itálicos, larguras e eixos realmente disponíveis;
5. avaliar custo de webfont, subset e layout shift;
6. usar variable axes somente quando resolverem responsividade, composição ou motion;
7. testar títulos reais e parágrafos reais, não apenas specimen;
8. preservar fallback e licença.

## Motion tipográfico

Variable font pode ser parte da animação quando o eixo comunica estado ou narrativa. Exemplos válidos: largura abrindo espaço, peso respondendo a ênfase, transição Sans/Mono quando suportada pela família. Evitar loops contínuos de eixos em body text e qualquer animação que prejudique leitura ou reduced motion.
