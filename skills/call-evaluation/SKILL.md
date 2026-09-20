---
name: call-evaluation
description: "Avaliar ligações comerciais de consultoria financeira pelo Card de Ligação, com evidências, rubrica e qualidade do agendamento."
---

# call-evaluation

## Objetivo

Avaliar ligações de prospecção/agendamento de consultoria financeira usando como referência o framework do material “Card de Ligação”, identificando aderência ao processo, qualidade da comunicação, descoberta do cliente, construção de valor e força do agendamento.

## Quando usar

Use quando o usuário pedir para avaliar, revisar, dar feedback ou comparar uma ligação com o processo comercial do Card de Ligação.

Entradas aceitas:

- transcrição completa;
- áudio já transcrito;
- resumo detalhado da ligação, com menor confiança;
- ligação acompanhada de observações do gestor.

## Workflow

1. Identificar a fonte disponível e seus limites: transcrição, áudio ou resumo.
2. Ler [rubrica e fluxo](references/rubrica-e-fluxo.md) antes de pontuar.
3. Mapear trechos e timestamps às etapas e dimensões; distinguir ausência de evidência de etapa não realizada.
4. Calcular o total a partir das dimensões, justificar a avaliação e entregar o formato indicado em Saída padrão.

## Princípio

Avaliar o comportamento e o objetivo de cada etapa, não exigir reprodução literal do script. Linguagem natural é aceitável quando preserva a função da etapa.

## Objetivo central da ligação

Agendar uma reunião que realmente aconteça.

## Saída padrão

Entregar:

1. Resumo executivo em 3–6 linhas;
2. Nota total /100;
3. Quadro por dimensão com nota, evidência e impacto;
4. Etapas do fluxo: feita / parcial / ausente / não aplicável;
5. BIG POINT emocional identificado;
6. Melhor momento da ligação;
7. Principal oportunidade perdida;
8. 3 prioridades de melhoria;
9. Exemplos de como reformular trechos fracos, preservando linguagem natural;
10. Se houver agendamento: avaliar a força do compromisso de comparecimento.

## Evidências

Sempre justificar pontos relevantes com:

- timestamp, quando disponível;
- trecho curto da transcrição;
- comportamento observável.

Separar “não aconteceu” de “não aparece na transcrição”.

## Regras de feedback

- Ser específico e comportamental.
- Não chamar a pessoa de insegura, fraca, despreparada ou usar rótulos pessoais.
- Criticar a execução, não a pessoa.
- Destacar acertos antes das correções quando houver acertos reais.
- Priorizar poucas melhorias de alto impacto.
- Não transformar o feedback em cobrança de script decorado.
- Quando a conversa for natural e cumprir a função da etapa, considerar a etapa atendida.

## Limitações

- Se houver apenas resumo da ligação, declarar confiança reduzida.
- Sem áudio, não avaliar com segurança tom de voz, velocidade, pausas ou energia; só inferir quando a transcrição contiver pistas explícitas.
- Não inventar falas, respostas ou intenções do cliente.
- Não adicionar frameworks externos como SPIN Selling, Golden Circle ou outros, a menos que o usuário peça uma análise combinada.

## Integração

Quando o usuário pedir avaliação e devolutiva de gestão, aplicar esta skill e depois golden-circle-feedback. Não depender do stack call-feedback-stack, que não acompanha esta biblioteca.

## Referências

[rubrica-e-fluxo](references/rubrica-e-fluxo.md) — Ler antes de pontuar uma ligação; contém as 13 etapas, dimensões, pesos e faixas de nota.

Fonte citada pelo DOCX: Card de Ligação.pdf, 15 páginas.

O PDF Card de Ligação não foi fornecido nesta migração. O fluxo e a rubrica aqui registrados provêm do DOCX; a escala é derivada, não atribuída ao PDF. Solicitar a fonte apenas se a tarefa exigir conferência literal ou atualização do material.

Origem local: [call-evaluation.docx](../call-evaluation.docx).
