---
name: merge-conflict-resolution
description: Resolver conflitos de merge ou rebase por intenção e fonte primária, preservando comportamentos compatíveis, validando checks e concluindo a operação sem inventar mudanças novas.
---

# Merge Conflict Resolution

## Objetivo
Resolver conflitos Git preservando a intenção original de cada lado, em vez de escolher linhas mecanicamente.

## Workflow
1. Identifique o estado atual do merge ou rebase e todos os arquivos conflitantes.
2. Para cada conflito, recupere as fontes primárias relevantes: commits, PRs, issues, specs e testes.
3. Explique o propósito de cada lado antes de editar.
4. Preserve ambos os comportamentos quando forem compatíveis.
5. Quando forem incompatíveis, escolha a resolução que corresponde ao objetivo atual da integração e registre o trade-off.
6. Não introduza comportamento novo que não esteja sustentado por nenhuma das fontes.
7. Rode os checks do projeto, priorizando typecheck, testes e formatação conforme disponíveis.
8. Corrija apenas regressões causadas pela integração.
9. Conclua o merge ou rebase e verifique o estado final.

## Guardrails
- Não resolva por preferência estética quando houver intenção funcional documentada.
- Não use conflito como oportunidade para refatoração lateral.
- Não descarte silenciosamente alterações de um dos lados.
- Preserve rastreabilidade entre resolução e fonte original.

## Origem adaptada
Metodologia inspirada em `mattpocock/skills/resolving-merge-conflicts`, adaptada ao Skill Arsenal.
