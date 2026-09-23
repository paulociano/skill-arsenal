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
3. Comparar plano versus evidência atual: marcos, atrasos, bloqueios, aging, dependências, mudança de escopo e capacidade.
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

dashboard-design, project-planning, project-complexity-management, root-cause-analysis, scenario-forecasting e verify-before-claim.

## Origem metodológica

Adaptada de project-health e status-report patterns em borghei/Claude-Skills, alirezarezvani/claude-skills, janellecipriano/pm-skills, britt/agent-skills, KirKruglov/claude-skills-kit e travisjneuman/.claude.
