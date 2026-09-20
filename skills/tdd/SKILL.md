---
name: tdd
description: "Aplicar desenvolvimento orientado a testes por ciclos red–green em fatias verticais de comportamento observável."
---

# tdd

## Objetivo

Aplicar desenvolvimento orientado a testes com ciclos pequenos de red → green, priorizando comportamento observável em interfaces públicas.

## Quando usar

Aplicar desenvolvimento orientado a testes por ciclos red–green em fatias verticais de comportamento observável.

## Workflow

- Definir previamente os seams públicos que serão testados.
- Escrever um teste que falha antes da implementação.
- Implementar somente o necessário para fazê-lo passar.
- Trabalhar em slices verticais, um teste e uma mudança por ciclo.
- Evitar testes acoplados à implementação, tautológicos ou horizontais.

## Teste no aplicativo real

Quando o comportamento só existe com o app inteiro rodando:

- declarar a consequência esperada antes da ação;
- observar o RED real;
- implementar a menor mudança;
- repetir a **mesma** expectativa até GREEN;
- `unknown` não conta como red nem green;
- não editar o oracle para encaixar o comportamento construído sem explicar por que a expectativa original estava errada;
- preferir consequências de domínio/state/network a assertions apenas visuais quando o ambiente permitir.

Se houver instrumentação adequada, encadear com `runtime-ui-verification`.

## Referências

[GitHub · mattpocock/skills · tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)

Origem local: [tdd.docx](../tdd.docx).
