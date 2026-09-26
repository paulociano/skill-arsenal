---
name: agent-choice-audit
description: Auditar decisões que um agente tomou por conta própria durante implementação, distinguindo o que veio da spec do que foi inventado, registrando impacto, confiança, reversibilidade e decisão corrigida quando necessário.
---

# Agent Choice Audit

## Objetivo
Revisar as escolhas introduzidas pelo agente onde a tarefa original era silenciosa. O foco não é o diff em si, mas as decisões de arquitetura, produto ou operação que agora passam a fazer parte do sistema.

## Quando usar
Use:
- antes de integrar uma implementação grande feita por agente;
- depois de trabalho delegado;
- quando "funciona" mas pode ter resolvido apenas o caso observado;
- quando o usuário quer saber o que foi decidido em seu nome.

## Workflow
1. Recupere a intenção original: prompt, spec, plano, ADRs e restrições.
2. Trace implementação, commits, diffs, relatórios e handoffs.
3. Liste apenas decisões que não estavam determinadas pelo pedido original.
4. Varra categorias como:
   - shape de dados;
   - storage;
   - API e erros;
   - dependências;
   - concorrência;
   - performance;
   - naming e escopo quando carregam impacto durável;
   - trade-offs futuros.
5. Para cada decisão, registre:
   - o que foi escolhido;
   - qual lacuna obrigou a escolha;
   - alcance futuro;
   - evidência;
   - reversibilidade;
   - confiança.
6. Classifique como:
   - **sound**;
   - **unsound**;
   - **needs-user**.
7. Para `unsound`, registre a decisão correta a partir da qual o trabalho deveria ser refeito.
8. Para `needs-user`, proponha uma opção provisória reversível sem fingir que a escolha foi autorizada.
9. Preserve decisões sound e load-bearing como contexto futuro para não serem rediscutidas acidentalmente.

## Regra central
"Passou nos testes" não prova que a decisão foi boa. Procure a propriedade geral que torna a escolha correta, não apenas o caso que ficou verde.

## Guardrails
- A auditoria não modifica o código por padrão.
- Não infira preferência do usuário quando a escolha for de produto ou gosto.
- Não esconda decisões importantes só porque a implementação ficou limpa.
- Um trabalho não trivial com zero escolhas implícitas merece rechecagem.

## Relação com outras skills
Complementa `code-review`, `decision-analysis`, `codebase-design` e `handoff`.

## Origem adaptada
Metodologia inspirada em `dzhng/skills/audit-choices`, simplificada para não depender de ledger, subagentes ou arquivos de spec específicos.
