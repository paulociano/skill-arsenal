---
name: seo-research-audit
description: "Pesquisar palavras-chave ou auditar SEO e concorrentes com evidências reais, métricas disponíveis e prioridades acionáveis."
---

# seo-research-audit

## Objetivo

Executar pesquisa e auditoria SEO orientadas por evidência, priorizando fit de negócio, intenção de busca e uma ação concreta em vez de listas intermináveis de otimizações.

## Quando usar

Pesquisar palavras-chave ou auditar SEO e concorrentes com evidências reais, métricas disponíveis e prioridades acionáveis.

## Modos

1. **Keyword research** — descobrir e priorizar oportunidades.
2. **SEO audit** — diagnosticar domínio/páginas e definir uma prioridade.
3. **Competitive landscape** — mapear quem vence, em quais temas e por quê.
4. **SEO report** — converter evidências em relatório acionável e rastreável.

## Workflow

1. Definir negócio, objetivo, mercado, idioma/local e páginas importantes.
2. Reusar pesquisa recente quando ainda for válida; não recomprar/rebuscar a mesma informação sem motivo.
3. Usar dados first-party quando disponíveis, especialmente Search Console.
4. Separar:
   - métricas reportadas por ferramenta;
   - evidência observada na página/SERP;
   - interpretação/recomendação.
5. Não inventar volume, KD, CPC, posição ou backlinks. Ausente = `unknown`.
6. Verificar manualmente findings importantes na página/site real antes de reportar.
7. Priorizar ações por impacto plausível, intenção e capacidade real do site, não por volume isolado.
8. Fechar com **uma prioridade principal** e próximos passos ordenados.

## Keyword research

- começar por demanda first-party/near-ranking quando disponível;
- gerar sementes distintas;
- hidratar métricas somente de fonte confiável;
- remover duplicatas, termos off-intent e branded-only irrelevantes;
- priorizar product/page fit, intent, dificuldade plausível, volume e SERP fit;
- consultar SERP quando intenção for ambígua;
- salvar ou alterar estado em ferramenta externa somente dentro da autorização vigente; solicitar confirmação se a ação não estiver coberta.

## SEO audit

- crawl/audit técnico é evidência, não verdict;
- site quebrado/quase vazio precisa de investigação antes do relatório;
- verificar redirect/canonical/noindex/certificado e páginas reais quando relevante;
- não transformar nitpicks em prioridade;
- a ação principal deve ser executável nesta semana.

## Competitive landscape

- construir um conjunto representativo de queries;
- distinguir concorrentes diretos de publishers, marketplaces, comunidades e diretórios;
- comparar footprint, páginas, temas, backlinks e SERP features somente com dados disponíveis;
- oportunidades devem ser formuladas como gaps concretos, não "faça conteúdo melhor".

## Report

Um bom relatório deve conter:

- estado geral;
- uma prioridade;
- findings com **Status + Evidência + Fix**;
- tabelas/gráficos somente quando aceleram compreensão;
- caveats/unknowns;
- método: ferramentas usadas e o que foi verificado.

## Regras de comunicação

- linguagem calma e simples;
- glossar termos técnicos para público não especialista;
- não dramatizar ausência de dados como penalidade;
- não produzir vinte recomendações quando duas importam;
- fatos observados e estimativas de terceiros devem permanecer distinguíveis.

## Acessibilidade para agentes

Além do SEO clássico, auditar quando relevante a prontidão do site/docs para agentes:

- discoverability: robots.txt, llms.txt e entry docs;
- content structure: heading hierarchy, semantic HTML e exemplos de código;
- machine-readable/low-noise alternatives, especialmente Markdown/raw views;
- token economics: páginas excessivamente grandes podem ser descartadas ou mal aproveitadas;
- capability signaling: skill/agent docs, inputs, constraints e permissões;
- UX bridge: copy-for-AI/raw links quando ajudam humanos a transferir contexto.

Não tratar score AEO como garantia de ranking, citação ou preferência por agentes. É um audit heurístico de acessibilidade/consumo. Regras de crawler devem refletir a política real do site, não abrir bots automaticamente.

## Ferramentas e dependências

Se OpenSEO/DataForSEO/Search Console ou outro conector SEO não estiver disponível, usar web e evidência pública, mas deixar métricas proprietárias como `unknown`. Não inventar números para preencher tabelas.

## Referências

Adaptada de every-app/open-seo, especialmente keyword-research, seo-audit, competitive-landscape e seo-report.

Origem local: [seo-research-audit.docx](../seo-research-audit.docx).
