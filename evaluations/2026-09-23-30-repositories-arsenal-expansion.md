# Avaliação em lote: 30 repositórios para expansão do Arsenal

Data: 2026-09-23. Método: `evaluate-and-import-skill` + `skill-security-review`.

Objetivo: avaliar 30 candidatos encontrados como possíveis enriquecimentos do Skill Arsenal, comparar contra owners existentes, incorporar somente deltas metodológicos reais e evitar duplicação de runtimes/wrappers.

## Resultado executivo

Foram adotadas **2 novas skills** e refinados **6 owners + 2 fluxos relacionados**.

Novas skills:

- `llm-red-team-evaluation` — red teaming de aplicações GenAI autorizadas;
- `web-quality-audit` — auditoria de performance, acessibilidade e qualidade web em runtime.

Owners refinados:

- `llm-observability-evaluation`;
- `retrieval-quality-engineering`;
- `document-extraction-pipeline`;
- `code-understanding-audit`;
- `academic-paper-orchestration`;
- `session-learn`;
- stack `research-and-synthesize`;
- `runtime-ui-verification`.

Nenhum runtime externo foi instalado ou executado durante a avaliação.

## Classificação dos 30 candidatos

| # | Fonte | Revisão observada | Classe | Decisão |
|---|---|---|---|---|
| 1 | promptfoo/promptfoo | `b9048345c3e26cc417c6e6a0ef65af89c75f31b7` | A/D | absorver eval matrix, CI e red teaming; sem dependência |
| 2 | confident-ai/deepeval | `b413bb19ac364154ec3d92ccdbb60afca054dc78` | A/D | absorver métricas de trajectory/tool/task |
| 3 | explodinggradients/ragas → vibrantlabsai/ragas | `298b68274234c060deacab3cf5fb52aa3a20e885` | B/D | reforçar RAG end-to-end; não criar owner |
| 4 | Arize-ai/phoenix | `e4b8130773c7b15de11c9337d509d0eaab4883e7` | B/D | já coberto por observability owner; incorporar experimento/dataset discipline |
| 5 | comet-ml/opik | `02775d887a7713aa557b92343ccd5d1df4727766` | B/D | incorporar CI/online eval pattern |
| 6 | langfuse/langfuse | `5b59af472bbd5f8368d821b14f7a9e2a8701958c` | B/D | já é referência canônica de llm-observability-evaluation |
| 7 | openlit/openlit | `88ff0b54ab125c2a579276116c79548f1c8fd5ab` | B/D | reforça OpenTelemetry e full-agent tracing; sem nova skill |
| 8 | microsoft/pyrit | `5453025c128d36a4ac624c10097a5e85031302ec` | A/D | base forte para nova skill de red teaming |
| 9 | NVIDIA/garak | `8d1259ef310e4803cf5a4cc77267fdfdc24434ec` | A/D | probes/detectors e coverage para red teaming |
| 10 | meta-llama/PurpleLlama | `4be64c3a24442b51c76175e6ec67722cc3f5fe38` | B/D | purple-team taxonomy e benchmark discipline |
| 11 | browser-use/browser-use | `d8110c5ff87ccba887aaa726cdb780f2f84bef8d` | D | runtime; action-space pattern já coberto |
| 12 | browserbase/stagehand | `fbcdf6169e61431fc9be2ef0849c16424bc6d3bc` | B/D | incorporar observe/act/extract e isolamento de credentials |
| 13 | vercel-labs/agent-browser | `d01253d9db28d75080e36da3c1c31ef89454731e` | D | CLI/harness útil, sem metodologia nova suficiente |
| 14 | microsoft/markitdown | `b8f79c57ebc0044be41323d89b2a45d3fda8460e` | B/D | já absorvido em document-extraction-pipeline |
| 15 | docling-project/docling | `fc4aa7fb780847fde32c3b1b60780e1ddec3fd6e` | A/D | incorporar representação layout-aware e block tree |
| 16 | VikParuchuri/marker → datalab-to/marker | `8a1d2344de25d7ec4c5209133aed7af565874ff0` | A/D | já é referência do pipeline documental |
| 17 | opendatalab/MinerU | `48a92548263a919f49138d856d2581698536c474` | B/D | locators/reading order/structured blocks |
| 18 | Unstructured-IO/unstructured | `0ca5563220683953afdd47619b72a5d55ea4ddde` | B/D | preprocessing/chunking por estrutura |
| 19 | yamadashy/repomix | `4299b5838ef4013cf63b54c93208a6bbfb0f5383` | B/D | contexto de codebase com include/exclude/token budget |
| 20 | ast-grep/ast-grep | `6175e07b668b388a1a326d8fc543c4856eb5f54b` | A/D | busca estrutural por AST como degrau entre grep e análise pesada |
| 21 | semgrep/semgrep | `594a78a0589ec7a4a15feb25eb3f12d47008a28d` | A/D | static/semantic rules como linha de evidência; não oracle |
| 22 | pydantic/pydantic-ai | `06be8e7a0056d6c6c72d2868f6b26ee8e7364c77` | B/D | typed agents, evals e durable execution já distribuídos entre owners existentes |
| 23 | huggingface/smolagents | `30bb1161095dbae2271e6bc3cc4c219cc3897a57` | B/D | minimal agent abstraction + sandbox; sem novo owner |
| 24 | assafelovic/gpt-researcher | `6f998577d547b1e54ec662dac63583aa11e3b84b` | B/D | planner → research questions → gather → source-track → synthesize |
| 25 | stanford-oval/storm | `fb951af7744dab086e34962e9bc6fe878e145f83` | A/B/D | perspective-guided questions + outline-before-writing |
| 26 | Future-House/paper-qa | `57e89f7223b0960d5ee5ea048c69e3c47e088572` | A/D | metadata/retraction/contradiction discipline para pesquisa científica |
| 27 | getzep/graphiti | `16cdf7045378c8d53ae01f94e2fa60d238cb0f68` | A/D | temporal validity + provenance por episode |
| 28 | microsoft/graphrag | `82b87bf0434fc69f857663280e2c36a1c48e52fe` | B/D | metodologia útil de graph context; repo declara maintenance mode |
| 29 | w3c/aria-practices | `3f094fde1c81b25dfa69162563bf28d093f854d4` | A/B | fonte normativa/prática forte para accessibility patterns |
| 30 | GoogleChrome/lighthouse | `08c05cdee7e191719480477056bd145abcb09c17` | A/D | auditoria reproduzível de performance/accessibility/best practices |

## Deltas incorporados

### 1. Evals e observabilidade de agentes

`llm-observability-evaluation` agora explicita que agentes precisam ser avaliados por eixos separados:

- task success;
- trajectory/steps;
- tool selection;
- argument correctness;
- retrieval;
- final answer;
- safety;
- cost/latency.

Também incorpora matriz `case × version × metric`, assertions determinísticas antes de judges quando possível, datasets versionados e CI regression gates.

Fontes principais: Promptfoo, DeepEval, Phoenix, Opik, Langfuse e OpenLIT.

### 2. Nova skill: llm-red-team-evaluation

`skill-security-review` continua dono da pergunta “é seguro adotar/instalar esta skill, agente ou plugin?”.

A nova `llm-red-team-evaluation` responde outra pergunta: “como testar adversarialmente um sistema GenAI autorizado em execução?”.

Workflow incorporado:

`authorize scope → threat model → attack taxonomy → baseline → probes → detectors → bounded execution → evidence → mitigation → retest → coverage report`.

Fontes: Promptfoo, PyRIT, garak e Purple Llama.

### 3. RAG end-to-end

`retrieval-quality-engineering` agora separa:

- retriever quality;
- context quality;
- answer grounding;
- answer relevance/completeness;
- citation correctness.

RAGAS foi tratado como metodologia/ferramenta de avaliação, não como owner separado.

### 4. Documentos complexos

`document-extraction-pipeline` agora formaliza representação intermediária com:

- page;
- reading order;
- block type;
- hierarchy;
- tables/formulas/images/captions/code;
- bbox/locator;
- provenance.

Também reforça chunking orientado à estrutura antes de token budget quando necessário.

Fontes: Docling, MinerU e Unstructured. Marker e MarkItDown já estavam previamente incorporados.

### 5. Análise de codebases

`code-understanding-audit` agora usa uma escada de potência:

`text search → symbol/AST search → semantic/static analysis → manual source verification`.

Também formaliza empacotamento de contexto com include/exclude, secrets/generated/binaries boundaries, token budget e provenance.

Fontes: Repomix, ast-grep e Semgrep.

### 6. Pesquisa profunda

A stack `research-and-synthesize` agora inclui:

- subperguntas não redundantes;
- cobertura por perspectivas;
- provenance por subpergunta;
- outline baseado em evidência antes de texto longo;
- revisão do outline quando a pesquisa contradiz o plano inicial.

Fontes: GPT Researcher e STORM.

### 7. Integridade científica

`academic-paper-orchestration` agora explicita:

- status de retratação/correção quando material;
- distinção preprint/publicação/errata;
- busca de evidência contraditória;
- metadata/content/claim verification separados.

Fonte: PaperQA2.

### 8. Memória temporal

`session-learn` agora preserva:

- início/fim de validade;
- supersession;
- episode/source provenance;
- distinção event time / ingestion time / review time quando relevante.

Fonte: Graphiti.

GraphRAG foi mantido apenas como referência metodológica porque seu próprio README declara o projeto em maintenance mode.

### 9. Browser automation

`runtime-ui-verification` absorveu de Stagehand:

`observe → act → extract`

com isolamento de credentials e schema validation para extração.

Browser Use e agent-browser continuam classificados como runtimes, não owners metodológicos.

### 10. Nova skill: web-quality-audit

Criada para separar auditoria técnica de criação visual.

Cobre:

- baseline reproduzível;
- Lighthouse/equivalente quando disponível;
- HTML nativo antes de ARIA;
- keyboard/focus/name/role/state;
- lab vs field metrics;
- performance diagnosis;
- rerun sob condições equivalentes;
- findings com evidence + impact + correction + verification.

Fontes: WAI-ARIA Authoring Practices e Lighthouse.

## Candidatos sem alteração canônica própria

### Pydantic AI
Excelente runtime/SDK. Typed outputs, durable execution, capabilities, graph/evals e agent harness já possuem owners no Arsenal: `structured-output-contract`, `graph-engineering`, `loop-engineering`, `llm-observability-evaluation`, `model-routing-gateway` e `skill-security-review`.

### smolagents
A filosofia de abstração mínima é boa, mas não justifica skill. Code agents e sandboxing dependem de runtime real.

### Microsoft GraphRAG
A metodologia de graph-based context continua útil, porém o próprio projeto declara maintenance mode. Não deve virar dependência padrão.

### agent-browser
É uma ferramenta/harness. O Arsenal deve usar browser controlável realmente disponível, não criar dependência fixa.

## Segurança

A revisão foi estática/read-only.

Não foram executados:

- installers;
- pip/npm/cargo installs;
- Docker;
- scanners adversariais;
- browser agents externos;
- document models;
- code scanners;
- MCP servers;
- SaaS externos.

Runtimes de red teaming podem gerar conteúdo adversarial e fazer chamadas a modelos/alvos. A adoção metodológica não autoriza sua execução.

Document parsers e agent frameworks podem ter acesso a arquivos, rede, credentials, browsers, subprocesses ou modelos remotos. Cada uso real ainda requer grounding de versão, boundary de dados e autorização adequada.

## Estado final do Arsenal

Criadas:

- `skills/llm-red-team-evaluation/SKILL.md`;
- `skills/web-quality-audit/SKILL.md`.

Refinados:

- `skills/llm-observability-evaluation/SKILL.md`;
- `skills/retrieval-quality-engineering/SKILL.md`;
- `skills/document-extraction-pipeline/SKILL.md`;
- `skills/code-understanding-audit/SKILL.md`;
- `skills/academic-paper-orchestration/SKILL.md`;
- `skills/session-learn/SKILL.md`;
- `stacks/research-and-synthesize/STACK.md`;
- `skills/runtime-ui-verification/SKILL.md`.

Atualizado:

- `ARSENAL INDEX.md` apenas para as duas novas skills.

## Limites

A avaliação buscou metodologia e arquitetura operacional, não uma auditoria linha a linha de cada runtime. Para os repositórios técnicos classe D, a decisão “adotar metodologia” não implica “aprovar instalação”.

Os aliases históricos observados foram resolvidos pelo GitHub:

- `explodinggradients/ragas` atualmente resolve para `vibrantlabsai/ragas`;
- `VikParuchuri/marker` atualmente resolve para `datalab-to/marker`.
