---
name: structured-output-contract
description: "Definir e validar schemas para saídas LLM consumidas por código, com tipos, incerteza explícita e retries limitados."
---

# structured-output-contract

## Objetivo

Projetar saídas de LLM com estrutura explícita, tipos e validação antes da geração, reduzindo parsing frágil, ambiguidade e retrabalho downstream.

## Princípio central

**Defina o contrato da saída antes de gerar.**

Quando a próxima etapa depende de dados estruturados, não pedir “JSON bonito” em texto livre e tentar consertar depois. Especificar a estrutura, os tipos válidos, enumerações, campos opcionais, fallbacks e critérios de validação de forma explícita.

## Quando usar

- classificação;
- extração estruturada;
- tickets, formulários e handoffs;
- tool inputs;
- pipelines multi-etapa;
- geração de objetos que serão consumidos por código;
- relatórios com schema previsível;
- qualquer fluxo em que uma saída inválida quebre o próximo passo.

## Workflow

1. **Define consumer** — quem ou o quê vai consumir a saída?
2. **Define schema** — campos, tipos, enums, listas, opcionalidade, cardinalidade e constraints.
3. **Define uncertainty** — como representar desconhecido, ausente, ambíguo ou não verificável.
4. **Constrain generation** — usar structured outputs/schema/tool calling/grammar nativos quando o runtime suportar.
5. **Validate** — rejeitar ou corrigir saídas que não obedecem ao contrato.
6. **Test edge cases** — dados incompletos, campos vazios, valores fora de enum, listas extensas e caracteres inesperados.
7. **Separate semantics from syntax** — estrutura válida não prova que o conteúdo está correto.
8. **Verify downstream** — confirmar que o consumidor real aceita o objeto gerado.

## Regras

- schema mínimo necessário é melhor que um objeto gigante “para o futuro”;
- usar enum/Literal quando o domínio é realmente fechado;
- usar optional/unknown quando a fonte pode não conter a resposta;
- não transformar ausência de evidência em valor default inventado;
- não usar regex ad hoc quando schema/tipo resolve de forma mais clara;
- constraints sintáticas não substituem avaliação semântica;
- structured output não é licença para omitir provenance, confidence ou caveats quando o domínio exige.

## Níveis de enforcement

1. **Prompt-only** — último recurso, sem garantia estrutural.
2. **Post-validation** — gera e valida depois.
3. **Provider structured output** — schema suportado pelo provider.
4. **Grammar/token-constrained generation** — quando o runtime realmente permite restringir tokens durante a geração.

Escolher o nível mais forte disponível que não complique desnecessariamente a arquitetura.

## Retries de transporte e validação

Quando a extração estruturada falhar:

- separar **transport retry** de **validation retry**;
- cada retry precisa de budget/stop condition;
- retornar ao modelo o erro de validação específico quando isso ajudar correção;
- não multiplicar limites de retry para afirmar quantidade real de requests: medir;
- se usage/latency não puder ser observado, manter como unknown;
- validation retry não substitui whole-operation deadline;
- usar token/cost budget quando loops de correção puderem ficar caros;
- streaming parcial não significa que o objeto final validou;
- schema-first continua simples: não transformar uma extração em um agent loop sem necessidade.

## Ferramentas e dependências

Usar schemas de ferramentas ou structured outputs quando suportados pela API real do projeto; caso contrário, gerar e validar o objeto com código disponível. Não presumir controle de tokens, Outlines ou Pydantic instalado.

## Integração

Combina com `to-spec`, `graph-engineering`, `experiment-design`, `runtime-ui-verification` e `verify-before-claim`.

## Referências

Adaptada de dottxt-ai/outlines.

Origem local: [structured-output-contract.docx](../structured-output-contract.docx).
