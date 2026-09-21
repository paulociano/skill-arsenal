---
name: checkpoint-nao-iniciados
description: Lista clientes ainda “Não iniciados” em um período definido pelo usuário, agrupando por mês e por líder direto ou responsável do consultor, com saída pronta para WhatsApp.
---

# Checkpoint Não Iniciados

## Objetivo

Transformar a planilha de Check Point em uma cobrança operacional rápida dos clientes cuja AP ainda está com status **Não iniciado**, dentro de um período variável definido em cada execução.

## Quando usar

Use quando o usuário pedir levantamento de clientes não iniciados, backlog de APs ou acompanhamento semelhante por período, especialmente em comandos como:

- `arsenal: checkpoint não iniciados de agosto até hoje`
- `arsenal: liste os não iniciados de 01/07 a 31/08`
- `arsenal: checkpoint dos últimos 30 dias`

Não execute por recorrência automática. A stack é **sob demanda**.

## Entrada obrigatória

Definir o **período da pesquisa** em cada execução:

- data inicial + data final;
- mês inicial + “até hoje”;
- intervalo relativo inequívoco, como “últimos 30 dias”.

Se o período não estiver informado e não puder ser inferido com segurança da mensagem atual, pedir apenas o período. Não assumir junho, mês corrente ou qualquer outra janela fixa.

## Fonte

Usar a planilha de Check Point indicada pelo usuário ou a versão conectada/autorizada correspondente.

Preferir dados atuais da fonte quando o usuário pedir “hoje”, “atual”, “agora” ou equivalente.

## Campos mínimos

Localizar na base, mesmo que a posição das colunas mude:

- Cliente
- Consultor
- Líder
- Responsável
- Mês/Data da AP
- Status

## Workflow

1. Resolver o período solicitado em datas ou meses concretos.
2. Ler a base atual da planilha.
3. Filtrar somente registros dentro do período.
4. Manter somente registros cujo status seja **Não iniciado**.
5. Para cada registro, extrair:
   - cliente;
   - consultor;
   - líder direto;
   - responsável, quando houver.
6. Definir o agrupador operacional:
   - se houver responsável nominal específico e ele representar a responsabilidade operacional do caso, usar esse responsável;
   - caso contrário, usar o líder direto do consultor;
   - nunca substituir silenciosamente um responsável nominal por outro nome.
7. Agrupar primeiro por **mês**.
8. Dentro de cada mês, agrupar por **líder/responsável operacional**.
9. Listar cada cliente com o respectivo consultor.
10. Conferir os totais por mês e o total geral contra os registros filtrados.
11. Entregar em formato de mensagem pronta para WhatsApp, salvo se o usuário pedir outro formato.

## Formato padrão de saída

A mensagem deve seguir esta hierarquia:

- abertura curta explicando o período;
- mês;
- líder/responsável;
- `Cliente — Consultor`;
- resumo por mês;
- total geral.

Exemplo estrutural:

```text
Pessoal, segue o acompanhamento das APs de [período] que ainda estão como Não iniciado:

📅 AGOSTO | 4 clientes

Líder / Responsável
• Cliente A — Consultor A
• Cliente B — Consultor B

📊 RESUMO
• Agosto: 4
Total: 4 clientes ainda não iniciados.
```

## Regras de qualidade

- Não carregar automaticamente o período de uma execução anterior.
- Não contar registros fora do período informado.
- Não misturar “Em andamento”, “Concluído” ou outros status com “Não iniciado”.
- Não deduplicar clientes diferentes apenas por nomes parecidos.
- Se o mesmo cliente aparecer em mais de uma AP válida no período, preservar os registros salvo regra explícita da base.
- Conferir se a soma dos grupos bate com o total filtrado antes de responder.
- Se houver divergência entre líder e responsável, preservar essa informação quando for relevante para a cobrança.
- Para “até hoje”, usar a data corrente da execução.

## Saída padrão

Português do Brasil, objetiva, operacional e pronta para copiar no WhatsApp.
