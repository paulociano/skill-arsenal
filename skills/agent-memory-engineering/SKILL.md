---
name: agent-memory-engineering
description: "Projetar memória durável para agentes separando captura, distilação, retrieval, gestão e provenance, com source of truth legível, caches reconstruíveis, validade temporal, níveis de leitura e avaliação empírica antes de automatizar esquecimento ou promoção."
---

# Agent Memory Engineering

## Objetivo

Projetar memória de longo prazo como um sistema operável e auditável, não como um vetor de transcripts.

## Quando usar

Use quando:
- um agente precisa aprender entre sessões;
- fatos, decisões, procedimentos ou episódios devem sobreviver a context resets;
- há necessidade de corrigir, superseder, consolidar ou esquecer memórias;
- retrieval precisa ser econômico e rastreável;
- múltiplos agentes/hosts compartilham conhecimento durável.

Para documentação canônica de repositório, use `repository-evidence-docs`.
Para contexto transitório de uma tarefa, prefira `handoff` ou workspace state.

## Modelo W-R-M

Separe três subsistemas:

1. **Write**
   - capturar evidência bruta;
   - distilar unidades reutilizáveis;
   - classificar tipo e provenance;
   - nunca depender apenas de o agente "lembrar de lembrar".

2. **Read**
   - encontrar candidatos;
   - rankear;
   - devolver ponteiros/resumos antes de conteúdo integral;
   - expandir progressivamente somente o necessário.

3. **Manage**
   - corrigir;
   - superseder;
   - fundir;
   - arquivar;
   - propor esquecimento;
   - manter histórico suficiente para auditoria/as-of.

## Tipos de memória

Separar quando útil:
- **semantic**: fatos e conceitos;
- **procedural**: como fazer algo;
- **episodic**: sequência/evento específico;
- **decision**: escolha, contexto e razão;
- **preference**: preferência explicitamente sustentada e com escopo.

Não tratar esses tipos como ontologia universal. Use apenas os necessários.

## Correções e aprendizado supervisionado

Correções explícitas e padrões recorrentes são **candidatos** a memória, não instruções permanentes automáticas. Capturar evidência da correção, distinguir preferência durável de ajuste pontual, normalizar regra curta e propor escopo (sessão, projeto ou global). Revisar duplicatas, contradições e dados sensíveis; promover para arquivo canônico/AGENTS.md somente com aprovação e provenance. Padrões de workflow podem gerar propostas de skill quando recorrência e ganho incremental forem demonstrados. No ChatGPT, não presumir hooks de Claude Code nem sincronização automática de memória ou histórico; usar apenas fontes e ações efetivamente acessíveis. Origem: https://github.com/BayramAnnakov/claude-reflect.

## Source of truth

Preferir uma representação durável que possa ser inspecionada e exportada independentemente do índice.

Quando arquivos legíveis forem adequados:
- arquivo é truth;
- FTS/vector/graph index é cache reconstruível;
- links e IDs permanecem estáveis;
- rebuild não pode destruir conhecimento.

Quando database for necessária, preserve equivalente:
- export;
- provenance;
- versionamento;
- migração;
- forma de reconstruir índices derivados.

## Workflow

1. **Memory contract**
   - quem escreve;
   - quem lê;
   - escopo;
   - sensibilidade;
   - duração;
   - tipos;
   - critérios de retenção.

2. **Capture first**
   - quando perda seria cara, preservar trace/evidência antes da distilação;
   - distiller incompleto não deve significar dado irrecuperável;
   - ao criar um store novo, usar o próprio briefing ou onboarding como bootstrap inicial: transformar apenas fatos confirmados em registros reais, para que captura e recuperação sejam testadas desde o primeiro uso;
   - captura automática precisa respeitar o memory contract: não transformar toda mensagem em memória permanente sem regra de escopo, sensibilidade e retenção.

3. **Distill**
   - extrair uma unidade por ideia durável;
   - adicionar abstract curto;
   - provenance para source/episode;
   - evitar copiar grandes transcripts.

4. **Promote**
   - só promover ao store principal o que tem reutilização plausível;
   - usar frequência, impacto, estabilidade e confirmação como sinais;
   - não promover segredo, ruído, erro transitório ou inferência fraca.

5. **Retrieve**
   - começar com índice curto;
   - expandir abstract → outline/anchor → full → raw trace;
   - em stores de arquivos grandes, usar mapas hierárquicos locais por domínio/pasta quando isso reduzir busca: o mapa lista conteúdo, rotas e pegadinhas, mas nunca substitui o arquivo como fonte da verdade;
   - manter esses mapas pequenos e atualizáveis; divergência entre mapa e arquivo corrige o mapa, não o fato;
   - combinar lexical/vector/graph apenas quando melhorar recall medido;
   - quando um store local combinar relações, BM25 e vetores na mesma unidade transacional, explorar consultas híbridas em vez de manter três índices desconectados;
   - durable changefeed/event streams podem alimentar projections e memória incremental sem revarrer todo o corpus;
   - miss em um mecanismo não significa ausência.

6. **Use**
   - citar/identificar a memória usada quando decisão importante depender dela;
   - distinguir memória histórica de estado atual;
   - facts externos mutáveis precisam de revalidação.

7. **Portable handoff / shared recall**
   - quando múltiplos agentes ou sessões participarem do mesmo projeto, preferir registros portáveis, inspecionáveis e vinculados ao workspace em vez de transcripts proprietários;
   - um handoff deve registrar fonte, horário/estado observado, o que mudou, pendências, próximo passo e target quando houver;
   - recuperar memória antes de criar outra cópia equivalente;
   - tratar memória recuperada como evidência potencialmente desatualizada, nunca como autorização ou verdade atual;
   - separar escopos de projeto, equipe e usuário quando o runtime suportar isso; labels de harness/target roteiam contexto, não concedem permissão;
   - um miss incompleto, store truncado ou documento inválido não deve ser apresentado como “não existe” sem verificar diagnósticos do mecanismo.

8. **Correct / supersede**
   - correção não apaga silenciosamente a história;
   - manter `valid_from` / `invalid_at` ou mecanismo equivalente quando temporalidade importa;
   - permitir consulta as-of quando decisões históricas dependem do estado anterior.

9. **Consolidate**
   - rodar em ciclo separado quando possível;
   - merge exige preservar provenance;
   - unattended deletion deve ser mais restrita que unattended add/update.

10. **Session close / checkpoint**
   - quando o host não garante persistência contínua confiável, fechar blocos substanciais com uma varredura curta de fatos, decisões, tarefas e correções ainda não materializados;
   - atualizar somente os índices/mapas afetados, evitando revarrer o store inteiro;
   - não usar o checkpoint como desculpa para adiar toda captura até o fim.

11. **Evaluate**
   - dataset/casos reais;
   - medir retrieval exposure, acerto e custo;
   - verificar se o agente realmente usou o caminho testado;
   - comparar com baseline sem memória;
   - não atribuir ganho a retrieval se o agente bypassou o mecanismo.

## Ambient capture

Quando contexto for capturado automaticamente do ambiente de trabalho:

- preservar **record bruto** separado de knowledge/summaries derivados;
- registrar app, horário e referência/path/URL quando disponíveis;
- deduplicar e filtrar chrome/ruído antes de persistir;
- separar mensagens/mail quando isso permitir exclusão seletiva do prompt;
- derived knowledge precisa apontar de volta ao record;
- capture scope deve ser configurável por app/site e suportar redaction;
- password managers, secure fields e private browsing devem ser excluídos quando o runtime permitir;
- local-first reduz exposição, mas não elimina risco: plaintext local continua sensível;
- synced folders e downstream agent CLIs são trust boundaries independentes;
- redaction é defence-in-depth, nunca garantia de DLP.

## Governed organizational context

Quando memória/contexto é compartilhado por uma organização:
- identidade, role, namespace e source scope devem vir do credential/runtime, não de campos enviados pelo agente;
- corrections devem superseder fatos anteriores em vez de apagar histórico silenciosamente;
- retrieval engine deve receber uma view já ACL-scoped e, idealmente, não possuir write path;
- success, denial, miss e error podem precisar de audit trail;
- cold knowledge e operational context podem viver em tiers distintos, desde que authority e provenance permaneçam claros;
- erasure precisa alcançar tombstones/derivados conforme contrato e produzir evidência verificável quando necessário;
- retrieval backend deve ser replaceable sem mover o policy boundary para dentro dele.

## Segurança e privacidade

- memória amplifica blast radius de dados sensíveis;
- segredos, tokens e autenticação não entram no store;
- separar memória de pessoa, projeto e organização;
- acesso compartilhado precisa de autorização explícita;
- deletion request e retention policy precisam alcançar cópias derivadas quando aplicável;
- embeddings externos podem exfiltrar conteúdo mesmo quando o store principal é local.

## Regras

- transcript não é memória curada.
- vector DB não é source of truth por definição.
- maior recall não compensa memória incorreta sendo aplicada.
- store invisível ao usuário exige controles mais fortes de inspeção e correção.
- memória velha pode ser menos confiável que ausência de memória.
- cache deve ser reconstruível ou explicitamente tratado como dado autoritativo.

## Integração

Combina com:
- `ai-workspace-operating-cycle`;
- `repository-evidence-docs`;
- `retrieval-quality-engineering`;
- `llm-observability-evaluation`;
- `session-learn`;
- `verify-before-claim`.

## Provenance

O padrão de handoff portátil, scopes project/team/user, recall-before-write e memória como evidência revisável foi refinado a partir de `affaan-m/ECC` (`unified-memory`), sem adotar o runtime ECC Memory Vault como dependência.

Consolidada de [TIMAN-group/PlugMem](https://github.com/TIMAN-group/PlugMem), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [mem0ai/mem0](https://github.com/mem0ai/mem0) e [letta-ai/letta](https://github.com/letta-ai/letta). A avaliação local `Segundo Cérebro v3` (2026-10-02) acrescentou os padrões portáveis de bootstrap pelo briefing, mapas hierárquicos locais e checkpoint de sessão. LatticeDB acrescentou retrieval híbrido local graph+vector+BM25 e changefeeds duráveis. dragthelake/ambient-context acrescentou captura ambiente local-first com record bruto separado de knowledge/notes. kunchenguid/backpass reforçou edição de memória baseada em evidência de sessões reais com human apply gate. halofyai/halofy acrescentou namespace ACL server-owned, supersedence, scoped retrieval e signed erasure. A skill continua sem assumir esses runtimes ou stores específicos.
