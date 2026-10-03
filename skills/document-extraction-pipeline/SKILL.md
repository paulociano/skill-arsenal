---
name: document-extraction-pipeline
description: "Converter documentos complexos em conteúdo estruturado, usando extração textual primeiro e OCR seletivo quando necessário."
---

# document-extraction-pipeline

## Objetivo

Converter documentos complexos em Markdown/JSON/chunks/HTML com estratégia adaptativa entre text layer, layout analysis, OCR e correção assistida por LLM, preservando estrutura e evidência.

## Quando usar

- PDF complexo;
- scans/imagens;
- documentos com tabelas, fórmulas, múltiplas colunas ou forms;
- PPTX/DOCX/XLSX/EPUB/HTML para ingestion;
- criação de corpus RAG;
- preparação de fonte para `source-to-skill`.

## Princípio central

**Usar a menor camada de percepção necessária para cada página/bloco.**

Não aplicar OCR/VLM pesado a tudo quando text layer confiável já resolve.

## Workflow

1. **Inventory** — formato, páginas, idiomas, presença de scan, tabelas, math e imagens.
2. **Fast path** — extrair text layer/layout simples primeiro quando confiável.
3. **Quality detection** — detectar blocos/páginas vazios, garbled ou estruturalmente suspeitos.
4. **Selective repair** — aplicar OCR/VLM apenas onde a evidência indicar necessidade.
5. **Full-page OCR** — reservar para scans ou páginas majoritariamente ruins.
6. **Structure reconstruction** — preservar headings, tables, equations, links, references, code e reading order.
7. **Output choice**:
   - Markdown para leitura/edição;
   - JSON para estrutura/blocos;
   - chunks para retrieval;
   - HTML quando fidelidade estrutural ajudar.
8. **Semantic validation** — quando o documento representa um domínio com invariantes verificáveis, validar o output tipado contra essas regras (por exemplo totais, saldos, datas, contagens ou relações entre campos). Schema válido não prova conteúdo correto.
9. **Visual/source verification** — revisar amostra representativa e páginas difíceis contra a fonte.
10. **Batch strategy** — checkpoint, skip-existing e shard apenas quando o volume justificar.
11. **Downstream validation** — confirmar que o formato extraído atende ao uso final.

## Region-locked sequential OCR

Para viewers paginados onde o texto não é selecionável:
- calibrar a região uma vez e reutilizá-la página a página;
- capturar em fila serial para preservar ordem e evitar corrupção;
- manter thumbnail/crop de verificação por página;
- detectar páginas duplicadas para flag de drift ou fim do documento;
- auto-advance deve ter condição explícita de parada, timeout e page cap;
- preferir OCR local quando privacidade e volume justificarem;
- layout segmentation deve ser validado em páginas multi-coluna, pois confidence alta não garante reading order correto;
- exportar com separadores de página para preservar provenance mínima.

## Regras

- OCR não deve substituir text layer boa sem motivo;
- preservar page/block provenance quando retrieval ou auditoria exigirem;
- cabeçalhos/rodapés repetitivos podem ser removidos, mas não conteúdo legítimo;
- tabelas reconstruídas precisam de verificação de linhas/colunas e valores;
- fórmulas e inline math são zonas de alto risco;
- correção por LLM deve ser restrita ao material observado, sem adicionar fatos;
- output limpo não prova fidelidade ao documento;
- typed/structured output reduz ambiguidade, mas ainda precisa de invariantes de domínio quando houver propriedades calculáveis ou relações verificáveis.

## Router de formato e conversão leve

Antes de acionar OCR, layout pesado ou VLM:

- identificar se o formato já possui estrutura textual utilizável;
- para DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, ZIP e formatos semelhantes, preferir primeiro um conversor determinístico para Markdown/texto estruturado;
- tratar imagens embutidas, áudio e vídeo como capacidades adicionais, não como motivo para tornar todo o pipeline multimodal;
- manter plugins e converters opcionais desativados por padrão quando não forem necessários;
- serviços remotos de document intelligence/content understanding entram apenas quando o ganho esperado justifica custo, upload e boundary de dados;
- quando houver várias estratégias de conversão para o mesmo formato, escolher a menor que preserve o downstream contract.

A saída Markdown é uma representação intermediária útil, não prova de fidelidade. Estrutura perdida, tabelas achatadas e conteúdo visual ainda precisam de verificação contra a fonte.

## Representação intermediária e locators

Para documentos complexos, preferir uma representação intermediária que preserve mais do que texto corrido:

- página e reading order;
- tipo de bloco;
- hierarchy/parent-child quando disponível;
- tabela, fórmula, imagem, caption e code como tipos distintos;
- bbox/locator ou outro ponteiro estável quando downstream precisar citar/verificar;
- provenance até o arquivo/página/bloco original.

Markdown pode ser a saída final para leitura, mas JSON/árvore de blocos é melhor quando reconstrução, citation mapping, chunking ou reprocessamento seletivo importam. Ferramentas como Docling, MinerU e Unstructured reforçam esse padrão sem se tornarem dependências obrigatórias.

Ao fazer chunking para RAG, não quebrar automaticamente tabelas, fórmulas, listas ou seções apenas por tamanho. Chunk boundary deve respeitar estrutura antes de token budget quando isso preservar significado.

## Modos conceituais

- **No-OCR:** text-layer only.
- **Fast:** layout/text first, reparo seletivo.
- **Balanced:** percepção mais forte e OCR/layout robusto.
- **LLM-assisted:** correção estrutural adicional para casos difíceis.

Esses nomes representam estratégias; não exigem o runtime Marker.

## Licença e uso

A implementação Marker separa licença do código e licença de modelos/pesos. Antes de usar pesos/modelos em produção/comercialmente, verificar os termos atuais aplicáveis ao caso do usuário. Não assumir que Apache-2.0 do código cobre os pesos.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Usar as skills de PDF, documentos, planilhas e apresentações conforme o formato. Extrair texto primeiro; aplicar OCR somente em blocos que precisem. Antes de adotar Marker ou modelos externos, verificar runtime, versão e licença.

## Integração

Combina com `source-to-skill`, `kb-retriever`, `retrieval-quality-engineering` e `verify-before-claim`.

## Referências

Adaptada de datalab-to/marker.

Router de formatos e fast path de conversão adaptados de https://github.com/microsoft/markitdown, sem exigir MarkItDown, plugins, Azure Content Understanding ou Document Intelligence.

Representação layout-aware, reading order, block tree e locators refinados a partir de https://github.com/docling-project/docling, https://github.com/opendatalab/MinerU e https://github.com/Unstructured-IO/unstructured.

Validação de schema + invariantes semânticas refinada a partir de `PrettyPrinted/youtube_video_code` (2026-06-13, extração de PDF com Pydantic AI), preservando a ideia de checar relações como saldos/totais sem adotar Pydantic AI, Phoenix ou modelos específicos.

thiagotigaz/ocr-it acrescentou region-locked sequential OCR, duplicate/end detection, local OCR e verificação por thumbnail para viewers paginados. Nenhum browser extension/runtime é requisito.

Origem local: [document-extraction-pipeline.docx](../document-extraction-pipeline.docx).
