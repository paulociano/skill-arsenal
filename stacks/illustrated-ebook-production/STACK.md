---
name: illustrated-ebook-production
description: Produzir ebooks ilustrados, livros infantis, HQs educativas e guias visuais do briefing ao PDF/EPUB/HTML, coordenando pesquisa, arquitetura pedagógica, personagens, storyboard, geração visual, continuidade e QA factual/editorial.
---

# Illustrated Ebook Production

## Objetivo
Orquestrar uma linha editorial multimodal reutilizável sem concentrar pesquisa, escrita, ilustração, continuidade e exportação em uma skill monolítica.

## Skills candidatas
- explanation-architecture
- eli5
- plain-writing
- evidence-claim-verification
- educational-comic
- character-continuity
- high-fidelity-image-generation
- editable-visual-design
- typographic-composition
- visual-explanation-sketch
- verify-before-claim

Use somente as necessárias.

## Modos
- picture book: narrativa curta, forte dependência imagem-texto;
- educational comic: conhecimento convertido em sequência de painéis;
- illustrated guide: capítulos explicativos com diagramas/ilustrações;
- health/science guide: guia ilustrado com evidence gate elevado.

## Pipeline
1. Brief: público, idade quando relevante, objetivo, formato, extensão, idioma e canal de saída.
2. Evidence: pesquisar fatos necessários. Para saúde/ciência, fixar claims e fontes antes da adaptação.
3. Architecture: definir promessa pedagógica, sequência cognitiva e outline.
4. Manuscript pass: escrever o conteúdo completo primeiro, incluindo arco e personagens.
5. Visual-direction pass: somente com o manuscrito inteiro, criar mapa de páginas, motivos recorrentes e direção de arte.
6. Character system: quando houver recorrência, criar bíblia/atlas e estados narrativos.
7. Storyboard/page map: definir por página texto, função, visual, personagens, continuidade e assets.
8. Generate visuals: produzir ilustrações/painéis com referências adequadas.
9. Continuity QA: revisar personagens, props, cenário, paleta e mudanças de estado entre páginas.
10. Editorial assembly: compor texto controlável, imagens, legendas, balões, hierarquia e paginação.
11. Fact/safety QA: rever claims contra as fontes; saúde exige atenção a população, escopo, contraindicações e incerteza.
12. Render/export: usar a capacidade documental real disponível para PDF, EPUB ou HTML. Não prometer formato que o ambiente não consegue produzir.
13. Final inspection: páginas faltantes, cortes, overflow, legibilidade, resolução, ordem, créditos/fontes e coerência.

## Two-pass rule
Não gerar prompts de todas as páginas enquanto o manuscrito ainda está mudando materialmente. Primeiro estabilize texto/arco; depois gere direção visual com contexto global. Isso reduz contradições tardias e melhora motivos visuais e continuidade.

## Asset architecture sugerida
project/
- manuscript/
- characters/
- references/
- storyboard/
- prompts/
- illustrations/
- layout/
- sources/
- output/

É convenção, não requisito.

## Acceptance case: Césio-137 para crianças
A stack deve conseguir:
- pesquisar e fixar a sequência factual do acidente;
- adaptar linguagem à idade sem banalizar risco radiológico;
- separar falas ficcionais de citações históricas;
- manter personagens consistentes;
- evitar gore e exploração visual;
- explicar contaminação/radiação com recurso visual compreensível;
- produzir storyboard completo antes da geração em lote;
- verificar fatos novamente antes do artefato final.

## Limites
- consistência visual é controlada, não garantida;
- texto exato deve preferencialmente ser composto fora da imagem;
- geração de imagens não substitui verificação factual;
- guia de saúde não é diagnóstico ou plano terapêutico individual;
- runtime externo observado nas fontes não é herdado pelo Arsenal.

## Provenance
Stack consolidada a partir de padrões portáveis observados em GenielabsOpenSource/style-consistency-ai, kart-io/picture-skills, JimLiu/baoyu-skills, jmilinovich/comicgen e jakerains/StoryFox.
