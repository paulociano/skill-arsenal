---
name: brand-asset-production
description: "Produzir, nomear, organizar e validar variantes e exports de marca a partir de masters aprovados para digital, social, app e print sem redesenhar silenciosamente a identidade."
---

# brand-asset-production

## Objetivo

Transformar masters aprovados em um pacote de assets previsível e reutilizável. A skill cuida da produção e governança de variantes, não da criação conceitual do logo.

## Quando usar

- exportar logo para light/dark/mono;
- criar favicons, app icons, social/OG assets e formatos print;
- organizar brand asset repository;
- definir naming convention;
- produzir small-size variants a partir de uma direção aprovada;
- regenerar derivados quando o master muda.

## Princípio central

**Master primeiro, derivados depois.** Não editar manualmente um arquivo derivado para corrigir algo que pertence ao master ou à regra de export.

## Workflow

1. Confirmar masters aprovados e owner.
2. Inventariar superfícies-alvo: web, app, favicon, social, apresentações, documentos, print, signage ou outras.
3. Definir matriz de variantes necessária, evitando combinações inúteis:
   - asset type: logomark, wordmark, lockup;
   - orientation: inline, primary, stacked;
   - treatment: color, reversed, mono;
   - background: light/dark;
   - scale: normal/small-size quando necessário;
   - medium: screen/print.
4. Criar naming convention estável e legível.
5. Gerar derivados a partir dos masters usando tooling disponível e autorizado.
6. Para small-size variants, permitir ajustes ópticos deliberados de stroke, spacing ou simplificação sem fingir que é o mesmo desenho em escala.
7. Gerar favicons/app icons/social assets apenas quando fazem parte do escopo.
8. Para print, preservar vetores e converter espaços de cor somente com método validado.
9. Criar manifesto/inventário de assets com source, derived-from, variante, formato e uso.
10. Verificar cada família:
   - transparência;
   - bounding box/viewBox;
   - proporção;
   - legibilidade;
   - fundo correto;
   - dimensões;
   - ausência de clipping;
   - consistência de naming.
11. Publicar derivados em estrutura previsível; preservar fontes separadamente.

## Estrutura de referência

Adaptar ao projeto, por exemplo:

```
brand/
  logo/
    source/
    screen/
      lockup/
      logomark/
    print/
      lockup/
      logomark/
  social/
  app-icon/
  templates/
  manifest.json
```

## Naming

Um formato útil é:

`{brand}-{type}-{variant}-{treatment}-{background}-{size}.{ext}`

Omitir dimensões que não acrescentem informação. Naming deve permitir inferir uso sem abrir o arquivo.

## Matriz mínima de logo

Quando aplicável:
- primary lockup;
- mark;
- reversed;
- mono dark;
- mono light;
- small-size mark;
- favicon/app icon.

Não criar todas as permutações apenas porque são possíveis.

## Regras

- nunca re-typeset wordmark aprovado para criar export;
- nunca alterar proporção para caber em dimensão;
- não usar raster como master quando vetor existe;
- não afirmar que um CMYK/Pantone está correto sem validação;
- não rasterizar apenas para medir geometria vetorial;
- não importar scripts externos sem revisão;
- não tratar mockup como asset master;
- preservar direitos e licenças de fonts, logos e outros assets.

## Saída mínima

- matriz de variantes;
- naming convention;
- diretórios;
- derivados produzidos;
- manifesto/provenance;
- checks executados;
- limitações de export.

## Integração

Recebe masters de `brand-logo-exploration` e regras de `brand-guidelines-authoring`. Pode alimentar websites, apps, presentations e design systems.

## Origem metodológica

Síntese adaptada de OpenHomeFoundation/brand-assets, git-grader/brand, sacredvoid/logo-generator e OpenAEC-Foundation/OpenAEC-style-book. A lógica de export foi preservada como metodologia, sem exigir Sharp, CairoSVG, Affinity, Python ou scripts específicos da fonte.
