---
name: beautiful-web-article
description: "Transformar fontes fornecidas em artigos ou páginas editoriais HTML legíveis e fiéis ao conteúdo."
---

# beautiful-web-article

## Objetivo

Transformar materiais fornecidos pelo usuário em uma página/artigo HTML visualmente forte, legível, compartilhável e fiel ao conteúdo de origem.

## Quando usar

Transformar fontes fornecidas em artigos ou páginas editoriais HTML legíveis e fiéis ao conteúdo.

## Escopo

Usar quando o produto final for **artigo/página editorial**, não aplicação. Fontes possíveis incluem URL, PDF, DOCX, Markdown, texto, screenshots e notas.

## Workflow

1. **Source grounding:** extrair e organizar o conteúdo sem preencher lacunas silenciosamente.
2. **Editorial plan:** definir público, tipo de artigo, densidade de informação, outline, tema, layout e política de assets.
3. **Preservation:** registrar o que deve ser preservado e o que pode ser condensado.
4. **Visual direction:** decidir capa, largura, ritmo, tabelas, diagramas, code blocks e interações apenas quando ajudarem leitura ou entendimento.
5. **Build:** produzir HTML autocontido ou uma implementação web equivalente conforme o ambiente disponível.
6. **Review:** revisar em três eixos: editorial, visual e técnico.
7. **Repair:** corrigir problemas pontuais antes da entrega, evitando reconstrução desnecessária.

## Integração com o Arsenal

- Usar `writing-quality` para integridade editorial e estilo.
- Usar `web-design-engineer` quando a camada visual/interativa exigir mais engenharia de frontend.
- Para PDFs como fonte, seguir o fluxo oficial de PDF do ambiente em vez dos scripts específicos do repositório.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Para páginas web, usar o navegador controlável disponível e sua API documentada; separar inspeção de DOM, evidência visual e estado de aplicação. Controle de navegador não implica controle de aplicativos nativos ou dispositivos móveis. Não exigir reacticle, scaffolds ou equipes de agentes. Para PDF como fonte, usar a skill de PDF disponível; preservar fidelidade editorial e checkpoints apenas quando úteis.

## Referências

[GitHub · ConardLi/garden-skills · beautiful-article](https://github.com/ConardLi/garden-skills/tree/main/skills/beautiful-article)

Origem local: [beautiful-web-article.docx](../beautiful-web-article.docx).
