---
name: surgical-engineering
description: Executar mudanças de código com escopo mínimo, suposições explícitas, simplicidade, critérios verificáveis e zero refatoração lateral não solicitada.
---

# Surgical Engineering

## Objetivo
Reduzir erros de agentes de código mantendo cada mudança diretamente ligada ao pedido, simples o bastante para ser entendida e verificável por evidência.

## Quando usar
Use em implementação, correção, refatoração ou manutenção de código quando houver risco de:
- assumir requisitos silenciosamente;
- criar abstrações especulativas;
- mexer em código adjacente;
- declarar sucesso sem critério observável;
- transformar uma tarefa pequena em uma reforma ampla.

## Workflow
1. **Explicite as suposições relevantes.**
   - Se houver ambiguidade material, apresente interpretações possíveis.
   - Não invente requisito silenciosamente.
2. **Defina o menor resultado aceitável.**
   - Transforme o pedido em critérios verificáveis.
   - Para bugs, prefira uma reprodução antes da correção.
   - Para refactors, preserve comportamento antes e depois.
3. **Escolha a solução mais simples que atende ao contrato.**
   - Evite extensibilidade não pedida.
   - Evite abstrações de uso único sem ganho claro.
   - Não crie configuração "para o futuro" sem demanda atual.
4. **Mude apenas o necessário.**
   - Cada linha alterada deve ter ligação clara com o pedido.
   - Não reformate, renomeie ou "melhore" vizinhanças sem necessidade.
   - Remova apenas os órfãos criados pela própria mudança.
5. **Verifique.**
   - Rode checks proporcionais ao risco.
   - Confirme o critério de sucesso, não apenas ausência de erro.
6. **Feche com escopo honesto.**
   - Diga o que foi alterado.
   - Separe limitações reais de ideias futuras.
   - Mencione problemas adjacentes sem corrigi-los quando estiverem fora de escopo.

## Delete-list e dívida explícita

Para revisão de over-engineering:
- produzir uma **delete-list** concreta antes de propor novas abstrações;
- preferir remoção de código, configuração e wrappers sem uso real a "simplificação" que apenas troca uma abstração por outra;
- quando um shortcut consciente for adiado, registrá-lo como dívida explícita com motivo, impacto e condição de revisita;
- não reivindicar economia percentual de linhas, custo ou tempo sem baseline mensurado da mesma tarefa;
- separar métricas publicadas por terceiros de resultados do repositório atual.

## Heurísticas
- Se 200 linhas podem ser 50 sem perda de clareza, simplifique.
- Se uma abstração tem um único caller e nenhum seam real, questione se ela ajuda.
- Se uma alteração não pode ser relacionada ao pedido, ela provavelmente não pertence ao diff.
- Se o teste só cobre o exemplo observado, procure a propriedade geral que torna a correção válida.

## Relação com outras skills
Use `tdd` para red-green-refactor, `diagnosing-bugs` para investigação, `code-review` para revisão do diff e `agent-choice-audit` para decisões implícitas tomadas durante a implementação.

Delete-list, auditoria de over-engineering e ledger de shortcuts adaptados de https://github.com/DietrichGebert/ponytail, sem importar hooks, modos persistentes ou benchmarks como garantia.

## Origem adaptada
Metodologia inspirada em `multica-ai/andrej-karpathy-skills` e reforçada por padrões recorrentes de `affaan-m/ECC` e `ruvnet/ruflo`, removendo dependências de harness, hooks e runtimes específicos.
