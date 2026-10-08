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
11. Antes de exportar, escolher o formato pelo uso final: raster fotográfico, gráfico/ilustração, documento digital, impressão, vetor/web ou animação; não usar o mesmo formato por hábito.
12. Quando a peça fizer parte de uma série ou campanha, preservar tokens de marca e componentes reutilizáveis em template/brand system quando o ambiente suportar isso, evitando drift entre variações.
13. Entregar fonte editável + render final quando possível.

## Contrato de editabilidade, reversibilidade e exportação

Quando o usuário precisa modificar ou reutilizar a peça, defina antes de produzir:
- **Fonte de verdade:** formato nativo editável, proprietário do arquivo e quais objetos precisam permanecer editáveis (texto, formas, camadas, vetores, posicionamento).
- **Operações seguras:** trabalhar em cópia/versionamento quando não houver undo confiável; não sobrescrever o original sem autorização; registrar transformação que não pode ser revertida.
- **Pipeline explícito:** fonte editável → alterações → render de prova → export no formato solicitado → inspeção do arquivo exportado. Um PNG de preview não substitui o arquivo-fonte.
- **Compatibilidade:** identificar fontes ausentes, flattening, efeitos não suportados e perda de layers/semântica. Não prometer round-trip fiel sem abrir e salvar novamente quando a ferramenta permitir.
- **Controle por agente:** quando houver CLI/API/MCP efetivamente conectados, preferir comandos com contratos de entrada/saída e efeitos verificáveis; exigir aprovação para alterações destrutivas. Uma ferramenta citada em README não é automaticamente executável neste ambiente.

### Critérios de aceitação observáveis

1. **Editabilidade:** reabrir o arquivo, alterar um texto ou objeto-alvo e salvar; confirmar a preservação dos demais elementos. Se impossível, declarar a limitação.
2. **Reversibilidade:** demonstrar undo, histórico ou restauração do original antes de aplicar alterações de alto impacto; caso contrário, editar uma cópia.
3. **Fidelidade visual:** comparar fonte e export no tamanho final: texto, fonte, cortes, transparência, geometria, cores e alinhamentos.
4. **Interoperabilidade:** quando solicitado, executar o ciclo abrir → modificar → salvar → reabrir, inclusive em formatos de troca, e registrar diferenças.
5. **Evidência:** separar verificações realmente executadas de inspeções parciais, claims do fornecedor e suposições; entregar fonte e export apenas se ambos existirem.

Aplique esses testes proporcionalmente ao artefato: uma imagem final sem exigência de editabilidade não requer motor de camadas; um pôster SVG editável não requer integração com aplicativo de desktop. Não instalar ferramentas externas sem necessidade, revisão de segurança e autorização.

## Imagens geradas

Não pedir ao modelo lettering que precisa ser exato no artefato final. Quando texto deve ser preciso, mantê-lo como texto ou vetor controlado.

## Revisão

Separar factualidade, estrutura/editabilidade, composição tipográfica, qualidade visual, runtime/export, licença e proveniência.

No QA visual, verificar também:
- consistência de spacing e alinhamento;
- contraste direcionando atenção para o elemento certo;
- espaço negativo suficiente para preservar hierarquia;
- excesso de elementos sem função;
- consistência entre peças da mesma série.

## Integração

typographic-composition, visual-explanation-sketch, web-design-engineer, design-system-governance, publication-figure-engineering e verify-before-claim.

## Referências

Adaptada de yejy53/Editable-Design e owners tipográficos/visuais do Arsenal.

Princípios de consistência de spacing, espaço negativo, contraste, templates/brand controls e seleção de formato de exportação refinados a partir de [Curious Refuge · 74 Canva Tips and Tricks for Better Designs](https://curiousrefuge.com/blog/canva-tips), tratados como heurísticas contextuais e não regras universais de design.

Metodologia de contratos editáveis, operações reversíveis, separação fonte/comandos/render e QA de round-trip refinada a partir da [avaliação do ecossistema Storytold / ArtCraft](../../evaluations/2026-10-08-storytold-artcraft-ecosystem.md). Não implica instalação ou disponibilidade dos apps Craft.

Origem local: editable-visual-design.docx.