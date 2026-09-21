---
name: editable-visual-design
description: "Criar pôsteres, infográficos, capas, banners e social cards em canvas fixo com estrutura editável, assets rastreáveis e revisão visual do render."
---

# editable-visual-design

## Objetivo

Criar peças visuais de canvas fixo com acabamento alto sem achatar o trabalho inteiro em uma imagem única. Texto, geometria, camadas e assets devem permanecer editáveis sempre que isso agregar valor, além de existir um render final revisado.

## Quando usar

- pôsteres, campanhas, social cards, capas, menus, banners e infográficos;
- peças visuais fixas que precisam continuar editáveis;
- reconstrução de uma referência em HTML, SVG ou estrutura equivalente;
- layouts com texto exato, números, preços, datas ou evidência que não pode virar lettering gerado.

Não usar para websites responsivos, decks tradicionais, vídeo, logo isolado ou edição de footage.

## Princípios

1. Pixels finais não são a fonte de verdade.
2. Fato não é matéria criativa: datas, preços, nomes, números, avisos e claims vêm da fonte ou do usuário.
3. Referência define relações visuais, não pixels obrigatórios.
4. Asset architecture vem antes da geração.
5. Render é evidência: código válido não prova composição ou legibilidade.
6. Editabilidade tem custo: não fragmentar uma cena contínua sem necessidade.

## Workflow

1. Separar conteúdo factual obrigatório de decisões de design.
2. Definir modo de referência: off, art-directed ou reproduce.
3. Registrar canvas, hierarquia, regiões, paleta, escala tipográfica, alinhamentos e safe areas.
4. Escolher a topologia:
   - slot matrix;
   - code-native field;
   - continuous scene;
   - cutout stack;
   - layered collage.
5. Para conteúdo acadêmico ou factual, criar um evidence brief e preservar números, unidades, sinais e limitações.
6. Construir:
   - texto como texto;
   - shapes e layout importantes como elementos editáveis;
   - raster somente onde fotografia, ilustração ou materialidade pedirem.
7. Renderizar em tamanho real.
8. Inspecionar hierarquia, overflow, contraste, crop, alinhamento, repetição e qualidade dos assets.
9. Corrigir apenas findings observados e re-renderizar.
10. Entregar fonte editável + render final quando o formato permitir.

## Imagens geradas

Para séries com identidade consistente, edição por referência ou export de assets gerados, ler [referências e validação de imagens](references/imagens-consistentes.md). Aplicar somente quando houver raster necessário à peça.

- Não pedir ao modelo lettering que precisa ser exato no artefato final.
- Adequar cada prompt ao slot, crop, perspectiva e função visual.
- Usar transparência apenas quando a ferramenta realmente suportar alpha.
- Gerar assets independentes em paralelo somente quando não houver dependência visual.
- Preservar resultados bons de um batch e repetir apenas os que falharam.

## Revisão

Separar:
- factualidade;
- estrutura/editabilidade;
- qualidade visual;
- runtime/export;
- licença e proveniência.

## Ferramentas e dependências

Usar somente capacidades reais disponíveis no ambiente. Não exigir editor, scripts, Playwright ou assets do repositório de origem. Para geração ou edição de imagem, usar a ferramenta de imagem disponível. Detectar o runtime antes de prometer export ou render.

## Integração

Combina com web-design-engineer, design-system-governance, publication-figure-engineering, runtime-ui-verification e verify-before-claim.

## Referências

Adaptada de https://github.com/yejy53/Editable-Design, especialmente a skill editable-design, preservando fixed-canvas editability, asset architecture, evidence boundaries e render-review loop.

Princípios complementares de revisão versionada e export verificado consultados em https://github.com/bestagentkits/design-studio-ai.
