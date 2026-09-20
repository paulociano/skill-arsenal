---
name: shader-graphics-engineering
description: "Implementar, depurar ou otimizar shaders GLSL/WebGL e gráficos procedurais conforme efeito, runtime e orçamento de desempenho."
---

# shader-graphics-engineering

## Objetivo

Projetar, implementar, depurar e otimizar shaders e gráficos procedurais em tempo real, escolhendo técnicas de GLSL/WebGL adequadas ao efeito desejado e ao orçamento de performance.

## Quando usar

- GLSL/WebGL/ShaderToy;
- SDF 2D/3D;
- ray marching;
- procedural noise;
- particles;
- fluid/smoke;
- terrain/ocean/clouds;
- lighting/shadows/AO;
- post-processing;
- fractals;
- multipass buffers;
- debugging de shaders.

## Princípio central

**Escolher a técnica pelo efeito e pelo budget, não pelo quão impressionante ela parece.**

## Router conceitual

- formas 2D → SDF 2D;
- objetos 3D matemáticos → SDF 3D + ray marching;
- geometria analítica → ray intersections;
- materiais/iluminação → lighting model + normals + shadows/AO;
- natureza/organicidade → noise + domain warping;
- água/terreno/atmosfera → técnicas especializadas;
- partículas/simulações → buffers/state;
- polish → anti-aliasing + tone mapping/post;
- erro visual → debug views isolando normals/depth/steps/material IDs.

## Workflow

1. **Define target** — plataforma, API, resolução, FPS e orçamento.
2. **Choose technique** — selecionar a menor combinação suficiente.
3. **Establish coordinate system** — UV, câmera, espaço e transforms.
4. **Build minimal visual** — provar geometria/efeito antes de polish.
5. **Add lighting/material** — separar shape correctness de shading.
6. **Profile** — loops, samples, overdraw, resolution, branching.
7. **Optimize** — reduzir passos/samples, usar bounds/early exits, LOD ou lower-res passes quando fizer sentido.
8. **Debug visually** — trocar temporariamente output por normals, depth, step count, UV ou material IDs.
9. **Adapt runtime** — ShaderToy, WebGL2, Three.js/R3F ou engine real do projeto.
10. **Verify output** — render real antes de afirmar qualidade/performance.

## Regras

- não copiar budgets fixos de outra máquina como garantia de performance;
- ray marching, volumetrics e multipass são caros: medir antes de aumentar qualidade;
- função visualmente correta pode ainda estar numericamente instável;
- compilar não prova que o shader está correto;
- usar antialiasing, tone mapping e gamma conscientemente;
- preservar reduced motion e fallback quando o shader for parte de UI crítica;
- em aplicações web, não deixar um efeito decorativo destruir responsividade ou bateria.

## WebGL adaptation

Ao portar ShaderToy/GLSL para WebGL:

- confirmar versão GLSL/ESSL;
- adaptar inputs/outputs/uniforms;
- verificar coordinate conventions;
- confirmar precision e texture functions;
- respeitar ordem/declaration rules do compilador;
- testar no browser/runtime real.

## Segurança

Shaders podem travar GPU/browser com loops ou allocations excessivos. Usar limites defensivos e testar progressivamente. Não executar shaders externos não confiáveis sem inspeção.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Para páginas web, usar o navegador controlável disponível e sua API documentada; separar inspeção de DOM, evidência visual e estado de aplicação. Controle de navegador não implica controle de aplicativos nativos ou dispositivos móveis. Confirmar contexto WebGL/GPU e bibliotecas antes de renderizar. Sem runtime gráfico, entregar código e estratégia de teste, declarando a ausência de medição e revisão visual.

## Integração

Combina com `web-design-engineer`, `procedural-3d-reconstruction`, `runtime-ui-verification` e `verify-before-claim`.

## Referências

Adaptada de MiniMax-AI/skills · `shader-dev`.

Origem local: [shader-graphics-engineering.docx](../shader-graphics-engineering.docx).
