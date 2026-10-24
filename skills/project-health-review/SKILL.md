---
name: project-health-review
description: "Revisar saúde de projetos por evidências de entrega, marcos, dependências, bloqueios, riscos, aging e próximas ações sem esconder incerteza em uma nota única."
---

# project-health-review

## Objetivo

Produzir uma visão operacional confiável da saúde de um projeto ou portfólio e converter exceções em decisões e ações.

## Quando usar

- checkpoint semanal de projetos;
- portfolio review;
- status report executivo;
- análise de projetos em risco;
- preparação de gestão à vista.

## Dimensões

- outcome / valor esperado;
- escopo;
- cronograma e marcos;
- capacidade;
- dependências;
- bloqueios;
- riscos;
- qualidade;
- decisões pendentes;
- aging e fluxo.

## Workflow

1. Definir período, projetos cobertos e fontes.
2. Para cada projeto, confirmar outcome, próximo marco e owner.
3. Comparar plano versus evidência atual: marcos, atrasos, bloqueios, aging, dependências, mudança de escopo e capacidade. Quando houver record operacional, ler essas dimensões do mesmo sistema de execução em vez de reconstruir status manualmente.
3a. Distinguir target date, committed date, external deadline e forecast quando coexistirem; atraso contra baseline e mudança de previsão são fatos diferentes.
4. Separar fato, inferência e dado ausente.
5. Registrar riscos com probabilidade/impacto apenas quando houver base suficiente; caso contrário usar descrição qualitativa explícita.
6. Identificar decisões necessárias, dono e data-limite.
7. Se usar RAG, definir limiares antes de colorir e permitir UNKNOWN quando faltarem dados.
8. Priorizar exceções que exigem ação, não volume de atividade.
9. Produzir próximas ações com owner, prazo e condição de fechamento.
10. Comparar com revisão anterior quando houver histórico.

## Output

- resumo executivo;
- projetos/áreas que exigem atenção;
- marcos e variações;
- bloqueios e dependências;
- riscos e decisões;
- aging / fluxo;
- próximas ações;
- lacunas de dados;
- tendência desde a revisão anterior.

## Regras

- Não usar uma score única para esconder problemas de naturezas diferentes.
- Não declarar GREEN por ausência de evidência negativa.
- Atividade não substitui outcome.
- Toda cor, alerta ou conclusão precisa de regra ou evidência rastreável.
- Bad news deve aparecer cedo e com ação associada.
- Não inventar owner, ETA ou progresso percentual.

## Integração

work-delivery-flow, dashboard-design, project-planning, project-complexity-management, root-cause-analysis, scenario-forecasting e verify-before-claim.

## Origem metodológica

Adaptada de project-health e status-report patterns em borghei/Claude-Skills, alirezarezvani/claude-skills, janellecipriano/pm-skills, britt/agent-skills, KirKruglov/claude-skills-kit e travisjneuman/.claude.

## Reconciliação de capacidade e rentabilidade do portfólio (Worklenz, 2026-10-24)

Quando houver dados de tasks, timesheets, allocations e orçamento numa ferramenta de projetos, reconciliar identificadores, granularidade e períodos antes de concluir status: planned capacity vs allocated vs recorded time; budget vs actual cost vs forecast; backlog aging vs entregas aceitas; tarefas bloqueadas vs milestones em risco. Não somar horas planejadas e lançadas como se fossem a mesma métrica e não inferir lucro apenas de porcentagem concluída. Registrar owner, cliente/projeto, unidade monetária, datas de corte, fonte de custo/taxa e work in progress; expor lacunas e divergências. Ferramentas com list/board/Gantt ou dashboards são views do mesmo registro, não múltiplas provas independentes. Dados insuficientes geram UNKNOWN, não saúde verde.

Referência: https://github.com/Worklenz/worklenz . Produto externo React/Express/PostgreSQL (AGPL-3.0), com opção self-host/cloud; não instalado nem conectado aqui.
