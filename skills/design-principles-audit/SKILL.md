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

## Evidência localizada e cobertura por superfície

Para auditorias de frontend existente, combinar heurística com evidência de implementação e uso:

1. Definir jornadas críticas, rotas e componentes compartilhados; incluir estados ocultos (modal, menu, erro, vazio, loading, permissão) e áreas de maior risco. Não inventar uma quantidade mínima de findings.
2. Para cada achado, registrar superfície/rota, componente, arquivo/linha ou seletor **quando observável**, viewport/estado, sintoma, princípio relevante e impacto na tarefa. Se a evidência for apenas HTML estático, sinalizar o que não foi testado em runtime.
3. Severidade 0–4 por frequência, impacto e persistência, sem converter esses fatores em precisão estatística fictícia: 1 cosmético; 2 menor; 3 importante; 4 bloqueio/erro sério. Prioridade de correção considera também risco e esforço, mas não reclassifica gravidade pelo custo.
4. Anexar correção concreta (before/after ou contrato), fonte do critério (WCAG quando normativa; heurística quando interpretativa), risco/trade-off e teste de aceitação verificável.
5. Selecionar checklist por superfície **sob demanda**: botões/CTAs, formulários, navegação, cards, tabelas, overlays e dashboards. Conferir foco/teclado, estados, overflow, conteúdo longo, zoom, mobile e contraste onde aplicável. Regras numéricas como quantidade de linhas para paginação são hipóteses contextuais, não leis universais.
6. Separar PASS, FAIL, UNKNOWN e NOT_APPLICABLE; ausência de prova não é aprovação. Não tratar screenshot, lint ou nota agregada como substitutos de teste de usuário.
7. Revisar consistência entre telas e revalidar as correções com `runtime-ui-verification` e `web-quality-audit` quando o runtime estiver acessível.

### Modelo enxuto de finding

`ID | superfície/estado | evidência + localização | impacto | severidade (0–4) | tipo (norma/heurística/preferência) | correção | critério de aceite | status de verificação`.

### Origem incremental

- mistyhx/frontend-design-audit: escala de severidade, descoberta de estados ocultos, relatório acionável e revisão posterior.
- narenkatakam/ux-audit: seleção de checklists conforme tipo de componente e modo review/guide, sem adotar proibições estéticas universais.
- tommygeoco/ui-audit: decisão orientada à tarefa, conhecimento institucional, convenções e evidência de usuário antes da escolha visual.
- Aboudjem/ui-ux-suite: evidência por arquivo/linha, valor medido e correção localizada, sem assumir sua CLI/MCP ou equivalência entre score heurístico e qualidade real.
- thedaviddias/Front-End-Checklist: consultar regras atuais, de forma seletiva, para complementar critérios normativos e revisão pré-release, sem importar seu catálogo integral.
