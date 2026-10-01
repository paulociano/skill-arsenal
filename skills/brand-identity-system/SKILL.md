---
name: brand-identity-system
description: "Transformar estratégia e referências em uma identidade visual coerente por direções contrastantes, escolha explícita e sistema final de cor, tipografia, imagem, grafismos e aplicações."
---

# brand-identity-system

## Objetivo

Construir uma identidade visual completa, não apenas um logo. Traduzir estratégia, audiência, diferenciação e personalidade em um sistema visual reconhecível, testável e aplicável em diferentes superfícies.

## Quando usar

- criação de identidade visual do zero;
- rebrand com estratégia suficientemente definida;
- brand kit que precisa incluir mais do que logo;
- definição conjunta de cor, tipografia, imagery, iconografia e linguagem gráfica;
- quando o usuário precisa comparar direções visuais antes de escolher.

## Pré-condições

Use o contexto já disponível e marque hipóteses. Idealmente tenha:
- audiência e categoria;
- diferenciação/prova;
- personalidade ou atributos;
- concorrentes ou referências de categoria;
- principal coisa que a marca precisa fazer alguém lembrar;
- restrições de aplicação.

Quando estratégia estiver ausente, não invente. Use `brand-strategy` ou declare a identidade como exploratória.

## Workflow

1. **Grounding** — ler estratégia, assets, produto, referências e contexto competitivo.
2. **Visual landscape** — identificar padrões dominantes da categoria e oportunidades de diferenciação sem assumir que diferente é automaticamente melhor.
3. **Anchor** — registrar a ideia ou percepção prioritária que deve sobreviver em todas as decisões visuais.
4. **Direction set** — criar 3 direções realmente contrastantes. Variar pelo menos tipografia, temperatura cromática, ritmo/layout, shape language e imagery.
5. **Anti-convergence check** — se duas direções aceitam trocar wordmark/paleta sem parecer marcas diferentes, refazer uma delas.
6. **Present in context** — mostrar cada direção com conteúdo e aplicações reais do domínio, não só swatches soltos.
7. **Risk note** — declarar força e risco de cada direção.
8. **Selection gate** — preservar a escolha humana. Refinar apenas a direção escolhida ou combinação explicitamente pedida.
9. **System build** — definir:
   - logo direction e relações com `brand-logo-exploration`;
   - color roles e acessibilidade;
   - typography roles e hierarchy;
   - imagery/photography/illustration stance;
   - iconography;
   - graphic devices, patterns e shape language;
   - layout grammar e spacing;
   - motion stance quando relevante.
10. **Applications** — provar o sistema em pelo menos 3 superfícies materialmente diferentes.
11. **Handoff** — produzir especificação estruturada para `brand-guidelines-authoring`, design system ou implementação.

## Direções contrastantes

Cada direção deve declarar:
- tese visual;
- palette logic;
- type pairing;
- imagery;
- shape language;
- layout rhythm;
- assinatura visual;
- aplicações;
- risco.

Não gerar três skins da mesma solução.

## Moodboards e referências

Quando houver referências:
- extrair relações transferíveis, não copiar marcas;
- separar paleta, contraste, textura, composição, tipo, materialidade e linguagem de forma;
- quando referências entrarem em tensão, nomear a tensão e escolher uma linha dominante em vez de fazer média estética;
- registrar observed, derived e proposed.

## Regras

- identidade não é soma de tendências;
- não usar psicologia de cor como determinismo;
- não escolher fonte só por "vibe";
- não confundir logo com identidade inteira;
- não usar mockup para esconder uma marca fraca;
- não fabricar diferenciação visual sem considerar categoria e uso;
- não exigir que toda marca tenha mascote, gradiente, motion ou ilustração;
- não converter preferências do agente em regra da marca.

## Saída mínima

- anchor;
- landscape visual;
- 3 direções contrastantes;
- escolha/refinamento;
- sistema final de cor, tipo, imagery, iconografia, linguagem gráfica e layout;
- relação com logo;
- aplicações;
- riscos e hipóteses;
- handoff estruturado.

## Integração

Usar `brand-strategy` antes quando necessário. Usar `brand-logo-exploration` para exploração do logo, `color-psychology-context` para cor, `typographic-composition` para tipografia, `brand-guidelines-authoring` para documentação e `design-system-governance` quando a identidade virar produto digital.

## Origem metodológica

Síntese adaptada de dhernz/brand-identity e jgerton/brand-toolkit (especialmente visual identity/stylescapes), com princípios de comparação de direções, anti-convergência, moodboard reading e risco explícito. Dependências específicas de Claude Code e Figma foram removidas.
