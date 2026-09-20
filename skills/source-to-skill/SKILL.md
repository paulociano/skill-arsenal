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
