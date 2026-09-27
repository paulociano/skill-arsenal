---
name: response-latency-optimization
description: Reduzir tempo de resposta e latência percebida em workflows com LLMs por contexto progressivo, menos round-trips, paralelização segura, orçamento de ferramentas e medição de TTFT/tempo total. Usar quando velocidade de resposta ou excesso de etapas for um gargalo.
---

# Otimização de latência de resposta

## Objetivo

Diminuir o tempo até uma resposta útil e o tempo total da tarefa sem sacrificar correção, evidência necessária ou segurança.

## Procedimento

1. Definir o que está lento e medir, quando a superfície expuser dados: tempo até o primeiro resultado útil, tempo de ferramentas, número de round-trips, tempo total e retries. Não atribuir lentidão ao modelo sem evidência.
2. Mapear o caminho crítico. Separar operações dependentes das independentes e identificar esperas seriais evitáveis.
3. Aplicar contexto progressivo:
   - começar por índice, busca, metadados ou trechos;
   - abrir arquivos, páginas ou resultados completos somente quando necessários;
   - evitar recarregar contexto estável já disponível;
   - preservar prefixos úteis quando o runtime puder se beneficiar de cache, em vez de reescrever tudo apenas para reduzir tokens.
4. Reduzir round-trips:
   - agrupar consultas independentes na mesma chamada quando a ferramenta permitir;
   - executar operações independentes em paralelo;
   - não paralelizar etapas com dependência causal, writes conflitantes ou risco de ordem;
   - evitar ciclos de pesquisa sem nova hipótese ou ganho material.
5. Definir um orçamento proporcional de ferramentas antes de explorar: poucas chamadas para tarefas simples; ampliar somente quando evidência, risco ou ambiguidade exigirem.
6. Produzir valor cedo: quando houver resultado parcial confiável, apresentá-lo sem esperar investigação lateral que não altera a decisão.
7. Encerrar quando os critérios de aceite estiverem satisfeitos. Não adicionar skills, buscas, verificações ou explicações apenas porque estão disponíveis.
8. Comparar baseline e versão otimizada em tarefas equivalentes. Medir qualidade, retrabalho e latência total; reverter otimizações que aumentem erros ou retries.

## Heurística de execução

Preferir:

`router compacto → recurso mínimo → leituras localizadas → operações independentes em paralelo → síntese → resposta`

Evitar:

`contexto amplo → várias skills → leituras completas → chamadas seriais independentes → síntese tardia`

## Relação com outras skills

- `arsenal-router`: usar para selecionar o menor conjunto de recursos antes desta otimização.
- `codex-cost-efficiency`: usar quando o objetivo principal for tokens, quota ou custo no Codex. Pode coexistir, mas custo e latência são métricas diferentes.
- `graph-engineering`: usar quando dependências e joins forem complexos o bastante para exigir um grafo explícito.
- `llm-observability-evaluation`: usar quando for necessário instrumentar benchmarks reproduzíveis.
- `handoff`: usar quando histórico excessivo justificar continuidade em uma sessão compacta.

## Limites

- Uma skill não muda por si só o modelo, a infraestrutura, o scheduler, speculative decoding, KV cache ou parâmetros internos do ChatGPT.
- Não prometer redução percentual sem benchmark comparável.
- Menos tokens não implica necessariamente menor latência; cache, ferramentas, rede, retries e geração podem dominar o tempo total.
- Não remover verificação necessária em tarefas de alto risco apenas para responder mais rápido.
- Não instalar wrappers, proxies ou serviços externos de otimização sem revisão de segurança, privacidade e benefício mensurável.

## Fontes da adaptação

- [progressive-skill](https://github.com/freehul/progressive-skill): descoberta progressiva e redução do catálogo carregado.
- [ai-token-efficiency-playbook](https://github.com/ravinperera/ai-token-efficiency-playbook): higiene de contexto e leitura seletiva.
- [distil](https://github.com/dshakes/distil): compressão de contexto com atenção à estabilidade de prefixo e cache.
- [fannypack-agents](https://github.com/nikhilkulkarni1755/fannypack-agents): inspiração para batching, roteamento e paralelização; adaptar somente mecanismos disponíveis no runtime real.
