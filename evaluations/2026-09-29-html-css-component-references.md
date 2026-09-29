# Avaliação — referências HTML/CSS

Data: 2026-09-29.
Escopo autorizado: incorporar a pesquisa de 20 fontes ao Arsenal.

## Decisão e ownership

Todas as 20 fontes listadas em [catálogo HTML/CSS](../skills/web-design-engineer/references/html-css-component-references.md) recebem KEEP_EXTERNAL_REFERENCE. Classe D para código/tooling; geradores e catálogos são referências externas, não Agent Skills. Nenhuma instalação.

UPDATE_EXISTING: web-design-engineer passa a rotear projetos HTML/CSS para o catálogo; creative-web-effects aponta aos efeitos CSS. Não criar skill por biblioteca: os owners já cobrem construção, efeitos e validação. Nomes/descriptions preservados, portanto índice não requer alteração.

## Valor incremental

O lote anterior era concentrado em frameworks de componentes e shaders. Este acrescenta CSS copiável, keyframes, tokens, frameworks CSS e temas, com distinção explícita entre build, estilos e comportamento. Pico/Bulma/Pure são alternativas, não uma combinação padrão; daisyUI e Bulmaswatch dependem do contexto do projeto.

## Segurança e portabilidade

Revisão documental proporcional: nenhuma execução de scripts, instalador, hook, credencial ou alteração de projeto consumidor. Licenças não foram auditadas integralmente; confirmar por versão/item antes de copiar. Evitar CDN obrigatório em HTML offline, conflitos de resets, informação oculta em hover e controles sem semântica. Não afirmar desempenho ou acessibilidade sem runtime.

## Adotado e descartado

Adotado: catálogo das 20 fontes e critérios de seleção, mais roteamento nos owners existentes.
Descartado: importação de catálogos inteiros, instalação automática, nova skill/stack redundante e prescrição universal de estética.

## Aceitação

Should-trigger: pedido de componentes/efeitos para HTML estático ou CSS sem framework JS.
Near-miss: app React existente não exige migração para CSS framework.
Verificação de publicação: reler todos os arquivos alterados, preservar frontmatter, validar destinos internos e exatamente 20 entradas. Testes de navegador ficam para adoção em projeto real.
