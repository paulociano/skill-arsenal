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

## Spec como artefato vivo e convergência

Quando a implementação nasce diretamente da spec:

1. manter uma cadeia explícita **spec → plano → tarefas → implementação → verificação**;
2. requisitos descrevem what/why; decisões de implementação ficam no plano;
3. incerteza material deve aparecer como marcador/pergunta explícita, não ser preenchida silenciosamente;
4. checar consistência cruzada entre spec, plano e tarefas antes de executar;
5. após implementação, comparar o estado real com os três artefatos;
6. gaps encontrados viram atualização da spec/plano ou novas tarefas, conforme a origem do desvio;
7. repetir implementação → verificação até convergir ou atingir um stop condition;
8. não regenerar toda a cadeia para resolver uma clarificação localizada quando editar o artefato existente preserva melhor o histórico.

Uma constituição ou conjunto de princípios do projeto pode funcionar como gate, mas não deve impor arquitetura genérica que contradiga necessidades reais.

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

Convergência spec-driven adaptada de https://github.com/github/spec-kit, sem exigir o CLI Specify, templates ou branches geradas pela ferramenta.

Origem local: [to-spec.docx](../to-spec.docx).
