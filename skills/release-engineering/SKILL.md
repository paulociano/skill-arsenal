---
name: release-engineering
description: "Projetar e governar releases de software por change impact, versionamento, changelog, release unit, artifact identity, compatibility, publication e comunicação ao consumidor, separando release de deploy."
---

# Release Engineering

## Objetivo

Transformar mudanças verificadas em releases identificáveis, comunicáveis e reproduzíveis, com versionamento e artifact lineage coerentes.

## Quando usar

- definir processo de release;
- SemVer/versionamento;
- changelog/release notes;
- release PR;
- monorepo/package releases;
- package publishing;
- preparar breaking change;
- organizar prerelease/beta/stable;
- separar build, release e deploy.

Para provisionar ou publicar aplicação em ambiente use `production-go-live`. Para exposição progressiva pós-deploy use `progressive-delivery-verification`.

## Princípio central

**Release é uma unidade de mudança consumível e identificável; deploy é a colocação de software em um ambiente.**

## Workflow

1. **Define consumer**
   - end user;
   - API/client;
   - package consumer;
   - internal service;
   - operator.

   Versionamento deve comunicar impacto ao consumidor relevante.

2. **Define release unit**
   - repo/package/service/app;
   - multi-package dependencies;
   - artifact(s);
   - source commit;
   - config/schema assumptions.

3. **Classify change**
   Separar:
   - fix;
   - feature;
   - breaking change;
   - performance/internal;
   - security;
   - deprecation/removal.

   Conventional commits podem ajudar, mas mensagem de commit não é verdade automática sobre impacto.

4. **Compatibility**
   Verificar:
   - API/schema;
   - data migration;
   - protocol;
   - client compatibility;
   - config/env;
   - rollout sequencing;
   - deprecation window.

5. **Version policy**
   Definir conforme ecossistema:
   - SemVer ou outra policy explícita;
   - prerelease channel;
   - patch/minor/major mapping;
   - independent vs fixed/grouped versions em monorepo.

   Não aplicar SemVer onde o produto não possui contrato de versão útil.

6. **Change declaration**
   Capturar perto da contribuição:
   - consumer impact;
   - release type candidate;
   - changelog text;
   - breaking/deprecation note.

   O contributor pode declarar impacto; o release owner ainda valida.

7. **Release readiness**
   Antes de cortar release:
   - required tests green;
   - known blockers reviewed;
   - artifact reproducible/traceable;
   - dependency/security policy satisfeita;
   - docs/migration notes prontas;
   - rollback/recovery constraints conhecidos.

8. **Release PR / candidate**
   Quando útil:
   - agregar releasable changes;
   - atualizar versions;
   - gerar changelog;
   - permitir revisão humana antes de tag/publication;
   - manter branch principal legível.

9. **Build and artifact identity**
   - source commit;
   - version;
   - digest;
   - build provenance quando disponível;
   - package/image/archive identity.

   Preferir promover o mesmo artifact verificado em vez de rebuild silencioso.

10. **Publish**
    - tag/release record;
    - package/artifact publication;
    - release notes;
    - distribution channel;
    - permissions/credentials mínimos;
    - idempotency e recovery onde publicação puder ser repetida.

11. **Communicate**
    Release notes devem destacar:
    - user impact;
    - breaking changes;
    - migration;
    - deprecation;
    - security guidance;
    - known limitations.

    Changelog não precisa reproduzir histórico interno irrelevante ao consumidor.

12. **Post-release**
    - verificar artifacts publicados;
    - confirmar version metadata;
    - monitorar regressões iniciais;
    - corrigir ou yank/deprecate conforme política e suporte do ecossistema.

## Monorepos

Definir explicitamente:
- package graph;
- dependentes afetados;
- linked/fixed groups;
- independent versions;
- cross-package compatibility;
- ordem de publicação.

## Automation

Automatizar quando o contrato estiver estável:
- version calculation;
- changelog generation;
- release PR;
- tagging;
- publication;
- provenance.

Mas preservar human gate quando:
- change impact é ambíguo;
- breaking change material;
- publicação irreversível;
- security disclosure;
- múltiplos consumidores/branches têm políticas distintas.

## Guardrails

- commit prefix não prova consumer impact;
- changelog gerado não substitui migration guidance;
- versão incrementada não prova release testada;
- não rebuildar depois do QA sem registrar nova identidade;
- publicação e deploy são fronteiras diferentes;
- breaking change acidental não vira "patch" porque a mensagem dizia fix;
- secrets/token de registry não entram em release notes/logs;
- rollback de package publicado depende do ecossistema e pode exigir nova versão.

## Entregável

- release unit;
- change classification;
- compatibility assessment;
- version;
- changelog/release notes;
- artifact identity;
- publish plan;
- verification;
- rollback/deprecation constraints.

## Integração

Combina com:
- `software-testing-engineering`;
- `software-supply-chain-engineering`;
- `build-system-engineering`;
- `production-go-live`;
- `progressive-delivery-verification`;
- `verify-before-claim`.

## Provenance

Adaptada de:
- https://github.com/semantic-release/semantic-release
- https://github.com/changesets/changesets
- https://github.com/googleapis/release-please

Preserva consumer-impact versioning, contribution-time change declaration, release PRs, changelog/version automation e artifact publication, sem exigir Node.js, Conventional Commits ou qualquer registry específico.
