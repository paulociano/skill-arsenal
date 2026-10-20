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
