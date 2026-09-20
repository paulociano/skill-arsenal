# Estrutura antes do tema

Adaptação seletiva de Hallmark. Usar em página nova, redesign de composição ou comparação de direções. Não impõe tema, estilo editorial, rotação automática ou catálogo externo.

## Escopo primeiro

Identifique o pedido: construir, auditar, redesenhar ou estudar referência. Auditoria entrega achados; redesign altera somente o escopo autorizado. Estudo extrai decisões observadas, inferidas e desconhecidas. Um componente isolado herda tokens e convenções existentes, sem criar hero, rodapé ou sistema visual novo.

Leia o contexto já fornecido antes de perguntar. Se objetivo, público e restrições estiverem claros, prossiga. Dependência instalada não comprova comportamento ativo; confirme seu uso no código/runtime.

## Selecionar composição pela tarefa

1. Identifique a ação principal e o conteúdo realmente disponível: demonstração, catálogo, narrativa, comparação, casos, dados ou documentação.
2. Escolha uma estrutura que facilite essa ação antes de escolher paleta e fontes. Exemplos: catálogo para comparar itens; demonstração para experimentar ferramenta; documento para leitura progressiva; portfolio para explorar trabalhos; narrativa para explicar transformação.
3. Registre em uma frase por que a estrutura serve à tarefa. Se houver dúvida material, contraste poucas alternativas realmente distintas. Não peça escolha adicional por regra quando já há direção suficiente.
4. Defina as relações necessárias: posição dos títulos, composição do corpo, separação de seções, forma da ação principal, função das imagens e comportamento de revelação. Esses são eixos de comparação, não seis decisões obrigatórias para todo componente.
5. Faça um mapa de seções com propósito, conteúdo real e próxima ação. Ajuste quantidade e ordem ao conteúdo; não preencha uma quota de seções ou provas inexistentes.
6. Aplique os tokens do sistema vigente à estrutura. Dentro do mesmo produto, consistência prevalece sobre variar entre execuções. Variedade entre projetos só é útil quando os briefs diferem.

## Construção e revisão

- Preserve rotas, dados, lógica, contratos de componentes e diretivas de entrada de CSS. Faça edições localizadas; não imponha CSS somente por acréscimo se isso acumular regras contraditórias.
- Uma biblioteca de temas é referência opcional. Não criar automaticamente um segundo arquivo de tokens, exports para frameworks não usados ou histórico oculto de escolhas.
- Verifique estados pertinentes à função: foco, hover quando disponível, ativo, desabilitado, carregando, vazio, erro e sucesso conforme aplicáveis. Não inventar estados de sucesso/erro para todo elemento nem tratar classes de demonstração como prova de comportamento.
- Teste largura estreita, conteúdo longo, zoom e layout amplo quando relevantes. Resolva a origem de overflow; ocultar ou recortar o documento pode esconder conteúdo e foco.
- Separe defeitos observáveis, inadequação ao briefing e preferência estética. Não certificar qualidade por notas subjetivas ou por contagem de regras.
- Uma fonte carregada no CSS não é prova de que aparece no elemento; em análise de referência, prefira estilo computado e observação visual quando disponíveis. Identificação por screenshot permanece estimativa.

## Entrega

Explique escolha estrutural, mudanças realizadas e evidência obtida. Registre decisões no design system que o projeto já usa quando necessário; não crie checkpoints de confirmação nem arquivos de memória obrigatórios.

## Fonte e alterações

[Hallmark](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/SKILL.md), especialmente `references/structure.md` e `references/contract.md`.

Modificação do Arsenal em 2026-09-20: síntese em português; removidas perguntas universais, rotação obrigatória de tema/navegação, oito estados indiscriminados, recorte global para mascarar overflow, scores de gosto e dependências de ferramentas específicas. Nenhum catálogo, asset ou script foi importado. [Licença MIT da origem](licenses/hallmark-MIT.txt).
