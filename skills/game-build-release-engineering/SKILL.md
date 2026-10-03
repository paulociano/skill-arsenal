---
name: game-build-release-engineering
description: "Projetar e validar builds e releases de jogos por plataforma com reproducible configuration, asset/content packaging, signing/secrets, CI, versioning, smoke tests, release artifacts e rollback/update strategy."
---

# Game Build & Release Engineering

## Objetivo

Transformar projeto de jogo em artefatos reproduzíveis e verificáveis por plataforma, separando build, content delivery, signing e publicação.

## Quando usar

- Windows/macOS/Linux builds;
- mobile;
- WebGL/web;
- console build planning;
- CI/CD de jogos;
- addressables/asset bundles/content catalogs;
- release candidate;
- signing/versioning.

## Workflow

1. **Ground**
   - engine/version;
   - target platform;
   - scripting/backend;
   - architecture;
   - build config;
   - content pipeline;
   - store/distribution target.

2. **Version**
   - game version;
   - build number;
   - commit/revision;
   - content/catalog version;
   - package/plugin lock.

3. **Build inputs**
   - deterministic project settings quando possível;
   - explicit scenes/content;
   - no editor-only dependency leaking into player;
   - environment-specific config externalized.

4. **Content packaging**
   - direct assets versus bundled/addressable content;
   - reference ownership;
   - load/release lifecycle;
   - catalog/content compatibility;
   - remote content rollback/update policy.

5. **Secrets/signing**
   - certificates/keystores/tokens fora do repo;
   - least privilege;
   - CI secret store;
   - never echo secret values;
   - signing material rotation/recovery plan.

6. **CI**
   - clean checkout;
   - restore/pinned dependencies;
   - license activation where required;
   - tests;
   - build;
   - artifact upload;
   - checksums/metadata.

7. **Release candidate**
   - immutable build artifact;
   - release notes;
   - known issues;
   - smoke test on target;
   - save compatibility;
   - online/backend compatibility;
   - content catalog compatibility.

8. **Platform validation**
   - install/update/uninstall;
   - permissions;
   - first boot;
   - controller/input;
   - suspend/resume where applicable;
   - path/storage differences;
   - graphics/audio defaults.

9. **Publish**
   - staged channels/branches when platform permits;
   - do not rebuild after QA approval if the store artifact can reuse the same binary;
   - record artifact hash/build id.

10. **Rollback/update**
    - player rollback may be limited by store;
    - remote content needs compatible catalog;
    - save migrations may be forward-only;
    - declare rollback limits before launch.

## Addressable/content lifecycle

- async load precisa de error path;
- ownership/ref counts explícitos;
- release assets/instances correctly;
- content update cannot assume player and catalog are same version;
- test offline/missing/old catalog conditions.

## CI guardrails

- cache is optimization, not source of truth;
- clean build periodically;
- editor license handling is operational dependency;
- build success does not prove runtime;
- console/NDA toolchains cannot be inferred or reproduced from public repos.

## Regras

- release candidate é artifact, não branch abstrata;
- QA deve testar o mesmo artifact que será publicado quando possível;
- secrets nunca em build logs;
- remote content incompatível pode quebrar um binary saudável;
- version every surface that can drift independently.

## Integração

`game-testing-quality-engineering`, `production-go-live`, `game-performance-engineering`, `save-game-persistence-engineering`, `live-game-operations-engineering`, `library-version-grounding` e `verify-before-claim`.

## Provenance

Consolidada de GameCI Unity Actions/Test Runner, Unity Addressables Samples e práticas oficiais de package/release observadas em Cinemachine/Input System. Não presume acesso a runners, Unity licensing, stores ou console SDKs.
