---
name: decision-questionnaire
description: "Transformar uma decisão bloqueada por conhecimento de outra pessoa em um questionário objetivo, priorizado e pronto para resposta assíncrona ou reunião."
---

# Decision Questionnaire

## Objetivo

Converter uma lacuna de conhecimento externa em um questionário que extraia exatamente os fatos e decisões necessários da pessoa que os detém.

## Quando usar

Use quando:
- o usuário precisa decidir ou agir, mas outra pessoa possui parte crítica do contexto;
- uma entrevista completa seria exagero e um documento assíncrono resolve;
- o resultado esperado é um conjunto de respostas de um destinatário específico, não uma pesquisa pública.

Não use quando:
- os fatos podem ser encontrados diretamente em fontes disponíveis;
- o usuário já possui o conhecimento necessário e precisa apenas estruturar a própria decisão;
- o problema pede discovery amplo com vários stakeholders.

## Princípio

**Investigue o envio, não o assunto.**

O usuário nem sempre consegue responder o conteúdo que falta, mas normalmente consegue dizer:
1. quem sabe;
2. o que precisa receber de volta para seguir.

## Workflow

1. **Defina o destinatário**
   - papel, especialidade e relação com o usuário;
   - qual conhecimento essa pessoa possui que falta ao usuário.
   - Concluído quando o público e seu nível de contexto estiverem claros.

2. **Defina o retorno necessário**
   - decisões, fatos, restrições ou aprovações que precisam ser obtidos;
   - o que o usuário precisa conseguir fazer depois das respostas.
   - Concluído quando houver uma lista concreta de outputs esperados.

3. **Construa o gap**
   - para cada output necessário, identifique qual informação do destinatário fecha a lacuna;
   - não pergunte o que pode ser pesquisado diretamente pelo agente.

4. **Escreva as perguntas**
   - uma ideia por pergunta;
   - ordem de importância primeiro;
   - agrupe por tema quando houver mais de algumas perguntas;
   - adicione "por que isso importa" apenas quando evitar resposta superficial ou interpretação errada;
   - permita resposta parcial, incerteza e "não sei".

5. **Valide cobertura**
   - cada output esperado precisa estar coberto por pelo menos uma pergunta;
   - remova perguntas sem impacto sobre a decisão;
   - destaque dependências entre respostas quando existirem.

## Estrutura recomendada

- título;
- propósito e decisão dependente;
- destinatário e contexto mínimo;
- instruções de resposta;
- seções temáticas com perguntas;
- campo final para fatos importantes não perguntados.

## Critério de conclusão

O questionário está pronto quando:
- o destinatário consegue entender o contexto sem participar da conversa original;
- todas as lacunas necessárias para a decisão estão cobertas;
- nenhuma pergunta depende de informação que o próprio agente poderia obter diretamente;
- responder ao documento permite ao usuário tomar a próxima ação prevista.

## Provenance

Metodologia adaptada de `mattpocock/skills`, skill `to-questionnaire`, removendo convenções específicas de diretório e invocação de outros agentes.
