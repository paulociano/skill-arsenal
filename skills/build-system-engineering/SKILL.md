---
name: build-system-engineering
description: "Projetar e otimizar build systems e monorepos com dependency graphs, hermetic inputs, incremental execution, content-addressed caching, remote execution e reproducibility sem confundir cache hit com correção."
---

# Build System Engineering

## Objetivo

Tornar builds grandes previsíveis, reproduzíveis e incrementais por dependências explícitas e inputs controlados.

## Quando usar

- monorepo;
- Bazel/Pants-like build;
- slow builds;
- build caching;
- hermetic builds;
- remote execution;
- dependency graph;
- reproducible artifacts.

## Princípio central

**Um build só pode reutilizar resultado se todos os inputs que afetam o output estiverem modelados.**

## Workflow

1. **Graph**
   - targets;
   - source inputs;
   - generated inputs;
   - dependencies;
   - outputs.

2. **Hermeticity**
   - toolchain/version explicit;
   - environment variables controlled;
   - no undeclared host files;
   - network access minimized/declared.

3. **Incrementality**
   - rebuild affected graph only;
   - avoid global invalidation;
   - generated outputs content-addressed when suitable.

4. **Caching**
   - key from true inputs;
   - local/remote cache;
   - cache poisoning/corruption handling;
   - clean-build comparison periodically.

5. **Parallelism**
   - independent targets concurrently;
   - resource limits;
   - critical path visibility.

6. **Remote execution**
   - deterministic actions;
   - explicit platform/toolchain;
   - artifact transport;
   - retry semantics.

7. **Monorepo**
   - ownership boundaries;
   - dependency visibility;
   - affected tests/builds;
   - avoid forcing every package into same release lifecycle.

8. **Metrics**
   - clean build;
   - incremental build;
   - cache hit rate;
   - critical path;
   - queue/execution time;
   - flake/failure rate.

## Regras

- cache hit does not prove output correctness if key is incomplete;
- hermeticity is a spectrum but hidden host dependency is technical debt;
- remote cache should not store secrets;
- monorepo is organizational choice, not automatic best practice;
- build optimization starts with critical path measurement.

## Integração

`software-testing-engineering`, `production-go-live`, `software-supply-chain-engineering`, `codebase-design`, `software-observability-engineering`.

## Provenance

Consolidada de Bazel, Pants and Dagger patterns: dependency graph, hermetic/repeatable execution, content-addressed caching and explicit artifacts. Não exige nenhum desses runtimes.
