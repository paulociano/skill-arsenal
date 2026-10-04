# Responsive Layout Engineering

## Objetivo

Aplicar responsividade como propriedade estrutural da interface, não como coleção de correções por dispositivo. O alvo é produzir componentes que se adaptem ao espaço disponível, conteúdo, preferências do usuário e capacidades do input com o menor número possível de exceções.

## Ordem de decisão

Antes de adicionar um breakpoint, tentar nesta ordem:

1. **Intrinsic layout** — deixar Grid, Flexbox, sizing intrínseco, wrapping e constraints resolverem a variação.
2. **Bounded fluid values** — usar `min()`, `max()` e `clamp()` para tipografia, spacing e dimensões que devem variar continuamente dentro de limites seguros.
3. **Container queries** — adaptar componentes ao espaço realmente disponível no container quando sua composição é reutilizável em contextos diferentes.
4. **Media queries** — usar quando a decisão realmente depende do viewport, orientação, input ou preferência do usuário.
5. **JavaScript** — reservar para comportamento que não pode ser expresso de forma confiável em CSS; não usar leitura de largura de viewport como primeira ferramenta de layout.

Essa ordem é uma heurística, não uma proibição. Um breakpoint explícito continua correto quando existe uma mudança discreta real de composição.

## Intrinsic layout

Preferir layouts que se reorganizem por restrições:

- Grid com `auto-fit`/`auto-fill`, `minmax()` e limites ligados ao conteúdo;
- Flexbox com wrapping e bases mínimas coerentes;
- `min-inline-size: 0` em children que precisam encolher sem overflow acidental;
- `max-inline-size` para controlar medida de leitura;
- `min(100%, ...)` e `max()` quando um tamanho precisa respeitar o container;
- evitar larguras fixas que assumem uma família específica de devices.

A pergunta principal não é "qual device estou atendendo?", e sim "qual restrição faz este layout deixar de funcionar?".

## Fluid sizing

Escalas fluidas funcionam melhor quando têm limites explícitos.

Exemplo:

```css
:root {
  --space-fluid-2: clamp(1rem, 2vw, 1.5rem);
  --font-fluid-2: clamp(1.5rem, 1rem + 2vw, 2.5rem);
}
```

Princípios:

- preservar `rem` ou outra componente relativa ao texto quando zoom do usuário deve continuar influenciando o resultado;
- não usar `vw` puro para texto crítico;
- limitar mínimos e máximos por legibilidade e composição, não por hábito;
- derivar poucas escalas coerentes em vez de espalhar valores fluidos independentes;
- spacing, radius e outras propriedades podem ser fluidos quando a transição contínua melhora o layout, mas não precisam ser.

RFS demonstra a utilidade de rescaling limitado para font-size, margin, padding, radius e outras propriedades. Open Props demonstra escalas reutilizáveis com `clamp()`. Utopia é uma referência útil para cálculos de type/space scales e para checar conflitos de zoom em escalas tipográficas.

## Container queries

Use container queries quando um componente precisa mudar devido ao espaço local, não ao viewport global.

Exemplos típicos:
- card usado em sidebar e conteúdo principal;
- widget que muda de linha para coluna conforme sua coluna;
- painel embutido em grids diferentes;
- componente reutilizável dentro de shells com densidades distintas.

Container queries reduzem acoplamento entre componente e página. Não as use apenas para trocar uma media query por sintaxe nova quando o owner real da decisão continua sendo o viewport.

## Media queries com intenção

Media queries continuam adequadas para:

- macrocomposição ligada ao viewport;
- orientação;
- `hover`, `pointer`, `any-hover` e características de input;
- `prefers-reduced-motion`;
- `prefers-color-scheme`;
- `prefers-contrast`, `forced-colors` e preferências equivalentes quando suportadas;
- `prefers-reduced-data` quando aplicável e suportado.

Open Props é uma boa referência para tratar preferências como tokens/custom media, mas o projeto consumidor não precisa adotar Open Props.

## Responsive media

Imagens e mídia devem participar do layout responsivo:

- usar dimensões intrínsecas ou `aspect-ratio` para reduzir layout shift;
- aplicar `max-inline-size: 100%` quando a mídia não pode exceder o container;
- preservar proporção com `height: auto` quando apropriado;
- usar `object-fit` deliberadamente para crops;
- usar `srcset`/`sizes` quando imagens responsivas reduzem custo de transferência;
- não carregar mídia grande apenas para escondê-la em viewport estreito.

## Conteúdo real é teste de responsividade

Testar:
- títulos curtos e longos;
- labels localizadas;
- números grandes;
- estados vazios, loading e error;
- listas com 1 e muitos itens;
- tabelas ou conteúdo não quebrável;
- zoom;
- fontes carregando tarde;
- imagens ausentes ou com proporções inesperadas.

Uma interface que só funciona com copy de demo ainda não é responsiva.

## Matriz mínima de runtime

Não testar apenas modelos de telefone. Cobrir restrições:

1. largura estreita;
2. largura intermediária onde o layout costuma "quebrar entre breakpoints";
3. largura ampla;
4. zoom de 200% quando a superfície é de uso geral;
5. navegação por teclado quando houver interação;
6. reduced motion quando houver animação;
7. input sem hover quando affordances dependem de hover;
8. conteúdo extremo ou localizado quando isso for plausível.

Adicionar viewports específicos do produto quando dados reais mostrarem que eles importam.

## Anti-patterns

Evitar como default:

- breakpoint por modelo de device;
- dezenas de media queries para corrigir decisões estruturais frágeis;
- JS observando `window.innerWidth` para escolher layout que CSS poderia resolver;
- esconder conteúdo relevante apenas para fazê-lo caber;
- tipografia em `vw` sem limites;
- pixels rígidos para componentes reutilizáveis sem razão;
- duplicar markup mobile/desktop apenas por estilo;
- definir breakpoints globais para componentes que deveriam responder ao próprio container;
- considerar ausência de overflow horizontal como prova suficiente de boa responsividade.

## Critério de aceitação

Uma implementação responsiva deve provar:

- composição permanece utilizável nas larguras relevantes;
- conteúdo crítico não é cortado nem sobreposto;
- reflow ocorre por regras compreensíveis e estáveis;
- zoom e preferências relevantes continuam funcionais;
- componentes reutilizáveis não dependem desnecessariamente do viewport global;
- não foram adicionados breakpoints ou JS responsivo sem necessidade observável;
- runtime foi verificado após a última mudança material.

## Provenance e referências

Metodologia refinada em 2026-10-04 a partir de:

- [twbs/rfs](https://github.com/twbs/rfs) — rescaling fluido limitado e preservação de legibilidade;
- [argyleink/open-props](https://github.com/argyleink/open-props) — fluid size/type tokens e custom media para preferências adaptativas;
- [tachyons-css/tachyons](https://github.com/tachyons-css/tachyons) — princípios mobile-first, responsividade, legibilidade e baixo peso;
- [pure-css/pure](https://github.com/pure-css/pure) — módulos CSS pequenos e responsive-by-default;
- [trys/utopia-core](https://github.com/trys/utopia-core) — cálculo de escalas fluidas de tipografia e spacing, inclusive relativas a viewport/container.

As fontes são referências metodológicas. Nenhuma biblioteca é dependência obrigatória do Arsenal ou de projetos consumidores.
