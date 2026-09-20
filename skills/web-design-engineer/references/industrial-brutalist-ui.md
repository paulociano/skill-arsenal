# Brutalismo industrial

Referência opcional para uma direção explicitamente industrial/brutalista no briefing ou nos assets. Complementa a implementação e QA da skill principal. Não presume que interfaces com dados precisem de estética militar.

## Definir o vocabulário visual

Escolha uma família dominante e registre os tokens compatíveis com a marca:

| Família | Estrutura | Tipografia | Cor e superfície |
|---|---|---|---|
| Impressão industrial suíça | Grade aparente, alinhamentos fortes, assimetria deliberada | Títulos de grande peso contrastando com dados compactos | Fundo de papel, tinta escura e acento restrito |
| Telemetria e terminal | Painéis de leitura e agrupamentos operacionais | Monoespaçada onde favorece comparar dados; títulos claramente hierárquicos | Fundo escuro, texto legível e acentos com significado |

Não alternar famílias de forma arbitrária; modos claro/escuro e exceções legítimas do produto continuam permitidos. Paletas e famílias tipográficas upstream são exemplos, não obrigação.

## Traduzir a direção em decisões

1. Organize conteúdo real em uma grade legível. Bordas e divisores devem indicar agrupamento; dados tabulares preservam semântica de tabela quando apropriado.
2. Separe escala expressiva de títulos da escala de leitura. Use tamanho fluido quando útil, teste quebras de palavras, zoom e viewport estreito. Não herde metadados de 10px, caixa alta universal ou entrelinha comprimida sem verificar leitura.
3. Use cantos retos e linhas firmes como linguagem visual, preservando affordances, estados e componentes existentes. Espaço vazio deve criar hierarquia; densidade deve facilitar comparação.
4. Mantenha acentos decorativos distintos da sinalização de erro/perigo/sucesso. Não dependa só de cor para transmitir estados.
5. Se textura for relevante, concentre retícula, grão ou scanlines em áreas decorativas. Preserve texto, controles e gráficos limpos; overlays não interceptam ponteiro e não entram na árvore de acessibilidade.
6. Use marcações técnicas somente quando representam informações reais. Não invente revisões, unidades, coordenadas ou estados de sistema para simular telemetria. Não use símbolos de marca registrada como decoração.
7. Escolha tags pelo significado real: `kbd` para entrada de teclado, `samp` para saída de programa e `output` para resultado pertinente, não apenas para aparência de terminal.

## Verificação específica

Confira contraste após os filtros, leitura em zoom, foco visível, overflow e separação entre decoração e estado operacional. Efeitos analógicos são opcionais; evite cintilação, movimento contínuo dispensável e filtros globais que prejudiquem desempenho ou legibilidade. Avalie o visual no runtime disponível, sem prometer fidelidade só pela inspeção de CSS.

## Origem e alterações

Adaptada de [Leonxlnx · industrial-brutalist-ui](https://github.com/leonxlnx/taste-skill/blob/e79ca9ec7e071eb3a3b623c4fb752e853fc3ed58/skills/brutalist-skill/SKILL.md), blob `f5375b908340e1376ed391232a31c5d82d5babfb`.

Modificação do Arsenal em 2026-09-20: referência contextual em português, com flexibilidade de marca, sem microtexto obrigatório, telemetria inventada, decoração com marcas ou proibições universais. Nenhum script ou asset importado. [Licença MIT da origem](licenses/taste-skill-MIT.txt).
