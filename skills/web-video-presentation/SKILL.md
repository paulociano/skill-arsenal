---
name: web-video-presentation
description: "Criar apresentações HTML por cenas e narração para navegação por clique ou gravação, quando a entrega em navegador é parte do pedido."
---

# web-video-presentation

## Objetivo

Transformar artigo ou roteiro em uma apresentação web 16:9, orientada por passos/narração, pensada para navegação por clique e eventual gravação como vídeo.

## Quando usar

Criar apresentações HTML por cenas e narração para navegação por clique ou gravação, quando a entrega em navegador é parte do pedido.

## Conceito central

- roteiro define o ritmo;
- artigo/material original define a densidade visual;
- uma batida de narração corresponde a um step visual;
- cada step ocupa a tela inteira;
- animação deve nascer da relação entre as ideias, não de um preset genérico;
- tema mantém coerência, mas cada capítulo pode ter dinâmica própria.

## Workflow

1. Gerar ou organizar `script` + `outline` a partir do material fornecido.
2. Definir tema, assets e modo de construção.
3. Implementar uma primeira cena/capítulo como âncora de qualidade quando a tarefa permitir iteração.
4. Construir os capítulos restantes mantendo uma fonte única de verdade para sequência e narração.
5. Opcionalmente preparar áudio/TTS somente quando ferramentas e autorização realmente existirem.
6. Verificar navegação, timing visual e gravação.

## Apresentações web e Markdown

Para apresentações web/Markdown:

- **um ponto principal por slide**;
- exemplos/decks de referência servem como quality bar de composição, não como template para cópia;
- variar visual type entre slides: hero, chart, metric card, timeline, comparison, image-led etc.;
- conteúdo precisa ser escrito para a capacidade real do slide, porque overflow pode ser silencioso;
- sempre fazer preview/render antes de considerar concluído;
- charts quantitativos devem vir de dados reais, não de SVG decorativo inventado;
- interações HTML (details, tooltips, controls) só contam quando o output final é HTML; PDF/PPTX podem perder comportamento;
- fontes/cores fixas do repo original são exemplos, não design system universal.

Quando o usuário pedir **MARP especificamente**, Markdown + frontmatter + CSS/SVG pode ser o artefato correto. Para PPTX/Google Slides tradicionais, preferir a capacidade nativa de apresentações.

## Decks HTML interativos

Para decks HTML interativos:

- tokens de tema e layouts reutilizáveis devem ser separados do conteúdo;
- começar do layout mais próximo quando isso reduz risco de overflow e inconsistência, sem obrigar uma biblioteca específica;
- imagens de screenshot/diagrama usam contain, fotos podem usar cover;
- speaker notes ficam fora do conteúdo visível;
- presenter view, timer, next-slide preview e keyboard navigation são recursos úteis somente quando runtime real suportar;
- tema, animação e FX não substituem narrativa nem hierarquia;
- render/preview é obrigatório antes de declarar deck pronto;
- assets paths e offline behavior precisam ser verificados.

Para PPTX/Google Slides tradicionais, continuar preferindo ferramentas nativas. HTML deck é escolhido quando interatividade/browser delivery for parte real do pedido.

## Correção de comentários visuais

Quando o deck for código/web e houver inspector/runtime:

1. render/present;
2. ancorar comentário ao slide/elemento exato;
3. persistir o finding próximo da fonte ou com locator estável;
4. aplicar apenas comentários pendentes;
5. limpar/marcar resolvido;
6. rerender e comparar.

Esse loop reduz feedback vago como “melhora essa página”. Comentários devem apontar para elemento/slide, e a resolução só conta depois do novo render.

Canvas fixo, React ou 1920×1080 são escolhas do Open Slide, não regras universais do Arsenal.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Para páginas web, usar o navegador controlável disponível e sua API documentada; separar inspeção de DOM, evidência visual e estado de aplicação. Controle de navegador não implica controle de aplicativos nativos ou dispositivos móveis. Para decks tradicionais, usar a skill de apresentações. TTS e gravação são módulos opcionais que dependem de ferramenta real; não exigir Agent Teams, MiniMax, chaves de API ou scaffolds externos.

## Referências

[GitHub · ConardLi/garden-skills · web-video-presentation](https://github.com/ConardLi/garden-skills/tree/main/skills/web-video-presentation)

Origem local: [web-video-presentation.docx](../web-video-presentation.docx).
