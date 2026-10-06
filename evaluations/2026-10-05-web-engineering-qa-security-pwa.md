# Avaliação — engenharia web, QA, segurança, PWA e inovação

Data: 2026-10-05

## Objetivo

Avaliar o lote pesquisado de repositórios relevantes para engenharia de software, testes, auditoria e inovação aplicada a web apps/PWAs, comparando capabilities com o Arsenal canônico e materializando somente ganho incremental.

## Resultado executivo

Criados:
- `web-application-security-audit`;
- `pwa-engineering`;
- stack `web-app-engineering-audit`.

Atualizados:
- `software-testing-engineering` com browser E2E mais robusto inspirado no Playwright;
- `secure-code-privacy-review` para separar code review de auditoria web em runtime;
- `software-engineering-cycle` com roteamento para segurança web e PWA;
- `ARSENAL INDEX.md`.

Mantidos sem duplicação:
- `system-design-engineering`;
- `code-review`;
- `web-quality-audit`;
- `software-supply-chain-engineering`.

## Triage

| Fonte | Classe | Decisão | Owner |
|---|---|---|---|
| OWASP/ASVS | A/B | CREATE_NEW + ABSORB_METHOD_ONLY | web-application-security-audit |
| OWASP/wstg | A/B | CREATE_NEW + ABSORB_METHOD_ONLY | web-application-security-audit |
| microsoft/playwright | A/D | UPDATE_EXISTING | software-testing-engineering |
| GoogleChrome/workbox | A/D | CREATE_NEW + ABSORB_METHOD_ONLY | pwa-engineering |
| pwa-builder/PWABuilder | B/D | ABSORB_METHOD_ONLY | pwa-engineering |
| GoogleChrome/lighthouse | A/D | KEEP_EXISTING_OWNER | web-quality-audit |
| donnemartin/system-design-primer | A/B | KEEP_EXISTING_OWNER | system-design-engineering |
| google/eng-practices | B | KEEP_EXISTING_OWNER | code-review |
| semgrep/semgrep | A/D | KEEP_EXISTING_OWNER | software-supply-chain-engineering / secure-code-privacy-review |
| ossf/scorecard | A/D | KEEP_EXISTING_OWNER | software-supply-chain-engineering |
| SonarSource/sonarqube | D | KEEP_EXTERNAL_REFERENCE | code-review / quality tooling |
| cypress-io/cypress | A/D | KEEP_EXTERNAL_REFERENCE | software-testing-engineering |
| vitest-dev/vitest | A/D | KEEP_EXTERNAL_REFERENCE | software-testing-engineering |
| testing-library/dom-testing-library | B/D | KEEP_EXISTING_OWNER | software-testing-engineering / runtime-ui-verification |
| thoughtworks/build-your-own-radar | C/D | REJECT standalone skill | decision-analysis remains owner of technology trade-offs |

## 1. OWASP ASVS + WSTG

### O que acrescentam

O Arsenal tinha revisão de segurança no código e supply chain, mas não um owner explícito para auditoria autorizada da aplicação em runtime.

ASVS adiciona:
- requisitos verificáveis;
- versionamento do requisito;
- estrutura útil para matriz de cobertura.

WSTG adiciona:
- taxonomia de cenários;
- teste de autenticação, autorização, sessão, input, client-side, API e business logic;
- prática de referenciar cenários por versão.

### Decisão

Criar `web-application-security-audit`.

Separação de ownership:
- code/diff: `secure-code-privacy-review`;
- dependências/artifacts: `software-supply-chain-engineering`;
- comportamento de segurança no alvo autorizado: `web-application-security-audit`.

Guardrails adicionados:
- autorização explícita;
- testes proporcionais e não destrutivos;
- sem DoS, credential stuffing, persistência ou pivot fora do escopo;
- proof mínima;
- redaction de material sensível;
- coverage explícita em vez de claim de segurança total.

## 2. Playwright

### Valor incremental

`software-testing-engineering` já possui owner correto para E2E, integração e flakiness. Playwright não justifica skill própria.

Capabilities absorvidas:
- isolamento de browser/context por teste;
- auto-wait e assertions orientadas a estado observável;
- locators resistentes baseados em role/label/text quando apropriado;
- cross-browser somente quando faz parte da support matrix;
- traces com DOM/network/console/screenshots como artefatos de falha;
- evitar sleeps e selectors acoplados à implementação.

### Decisão

UPDATE_EXISTING em `software-testing-engineering`.

A CLI, MCP, instalação e runtime do Playwright não foram incorporados como requisito.

## 3. Workbox + PWABuilder

### Valor incremental

O Arsenal possuía qualidade web, design e runtime verification, mas não tinha owner para:
- service-worker lifecycle;
- estratégia de caching por classe de recurso;
- offline contract;
- update compatibility;
- storage/eviction;
- background sync/push;
- installability/manifest;
- packaging como etapa opcional.

### Decisão

Criar `pwa-engineering`.

Workbox contribui principalmente com caching e service-worker patterns. PWABuilder contribui com installability, packaging e uma visão operacional de PWA. Nenhuma ferramenta foi tornada obrigatória.

## 4. Lighthouse

`web-quality-audit` já é adaptada de Lighthouse e separa lab metrics, field evidence e synthetic score.

Decisão: KEEP_EXISTING_OWNER.

Nenhuma duplicação.

## 5. System Design Primer

`system-design-engineering` já foi criada a partir dessa fonte e cobre requirements → workload → SLOs → design → scale → failures → operations → trade-offs.

Decisão: KEEP_EXISTING_OWNER.

## 6. Google Engineering Practices

O lote anterior de software engineering já registrou overlap e o repositório está arquivado. O Arsenal já possui `code-review` com separação Standards/Spec, impacto, simplificação, blast radius e coverage.

Decisão: KEEP_EXISTING_OWNER.

Não criar nova skill de code review.

## 7. Semgrep, Scorecard e SonarQube

- Semgrep já contribuiu para `software-supply-chain-engineering` e padrões de static analysis.
- Scorecard já foi incorporado ao owner de supply chain com a regra de não tratar score agregado como garantia.
- SonarQube é tooling de continuous inspection; seus conceitos de code quality não justificam novo owner diante de `code-review`, testing e supply chain.

Decisão: nenhuma nova skill.

## 8. Cypress, Vitest e Testing Library

Todos são úteis, mas o valor é majoritariamente implementação/tooling.

O owner canônico deve permanecer technology-agnostic:
- unit/component/integration/E2E por risco;
- comportamento observável;
- dependências reais quando semântica importa;
- locators e assertions resistentes;
- controle de flakiness.

Decisão: KEEP_EXTERNAL_REFERENCE / KEEP_EXISTING_OWNER.

## 9. Thoughtworks Build Your Own Radar

### O que faz de verdade

O repositório é uma aplicação para renderizar um technology radar a partir de Sheet/CSV/JSON, com rings como Adopt, Trial, Assess e Caution.

### Limite

Ele não fornece sozinho uma metodologia suficientemente completa para:
- due diligence tecnológica;
- scoring de fit;
- evidência de maturidade;
- decisão de adoção;
- governança de experimentos.

Criar `technology-radar` a partir desse repo importaria mais branding/formato do que processo decisório novo.

### Decisão

C/D — REJECT standalone skill.

`decision-analysis` continua owner de trade-offs e foi usado na nova stack `web-app-engineering-audit` para modernização/adoção tecnológica. Um futuro lote pode criar uma skill de technology strategy se trouxer metodologia independente e empiricamente útil, não apenas o renderer.

## Stack criada: web-app-engineering-audit

A auditoria de web apps é um fluxo recorrente que cruza owners já existentes. A nova stack seleciona apenas os necessários e produz:
- system map;
- findings deduplicados;
- risk register;
- evidência e limitações;
- roadmap Now/Next/Later;
- avaliação de modernização por trade-off.

A stack não exige executar todas as skills.

## Segurança e portabilidade

Verdict geral: CAUTION para ferramentas; SAFE para metodologia adaptada quando aplicada dentro dos guardrails.

Não foram executados:
- scanners;
- installers;
- CLIs;
- containers;
- browser automation externa;
- pentest suites;
- PWABuilder/Workbox runtime;
- SonarQube/Semgrep/Scorecard.

Dependências específicas foram removidas do contrato das skills. Ferramentas podem ser usadas apenas quando realmente disponíveis e apropriadas.

## Prova de valor incremental

### web-application-security-audit
Should trigger:
- “audite a segurança desse web app/API em staging autorizado”.

Near miss:
- “revise este diff de auth” → `secure-code-privacy-review`.

### pwa-engineering
Should trigger:
- “faça nosso app funcionar offline e revise o service worker/update”.

Near miss:
- “melhore LCP e acessibilidade” → `web-quality-audit`.

### web-app-engineering-audit
Should trigger:
- “faça uma auditoria técnica completa deste SaaS/PWA e priorize o roadmap”.

Near miss:
- “corrija este bug visual” → `debug-and-fix` / `improve-existing-web-app`.

## Fontes

- https://github.com/OWASP/ASVS
- https://github.com/OWASP/wstg
- https://github.com/microsoft/playwright
- https://github.com/GoogleChrome/workbox
- https://github.com/pwa-builder/PWABuilder
- https://github.com/GoogleChrome/lighthouse
- https://github.com/donnemartin/system-design-primer
- https://github.com/google/eng-practices
- https://github.com/semgrep/semgrep
- https://github.com/ossf/scorecard
- https://github.com/SonarSource/sonarqube
- https://github.com/cypress-io/cypress
- https://github.com/vitest-dev/vitest
- https://github.com/testing-library/dom-testing-library
- https://github.com/thoughtworks/build-your-own-radar

## Limites

- avaliação aprofundou os owners e as fontes com maior ganho incremental; ferramentas redundantes foram triadas por overlap e não transformadas em skills;
- critérios de browser/PWA e padrões OWASP mudam, portanto versões e support matrix devem ser revalidados em uso concreto;
- auditoria de segurança por esta skill não substitui pentest profissional quando escopo, obrigação regulatória ou risco exigirem avaliação especializada.
