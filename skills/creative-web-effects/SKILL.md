---
name: creative-web-effects
description: "Selecionar e integrar efeitos visuais contemporâneos para web como shaders, texturas, partículas, pós-processamento, WebGL e backgrounds procedurais sem sacrificar legibilidade ou performance."
---

# creative-web-effects

## Objetivo

Tratar efeitos criativos como camada de direção visual com orçamento explícito, e não como coleção de truques. Decide qual técnica serve ao conceito e encaminha implementação especializada quando necessário.

## Quando usar

- hero/background visual expressivo;
- distortion, refraction, noise, grain, dithering, particles;
- image transitions e WebGL galleries;
- bloom, depth of field, chromatic effects e postprocessing;
- interfaces que pedem atmosfera/texture além de CSS convencional.

## Famílias de efeito

- **texture** — noise, grain, dithering, halftone, ASCII;
- **light** — glow, bloom, beams, gradients vivos;
- **space** — particles, depth, parallax, 3D fields;
- **material** — glass/refraction/distortion/liquid;
- **image transition** — displacement, masks, shader wipes;
- **postprocessing** — color grade, vignette, DOF, aberration;
- **procedural background** — canvas/WebGL/SVG systems.

## Workflow

1. Começar pela visual thesis e definir a função do efeito.
2. Escolher 1 efeito assinatura dominante antes de empilhar efeitos.
3. Decidir o menor runtime:
   - CSS/SVG para composição simples;
   - Canvas para desenho procedural 2D;
   - shader-graphics-engineering para GLSL/WebGL;
   - Three/R3F quando cena, câmera, geometria e ecossistema 3D justificarem;
   - OGL/Curtains-like approach quando um WebGL enxuto ou DOM-to-plane resolver melhor.
4. Construir prova mínima sem polish.
5. Testar contraste/legibilidade sobre o efeito.
6. Definir quality tiers para mobile, low-power ou reduced motion quando necessário.
7. Lazy-load dependências grandes quando o efeito não é essencial à primeira pintura.
8. Medir CPU/GPU, memória, DPR e impacto em Core Web Vitals.
9. Verificar cleanup e perda/restauração de contexto quando aplicável.
10. Manter fallback estático coerente com a direção.

## Regras

- Efeito assinatura deve servir marca/narrativa, não apenas demonstrar tecnologia.
- Não empilhar bloom + particles + distortion + cursor + parallax por padrão.
- Evitar pós-processamento em UI textual quando reduz nitidez.
- Não usar WebGL para substituir HTML que precisa ser selecionável, indexável ou acessível.
- Bibliotecas de componentes/effects são repertório, não identidade pronta.
- Respeitar licença de shaders/assets/exemplos.

## Integração

design-direction, web-design-engineer, scroll-storytelling, shader-graphics-engineering, ui-motion-design e web-quality-audit.

## Origem metodológica

Adaptada de pmndrs/react-three-fiber, drei, postprocessing, oframe/ogl, curtainsjs, React Bits, Magic UI, tsParticles e exemplos de transição WebGL. Importa decisões e budgets, não uma stack obrigatória.
