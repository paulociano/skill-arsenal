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


## Protocolo de auditoria UX por jornada (incremento 2026-10)

Usar quando a tarefa pedir auditoria de interface existente, não para redesenho sem diagnóstico solicitado. A unidade primária é **jornada + estado + evidência**, e não uma nota arbitrária.

1. **Escopo e risco:** registrar produto, público, tarefas essenciais, perfis/permissões, ambiente/versão e criticidade (maior cuidado com saúde, finanças, privacidade e ações irreversíveis). Distinguir acesso via URL navegável, código, screenshots, protótipo ou mera descrição; cada modalidade tem limites de inferência.
2. **Mapa de jornadas:** listar começo, decisão, ação, feedback e recuperação. Cobrir rotas de maior impacto e cenários alternativos (primeiro uso, usuário recorrente, fluxo interrompido), com amostragem explícita quando o produto for grande.
3. **Evidências reproduzíveis:** para cada passo inspecionado registrar URL/rota, perfil, device/viewport, estado inicial, ação, resultado esperado/observado, evidência visual/DOM/código quando disponível, hora/versão e restrições de acesso. Capturas não demonstram estados de rede, foco ou sucesso de operações.
4. **Dimensões sob demanda:** onboarding; arquitetura da informação/navegação; tarefas essenciais; entradas/formulários; status/feedback; prevenção/recuperação de erros; estados vazios/loading/erro; conteúdo e microcopy; hierarquia/layout; consistência de design system; exibição de dados; acessibilidade; responsividade; performance percebida; confiança/privacidade; padrões manipulativos. Em auditoria completa explicitar dimensões cobertas e não cobertas, sem exigir o mesmo esforço para todas.
5. **Triagem:** usar 0–4 para severidade (0 observação, 1 cosmético, 2 menor, 3 importante, 4 bloqueador/sério); classificar confiança como alta/média/baixa com base na força da evidência, separadamente de severidade. Marcar cada afirmação como norma, medição, heurística ou preferência. Não converter pesos ou percentuais arbitrários em conformidade ou certeza.
6. **Finding acionável:** `ID | jornada/passo/rota/estado | condição e viewport | esperado x observado | evidência/link/localização | impacto | categoria | severidade | confiança | critério/fonte | hipótese causal | correção concreta | trade-off | teste de aceitação | estado (PASS/FAIL/UNKNOWN/NA)`.
7. **Saída:** resumo executivo e riscos críticos; cobertura e lacunas; backlog deduplicado por prioridade (impacto, urgência, frequência, esforço/dependências sem confundir prioridade com gravidade); quick wins; recomendações estruturais; plano de reteste. Encontrar zero falhas não significa que a área não testada foi aprovada.
8. **Fechamento do ciclo:** antes de corrigir, fixar condição de teste e baseline; depois repetir mesmos passos, perfis, viewports e estados; comparar antes/depois; verificar regressões laterais e manter pendências UNKNOWN quando acesso ou ferramenta faltarem. Não atualizar baseline apenas para deixar testes verdes.
9. **Portabilidade e segurança:** não executar scripts, instaladores, automações de browser ou MCPs citados nas fontes externas por padrão. Usar somente capacidades realmente disponíveis, com autorização explícita para efeitos externos e proteção de credenciais. A inspeção visual por screenshot não equivale a testes de usuário nem prova WCAG integral.

### Gatilhos de integração

- Quando houver runtime: `runtime-ui-verification` para executar jornada, verificar consequência real e capturas comparáveis.
- Para critérios técnicos e normativos: `web-quality-audit` (WCAG 2.2 aplicável, sem substituir teste manual por axe/Lighthouse).
- Quando houver implementação: `improve-existing-web-app` para correção com preservação funcional e reteste.
- Para achados compartilhados por múltiplas páginas: `design-system-extraction` ou `design-system-governance` apenas quando a causa estiver em tokens/componentes.

### Proveniência do incremento

Metodologia adaptada, sem copiar código ou depender de runtimes terceiros:
- https://github.com/paulunemoon/ux-audit-skill — matriz de dimensões, severidade distinta de confiança e limites conforme tipo de evidência.
- https://github.com/EnchStyle/ui-ux-audit-skill — cobertura responsiva orientada a medições; não assumir Playwright disponível.
- https://github.com/scottkw/ui-audit-skill — ciclo diagnóstico/correção/reauditoria e evidências duráveis.
- https://github.com/meshcode-ai/skills-design — critérios de hierarquia, tokens e consistência visual, sem importar pontuação A–F como padrão.

## Gate de decisões genéricas de IA em UI

Ao auditar interfaces geradas com IA, evitar inferir a ferramenta criadora pela aparência. Um efeito (gradiente, glass, serif, cards, dark mode) **não é** problema por si só: examinar se a decisão é coerente com o produto, repetida sem propósito, incompatível com o sistema local ou prejudica tarefa, hierarquia ou acessibilidade.

1. Inspecionar evidência real: captura, layout e código quando disponíveis.
2. Descrever defeitos observáveis separadamente de preferências subjetivas de direção artística.
3. Aplicar teste de remoção: retirar/simplificar um elemento melhora leitura, função ou identidade sem perder informação importante?
4. Priorizar a menor correção com impacto mensurável; preservar deliberadamente identidade, tipos, cor e ritmo estabelecidos.
5. Não dar nota numérica de "AI slop" sem critérios verificáveis, nem redesenhar tudo quando foi pedida apenas auditoria.
6. Para revisão do runtime, inspecionar navegação, estados e acessibilidade; screenshot isolada não prova comportamento.

Proveniência metodológica: `MengTo/Skills`, `agent-skills/ui/audit-ai-design-slop` e `no-ai-design-slop` (2026-10-15), absorvidos como gate adicional, não skill separada.
