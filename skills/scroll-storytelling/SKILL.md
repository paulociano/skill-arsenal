---
name: scroll-storytelling
description: "Projetar experiências narrativas guiadas por scroll com estágios, pinning, parallax, transições e sincronização DOM/WebGL sem sacrificar acessibilidade ou performance."
---

# scroll-storytelling

## Objetivo

Transformar scroll em estrutura narrativa quando a progressão espacial ajuda a explicar, revelar ou dramatizar conteúdo. A skill decide a gramática de scroll antes da biblioteca.

## Quando usar

- landing pages e portfolios com storytelling progressivo;
- sticky/pinned sections, scrollytelling, galleries e capítulos;
- sincronização entre DOM e WebGL;
- parallax deliberado;
- transições entre cenas guiadas pelo progresso do scroll.

## Modelo

Classifique cada trecho como um destes padrões:

- **flow** — conteúdo segue o documento normalmente;
- **reveal** — elemento entra conforme se torna relevante;
- **sticky-stage** — um palco permanece enquanto conteúdo/estado muda;
- **progress-linked** — propriedade depende continuamente do progresso;
- **chapter-transition** — troca explícita entre cenas/seções;
- **DOM/WebGL sync** — elemento semântico no DOM recebe camada visual sincronizada.

Use o padrão mais simples que preserve a narrativa.

## Workflow

1. Definir a história: o que o usuário deve entender antes, durante e depois de cada seção.
2. Dividir em beats/capítulos e definir o papel do scroll em cada um.
3. Manter conteúdo crítico no fluxo semântico do documento.
4. Definir quais trechos realmente precisam de sticky, pinning, parallax ou progress-linked motion.
5. Escolher o mecanismo:
   - CSS/sticky + IntersectionObserver para casos simples;
   - GSAP/ScrollTrigger quando timelines e pinning coordenado forem necessários;
   - Lenis ou smooth-scroll equivalente apenas quando suavização/sincronização tiver função real;
   - R3F/scroll-rig ou WebGL equivalente quando DOM e cena 3D precisarem permanecer alinhados.
6. Planejar mobile/touch separadamente; não presumir que o desktop pinned funciona em tela curta.
7. Criar fallback/reduced-motion que preserve leitura e ordem.
8. Testar resize, deep links, anchor navigation, back/forward e navegação por teclado.
9. Medir custo de renderização e evitar múltiplos loops de scroll competindo.
10. Verificar a narrativa no runtime, não apenas cada animação isolada.

## Smooth scroll

Smooth scrolling não é storytelling por si só.

Só adote uma camada como Lenis quando ela resolver:
- sincronização com WebGL;
- consistência temporal necessária a uma experiência;
- parallax/timelines que dependem de um único loop.

Preserve scroll nativo, anchors, sticky, keyboard e acessibilidade sempre que possível. Não substituir o modelo de scroll do browser apenas para "parecer premium".

## DOM + WebGL

Quando WebGL complementar elementos HTML:
- manter um canvas compartilhado quando isso reduzir contextos/recursos;
- usar proxies/medidas do DOM em vez de duplicar layout em 3D;
- observar resize/intersection em vez de medir layout a cada frame quando possível;
- HTML continua responsável por conteúdo, semântica e acessibilidade;
- WebGL é enhancement, não pré-requisito para entender a página.

## Regras

- Não pinne se a seção funciona melhor em flow.
- Parallax deve reforçar profundidade/hierarquia, não causar perda de orientação.
- Scroll hijacking agressivo, bloqueio de wheel/touch e snapping forçado exigem forte justificativa.
- Reduced motion precisa remover movimento vestibular sem esconder conteúdo.
- Não usar progresso de scroll como única forma de fornecer controle essencial.

## Integração

web-design-engineer, ui-motion-design, gsap-animation, shader-graphics-engineering, runtime-ui-verification e web-quality-audit.

## Origem metodológica

Adaptada de darkroomengineering/lenis, 14islands/r3f-scroll-rig, barbajs/barba e locomotive-scroll, preservando os princípios de narrativa, progressive enhancement, sincronização e acessibilidade sem exigir bibliotecas específicas.
