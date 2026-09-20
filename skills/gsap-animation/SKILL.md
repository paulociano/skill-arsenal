---
name: gsap-animation
description: "Implementar e revisar animações GSAP com timelines, ScrollTrigger e integração ao ciclo de vida, preservando escopo, acessibilidade e limpeza."
---

# gsap-animation

## Quando usar

GSAP existente, pedido explícito ou animação cuja coordenação justifique essa biblioteca. Para transições simples, avalie CSS e a solução já instalada; não recomende GSAP automaticamente para toda animação.

## Workflow

1. Identifique framework, versão instalada, efeito desejado e motivo funcional. Consulte somente o módulo upstream relevante e a documentação oficial correspondente.
2. Verifique disponibilidade de `gsap`, plugins usados e `@gsap/react` quando aplicável; registre plugins conforme a API da versão real.
3. Delimite alvos por container/refs e defina propriedade do ciclo de vida. Use timelines e labels para sequências em vez de acumular delays frágeis.
4. Em React, use `useGSAP` se disponível ou contexto com limpeza no efeito. Configure dependências/reversão conforme o comportamento esperado. Callbacks tardios exigem associação ao contexto e remoção de listeners/timers; `contextSafe` não deve ser tratado como cancelamento automático de qualquer callback.
5. Em scroll, escolha entre progresso vinculado e eventos discretos. Associe ScrollTrigger à timeline principal ou tween independente, sem disputar controle do mesmo playhead. Recalcule medidas após mudanças relevantes de layout.
6. Em deslocamento horizontal, separe wrapper fixado de conteúdo animado; confira unidades: `x` em pixels, `xPercent` em porcentagem. Calcule distância a partir da largura real do conteúdo e viewport; não copie exemplos sem validar nomes, sinais e unidades.
7. Limpe apenas animações/triggers pertencentes ao componente ou fluxo. Evite matar globalmente triggers de outras partes da aplicação.
8. Verifique montagem/desmontagem, navegação repetida, resize, conteúdo dinâmico e preferência de movimento reduzido. Mantenha conteúdo e ações acessíveis no estado sem animação. Remova marcadores de debug antes da entrega.

## Leitura sob demanda

No [repositório oficial de skills](https://github.com/greensock/gsap-skills/tree/main/skills):
- `gsap-core` / `gsap-timeline`: API e sequenciamento.
- `gsap-scrolltrigger`: scroll, pinning e refresh.
- `gsap-react` / `gsap-frameworks`: ciclo de vida.
- `gsap-performance`: custo de animação.
- `gsap-plugins` / `gsap-utils`: somente para plugins/helpers necessários.

Trate snippets como material de referência sujeito à versão e verificação, não como garantia de correção. A avaliação de 2026-09-20 identificou `Max.max` e mistura de pixels com `xPercent` em um exemplo upstream; esses trechos não foram importados.

## Dependências e validação

Runtime de navegador e biblioteca GSAP compatível com o projeto. Nenhum pacote é instalado por ler esta skill. Não alegue validação visual sem executar e inspecionar a aplicação. Prefira transform/opacity quando apropriado e limite animações automáticas que não ajudam a tarefa.
