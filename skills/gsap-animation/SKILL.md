---
name: gsap-animation
description: "Implementar e revisar animações GSAP com timelines, ScrollTrigger, matchMedia, performance e integração ao ciclo de vida, preservando acessibilidade e limpeza."
---

# gsap-animation

## Quando usar

GSAP existente, pedido explícito ou animação cuja coordenação justifique essa biblioteca. Para transições simples, avalie CSS/WAAPI e a solução já instalada; não recomende GSAP automaticamente para toda animação.

## Workflow

1. Identifique framework, versão instalada, efeito desejado e motivo funcional. Consulte somente o módulo upstream relevante e a documentação oficial correspondente.
2. Verifique disponibilidade de gsap, plugins usados e @gsap/react quando aplicável; registre plugins conforme a API da versão real.
3. Delimite alvos por container/refs e defina propriedade do ciclo de vida.
4. Para tweens simples:
   - prefira propriedades transform/opacity quando servirem ao efeito;
   - use aliases GSAP como x/y/scale/rotation em vez de strings transform complexas quando isso melhorar controle;
   - em from/fromTo que disputam a mesma propriedade, verifique immediateRender antes de concluir que o segundo tween está quebrado;
   - use overwrite deliberadamente quando houver concorrência entre animações.
5. Para sequências, use timelines e labels em vez de acumular delays frágeis.
6. Em React, use useGSAP quando disponível ou contexto/efeito com cleanup. Callbacks tardios exigem associação ao contexto e remoção de listeners/timers; contextSafe não é cancelamento automático.
7. Para responsividade e reduced motion, preferir gsap.matchMedia() ou mecanismo equivalente do framework quando disponível, mantendo conteúdo e ações acessíveis sem animação.
8. Em scroll, escolha entre progresso vinculado e eventos discretos. Associe ScrollTrigger à timeline/tween correto e evite dois controladores disputando o mesmo playhead.
9. Em pinning/horizontal scroll:
   - separe wrapper fixado de conteúdo animado;
   - x é pixels; xPercent é porcentagem;
   - derive distância da geometria real;
   - refreshe medidas após mudanças relevantes de layout/fontes/assets.
10. Limpe apenas animações/triggers pertencentes ao componente ou fluxo.
11. Verifique montagem/desmontagem, navegação repetida, resize, conteúdo dinâmico, toque/teclado e movimento reduzido.
12. Remova markers/debug antes da entrega.

## Performance

- Evite animar propriedades que provoquem layout contínuo quando transform/opacity resolvem o efeito.
- Não aplique will-change indiscriminadamente.
- Grandes quantidades de elementos, filtros, blur, SVG complexo e scroll handlers exigem teste no runtime real.
- FPS percebido e fluidez não podem ser inferidos apenas pelo código.

## Leitura sob demanda

No repositório oficial greensock/gsap-skills:
- gsap-core: tweens, easing, stagger, matchMedia;
- gsap-timeline: sequenciamento;
- gsap-scrolltrigger: scroll, pinning e refresh;
- gsap-react / gsap-frameworks: ciclo de vida;
- gsap-performance: custo de animação;
- gsap-plugins / gsap-utils: somente quando necessários.

Trate snippets como referência sujeita à versão e verificação. A avaliação anterior identificou exemplos upstream com erros; não importar trechos cegamente.

## Integração

ui-motion-design decide a linguagem de movimento. gsap-animation entra quando a implementação realmente pede GSAP. runtime-ui-verification e web-quality-audit validam o comportamento final.

## Dependências e validação

Runtime de navegador e biblioteca GSAP compatível com o projeto. Nenhum pacote é instalado por ler esta skill. Não alegue validação visual sem executar e inspecionar a aplicação.

## Referências

Atualizada com base no repositório oficial greensock/gsap-skills, preservando apenas orientação portátil e compatível com a versão real do projeto.
