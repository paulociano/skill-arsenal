---
name: strategic-landscape-mapping
description: "Mapear paisagens estratégicas por necessidade do usuário, cadeia de valor, dependências, estágio de evolução, inertia e movimentos plausíveis para melhorar decisão de build/buy, investimento, plataforma e inovação sem tratar o mapa como previsão."
---

# Strategic Landscape Mapping

## Objetivo

Aumentar consciência situacional antes de decisões estratégicas, representando o sistema de valor e como seus componentes diferem em maturidade, dependência e dinâmica competitiva.

A skill é inspirada em Wardley Mapping, mas não exige uma ferramenta gráfica específica.

## Quando usar

- build vs buy;
- platform strategy;
- inovação e portfólio;
- modernização;
- make/partner/commodity decisions;
- identificar diferenciação vs commodity;
- avaliar onde investir ou padronizar;
- mapear dependências que restringem estratégia;
- challenge de planos baseados apenas em trend ou tecnologia.

Não usar apenas para desenhar arquitetura técnica. Para isso, use `architecture-visualization` ou `system-design-engineering`.

## Princípio central

**Estratégia melhora quando posição e movimento são explícitos. Um diagrama estático de componentes não é ainda um mapa estratégico.**

## Workflow

1. **Purpose and user**
   - quem recebe valor;
   - qual need/outcome;
   - qual decisão o mapa deve informar.

2. **Value chain**
   - começar no user need;
   - decompor capabilities/components necessários;
   - representar dependências;
   - evitar listar organograma em vez de cadeia de valor.

3. **Visibility**
   - quanto cada componente é visível/direto para o usuário;
   - usar a dimensão apenas para clareza da cadeia, não como score de importância.

4. **Evolution**
   Posicionar qualitativamente componentes em continuum:
   - genesis;
   - custom-built;
   - product/rental;
   - commodity/utility.

   Basear posição em sinais como:
   - ubiquity;
   - certainty/standardization;
   - competition;
   - differentiation;
   - ecosystem maturity.

   Não fingir precisão temporal.

5. **Inertia**
   Para componentes em mudança, mapear:
   - sunk cost;
   - skills;
   - process;
   - contracts;
   - identity/status;
   - legacy integration;
   - incentives;
   - regulation.

6. **Economic and ecosystem patterns**
   Investigar:
   - commoditization;
   - enabling higher-order innovation;
   - constraints/bottlenecks;
   - co-evolution of practice;
   - centralization vs decentralization;
   - substitution;
   - ecosystem effects.

7. **Doctrine check**
   Antes de movimentos sofisticados, revisar princípios básicos:
   - user focus;
   - situational awareness;
   - remove duplication;
   - use appropriate methods by evolutionary stage;
   - challenge assumptions;
   - learn continuously.

8. **Strategic options**
   Gerar opções como hipóteses:
   - build/differentiate;
   - buy/consume utility;
   - standardize;
   - open-source/ecosystem;
   - platform;
   - partner;
   - migrate;
   - wait/observe;
   - invest in constraint.

   Não aplicar gameplay mecanicamente.

9. **Challenge**
   - o mapa está ancorado em user need?
   - dependências são reais?
   - componente foi posicionado por evidência ou preferência?
   - estamos confundindo novel com valuable?
   - estamos custom-building commodity?
   - commodity emergente pode liberar inovação acima dela?
   - qual inertia distorce a escolha?

10. **Decision handoff**
    Traduzir o mapa em:
    - decisões;
    - assumptions;
    - bets;
    - risks;
    - signals to monitor;
    - revisit condition.

    Usar `decision-analysis` quando alternativas precisarem de comparação formal.

11. **Iterate**
    O mapa é instrumento de aprendizado, não documento final. Atualizar quando evidência, mercado ou dependências mudarem.

## Guardrails

- não apresentar posição no mapa como fato científico;
- não prever data exata de commoditization sem evidência própria;
- não usar o mapa como score automático;
- não transformar todas as decisões em build-vs-buy;
- não copiar gameplay sem contexto;
- não confundir difusão com evolução;
- estratégia continua dependente de julgamento e evidência.

## Entregável

- user need;
- value chain;
- evolutionary positions;
- inertia/constraints;
- patterns relevantes;
- strategic options;
- bets/risks;
- signals/revisit conditions.

Quando visualização ajudar, combinar com `architecture-visualization` ou outro meio disponível.

## Integração

Combina com:
- `decision-analysis`;
- `business-decision-intelligence`;
- `system-design-engineering`;
- `codebase-design`;
- `venture-building-cycle`;
- `scenario-forecasting`;
- `research-and-synthesize`.

## Provenance

Adaptada de:
- https://github.com/wardley-maps-community/awesome-wardley-maps
- https://github.com/andrewharmellaw/wardley-maps-book
- https://github.com/swardley/WARDLEY-MAP-REPOSITORY

Preserva user need, value chain, evolution, inertia, doctrine, patterns e gameplay como análise contextual. A skill rejeita a ideia de que o mapa fornece resposta correta ou previsão determinística.
