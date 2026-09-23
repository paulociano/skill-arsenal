---
name: shader-graphics-engineering
description: "Implementar, depurar ou otimizar shaders GLSL/WebGL e gráficos procedurais conforme efeito, runtime, integração DOM/3D e orçamento de desempenho."
---

# shader-graphics-engineering

## Objetivo

Projetar, implementar, depurar e otimizar shaders e gráficos procedurais em tempo real, escolhendo técnica e runtime adequados ao efeito e ao orçamento.

## Quando usar

- GLSL/WebGL/ShaderToy;
- SDF 2D/3D, ray marching, procedural noise;
- particles, fluid/smoke, terrain/ocean/clouds;
- lighting/shadows/AO/post-processing;
- WebGL image transitions, refraction e creative web effects;
- Three.js/R3F, OGL ou DOM-to-WebGL planes quando o projeto já usa ou justifica esse runtime.

## Princípio central

**Escolher técnica e runtime pelo efeito e pelo budget, não pelo prestígio da tecnologia.**

## Router conceitual

- formas 2D → SDF 2D;
- objetos matemáticos 3D → SDF 3D + ray marching;
- geometria/cena/asset 3D → Three.js/R3F quando o ecossistema ajuda;
- shader/enhancement pequeno → WebGL/OGL-like runtime enxuto quando suficiente;
- imagens/vídeos DOM com distortion → Curtains-like DOM-to-plane approach;
- materiais/iluminação → lighting model + normals + shadows/AO;
- organicidade → noise + domain warping;
- partículas/simulações → buffers/state;
- polish → anti-aliasing + tone mapping/post;
- erro visual → debug views de normals/depth/steps/material IDs.

## Workflow

1. Define target: plataforma, API, resolução, FPS e budget.
2. Choose runtime: CSS/SVG/Canvas/WebGL/Three/R3F conforme necessidade.
3. Choose technique: menor combinação suficiente.
4. Establish coordinate system: UV, câmera, espaços e transforms.
5. Build minimal visual antes de polish.
6. Add lighting/material/postprocessing de forma incremental.
7. Integrar com DOM/scroll apenas depois que o efeito funciona isoladamente.
8. Profile loops, samples, overdraw, DPR, resolution, branching e passes.
9. Optimize com bounds, early exits, LOD, lower-res passes e quality tiers quando fizer sentido.
10. Debug visually.
11. Testar context loss/restore e cleanup quando relevante.
12. Verify output no browser/runtime real.

## Creative web integration

- manter texto/controles em HTML sempre que possível;
- usar canvas compartilhado quando várias cenas pequenas puderem reutilizar contexto/recursos;
- sincronização DOM/WebGL deve evitar layout reads a cada frame quando observers/proxies resolvem;
- lazy-load runtime 3D pesado quando o efeito não é crítico à primeira pintura;
- pós-processamento deve respeitar legibilidade e não ser empilhado por padrão;
- mobile/low-power pode receber qualidade reduzida ou fallback estático.

## Regras

- não copiar budgets fixos de outra máquina;
- compilar não prova correção visual;
- usar gamma/tone mapping conscientemente;
- preservar reduced motion e fallback em UI crítica;
- efeito decorativo não pode destruir responsividade, bateria ou Core Web Vitals;
- não transformar biblioteca de efeitos em identidade visual pronta.

## Segurança

Shaders podem travar GPU/browser com loops/allocations excessivos. Usar limites defensivos e inspecionar código externo antes de executar.

## Ferramentas e dependências

Confirmar contexto WebGL/GPU e bibliotecas reais do projeto. Sem runtime gráfico, entregar código e estratégia de teste declarando ausência de medição.

## Integração

creative-web-effects, scroll-storytelling, web-design-engineer, procedural-3d-reconstruction, runtime-ui-verification e verify-before-claim.

## Referências

Adaptada de MiniMax-AI/skills shader-dev e refinada com padrões portáveis de pmndrs/react-three-fiber, drei/postprocessing, oframe/ogl, curtainsjs e r3f-scroll-rig.

Origem local: shader-graphics-engineering.docx.
