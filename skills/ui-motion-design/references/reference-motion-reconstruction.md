# Reconstruir uma animação a partir de uma referência, com verificação medida

Método para clonar o movimento de um site, gravação de tela, vídeo, GIF ou Lottie dentro do código do usuário, provando a semelhança com números em vez de "parece certo". Adaptado de [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate) (MIT, commit `3f7a55a`, 2026-10-31), sem exigir seus scripts (Bun, Playwright, ffmpeg).

**Direitos.** Clonar o movimento serve de ponto de partida para algo próprio. Fontes, imagens, ilustrações, shaders, modelos e código de outro site continuam de seus donos: usar só o que se pode usar e trocar marca, textos e assets. Para reconstruir um produto inteiro de terceiros, usar a stack `clean-room-product-reconstruction`.

## 1. Escopo antes de capturar

Três linhas no topo de um `spec.md`:

- **Alvo:** exatamente o que clonar (URL + seletor, intervalo de tempo do vídeo, "o toggle no GIF"). Clonar só isso, não a página inteira.
- **Destino:** onde o código vai e em que stack. Ler `package.json` e os componentes existentes e usar a biblioteca de animação que o projeto já tem.
- **Fidelidade**, declarada na primeira mensagem porque decide o que se verifica:

| Nível | Quando | Precisa bater | Pode diferir |
|---|---|---|---|
| **movimento** (padrão) | "clona essa animação", "mesmo hero mas com nosso texto" | gatilho, ordem, stagger, tempo de cada passo (±80 ms), família de easing, direção e distância relativas ao tamanho, proporções do layout | textos, cores, fontes, imagens, marca |
| **pixel** | "igualzinho", "pixel-perfect", "1:1" | tudo acima + fontes, tamanhos, cores, espaçamentos, raios, sombras, assets; divergência média ≤ 2 % por quadro | só o que o usuário pediu para mudar |
| **misto** | "clona X e adiciona Y" | as partes clonadas num dos níveis acima | as adições, separadas e verificadas só por não quebrarem o movimento clonado |

Perguntar só quando duas leituras levam a trabalhos diferentes. Página com login, YouTube ou Loom que não dá para baixar: pedir uma gravação de tela e seguir com o resto.

## 2. Capturar a referência

Regra que vale para tudo: **capturar referência e clone nas mesmas condições** — mesma viewport, mesmo recorte, mesmo gatilho, mesma duração e mesmo fps. Do contrário a comparação mede a configuração, não o trabalho.

- **Site:** gravar em navegador headless numa viewport fixa; extrair as animações CSS e Web Animations declaradas (durações, delays e easings exatos) e, por quadro, posição, tamanho, opacidade e transform dos elementos que se movem.
- **Vídeo ou GIF:** extrair quadros numerados no intervalo e recorte do widget (10–30 fps), sem cursor, moldura de navegador ou ruído de compressão.
- **Canvas, WebGL, WebGPU, 3D:** pixels não bastam. Capturar com **relógio virtual** (avançado quadro a quadro, com `Math.random` semeado) para que toda captura seja idêntica e nenhum quadro caia em GPU lenta; registrar shaders, uniforms constantes, passes de render, grafo de cena e cada valor animado como curva. Ler o shader já capturado antes de escrever GLSL a partir de screenshots.
- **Lottie, Rive, export de protótipo:** o arquivo é a especificação; ler, não rederivar de pixels.

Montar folhas de quadros rotuladas com o tempo e **ler todas**, não só a primeira.

## 3. Especificação de movimento

Uma linha por elemento por propriedade: gatilho, início, duração, delay/stagger, de → para, easing, observações. Mais os fatos estáticos dos quais o movimento depende: tamanhos e posições, ordem de empilhamento, recorte por overflow, transform-origin (e, no nível pixel, fontes, cores, espaçamentos e assets).

Origem dos números, em ordem de preferência:

1. animações declaradas (CSS/Web Animations): copiar duração, delay e easing;
2. trilha de posições por quadro com ajuste de curva: delay, duração visível, overshoot e a easing nomeada que melhor se ajusta;
3. curvas de uniforms/objetos de canvas e 3D;
4. leitura de quadros: início = primeiro quadro que muda ÷ fps; duração = (último − primeiro + 1) ÷ fps. Se cobriu mais da metade da distância a 1/3 da duração, é ease-out; menos de 1/4, ease-in; simétrico, ease-in-out; passos iguais, linear; passa do ponto e volta, back/spring;
5. stagger: intervalo entre os inícios de irmãos (constante, crescente ou por caractere/palavra).

**Uma linha com "?" significa que os quadros ainda não foram lidos.** Anotar também o que **não** se move: animar algo que na referência fica parado é tão errado quanto o contrário. E procurar o que passa despercebido: fundo que esmaece, sombra que cresce, letter-spacing que aperta, blur que limpa, borda que aparece.

### Padrões que economizam rodadas

| Padrão | Sinais nos quadros | Números típicos |
|---|---|---|
| fade-up em stagger | irmãos sobem 16–48 px enquanto aparecem, cada um um pouco depois | 500–800 ms, ease-out expo/quint, stagger 60–150 ms |
| revelação de texto | linhas/palavras/letras surgem em ordem, recortadas pela própria linha | 600–1000 ms, stagger 20–50 ms por peça |
| revelação por máscara | conteúdo descoberto por uma borda, sem fade | 800–1200 ms, ease-in-out, `clip-path: inset()` |
| scale-in (modal, menu, card) | cresce de 0,9–0,96 com fade, origem no ponto de ancoragem | 150–250 ms, ease-out |
| hover lift | card sobe 2–8 px e a sombra cresce | 150–300 ms, ease-out |
| marquee | translateX contínuo de uma linha duplicada | linear, período 10–40 s — medir o período, não a easing |
| ligado ao scroll | só muda enquanto rola | função da posição de scroll, não do tempo |
| seção fixada | elemento parado enquanto a página passa | y constante num intervalo de scroll |
| parallax | camadas em frações diferentes do scroll | razões tipo 0,2 / 0,5 / 1 |
| contador / máquina de escrever | número ou caractere muda por quadro | duração + easing no valor |
| spring | passa do ponto e assenta, às vezes duas vezes | ajustar por overshoot e tempo de assentamento |
| loader / pulso | opacidade ou gradiente oscilando | período 1–2 s, ease-in-out, alternado infinito |
| transição de página | tela antiga sai, nova entra, às vezes com elemento compartilhado | 300–600 ms, saída mais curta que entrada |
| relógio de shader | canvas que nunca para (`u_time`) | taxa do relógio e o shader que a usa |
| ponteiro com atraso (WebGL) | valor perseguindo o cursor | taxa `k` em `x += (alvo − x)·k` |

## 4. Construir

Implementar na stack do usuário (CSS, Framer Motion, GSAP, three.js), mantendo a estrutura do DOM próxima dos papéis da referência para que os elementos rastreados tenham equivalentes. Adições do modo misto em componentes separados. Respeitar `prefers-reduced-motion`. Criar uma rota ou página estática que renderize o componente na mesma viewport e com o mesmo gatilho, para capturar o clone exatamente como a referência.

## 5. Verificar, corrigir, repetir

A cada rodada: capturar o clone com o mesmo comando da referência → comparar → montar folhas lado a lado (referência, clone, diferença) → comparar as curvas de cada elemento → **corrigir uma causa** → próxima rodada. Guardar os artefatos de cada rodada como prova.

**Critérios para o nível movimento** (por linha da especificação):

- erro de início, fim e duração ≤ 0,08 s;
- mesma família de easing e erro médio da curva ≤ 5 % da distância percorrida;
- ordem e intervalos de stagger dentro de 0,04 s;
- distância dentro de 10 % (relativa ao tamanho), mesma direção;
- nada se move no clone que esteja parado na referência, e vice-versa.

**Nível pixel acrescenta:** divergência média ≤ 2 %, nenhum quadro acima de 5 %, quadros em repouso ≤ 0,5 %; mesmas fontes carregadas, mesmas cores e tamanhos, mesmos assets.

**Canvas/3D:** cada canal animado da referência tem equivalente no clone, do mesmo tipo, com início e fim dentro de 0,08 s e erro médio ≤ 5 % da amplitude; mesmas configurações de renderer e estrutura de draw.

### Sintoma → causa provável

| Sintoma | Causa provável | Correção |
|---|---|---|
| tudo deslocado pelo mesmo tempo, mesma forma | latência do gatilho ou delay faltando | ajustar o delay inicial |
| clone mais curto e concentrado no início | easing agressiva demais, ou duração tirada da janela visível | usar a duração ajustada/declarada |
| termina no tempo mas começa tarde | delay longo e duração curta | corrigir os dois juntos |
| clone uniforme, referência com pico | linear ou ease-in-out onde a referência é ease-out | trocar a família |
| divergência alta em repouso | layout, fonte de fallback ou recorte diferentes | corrigir o recorte; no nível pixel, carregar a fonte |
| referência passa do ponto, clone não | bezier no lugar de spring | usar spring ou `back.out`/`elastic`, ou `linear()` amostrado |
| intervalos de stagger diferentes | conta do delay por item | `delay = base + índice × passo` |
| só os últimos quadros diferem | estado final não mantido | `fill-mode: forwards` |
| gatilho de scroll cedo ou tarde | threshold/rootMargin diferentes | igualar ao ponto de entrada medido |

### Armadilhas

- viewport ou recorte diferente entre referência e clone: consertar a captura antes de mexer no código;
- julgar pelo primeiro e último quadro: a easing está nos quadros do meio;
- página aquecida na referência e fria no clone: fazer os dois partirem do repouso;
- scroll: comparar por posição de scroll, não por segundo;
- bibliotecas JS (GSAP, springs do Framer) não desaceleram com playback rate: ajustar pelo overshoot e pelo tempo de assentamento;
- conteúdo aleatório ou A/B na referência: capturar com relógio virtual e mesma semente; medir o ruído comparando a referência com ela mesma antes de julgar o clone.

### Quando parar

Parar quando toda linha passar e as folhas mostrarem o mesmo estado no mesmo instante — e dizer isso com os números. Esperar 2–5 rodadas. Depois de 5 rodadas sem progresso numa linha, ou quando a diferença restante estiver fora de controle (licença de fonte, shader ou modelo que não se pode copiar, embed de terceiros, física aproximada), parar e reportar a linha, seus números e o motivo. **Nunca afrouxar o limite em silêncio**; se um limite mais solto for aceitável, dizer qual e por quê.

## 6. Relatório

Precisa se sustentar sozinho: nível de fidelidade, o que foi clonado e o que foi adicionado, onde está o código e como disparar o movimento, tabela da última rodada (erro de tempo, divergência média e pior quadro, easing referência → clone, passou/falhou por elemento), caminhos das folhas de comparação e desvios residuais com número e motivo.

```markdown
## Verificação (rodada N de M)
| elemento / propriedade | erro de tempo (início/fim/dur) | easing (ref → clone) | divergência média / pior | resultado |
| h1 translateY+opacity | +0,00 / −0,04 / −0,04 s | easeOutExpo 700 → easeOutExpo 700 | 0,3 % / 1,1 % | passou |
Residuais: <nenhum | linha, números, motivo>
```

Se só houve inspeção de screenshots, não afirmar que o movimento foi verificado.
