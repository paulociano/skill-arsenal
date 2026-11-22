---
name: source-to-skill
description: "Converter fontes longas em skills de conhecimento com entrada compacta, referências sob demanda e fidelidade à origem."
---

# source-to-skill

## Objetivo

Transformar uma fonte longa ou coleção de fontes em uma skill de conhecimento reutilizável, estruturada para carregamento sob demanda em vez de contexto integral.

## Quando usar

Converter fontes longas em skills de conhecimento com entrada compacta, referências sob demanda e fidelidade à origem.

## Princípio

Extrair estrutura, não produzir um resumo gigante.

## Estrutura de saída

- arquivo principal pequeno com propósito, router, modelos centrais e índice;
- módulos ou capítulos carregados somente quando necessários;
- glossário;
- padrões e anti-padrões;
- cheatsheet ou decision tables quando fizer sentido.

## Modos

1. Analyze only.
2. Full conversion.
3. Generate from prior analysis.
4. Update / fold-in.

## Workflow

1. Confirmar que a fonte pode ser processada para o uso pretendido.
2. Ler a fonte real usando Files, Drive, PDF, Docs ou outra capacidade disponível.
3. Mapear capítulos, seções, termos, frameworks, técnicas e relações.
4. Preservar nomes, definições, ressalvas e terminologia da fonte.
5. Projetar uma hierarquia de carregamento sob demanda.
6. Deduplicar conceitos repetidos.
7. Manter provenance para seção, capítulo ou fonte original.
8. Testar perguntas representativas e verificar se o router encontra o módulo correto.
9. Em updates, alterar apenas conceitos e módulos afetados e registrar conflitos.
10. Fazer read-after-write antes de afirmar sucesso.

## Regras

- Não preencher lacunas com conhecimento externo sem rotular.
- Distinguir conteúdo da fonte, inferência estrutural e conhecimento externo.
- Para fontes conflitantes, preservar a divergência.
- Não usar para fontes curtas que já cabem confortavelmente no contexto.

## Copyright e privacidade

- uso pessoal ou interno não implica permissão para redistribuir;
- derivados de material protegido devem permanecer privados salvo licença ou permissão;
- fontes sensíveis permanecem na fonte autorizada e não devem ser enviadas a serviços externos sem necessidade.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Ler fontes pelas skills de documento apropriadas ou conectores disponíveis. Gerar pasta com SKILL.md e referências locais sob demanda, sem depender de diretórios ou ferramentas da fonte original.

## Ingestão de documentos complexos

Quando a fonte for scan, PDF com layout difícil, tabela, matemática ou multi-coluna, encadear primeiro `document-extraction-pipeline`. A conversão de uma fonte para skill depende da fidelidade da extração; texto limpo mas errado não deve virar conhecimento canônico.

## Curadoria em domínios regulados

Para domínios regulados ou high-stakes:

- definir whitelist/authority policy antes da coleta quando houver autoridades claras;
- preferir documento primário ao resumo/aggregator;
- distinguir **auto-fetched / needs-verification / human-verified**;
- metadata e recommendation claims não recebem status “verified” apenas porque o fetch funcionou;
- não inventar classe/nível/grade ausente;
- checar supersedence/version/ano;
- quando a fonte não puder ser acessada, deixar lacuna explícita em vez de completar por memória.

Verificação humana obrigatória deve continuar humana quando o domínio exigir sign-off profissional.

## Integração

Combina com kb-retriever, skill-builder, writing-quality e verify-before-claim.

## Formato nativo

Criar uma pasta com SKILL.md iniciado por frontmatter YAML `name` e `description`; usar referências Markdown locais para módulos extensos e validar as rotas.

## Referências

Adaptada de virgiliojr94/book-to-skill.

Origem local: [source-to-skill.docx](../source-to-skill.docx).

## Material de estudo derivado com cobertura e auditoria de fonte (Skill-Anything, 2026-11-21)

Quando uma fonte longa também precisar virar guia de estudo, quiz, exercícios ou flashcards, preservar a distinção entre **skill de conhecimento** e **study pack**:

1. Segmentar por capítulos/seções reais e construir um índice de cobertura antes de gerar perguntas; para fontes extensas, processar blocos menores e consolidar síntese global sem truncar silenciosamente o final.
2. Para cada cartão, questão e exercício factual, armazenar locator da seção e evidência local (trecho literal curto ou referência verificável). Checar o trecho contra a fonte; não inventar citações.
3. Distribuir itens por seções de acordo com objetivos de aprendizagem, importância e volume; não alegar “cobertura completa” se uma seção relevante não foi examinada.
4. Auditar duplicatas semânticas, gabaritos, alternativas, soluções, resposta impossível, confusão entre fonte e inferência e itens sem evidência; rejeitar ou sinalizar os itens não sustentados.
5. Exportar para Markdown, tabela TSV compatível com importação no Anki, HTML estático ou formato de skill **somente quando solicitado e realmente gerado**. A existência de um arquivo TSV não equivale a inserir cards no Anki.
6. Em material privado, evitar publicações automáticas, analytics, URLs remotas incorporadas e envio de conteúdo para modelos externos sem necessidade ou autorização. Verificar licença e redistribuição antes de compartilhar o pacote.

**Should-trigger:** “Transforme este livro em guia, 30 flashcards e quiz, mostrando a fonte de cada questão.”
**Near-miss:** “Resuma este parágrafo”; não exigir pipeline nem exportação múltipla.

**Proveniência:** [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything), especialmente sua abordagem de segmentação, cobertura, verificação de citações e auditoria; também [PaoloJN/recap](https://github.com/PaoloJN/recap) para navegação de transcrições por momento/capítulo, quando houver timestamps verificáveis. Metodologia absorvida sem instalar CLI, extensões, modelos ou executores externos.
