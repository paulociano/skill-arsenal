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

Quando existir captura ambiente:
- manter raw record separado de summaries/knowledge;
- capturar somente a superfície autorizada;
- preservar references e timestamps;
- permitir regras de exclusão/redaction;
- tratar a camada derivada como reconstruível.

### 2. Structure
Distinguir source, note, decision, artifact, transformation, task, relation e unknown. Quando houver grafo/canvas real, nodes, edges e groups podem representar essas relações. Proximidade espacial é sinal de organização, não verdade semântica. Usar domain-modeling quando o vocabulário do domínio for material.

### 3. Focus
Construir um context pack mínimo para o objetivo atual: goal, active constraints, selected/focused items, explicit references, relevant neighborhood/dependencies, fresh evidence e output contract. Aplicar orçamento. Não carregar o workspace inteiro por conveniência. Usar handoff/KEEP-SUMMARIZE-DROP-RETRIEVE quando houver contexto acumulado.

### 4. Work
Escolher o operador mínimo: pesquisa/síntese, decisão, criação, implementação, workflow ou agente/worker. Multi-agent-orchestration só entra quando existem ferramentas reais de delegação e o paralelismo reduz o caminho crítico.

Quando um trabalho recorrente precisa de estado próprio, várias ações e interface específica, considerar promovê-lo de workflow para **app/capability persistente**:
- workflow é verbo: executa uma tarefa;
- app/capability é substantivo: dá ao trabalho um lugar próprio, dados persistentes e superfícies reutilizáveis;
- ações, skills, agents, hooks, UI/API e data podem compor a mesma capability;
- a implementação deve continuar exportável/versionável quando possível.

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

## Shared human-agent workspace

Quando humanos e agentes compartilham o mesmo workspace:
- identidades de agentes devem ser próprias, não mascaradas como usuários humanos;
- mensagens, workflow steps, approvals e repo events devem compartilhar audit trail quando isso simplificar provenance;
- channel/room can become the durable record of why work happened;
- agent access should be scoped like a teammate: explicit membership, tools and credentials;
- event log can be canonical while chat/canvas/search/git views remain projections;
- approvals and consequential writes remain human-visible and attributable.

## Deictic and live-canvas interaction

Quando o runtime permitir entrada multimodal/contextual:
- voz pode carregar a intenção enquanto pointer/circle/selection aponta o referente visual;
- preservar ordem entre fala e referências capturadas;
- uma captura de tela é evidência sensível e deve ser minimizada ao necessário;
- apontar para algo não autoriza ação sobre esse algo;
- em canvas colaborativo, humanos e agentes devem ver edits/status/presence de forma atribuível;
- design memory pode registrar exemplars e decisões duráveis, mas regras propostas por distillation precisam de revisão humana.

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

block/buzz reforçou o padrão de workspace humano-agente baseado em event log auditável, identidade própria de agentes e views compartilhadas. dragthelake/ambient-context reforçou raw capture local-first separado de knowledge/summaries. rome-os/rome acrescentou o padrão workflow→app/capability persistente e compounding de ações/skills/apps em código versionável. kgoedecke/doop acrescentou canvas multiplayer humano-agente, presença e design memory. TarunTomar122/better-voice acrescentou entrada de voz com referência visual deíctica por apontamento. Nenhum desses runtimes é dependência desta stack.
