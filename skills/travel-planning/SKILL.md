---
name: travel-planning
description: "Transformar uma ideia de viagem em plano verificável e pronto para reservar: roteiro por dia, deslocamentos, hospedagem, custos com fonte e data, documentos e checklist, sem reservar nem pagar nada."
---

# travel-planning

## Objetivo

Entregar um plano de viagem que a pessoa consegue reservar link por link, em que todo preço, horário e exigência tem fonte e data de consulta, ou a marcação explícita "conferir no link".

## Quando usar

- "Planeja uma viagem para…", "roteiro de X dias", "quanto custa ir para…", "o que preciso para viajar para…".
- Viagens a lazer, a trabalho (eventos, clientes) ou em família.

## Regras fixas

1. **Nunca reservar, pagar, segurar vaga ou inserir dados pessoais.** Entregar links e checklist; a pessoa reserva.
2. **Preço e horário vêm de consulta, nunca de memória.** Memória serve para geografia e "o que vale ver"; tudo que se reserva ou fecha é conferido. Sem dado: "—, conferir no link".
3. **Orçamento de pesquisa limitado.** Definir quantas buscas usar; esgotado o orçamento, entregar com os itens menos verificados sinalizados em vez de continuar procurando.
4. **Moeda da pessoa.** Converter para a moeda de origem dizendo a cotação, a fonte e a data uma vez; conferir se a fonte realmente devolveu a moeda pedida.
5. Responder no idioma do pedido.

## Workflow

1. **Briefing curto.** Origem, datas ou flexibilidade, número de pessoas e idades relevantes, orçamento, ritmo (corrido ou tranquilo), interesses, restrições (mobilidade, alimentação, pets), estilo de hospedagem.
2. **Exigências de entrada.** Passaporte e validade, visto ou autorização eletrônica, vacinas, seguro obrigatório, regras para menores. Fonte oficial (consulado, governo do destino, Itamaraty), com data.
3. **Feriados e eventos** nas datas: fechamentos, lotação, preços em alta.
4. **Rota e deslocamentos.** Ordem das cidades que minimiza volta; tempo real porta a porta; opções (voo, trem, ônibus, carro) com preço de referência e link.
5. **Hospedagem.** Bairro sugerido e por quê; 2–3 opções por faixa com preço, data da consulta e política de cancelamento.
6. **Roteiro por dia.** Manhã/tarde/noite com deslocamentos, horários de funcionamento conferidos, reserva antecipada necessária, plano B para chuva; não lotar o dia.
7. **Orçamento.** Tabela por categoria (transporte, hospedagem, alimentação, atrações, seguro, extras), faixa mínima–provável, itens não verificados destacados.
8. **Checklist de reservas** em ordem de urgência (o que esgota primeiro) e checklist de documentos e bagagem.

## Guardrails

- Não inventar horários, preços, regras de visto ou de saúde.
- Avisar quando a informação é volátil (passagem aérea, câmbio, regras de entrada).
- Dados do viajante (passaporte, cartão) nunca são pedidos nem guardados.

## Integração

`agenda-operations`, `personal-financial-planning`, `web-extraction-pipeline`.

## Origem

Adaptado de [skywain/trip-planner-skill](https://github.com/skywain/trip-planner-skill) (MIT: plano "verificado e reservável", nunca reservar, preço só de ferramenta, orçamento de buscas, câmbio com fonte e checagem da moeda retornada), avaliado em 2026-11-10. Scripts e APIs da fonte não importados. Garantia `static_only`.
