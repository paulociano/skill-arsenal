---
name: debug-and-fix
description: Investiga, corrige e valida bugs em software com diagnóstico estruturado, testes e revisão proporcional ao risco.
---

# Debug And Fix

## Objetivo
Encontrar a causa raiz de um bug, corrigi-lo com a menor mudança segura e validar o resultado.

## Skills candidatas
- diagnosing-bugs
- code-understanding-audit
- tdd
- code-review
- verify-before-claim

## Workflow
1. Reproduza ou caracterize o problema.
2. Use `diagnosing-bugs` para formular e testar hipóteses.
3. Use `code-understanding-audit` quando o fluxo afetado ainda não estiver claro.
4. Use `tdd` quando um teste de regressão agregar valor.
5. Implemente a menor correção coerente.
6. Use `code-review` quando o risco ou a abrangência justificar revisão adicional.
7. Use `verify-before-claim` antes de declarar o bug resolvido.

## Regra de parcimônia
Não transforme correções simples em auditorias completas sem necessidade.
