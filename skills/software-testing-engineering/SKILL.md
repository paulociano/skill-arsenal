---
name: software-testing-engineering
description: "Projetar estratégia de testes de software combinando example-based, property-based, integration com dependências reais, contract/e2e e flakiness control, escolhendo a camada mínima que prova cada risco."
---

# Software Testing Engineering

## Objetivo

Projetar testes por risco e contrato observável, indo além de unit tests e TDD local para cobrir propriedades, integrações reais e falhas difíceis de imaginar manualmente.

## Quando usar

- estratégia de testes;
- property-based testing;
- integração com banco/queue/cache/serviço real;
- contract tests;
- flaky tests;
- test pyramid/portfolio;
- regression suites.

## Princípio central

**Teste o risco na camada mais barata que consegue prová-lo.**

## Workflow

1. **Risk map**
   - lógica pura;
   - parsing/serialization;
   - persistence;
   - network/protocol;
   - concurrency;
   - external integrations;
   - user journey.

2. **Example-based**
   - casos nominais e regressões específicas;
   - exemplos pequenos e legíveis;
   - usar TDD quando o comportamento está sendo construído.

3. **Property-based**
   - definir invariantes;
   - generators restritos ao domínio válido;
   - edge cases automáticos;
   - shrinking/minimização do contraexemplo;
   - registrar seed/exemplo mínimo para regressão.

4. **Integration**
   - usar dependência real descartável quando semântica do serviço importa;
   - database, broker, cache ou browser reais podem ser mais confiáveis que mocks profundos;
   - fixtures isoladas;
   - lifecycle determinístico;
   - cleanup explícito.

5. **Contract and API**
   - validar request/response/schema/protocol;
   - producer/consumer contracts quando múltiplos serviços evoluem independentemente;
   - quando houver OpenAPI/GraphQL/schema executável, derivar casos válidos e inválidos em vez de depender só de exemplos manuais;
   - testar violações de schema, validação bypass, edge cases e sequências stateful quando o risco justificar;
   - falhas geradas devem ser minimizadas/reproduzíveis e virar regressão quando confirmadas.

6. **Service virtualization**
   - usar serviço real descartável quando a semântica verdadeira importa;
   - usar virtualization/mocks de rede quando o objetivo é controlar respostas ou falhas difíceis de reproduzir;
   - modelar contratos relevantes: status, headers, payload, latency, timeout, disconnect, rate limit e malformed responses;
   - não deixar mock permissivo aceitar comportamento que o provider real rejeitaria.

7. **Browser/E2E**
   - reservado a jornadas críticas;
   - ambiente previsível e dados isolados;
   - preferir um contexto/sessão limpo por teste quando estado residual puder contaminar resultado;
   - usar assertions que aguardem estado observável em vez de sleeps fixos;
   - preferir locators próximos da experiência do usuário, como role, label e texto, antes de seletores acoplados à implementação;
   - testar múltiplos browsers somente quando fizerem parte da support matrix real;
   - em falhas difíceis, preservar trace/artifacts com DOM, network, console e screenshot quando a ferramenta suportar;
   - evitar cobrir toda regra de negócio apenas por E2E.

8. **Flakiness**
   - eliminar sleeps fixos quando condição observável existe;
   - clock/randomness/network controláveis;
   - retry serve para diagnóstico, não para transformar vermelho em verde;
   - registrar causa antes de quarantine permanente.

9. **Test data**
   - builders/factories;
   - dados mínimos;
   - evitar PII/segredos reais;
   - snapshots/versioned fixtures apenas quando ajudam revisão.

10. **CI**
   - focused suite primeiro;
   - full suite nos gates adequados;
   - artifacts/logs de falha;
   - não baixar threshold só para passar pipeline.

## Property examples

Boas propriedades:
- encode/decode round-trip;
- sort preserves multiset and ordering;
- retry is idempotent;
- parser never crashes on valid grammar;
- balance/invariant remains conserved;
- migration preserves semantic state.

## Regras

- coverage percentual não prova qualidade;
- mock de tudo pode testar apenas o próprio mock;
- dependência real em teste precisa ser descartável e isolada;
- property test precisa de invariant útil, não randomização ornamental;
- falha encontrada deve virar regressão reproduzível;
- browser E2E não deve depender de sleeps arbitrários ou selectors frágeis quando existe condição observável mais estável;
- trace, screenshot ou vídeo ajudam diagnóstico, mas não substituem assertions sobre o efeito correto;
- schema-derived/fuzz testing deve respeitar rate limits, autorização e ambiente;
- service virtualization complementa, não substitui, uma verificação contra integração real quando compatibility é material.

## Integração

`tdd`, `behavior-contract-validation`, `diagnosing-bugs`, `production-go-live`, `system-design-engineering`.

## Provenance

Consolidada de Hypothesis e Testcontainers. Absorve property-based testing, shrinking e dependências reais descartáveis sem exigir Python, Java, Docker ou bibliotecas específicas.

Playwright acrescentou princípios de browser isolation, auto-wait/web-first assertions, locators orientados à superfície do usuário e traces de falha. Schemathesis reforçou schema-derived/property/stateful API testing; Pact reforçou consumer/provider contracts; WireMock, MockServer e Karate reforçaram service virtualization e fault-aware integration testing. A skill continua framework-agnostic e não exige essas ferramentas.
