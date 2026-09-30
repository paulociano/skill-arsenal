# Avaliação — AI Workspace / Creative Operating System

Data: 2026-09-30

## Pergunta
Os padrões encontrados nas rodadas de canvas, generative UI, agentes, artifacts e knowledge work justificam uma nova capability no Arsenal?

## Fontes aprofundadas
- joyedz/melda
- miurla/morphic
- harishkotra/pixel-council
- jack112806/FrameForge

## Resultado
**A — fluxo realmente útil, materializado como stack.**

Não foi criada uma skill AI Workspace, porque os owners funcionais já existem. O valor incremental está na ordem e no contrato entre eles.

## Padrão recorrente observado
1. manter record persistente;
2. representar fontes/assets/decisões/relations;
3. recuperar contexto seletivamente;
4. executar geração/decisão/workflow;
5. materializar resultado;
6. verificar;
7. persistir mudança;
8. retomar pela frontier.

Forma compacta: capture → structure → focus → work → materialize → verify → persist → resume

## Por que stack
O fluxo cruza owners existentes: kb-retriever, handoff, wayfinder, structured-output-contract, verify-before-claim, multi-agent-orchestration, graph-engineering, domain-modeling e owners de artifacts conforme output. Criar uma skill monolítica duplicaria essas responsabilidades.

## Novidade incremental
A stack torna explícitos quatro contratos antes dispersos: workspace/record separado da interface; context pack seletivo por tarefa; artifact importante retorna ao record; retomada parte da frontier, não do histórico bruto do chat.

## Fontes
### joyedz/melda
Session Context Graph compartilhado por agent, canvas e workflow. Nodes/assets/groups/references e context packing tornam o canvas uma view operacional do contexto.

### miurla/morphic
Generative UI por streamed structured spec reforça que a forma da resposta pode ser dinâmica sem liberar geração arbitrária de código.

### harishkotra/pixel-council
Representa agentes, conexões, outputs e audit logs em um workspace espacial. Valor metodológico: tornar estado/fluxo observável. Pixel avatars e stack gráfica são detalhes de produto, não capability do Arsenal.

### jack112806/FrameForge
Pipeline criativo trata Scene Graph/asset records como fonte estruturada, prompts como requests efêmeros, assets como versões/IDs/approvals e revisão como rollback localizado ao owner. Reforça separação entre record, generation request e accepted artifact.

## Guardrails
- canvas não é truth;
- chat não é database;
- prompt não é canonical artifact;
- agent persona não substitui ownership;
- generated não significa approved;
- spatial proximity não significa semantic relation;
- self-hosted não significa automaticamente private;
- external action continua sujeita a permission boundary;
- nenhuma capability de runtime é presumida sem ferramenta real.

## Materialização
Criada: stacks/ai-workspace-operating-cycle/STACK.md
Indexada em: ARSENAL INDEX.md

## Segurança e execução
Nenhum projeto externo foi instalado ou executado. Nenhuma API key, provider, daemon, Docker stack, model runtime ou agent runtime foi ativado.