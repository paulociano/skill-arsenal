---
name: sales-pipeline-diagnostics
description: "Diagnosticar a saúde de um funil comercial por etapa: volume, conversão, velocidade, tempo parado, cobertura e qualidade dos negócios, com previsão em faixas e sinalização explícita de qualidade dos dados, sem benchmarks inventados."
---

# Sales Pipeline Diagnostics

## Objetivo

Transformar dados de um funil comercial (CRM, planilha, export) em decisões: onde os negócios travam, o que está subindo ou caindo, quais precisam de intervenção e quanto se pode esperar fechar, sempre com incerteza explícita.

Origem metodológica: agente `sales-pipeline-analyst` de msitarzewski/agency-agents (MIT), adaptado. Foram removidos benchmarks genéricos tratados como regra (cobertura "3x", "probabilidade por etapa") e a dependência de MEDDPICC para vendas B2B enterprise.

## Quando usar

- revisar a saúde de um funil de etapas (por exemplo, C1 a C4 ou qualquer pipeline definido pelo usuário);
- explicar por que a conversão ou o fechamento mudou;
- identificar negócios parados e priorizar ação;
- montar uma previsão de fechamento do período.

Não usar para:
- limpar ou deduplicar cadastros: `crm-data-quality`;
- diagnóstico geral de métricas de produto: `product-metrics-diagnostics`;
- avaliar uma ligação específica: `call-evaluation`;
- projeções financeiras de cenários: `scenario-forecasting`.

## Entradas

Export com, no mínimo: identificador do negócio, etapa atual, datas de entrada em cada etapa (ou ao menos de criação e última atualização), responsável, origem, valor (se houver) e resultado (ganho, perdido, aberto). Se faltar campo essencial, declare o que deixa de ser calculável em vez de estimar.

## Workflow

1. **Dados primeiro.** Reporte tamanho da amostra, período, campos faltantes, etapas inconsistentes e registros sem atualização recente. Previsão feita sobre dado incompleto deve dizer isso no topo.
2. **Definir as etapas e a janela** com o usuário; calcular métricas por etapa, por origem e por responsável, nunca só a média geral (médias misturadas escondem o problema).
3. **Métricas centrais:**
   - volume que entra por período e por origem (sinal mais antecipado);
   - conversão etapa a etapa, em coortes por data de entrada;
   - tempo em cada etapa (mediana e dispersão) e tempo total até o resultado;
   - valor médio, quando houver valor;
   - velocidade do funil = (negócios qualificados × valor médio × taxa de ganho) ÷ duração do ciclo, como indicador composto e não como meta.
4. **Negócios parados:** marcar os que estão além de um múltiplo da mediana histórica da etapa (use a história do próprio funil para calibrar) ou sem atualização recente, e propor ação concreta por negócio ou retirada do funil.
5. **Cobertura:** relacionar o funil aberto com a meta restante do período, descontando por idade e atividade; calibrar com a taxa de conversão histórica própria, não com referência de mercado.
6. **Previsão em faixas:** apresentar faixa conservadora, provável e otimista, com as premissas de cada uma. Comparar com o método simples (probabilidade fixa por etapa) para mostrar a diferença.
7. **Separar indicador antecedente** (volume de entrada, atividade, agendamentos realizados) **de consequente** (fechamentos, ciclo), e agir nos antecedentes.
8. **Relatório:** resumo executivo, tabela por etapa, lista de intervenções, riscos e dados que faltam.

## Princípios de rigor

- Nunca apresentar um único número de previsão sem faixa e premissas.
- Correlação não é causa: alta taxa de ganho com poucos negócios pode ser seleção, não desempenho.
- Reportar achados ruins com a mesma precisão dos bons.
- Amostras pequenas: dizer que a conclusão é frágil em vez de calcular percentuais com falsa precisão.

## Limites

- Não inventar taxas, ciclos ou referências de mercado; se citar benchmark, informar a fonte e a data.
- Dados de clientes são pessoais: não expor nomes em relatórios compartilhados sem necessidade e respeitar a LGPD.
- Não alterar cadastros do CRM; propor mudanças e aguardar autorização.
