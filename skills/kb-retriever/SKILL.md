---
name: kb-retriever
description: "Responder perguntas em bases documentais grandes por busca progressiva, leitura localizada e citações rastreáveis."
---

# kb-retriever

## Objetivo

Responder perguntas a partir de uma base documental grande usando recuperação progressiva, navegação por estrutura e leitura localizada, evitando despejar arquivos inteiros no contexto.

## Quando usar

Responder perguntas em bases documentais grandes por busca progressiva, leitura localizada e citações rastreáveis.

## Workflow

1. Extrair tema, entidades, restrições de tempo/escopo e tipo de resposta desejada.
2. Identificar a fonte oficial: arquivos locais ou fonte remota acessível por conector indicado pelo usuário.
3. Navegar primeiro por índices, títulos, estrutura e resultados de busca para reduzir o espaço de procura.
4. Começar pelos arquivos mais prováveis e ler apenas os trechos necessários.
5. Refinar termos com sinônimos, siglas, nomes alternativos e termos de domínio quando a primeira busca for insuficiente.
6. Limitar exploração redundante; mudar de ramo quando uma fonte deixa de acrescentar evidência.
7. Responder com rastreabilidade e distinguir fatos encontrados de inferências.

## Regras por arquivo

- Para PDF: usar a skill de PDF disponível e analisar páginas relevantes; confirmar extratores instalados antes de executá-los.
- Para planilhas: usar a capacidade de spreadsheets adequada e ranges relevantes; não carregar a planilha inteira sem necessidade.
- Para docs/texto: preferir busca, find e leitura localizada.

## Ferramentas e dependências

Buscar arquivos locais com rg, índices e trechos; usar os conectores disponíveis para fontes remotas. Para PDF e planilhas, usar as skills correspondentes e leitura localizada. Não pressupor diretório knowledge/, Notion ou uma biblioteca remota acessível.

## Governança documental

- preservar a fonte original como evidência e separar fonte de interpretação;
- pesquisar identidade/título/URL antes de criar duplicatas;
- tratar similaridade semântica como sinal de revisão, não prova de equivalência;
- preferir store canônico + índices substituíveis;
- manter fatos, interpretações, contradições e unknowns distinguíveis;
- quando houver write-back, fazer read-after-write e verificar links/locators antes de afirmar sucesso.

## Versão e escopo de recuperação

Além de localizar conteúdo, perguntar:

- qual versão/status é válida?
- quem pode usar esta informação?
- qual agente/tarefa precisa dela?
- quanto contexto é suficiente?

Preferir loadouts específicos a um prompt global gigantesco. Para bases em camadas, começar por cenário/core para bootstrap e descer a atom/raw somente quando a decisão exigir precisão. Aplicar orçamento por número de itens, caracteres e tempo para impedir que memória engula o contexto.

## Economia de contexto

- buscar símbolo/termo antes de abrir arquivo inteiro;
- preferir trechos/ranges e resumos de erro ao output bruto gigante;
- não reler conteúdo imutável já presente no contexto;
- para build/test/logs grandes, recuperar falhas e summaries primeiro;
- a dieta reduz transporte, nunca compreensão: ao editar/debugar, ler contexto suficiente para entender de fato.

## Referências

[GitHub · ConardLi/garden-skills · kb-retriever](https://github.com/ConardLi/garden-skills/tree/main/skills/kb-retriever)

Origem local: [kb-retriever.docx](../kb-retriever.docx).
