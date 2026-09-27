# Avaliação — cinematic web & presentation repositories

Data: 2026-09-27

## Objetivo

Avaliar referências externas para elevar landing pages e apresentações do Arsenal com composição cinematográfica, vídeo, motion graphics, scroll, WebGL e image-to-video controlável.

## Avaliações

### Doubiiu/MotionCanvas — D

Skill técnica/paper de SIGGRAPH 2025. O valor incremental está na decomposição explícita entre movimento de câmera e movimento de objetos para cinematic shot design. A execução real depende de modelos, pesos e runtime próprios; o Arsenal adota a gramática de direção, não finge executar o backend.

**Adotar:** shot contract, camera motion, object motion, continuidade e planejamento de image-to-video.
**Não adotar:** instalação/modelos específicos como requisito.

### slidevjs/slidev — A

Ecossistema de apresentações web com componentes, animações e extensibilidade. A skill oficial é uma boa referência operacional. Acrescenta uma rota concreta para decks interativos/cinematográficos quando HTML é aceitável.

**Adotar:** scene-oriented slides, componentes, mídia e progressive reveals.
**Limite:** não substituir PPTX/Google Slides quando editabilidade nativa for requisito.

### hakimel/reveal.js — B

Framework maduro para apresentações HTML, útil como metodologia e runtime opcional para backgrounds em vídeo, auto-animate, parallax e mídia.

**Adotar:** estados visuais, backgrounds, continuidade e mídia.
**Não criar skill separada:** overlap alto com web-video-presentation.

### remotion-dev/remotion + remotion-dev/skills — A/D

Metodologia forte para vídeo programático e boas práticas de mídia. Execução depende de runtime React/Remotion disponível, portanto é A como conhecimento operacional e D na execução técnica.

**Adotar:** composição temporal, vídeo como componente, loops, timing e pré-render quando mais eficiente que runtime gráfico.
**Não exigir:** Remotion como dependência universal.

### motion-canvas/motion-canvas — B/D

Boa metodologia de animação programática orientada por cenas e sincronização. Runtime específico para execução.

**Adotar:** scene graph, timing e motion graphics explicativos.
**Não duplicar:** procedural-film ou video-editing-pipeline.

### Codrops + demos GSAP/WebGL — B

Biblioteca de padrões e experimentos de alta qualidade para scroll, shaders, transições e tipografia. O Arsenal já possui as skills técnicas correspondentes.

**Adotar:** referências de composição, continuidade espacial e padrões de hero/scroll.
**Atualizar:** creative-web-engineering e landing-craft, sem criar nova skill Codrops.

## Decisão

Criar `cinematic-visual-direction` como owner transversal da gramática de shots e `cinematic-presentation` como stack. Atualizar rotas existentes para acionar essa capacidade somente quando motion cinematográfico melhorar materialmente a experiência.
