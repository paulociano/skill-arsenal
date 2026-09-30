---
name: cinematic-visual-direction
description: Projetar cenas e sequências visuais cinematográficas para landing pages, apresentações e vídeos por enquadramento, profundidade, câmera, movimento de sujeito, duração, transições e continuidade, sem depender de um gerador específico.
---

# Cinematic Visual Direction

## Objetivo

Transformar uma direção visual em uma sequência de shots executáveis. Tratar motion como linguagem narrativa e espacial, não como decoração, permitindo que uma mesma direção seja implementada em web, slides HTML, vídeo renderizado ou assets animados.

## Quando usar

- hero sections com vídeo, parallax, camera move ou image-to-video;
- apresentações que precisam funcionar como cenas e não como layouts estáticos repetidos;
- referências de estética cinematográfica, campanhas de moda/produto, trailers, title sequences ou experiências no estilo de geradores de vídeo com camera control;
- quando uma imagem estática precisa virar um loop, reveal, transição ou shot curto;
- antes de Remotion, Motion Canvas, GSAP, WebGL, Rive, Lottie ou geradores image-to-video.

## Shot contract

Para cada cena relevante, definir somente os campos que afetam a execução:

- **purpose** — o que o shot comunica ou faz avançar;
- **subject** — foco visual principal;
- **framing** — wide, medium, close, macro, top-down, profile ou composição específica;
- **camera** — static, pan, tilt, dolly, truck, pedestal, orbit, crane, zoom ou combinação controlada;
- **subject motion** — movimento independente do assunto;
- **depth** — foreground, midground, background e oclusões úteis;
- **duration** — duração e ponto de entrada/saída;
- **easing/rhythm** — aceleração, desaceleração, hold e beat;
- **transition** — cut, match cut, mask, wipe espacial, morph, dissolve, camera continuation ou transição por objeto;
- **loop** — quando aplicável, condição para início/fim compatíveis;
- **fallback** — frame estático ou versão reduced-motion.

## Workflow

1. Ler brand/design direction, narrativa, assets e formato de destino.
2. Definir a função da sequência: capturar atenção, revelar produto, explicar mecanismo, criar atmosfera, demonstrar transformação ou conectar capítulos.
2a. Quando a referência vier de cinema, extrair uma gramática estrutural específica — enquadramento, luz, textura, ritmo, profundidade, montagem e relação câmera/sujeito — em vez de pedir genericamente "estilo cinematográfico". A referência inspira decisões; não é uma spec para copiar.
3. Criar poucos shots com funções distintas. Evitar movimento contínuo sem mudança narrativa.
3a. Para web, tratar o primeiro frame/hero como um pôster: a composição precisa funcionar parada antes de depender de animação.
4. Planejar continuidade entre shots: direção de movimento, escala, luz, cor, posição do sujeito e vetor dominante.
5. Separar movimento de câmera de movimento do sujeito. Não pedir “cinematic motion” como propriedade abstrata.
6. Usar profundidade e oclusão para produzir sensação espacial antes de adicionar efeitos.
7. Escolher a técnica mínima capaz de executar o shot. Roteie pelo efeito necessário e pelo custo, não pelo prestígio técnico:
   - CSS/SVG para transformações simples;
   - GSAP/scroll para progressão ligada à interface;
   - Canvas/WebGL/Three.js para câmera, profundidade e shaders em runtime;
   - Lottie/Rive para assets vetoriais;
   - vídeo/Remotion/Motion Canvas para motion pré-renderizado;
   - image-to-video quando geração temporal for realmente necessária e houver ferramenta disponível.
8. Definir reduced-motion e frame de fallback antes da implementação.
9. Validar legibilidade, CTA, conteúdo e performance no meio de destino. Motion nunca deve esconder a mensagem principal.
10. Revisar a sequência como filme: ritmo, repetição de câmera, continuidade, excesso de cortes e ponto de clímax.

## Gramática cinematográfica

- **Push/dolly in:** aproxima importância ou revela detalhe.
- **Pull/dolly out:** contextualiza e amplia escala.
- **Orbit:** revela forma/volume; usar com parcimônia.
- **Parallax:** comunica profundidade quando planos têm velocidades coerentes.
- **Rack-focus equivalente:** desloca atenção entre planos; em interfaces pode ser simulado por foco, blur, escala ou contraste.
- **Object-led transition:** um objeto cruza o frame e mascara a troca de cena.
- **Match movement:** mantém direção/velocidade entre cenas para continuidade.
- **Hold:** pausa deliberada que permite leitura; não preencher todo segundo com movimento.

## Aplicação em apresentações

Tratar slides importantes como beats de uma sequência:
- slide = estado visual, não necessariamente cena isolada;
- transição deve preservar ou romper continuidade de forma intencional;
- títulos podem entrar como elementos de composição, não como cabeçalhos automáticos;
- vídeo pode ocupar background, janela, máscara tipográfica ou detalhe;
- animação deve respeitar tempo de fala e leitura;
- manter uma versão estática/exportável quando o formato final não reproduzir motion.

## Aplicação em landing pages

- hero motion deve reforçar a promessa e preservar LCP/CTA;
- scroll pode controlar câmera, tempo ou reveal somente quando fizer parte da narrativa;
- vídeo de fundo precisa de poster/fallback, compressão e comportamento mobile;
- evitar smooth scroll, WebGL ou vídeo apenas para sinalizar “premium”;
- cenas pesadas podem ser pré-renderizadas quando vídeo comprimido for mais barato que runtime gráfico.

## Limites

- Esta skill dirige shots; não afirma gerar vídeo quando não houver ferramenta real disponível.
- Uma signature idea forte por superfície costuma ser melhor que empilhar efeitos concorrentes; exceções precisam de intenção composicional clara.
- Referências de marcas ou produtos servem para extrair linguagem de câmera, ritmo e composição, não para copiar identidade.
- Não presumir que image-to-video preservará produto, tipografia, rosto ou geometria com precisão; validar o output.
- Não transformar toda landing ou apresentação em filme. Motion é opcional e proporcional à função.

## Fontes da adaptação

- Doubiiu/MotionCanvas (SIGGRAPH 2025): decomposição de movimento de câmera e movimento de objeto em image-to-video controlável.
- remotion-dev/remotion e remotion-dev/skills: composição programática de vídeo com React e boas práticas de mídia.
- motion-canvas/motion-canvas: animação programática orientada por cenas e sincronização.
- hakimel/reveal.js e slidevjs/slidev: apresentações web com mídia, transições e estados animados.
- Codrops e demos associadas de GSAP/WebGL: continuidade espacial, scroll cinematográfico, shaders e transições.
- MustBeSimo/web-design-studio, ridelink0/ultimate-frontend-skills, omarkhandji-commits/scroll-3d-cinematic-stack e PyModel/cinematic-ui: route-before-renderer, primeiro frame como pôster, gramática cinematográfica explícita, referências divergentes, fallbacks e verificação proporcional.