---
name: postgres-migration-safety
description: "Planejar, revisar e validar migrações PostgreSQL em produção considerando versão, locks, tamanho de dados, compatibilidade entre deploys, backfill, rollback e evidência pós-migração."
---

# PostgreSQL Migration Safety

## Objetivo
Transformar uma mudança de schema em um plano operacional seguro para PostgreSQL real, evitando que uma migration correta em banco vazio cause lock prolongado, incompatibilidade de aplicação ou corrupção/perda de dados em produção.

## Quando usar
- ALTER TABLE em produção;
- add/drop/rename/change type de coluna;
- índices e constraints em tabelas grandes;
- backfills;
- zero-downtime migration;
- rollback/roll-forward de schema;
- teste de migration contra dados representativos.

## Workflow
1. **Ground version** — confirmar versão PostgreSQL e documentação correspondente; comportamento de DDL muda entre versões.
2. **Inventory** — schema atual, tamanho/row count, índices/constraints, dependências, long transactions, replicas e deploy topology.
3. **Classify operations** — para cada DDL, determinar lock requerido, duração plausível, rewrite/scan e efeito em reads/writes.
4. **Compatibility plan** — ordenar app deploy e schema deploy para que versões old/new coexistam durante rollout quando necessário.
5. **Backfill plan** — para grandes volumes, definir batches, ordering/keyset, pacing, idempotência, resume point e monitoramento.
6. **Constraint/index plan** — preferir padrões staged/concurrent suportados pela versão quando reduzem bloqueio; considerar failure artifacts como invalid indexes.
7. **Preflight** — verificar blockers, espaço, replication lag, timeout/lock timeout, backups e observabilidade proporcional ao risco.
8. **Test** — executar primeiro em clone/staging representativo quando disponível; medir duração e comportamento concorrente.
9. **Execute with gate** — mudanças materiais exigem aprovação e janela/stop conditions explícitos.
10. **Validate** — schema esperado, constraints, row counts/checks, app behavior, errors, locks, lag e readback da migration.
11. **Rollback or roll-forward** — definir antes da execução; não assumir que todo DDL é reversível sem perda.

## Padrões
- expand → migrate/backfill → contract para renames/type changes incompatíveis;
- adicionar constraint sem validação e validar depois quando a versão/operação suportar;
- índices concorrentes quando apropriado, com verificação de estado inválido após falha;
- separar remoção de uso pela aplicação da remoção física do schema;
- backfill deve poder pausar e retomar sem duplicar efeitos.

## Regras
- não copiar tabelas de lock de memória: verificar na documentação da versão alvo;
- metadata-only não significa risk-free: aquisição de lock ainda pode esperar atrás de transação longa;
- `DROP COLUMN` lógico não prova remoção física imediata dos bytes;
- não aplicar migration destrutiva sem backup/restore posture e aprovação adequados;
- não chamar uma migration de zero-downtime sem testar compatibilidade e concorrência reais;
- ORM migration generator não substitui análise operacional do SQL produzido.

## Saída
- operations ledger;
- risk/lock assessment;
- deploy sequence;
- backfill/validation plan;
- rollback/roll-forward;
- evidência executada vs. ainda pendente.

## Integração
`library-version-grounding`, `behavior-contract-validation`, `verify-before-claim`, `debug-and-fix`.

## Origem metodológica
Adaptada de `timescale/pg-aiguide · postgres-database-migration`, preservando lock awareness, staged constraints/indexes, backfills e pre/post validation sem exigir seu MCP ou runtime.
