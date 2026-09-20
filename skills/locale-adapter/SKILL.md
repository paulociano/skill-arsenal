---
name: locale-adapter
description: "Localizar conteúdo e UX copy para outro idioma ou mercado preservando fatos, termos protegidos e comportamento do produto."
---

# locale-adapter

## Objetivo

Adaptar conteúdo e UX copy para outro locale preservando significado, fatos, comandos, URLs e comportamento de produto, sem produzir tradução literal.

## Quando usar

Localizar conteúdo e UX copy para outro idioma ou mercado preservando fatos, termos protegidos e comportamento do produto.

## Workflow

1. Definir fonte canônica, locale de origem e locale alvo.
2. Marcar conteúdo protegido: números, comandos, URLs, IDs, citações, termos definidos e comportamento do produto.
3. Extrair tese, hierarquia de informação e ações que precisam permanecer equivalentes.
4. Reescrever no locale alvo segundo ordem natural, registro, terminologia e ritmo daquele público.
5. Evitar copiar ordem de frases, sujeito explícito, metáforas ou pontuação do idioma de origem quando soarem artificiais.
6. Não adicionar fatos ou promessas inexistentes no original.
7. Verificar parity sem exigir correspondência frase-a-frase.
8. Para UI, checar overflow, labels, CTA, acessibilidade e termos consistentes na superfície real quando disponível.

## Regra de atualização

Quando a fonte canônica mudar materialmente, versões derivadas devem ser tratadas como potencialmente desatualizadas e revistas nos trechos afetados.

## Integração com o Arsenal

`writing-quality` cuida da qualidade editorial; `locale-adapter` cuida da equivalência entre mercados/idiomas.

## Referências

Adaptada de [oh-my-design · omd-locale-adapter](https://github.com/kwakseongjae/oh-my-design/tree/main/skills/omd-locale-adapter) e princípios úteis de `omd-humanize`.

Origem local: [locale-adapter.docx](../locale-adapter.docx).
