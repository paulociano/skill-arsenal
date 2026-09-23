---
name: powerbi-engineering
description: "Projetar, construir, auditar e versionar soluções Power BI com modelo semântico, DAX, performance, temas, embedding e práticas de ALM conforme ferramentas realmente disponíveis."
---

# powerbi-engineering

## Objetivo

Tratar Power BI como produto de dados completo: ingestão/modelagem, semantic model, DAX, visual, performance, versionamento, deployment e embedding quando necessário.

## Quando usar

- PBIX/PBIP e semantic models;
- DAX e medidas;
- modelagem tabular;
- performance de relatório/modelo;
- temas e visuais;
- CI/CD/source control de Power BI;
- Power BI Embedded/API.

## Workflow

1. Definir pergunta de negócio, usuários, refresh e security requirements.
2. Inspecionar modelo:
   - facts/dimensions;
   - relationships/cardinality;
   - date table;
   - measures vs calculated columns;
   - hidden technical fields.
3. Validar definições de métricas antes de escrever DAX.
4. Preferir star schema e medidas explícitas quando apropriado.
5. Revisar DAX por correção de filter context antes de otimização.
6. Medir performance antes/depois quando ferramentas como DAX Studio estiverem disponíveis.
7. Aplicar best-practice checks quando Tabular Editor/BPA estiver disponível, tratando regras como diagnostics.
8. Projetar relatório via dashboard-design: hierarquia, comparação, drill-through, tooltips e filtros.
9. Usar theme JSON/schema para consistência quando aplicável.
10. Para source control, preferir formatos/projetos que possam ser versionados quando a stack real suportar.
11. Para embedding, separar app-owns-data vs user-owns-data e proteger credenciais/tokens.
12. Verificar refresh, RLS/security, performance e comportamento publicado antes de concluir.

## DAX e semantic model

- entender row context, filter context e context transition;
- evitar calculated columns quando medida resolve melhor e reduz modelo;
- validar grain antes de agregação;
- documentar measures críticas;
- observar cardinalidade e colunas caras;
- date/time intelligence exige calendário/modelo correto, não apenas função DAX.

## ALM e versionamento

Ferramentas como pbi-tools, PBIP, Tabular Editor e ALM Toolkit podem tornar artefatos mais diffáveis e automatizáveis. Só usar quando disponíveis/autorizadas; não executar installers externos para cumprir a skill.

## Regras

- Dashboard bonito não compensa modelo semântico errado.
- DAX que retorna número não prova que o número está correto.
- Best Practice Analyzer green não prova qualidade total.
- Performance precisa de medição.
- Source control de binário PBIX tem limitações; preferir artefatos estruturados quando suportados.
- Não expor embed tokens, service principals ou secrets.

## Integração

dashboard-design, product-metrics-diagnostics, data quality, scenario-forecasting e verify-before-claim.

## Origem metodológica

Adaptada de microsoft/powerbi-desktop-samples, PowerBI-Developer-Samples, PowerBI-JavaScript, Microsoft Analysis-Services, pbi-tools, Tabular Editor/BestPracticeRules e SQLBI Bravo. Ferramentas externas permanecem opcionais.
