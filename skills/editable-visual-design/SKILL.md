---
name: editable-visual-design
description: "Criar pôsteres, infográficos, capas, banners e social cards editáveis com hierarquia, composição tipográfica, assets rastreáveis e revisão visual do render."
---

# editable-visual-design

## Objetivo

Criar peças visuais de canvas fixo com alto acabamento preservando editabilidade, exatidão textual, hierarquia e revisão do render.

## Quando usar

- pôsteres, campanhas, social cards, capas, menus, banners e infográficos;
- peças fixas que precisam continuar editáveis;
- reconstrução de referência em HTML, SVG ou estrutura equivalente;
- layouts com texto exato, números, preços, datas ou evidência.

## Princípios

1. Pixels finais não são a fonte de verdade.
2. Fato não é matéria criativa.
3. Referência define relações visuais, não pixels obrigatórios.
4. Asset architecture vem antes da geração.
5. Render é evidência.
6. Tipografia é parte da composição, não decoração final.
7. Sketch pode preceder o layout final quando ajuda a resolver narrativa/hierarquia.

## Workflow

1. Separar conteúdo factual obrigatório de decisões de design.
2. Definir modo de referência.
3. Se a peça explica um conceito, usar visual-explanation-sketch para resolver relações antes do acabamento.
4. Registrar canvas, hierarquia, regiões, paleta, escala tipográfica, alinhamentos e safe areas.
5. Usar typographic-composition para display type, line breaks, measure, tracking e hierarquia.
6. Escolher topologia: slot matrix, code-native field, continuous scene, cutout stack ou layered collage.
7. Construir texto como texto, shapes/layout como elementos editáveis e raster somente onde necessário.
8. Renderizar em tamanho real.
9. Inspecionar hierarquia, overflow, contraste, crop, alinhamento, line breaks, repetição e qualidade dos assets.
10. Corrigir findings observados e re-renderizar.
11. Entregar fonte editável + render final quando possível.

## Imagens geradas

Não pedir ao modelo lettering que precisa ser exato no artefato final. Quando texto deve ser preciso, mantê-lo como texto ou vetor controlado.

## Revisão

Separar factualidade, estrutura/editabilidade, composição tipográfica, qualidade visual, runtime/export, licença e proveniência.

## Integração

typographic-composition, visual-explanation-sketch, web-design-engineer, design-system-governance, publication-figure-engineering e verify-before-claim.

## Referências

Adaptada de yejy53/Editable-Design e owners tipográficos/visuais do Arsenal.

Origem local: editable-visual-design.docx.
