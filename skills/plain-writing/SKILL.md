---
name: plain-writing
description: Escrever ou revisar prosa para máxima clareza usando palavras comuns, estrutura lógica, terminologia consistente, contexto suficiente e remoção de jargão, puffery e formulações artificiais.
---

# Plain Writing

## Objetivo
Produzir texto claro na primeira leitura, com linguagem simples, concreta e informativa.

## Quando usar
Use quando o usuário pedir para:
- simplificar, limpar, enxugar ou esclarecer texto;
- escrever relatórios, READMEs, mensagens, documentos ou explicações diretas;
- remover jargão, "AI slop", exagero ou abstração desnecessária.

Não aplique mecanicamente quando o usuário pedir uma voz literária, publicitária, acadêmica específica ou outro estilo deliberadamente não neutro.

## Regras
1. Prefira palavras comuns quando elas forem igualmente precisas.
2. Preserve termos técnicos estabelecidos quando forem a opção mais exata; defina-os quando o público puder não conhecê-los.
3. Remova puffery, adjetivos vazios e ênfase sem evidência.
4. Use terminologia consistente para a mesma coisa.
5. Escreva frases completas e mantenha cada frase focada em poucas ideias relacionadas.
6. Organize parágrafos com uma ideia principal seguida de suporte.
7. Em sequências, apresente as etapas na ordem em que acontecem.
8. Dê contexto suficiente para um leitor inteligente que não acompanhou toda a conversa.
9. Prefira precisão concreta a abstrações evocativas.
10. Use listas quando melhorarem leitura, não como substituto automático de prosa.
11. Evite analogias e slogans quando o objetivo for documentação literal.
12. Evite atribuir intenção humana a sistemas quando isso confundir o agente real da ação.

## Passo de revisão
Antes de entregar:
- corte frases que repetem a mesma ideia;
- substitua jargão evitável;
- verifique se cada parágrafo tem um ponto claro;
- confira se o leitor sabe quem faz o quê;
- preserve fatos e nuances do original;
- mantenha o nível técnico necessário ao público.

## Relação com outras skills
Use `writing-quality` para revisão ampla de significado, evidência e voz; use `prose-lint` para auditoria de problemas de linguagem; use esta skill quando a prioridade específica for clareza literal e leitura fácil.

## Origem adaptada
Metodologia inspirada em `docwriter-org/plain-writing-skill`, flexibilizada para não impor preferências estilísticas absolutas fora de contexto.

## Linguagem controlada para interfaces entre agentes

Quando a saída for consumida por outro agente (descrição de ferramenta, instrução de handoff, procedimento, erro operacional), avaliar disciplina inspirada em ASD-STE100, sem afirmar certificação ou aderência ao léxico normativo:

1. Uma ação principal por frase; explicitar ator, condição, objeto, resultado e exceção.
2. Preferir voz ativa, termos estáveis, verbos concretos e tempos simples quando eliminarem ambiguidade.
3. Separar fatos, hipóteses, permissões e obrigações: `must`, `may`, `should` não são intercambiáveis.
4. Não trocar nomes de API, campos, strings de erro ou sintaxe literal para parecer simples.
5. Em instruções de alto risco, usar pré-condição, passos numerados, pós-condição verificável e comportamento de falha.
6. Aplicar modo estrito somente a procedimentos e tool specs; prosa editorial mantém flexibilidade e voz.
7. Revisar se o leitor automatizado sabe quem executa cada passo, sob que condição, e quando parar.

Fonte metodológica: https://github.com/danyuchn/asd-ste100-skill . A disciplina de clareza é adaptada; não reproduzir conteúdo controlado da especificação oficial nem apresentar os textos como certificados ASD-STE100.
