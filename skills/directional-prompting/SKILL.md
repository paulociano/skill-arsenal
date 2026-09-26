---
name: directional-prompting
description: Projetar ou revisar prompts, instruções e descrições de skills combinando resultado verificável, critérios de sucesso, condição de parada e linguagem positiva orientada à ação.
---

# Directional Prompting

## Objetivo
Escrever instruções que deixem explícitos o destino e o caminho: o que precisa ser produzido, como saber que terminou e quais ações concretas conduzem até lá.

## Estrutura
Para tarefas não triviais, prefira:
- **Goal**: resultado em uma frase;
- **Success criteria**: critérios observáveis;
- **Stop condition**: condição explícita de conclusão;
- **Constraints**: somente invariantes reais.

Depois, escreva o corpo com verbos positivos que descrevem o comportamento desejado.

## Regras
1. Comece pelo resultado, não por uma lista de proibições.
2. Faça critérios de sucesso verificáveis.
3. Defina quando parar em workflows iterativos.
4. Use verbos concretos: ler, verificar, comparar, gerar, testar, retornar.
5. Quando houver uma proibição, acrescente o comportamento positivo que a substitui.
6. Reserve linguagem absoluta para safety, contratos e limites realmente invariáveis.
7. Remova meta-comentário que não altera comportamento.
8. Não force forma positiva quando uma negação curta for mais precisa, especialmente em segurança, escopo proibido ou desambiguação entre caminhos semelhantes.

## Auditoria
Ao revisar uma instrução:
1. identifique objetivos vagos;
2. transforme qualidade subjetiva em critérios observáveis quando possível;
3. encontre regras negativas sem substituto positivo;
4. procure loops sem condição de parada;
5. remova redundâncias que repetem a mesma intenção;
6. confirme que a descrição da skill contém gatilhos reais, não documentação excessiva.

## Saída
Entregue a instrução revisada e, quando útil, resuma as mudanças de estrutura: goal, success, stop e ações direcionais.

## Origem adaptada
Metodologia inspirada em `kingbootoshi/directional-prompting`, com afirmações dependentes de modelos específicos removidas e foco mantido em princípios portáveis.
