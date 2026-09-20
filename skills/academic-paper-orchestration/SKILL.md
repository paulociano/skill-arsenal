---
name: academic-paper-orchestration
description: "Estruturar e revisar manuscritos acadêmicos a partir de pesquisa real, verificando claims, resultados, figuras e citações."
---

# academic-paper-orchestration

## Objetivo

Transformar materiais reais de pesquisa em um manuscrito acadêmico estruturado, com outline, revisão de literatura, figuras, escrita, verificação de claims/citações e refinamento iterativo, sem inventar resultados ou referências.

## Quando usar

- escrever paper a partir de ideia + resultados/experimentos;
- estruturar submissão acadêmica;
- revisar Related Work;
- transformar experimental log em seções;
- preparar manuscrito para conference/journal;
- refinar paper com revisão simulada.

## Princípio central

**O paper deriva dos materiais de pesquisa; o modelo não preenche lacunas experimentais.**

## Inputs mínimos

- pergunta/ideia/contribuição;
- evidência experimental ou dados reais;
- venue/template/guidelines quando houver alvo de submissão;
- figuras existentes, quando houver;
- fontes/citações verificáveis.

Se evidência essencial estiver ausente, marcar gap em vez de inventar conteúdo.

## Workflow

1. **Pre-flight** — inventariar inputs, venue, deadline, limites de página e claims pretendidos.
2. **Evidence map** — ligar cada claim central a experimento, dado, figura ou fonte.
3. **Outline** — produzir estrutura com objetivo de cada seção, figuras previstas e necessidades de literatura.
4. **Literature review** — descobrir candidatos, verificar identidade/metadata/data de publicação e construir pool de citações permitido.
5. **Figures** — em paralelo quando possível, produzir/planejar figuras a partir do evidence map.
6. **Reconcile** — ajustar outline ao que a literatura realmente sustenta.
7. **Draft** — escrever seções preservando dados/claims e guidelines.
8. **Integrity gates**:
   - citation existence;
   - claim-evidence alignment;
   - numeric provenance;
   - venue/style constraints;
   - LaTeX/document sanity quando aplicável.
9. **Refinement** — revisão simulada → revisão direcionada → reavaliação.
10. **Accept/revert** — manter snapshot anterior se nova iteração piorar ou introduzir claim sem suporte.
11. **Halt** — parar por limite de iterações, ausência de novos findings materiais ou plateau.
12. **Final provenance** — registrar fontes, datasets/inputs, figures e versão final.

## Literature discipline

- busca encontra candidatos; não prova que a referência existe;
- verificar título/autores/ano/venue em fonte bibliográfica confiável;
- não citar paper apenas por snippet;
- não usar referência posterior ao cutoff da venue se o trabalho exigir cutoff histórico;
- Related Work precisa representar diferenças reais, não criar strawman;
- citações verificadas formam um pool permitido para a escrita.

## Claim discipline

- número no paper precisa apontar para dado/experimento/fonte;
- ablation/result não existe se não estiver nos dados;
- novelty claim exige comparação sustentada;
- causalidade não nasce de correlação;
- reviewer simulated score é ferramenta de iteração, não garantia de aceitação.

## Refinement

Usar:

- revisão por eixos;
- devil’s-advocate para claims centrais quando útil;
- memória de findings resolvidos para evitar repetir crítica;
- snapshot antes de cada mudança;
- revert real quando a revisão piorar;
- limite de iteração para impedir polish infinito.

## Integridade acadêmica

- preservar autoria e responsabilidade humanas;
- não fabricar experimento, participante, métrica, baseline, citação ou aprovação ética;
- explicitar assistência de IA quando a política da instituição/venue exigir;
- não usar essa skill para esconder plágio ou inventar provenance.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Usar pesquisa web para verificar literatura e as ferramentas de documentos, apresentações e gráficos disponíveis. Scripts do projeto de origem e revisores externos não são pré-requisitos. Declarar gates de LaTeX/render que não puderem ser executados.

## Integração

- `discovery-research-synthesis`
- `publication-figure-engineering`
- `writing-quality`
- `structured-output-contract`
- `verify-before-claim`

## Referências

Adaptada metodologicamente de Ar9av/PaperOrchestra e do paper PaperOrchestra (Song et al., 2026).

Origem local: [academic-paper-orchestration.docx](../academic-paper-orchestration.docx).
