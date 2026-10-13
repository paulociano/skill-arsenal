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

## Originalidade e QA de jornada

Em sites premium guiados por scroll, comparar gramática de página, navegação, hero, progressão dos atos, encerramento e interação exclusiva antes de reutilizar um template. Planejar a curva de atenção e um pico narrativo sem impor estética ou número fixo de efeitos. Para heróis em camadas, estabelecer planos, oclusão e âncoras de contato; compor o mobile como cena própria. Conferir capturas em início, meio, fim e estados intermediários em desktop e mobile, com fallback de reduced motion, foco e conteúdo legível. Referência metodológica: https://github.com/nateherkai/scroll-craft ; não exigir seus serviços de geração, engine ou scripts.

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

## Taxonomia técnica complementar (scrollytelling)

Ao desenhar os beats, identifique também a técnica visual concreta:
- **graphic sequence**: troca discreta de gráfico/estado por capítulo;
- **animated transition**: interpolação de estados quando a continuidade explica a mudança;
- **pan and zoom**: revelar escala ou região de imagem/mapa com propósito;
- **moviescroller**: sequência de frames guiada por scroll, somente quando os assets e o orçamento suportarem;
- **show-and-play**: ativação de mídia ou interação em marcos narrativos, sempre com controle alternativo.

Essa taxonomia descreve a experiência, não determina a biblioteca. Documentar o beat, estado inicial/final, trigger, fallback e critério verificável de entendimento.

## Escolha progressiva de mecanismos nativos

- Considerar CSS `animation-timeline: view()` ou `scroll()` com `@supports` para casos declarativos, verificando suporte real nos navegadores-alvo e fallback legível sem animação.
- Preferir `IntersectionObserver` para revelar conteúdo e atualizar passos discretos; não usar listener de scroll contínuo quando um observer resolver.
- Em React, avaliar Motion para progressos mapeados a transform/opacity; GSAP ScrollTrigger para múltiplas timelines ou pinning; não introduzir ambos sem necessidade.
- Em código dependente de scroll contínuo, usar listeners passivos, `requestAnimationFrame` quando cabível e cleanup correto. Evitar medidas de layout e setState por frame desnecessários.
- Não presumir bundle sizes, compatibilidade entre browsers ou ganhos de performance a partir de números retirados de exemplos externos; medir o caso real.

## Mobile e interação robusta

1. Desenhar versão empilhada e semanticamente completa antes de expandir para pinned desktop. Nunca ocultar o único visual explicativo no mobile.
2. Validar `svh`, mudanças da chrome do navegador, sticky com ancestrais `overflow`, rolagem por momentum e mudanças de orientação.
3. Não bloquear `touch`, pull-to-refresh ou back-swipe sem justificativa funcional e alternativa acessível; evitar `scroll-snap: mandatory` em painéis cujo conteúdo excede a altura útil.
4. Toda interação por gesto deve ter controle equivalente por toque/teclado. Manter landmarks, links de âncora, histórico, leitura por screen reader e ordem de foco.
5. Verificar no runtime progressão completa, estados intermediários, reduced motion, throttling, memória e navegação em dispositivos reais quando disponíveis. Não alegar testes em hardware que não foram feitos.

## Evidência e limites

Não usar alegações genéricas de aumento de engajamento, retenção ou conversão como expectativa causal para um projeto. Definir hipóteses e métricas próprias quando o negócio exigir validação.

Referência adicional: [doodledood/claude-code-plugins, scrollytelling, commit 3c29306](https://github.com/doodledood/claude-code-plugins/blob/3c29306a42255bb58c1fdfd0060d449b7dd1335e/claude-plugins/frontend-design/skills/scrollytelling/SKILL.md). Adaptada sem depender das perguntas de interface, comandos ou runtime do Claude Code.
