---
name: scientific-hypothesis-discovery
description: "Gerar, verificar, comparar e evoluir hipóteses científicas em ciclos rastreáveis, mantendo grounding, hipóteses rivais, deduplicação, evidência acumulada e limites explícitos entre descoberta assistida e prova científica."
---

# Scientific Hypothesis Discovery

## Objetivo

Operar uma população pequena de hipóteses científicas como um processo rastreável de geração, crítica, verificação, comparação e evolução, sem transformar criatividade do modelo em evidência e sem confundir um mecanismo de busca de hipóteses com descoberta científica validada.

## Quando usar

Use quando o usuário pedir para:
- gerar e desenvolver várias hipóteses rivais sobre um fenômeno;
- explorar mecanismos causais alternativos a partir de literatura ou evidência;
- comparar hipóteses por testabilidade, grounding e poder discriminante;
- iterar hipóteses após críticas ou novas evidências;
- construir um mapa hipótese ↔ evidência antes de selecionar experimentos.

Para formular uma única pergunta de pesquisa forte, prefira `research-question-design`.
Para verificar um claim já definido, prefira `evidence-claim-verification`.
Para transformar uma hipótese madura em experimento, use `experiment-design`.

## Princípio central

**Hipótese gerada não é evidência.**

Cada hipótese deve permanecer ligada a:
- mecanismo proposto;
- claims verificáveis;
- evidência que a sustenta;
- evidência que a enfraquece;
- observação discriminante;
- incerteza residual.

## Workflow

1. **Frame**
   - definir fenômeno, população/sistema, escala, horizonte e variável de interesse;
   - separar fatos conhecidos, premissas do usuário e lacunas reais;
   - quando novidade ou literatura atual importarem, pesquisar antes de chamar algo de gap.

2. **Seed hypotheses**
   - gerar poucas hipóteses mecanisticamente distintas;
   - incluir pelo menos uma rival plausível e uma explicação mais simples quando apropriado;
   - evitar variações parafrásticas apresentadas como diversidade.

3. **Hypothesis graph**
   - para cada hipótese, decompor em claims testáveis;
   - ligar claims a evidências, contradições e dependências;
   - marcar cada aresta como `source-backed`, `inference` ou `unknown`.

4. **Grounding check**
   - verificar se citações/fontes realmente sustentam o claim exato;
   - detectar números deslocados, mudança de população, inversão de causalidade e linguagem mais forte do que a fonte;
   - claims críticos sem grounding suficiente permanecem `unknown` ou `insufficient`.

5. **Deduplicate**
   - agrupar hipóteses semanticamente equivalentes ou que só mudam redação;
   - preservar diferenças de mecanismo, boundary conditions ou previsão observável;
   - não inflar diversidade contando paráfrases.

6. **Critique / debate**
   - submeter cada hipótese às objeções mais fortes;
   - procurar explicações alternativas, confounders, mecanismos ausentes e previsões que não a distinguem das rivais;
   - crítica deve apontar uma fraqueza verificável, não apenas "ser cético".

7. **Evolve**
   - revisar hipóteses por operações explícitas, como:
     - narrowing de escopo;
     - decomposição de claim;
     - substituição de variável/mecanismo;
     - combinação apenas quando os mecanismos forem compatíveis;
     - criação de boundary conditions;
   - registrar o parent e o motivo da revisão.

8. **Compare**
   - comparar por dimensões explícitas, por exemplo:
     - grounding;
     - testabilidade;
     - capacidade de gerar previsão discriminante;
     - consistência interna;
     - valor de um resultado negativo;
     - custo/viabilidade do próximo teste;
   - não esconder julgamento em uma pontuação única quando as dimensões entrarem em trade-off.

9. **Evidence accumulation**
   - atualizar o estado de cada hipótese quando nova evidência chegar;
   - separar evidência independente de múltiplas citações do mesmo resultado;
   - fazer análise de sensibilidade quando priors ou pesos forem relevantes;
   - contradições permanecem visíveis em vez de serem "médias" até desaparecer.

10. **Select next test**
    - escolher o menor teste ou observação que mais discrimina entre hipóteses relevantes;
    - explicitar qual resultado favorece, enfraquece ou não diferencia cada hipótese;
    - encaminhar para `experiment-design` quando virar protocolo experimental.

11. **Report**
    - entregar:
      - conjunto de hipóteses;
      - mapa hipótese ↔ claims ↔ evidência;
      - principais críticas;
      - hipóteses fundidas/removidas por duplicação;
      - revisões/evoluções;
      - divergências ainda abertas;
      - próximo teste discriminante;
      - limitações.

## Regras de evidência

- Não usar fluência do modelo como prova de plausibilidade científica.
- Não declarar novidade sem busca adequada.
- Não tratar ausência de paper encontrado como evidência de inexistência.
- Não converter benchmark sintético de um método em evidência de descoberta científica real.
- Não misturar suporte direto, analogia e plausibilidade mecanística sem rotular.
- Quando a evidência for observacional, não elevar automaticamente para causalidade.

## Ranking e comparação

Métodos pairwise, Elo, Bradley–Terry ou scoring podem ser úteis em runtimes específicos, mas **não são requisito** desta skill.

Se usados:
- declarar a rubrica;
- preservar empates/incerteza;
- testar sensibilidade à ordem e ao judge;
- não tratar a posição final como verdade científica;
- manter dimensões individuais auditáveis.

## Reprodutibilidade

Quando o ambiente permitir:
- usar IDs estáveis para hipóteses, claims e evidências;
- manter artefatos/checkpoints por etapa;
- registrar versão das fontes, prompts ou critérios que mudam resultados;
- separar geração, verificação e julgamento em artefatos distintos;
- permitir replay sem reescrever silenciosamente o histórico.

## Segurança e limites

- Não executar código, modelos, instaladores ou agentes externos apenas porque a fonte original os usa.
- Não presumir acesso a bases científicas pagas, embeddings, rankers ou GPUs.
- Em temas médicos, biológicos de alto risco ou outros domínios sensíveis, elevar o padrão de evidência e respeitar as políticas aplicáveis.
- Hipóteses científicas assistidas por IA precisam de validação humana e experimental antes de qualquer conclusão substantiva.

## Integração

Combina com:
- `research-question-design`;
- `evidence-claim-verification`;
- `research-and-synthesize`;
- `experiment-design`;
- `academic-paper-orchestration`;
- `graph-engineering`;
- `verify-before-claim`.

## Provenance

Metodologia adaptada de [OpSafari/hypoarena](https://github.com/OpSafari/hypoarena), preservando a decomposição do ciclo de descoberta de hipóteses em estágios verificáveis e removendo dependências de CLI, NumPy/PyTorch, synthetic-corpus tooling, rankers e adapters de agentes que não fazem parte do runtime do ChatGPT.
