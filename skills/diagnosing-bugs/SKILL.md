---
name: diagnosing-bugs
description: "Diagnosticar bugs difíceis e regressões com reprodução mínima, hipóteses falsificáveis e teste da correção."
---

# diagnosing-bugs

## Objetivo

Diagnosticar bugs difíceis e regressões de performance por meio de um loop disciplinado e verificável.

## Quando usar

Diagnosticar bugs difíceis e regressões com reprodução mínima, hipóteses falsificáveis e teste da correção.

## Workflow

1. Construir primeiro um feedback loop rápido, determinístico e capaz de reproduzir o sintoma exato.
2. Reproduzir e minimizar o caso.
3. Gerar 3–5 hipóteses falsificáveis antes de testar.
4. Instrumentar uma variável por vez.
5. Criar teste de regressão no seam correto, aplicar a correção e reverificar o repro original.
6. Remover instrumentação e artefatos temporários.

## Regras

Sem um loop vermelho que capture o bug real, não avançar para teorias.

## Referências

[GitHub · mattpocock/skills · diagnosing-bugs](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)

Origem local: [diagnosing-bugs.docx](../diagnosing-bugs.docx).
