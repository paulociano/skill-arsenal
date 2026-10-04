---
name: design-principles-audit
description: "Auditar decisões de design com heurísticas de percepção, cognição, comportamento, erro, hierarquia e usabilidade sem transformar princípios em checklist dogmático."
---

# design-principles-audit

## Objetivo

Usar princípios gerais de design como lentes de diagnóstico. A skill serve para explicar por que uma solução pode estar difícil de entender ou usar e para propor intervenções testáveis, sem supor que toda heurística vale igualmente em todo contexto.

## Quando usar

- revisão de interface, fluxo, formulário, navegação, apresentação ou comunicação visual;
- diagnóstico de confusão, abandono, erro ou sobrecarga;
- comparação entre duas soluções de design;
- preparação de critique estruturado antes de redesign;
- quando o problema parece envolver percepção, memória, atenção, affordance, feedback, restrições ou trade-offs.

## Workflow

1. Definir a tarefa do usuário e o comportamento desejado.
2. Identificar o sintoma observável: erro, hesitação, baixa descoberta, ambiguidade, excesso de opções, falta de feedback ou outra fricção.
3. Selecionar apenas 2–5 princípios relevantes ao sintoma.
4. Para cada princípio, registrar:
   - evidência observada;
   - mecanismo provável;
   - hipótese de melhoria;
   - risco ou trade-off.
5. Separar princípios perceptuais, cognitivos, comportamentais e sistêmicos quando isso ajudar o diagnóstico.
6. Priorizar mudanças que removem fricção estrutural antes de mudanças cosméticas.
7. Validar em runtime, protótipo ou teste quando a conclusão depender de comportamento real.
8. Não empilhar heurísticas contraditórias sem explicitar a tensão.
9. Quando um catálogo amplo ajudar a formar hipótese, pode-se usar [Growth.Design Psychology](https://growth.design/psychology) como índice de repertório. A organização por informação, significado, tempo e memória serve para descoberta, não como taxonomia científica canônica nem prova causal.

## Biblioteca de lentes

Escolher sob demanda, entre outras:

- visibilidade e feedback;
- affordance e signifiers;
- consistência e padrões;
- constraints e prevenção de erro;
- reconhecimento em vez de memória;
- progressive disclosure;
- chunking;
- hierarquia visual;
- proximidade e similaridade;
- relação figura-fundo;
- custo de decisão e número de opções;
- mapeamento entre controle e efeito;
- tolerância a erro e recuperação;
- acessibilidade e legibilidade;
- redundância multimodal quando necessária;
- familiaridade versus inovação;
- flexibilidade versus simplicidade.

## Regras

- princípio não é prova;
- nomear uma heurística não substitui observar o problema;
- não usar “lei” ou “efeito” como argumento de autoridade;
- não otimizar uma métrica local sacrificando a tarefa inteira;
- não assumir que menor número de opções é sempre melhor;
- não confundir consistência com uniformidade;
- não usar padrões de atenção como certeza sobre indivíduos.

## Saída mínima

- sintoma;
- evidência;
- princípios selecionados;
- mecanismo provável;
- intervenção proposta;
- trade-offs;
- forma de validação.

## Integração

Combina com `design-direction`, `dashboard-design`, `web-quality-audit`, `web-design-engineer`, `material-design-3` e `interaction-polish`.

## Origem metodológica

Adaptação operacional inspirada em *Princípios Universais do Design*, de William Lidwell, Kritina Holden e Jill Butler. A obra é usada como fonte conceitual; esta skill reorganiza princípios em um workflow de auditoria e não reproduz o catálogo do livro. Growth.Design Psychology entra como repertório complementar de exemplos e vieses, mantendo a regra de que princípio não substitui evidência.
