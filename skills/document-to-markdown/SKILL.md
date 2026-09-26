---
name: document-to-markdown
description: Converter documentos de escritório, apresentações, planilhas, ebooks e PDFs em Markdown limpo usando extração local primeiro, tratando OCR como fallback explícito e proporcional ao conteúdo realmente ilegível.
---

# Document to Markdown

## Objetivo
Obter uma representação Markdown legível e consistente de documentos heterogêneos sem enviar conteúdo para serviços externos quando a extração local for suficiente.

## Quando usar
Use para converter:
- Word;
- PowerPoint;
- Excel;
- OpenDocument;
- RTF;
- EPUB;
- CSV;
- PDF textual.

Use OCR apenas quando o conteúdo relevante for imagem ou scan e não puder ser extraído de outra forma.

## Workflow
1. Identifique o formato real pelo conteúdo quando possível, não apenas pela extensão.
2. Prefira extração local ou bibliotecas nativas disponíveis.
3. Para documentos grandes, grave o Markdown em arquivo e leia somente os trechos necessários.
4. Preserve, quando possível:
   - headings;
   - listas;
   - tabelas;
   - links;
   - notas;
   - equations;
   - footnotes;
   - speaker notes.
5. Se a extração indicar páginas image-only ou scan:
   - marque a limitação;
   - use OCR seletivo quando houver ferramenta local;
   - use OCR hospedado apenas com autorização adequada e disclosure de que o conteúdo será enviado.
6. Verifique rapidamente se a saída preserva estrutura e conteúdo suficiente para a tarefa.
7. Se o objetivo for análise, use o Markdown como camada intermediária, não como substituto do arquivo original para elementos que dependem de layout.

## Guardrails
- Não enviar documento completo a OCR remoto por padrão.
- Não assumir que conversão preserva layout visual.
- Não tratar Markdown como prova de campos dinâmicos, fórmulas executáveis ou semântica específica de Office.
- Para planilhas, preserve tabelas e cabeçalhos antes de tentar "embelezar" a saída.

## Relação com outras skills
Complementa `document-extraction-pipeline`, que continua sendo a opção para extração mais complexa e OCR seletivo; esta skill é a rota rápida para normalização em Markdown.

## Origem adaptada
Metodologia inspirada em `firecrawl/anydoc`, sem assumir que o CLI ou o serviço Firecrawl estão instalados ou autorizados.
