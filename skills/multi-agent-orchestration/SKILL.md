---
name: multi-agent-orchestration
description: Coordenar múltiplos agentes ou workers em tarefas paralelas com isolamento, ownership explícito, contratos de entrada e saída, estados observáveis e integração centralizada, somente quando ferramentas reais de delegação estiverem disponíveis.
---

# Multi-Agent Orchestration

## Objetivo
Usar paralelismo entre agentes sem criar caos de ownership, sobreposição de edição, resultados incompatíveis ou falsa sensação de progresso.

## Quando usar
Use somente quando houver ferramentas reais para:
- iniciar workers/agentes;
- dar prompts;
- observar estado;
- recuperar resultados;
- manter isolamento de arquivos, worktrees ou áreas de responsabilidade.

Não simule multiagente quando esses recursos não existirem.

## Workflow
1. Mantenha um coordenador responsável pela integração final.
2. Separe trabalho em unidades independentes.
3. Para cada worker, defina:
   - objetivo;
   - escopo;
   - arquivos ou área de ownership;
   - inputs;
   - output esperado;
   - critério de aceitação.
4. Prefira isolamento por worktree, branch ou ownership de arquivos quando houver escrita concorrente.
5. Inicie no máximo o número de workers que realmente reduz o caminho crítico.
6. Observe estados como:
   - idle;
   - working;
   - blocked;
   - done;
   - unknown.
7. Não trate envio de prompt como prova de execução.
8. Em timeout ou estado ambíguo, inspecione antes de reenviar.
9. O coordenador revisa os resultados e resolve incompatibilidades.
10. Reexecute checks de integração no estado consolidado, não apenas nos branches individuais.
11. Em workspaces compartilhados, preferir identidade e audit trail próprios para cada agente, com membership/scopes explícitos, em vez de credenciais compartilhadas.
12. Quando chat, patch, CI, review e aprovação coexistirem, manter um record comum ou relações rastreáveis entre esses eventos.
13. Para coding agents paralelos, preferir uma unidade isolada por tarefa: branch/worktree + terminal/conversation/review state próprios.
14. Ferramentas e integrações compartilhadas podem ser configuradas uma vez, mas cada worker recebe somente o subset necessário para seu escopo.
15. Subagent delegation precisa devolver resultado ao parent/coordinator; child completion não equivale a integração concluída.
16. Papéis como explorer, researcher, worker, tester e reviewer só devem existir quando cada um tem contrato, escopo e evidência próprios; não criar personas ornamentais.
17. Separar execução de revisão: reviewer deve receber o artefato/diff e critérios, não apenas a narrativa do worker.
18. Em ambientes multi-dispositivo/headless, continuidade do workspace não autoriza controle remoto irrestrito; identidade, rede e filesystem continuam boundaries explícitos.
19. Delegação deve ser capability-routed e bounded: cada subagente recebe um deliverable concreto, não uma persona genérica.
20. Antes de delegar, fazer capability preflight; se model/effort/tool control não for observável no runtime, não fingir que foi aplicado.
21. Requested settings e runtime-observed settings devem ser reportados separadamente quando isso importar.
22. Após implementação substancial, usar reviewer fresco/read-only quando disponível; `fix-first` exige nova verificação antes de nova revisão.

## Plano de controle operacional (quando múltiplos runtimes existirem)
- Separar plano de controle (fila, atribuição, aprovação, custo, logs) dos agentes que executam; dashboard não substitui a execução nem sua evidência.
- Associar cada tarefa a identidade de agente, sessão/runtime, eventos, decisões, artefato resultante, revisão e recibo verificável de conclusão.
- Diferenciar `queued`, `claimed`, `running`, `needs-review`, `blocked`, `completed-verified` e `unknown`; evitar declarar sucesso só com log ou evento `done`.
- Monitorar orçamento de tokens/custo, falhas e filas apenas quando a telemetria for realmente fornecida.
- Exigir autorização humana para operações sensíveis, least privilege por workspace e isolamento de chaves; não expor painel alfa à rede sem endurecimento.
- Mission Control (builderz-labs) é referência de arquitetura self-hosted; não presumir integração, servidor MCP ou agentes ativos neste ambiente.

## Segurança
- Não responda automaticamente a prompts de aprovação de outro agente.
- Não feche sessões ou ambientes que não foram criados pelo coordenador sem autorização.
- Não reutilize IDs ou caminhos por suposição; leia-os da ferramenta real.
- Em ambientes remotos, trate falha de conexão como estado desconhecido, não como prova de que uma mutação não ocorreu.

## Heurística
Use workers para:
- exploração independente;
- revisão adversarial;
- geração de assets;
- implementação de slices separáveis;
- testes ou análise paralela.

Evite paralelizar trabalho altamente acoplado ou decisões que precisam de uma única arquitetura coerente.

## Relação com outras skills
Complementa `graph-engineering`, `handoff`, `code-review`, `agent-choice-audit` e `project-planning`.

## Origem adaptada
Metodologia inspirada também em https://github.com/builderz-labs/mission-control (plano de controle, receipts, custo e approvals), e em `herdrdev/herdr`, `stablyai/orca`, `chaseai-yt/claudex-loop`, block/buzz, proliferate-ai/proliferate, donvito/codex-astra-luna-orchestrator, rizqinrr/viserys-agent, unstablebuild/rune e DannyMac180/astra-advisor. Foram preservados isolamento por tarefa, papéis contratuais, reviewer independente e continuidade de workspace, sem depender de perfis/modelos/CLIs específicos.


## Orquestracao pedagogica por agentes: OpenMAIC (2026-10-18)

Quando o objetivo for projetar uma experiencia educacional interativa com professores e colegas de IA, reutilizar o rigor de coordenacao multiagente sem pressupor agentes independentes no ChatGPT:
- definir objetivo de aprendizagem, publico, pre-requisitos e criterios de dominio antes de gerar aulas;
- separar os papeis pedagogicos de exposicao, pergunta socratica, simulacao, feedback e avaliacao, com contratos por etapa;
- usar checkpoints de entendimento (quiz, aplicacao, exercicio, projeto), feedback formativo e adaptacao da proxima atividade ao erro observado;
- tratar slide, quadro, voz, simulacao e projeto como modalidades opcionais, somente quando o runtime oferecer suporte real;
- persistir progresso, materiais de origem, versao do curso e estado de avaliacao quando houver armazenamento conectado;
- exportar e validar artefatos somente com ferramenta real; narrativas de personagens nao provam varios agentes ativos;
- revisar factualidade, acessibilidade, seguranca de conteudo de alunos e respostas do sistema antes de implantar.

Usar esta secao em desenho de plataformas educacionais multiagentes. Para tutoria em conversa comum, aplicar os passos pedagogicos diretamente sem ativar a skill de workers.

Proveniencia: https://github.com/THU-MAIC/OpenMAIC (README da branch main, consultado em 2026-10-18). A plataforma externa depende de servidor, banco e modelos; sua orquestracao completa nao foi instalada.
