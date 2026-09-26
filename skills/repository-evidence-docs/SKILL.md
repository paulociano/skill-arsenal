---
name: repository-evidence-docs
description: Criar e manter documentação viva de repositórios a partir de comportamento real, conceitos, mapa de código, evidências e regras de sincronização, atualizando apenas o que ficaria enganoso após mudanças.
---

# Repository Evidence Docs

## Objetivo
Documentar um repositório para que uma pessoa entenda o que ele faz, como um comportamento real percorre o sistema, onde ficam as responsabilidades e quais evidências sustentam a explicação.

## Princípios
- Comportamento antes de inventário.
- Conceito antes de caminho de arquivo.
- Evidência antes de claim durável.
- Um fato durável deve ter um único lugar canônico.
- Atualize somente quando a documentação atual passaria a enganar.
- Valide a documentação antes de entregá-la.

## Workflow
1. Leia instruções do projeto, README, entrypoints, testes, configurações, schemas e documentação existente.
2. Escolha um comportamento real representativo, como request, job, fluxo de dados ou falha.
3. Trace esse comportamento da entrada ao resultado usando fonte, testes e artefatos.
4. Construa um mapa mínimo de responsabilidades no código.
5. Separe:
   - orientação;
   - walkthrough;
   - conceitos duráveis;
   - mapa de código;
   - glossário;
   - evidências;
   - histórico de mudanças da documentação.
6. Para cada claim importante, mantenha uma evidência verificável.
7. Em repositórios grandes, declare explicitamente o subsystem ou workflow coberto.
8. Antes de qualquer sync, pergunte: "o que um novo leitor entenderia errado se lesse a documentação atual?"
9. Faça a menor atualização que corrige esse modelo mental.
10. Verifique links, caminhos, source references, cobertura e coerência antes de concluir.

## Modos
- **Seed**: projeto novo ou ainda sem comportamento implementado. Marque fatos como confirmado, planejado ou desconhecido.
- **Build**: primeira documentação útil.
- **Sync**: ajuste cirúrgico após mudança de código ou descoberta estável.
- **Question refinement**: uma pergunta revela que a documentação ensinou o modelo errado.
- **Cleanup**: remoção explícita de documentação gerada.

## Guardrails
- Não gere um tour da árvore como substituto de explicação.
- Não copie o código em prosa.
- Não trate memória de chat como fonte superior ao repositório atual.
- Não edite docs por qualquer mudança trivial.
- Não registre estado local, workaround efêmero ou preferência pessoal como arquitetura durável sem pedido explícito.

## Relação com outras skills
Use `code-understanding-audit` para análise localizada, `legacy-system-reconstruction` para sistemas legados e `plain-writing` para clareza editorial.

## Origem adaptada
Metodologia inspirada em `YurunChen/repo-docs-skills`, removendo estrutura de diretórios obrigatória e scripts específicos, preservando o modelo behavior-first, evidence-first e sync cirúrgico.
