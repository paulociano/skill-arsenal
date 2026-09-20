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

## Quando tentativas deixam de informar

- Antes de repetir uma tentativa, explicite a nova evidência ou a hipótese que ela distingue. Se sucessivas tentativas não reduzem a incerteza, pare a repetição, confira se o caminho de código/configuração é realmente executado e reformule a hipótese.
- Diferencie correção causal de mitigação. Guards, retries e tratamento de erro podem ser legítimos; não os apresente como remoção da causa sem evidência. Quando a causa estiver fora do alcance, registre a limitação, o efeito esperado da mitigação e como verificá-la.
- Ao receber contestação, confira o caso e a evidência específica. Não reverta uma conclusão apenas pela pressão nem defenda a hipótese anterior por apego; contexto novo do usuário é evidência relevante.
- Se novas evidências invalidarem a abordagem, escolha a solução mais simples adequada ao escopo atual. Não faça reescrita ampla, varredura global ou prevenção especulativa apenas para justificar o trabalho anterior.
- Releia estado quando houver mudança, concorrência ou dúvida concreta de validade; não repita leituras idênticas por ritual.

Síntese metodológica de [buddhist-method](https://github.com/nai0om/buddhist-method/blob/745caa74ef27fce7c57cbdbf27af5add3de884d7/SKILL.md), com suas referências de debugging e tentativas sem progresso. Modificação do Arsenal em 2026-09-20: integração secular e contextual, sem gatilho global, alegações religiosas ou número fixo de tentativas. [Licença MIT da origem](references/buddhist-method-MIT.txt).

## Referências

[GitHub · mattpocock/skills · diagnosing-bugs](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)

Origem local: [diagnosing-bugs.docx](../diagnosing-bugs.docx).
