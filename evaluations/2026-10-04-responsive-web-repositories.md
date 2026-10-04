# Avaliação — responsividade web moderna

Data: 2026-10-04

## Escopo

Pesquisa de repositórios GitHub bem avaliados ou tecnicamente relevantes para fortalecer responsividade no Skill Arsenal. O objetivo não foi importar frameworks, e sim identificar capabilities incrementais que melhorem o owner canônico de web design.

Owner encontrado no Arsenal: `skills/web-design-engineer/SKILL.md`.

Stack usada: `arsenal-autopilot`, porque o lote envolve múltiplas fontes e overlap de capabilities.

## Capability ledger

| Fonte | Capability observada | Classificação | Decisão |
| --- | --- | --- | --- |
| twbs/rfs | rescaling fluido limitado de valores CSS, com foco original em tipografia e legibilidade | B/D | ABSORB_METHOD_ONLY |
| argyleink/open-props | tokens de spacing/type fluidos e custom media para preferências adaptativas | B/D | ABSORB_METHOD_ONLY |
| tachyons-css/tachyons | princípios mobile-first, 100% responsive, legibilidade, modularidade e baixo peso | B | ABSORB_METHOD_ONLY |
| pure-css/pure | CSS pequeno, modular e responsive-by-default com grids responsivos | B | KEEP_EXTERNAL_REFERENCE + ABSORB_METHOD_ONLY |
| trys/utopia-core | cálculo de type/space scales fluidas, viewport/container relative e sinalização de violações de zoom em tipografia | A/D | ABSORB_METHOD_ONLY |
| twbs/bootstrap | benchmark maduro de mobile-first, grids e utilities | D | KEEP_EXTERNAL_REFERENCE |
| tailwindlabs/tailwindcss | benchmark maduro de responsive variants e utility-first | D | KEEP_EXTERNAL_REFERENCE |

## Conclusão de ownership

Não criar `responsive-web-engineering`.

`web-design-engineer` já é o owner correto para estrutura e responsividade. Criar outra skill dividiria ownership e aumentaria overlap. O ganho incremental deve entrar como:

1. seção curta no owner;
2. referência sob demanda com a engenharia responsiva detalhada.

## Metodologia adotada

A síntese adotada é:

`intrinsic layout → bounded fluid sizing → container queries → media queries → JavaScript apenas quando necessário`.

Também entram:
- testes baseados em restrições, não apenas devices;
- conteúdo extremo/localizado como teste estrutural;
- responsive media;
- preferências de motion/input;
- cuidado com tipografia baseada somente em viewport;
- evitar breakpoints mágicos e JS para layout que CSS pode resolver.

## O que não foi adotado

- classes, APIs e presets específicos de Bootstrap, Tailwind, Tachyons, Pure ou Open Props;
- preprocessors ou PostCSS como dependência obrigatória;
- breakpoints prontos;
- design tokens externos como defaults do Arsenal;
- installers, CLIs ou scripts das fontes.

## Segurança e portabilidade

Verdict: **APPROVE para absorção metodológica**.

A avaliação foi estática. Nenhum installer, script ou pacote externo foi executado.

Riscos de supply chain das implementações externas deixam de ser relevantes para o Arsenal porque nenhuma delas foi instalada. As referências preservam apenas princípios e exemplos CSS portáveis. Se um projeto consumidor decidir instalar uma dessas bibliotecas no futuro, a dependência deve ser avaliada no contexto real do projeto.

## Prova de valor incremental

Antes desta avaliação, `web-design-engineer` exigia responsive behavior e runtime verification, mas não definia como escolher entre intrinsic layout, fluid sizing, container queries, media queries e JavaScript.

A mudança é útil quando:
- uma interface acumula media queries frágeis;
- um componente precisa funcionar em containers diferentes;
- spacing/type precisam escalar suavemente;
- o layout precisa sobreviver entre breakpoints;
- o usuário pede para "deixar responsivo" sem impor framework.

Near-miss:
- auditoria pura de performance/acessibilidade continua pertencendo a `web-quality-audit`;
- design tokens e governança continuam pertencendo a `design-system-governance`;
- bugs específicos de layout sem redesign podem usar `debug-and-fix`/owners de engenharia conforme contexto.

## Fontes

- https://github.com/twbs/rfs
- https://github.com/argyleink/open-props
- https://github.com/tachyons-css/tachyons
- https://github.com/pure-css/pure
- https://github.com/trys/utopia-core
- https://github.com/twbs/bootstrap
- https://github.com/tailwindlabs/tailwindcss

## Decisão final

**Atualizar `web-design-engineer`; não criar nova skill.**

Materializar a metodologia detalhada em `skills/web-design-engineer/references/responsive-layout-engineering.md` e manter o core skill compacto.
