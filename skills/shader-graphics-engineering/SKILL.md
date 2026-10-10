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
   - Para galerias/carrosséis SDF, preferir uma passagem única quando isso simplificar composição e continuidade visual; manter dados de cards/projetos como fonte única para atlas, ordem e metadata quando o design depender dessa coerência.
   - Em cenas procedurais densas, usar seed determinística quando reproducibility importar e separar sistemas gráficos em contextos/iframes quando o isolamento de estado WebGL reduzir vazamentos ou conflitos.
8. Profile loops, samples, overdraw, DPR, resolution, branching e passes.
9. Optimize com bounds, early exits, LOD, lower-res passes e quality tiers quando fizer sentido.
10. Debug visually.
11. Testar context loss/restore e cleanup quando relevante.
12. Verify output no browser/runtime real.

## Large scientific point-cloud mode

Quando a cena representa centenas de milhares ou milhões de observações científicas ou espaciais:

1. **Data contract** — documentar fonte, filtros, unidades, coordinate transform e o significado de cada atributo antes da renderização.
2. **Preprocess once** — converter formatos científicos pesados para buffers compactos adequados ao browser/runtime; preservar um pipeline reproduzível e os metadados necessários para rastrear a transformação.
3. **GPU-first representation** — preferir buffers interleaved/typed arrays, instancing ou point primitives que possam ser enviados à GPU sem reconstruir objetos JS por observação.
4. **Visual encoding** — cor, tamanho, alpha e slicing precisam mapear atributos documentados; não usar estética que sugira precisão não presente no dado.
5. **Picking** — ajustar estratégia de seleção à densidade e à distância da câmera; um raio fixo costuma falhar em escalas muito diferentes.
6. **LOD / streaming gate** — quando o dataset inteiro não couber confortavelmente em memória/GPU, introduzir level of detail, chunking ou streaming em vez de simplesmente aumentar o limite.
7. **Scientific truth boundary** — separar visualização derivada dos dados de imagens ilustrativas ou geradas por IA. Representações imaginadas devem ser rotuladas como tais e nunca apresentadas como observações.
8. **Performance evidence** — medir FPS, memória/download e interação no hardware alvo; benchmark de uma máquina potente não vira budget universal.
9. **Provenance** — manter créditos, licença/política de dados e versão/release do dataset junto do artefato quando a fonte exigir.

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

Adaptada de MiniMax-AI/skills shader-dev e refinada com padrões portáveis de pmndrs/react-three-fiber, drei/postprocessing, oframe/ogl, curtainsjs e r3f-scroll-rig. Padrões de SDF carousel, fonte única de ordem/atlas e seed/isolation refinados a partir de Yousuf-developer/Viscose-carousel e MengTo/sylva. O modo de point cloud científico em grande escala foi refinado a partir de blendi-remade/desi-universe, preservando preprocessing rastreável, buffers GPU-first, slicing/picking, LOD gate e separação entre dados observados e artist impressions sem depender de DESI, Three.js ou fal.ai.

Origem local: shader-graphics-engineering.docx.


## Biblioteca WebGPU declarativa como alternativa

Quando o alvo for frontend com efeitos GPU reutilizáveis, considerar o padrão de `shader-effects-inc/shaders` como referência externa: canvas com camadas declarativas, geradores, pós-efeitos, máscaras e composição. Separar geração de imagem de transformação aplicada a camadas prévias; validar ordem, blend, custo de overdraw e fallback para WebGPU ausente. Conferir versão, API, framework, SSR, licença e suporte real antes de instalar dependências. Preservar HTML acessível para conteúdo e controles, respeitar reduced-motion, qualidade móvel e desligamento de efeitos não essenciais. Não exigir conta, editor, MCP ou CLI, nem assumir presets pagos. A biblioteca não substitui implementação GLSL/WebGL apropriada a projetos existentes. Fonte: https://github.com/shader-effects-inc/shaders/tree/main/skills/shaders.
