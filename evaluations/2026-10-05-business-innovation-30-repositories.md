# Avaliação — 30 repositórios de práticas inovadoras de negócios

Data: 2026-10-05

## Objetivo

Avaliar 30 repositórios com forte sinal público em estratégia, produto, growth, monetização, GTM, operação e venture building, comparando-os com o Arsenal canônico e adotando apenas capabilities com ganho incremental.

## Resultado executivo

Criados:
- `saas-pricing-monetization`;
- `go-to-market-strategy`;
- `strategic-landscape-mapping`.

Atualizados:
- `experiment-design` com integridade de exposure, SRM, leitura sequencial e variance reduction;
- `venture-building-cycle` com owners explícitos de GTM, monetização e landscape strategy;
- `ARSENAL INDEX.md`.

Não criado:
- `company-operating-system`: overlap alto com `work-delivery-flow`, `team-health-management`, `project-health-review`, `dashboard-design`, `meeting-to-actions` e stacks de gestão; as fontes avaliadas trazem práticas úteis, mas não um contrato novo suficientemente separável.

## Triage dos 30

| Fonte | Classe | Decisão principal |
|---|---|---|
| coreyhaines31/marketingskills | A/B/D | CREATE_NEW + UPDATE_EXISTING |
| PostHog/posthog | A/D | UPDATE_EXISTING |
| kuchin/awesome-cto | B | KEEP_EXTERNAL_REFERENCE |
| getlago/lago | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| growthbook/growthbook | A/D | UPDATE_EXISTING |
| mmccaff/PlacesToPostYourStartup | B | ABSORB_METHOD_ONLY |
| deanpeters/Product-Manager-Skills | A/B | KEEP_EXISTING_OWNERS |
| EdoStra/Marketing-for-Founders | B | CREATE_NEW / ABSORB_METHOD_ONLY |
| flexprice/flexprice | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| basecamp/handbook | B | ABSORB_METHOD_ONLY |
| draftdev/startup-marketing-checklist | B | KEEP_EXTERNAL_REFERENCE |
| ProductHired/open-product-management | B | KEEP_EXISTING_OWNERS |
| ericosiu/ai-marketing-skills | A/B/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| kuchin/awesome-ceo | B | KEEP_EXTERNAL_REFERENCE |
| dend/awesome-product-management | B | KEEP_EXISTING_OWNERS |
| KrishMunot/awesome-startup | B | KEEP_EXTERNAL_REFERENCE |
| wondelai/skills | B/C | KEEP_EXTERNAL_REFERENCE |
| trekhleb/promote-your-next-startup | B | ABSORB_METHOD_ONLY |
| uselotus/lotus | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| lorabv/awesome-agile | B | KEEP_EXISTING_OWNERS |
| RefoundAI/lenny-skills | A/B | KEEP_EXISTING_OWNERS |
| kdeldycke/awesome-billing | A/B | CREATE_NEW / ABSORB_METHOD_ONLY |
| PostHog/posthog.com | B | ABSORB_METHOD_ONLY |
| Ibexoft/awesome-startup-tools-list | C | REJECT AS SKILL |
| wardley-maps-community/awesome-wardley-maps | A/B | CREATE_NEW |
| charlax/entrepreneurship-resources | B | KEEP_EXTERNAL_REFERENCE |
| operately/operately | B/D | ABSORB_METHOD_ONLY |
| ronakganatra/awesome-marketing | B | KEEP_EXTERNAL_REFERENCE |
| AIDevGTM/gtm-cofounder | A/B | CREATE_NEW / ABSORB_METHOD_ONLY |
| LeCoupa/awesome-bootstrappers | B | KEEP_EXTERNAL_REFERENCE |

## 1. SaaS pricing & monetization

### Fontes principais

- coreyhaines31/marketingskills — pricing;
- getlago/lago;
- flexprice/flexprice;
- uselotus/lotus;
- kdeldycke/awesome-billing;
- AIDevGTM/gtm-cofounder.

### Valor incremental

O `venture-building-cycle` já tratava pricing como hipótese, e `payment-billing-operations` cobre billing operacional. Faltava o owner estratégico entre essas camadas:

`value → value metric → pricing model → packaging → price point → economics → rollout → billing contract`.

Lago e Flexprice reforçam que usage, metering, credits, entitlements e billing são primitives distintas. O material de marketing/pricing reforça separar packaging, metric e price point e tratar preço como hipótese a aprender.

### Decisão

Criar `saas-pricing-monetization`.

Ownership:
- estratégia econômica/comercial → `saas-pricing-monetization`;
- cobrança, invoices, retries, reconciliation → `payment-billing-operations`;
- forecast/finance → owners financeiros.

## 2. Go-to-market strategy

### Fontes principais

- AIDevGTM/gtm-cofounder;
- EdoStra/Marketing-for-Founders;
- coreyhaines31/marketingskills;
- ericosiu/ai-marketing-skills;
- trekhleb/promote-your-next-startup.

### Valor incremental

O Arsenal tinha as peças de discovery, brand, first-customer research, content e venture building, mas não um owner para o sistema comercial completo.

Capabilities adotadas:
- diagnosis before tactics;
- roadmap stage-aware;
- adopter vs buyer;
- ICP + buying system;
- positioning → activation → channel → sales → pricing;
- first-user distribution;
- launch como processo, não evento;
- Now / Next / Later;
- vanity metrics não substituem activation/retention/revenue.

### Decisão

Criar `go-to-market-strategy`.

## 3. Strategic landscape mapping

### Fontes principais

- wardley-maps-community/awesome-wardley-maps;
- andrewharmellaw/wardley-maps-book;
- swardley/WARDLEY-MAP-REPOSITORY.

### Valor incremental

`decision-analysis` compara alternativas, mas não modelava explicitamente:
- user need;
- value chain;
- dependencies;
- evolution from genesis to commodity;
- inertia;
- co-evolution;
- strategic movement.

Isso é útil para build/buy, platform strategy, innovation e modernização.

### Decisão

Criar `strategic-landscape-mapping`.

A skill mantém o caráter contextual do método: o mapa não produz uma resposta correta nem uma previsão determinística.

## 4. Experimentation upgrade

### Fontes

- growthbook/growthbook;
- PostHog/posthog;
- coreyhaines31/marketingskills.

### Valor incremental

`experiment-design` já era o owner correto. Não criar `growth-experimentation`.

Capabilities absorvidas:
- assignment vs exposure;
- integrity checks;
- sample-ratio mismatch;
- contamination;
- metric-definition drift;
- sequential testing sem peeking ingênuo;
- CUPED/variance reduction com covariável pré-tratamento;
- bandit como objetivo diferente de estimativa causal limpa;
- ligação entre feature flag, rollout e experimento.

### Decisão

UPDATE_EXISTING em `experiment-design`.

## 5. Product management sources

`deanpeters/Product-Manager-Skills`, `ProductHired/open-product-management`, `dend/awesome-product-management` e `RefoundAI/lenny-skills` possuem conteúdo forte, mas o Arsenal já tem owners específicos para discovery, JTBD, prioritization, metrics, experiments, specs e lifecycle.

Decisão: KEEP_EXISTING_OWNERS.

Não importar uma mega-skill de product management.

## 6. Company operating system

### Fontes

- basecamp/handbook;
- PostHog/posthog.com;
- operately/operately;
- kuchin/awesome-ceo;
- kuchin/awesome-cto.

### Conteúdo útil

- princípios explícitos;
- accountability;
- goals/OKRs;
- project check-ins;
- async communication;
- documentation;
- decision cadence;
- people-management practices.

### Overlap

O Arsenal já possui:
- `work-delivery-flow`;
- `team-health-management`;
- `project-health-review`;
- `dashboard-design`;
- `weekly-review-planning`;
- `meeting-to-actions`;
- `agenda-operations`.

As fontes não demonstraram um owner novo suficientemente estreito. Operately é principalmente software opinionado; Basecamp/PostHog são handbooks específicos de empresas.

### Decisão

ABSORB_METHOD_ONLY / REJECT standalone skill.

O padrão útil é manter goals, work, check-ins, decisions e ownership conectados, sem copiar políticas empresariais como universais.

## 7. Awesome lists e diretórios

Fontes como:
- KrishMunot/awesome-startup;
- Ibexoft/awesome-startup-tools-list;
- charlax/entrepreneurship-resources;
- LeCoupa/awesome-bootstrappers;
- ronakganatra/awesome-marketing;
- mmccaff/PlacesToPostYourStartup.

São bons radares de descoberta, mas catálogo não é metodologia.

Decisão:
- KEEP_EXTERNAL_REFERENCE ou ABSORB_METHOD_ONLY;
- nunca criar skill diretamente do ranking/lista sem resolver a fonte original.

## Segurança e portabilidade

Verdict geral:
- metodologias adaptadas: SAFE;
- ferramentas/plataformas: D / tool-dependent.

Não foram executados:
- installers;
- scripts;
- billing systems;
- analytics platforms;
- feature-flag services;
- GTM automation;
- outreach;
- company operating software.

Nenhum serviço externo foi tornado requisito das skills.

## Prova de valor incremental

### saas-pricing-monetization
Should trigger:
- “reestruture nosso pricing SaaS com tiers, usage, credits e rollout”.

Near miss:
- “implemente retry de cobrança e reconciliação” → `payment-billing-operations`.

### go-to-market-strategy
Should trigger:
- “temos produto e alguns usuários, mas não sabemos ICP, motion e canal; monte o GTM”.

Near miss:
- “encontre 20 empresas que podem ser design partners” → `first-customer-research`.

### strategic-landscape-mapping
Should trigger:
- “mapeie onde devemos construir, comprar, padronizar e investir nesta cadeia de valor”.

Near miss:
- “compare dois fornecedores por preço, risco e SLA” → `decision-analysis`.

## Limites

- a triagem dos 30 foi ampla; aprofundamento foi concentrado nas fontes com maior novidade plausível;
- popularidade foi usada como sinal de descoberta, nunca como prova de qualidade;
- números e thresholds trazidos por fontes externas não foram adotados como regras universais;
- práticas de pricing, GTM e experimentation precisam de evidência do negócio real para produzir recomendação consequencial.
