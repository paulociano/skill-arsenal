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

## Integração

`golden-path-capture`, `production-go-live`, `system-design-engineering`, `software-supply-chain-engineering`, `software-observability-engineering`, `project-skill-architecture`.

## Provenance

Consolidada de Backstage: software catalog, software templates, TechDocs and plugin ecosystem. Não presume Backstage runtime disponível.
