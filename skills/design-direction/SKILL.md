---
name: design-direction
description: "Transformar um briefing visual vago em uma direção de design explícita, específica ao produto e reutilizável antes da implementação."
---

# design-direction

## Objetivo

Resolver a direção visual antes da construção: estabelecer uma tese coerente sobre hierarquia, tipografia, cor, densidade, superfícies, composição, motion e elementos assinatura, sem inventar uma segunda identidade quando já existe sistema de marca.

## Quando usar

- briefing visual aberto ou contraditório;
- produto novo sem direção consolidada;
- redesign que precisa escolher o grau de mudança antes de codar;
- quando referências visuais existem, mas ainda não foram traduzidas em decisões;
- antes de web-design-engineer quando a estética é parte central do pedido.

## Workflow

1. Ler assets, brand guide, screenshots, design system e código existente antes de propor estilo.
2. Classificar o contexto como existing-system, partial-system ou greenfield.
3. Pesquisar referências atuais quando o pedido depende de linguagem contemporânea ou marcas específicas.
4. Extrair de 2–5 referências apenas relações úteis: estrutura, ritmo, type roles, contraste, densidade, motion, assets e elementos assinatura.
5. Escrever uma visual thesis em uma frase.
6. Definir os dials: energia, densidade, variância visual, fidelidade de marca, dependência de assets e intensidade de motion.
7. Declarar decisões concretas de tipografia, cor, grid/spacing, radius/depth, composição, motion e 1–3 signature elements.
8. Registrar o que é observed, derived e proposed.
9. Quando houver escolha real entre direções, mostrar poucas alternativas estruturalmente diferentes; não criar variantes que só trocam cor.
10. Entregar a direção para web-design-engineer, landing-craft ou design-system-governance.

## Reference grounding and taste memory

Quando houver referências visuais concretas, preferir extrair decisões observáveis delas antes de reescrever a estética como um adjetivo vago:

- separar macroestrutura, hierarquia, tipografia, paleta, densidade, shape language, motion e assets;
- usar medições determinísticas quando disponíveis para propriedades objetivas como cor/contraste, sem confundir isso com prova de qualidade estética;
- registrar decisões do projeto em um contrato persistente somente quando o ambiente realmente suportar arquivo/estado persistente;
- distinguir **project lock** de **preference memory**: o primeiro preserva consistência do produto atual; o segundo só deve promover preferências reutilizáveis após evidência repetida ou aprovação explícita;
- manter precedence clara: pedido atual > regras do projeto > decisões anteriores resolvidas > preferências gerais;
- não transformar uma preferência de um projeto em default universal.

Quando a direção ainda estiver incerta, prototipar poucas alternativas estruturalmente distintas e capturar explicitamente o que foi mantido ou rejeitado. O histórico serve como evidência de preferência, não como autoridade automática sobre o próximo projeto.

## Saída mínima

- visual thesis;
- público e tarefa principal;
- dials;
- palette logic;
- type roles;
- layout grammar;
- motion stance;
- signature elements;
- anti-patterns específicos do contexto;
- provenance das decisões.

## Regras

- Não reabrir identidade aprovada sem pedido.
- Não impor listas universais de fontes, cores ou estilos proibidos.
- Estilos nomeados como Scandinavian/Nordic/minimal devem ser tratados como direção contextual, não preset universal: preservar semântica, densidade necessária e identidade existente; remover decoração apenas quando melhora hierarquia ou tarefa.
- Referência visual é evidência, não licença para copiar marca.
- Se a mesma direção servir a qualquer produto após trocar o nome, ela ainda está genérica.
- Perguntas só são necessárias quando uma ambiguidade muda materialmente a direção; caso contrário, faça uma proposta explícita e verificável.

## Integração

Usar antes de web-design-engineer ou landing-craft quando a direção não estiver resolvida. Usar design-system-extraction antes quando um sistema já existe e precisa ser documentado.

## Origem metodológica

Síntese adaptada de dawitlabs/ui-skills, travisjneuman/.claude, Firzus/agent-skills, nolly-studio/agent-skills e AgentsORG/DESIGN, sem dependências de Claude Code, slash commands ou instaladores.

Grounding por referências, separação entre style lock do projeto e memória de preferências, e distinção entre checks objetivos e julgamento estético refinados a partir de [codeswithroh/tastemaker](https://github.com/codeswithroh/tastemaker), sem importar seus scripts, diretórios ou perfil local.

## Bibliotecas de referências

Quando precisar de fontes de inspiração, fluxos reais ou templates, consultar [bibliotecas de referências de design](references/design-reference-libraries.md). Escolher fontes pela pergunta de design e registrar exemplos específicos; distinguir conceito, screenshot, produto e template antes de derivar decisões.

## Referências premiadas com evidência de design e motion

Quando referências de sites premiados forem úteis, usar fonte observável como Awwwards (ou screenshots/DOM autorizados) para selecionar **2–5 candidatos por objetivo**, não por prestígio. Para cada candidato registrar URL, data, viewport, captura, paleta, tipografia, estrutura de seções, tecnologias observadas e o que não foi verificável. Comparar **sinais compartilhados vs. exceções** e converter em um brief com tese visual, plano de interação e evidências por decisão. Motion exige registro/captura própria: não inferir easing, duração, ScrollTrigger ou comportamento 3D de imagem estática. Investigar no máximo a estrutura e motion relevantes para o objetivo; respeitar reduced motion, teclado, touch, acessibilidade de conteúdo e custo de runtime. Não presumir que `awwwards-mcp`, índice FTS5, crawl, captura de pose 3D ou Playwright estejam instalados. Fonte: https://github.com/INSANE0777/Awwwards-mcp (avaliação 2026-10-17).

## Gate de especificidade visual e autocritica (Anthropic frontend-design, 2026-10-19)

Em projetos visuais novos ou redesenhos substanciais, executar uma checagem curta **antes de implementar**:

1. Derivar a assinatura visual do assunto, do publico, do conteudo real e da tarefa principal. O hero deve mostrar primeiro a caracteristica mais propria desse universo, podendo ser texto, imagem, demonstracao ou interacao, e nao necessariamente uma metrica com gradiente.
2. Formular em dois passes uma proposta compacta: 4–6 cores nomeadas quando fizer sentido, papeis tipograficos e escala, gramática de layout/alinhamento, wireframe textual minimo e postura de movimento. Revisar a proposta perguntando: "Se eu trocasse o nome deste produto pelo de um concorrente, esta pagina permaneceria praticamente igual?" Se sim, revisar antes de codar.
3. Testar cada marca estrutural (borda, rotulo, numero, separador e card): ela codifica hierarquia, agrupamento ou sequencia real? Numerar somente sequencias reais; evitar metadados decorativos repetidos.
4. Fazer uma **checagem de defaults gerativos** sem transformar tendencias em proibicoes: repeticao de cards identicos, sombras e raios universais, fundos escuros com acento neon sem motivo, tons creme/terracota como receita, serif editorial deslocada do dominio, caps tracking em todos os rotulos, setas ornamentais e realce isolado de uma palavra no titulo. Qualquer escolha pode permanecer quando houver razao do briefing.
5. Concentrar ousadia em um elemento principal reconhecivel; reduzir ornamentos concorrentes. Usar animacao automatica apenas para comunicar um momento intencional; preferir motion reativo a acoes e estados a revelacoes repetitivas em todas as secoes.
6. Revisar microcopy sob a perspectiva do usuario: nomear tarefas e controles de forma direta, manter verbo da acao coerente com feedback de sucesso, e tornar estados vazios e erros orientados a recuperacao.
7. Durante build, revisar conflitos de especificidade CSS e espacamento entre seletores; depois conferir mobile, foco visivel, reduced motion, contraste, conteudo longo e render real quando disponivel. Capturas isoladas nao comprovam funcionamento.

**Regra de ownership:** este gate complementa design-direction; a implementacao, a tipografia efetiva e o QA de runtime pertencem a web-design-engineer e aos owners especializados. Nao criar um novo owner frontend-design para o mesmo ciclo.

**Fonte:** https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md (consulta 2026-10-19). Metodo absorvido sem executar Claude Code, instalar plugin ou assumir screenshots/browser externos.

## Protocolo de variantes comparáveis (jakubkrehel/skills, 2026-10-26)

Quando uma decisão visual de um componente merecer exploração, criar por padrão três direções nomeadas, distintas num único eixo primário: estrutura, densidade, ênfase, tipografia ou voz. Outras alterações devem ser somente consequências do eixo, sem confundir múltiplas variáveis. Cinco variantes somente quando solicitado.

Comparar no contexto real da página, com vizinhos, tokens e conteúdo plausível; mostrar uma variante em tamanho real por vez. Quando o runtime permitir, seletor e parâmetro de URL tornam cada alternativa compartilhável. Sem runtime, indicar claramente que a comparação é estática. Toda variante deve respeitar acessibilidade (nome, foco, teclado), contraste, zoom, mobile, movimento reduzido, recuperação de erros e proteção para ações destrutivas. Rejeitar a direção que só funciona rompendo esses mínimos.

Entregar matriz neutra de nome, posição no eixo, contexto adequado e trade-off, sem predileção estética implícita. Após a seleção, promover uma direção e remover seletor, alternativas rejeitadas e código temporário, verificando o diff. Não presumir integração automática com Figma, navegador ou Claude Code.

Fonte: https://github.com/jakubkrehel/skills/tree/main/skills/variant .
