---
name: prose-lint
description: "Auditar prosa por clareza, redundância, ambiguidade, jargão, inconsistência e linguagem potencialmente excludente usando checks como sinais, não regras absolutas."
---

# prose-lint

## Objetivo

Executar uma revisão editorial sistemática e verificável sem confundir lint com reescrita automática. A skill encontra padrões suspeitos, explica por que podem prejudicar o leitor e propõe correções somente quando o contexto sustenta a mudança.

## Quando usar

- revisão final de textos;
- documentação, artigos, relatórios, e-mails ou páginas;
- style guide enforcement;
- textos muito longos para revisão apenas intuitiva;
- quando o usuário quer clareza, concisão ou consistência.

## Famílias de checks

- redundância e repetição;
- palavras vazias e vagueza;
- qualificadores/hedging excessivo;
- voz passiva quando obscurece agente/responsabilidade;
- frases longas ou estruturalmente pesadas;
- jargão não explicado;
- terminologia inconsistente;
- referências/pronomes ambíguos;
- nominalizações e abstrações desnecessárias;
- clichês e fórmulas;
- linguagem potencialmente excludente/condescendente;
- leitura difícil incompatível com o público;
- inconsistência de capitalização, headings ou formato quando houver style guide.

## Workflow

1. Definir público, meio, idioma e objetivo.
2. Ler o texto inteiro antes de sinalizar padrões locais.
3. Rodar checks conceituais por família.
4. Classificar findings:
   - **defect** — ambiguidade/erro/materialmente prejudicial;
   - **risk** — pode dificultar leitura no contexto;
   - **style choice** — preferência legítima do autor.
5. Para cada finding relevante, registrar trecho, motivo e correção sugerida.
6. Preservar significado, certeza, obrigação, escopo, causalidade e atribuição.
7. Aplicar correções apenas quando o usuário pediu revisão/rewrite; em audit, reportar sem substituir tudo.
8. Repassar o texto para detectar over-correction.

## Regras

- Passive voice não é automaticamente erro.
- Frase longa não é automaticamente ruim.
- Flesch/readability score é sinal, não verdade.
- Palavra marcada por um linter pode estar correta no domínio.
- Linguagem inclusiva exige contexto; não substituir termos definidos ou citações sem motivo.
- Não remover precisão técnica para obter "texto simples".
- Não impor regras do inglês ao português.
- Checks automatizáveis podem ser implementados por Vale, textlint, proselint, LanguageTool ou equivalentes quando já disponíveis, mas esta skill não exige instalação.

## Integração

writing-quality é o owner da escrita e reescrita; prose-lint é a camada de auditoria sistemática. Combina com voice-builder, locale-adapter e verify-before-claim.

## Origem metodológica

Adaptada de amperser/proselint, btford/write-good, get-alex/alex, textlint, retext, readability e LanguageTool. O Arsenal preserva a filosofia de checks configuráveis e contexto-sensitive, não listas universais de palavras proibidas.
