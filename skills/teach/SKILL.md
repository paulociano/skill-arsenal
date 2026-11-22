---
name: teach
description: "Organizar aprendizagem em múltiplas sessões com arquitetura de explicação, prática de recuperação, espaçamento e progressão por domínio demonstrado."
---

# teach

## Objetivo

Ensinar um tema ao longo de múltiplas sessões, mantendo missão, conteúdo, prática, evidência de domínio e progressão pedagógica.

## Workflow

1. Definir missão, conhecimento atual e resultado de aprendizagem. Quando o nível estiver incerto, fazer um probe curto por strands e aprofundar apenas onde a resposta discriminar conhecimento, evitando um pré-teste enciclopédico.
   - para cada strand relevante, encontrar um floor (algo que o aluno domina) e um ceiling (onde começa a falhar);
   - se tudo estiver correto, subir a dificuldade em saltos maiores até localizar a fronteira;
   - um erro isolado não prova lacuna ampla: sondar ao redor para distinguir deslize de misconception.
2. Para cada bloco, escolher o modo com explanation-architecture:
   - tutorial para aprender fazendo;
   - explanation para modelo mental;
   - how-to para tarefa;
   - reference para consulta.
3. Escolher conteúdo e prática proporcionais ao nível.
4. Ensinar com exemplos trabalhados e pedir recuperação ativa.
5. Revisitar conteúdos com spacing e interleaving.
6. Exigir evidência proporcional de domínio antes de marcos importantes.
7. Registrar progresso e próxima sessão quando autorizado.

## Fundamentos e descoberta motivada

### Fundamentos seguros primeiro

Antes de empilhar detalhes, identificar poucas afirmações simples que o aluno possa aceitar sem depender de exceções escondidas. Construir os conceitos seguintes explicitamente a partir delas.

Não chamar toda afirmação fundamental de axioma. Reserve “axioma” para uma raiz lógica real; normalmente “fundamento” ou “verdade base” é mais preciso.

### Como eu poderia ter descoberto isso?

Quando houver um caminho explicável, não apresentar a nova ideia como decreto. Reconstruir:

`problema → restrição → tentativa natural → limite/falha → nova ideia → consequência`

O objetivo é transformar fatos desconectados em uma rede derivável.

Escolher entre:
- **Socrático**: o aluno tenta produzir o próximo passo quando isso está ao alcance;
- **Expositivo**: narrar a descoberta quando o próximo passo exige conhecimento ainda indisponível.

## Princípios

- Começar pela missão.
- Diferenciar fluência imediata de retenção.
- Usar retrieval practice, spacing e interleaving.
- Ensinar dentro da zona de desenvolvimento proximal.
- Apoiar conhecimento em fontes confiáveis.
- Não usar exposição contínua quando prática seria mais útil.
- Buscar compressão conceitual: várias observações devem, quando possível, parecer consequências de poucas ideias geradoras.
- Não confundir confiança do aluno com domínio; verificar mecanismo, transferência e capacidade de derivar.
- Alternar explicação e prática conforme o tipo de conhecimento.

## Progressão por domínio demonstrado

1. Lesson / worked example.
2. Practice.
3. Review / retrieval.
4. Quiz / check.
5. Lab / project.
6. Assessment, quando necessário.
7. Progression quando a evidência corresponde ao resultado esperado.

Regras:
- não exigir todas as etapas em toda sessão;
- projeto não substitui automaticamente conhecimento conceitual;
- quiz não substitui capacidade de construir;
- avaliações testam o que foi ensinado/praticado;
- erros alimentam revisão direcionada;
- distinguir completou atividades de demonstrou domínio.

## Aprender construindo

Para engenharia/computação:
1. escolher sistema pequeno;
2. definir interface observável;
3. implementar núcleo mínimo;
4. comparar com tecnologia/testes reais;
5. explicar mecanismo aprendido;
6. aumentar fidelidade gradualmente;
7. refletir sobre abstrações visíveis e ainda ocultas.
## Ownership cognitivo ao aprender construindo

- dar ao aluno oportunidade proporcional de propor a abordagem antes de revelar a arquitetura completa;
- separar Build checkpoint (raciocínio), Design checkpoint (confirmar arquitetura) e Implementation checkpoint (autorizar edição);
- adaptar frequência e profundidade ao nível demonstrado e à preferência do aluno;
- depois da implementação, explicar mudanças, mecanismo, trade-offs e testes executados;
- requisito fornecido pelo aluno não significa aprovação automática da arquitetura sugerida.


## Quiz e checks diagnósticos

Quando usar questões:
- cada alternativa deve ser uma claim paralela em tamanho e estrutura;
- distractors devem representar misconceptions plausíveis;
- não fazer a alternativa correta se denunciar por ser mais longa, explicada ou destacada;
- feedback deve explicar o mecanismo, não apenas marcar certo/errado;
- acertar uma questão não encerra automaticamente o diagnóstico.

## Visual teaching

Quando uma relação espacial, fluxo ou comparação for difícil em texto, usar visual-explanation-sketch antes de aumentar o volume de explicação.

## Integração

explanation-architecture, eli5, visual-explanation-sketch e writing-quality.

## Referências

mattpocock/teach, build-your-own-x, TheAlgorithms, freeCodeCamp, amosblomqvist/learn e arquitetura explicativa do Arsenal. De amosblomqvist/learn foram absorvidos fundamentos seguros primeiro, descoberta motivada e probing adaptativo, removendo dependências de pi, tmux, subagents, popup UI e quiz extensions.

Origem local: teach.docx.

## Trilhas de estudo técnicas com fontes externas

Quando a missão for aprender programação, computação, engenharia ou ML de forma estruturada:
1. Partir da competência-alvo e diagnosticar pré-requisitos reais; não copiar um roadmap inteiro como plano obrigatório.
2. Construir um grafo pequeno de dependências, distinguindo fundamentos duráveis, ferramentas específicas e extensões opcionais.
3. Definir marcos com entregáveis observáveis: explicar um mecanismo, resolver um exercício novo e construir um projeto verificável.
4. Intercalar fundamentos e implementação. Para computação, usar currículos como OSSU como checklist de cobertura; usar roadmap.sh para descobrir caminhos, não como certificação de domínio.
5. Escolher materiais de leitura gratuitos via catálogos como free-programming-books, verificando idioma, acesso, licença, atualidade e adequação ao nível na fonte original.
6. Usar a prática de reconstrução de build-your-own-x e exercícios de TheAlgorithms/ML-From-Scratch como instrumentos didáticos, jamais presumindo que código antigo seja adequado à produção.
7. Revisar progresso por evidência: lacunas demonstradas, explicação sem consulta, exercícios de transferência e projeto funcionando. Ajustar sequência e espaçamento em vez de marcar tópicos vistos como aprendidos.

**Should-trigger:** criar uma trilha de seis meses para aprender backend/IA do nível atual com projetos, fontes e checkpoints.
**Near-miss:** pedido de implementar uma API agora sem intenção de aprendizagem; priorizar a skill de engenharia.

Fontes de descoberta: https://github.com/nilbuild/developer-roadmap, https://github.com/ossu/computer-science e https://github.com/EbookFoundation/free-programming-books. Links de terceiros são referências mutáveis, não conteúdo instalado ou validado automaticamente.


## Feedback matemático localizado e pistas graduais (Penmentor, 2026-10-24)

Quando o aluno enviar resolução manuscrita ou imagem de etapas matemáticas:
1. Ler o enunciado, explicitar trechos ambíguos e acompanhar cada transformação; não inferir símbolos ilegíveis como fato.
2. Identificar o primeiro erro verificável, distinguir erro originário de etapas subsequentes contaminadas e reconhecer trechos corretos.
3. Devolver feedback referenciando linha/região visual quando identificável, sem simular marcações que não foram produzidas; se houver ferramenta de edição de imagem, círculos/setas podem ser gerados de fato.
4. Oferecer pistas em escada: direção mínima → técnica pertinente → próximo passo parcial; preservar agência do aluno e só apresentar solução integral quando solicitada ou pedagogicamente necessária.
5. Checar domínio com recuperação ativa, 'encontre o erro' e escolha de técnica. Quando uma figura/simulação ajudar, conectar integral, área, derivada ou geometria ao modelo visual com limites explícitos; não afirmar interatividade Manim sem render real.
6. Verificar contas e equivalências com raciocínio independente ou ferramenta matemática disponível; separar confiança de validade do cálculo.

**Should trigger:** 'Corrija minha resolução fotografada da integral e me dê uma dica sem resolver'. **Near miss:** 'Quanto é 8 vezes 7?'.

**Origem:** https://github.com/AbdullahAlhariri/penmentor. Padrão pedagógico incorporado sem Xournal++, X11, Python, Manim ou CLI de agentes.

## Ciclo adaptativo de prática e remediação (fontes educacionais, 2026-11-21)

Quando a tarefa for tutoria, aprendizagem de idiomas ou revisão recorrente:

1. **Contrato de competência:** escolher objetivo observável, nível inicial e pré-requisitos; registrar o que conta como desempenho independente, com suporte e em transferência.
2. **Prática variada:** distinguir recuperação livre, recuperação com pista e reconhecimento; usar reconhecimento como apoio inicial, não como prova final de domínio.
3. **Revisão planejada:** distribuir recuperações ao longo do tempo, ajustando a distância ao horizonte de retenção e ao resultado real; não afirmar que exista uma curva de esquecimento individual exata ou um intervalo universal.
4. **Erro com diagnóstico:** classificar resposta incorreta como desconhecimento, confusão conceitual, falha de recuperação ou lapso; verificar essa hipótese com uma questão contrastiva curta antes de reensinar.
5. **Remediação direcionada:** explicar o mecanismo do erro, oferecer uma pista graduada e uma nova tarefa equivalente; para erros recorrentes, alternar representação textual, exemplo contextual e mnemônico autorizado pelo aluno, sem reescrever registros externos automaticamente.
6. **Roleplay por missão:** definir situação, papel do interlocutor, objetivo e nível. Oferecer modo **guiado** (pistas e traduções) ou **imersivo** (interação prioritariamente na língua-alvo); permitir saída do modo imersivo a pedido, sem bloquear a aprendizagem por regra artificial.
7. **Evidência e progressão:** registrar, quando autorizado, item/competência, erro observado, auxílio utilizado, desempenho na transferência e próxima oportunidade de revisão. Não confundir streak, XP, confiança ou quantidade de cards com domínio.
8. **Privacidade e revisão:** nunca presumir conexão com Anki, ferramentas de áudio, calendário ou memória externa; apresentar exportação ou mudanças de decks como proposta, usando somente conector realmente disponível e respeitando aprovação para escritas.

**Should-trigger:** “Monte uma trilha de francês, teste minha fala por situações e revise os itens que errei ontem.”
**Near-miss:** “Traduza esta frase para francês”; resposta pontual, sem gerar um ciclo de estudo.

**Proveniência:** metodologias abstraídas de [FreeLingo](https://github.com/artcc/freelingo), [Immersive Language Learning](https://github.com/ZackAkil/immersive-language-learning-with-live-api), [AnkiAIUtils](https://github.com/thiswillbeyourgithub/AnkiAIUtils), [Tutor-GPT](https://github.com/plastic-labs/tutor-gpt) e amostra de *retrieval-practice-generator* e *spaced-practice-scheduler* do catálogo [education-agent-skills](https://github.com/GarethManning/education-agent-skills). Não pressupõe acesso aos runtimes, modelos de perfilamento, infraestrutura de voz ou ao Anki desses projetos.

## Competência multimodal, leitura contextual e evidência multidimensional (2026-11-21)

Usar quando a aprendizagem envolver vocabulário descoberto em imagens/vídeos, documentos longos ou tutoria com vários tipos de avaliação, não para tradução pontual.

1. **Captura contextual:** extrair palavras/frases de textos, legendas fornecidas, descrições de imagens ou situações reais; preservar frase original, significado contextual, uso pragmático e grau de confiança. Distinguir tradução contextual de equivalência literal. Quando não houver acesso a áudio, vídeo, OCR ou legenda, não alegar que foram processados.
2. **Prática sob demanda:** partir dos itens que o aluno ainda não domina e oferecer definição, contraste, produção em nova frase e simulação comunicativa; não assumir domínio a partir de autoavaliação binária 'sei/não sei'.
3. **Triangulação por competência:** analisar separadamente **recuperação da memória**, **compreensão**, **organização conceitual** e **aplicação/transferência**; evidências podem vir de explicação pelo aluno (Feynman), questões inéditas, situações reais e exercícios. Não reduzir todas as dimensões a um número sem rubrica auditável.
4. **Revisão não monotônica:** manter progresso histórico, mas permitir constatar regressão ou esquecimento em avaliações posteriores. Não usar score que só aumenta como prova de domínio real.
5. **Orientação visual:** quando houver elemento interativo realmente executável, relacionar ação, hipótese e mudança observável; preferir uma visualização causal a enfeites. Se não houver runtime de interação, usar desenho estático com o mesmo raciocínio, sem simular aula ao vivo.
6. **Foco e continuidade:** escolher base documental/trecho autorizado, citar a fonte de conteúdo estudado e distinguir contexto de sessão de memória durável. Antes de exportar flashcards, registros, notas ou agendas, exigir ferramenta e permissão real.

**Should-trigger:** “Quero estudar física a partir deste PDF: me teste, faça eu explicar e mostre onde ainda não consigo aplicar.” **Near-miss:** “Qual é a tradução desta palavra?” exige resposta curta, sem painel de domínio.

**Proveniência:** [wordpecker-app](https://github.com/baturyilmaz/wordpecker-app) (aquisição contextual e vocabulário visual), [LLPlayer](https://github.com/umlx5h/LLPlayer) (legendas bilíngues e tradução contextual), [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) e [ChatTutor](https://github.com/HugeCatLab/ChatTutor) (orientação visual e manipulação de representações), [DeepTutor](https://github.com/HKUDS/DeepTutor) (workspace de aprendizagem e modos especializados), [Get It](https://github.com/beltromatti/get-it) (dimensões de domínio, com **rejeição explícita** à pontuação monotônica). Apenas metodologia; sem aplicativos, voz, players, agentes ou modelos externos instalados.
