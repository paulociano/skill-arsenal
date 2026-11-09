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

## Padrão opcional: fontes vinculadas e cenas animadas (Mira)

Quando o pedido envolver transformar PDF, projeto, artigo ou material existente em apresentação HTML animada, trabalhar em quatro artefatos conceituais separados: **fontes somente leitura → outline/claims verificáveis → roteiro e contrato das cenas → deck renderizado**. Manter a pasta de saída separada das fontes e documentar seus caminhos; não escrever automaticamente nos arquivos de origem.

Para cada cena, especificar mensagem, fonte, metáfora visual ou gráfico justificado, tempo/interação, entrada e saída. Preferir transições que expliquem relações, sem impor loops contínuos a tudo; oferecer `prefers-reduced-motion`, controles por teclado e fallback estático. Testar viewport, overflow, sequência e sincronização de narração antes de exportar. Deck HTML autocontido/offline é opção, não promessa automática, e depende de verificar assets e scripts.

Reordenação, desenho, controle remoto, gravação em webcam/microfone e HTML→MP4 são módulos **opcionais**, usados só quando o runtime e permissões do usuário permitem testar. Para vídeo, verificar captura, áudio, duração, dimensões, sincronismo e render final; não assumir Puppeteer/ffmpeg. Não replicar a CLI de Claude ou templates proprietários da fonte.

Referência metodológica: https://github.com/sandeco/mira-animator (PolyForm Noncommercial 1.0.0; sem incorporação de código externo).

## Documento de apresentação HTML autocontido e editável (Bento, 2026-10-24)

Para apresentações portáveis em HTML, distinguir página de playback de **documento autocontido com editor e esquema de dados**. Quando requerido, armazenar slides, IDs estáveis, estados, gráficos, fontes e mídia com manifesto/versionamento e validar round-trip: editar dados estruturados → renderizar → salvar arquivo → reabrir → editar novamente. Identificadores compartilhados podem coordenar transições morph, mas requerem continuidade semântica e checks de colisões. Preferir fallback de download quando a File System Access API não existe. Colaboração em arquivo com chave embutida exige explicar que posse do arquivo pode equivaler a acesso e não assumir identidade autenticada; testar merge, conflitos e modo offline real. Atualizações assinadas e CRDT são alegações/implementações externas, não capacidades automaticamente herdadas por um HTML gerado aqui.

Fonte: https://github.com/nyblnet/bento . A publicação de HTML autocontido deve ser verificada no browser; aplicativo Bento não foi instalado.

## Deck HTML de arquivo único com descoberta visual de estilo (frontend-slides, 2026-11-09)

Para decks HTML feitos para pessoas sem repertório de design (pitch, aula, palestra, conversão de PPTX):

1. **Uma rodada de perguntas, todas juntas:** finalidade, tamanho aproximado, se o conteúdo já existe e a **densidade** — *falado* (uma ideia por slide, tipo grande, 1–3 bullets, mais slides) ou *de leitura* (slides autossuficientes, grades, tabelas, 4–8 bullets). Em dúvida, plateia ao vivo puxa para falado; circulação assíncrona puxa para leitura. Se o conteúdo excede a densidade, dividir em mais slides em vez de encolher.
2. **Imagens antes do roteiro:** inspecionar cada imagem fornecida (o que mostra, utilizável ou não, que conceito representa, cores dominantes) e desenhar o roteiro em volta delas (3 telas → 3 slides de feature; logo → abertura e fechamento), confirmando com o usuário.
3. **Mostrar em vez de perguntar o gosto:** gerar **três prévias reais** do primeiro slide (uma segura, uma ousada, uma curinga desenhada para o contexto), com o logo do usuário quando houver, e deixar escolher ou misturar. **Prévias precisam parecer slides de verdade:** nunca escrever no slide "opção A", nome de template, "seguro/ousado", caminhos de arquivo ou anotações do pedido; só elementos reais do deck (título, seção, data, autor).
4. **Palco fixo 16:9:** autorar cada slide num palco de 1920×1080 escalado por inteiro para a viewport (com faixas laterais se preciso), sem breakpoints que reorganizem o conteúdo no celular. Trocar slides por `visibility`/`opacity`/`pointer-events`, não por `display: none`, que conflita com classes de layout. Lembrar que `-clamp()`, `-min()` e `-max()` são ignorados silenciosamente: usar `calc(-1 * clamp(...))`. Respeitar `prefers-reduced-motion`. Reflow responsivo só quando o "deck" for na verdade uma página de leitura.
5. **Arquivo único:** HTML com CSS/JS inline, fontes de Google Fonts ou Fontshare (nunca as do sistema), cores e tipografia em variáveis CSS, seções comentadas; edição de texto inline como recurso padrão depois do primeiro rascunho, sem perguntar antes.
6. **Ao editar um deck existente:** contar o que já há no slide antes de adicionar; imagem nova num slide cheio vai para um slide novo; acima de 4–6 bullets, criar slide de continuação; reorganizar proativamente e avisar.
7. **Verificar no render:** sobreposição de painéis e texto estourando o card, em screenshots a 1280×720 e numa viewport de celular. Checar só `scrollHeight` não basta: painéis de grade podem se cobrir sem gerar rolagem.
8. **Conversão de PPTX:** extrair textos, imagens, ordem e notas do apresentador; confirmar o inventário com o usuário; escolher o estilo pelo passo 3; preservar todo o conteúdo e as notas (como comentários HTML).
9. **Publicar ou exportar só se o usuário pedir**, depois da entrega.

Quando o ambiente oferecer um tipo nativo de apresentação editável (ex.: artifact de Slides), ele tem preferência para decks que serão editados ou exportados para PPTX; este padrão serve quando a entrega é um HTML autocontido.

Fonte: [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) (MIT, commit `9906a34`). Absorção metodológica, sem o template pack, os scripts de deploy (Vercel) e PDF nem a dependência de `python-pptx`.

