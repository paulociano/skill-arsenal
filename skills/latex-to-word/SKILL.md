---
name: latex-to-word
description: Planejar, executar e revisar conversões acadêmicas de LaTeX para Word preservando conteúdo científico, estilos, numeração, citações, referências cruzadas e semântica de objetos com validação proporcional ao risco.
---

# LaTeX to Word

## Objetivo
Converter um manuscrito LaTeX em um DOCX revisável e adequado ao destino, preservando significado científico e semântica de numeração antes de buscar aparência perfeita ou editabilidade máxima.

## Workflow
1. Inventarie o projeto LaTeX:
   - arquivos;
   - bibliografia;
   - classes/packages;
   - figuras;
   - tabelas;
   - equações;
   - labels/references;
   - macros;
   - conteúdo gerado.
2. Compile a fonte quando houver toolchain disponível. Se não houver, registre essa validação como pendente.
3. Inspecione requisitos do DOCX alvo:
   - template;
   - estilos;
   - numeração;
   - citações;
   - cross-references;
   - headers/footers;
   - figuras/tabelas;
   - regras editoriais.
4. Preserve os arquivos originais.
5. Comece pela menor abordagem confiável, normalmente Pandoc com reference DOCX quando disponível.
6. Faça um probe pequeno com conteúdo representativo antes da conversão completa.
7. Mapeie explicitamente a ponte semântica LaTeX -> Pandoc -> Word:
   - headings;
   - estilos;
   - equations;
   - captions;
   - numbering;
   - citations;
   - bookmarks/fields;
   - cross-references.
8. Adicione pós-processamento somente para necessidades observadas.
9. Verifique objetos de alto risco:
   - equações;
   - tabelas complexas;
   - figuras;
   - footnotes;
   - citations;
   - cross-references;
   - numbering;
   - chemical formulae e units.
10. Diferencie texto visualmente correto de semântica Word realmente dinâmica.
11. Quando Word desktop ou Zotero forem necessários e não houver controle real disponível, entregue passos exatos para o usuário executar e reaudite o arquivo retornado.
12. Faça validação estrutural do DOCX e, quando possível, validação no Word real.

## Prioridades
1. conteúdo científico correto;
2. numeração e referências corretas;
3. citações corretas;
4. estrutura e estilos;
5. editabilidade;
6. fidelidade visual fina.

## Guardrails
- Um reference DOCX não cria sozinho semântica que o conversor não emite.
- Texto de citação visível não prova campo vivo de citação.
- Texto de referência cruzada visível não prova cross-reference nativa.
- LibreOffice ou inspeção OpenXML não substituem Word desktop para comportamento específico de campos Word.
- Não generalize workaround de um manuscrito para todos os projetos.

## Relação com outras skills
Use `document-extraction-pipeline` para inspeção de conteúdo, `academic-paper-orchestration` para integridade do manuscrito e capacidades DOCX disponíveis para edição e QA do artefato.

## Origem adaptada
Metodologia inspirada em `hajimi-kun/latex-to-word-workflow`, mantendo execução capability-neutral e removendo dependência obrigatória de scripts locais.
