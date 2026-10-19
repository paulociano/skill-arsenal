---
name: obsidian-vault-authoring
description: Criar e revisar arquivos Obsidian Markdown, Bases, JSON Canvas e templates de vault com validação sintática, links e compatibilidade, sem presumir Obsidian CLI ou vault conectado.
---

# Obsidian Vault Authoring

## Quando usar
O usuário pede criação, edição, migração ou auditoria de arquivos `.md`, `.base` ou `.canvas` para um cofre Obsidian, incluindo propriedades, wikilinks, embeds, callouts e visões dinâmicas.

## Workflow
1. Confirmar formato pretendido, estrutura do cofre e versão/aplicação quando a sintaxe for sensível; quando não houver acesso ao vault, trabalhar com arquivos fornecidos sem presumir sincronização.
2. **Markdown Obsidian**: preservar frontmatter YAML, links `[[nota|alias]]`, embeds, anchors, callouts e convenções já existentes; links relativos são derivados da estrutura real, não inferidos.
3. **Bases (.base)**: declarar filtros globais/por view, fórmulas e views (table/cards/list/map conforme suporte), validar YAML, nomes e referências `formula.X`, tipos e escaping; expressões não são equivalentes a SQL nem a fórmulas do Sheets.
4. **JSON Canvas (.canvas)**: validar JSON, IDs únicos, tipos de nó, geometria, edges com endpoints existentes e groups; não inventar conversão para edição nativa no Obsidian quando não testada.
5. **Templates e exportações**: usar dados CSV/JSON para materializar documentos apenas com permissão e ferramentas reais; revisar caminhos de output, escaping e sobrescritas. O renderizador Knap é opcional, não requisito.
6. Verificar parse/estrutura automaticamente quando possível; registrar validação visual em Obsidian como pendente se não houver runtime ou CLI conectado.
7. Para cofre compartilhado, evitar duplicar fatos canônicos, preservar histórico/backup e nunca processar notas privadas em serviços externos desnecessários.

## Limites
Não presumir Obsidian instalado, CLI acessível, Defuddle/Knap presentes ou acesso ao vault local. Priorizar arquivos Markdown/YAML/JSON legíveis e portáveis; a sintaxe da fonte deve ser verificada nas referências atuais quando houver dúvida.

## Relação com Arsenal
Usar `agent-memory-engineering` para memória e provenance e `repository-evidence-docs` para documentação governada. Esta skill é especializada em formatos e não substitui um sistema de memória.

## Fontes
https://github.com/kepano/obsidian-skills (obsidian-markdown, obsidian-bases, json-canvas, obsidian-cli, defuddle, knap), consultada em 2026-10-19. Adaptação metodológica sem instalar plugins.
