---
name: developer-platform-engineering
description: "Projetar plataformas internas de desenvolvimento com software catalog, ownership, golden paths, templates, self-service e docs-as-code, reduzindo cognitive load sem esconder limites operacionais."
---

# Developer Platform Engineering

## Objetivo

Transformar ferramentas dispersas em uma camada de self-service com ownership, padrões e caminhos seguros para times de produto.

## Quando usar

- internal developer platform;
- developer portal;
- software catalog;
- service ownership;
- project templates;
- golden paths;
- TechDocs/docs-as-code;
- platform engineering.

## Princípio central

**Platform is a product for developers, not a pile of infrastructure tools.**

## Workflow

1. **User research**
   - identificar toil;
   - workflows repetidos;
   - cognitive load;
   - bottlenecks de entrega.

2. **Catalog**
   - service/component/system;
   - owner;
   - lifecycle;
   - repository;
   - docs;
   - dependencies;
   - runtime links.

3. **Golden paths**
   - starter/template;
   - defaults;
   - security/observability/testing baseline;
   - escape hatch documentado;
   - caminhos promovidos só após prova real.

4. **Self-service**
   - create project/service;
   - provision approved resources;
   - environments;
   - docs;
   - ownership transfer;
   - external writes behind permission gates.

5. **Templates**
   - parameterized;
   - versioned;
   - minimal;
   - do not freeze obsolete architecture into every new service.

6. **Docs-as-code**
   - source near code;
   - discoverable through catalog;
   - ownership/freshness;
   - generated docs separated from authored rationale.

7. **Standards**
   - paved road vs mandatory policy explicit;
   - policy-as-code where enforcement is required;
   - measure exceptions.

8. **Measure**
   - lead time;
   - onboarding time;
   - template adoption;
   - support tickets/toil;
   - failed deployments;
   - developer satisfaction.

## Regras

- portal UI without reliable catalog/ownership is decoration;
- self-service without permission boundaries can expand blast radius;
- golden path is preferred path, not prison;
- platform team should remove toil, not centralize every decision;
- templates need upgrade strategy.


## Conformidade de geradores parametrizados (DontPanic)

Quando um golden path gerar projetos por presets ou remoção de features, tratar o **artefato gerado** como produto testável, não apenas o template original:

1. Fixar versão/tag de origem e exigir árvore de trabalho limpa para sincronização reproduzível; documentar quem publica o pacote para evitar pipelines concorrentes no mesmo nome.
2. Declarar cada feature em manifesto: arquivos exclusivos, costuras em arquivos compartilhados, migrations, variáveis de ambiente, dependências e documentação afetada. Remover features sem deixar imports, references ou serviços órfãos.
3. Após renomear projeto/tenant/roles, verificar mecanicamente todas as variantes do identificador anterior, inclusive SQL e configuração; falhar fechado em ocorrência residual.
4. Gerar **segredos novos** por projeto, nunca derivar credenciais do nome ou preservar senhas de seed de template público.
5. Testar uma **matriz por preset** sobre projetos realmente emitidos: install, build, typecheck, lint, unit tests e, nos caminhos críticos, testes de integração/e2e com infraestrutura real. Declarar cobertura ausente no CI, especialmente isolamento multi-tenant e RLS; resposta vazia não prova isolamento correto.
6. Conferir migrations consolidadas contra banco novo, permissões de roles, services do compose e arquivos estáticos exportados; builds bem-sucedidos podem gerar artefatos incompletos.
7. Quando a matriz completa for cara, separar checks rápidos obrigatórios e suite profunda acionável, sem apresentar o check rápido como prova total; preservar fallback de revisão humana e release gate.

Este método foi adaptado dos repositórios [marmottajr/dontpanic-create](https://github.com/marmottajr/dontpanic-create) e [marmottajr/dontpanic](https://github.com/marmottajr/dontpanic). Não executar seus scripts, instaladores nem assumir Node, pnpm, Docker ou acesso a banco disponíveis no ChatGPT. Usar ferramentas do projeto-alvo e validar resultado real quando houver runtime autorizado.

## Integração

`golden-path-capture`, `production-go-live`, `system-design-engineering`, `software-supply-chain-engineering`, `software-observability-engineering`, `project-skill-architecture`.

## Provenance

Consolidada de Backstage: software catalog, software templates, TechDocs and plugin ecosystem. Não presume Backstage runtime disponível.
