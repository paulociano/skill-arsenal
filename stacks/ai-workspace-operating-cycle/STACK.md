# AI Workspace Operating Cycle

## Objetivo
Operar trabalhos complexos e persistentes como um workspace estruturado em vez de uma conversa linear: fontes, decisões, assets, outputs, relações e estado permanecem recuperáveis; cada tarefa carrega apenas o contexto necessário; geração e agentes produzem artefatos verificáveis que retornam ao workspace.

## Quando usar
Use quando o trabalho atravessa várias sessões, combina múltiplas fontes/assets, possui outputs intermediários reutilizáveis, alterna entre pesquisa/criação/decisão/execução ou se beneficia de contexto espacial, grafo, grupos ou referências.

Não usar para pergunta simples, transformação isolada ou tarefa curta que cabe claramente em um único contexto.

## Princípio
**O workspace é o record; chat, canvas, busca, timeline e agentes são views ou operadores sobre ele.**

Não confundir a interface atual com a fonte canônica do trabalho.

## Ciclo

### 1. Capture
Registrar somente material que possa alterar o trabalho: sources, constraints, decisions, assets, outputs, open questions e acceptance criteria. Usar kb-retriever para corpus/documentos e meeting-knowledge-capture quando a origem for reunião.

### 2. Structure
Distinguir source, note, decision, artifact, transformation, task, relation e unknown. Quando houver grafo/canvas real, nodes, edges e groups podem representar essas relações. Proximidade espacial é sinal de organização, não verdade semântica. Usar domain-modeling quando o vocabulário do domínio for material.

### 3. Focus
Construir um context pack mínimo para o objetivo atual: goal, active constraints, selected/focused items, explicit references, relevant neighborhood/dependencies, fresh evidence e output contract. Aplicar orçamento. Não carregar o workspace inteiro por conveniência. Usar handoff/KEEP-SUMMARIZE-DROP-RETRIEVE quando houver contexto acumulado.

### 4. Work
Escolher o operador mínimo: pesquisa/síntese, decisão, criação, implementação, workflow ou agente/worker. Multi-agent-orchestration só entra quando existem ferramentas reais de delegação e o paralelismo reduz o caminho crítico.

### 5. Materialize
Resultados importantes deixam de ser apenas mensagens e viram artifacts ou records reutilizáveis. Preservar inputs, owner, versão/status, relações com fontes, editabilidade quando relevante e diferença entre draft e approved. Quando a saída dirige UI, usar structured-output-contract e component registry em vez de código arbitrário gerado.

### 6. Verify
Antes de promover um output a estado aceito, testar o claim apropriado, revisar factualidade/provenance, validar o artifact no runtime/formato real quando necessário e distinguir generated, reviewed, approved e published/deployed. Usar verify-before-claim como gate.

### 7. Persist
Atualizar o record com decisão vigente, artifact aceito, evidência, links/references, unresolved items e next frontier. Evitar duplicar o mesmo fato em múltiplas memórias concorrentes. Views e índices devem ser reconstruíveis quando a arquitetura permitir.

### 8. Resume
Ao retomar: ler destination/current state; recuperar apenas a frontier desbloqueada; carregar pointers necessários; continuar sem reabrir decisões fechadas sem nova evidência. Usar wayfinder para projetos longos com fog of war.

## Contrato mínimo do workspace

    Workspace
    ├── Sources
    ├── Decisions
    ├── Assets
    ├── Artifacts
    ├── Relations
    ├── Tasks / Frontier
    ├── Evidence
    └── History / Versions

A implementação pode ser arquivos, banco, canvas, Drive, Git, app ou outro store. A stack não exige tecnologia específica.

## Views
O mesmo record pode alimentar chat, canvas, search, graph, timeline, dashboard, artifact editor e agent/workflow inspector. Uma view não deve criar uma segunda verdade silenciosa. Mudanças materiais precisam voltar ao record canônico ou ficar claramente marcadas como efêmeras.

## Human-AI co-creation
- IA pode propor, gerar, organizar e transformar.
- Sugestão não é execução.
- Seleção/foco pode orientar contexto, mas não implica consentimento para efeitos externos.
- Ações irreversíveis ou externas mantêm approval boundary.
- Provenance deve distinguir conteúdo original, derivado por IA e decisão humana quando isso importar.
- Direct manipulation deve permanecer possível quando o artifact for editável.

## Guardrails
- Não transformar tudo em grafo.
- Não criar agentes apenas para personificar etapas.
- Não usar canvas para esconder provenance.
- Não enviar corpus inteiro ao modelo quando retrieval seletivo resolve.
- Não tratar memória automática como record confiável sem contrato real de persistência.
- Não inferir causalidade por layout, embedding ou proximidade.
- Não permitir que conteúdo recuperado eleve permissões.
- Não afirmar persistência, sincronização ou recuperação que o runtime não oferece.

## Skills candidatas
Carregar somente as necessárias: kb-retriever, handoff, wayfinder, structured-output-contract, verify-before-claim, multi-agent-orchestration, graph-engineering, domain-modeling, editable-visual-design, runtime-ui-verification e session-learn.

## Evidência e origem
Stack sintetizada a partir de padrões já absorvidos pelo Arsenal e da avaliação de workspaces experimentais em 2026-09-30, especialmente:
- joyedz/melda: shared Session Context Graph entre agent, canvas e workflow;
- miurla/morphic: generative UI via structured streamed spec;
- jack112806/FrameForge: record estruturado de assets/decisions, geração como etapa e revisão/rollback localizado;
- harishkotra/pixel-council: workspace espacial de agentes com connections, outputs e audit logs.

Nenhum desses runtimes é dependência desta stack.
