---
name: legal-temporal-research
description: "Pesquisar texto legal e alterações por jurisdição e data de vigência, verificando cobertura histórica, correções, fonte oficial e diferença entre legislação e jurisprudência."
---

# Pesquisa jurídica temporal

## Quando usar

Para descobrir o texto de um dispositivo em uma data, comparar versões, rastrear atos modificadores ou verificar se uma decisão citou versão ainda vigente. Não usar para transformar toda tarefa de escrita em parecer jurídico; revisão contratual continua em contract-review, privacidade em privacy-program-governance.

## Entradas mínimas

Jurisdição e nível federativo, dispositivo ou tema identificável, data do fato/pergunta e tipo de fonte. Obter apenas a lacuna que muda a pesquisa; distinguir lei, regulamento e decisão judicial.

## Workflow

1. **Delimitar corpus.** Registrar jurisdição, tipo, cobertura, lacunas, início histórico, data até a qual está completo e última checagem. Catálogo que lista um país não prova acesso nem cobertura de suas leis.
2. **Classificar a história.** Separar texto vigente com versões, somente atual, reconstruído por emendas, texto original promulgado e somente metadados. Não reconstruir uma versão histórica a partir de corpus que não a sustenta.
3. **Fixar o tempo jurídico.** Distinguir edição/promulgação, publicação, entrada em vigor, revogação e data da decisão. Data do commit ou atualização da cópia não é vigência. Confirmar regras transitórias, retroatividade ou efeitos sobre casos pendentes nas fontes pertinentes, sem inferir só pela cronologia.
4. **Ler versão e mudanças.** Localizar dispositivo na data e atos que o alteraram. Verificar correções do corpus, renumerações, mudanças de caminho, revogações e restaurações; separar correção editorial da cópia de alteração legislativa. Diff e blame de Git são pistas de proveniência, não autoridade jurídica.
5. **Verificar origem oficial.** Abrir fonte do legislador/órgão competente e confirmar texto, identificador e locator. Link que mostra só texto atual não prova versão histórica. Quando faltar versão oficial histórica, declarar a lacuna e identificar reconstrução/arquivo como tal; nunca fabricar URL, inciso ou citação.
6. **Separar precedentes.** Identificar tribunal, caso, data, dispositivo e versão aplicada. Mudança posterior do texto é sinal para revisão, não prova automática de superação do precedente. Não confundir decisão judicial com lei nem ausência em um corpus com inexistência de precedente.
7. **Controlar resultados parciais.** Percorrer partes/cursores relevantes, registrar corpora não pesquisados, limites de tempo e truncamento. Resultado vazio em busca parcial não fundamenta inexistência jurídica.
8. **Entregar.** Informar jurisdição/data, texto ou síntese pertinente, mudança observada, fonte oficial com locator, proveniência da cópia e limites. Separar evidência textual de interpretação e de aplicabilidade ao caso; aconselhamento ou decisão jurídica material pede profissional competente.

## Ferramentas reais

Usar busca web e fontes oficiais atuais para afirmações jurídicas. Global Law é uma cópia técnica opcional que pode ajudar a localizar versões, nunca substituir a fonte oficial. Só usar seu MCP/CLI se efetivamente disponível e autorizado; caso contrário, pesquisar pelo navegador de pesquisa/conectores existentes sem inventar resultados. A versão hospedada envia consultas a terceiro; não inserir dados confidenciais de um caso sem autorização apropriada. Instalação de servidor, download de corpora e autoexecução de configs não fazem parte da leitura de um repositório.

## Verificação

- Should-trigger: “Qual era o texto deste artigo em 2022 e o que mudou depois?” → versão temporal e fonte oficial, com cobertura explícita.
- Near-miss: “Revise a clareza deste contrato” → não executar pesquisa histórica sem necessidade.
- Corpus só atual + pedido histórico → declarar falta de suporte, procurar fonte histórica.
- Busca parcial sem resultado → não declarar inexistência.
- Lei alterada após julgamento → não declarar precedente inválido por esse fato isolado.

## Proveniência

Metodologia adaptada de https://github.com/lexifina/global-law, README.md e MCP.md consultados em 2026-11-12, ref eb74b642424415b374fde37e9bc9f3791e4cdb01. Código do índice declarado CC0; corpora têm termos próprios. Sem copiar motor, instalar MCP ou validar corpus jurídico nesta avaliação. Verificação estática do contrato, sem benchmark ou execução.
