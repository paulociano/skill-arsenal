---
name: cinematic-presentation
description: Criar apresentações de alta expressão como sequências de cenas, combinando narrativa, composição tipográfica, direção cinematográfica, mídia animada e QA, com fallback estático quando o formato não suportar motion.
---

# Cinematic Presentation

## Objetivo

Produzir apresentações em que layout, ritmo, câmera, vídeo e transições sirvam à narrativa sem sacrificar legibilidade, evidência ou editabilidade necessária.

## Skills candidatas

- design-direction
- typographic-composition
- cinematic-visual-direction
- presentation-template-adaptation
- motion-asset-engineering
- web-video-presentation
- publication-figure-engineering
- verify-before-claim

## Workflow

1. **Narrative** — definir audiência, tese, arco, duração e função de cada slide.
2. **Style discovery** — quando não houver template/brand obrigatório, derivar uma visual thesis do briefing, referências, conteúdo e audiência em vez de escolher um tema genérico. Materializar poucos tokens: famílias tipográficas, escala, grid, spacing, paleta, tratamento de imagem, charts e assinatura visual.
3. **Direction** — resolver regras de composição; preservar template/brand quando existir e deixar essa autoridade vencer style discovery.
4. **Scene map** — marcar quais slides são leitura estática, quais são beats sequenciais e quais justificam vídeo/motion.
5. **Shot design** — aplicar cinematic-visual-direction somente às cenas de alto valor.
6. **Composition** — usar typographic-composition para títulos, escala, line breaks, ritmo e relação texto/imagem.
7. **Media route** — escolher a tecnologia mínima:
   - slides nativos para conteúdo editável;
   - Slidev/reveal.js/web-video-presentation para apresentação web;
   - Remotion/Motion Canvas ou vídeo pronto para cenas pré-renderizadas quando houver runtime real;
   - Lottie/Rive/SVG quando motion vetorial for suficiente.
8. **Fallback** — cada cena animada relevante recebe frame estático/poster e comportamento reduced-motion quando aplicável.
9. **QA** — revisar narrativa, legibilidade, tempo de leitura/fala, continuidade, mídia ausente, overflow, contraste, consistência dos tokens e compatibilidade do formato final.
10. **Cut** — remover animações que competem com a mensagem ou não sobrevivem ao meio de apresentação.

## Regras

- Não animar todos os slides.
- Não usar transição diferente em cada página como demonstração de recursos.
- Não converter gráficos ou tabelas editáveis em vídeo quando precisam continuar sendo dados.
- Não depender de autoplay, áudio ou WebGL sem fallback.
- Quando o destino for PPTX/PDF, tratar motion externo como asset opcional e garantir que a versão estática continue completa.
- Não importar engines externas de apresentação quando a metodologia pode ser aplicada com as capacidades nativas disponíveis.

## Origem metodológica

Enriquecida com o princípio de style discovery do SlideSpeak/slide-design-skill: derivar linguagem visual do briefing e referências, preservando a metodologia sem depender do engine HTML ou da integração fal.ai da fonte.
