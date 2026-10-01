# Evaluation — Branding and Logo Repositories Batch — 2026-10-01

## Escopo

Avaliação em lote de 12 repositórios selecionados de uma pesquisa maior sobre logo design, branding, visual identity, brand guidelines, brand systems e asset production.

## Fontes avaliadas

1. https://github.com/ordinarynerds/brand-book
2. https://github.com/sacredvoid/logo-generator
3. https://github.com/SanbaoAI/logo-generator-skill
4. https://github.com/jgerton/brand-toolkit
5. https://github.com/dhernz/brand-identity
6. https://github.com/Better-Conversations/bc-brand
7. https://github.com/git-grader/brand
8. https://github.com/ThinkFizzApp/branding
9. https://github.com/OpenHomeFoundation/brand-assets
10. https://github.com/OpenAEC-Foundation/OpenAEC-style-book
11. https://github.com/Aioverse-HQ/Brand-System-Aiotize-Inc
12. https://github.com/InfoJobs/brand

## Capability ledger

| Capability | Principais fontes | Owner decidido | Ação |
|---|---|---|---|
| Estratégia e posicionamento de marca | jgerton/brand-toolkit | brand-strategy | KEEP / já coberto |
| Direções visuais contrastantes e seleção | dhernz/brand-identity, jgerton/brand-toolkit | brand-identity-system | CREATE_NEW |
| Exploração de logo com context scan | sacredvoid/logo-generator | brand-logo-exploration | UPDATE_EXISTING |
| Separação base-logo / mascot / colorway | SanbaoAI/logo-generator-skill | brand-logo-exploration | ABSORB_METHOD_ONLY |
| Manual de marca + machine-readable source | ordinarynerds/brand-book, ThinkFizzApp/branding | brand-guidelines-authoring | CREATE_NEW |
| Brand model → tokens/packages/docs | bc-brand, OpenAEC, Aiotize | design-system-governance | UPDATE_EXISTING |
| Export matrix, naming e small-size variants | OpenHomeFoundation/brand-assets, git-grader/brand | brand-asset-production | CREATE_NEW |
| Estrutura de manual/asset library real | InfoJobs/brand | brand-guidelines-authoring | ABSORB_METHOD_ONLY |
| Brand compliance review | ThinkFizz, jgerton | design-principles/design system review existentes | KEEP_EXTERNAL_REFERENCE |

## Classificação por fonte

### ordinarynerds/brand-book — A/D
Metodologia forte: uma fonte estruturada alimenta book, tokens e instruções operacionais. Scripts, hooks e Paper MCP são dependências técnicas não portadas. Absorvido em brand-guidelines-authoring e design-system-governance.

### sacredvoid/logo-generator — A/D
Bom fluxo de context scan → brainstorm adaptativo → conceitos → produção → preview → export. Sharp/Node e convenções de Claude não são assumidos. Context scan e separação criação/export foram absorvidos.

### SanbaoAI/logo-generator-skill — B/D
A separação base-logo, mascot e colorway é útil, principalmente preservação de invariantes durante recoloração. A maior parte do valor é prompt/tool-specific e não justifica três novas skills.

### jgerton/brand-toolkit — A/D
Ecossistema metodológico forte. Positioning já é majoritariamente coberto por brand-strategy. Stylescapes/anti-convergence e audit inspiram brand-identity-system; runtimes/manifest/agents específicos não foram importados.

### dhernz/brand-identity — A
Processo "show 3, pick 1" produz mudança real de comportamento: decisão de gosto por comparação, anti-convergência e uso de conteúdo real. Consolidado em brand-identity-system sem importar blacklists universais de estilos/fontes.

### Better-Conversations/bc-brand — A/D
Excelente modelo de source-of-truth com tokens derivados para múltiplos consumidores e separação de licenças. Absorvido em design-system-governance e brand-guidelines-authoring.

### git-grader/brand — A/D
Modelo forte de asset repository, small-size variant, motion/social/print e gated changes. Scripts específicos não foram importados. Capability central virou brand-asset-production.

### ThinkFizzApp/branding — B
Bom exemplo de brand.json + agent-facing voice/UI/review. Metodologia incremental, absorvida em brand-guidelines-authoring; não exige skill própria.

### OpenHomeFoundation/brand-assets — A
Naming convention e taxonomia screen/print + lockup/logomark são diretamente reutilizáveis. Absorvido em brand-asset-production.

### OpenAEC-Foundation/OpenAEC-style-book — A/D
Bom acoplamento entre brand book, design-system docs, token package, source assets e regeneração. Dependências de export não são presumidas. Absorvido em guidelines, asset production e design-system governance.

### Aioverse-HQ/Brand-System-Aiotize-Inc — B/D
Boa arquitetura de repo para docs/assets/tokens/packages/examples e review conjunto de design/engineering. Metodologia absorvida; npm/package specifics permanecem externos.

### InfoJobs/brand — B
Referência útil de estrutura de manual, logotypes, UI kits, templates, icons e examples. Mais acervo do que processo. Mantido como referência metodológica, sem skill própria.

## Segurança e portabilidade

- nenhum installer externo foi executado;
- hooks, shell scripts, npm installs, Paper MCP, Figma MCP e toolchains de geração não foram importados;
- assets de marca de terceiros não foram copiados;
- licenças e provenance foram tratados como parte do workflow;
- regras de trademark e não-derivação foram preservadas conceitualmente;
- ferramentas específicas foram substituídas por capabilities disponíveis apenas quando equivalentes existem.

## Mudanças adotadas

### Novas skills
- brand-identity-system
- brand-guidelines-authoring
- brand-asset-production

### Skills atualizadas
- brand-logo-exploration
- design-system-governance

### Nova stack
- brand-creation-system

## Decisões de não adoção

- não criar brand-source-of-truth como skill separada: a capability pertence a brand-guidelines-authoring + design-system-governance;
- não criar brand-audit neste lote: há overlap significativo com design-system-extraction, design-principles-audit e auditorias existentes; pode ser reavaliado se aparecer demanda recorrente específica de marca;
- não criar skills separadas para mascot-logo e logo-colorway: métodos úteis foram absorvidos no owner de logo;
- não importar scripts de export, hooks de lint ou installers de terceiros.

## Resultado

O Arsenal agora cobre explicitamente o ciclo:
strategy → identity directions → logo → guidelines → asset production → digital design governance.

A stack brand-creation-system orquestra esse fluxo de forma parcimoniosa, mantendo gates humanos nas decisões de direção.
