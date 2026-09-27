---
name: fast-response
description: Acelerar tarefas do Skill Arsenal selecionando o menor recurso útil e reduzindo contexto, round-trips e serialização desnecessária sem cortar validação essencial.
---

# Fast Response

## Objetivo

Aplicar um caminho curto e verificável para tarefas em que tempo de resposta é prioridade.

## Fluxo

1. Use `arsenal-router` para selecionar no máximo a menor skill ou stack principal que resolva a tarefa.
2. Aplique `response-latency-optimization` ao plano de execução.
3. Carregue apenas os arquivos apontados pelo router e somente os trechos necessários.
4. Agrupe e paralelize operações independentes quando as ferramentas reais permitirem.
5. Execute dependências em série somente quando a saída anterior for necessária.
6. Entregue resultado parcial confiável cedo quando isso for útil.
7. Pare ao cumprir os critérios de aceite; não faça exploração lateral automática.
8. Para benchmarks formais, acrescente `llm-observability-evaluation` somente quando solicitado ou quando a medição for parte do objetivo.

## Skills candidatas

- `arsenal-router`
- `response-latency-optimization`
- `llm-observability-evaluation` — opcional para benchmark reproduzível

## Regra de composição

Não adicionar `codex-cost-efficiency` por padrão. Incluí-la somente quando custo, tokens ou quota também forem objetivos explícitos.
