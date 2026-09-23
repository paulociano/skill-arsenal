---
name: motion-asset-engineering
description: "Escolher, integrar e validar assets animados em web entre SVG/CSS, Lottie, Rive, Canvas e vídeo conforme interação, peso, editabilidade e acessibilidade."
---

# motion-asset-engineering

## Objetivo

Escolher a forma correta de entregar motion como asset, separando animação de interface programática de assets produzidos em ferramentas de motion design.

## Quando usar

- Lottie, Rive, animated SVG ou motion asset fornecido por designer;
- mascotes, illustrations, onboarding, empty states, hero loops e microanimações;
- decisão entre reconstruir em código, usar asset vetorial ou vídeo;
- animações interativas/state-machine.

## Decision table

### SVG/CSS/WAAPI
Use para:
- ícones e ilustrações simples;
- poucos paths/propriedades;
- interação leve;
- controle sem runtime adicional.

### Lottie
Use quando:
- a animação vem de After Effects/bodymovin;
- a timeline é essencialmente pré-autorizada;
- precisa reproduzir vetor/shape animation com bom handoff designer-dev;
- interação é simples (play/pause/segment/speed).

### Rive
Use quando:
- asset precisa responder a inputs/estados;
- state machine faz parte da experiência;
- animação precisa ser reutilizável e interativa.

### Canvas/WebGL
Use quando:
- há partículas, shaders, simulação, milhares de elementos ou desenho procedural;
- o asset na prática é um sistema gráfico.

### Video
Use quando:
- fidelidade visual supera editabilidade/interação;
- compressão de vídeo é mais barata do que recriar/renderizar a cena em tempo real.

## Workflow

1. Confirmar origem, licença e formato do asset.
2. Identificar se a animação é linear ou interativa.
3. Definir necessidade de controle: autoplay, hover, progress, state machine, scroll, input.
4. Comparar peso/runtime, qualidade, escalabilidade e suporte do projeto.
5. Escolher a tecnologia mínima suficiente.
6. Definir lazy loading e placeholder quando o asset não for crítico acima da dobra.
7. Para autoplay/loops decorativos, respeitar reduced motion e pausar quando fora de viewport quando fizer sentido.
8. Garantir fallback estático quando o asset comunica informação importante.
9. Testar transparência, resize, DPR, theme/light-dark e lifecycle.
10. Verificar consumo de CPU/GPU e impacto em LCP/INP quando relevante.

## Regras

- Não instalar After Effects plugins ou ferramentas externas só para avaliar um asset.
- Não assumir que Lottie reproduz todo recurso de After Effects com fidelidade.
- Não usar vídeo como botão/interação essencial.
- Não usar autoplay pesado acima da dobra sem medir impacto.
- Assets animados de terceiros continuam sujeitos a licença e proveniência.
- Motion sem função pode ser substituído por um frame estático.

## Integração

ui-motion-design, interaction-polish, scroll-storytelling, shader-graphics-engineering, web-quality-audit.

## Origem metodológica

Adaptada de airbnb/lottie-web, rive-app/rive-wasm e práticas de SVG/Canvas/WebGL do Arsenal. Preserva a decisão tecnológica e o handoff sem exigir as ferramentas autorais de origem.
