# Unslop: redline em passes para UI com cara de IA

Metodologia adaptada de [heydamir/unslop](https://github.com/heydamir/unslop) (commit `97daa3e`, 2026-11-09), criada por Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), licença CC BY 4.0. Este arquivo reescreve e resume o método; mantenha este crédito em cópias ou adaptações.

Use quando uma tela existente (dashboard, app ou landing) parece "vibecoded" e o pedido é limpar, polir ou redesenhar **sem mudar o produto**: features, conteúdo e ordem das seções ficam; muda a intenção por trás de cada tamanho, cor, palavra e imagem.

## Princípio central

Slop espalha cor e efeito pelo chrome (fundos, botões, bordas, labels). Craft mantém o chrome quieto e concentra a riqueza em **um ou dois momentos de conteúdo** — um gráfico bem desenhado, um objeto renderizado, uma imagem do mundo do produto. Uma tela limpa que serviria a qualquer produto é só o próximo template.

## 1. Ver a tela real

- Com código: localizar os arquivos que renderizam a tela e, se possível, renderizar e capturar o resultado.
- Só com URL: salvar uma cópia estática da página (browser/Chrome quando disponível, ou script Playwright se instalado e com acesso de rede) e trabalhar sobre a cópia; registrar no relatório que a entrega é uma tela redesenhada em código para o dono do site real. Fundos animados por script não sobrevivem à cópia — descrevê-los a partir da página viva.
- Só com screenshot: reconstruir como um HTML estático fiel e tratá-lo como original.

## 2. Auditar e fazer triagem (obrigatório antes de editar)

Listar cada sinal observado, uma linha cada, com onde ele vive. Sinais típicos (são hipóteses a verificar no contexto, não proibições universais):

- **Superfície/cor**: gradientes de matiz em fundos/cards/botões; texto em gradiente; glows e sombras coloridas; manchas radiais/blobs atrás do conteúdo; bordas neon; vários tons quase iguais para texto; tudo destacado, nada se destaca; vidro com sombra colorida.
- **Tipo**: headings 800–900; labels em CAIXA ALTA com tracking largo; muitos tamanhos/pesos; números em formatos mistos; tracking negativo em texto pequeno; itálico como ênfase.
- **Ícones**: emoji como ícone/decoração/status; ícones de tamanhos e cores variados; ✨ para qualquer coisa de IA; ícones fora da coluna.
- **Espaçamento**: valores arbitrários (`mt-[13px]`); linhas de uma mesma lista com alturas diferentes; grupos mais perto dos vizinhos que dos próprios itens; padding desigual entre cards irmãos.
- **Copy**: headline genérica ou de saudação ("Welcome back! 👋"); exclamações; hype (supercharge, seamless, unlock, AI-powered em tudo); claims não verificáveis (10x, "loved by 10.000 teams"); badges "New ✨"/"Beta 🚀"; mock data com cara de placeholder.
- **Detalhes/visuais/motion**: tudo em pill; contadores em pills brilhantes; gráficos arco-íris numa só série; stat cards entupidos de sparklines; blobs/orbs/cérebros holográficos; `animate-pulse` em algo que não é ao vivo; `transition-all`, `hover:scale` em cards, springs saltitantes.

Depois, decidir o tamanho da intervenção com honestidade:
- **Slop pesado** (muitos sinais em cor, tipo, ícones e copy): processo completo.
- **Slop leve** (tela majoritariamente desenhada): modo polish — corrigir só o que a auditoria achou, manter paleta, tipo, layout e visual da marca existente; ideias maiores viram sugestões no relatório.
- **Sem slop**: dizer isso claramente e sugerir no máximo 2–3 refinamentos com valores exatos; aplicar só se o usuário concordar. Nunca mudar uma tela boa só para ficar diferente.

## 3. Direção em cinco linhas — e parar

Derivar do que a página diz sobre o produto e o público, nunca de tendência:
- **Produto**: o que faz e para quem, uma frase simples.
- **Caráter**: 2–3 palavras concretas (ex.: "calmo, exato, levemente quente"). Proibidos: clean, moderno, sleek, minimal, premium — descrevem qualquer template.
- **Mundo**: o lugar ou material a que o produto pertence (notas → papel e tinta; monitoramento → instrumentos e plantão noturno). Define tom dos neutros, accent e visual.
- **Momentos**: 1–2 lugares onde a tela ganha cor, material e detalhe, escolhidos do que o produto mostra.
- **Assinatura**: um único detalhe só deste produto, usado com consistência (ex.: dot de status ao vivo, keycaps, linha de rota).

Marca real (logo, cor, tipografia que não seja slop) é preservada e a direção se constrói em volta dela. Mostrar auditoria + direção ao usuário e aguardar antes de editar, salvo se ele já pediu para executar direto.

## 4. Nove passes, nesta ordem, cada um na tela inteira

A ordem tem razão: ritmo muda a leitura de tudo; copy antes de tipo/layout porque o tamanho do texto define tamanho e posição; visuais e motion por último porque devem caber numa tela que já funciona sem eles.

1. **Espaçamento** — grade de 4px; coisas iguais com tamanhos iguais; espaço interno do grupo menor que entre grupos; colunas alinhadas (ícones, labels, números à direita); remover valores avulsos. Navegação é a parte mais densa (linhas ~32–36px, 2–4px entre elas, label de seção mais perto dos próprios itens). Medir a sidebar ao final.
2. **Cor** — uma rampa neutra levemente tingida pelo mundo; em apps/dashboards superfícies ficam neutras e o conteúdo carrega a cor; três papéis de texto; um accent raro no chrome; riqueza de cor só dentro dos momentos, com cada cor significando algo; contraste ≥4,5:1 em accent com texto; bordas como hairline (6–10% do texto); profundidade por degraus de superfície em dark mode; gradiente só como leve variação dentro de um neutro.
3. **Ícones** — emoji vira ícone de linha de um único set (o do projeto, senão lucide); um tamanho e um stroke; cor do papel de texto; caixa de ícone de largura fixa; remover ícones que nada acrescentam.
4. **Copy** — headline diz o que faz e para quem com fatos já na página; sem exclamação, sem saudação, sem hype; labels curtos; variações dizem contra o quê comparam; claims não verificáveis: perguntar e remover se não confirmados; mock data plausível.
5. **Tipo** — família escolhida pelo caráter (preservar fonte de marca real; um default que ninguém escolheu pode trocar); uma família de interface + no máximo um par (mono ou display); poucos tamanhos; hierarquia por tamanho e cor, não peso; sentence case; `tabular-nums` e um formato numérico.
6. **Layout** — manter seções e ordem; apps com proporções reais de app (shell no viewport, sidebar ~240–280, conteúdo fluido); hero de landing como cena com texto em área calma, ou split assimétrico; um CTA primário + no máximo um secundário; primeira dobra composta sem faixa morta; mobile em ordem de leitura, previews simplificados em vez de reduzidos.
7. **Detalhes** — raio aninhado (interno = externo − padding, mínimo 4); contadores como texto mudo; atalhos como keycaps; um gráfico principal claramente dominante e os demais menores e de outro tipo; um accent por gráfico; stat card = label + número + variação com referência, sem decoração; tamanhos variados no grid; estados de hover/focus dentro da paleta e focus ring visível.
8. **Visuais** — remover filler decorativo; landing ganha visual que mostra algo verdadeiro (cena do mundo ou preview do produto em código com dados plausíveis); dashboards raramente precisam de imagem gerada; gerar imagem só com ferramenta disponível e aprovação antes de custo; sem ferramenta, construir em código o que der e deixar slots do tamanho certo com o prompt escrito.
9. **Motion** — remover loops sem motivo, `transition-all`, springs e hovers que deslocam muito; manter motion que explica (hover de cor/superfície, press com leve scale, menus que surgem de onde abrem, número que interpola); animar só color/background/border/opacity/transform; uma curva de easing; no máximo uma entrada no load.

## 5. Checar e reportar

- Renderizar e comparar com a lista da auditoria (limite prático: ~3 renders por rodada); o que restar da lista é corrigido.
- **Teste do template**: trocando o nome do produto por outro, a tela ainda serviria? Se sim, empurrar a direção na copy, no visual e na assinatura.
- Relatório: direção, poucas linhas por passe sobre o que mudou, prompts de imagem escritos, claims removidos ou pendentes de confirmação.

## Não fazer

- Renomear o produto ou trocar logo real (logo que é ela própria slop — emoji, sparkle em tile gradiente — é redesenhado plano).
- Mudar features, conteúdo ou ordem sem pedido; inventar features, claims ou dados.
- Substituir decoração removida por outra decoração, ou trocar uma tendência por outra (glass, grain, neon, bento).
- Repetir o mesmo visual para todo produto.

## Fora do escopo do Arsenal (componente técnico D)

O original inclui `scripts/snapshot.mjs` (cópia de site vivo via Playwright) e `scripts/story.mjs` (vídeo quadrado ~10 s da tela "se desslopando", com redlines e morph de CSS por etapas; exige Playwright + ffmpeg). Não foram importados. Para o vídeo, usar o repositório original quando houver Playwright e ffmpeg disponíveis, mantendo o crédito `unslop by @heydamir` exigido pela licença.
