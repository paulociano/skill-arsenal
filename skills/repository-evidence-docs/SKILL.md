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

## Arquitetura documental por ownership

Quando a documentação crescer a ponto de repetir fatos ou misturar propósitos:

- classifique cada documento por função, por exemplo: how-to, reference, ADR, README/orientação, changelog/histórico;
- cada fato durável deve ter um único owner canônico; outras páginas apontam para ele em vez de recontar;
- decisões de design e justificativas pertencem a ADRs ou registros equivalentes, não a procedimentos operacionais;
- valores voláteis como versões, status de deploy, contagens e limites devem apontar para a fonte executável/configuração quando ela existir, em vez de serem copiados para páginas long-lived;
- links e pointers devem identificar arquivo, símbolo, seção ou fonte concreta quando possível;
- se dois documentos disputam ownership de um fato e a evidência não resolve, explicite a decisão humana necessária em vez de escolher por idade do arquivo ou ordem de descoberta;
- exceções documentais precisam de motivo, escopo e revisão posterior; não usar suppression sem explicar por que ela existe.

## Gates para regras automáticas de documentação

Quando criar lint/checks heurísticos para docs:

1. separar checks mecânicos de checks heurísticos;
2. não promover uma heurística a gate de CI apenas porque funciona em exemplos construídos;
3. avaliar cada regra separadamente em casos reais;
4. medir falsos positivos, não apenas exemplos em que a regra dispara corretamente;
5. manter preview/experimental fora de blocking CI até haver evidência suficiente;
6. mudanças de comportamento após observar o holdout exigem nova avaliação independente;
7. um fixer automático deve preservar identificadores, links, números e significado fora do trecho alterado;
8. parser/checker que falha parcialmente deve reportar incompletude, não sucesso silencioso.

## Guardrails
- Não gere um tour da árvore como substituto de explicação.
- Não copie o código em prosa.
- Não trate memória de chat como fonte superior ao repositório atual.
- Não edite docs por qualquer mudança trivial.
- Não registre estado local, workaround efêmero ou preferência pessoal como arquitetura durável sem pedido explícito.

## Relação com outras skills
Use `code-understanding-audit` para análise localizada, `legacy-system-reconstruction` para sistemas legados e `plain-writing` para clareza editorial.

## Origem adaptada
Metodologia inspirada em `YurunChen/repo-docs-skills`, removendo estrutura de diretórios obrigatória e scripts específicos, preservando o modelo behavior-first, evidence-first e sync cirúrgico. Ownership de fatos, separação por tipo documental e promoção empírica de regras foram refinados a partir de `scarletkc/seiso`, sem exigir seu binário, formato de configuração ou thresholds específicos.
