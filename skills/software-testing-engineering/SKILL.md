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

## Gate de qualidade para testes gerados por agentes (2026-10-19)

Depois de criar ou modificar testes com auxílio de IA, fazer revisão separada da produção, focada em **capacidade de detectar regressão**:

1. Para cada teste, declarar comportamento/invariante que deveria falhar se o sistema estivesse errado; remover testes tautológicos ou que apenas confirmem mocks.
2. Preferir mocks nos limites externos; não mockar o próprio estado, algoritmo ou unidade sob teste a ponto de tornar o resultado predeterminado.
3. Inspecionar assertions de efeitos observáveis, estados de erro, concorrência, permissões e casos negativos relevantes; evitar assertions de detalhes internos sem contrato.
4. Consolidar casos duplicados por parametrização quando isso preservar clareza; não otimizar contagem de testes como objetivo.
5. Se possível, fazer teste de sensibilidade seguro (mutação local ou defeito controlado) e confirmar que a suíte falha; sem execução, registrar apenas a hipótese.
6. Preservar regressões de defeitos reais e comparar o teste à spec, não à implementação atual potencialmente incorreta.
7. Separar **teste escrito**, **teste executado**, **teste aprovado** e **defeito efetivamente detectável**; não inferir os últimos estados dos primeiros.

**Proveniência:** [amElnagdy/guard-skills](https://github.com/amElnagdy/guard-skills), especialmente a metodologia `test-guard` descrita no README consultado em 2026-10-19. Adaptação apenas metodológica, sem instalar Skills CLI, executar código externo ou pressupor agente independente.

## Regressão cumulativa sob requisitos evolutivos (SlopCodeBench, 2026-10)

Quando funcionalidades forem adicionadas em etapas (especialmente por coding agents), **não redefinir sucesso como apenas passar nos testes do requisito mais recente**:

1. Preservar suíte dos comportamentos já aceitos em cada etapa, vinculada à versão da especificação. Não reescrever assertions antigas para acomodar involuntariamente bugs novos.
2. Executar testes direcionados à mudança, depois regressões dos contratos anteriores afetados e, no gate apropriado, a suíte integrada completa. Registrar explicitamente os checks não executados.
3. Relatar **Core** (casos exigidos pela etapa) separadamente de **Strict** (Core + outras categorias relevantes + regressões). Sucesso parcial não autoriza claim de compatibilidade integral.
4. Incluir cenário cumulativo atravessando estados, persistência, permissões ou APIs afetadas quando houver risco. Verificar também o resultado **final da sequência**.
5. Distinguir **testes falhos**, **bugs distintos** e **sinais estáticos de qualidade**: muitas falhas podem ter uma causa, e lint/complexidade não substituem teste funcional.
6. Em comparações, fixar catálogo, versões, runner, categorias, ambiente e denominadores; relatar variação de repetições e interrupções quando houver.

**Aceite:** requisito novo funcionando com regressão antiga ainda falhando é resultado **parcial**, não concluído. Sem suíte executável ou evidência fresca, limitar a conclusão ao desenho dos testes.

**Proveniência:** [artigo SlopCodeBench](https://arxiv.org/abs/2603.24755) e [HumanLayer, 2026-10-15](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md). Metodologia cumulativa, sem exigir runner original.

## Espelho local de CI com cobertura explícita

Quando Actions estiver indisponível ou o pedido for reproduzir CI localmente:
1. Ler o workflow e job solicitados; extrair comandos, ordem, dependências, condições, working-directory, env, versões, serviços, actions e matriz. Não inferir checks obrigatórios apenas do trigger: confirmar branch protection/required checks quando acessíveis.
2. Inspecionar comandos antes de executar; limitar ao escopo de verificação autorizado. Não reproduzir deploy, release, publicação ou mutações remotas por estarem no YAML.
3. Executar comandos correspondentes na ordem/dependências reais. Validar actions reutilizáveis separadamente; não tratá-las como comandos locais conhecidos.
4. Registrar versões reais; divergência da versão do runner, serviços ausentes, secrets indisponíveis e combinações de matriz não executadas impedem alegar paridade completa. Verificar presença de secrets sem revelar valores; nunca usar valores fictícios para obter PASS.
5. Emitir tabela por job/step: PASS, FAIL, SKIPPED ou NOT REPLICATED, com comando, evidência e motivo. Interromper a cadeia dependente após falha, preservando checks independentes quando apropriado.
6. Distinguir checks locais aprovados de CI remoto aprovado. Nenhum resultado local prova merge gate verde sem observar o gate real.

**Aceite:** matriz com três versões e uma execução local deve reportar duas combinações não verificadas. Pedido para criar pipeline novo não ativa este espelho.
**Proveniência:** adaptação metodológica de https://github.com/mgiovani/cc-arsenal/blob/main/skills/ci-local/SKILL.md (2026-10-21); sem instalar ferramentas ou usar fallback de versão como equivalência.
