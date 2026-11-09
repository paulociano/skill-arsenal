# Direção de filme de lançamento de produto

Método de direção para transformar "faça um vídeo do meu produto" num filme específico, que só poderia ser sobre aquele produto. Adaptado de [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion) (MIT, v0.3.1, 2026-10-22), sem depender do CLI `om`, do estúdio, da biblioteca de sons ou de GSAP. Os números citados são medições do autor em filmes de lançamento de 2026-09/10; tratar como defaults, não leis.

## 1. Ler o produto antes de perguntar

Anotar uma linha para cada item, com a evidência:

- **O que é** e a categoria (dev tool, app de consumo, modelo de IA, hardware, serviço).
- **A única coisa** que o filme precisa deixar na cabeça de quem assiste. Se o usuário não disse, propor.
- **Personalidade** nos cinco eixos (§3), lida no tipo, nas cores e no texto do próprio produto.
- **Material real** coletado antes de desenhar qualquer coisa: logo original (nunca redesenhado), telas, cores e fontes declaradas, números com fonte, gravações. Executar o produto quando possível e capturar as telas com dados reais. Registrar origem e licença de cada imagem num `materials.md`.
- **Onde vai passar:** feed (autoplay mudo, 16:9 ou 1:1), Reels/Shorts (9:16 com legenda), hero de landing page (loop sem som), palco/keynote, GIF de README.
- **Material dominante:** código, CG, filmagem, gravação de tela ou mistura. Material muda o filme mais do que linguagem.
- **Pessoas:** nenhuma, só mãos, picture-in-picture ou em cena; quem fala.
- **Modo de som:** precisa ler sem som, ou é guiado pelo som.

Capturas de tela de máquinas reais podem mostrar dados privados: mascarar, recortar ou perguntar.

Perguntar só o que não dá para descobrir, numa única mensagem com os defaults já escritos, para o usuário corrigir linha a linha. Pedido de uma linha ("faz um vídeo do produto") é o caso em que o filme costuma sair com cara de slides: fazer a leitura sozinho e oferecer as 3–4 decisões que mais mudam o filme (onde passa e duração, energia, narração), cada uma com default e duas alternativas nomeadas por referências reconhecíveis (ex.: "keynote da Apple com cortes rápidos", "changelog do Linear em plano contínuo"). **Sempre fechar a narração:** nenhuma, voz sintética lendo roteiro, gravação do usuário, ou o som do próprio material.

## 2. Forma da mensagem → linguagem de motion

A forma da mensagem decide a linguagem muito mais do que a categoria do produto.

| Forma | Soa como | Linguagens naturais | Escolha errada |
|---|---|---|---|
| Afirmação / sensação | "Apresentando X." | tipografia cinética, campo generativo, objeto 3D, vinheta de marca | tour pela interface |
| Fluxo de trabalho | "Digite isto, receba aquilo." | demo com cursor, morph contínuo | formas abstratas sem o produto |
| Mecanismo | "Por que funciona." | mecanismo, diagrama de sistema, mundo flat | montagem de cortes rápidos |
| Evidência | "As inscrições dobraram." | data story, colagem editorial | números passando ilegíveis |
| Lista | "Cinco novidades." | capítulos tipográficos, grade modular, montagem de cards, um objeto que vira cada item | cinco slides iguais |
| Transformação | "Antes / depois." | morph contínuo, comparação dividida | corte seco entre duas imagens paradas |
| História | "Um pequeno agente acorda…" | apresentador, foto, personagem, mundo flat, desenho à mão | bullet points |
| Showcase | "Veja o que ele faz." | um artefato feito a fundo; showreel com espinha única | lista de features |

Um filme pode ter duas formas (abertura em história → meio em fluxo → fecho em afirmação). Trocar de linguagem só quando a troca significa algo.

## 3. Personalidade em cinco eixos (−2 … +2)

| Eixo | −2 | +2 | O que move |
|---|---|---|---|
| preciso ↔ brincalhão | Linear, Stripe | Duolingo, Figma | easing (ease-out duro → springs com overshoot), forma (grades → blobs) |
| calmo ↔ energético | Notion, apps de meditação | games, esportes | andamento, duração do plano, densidade de cortes |
| premium ↔ acessível | Apple, Leica | Canva, utilitários | espaço negativo, contraste de escala tipográfica, número de cores |
| técnico ↔ humano | CLIs, infra | social, saúde, infantil | monoespaçada/código/diagramas vs fotos, rostos, desenho à mão |
| estabelecido ↔ novo | bancos, enterprise | startups, betas | contenção e continuidade vs ousadia e surpresa |

Fechar numa frase ("Preciso, calmo, premium, técnico, novo — tipo Linear"). Essa frase é o brief de todas as escolhas seguintes.

**Energia de lançamento.** O que fez filmes de lançamento parecerem "cool" não foi andamento alto (mediana ~105 BPM), e sim **corte**: um corte a cada 1,8–3,5 s e, na maioria, uma rajada de 5–8 cortes dentro de 5 s. Default para lançamento: 100–125 BPM, primeiro corte ou evento em até 3 s, uma subida e uma rajada entre 30 % e 60 % da duração. A calma da marca define o visual (paleta, tipo, easing), não a energia. Ir para o calmo só quando pedido, ou em loop/vinheta ambiente.

## 4. Três direções realmente diferentes

Sem estilo escolhido pelo usuário, propor três direções sobre o mesmo conteúdo, diferentes em **linguagem ou material**, não só em cor:

- **A · Encaixe** — a linguagem que a forma da mensagem e a personalidade indicam.
- **B · Amplificar** — a mesma mensagem empurrada: plano contínuo em vez de cenas, tipografia como protagonista, mundo 3D em vez de flat.
- **C · Inesperada** — outra linguagem que ainda carrega a mensagem e serve à marca (o filme é o próprio output do produto; um mundo cotidiano que se desdobra na interface; um loop desenhado à mão).
- **Exatamente uma** das três é uma direção de profundidade (interface em camadas no espaço, produto como objeto em estúdio). As outras duas não têm 3D como ideia. Recomendar profundidade para lançamento premium, objeto físico ou interface com camadas; outra linguagem para frase, lista, changelog ou mecanismo.
- Nunca três direções calmas: em lançamento, todas têm batida, e uma é a versão rápida, guiada por montagem.

Para cada direção, renderizar **um quadro-chave real** em resolução final (não descrição, não wireframe) e um cartão:

```
A · <nome>     linguagem: <id> (+ técnicas)     visual: <tipo, material, luz>
Paleta:        <papel #hex proporção · …> — de onde veio cada cor
Logline:       <o filme numa frase, com o gancho e o final>
Por que serve: <forma da mensagem + frase de personalidade → esta escolha>
Sensação:      <rota (contínua / montagem / híbrida), BPM, eventos por compasso, o que os 3 primeiros segundos mostram sem som>
Risco:         <o que pode fazer falhar>
```

As três usam a **paleta do próprio produto** de formas diferentes; não inventar cores novas. Nomear direções por referência real, nunca por adjetivo ("premium moderno"). Música não vai no cartão: escolher depois, a partir do caráter do produto. Usuários misturam por camada ("composição da C com a sensação da B"), então manter paleta, visual e ritmo como linhas recombináveis. Se o usuário disser "só faz", escolher A, dizer por quê em uma linha e oferecer B e C na entrega.

## 5. Tratamento antes do build

Nenhum build completo antes de existir o tratamento:

1. **Folha de ritmo e mapa de batidas.** Escolher a rota: *contínua* (um mundo, poucos cortes, um objeto carregado de cena a cena), *montagem* (muitos cortes, cada um na batida) ou *híbrida* (espinha contínua aberta por rajadas de montagem na virada e no pico — o padrão de lançamentos que devem parecer tech). Desenhar a curva de energia por trecho, onde fica a rajada e o momento herói. Uma linha por evento: `compasso.tempo | tempo | o que acontece | movimento | som`. O momento herói cai no ponto musical mais forte.
2. **Quatro stills reais:** gancho, momento herói, quadro mais denso, cartela final. Se um still não funciona como pôster, o filme também não funciona.
3. **Cadeia de continuidade:** uma linha por transição dizendo qual objeto ou cor leva o olho de um plano ao próximo. Transição sem nada carregado é corte; manter só se o corte for o ponto. Cenas que se substituem sem nada carregado leem como slides.

Mostrar ao usuário antes do build quando o filme passar de ~15 s ou o usuário for exigente com gosto.

## 6. Regras de gosto para o filme inteiro

1. **Começar em movimento.** O quadro 0 é o pôster que feeds e players mostram: o assunto já está nele. Nunca tela em branco, quadro preto ou um objeto solitário surgindo num fundo escuro vazio (lê como protetor de tela).
2. **Rota escolhida de propósito;** todo corte é carregado ou cai na batida.
3. **A energia tem forma:** gancho em até 3 s, uma rajada, o maior reveal no ponto mais forte. Filme na mesma energia do início ao fim é chato, por melhor que seja cada quadro.
4. **Produto real.** A interface e o texto verdadeiros: captura limpa ou, quando precisa se mover, reconstrução em código traçada sobre a captura, no mesmo tamanho, comparada lado a lado. Nunca caixas cinza, nunca interface inventada, nunca placeholder onde vai foto ou avatar. Nunca uma captura sendo panoramizada.
5. **Craft aparece no repouso.** Todo hold é um pôster: tipografia real com contraste de peso, um acento, nada de fonte padrão.
6. **Som:** filmes longos e com pessoas são guiados pelo som; filmes curtos de UI e loops precisam ler sem som. Um impacto sonoro em cada pouso que importa (~8–15 por 30 s). Masters sociais em −14 LUFS.
7. **Terminar certo:** lançamento termina na marca; showcase, lista ou loop volta ao primeiro quadro.
8. **Dar algo para guardar:** salvamentos vieram de coisas reutilizáveis (lista nomeada, prompt na tela, specs rotuladas); filmes só de clima ganharam likes e poucos salvamentos.
9. **Não é template:** se o filme ficaria igual com o nome de outro produto, falhou. Dizer como o visual difere do "estilo da casa" que todo agente produz.
10. **A mudança explica:** cada plano tem um verbo (juntar, separar, alinhar, conectar, filtrar, revelar); decoração que não explica é ruído.

## 7. Revisão: as notas que o usuário daria

Antes de mostrar a primeira versão completa, assistir em velocidade normal (ou pedir a um agente separado que assista sem contexto) e escrever as três notas que um diretor exigente daria. As mais frequentes: chato (mesma energia, sem rajada, sem pausa); a abertura não é uma ideia forte; visualmente pobre (um fundo e uma cor de linha no filme inteiro); fontes ruins ou texto sobre a interface; nada que só poderia ser deste produto.

O revisor independente recebe só o pedido original, o arquivo final, a direção aprovada, o tratamento e uma tabela de **origem de cada texto na tela** (qual captura ou página). Sem essa tabela, o revisor confunde texto oficial com texto inventado. A revisão sempre pergunta: "em que trecho a atenção começa a cair?" — revisão que só procura erro não pega o tédio, que é o motivo mais comum de rejeição.

Separar aceite técnico de aceite artístico: determinismo e testes passando não provam que ficou bom. Só checar screenshots não autoriza dizer que o movimento foi revisado.

## 8. Ciclo de ajustes por apontamento

Quando o usuário aponta um ponto do quadro (comentário com tempo e elemento):

- olhar o quadro e o recorte apontado antes de mexer;
- mudar **exatamente ali e naquele tempo**, mantendo todo o resto; se uma variável cobre o caso, mudar só a variável;
- pedidos de tempo ("segura mais um pouco") empurram o que vem depois; manter os momentos seguintes ancorados aos mesmos eventos;
- se for ambíguo, escolher a leitura mais sensata, fazer e dizer qual leitura foi usada;
- fechar com uma linha no idioma do usuário dizendo o que mudou (ex.: "título segura 1,2 s → 2,0 s; o resto empurrado 0,8 s");
- nunca reformatar o arquivo nem renomear identificadores estáveis.

## 9. Contrato de composição editável

Para que o filme continue editável sem o autor:

- títulos, números, cores, dados e durações de hold como **variáveis declaradas** da composição, ligadas ao texto e ao CSS;
- **identificador estável** em todo elemento que alguém possa apontar;
- cenas como **rótulos na timeline** (`scene:intro`), que também servem de seções da música;
- som **declarado na timeline** (impacto no mesmo tempo do pouso), regenerado a partir dela, nunca editado à mão;
- tudo função do tempo: sem relógio do sistema, sem aleatório sem semente, sem rede; fontes e bibliotecas dentro do projeto;
- animar `transform` (x, y, escala, rotação), nunca `left/top/width`;
- comprimento derivado da timeline, salvo quando a entrega exige duração fixa.

## 10. Aprendizado entre filmes

Registrar o que cada filme ensinou, em três tipos que nunca se misturam: **preferência** (palavras do usuário, citadas; valem para ele até dizer o contrário), **observado** (visto num filme) e **verificado** (reproduzido em dois filmes ou medido). O gosto de um usuário nunca vira regra geral. Quando uma regra contradiz o filme na frente, o filme vence e a regra é corrigida. Se uma checagem automática pode pegar o problema, preferir mudar a checagem a acrescentar uma nota. Experiência nunca amplia permissões: diz como fazer, nunca que se pode publicar, gastar ou contatar alguém.
