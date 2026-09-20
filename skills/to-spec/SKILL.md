---
name: to-spec
description: "Converter decisões de uma conversa ou projeto em especificação executável sem reiniciar descoberta já resolvida."
---

# to-spec

## Objetivo

Sintetizar uma conversa e o contexto de um projeto em uma especificação executável, sem reiniciar a descoberta com uma nova entrevista.

## Quando usar

Converter decisões de uma conversa ou projeto em especificação executável sem reiniciar descoberta já resolvida.

## Workflow

1. Reunir decisões e evidências da conversa e do projeto.
2. Organizar requisitos e decisões na estrutura abaixo.
3. Separar requisitos de implementação e marcar somente lacunas indispensáveis.
4. Revisar intenção, execução, escopo dispensável e clareza.
5. Entregar a especificação e critérios verificáveis.

## Estrutura

- Problem Statement
- Solution
- User Stories
- Implementation Decisions
- Testing Decisions
- Out of Scope
- Further Notes

## Regras

Sintetizar o que já foi decidido; não fazer uma nova rodada de descoberta salvo quando faltar algo indispensável.

## Disciplina de PRD incorporada

- começar pela tarefa do usuário, resultado desejado, goals, non-goals e sucesso observável;
- preferir o estado final coerente mais simples, não o menor diff;
- incluir compatibilidade/migração apenas quando usuários, dados ou contratos reais exigirem;
- evitar escopo especulativo, abstrações prematuras e defesas contra futuros imaginários;
- revisar em passes de **Intent → Execution → Subtraction → Clarity**;
- manter checklist vivo e atualizá-lo quando descobertas invalidarem o plano, em vez de acumular tarefas compensatórias sobre uma fundação errada.

## Decisões da especificação

Quando a spec nasce de uma ideia ainda aberta:

- fechar decisões nas dimensões: solution shape, expected output, normal/edge/failure behavior, actor/context, scope boundaries e success criteria;
- defaults devem ser grounded no codebase quando houver evidência;
- separar requisito de plano de implementação;
- modular design deve privilegiar interfaces estáveis e esconder complexidade;
- open questions só permanecem quando realmente não podem ser fechadas, com owner/path de resolução;
- não exigir nova entrevista quando a conversa atual já resolveu essas decisões.

## Referências

[GitHub · mattpocock/skills · to-spec](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec)

Origem local: [to-spec.docx](../to-spec.docx).
