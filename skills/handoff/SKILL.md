---
name: handoff
description: "Preparar contexto compacto para continuar uma tarefa em outra sessão ou obter comparação independente ou crítica."
---

# handoff

## Objetivo

Criar um pacote compacto e pronto para colar para que outra IA, outro modelo ou um novo chat continue uma tarefa sem reler toda a conversa.

## Quando usar

- Continuar uma tarefa em novo chat.
- Transferir contexto para outra IA ou modelo.
- Pedir crítica ou segunda opinião.
- Fazer comparação independente sem contaminar a segunda resposta com a conclusão atual.
- Reduzir uma conversa muito longa para contexto essencial.

## Workflow

1. Escolher o modo de transferência.
2. Preencher o pacote com estado e fontes atuais.
3. Aplicar KEEP / SUMMARIZE / DROP / RETRIEVE.
4. Conferir se uma sessão sem contexto consegue retomar a próxima ação.

## Modos

1. **Continue** — transfere estado atual, decisões e próximos passos.
2. **Independent comparison** — transfere objetivo, restrições e fontes, mas omite a resposta/conclusões atuais.
3. **Critique / second opinion** — inclui o resultado atual e pede avaliação contra objetivo e evidências.
4. **Fresh context** — condensa uma conversa longa para retomada limpa.

## Conteúdo do pacote

- Objective
- Deliverable
- Current State
- Decisions and Constraints
- Sources and Files
- Remaining Work
- Continue From Here

## Regras

- Preservar formulações exatas quando forem materialmente importantes.
- Separar fatos confirmados de hipóteses.
- Não inventar contexto ausente.
- Indicar arquivos ou fontes que precisam ser reanexados quando o destinatário não tiver acesso.
- Remover filler, logs, discussões repetidas e passos concluídos sem relevância futura.
- Nunca incluir credenciais ou dados privados desnecessários.

## KEEP / SUMMARIZE / DROP / RETRIEVE

Ao condensar contexto longo, aplicar **KEEP / SUMMARIZE / DROP / RETRIEVE**:

- **KEEP:** objetivo, acceptance criteria, restrições, permissões, decisões, estado ativo, evidência fresca e blockers.
- **SUMMARIZE:** exploração concluída, tool output verboso e planos superseded, preservando decisões e locators.
- **DROP:** repetição, especulação stale e boilerplate reconstruível.
- **RETRIEVE:** manter apenas ponteiros para detalhes que só precisam ser carregados quando a próxima decisão exigir.

Um handoff bom deve permitir que um novo chat retome a tarefa sem perder restrições, decisões ou failure history.

## Retomada sem contexto implícito

Assumir que a sessão receptora começa com **zero contexto implícito**. Um handoff precisa carregar não só o que foi decidido, mas **por que**, especialmente quando não existe caminho de volta para perguntar à sessão anterior.

Aplicar progressive disclosure:

- manter sempre carregado apenas objetivo, constraints, active decisions e next action;
- carregar detalhes por pointers quando a próxima decisão exigir;
- contexto irrelevante não é neutro: compete com o sinal que importa.

Julgar o handoff perguntando: “uma sessão nova, sem memória do chat anterior, consegue continuar sem reabrir decisões já fechadas?”

## Referências

Documento avaliado: **The 7 ChatGPT Work Skills I Use Every Day — Copy-and-Paste Setup Prompts**.

Origem local: [handoff.docx](../handoff.docx).
