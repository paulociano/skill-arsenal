# Diagramas de stack com logos oficiais

Método para diagramas de arquitetura "estilo nuvem" — logos reais em tiles, grupos rotulados como VPCs, setas ortogonais com rótulos — a partir de uma frase como "Next.js e uma API Hono na Vercel, Postgres no Neon, auth com Clerk". Adaptado de [caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram) (MIT, commit `5af3b09`, 2026-11-09), sem exigir seus scripts, template, fontes nem a galeria pública.

## 1. Conteúdo antes do desenho

- **Nós:** cada tecnologia vira um nó com nome e um papel curto em minúsculas (`servidor http`, `banco sqlite`).
- **Grupos:** caixa em volta do que compartilha runtime, fornecedor ou repositório (provedor de nuvem contendo um runtime; um monorepo contendo o tooling). Um nível de aninhamento basta; mais vira ruído. Rótulo de grupo na grafia da marca (`GitHub`, `npm`).
- **Três tipos de aresta:**
  - cor de destaque, contínua — o fluxo principal de requisição/dados (um caminho contínuo lê melhor);
  - neutra, contínua — conexões internas secundárias;
  - neutra, tracejada — relações de dev/deploy (CI, git hooks, IaC).
- Se o usuário deu só uma lista solta de ferramentas, inferir grupos e fluxos pelo que cada uma é; perguntar só quando a ambiguidade deixaria o diagrama errado de qualquer jeito.
- "Deploy para a plataforma X", quando X é um grupo: apontar a seta para o nó mais representativo dentro do grupo e rotular a aresta (`deploy`).

## 2. Logos: oficiais e intactos

- **Nunca recolorir um logo.** Logo branco ou claro demais em tile branco vai num tile escuro; não se mexe no preenchimento. Um preenchimento branco pode ser só detalhe interno de uma marca colorida: olhar o SVG antes de trocar o tile.
- **Só marcas oficiais.** Ordem de busca do método original: svgl.app → devicon → gilbarbara/logos → arquivo do próprio projeto (`logo*.svg` na raiz, `docs/`, `assets/`, `public/`, `/logo.svg`, `/favicon.svg` do site). Bibliotecas de glifos monocromáticos redesenhados (ex.: simple-icons) ficam de fora: usuários reconhecem na hora que estão errados.
- **Conceitos abstratos ganham pictograma, não texto.** Ambiente de dev, cron, fila, cache, webhook: ícone de linha (ex.: Lucide). Nada de texto dentro de tile nem emoji. Nós genéricos (usuário, navegador, internet, dispositivo, servidor) seguem a mesma regra e podem ser tingidos com a cor do diagrama, porque não são marcas.
- **Subprodutos de um fornecedor** sem logo próprio (ex.: Cloudflare D1/R2/KV): reaproveitar o logo do fornecedor e deixar o nome do nó fazer a distinção.
- **Ícone de rótulo de grupo** aparece pequeno (~14 px): precisa de marca quadrada; wordmarks viram borrão nesse tamanho. Buscar o ícone quadrado da marca separadamente.
- **Tema escuro:** tiles continuam brancos para os logos manterem suas cores; nos rótulos de grupo (que ficam sobre o tom do grupo), usar a variante escura do logo quando existir, ou uma placa branca atrás quando a marca tiver partes pretas.
- **Crédito no rodapé** das fontes de ícones realmente usadas; logos continuam marcas de seus donos.

## 3. Nuvens com os ícones do próprio fornecedor

- **AWS, Google Cloud e Azure usam o pacote oficial de ícones de cada fornecedor**, baixado na hora; não usar cópias de terceiros (as do Google são os hexágonos aposentados que o próprio Google pede para não usar). Não versionar os pacotes nem os arquivos soltos em repositório: os fornecedores permitem uso em diagramas, mas a redistribuição não está confirmada. Azure: só em diagramas, treinamento e documentação; nunca recortar, espelhar, girar ou deformar.
- **AWS segue as regras de desenho da AWS dentro da área AWS:** ícones de serviço sem tile branco extra; grupos `AWS Cloud`, região, AZ, VPC, sub-rede pública/privada com cantos retos e só contorno; arestas numa cor com ponta aberta. Dentro de uma VPC, mostrar sub-redes pública e privada quando dá para inferir (load balancer exposto na pública; app e banco na privada) — VPC "achatada" é a primeira coisa que gente de AWS nota. Nomes completos (`Amazon S3`, `AWS Fargate`), com siglas como `ALB` na linha de papel.
- **Google Cloud:** só produtos centrais têm ícone próprio; os demais usam o ícone da categoria (Load Balancing e CDN → Networking). VPC é global e sub-rede é regional: a região vai dentro da VPC, nunca o contrário. Serviços globais/serverless (load balancer externo, Cloud Storage, Cloud Run) ficam fora da VPC. Sempre o nome completo do produto.
- **Azure:** VNet pertence a uma região, então vai dentro dela; serviços globais como Front Door ficam fora. App Service fica fora da VNet, salvo em App Service Environment; serviço PaaS via private endpoint pode ficar dentro, com papel `private endpoint`. Nome completo ao lado de cada ícone (`Azure SQL Database`, não `SQL`).
- **As regras de um fornecedor valem só dentro da área dele.** Usuário ao lado, aresta que entra na área e o resto do diagrama seguem o estilo normal.

## 4. Geometria que evita seta atravessando texto

**Um nó é o tile mais o texto abaixo dele.** Com tile de 60×60, nome e papel embaixo, o nó ocupa ~132 de largura × ~100 de altura; toda conta de ancoragem usa essa caixa.

- **Espaçamento:** ≥140 px entre centros de nós na mesma linha; 140 px entre topos de tiles de linhas consecutivas.
- **Grupos:** laterais 24 px fora da caixa de 132 px dos nós extremos (padding simétrico); topo 60 px acima do primeiro tile (faixa do rótulo); base ≥150 px abaixo do topo do último tile, para o texto ficar dentro. Grupo aninhado com recuo ≥24 px e começando ≥48 px abaixo do topo do pai. Rótulo no canto superior esquerdo, sem fundo, e nenhuma aresta nesse canto.
- **Arestas horizontais** (mesma linha): lado do tile a lado do tile, na meia altura do tile — não há texto ao lado dos tiles.
- **Arestas verticais:** da **base da caixa** do nó de cima até o **topo do tile** de baixo. Nunca da base do tile atravessando o nome.
- **Arestas em cotovelo:** segmento vertical num corredor livre de caixas de nó; segmento horizontal na faixa vazia entre linhas. Cruzar outra aresta é normal; cruzar uma caixa de nó não é.
- Deixar 4–6 px entre o fim da linha e a caixa; a ponta da seta completa o encontro.
- **Rótulos de aresta:** 1–2 palavras, com halo da cor do fundo; horizontal acima da linha, vertical à direita. O papel do nó carrega o detalhe.
- **Defesa extra:** nome e papel do nó com fundo da cor do papel, para que um cruzamento inevitável passe por trás do texto.
- **Checagem antes de desenhar:** listar cada segmento vertical/cotovelo e perguntar quais caixas de nó o corredor atravessa entre y1 e y2. A resposta tem que ser nenhuma.

## 5. Uma fonte, vários formatos

- Um **HTML autocontido** (fontes e logos embutidos como data URI, sem rede) é a fonte da verdade; PNG, componente React e artifact derivam dele.
- **PNG sempre por screenshot do HTML** num navegador headless, em escala 2×, em **tema claro e escuro**; nunca redesenhando a imagem com outra biblioteca.
- Cores e fontes atrás de variáveis CSS (tokens), não espalhadas.
- `lang` no `<html>` igual ao idioma dos rótulos; em japonês ou chinês, confirmar que o host tem a fonte certa, senão os glifos saem na variante errada.

## 6. Revisar olhando o render

Renderizar e ler a imagem antes de entregar:

- nenhuma seta atravessa texto; nenhuma ponta de seta pousa dentro de texto;
- rótulos de aresta legíveis (halo funcionando);
- todos os ícones visíveis — branco sobre branco é a falha clássica —, inclusive os rótulos de grupo no render escuro;
- rótulos de grupo no canto superior esquerdo, livres de nós e arestas; padding esquerdo e direito iguais;
- nada saindo do próprio grupo; nada cortado na borda do canvas.

Corrigir e renderizar de novo até ficar limpo.

## 7. Antes de publicar em qualquer lugar público

Diagrama de arquitetura real expõe informação interna. Antes de publicar (galeria, post, repositório público): mostrar exatamente o que vai sair, apontar hostnames, IPs, nomes de clientes, da empresa ou de serviços internos e sugerir re-renderizar sem eles; confirmar que o sistema é do usuário ou pode ser mostrado; enviar só após confirmação explícita sobre aquele conteúdo exato. Nunca preencher nome de exibição ou login a partir de configurações locais sem perguntar.
