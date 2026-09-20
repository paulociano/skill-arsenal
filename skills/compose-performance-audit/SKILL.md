---
name: compose-performance-audit
description: "Auditar desempenho de Jetpack Compose com baseline, diagnóstico, correção e comparação de métricas antes e depois."
---

# compose-performance-audit

## Objetivo

Auditar performance de Jetpack Compose com um ciclo verificável **Measure → Diagnose → Fix → Verify**, usando métricas reais antes e depois das mudanças.

## Quando usar

- app Compose "parece lento" sem causa clara;
- scroll jank amplo;
- início de performance sprint;
- pre-release performance gate;
- pedido de auditoria escrita de performance.

## Quando não usar

Se já existe um sintoma muito específico, diagnosticar diretamente a causa correspondente em vez de rodar auditoria ampla.

## Workflow

### 1. Measure

- estabelecer baseline **antes** de alterar código;
- medir variante release, com configuração real de otimização;
- usar hardware físico quando a conclusão depender de performance representativa;
- registrar startup/frame timing e ambiente.

### 2. Diagnose
Investigar, conforme o projeto:

- Compose Compiler reports;
- estabilidade e skippability;
- recomposition hotspots;
- state reads em fase errada;
- Lazy layouts;
- side effects/flows;
- modifier allocation/order;
- subcomposition;
- baseline/profile/build configuration.

### 3. Fix

- uma causa nomeada por vez;
- diff pequeno e atribuível;
- preferir um fix por PR/commit lógico;
- re-medir após cada mudança importante.

### 4. Verify

- comparar a mesma métrica antes/depois;
- verificar regressões;
- regenerar artefatos de baseline quando aplicável;
- criar guardrails/CI quando houver mecanismo confiável;
- produzir relatório com ambiente, baseline, diagnóstico, fixes, deltas e itens abertos.

## Princípios

- Performance sem baseline é palpite.
- Skippability é diagnóstico, não KPI final.
- "Mais estável" não prova "mais rápido".
- Um fix só é aceito se a métrica relevante melhorar ou, no mínimo, não regredir e a razão para mantê-lo for explícita.
- Não copiar números de benchmark entre máquinas/projetos como se fossem comparáveis.

## Ferramentas e dependências

- usar `library-version-grounding` antes de aplicar recomendações dependentes de Compose/Kotlin/AGP;
- usar GitHub/arquivos do projeto e ferramentas de execução realmente disponíveis;
- não presumir device, Gradle, adb, Layout Inspector, Macrobenchmark ou plugins instalados;
- quando esses recursos não estiverem disponíveis, produzir plano de diagnóstico e comandos verificáveis, mas não afirmar ganho de performance;
- fechar com `verify-before-claim`.

## Referências

Adaptada de skydoves/compose-performance-skills, especialmente o orchestrator `audit/auditing-compose-performance` e seu índice por sintoma/API.

Origem local: [compose-performance-audit.docx](../compose-performance-audit.docx).
