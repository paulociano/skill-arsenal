# Avaliação — Técnica do Soco de Café

- **Fonte:** https://institutoim.com.br/vendas/tecnica-do-soco-de-cafe/
- **Domínio:** comunicação, vendas, tratamento de objeções e fechamento
- **Data da avaliação:** 2026-09-30
- **Classificação:** A — Skill realmente útil
- **Decisão:** ADOTAR com adaptação
- **Owner criado:** `skills/sales-objection-handling/SKILL.md`

## O que a fonte faz

Apresenta um roteiro de cinco passos para o momento em que o cliente oferece resistência no fechamento: sorrir, concordar, desviar, canalizar e fechar. A sequência busca reduzir tensão antes de reconduzir a conversa à venda.

## Capability ledger

| Source fragment | Reusable capability | Keep | Remove/adapt | Owner | Proof |
| --- | --- | --- | --- | --- | --- |
| Sorria | reduzir confronto e sinalizar receptividade | sim | adaptar para texto/áudio, onde sorriso literal não existe | sales-objection-handling | cenário de objeção |
| Concorde | validar antes de responder | sim | não exigir concordância com afirmação falsa | sales-objection-handling | cenário de preço |
| Desvie | deslocar foco do atrito | sim | impedir evasão de informação material | sales-objection-handling | guardrail explícito |
| Canalize | construir ponte de volta à proposta | sim | exigir relação lógica com contexto | sales-objection-handling | padrão de resposta |
| Feche | pedir decisão/próximo passo | sim | tornar proporcional ao estágio e não coercitivo | sales-objection-handling | trigger tests |

## Comparação com o Arsenal

Não havia owner específico para tratamento de objeções comerciais. `call-evaluation` avalia ligações; `nonviolent-communication` estrutura conversas difíceis; `golden-circle-feedback` trata feedback comportamental. A nova skill ocupa um contrato diferente e estreito: resposta e treino de objeções no fluxo de venda.

## Valor incremental

A técnica muda o comportamento do modelo de uma resposta argumentativa imediata para uma sequência explícita de descompressão, validação, ponte e fechamento. É suficientemente pequena para ser aplicada de forma recorrente e suficientemente específica para não depender de um prompt longo a cada uso.

## Adaptações

- “Sorria” virou postura receptiva quando o canal não possui vídeo.
- “Concorde” foi limitado à parte legítima da preocupação, sem validar fatos falsos.
- “Desvie” não pode servir para omitir informação material.
- O fechamento deve ser proporcional ao estágio da venda.
- Foi incluído diagnóstico mínimo da objeção antes da resposta.
- Foram adicionados modos preparar, simular, revisar e criar playbook.
- Foram definidos limites para recusa clara e domínios regulados.

## Segurança

**Verdict: APPROVE.** A fonte é conteúdo textual e não exige scripts, instaladores, credenciais, rede adicional, persistência ou execução de código. O risco relevante é comportamental, especialmente pressão comercial ou evasão de objeções. A adaptação reduz esse risco com guardrails contra engano, ocultação de informação material e insistência após recusa clara.

## Dependências

Nenhuma dependência técnica obrigatória.

## Limites da validação

A fonte afirma aumento de eficácia comercial, mas a avaliação não encontrou, na própria página, experimento controlado ou dados quantitativos que permitam validar esse efeito. O Arsenal preserva o método como heurística operacional, não como garantia de conversão.

## Testes de trigger

**Should trigger:** objeção de preço, timing, confiança, comparação ou pedido explícito de simulação/revisão de objeções.

**Near-miss:** feedback de liderança, conflito interno, pesquisa de prospects e avaliação geral de ligação sem foco em objeções.
