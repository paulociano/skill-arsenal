---
name: library-version-grounding
description: "Fundamentar decisões de programação na versão instalada de bibliotecas e na documentação oficial correspondente."
---

# library-version-grounding

## Objetivo

Garantir que tarefas de programação que dependem de bibliotecas sejam guiadas pela versão realmente instalada e pela documentação oficial correspondente, não apenas por memória de treinamento.

## Quando usar

Fundamentar decisões de programação na versão instalada de bibliotecas e na documentação oficial correspondente.

## Workflow

1. Identificar biblioteca/framework e versão efetivamente usada no projeto por manifest, lockfile, código ou metadata disponível.
2. Preferir documentação oficial e skills oficiais da própria biblioteca quando existirem e corresponderem à versão em uso.
3. Verificar mudanças recentes, APIs removidas/deprecadas e padrões recomendados atuais antes de sugerir implementação.
4. Distinguir claramente: comportamento confirmado para a versão instalada, documentação mais recente e conhecimento geral.
5. Não atualizar dependências silenciosamente só para encaixar uma solução conhecida.
6. Se a versão não puder ser determinada, declarar a incerteza e usar documentação atual apenas como referência, não como prova de compatibilidade.

## Ferramentas e dependências

Ler manifests, lockfiles e código locais pelo terminal; consultar documentação oficial pela web quando necessário. Não exigir CLI library-skills ou symlinks. Skills instaladas podem complementar a documentação da versão real.

## Referências

Adaptada de [tiangolo/library-skills](https://github.com/tiangolo/library-skills).

Origem local: [library-version-grounding.docx](../library-version-grounding.docx).
