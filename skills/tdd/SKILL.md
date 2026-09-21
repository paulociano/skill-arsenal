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

## Test doubles de compatibilidade

Quando produção depende de um componente indisponível, caro ou inadequado para CI, um substituto de desenvolvimento pode ser útil se preservar **semântica observável**, mesmo sendo deliberadamente lento ou simples.

- reproduzir contrato, parser, operadores, erros e regras de visibilidade relevantes ao consumidor;
- preferir correção simples a otimizações que criem divergência;
- marcar explicitamente o substituto como não-production quando performance/armazenamento/arquitetura não forem equivalentes;
- rodar, quando possível, a mesma suíte contra implementação real e substitute;
- tratar diferenças descobertas como regressões de compatibilidade, não como oportunidade de ajustar o teste ao double;
- não afirmar equivalência fora da superfície realmente coberta pelos testes.

Um test double de compatibilidade é uma ferramenta de teste, não um fallback de produção.

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

Test doubles de compatibilidade inspirados em [planetscale/lead](https://github.com/planetscale/lead), que privilegia semântica correta de desenvolvimento/teste sobre performance de produção.

Origem local: [tdd.docx](../tdd.docx).
