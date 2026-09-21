---
name: to-tickets
description: "Decompor specs e planos em tickets verticais pequenos, demonstráveis e com dependências e critérios de aceitação explícitos."
---

# to-tickets

## Objetivo

Quebrar uma spec, plano ou conversa em tickets verticais pequenos, verificáveis e com dependências explícitas.

## Quando usar

Decompor specs e planos em tickets verticais pequenos, demonstráveis e com dependências e critérios de aceitação explícitos.

## Workflow

1. Ler a spec e seus critérios de sucesso.
2. Identificar fatias verticais de comportamento.
3. Definir resultado e critérios de aceitação de cada ticket.
4. Ordenar dependências e explicitar bloqueios.
5. Verificar que cada ticket é demonstrável em uma sessão e que o conjunto cobre o escopo.

## Princípios

- Preferir tracer bullets verticais a divisões horizontais por camada.
- Cada ticket deve entregar algo verificável ou demonstrável.
- Cada ticket deve caber em uma sessão/contexto fresco.
- Declarar blocking edges explicitamente.
- Usar expand–contract para refactors amplos que não podem permanecer verdes em slices verticais simples.

## Refinamento de slices e execução

- marcar slices como human-review-required ou autonomous-capable apenas quando isso muda execução;
- cada slice deve cobrir caminho end-to-end relevante e ser demonstrável/verificável isoladamente;
- acceptance criteria devem incluir failure behavior quando aplicável;
- issues muito largas devem ser quebradas por comportamento, não simplesmente por camada;
- ao transformar issue em tarefas, usar outputs verificáveis, dependências e tipos como WRITE / TEST / MIGRATE / CONFIG / REVIEW quando ajudarem o executor;
- preferir testes junto da mudança, não um bloco gigante no fim.

## Consistência com spec e plano

Ao gerar ou atualizar tarefas:

- cada tarefa deve apontar para requisito, contrato, entidade ou decisão do plano que a originou;
- constraints do modelo de dados e contratos precisam chegar aos acceptance criteria relevantes;
- tarefas paralelas só devem ser marcadas quando não disputam o mesmo owner/artefato ou quando a estratégia de merge está clara;
- após execução, comparar tarefas concluídas com spec e plano, não apenas com checkboxes;
- gaps de convergência entram como novas tarefas pequenas, sem reabrir trabalho já validado;
- alteração material de requisito deve atualizar a spec antes de multiplicar tickets compensatórios.

## Referências

[GitHub · mattpocock/skills · to-tickets](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets)

Rastreabilidade spec → plan → tasks e convergence pass adaptadas de https://github.com/github/spec-kit.

Origem local: [to-tickets.docx](../to-tickets.docx).
