# Avaliação — 30 repositórios de decisão, forecasting, dashboards e Power BI

Data: 2026-09-23

## Escopo

Quarta leva de pesquisa do Arsenal, focada em decision making, priorização, análise causal, forecasting, métricas, dashboards e Power BI. O objetivo foi preencher lacunas transversais de análise e decisão sem duplicar owners já existentes.

## Critérios

- **A** — metodologia/capacidade que muda comportamento do Arsenal.
- **B** — boa referência para enriquecer owner existente.
- **C** — pouco ganho incremental sobre owners atuais.
- **D** — valor técnico dependente de runtime, biblioteca ou plataforma específica.

## Resultado

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 1 | quatrope/scikit-criteria | A/D | MCDA estruturado; adotar decomposição, critérios, pesos e sensibilidade em decision-analysis. |
| 2 | kotbaton/pymcdm | A/D | Forte catálogo de MCDM/weighting; usar como referência, não impor TOPSIS/AHP. |
| 3 | Valdecy/pyDecision | B/D | Repertório adicional de métodos multicritério; sem owner próprio. |
| 4 | py-why/dowhy | A/D | Causal graphs, assumptions e refutation; base para root-cause-analysis. |
| 5 | py-why/EconML | A/D | Treatment effects e causal inference com ML; incorporar disciplina causal, não toolchain. |
| 6 | py-why/causal-learn | B/D | Causal discovery; referência técnica, sem transformar descoberta estatística em prova causal. |
| 7 | Nixtla/statsforecast | A/D | Baselines, statistical models, probabilistic forecasts e cross-validation. |
| 8 | Nixtla/mlforecast | A/D | Covariates/ML forecasting; referência para modelos além dos clássicos. |
| 9 | unit8co/darts | A/D | Backtesting, ensembles e probabilistic forecasting; metodologia incorporada. |
| 10 | sktime/sktime | A/D | Framework amplo de séries temporais; referência de avaliação/comparação. |
| 11 | awslabs/gluonts | B/D | Forecast probabilístico/deep learning; técnico, não default. |
| 12 | facebook/prophet | B/D | Modelo útil para certas séries; nunca default universal. |
| 13 | apache/superset | A/D | BI exploratório e dashboards; alimentar dashboard-design. |
| 14 | metabase/metabase | A/D | Perguntas de negócio, exploração e dashboards; boa referência de self-service BI. |
| 15 | grafana/grafana | A/D | Monitoring dashboards, thresholds e drill-down; incorporar observabilidade operacional. |
| 16 | plotly/dash | A/D | Data apps interativas; referência para dashboards custom. |
| 17 | streamlit/streamlit | A/D | Data apps rápidas e interativas; owner dashboard-design, não skill separada. |
| 18 | evidence-dev/evidence | A | Relatórios code-based com SQL/Markdown; forte referência para narrativa analítica. |
| 19 | observablehq/framework | A/D | Data apps e static snapshots; referência para dashboards performáticos e narrativos. |
| 20 | PostHog/posthog | A/D | Product analytics, funnels/cohorts; base para product-metrics-diagnostics. |
| 21 | growthbook/growthbook | A/D | Experimentation + métricas; reforça separação entre trend e experimento. |
| 22 | dbt-labs/metricflow | A/D | Semantic metrics; reforça definição/ownership antes de dashboard. |
| 23 | microsoft/powerbi-desktop-samples | A/D | Fonte oficial para reports, themes e recursos Power BI. |
| 24 | microsoft/PowerBI-Developer-Samples | A/D | Embedded analytics, REST APIs e cenários app-owns/user-owns-data. |
| 25 | microsoft/PowerBI-JavaScript | A/D | Client APIs/embedding; incorporar em powerbi-engineering. |
| 26 | microsoft/Analysis-Services | A/D | Tabular modeling, ALM, partitions e best practices. |
| 27 | pbi-tools/pbi-tools | A/D | Source control e workflows maduros de projetos Power BI. |
| 28 | TabularEditor/TabularEditor | A/D | Manipulação de semantic models e scripting; tooling opcional. |
| 29 | TabularEditor/BestPracticeRules | A | Excelente modelo de checks com severity/scope/fix; incorporar auditoria de modelos. |
| 30 | sql-bi/Bravo | A/B | Model analysis, DAX formatting e date tables; referência operacional complementar. |

## Mudanças adotadas

### Novas skills
- decision-analysis
- prioritization-engine
- root-cause-analysis
- scenario-forecasting
- dashboard-design
- powerbi-engineering
- product-metrics-diagnostics

### Nova stack
- business-decision-intelligence

## Decisões de arquitetura

1. **Decision analysis != prioritization**: decisão compara alternativas e trade-offs; priorização ordena fila sob capacidade.
2. **Root cause != correlação**: mecanismos e hipóteses precisam de evidência e alternativas.
3. **Forecast != scenario != target != budget**.
4. **Dashboard design é agnóstico de ferramenta**.
5. **Power BI engineering é específico da plataforma**: semantic model, DAX, performance, themes, ALM e embedding.
6. **Métrica deve ser definida antes de ser visualizada**.
7. **Dashboard não é coleção de gráficos**: deve responder perguntas e suportar ação.
8. **Scores, forecasts e causal models expõem assumptions e sensibilidade**.

## Segurança, portabilidade e dependências

- Nenhuma biblioteca, CLI ou instalador externo foi executado para avaliação.
- Métodos MCDM e causal/forecasting foram tratados como referências técnicas; não são dependências obrigatórias.
- Ferramentas Power BI como pbi-tools, Tabular Editor, DAX Studio/Bravo e APIs só devem ser usadas quando realmente disponíveis/autorizadas.
- Credenciais, embed tokens, service principals e secrets nunca devem ser expostos em artefatos.
- Regras de Best Practice Analyzer são diagnostics, não prova isolada de qualidade.
- Benchmarks publicados por bibliotecas de forecasting não foram importados como garantias universais de velocidade ou acurácia.

## Fontes principais

- https://github.com/quatrope/scikit-criteria
- https://github.com/kotbaton/pymcdm
- https://github.com/Valdecy/pyDecision
- https://github.com/py-why/dowhy
- https://github.com/py-why/EconML
- https://github.com/py-why/causal-learn
- https://github.com/Nixtla/statsforecast
- https://github.com/Nixtla/mlforecast
- https://github.com/unit8co/darts
- https://github.com/sktime/sktime
- https://github.com/awslabs/gluonts
- https://github.com/facebook/prophet
- https://github.com/apache/superset
- https://github.com/metabase/metabase
- https://github.com/grafana/grafana
- https://github.com/plotly/dash
- https://github.com/streamlit/streamlit
- https://github.com/evidence-dev/evidence
- https://github.com/observablehq/framework
- https://github.com/PostHog/posthog
- https://github.com/growthbook/growthbook
- https://github.com/dbt-labs/metricflow
- https://github.com/microsoft/powerbi-desktop-samples
- https://github.com/microsoft/PowerBI-Developer-Samples
- https://github.com/microsoft/PowerBI-JavaScript
- https://github.com/microsoft/Analysis-Services
- https://github.com/pbi-tools/pbi-tools
- https://github.com/TabularEditor/TabularEditor
- https://github.com/TabularEditor/BestPracticeRules
- https://github.com/sql-bi/Bravo

## Veredito

A leva justificou 7 skills novas e 1 stack. O maior ganho foi criar uma cadeia entre métrica, diagnóstico, causalidade, decisão, prioridade, futuro e superfície analítica, com Power BI tratado como engenharia de dados/modelo/visual e não apenas ferramenta de gráficos.
