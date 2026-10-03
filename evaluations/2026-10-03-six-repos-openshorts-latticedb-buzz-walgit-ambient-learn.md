# Avaliação — 6 repositórios: OpenShorts, LatticeDB, Buzz, walgit, Ambient Context e Learn

Data: 2026-10-03

## Objetivo

Avaliar seis repositórios enviados em sequência e incorporar apenas capacidades incrementais ao Skill Arsenal canônico.

Fontes:
- mutonby/openshorts
- jeffhajewski/latticedb
- block/buzz
- tobi/walgit
- dragthelake/ambient-context
- amosblomqvist/learn

Nenhum installer, binário, container, modelo ou runtime dessas fontes foi executado.

## Resultado executivo

Atualizados:
- `short-form-video-engineering`
- `vertical-video-reframing`
- `ai-reels-production`
- `agent-memory-engineering`
- `ai-workspace-operating-cycle`
- `multi-agent-orchestration`
- `system-design-engineering`
- `teach`

Nenhuma nova skill foi criada.

## 1. mutonby/openshorts

### Classe
A/D

### Decisão
UPDATE_EXISTING + KEEP_EXTERNAL_REFERENCE

### O que acrescenta

OpenShorts implementa um pipeline self-hosted de short-form video com:
- faster-whisper com word-level timestamps;
- moment detection por transcript + scene boundaries;
- possibilidade de LLM remoto ou local;
- layouts 9:16 por cena;
- TRACK, GENERAL, SPLIT e SCREENCAST;
- captions queimadas;
- hook overlays;
- UGC synthetic actors;
- publishing integrations;
- MCP/API.

### Adoção

`short-form-video-engineering`:
- moment selection engine híbrido;
- provider replaceability;
- local-first model path;
- hook overlays.

`vertical-video-reframing`:
- layouts per-scene TRACK / GENERAL / SPLIT / SCREENCAST.

`ai-reels-production`:
- caminho self-hosted/local-first como implementação opcional.

### O que não foi absorvido

- promessa de “viral moment” como previsão;
- dependência obrigatória de Gemini, ElevenLabs, fal.ai ou Upload-Post;
- auto-publicação sem approval;
- uso de AI actor sem consent/provenance apropriados.

## 2. jeffhajewski/latticedb

### Classe
A/D

### Decisão
UPDATE_EXISTING

### O que acrescenta

Banco local single-file com:
- property graph;
- vector similarity;
- BM25 full-text;
- mesma query layer;
- WAL;
- durable named streams;
- graph changefeed.

### Adoção

`agent-memory-engineering` ganhou:
- hybrid lexical/vector/graph retrieval;
- preferência por consultas híbridas quando o store suporta todas as modalidades na mesma unidade transacional;
- durable streams/changefeeds para projections e memória incremental.

### Limite

LatticeDB é implementação técnica, não dependência do Arsenal. O hash embedding de exemplo do repo é explicitamente placeholder e não foi tratado como embedding semântico.

## 3. block/buzz

### Classe
A/D

### Decisão
UPDATE_EXISTING

### O que acrescenta

Workspace self-hosted onde humanos e agentes compartilham:
- channels;
- repos/patches;
- workflows;
- canvas/media;
- search;
- audit log;
- agent identity própria;
- event log assinado;
- ACP/MCP surfaces.

### Adoção

`ai-workspace-operating-cycle`:
- shared human-agent workspace;
- identity separada para agentes;
- event log como record;
- chat/canvas/search/git como views/projections;
- approval/audit attribution.

`multi-agent-orchestration`:
- agent identity e membership explícitos;
- audit trail por agente;
- relação rastreável entre patch, CI, review e approval.

### O que não foi absorvido

- dependência de Nostr;
- ACP/MCP específicos como requisito;
- deployment stack Postgres/Redis/S3;
- claims de features listadas pelo próprio projeto como ainda “being wired up”.

## 4. tobi/walgit

### Classe
A/D

### Decisão
UPDATE_EXISTING

### O que acrescenta

Arquitetura Git server com:
- object storage como source of truth;
- append-only WAL;
- immutable content-addressed packs;
- small manifest CAS como commit/linearization point;
- local disk como disposable cache;
- checkpoints + log tail;
- remote range reads para repositórios maiores que a máquina;
- compaction publicada no próprio log.

### Adoção

`system-design-engineering` ganhou um padrão explícito de:
`immutable objects + WAL in object store + manifest CAS + disposable caches + remote range reads`.

### Limite

Esse padrão não é universal. Ele faz sentido para workloads com objetos grandes/imutáveis e object-store semantics adequadas.

## 5. dragthelake/ambient-context

### Classe
A/D

### Decisão
UPDATE_EXISTING

### O que acrescenta

Captura ambiente local-first por macOS Accessibility:
- focused-window text;
- plaintext Markdown;
- raw context separado de knowledge e notes;
- citations do derivado para o record;
- dedup;
- UI-chrome filtering;
- message separation;
- configurable exclusions/redaction;
- ledger de ações;
- MCP read/write surface.

### Adoção

`agent-memory-engineering`:
- ambient capture section;
- raw record ≠ derived memory;
- citations/provenance;
- app/site exclusion;
- redaction e trust boundaries.

`ai-workspace-operating-cycle`:
- capture ambiente como input opcional;
- raw record separado de summaries/knowledge;
- derived layers reconstruíveis.

### Segurança

CAUTION/HIGH SENSITIVITY.

O próprio projeto reconhece:
- plaintext local;
- banking/health/mail podem ser capturados em browser comum;
- regex redaction é best effort;
- file paths/URLs podem conter secrets;
- downstream agent CLI é um segundo trust boundary;
- synced folder é outro trust boundary.

Nenhuma captura automática foi executada.

## 6. amosblomqvist/learn

### Classe
A/B/D

### Decisão
UPDATE_EXISTING

### Descoberta importante

O Arsenal já possuía `skills/teach/SKILL.md`, embora busca textual inicial não o tenha retornado. O GitHub impediu criação duplicada e o owner real foi lido antes da atualização.

### O que acrescenta

Metodologia:
- unconditional/foundational truths first;
- “how could I have discovered this?”;
- probe → plan → teach;
- locate floor + ceiling por strand;
- Socratic vs expository adaptativo;
- quiz distractors construídos a partir de misconceptions;
- understanding como rede de dependências, não coleção de fatos.

### Adoção

`teach` ganhou:
- fundamentos seguros primeiro;
- descoberta motivada;
- probing por floor/ceiling;
- Socratic/expository routing;
- quiz diagnostic guidance;
- compressão conceitual.

### O que foi rejeitado/adaptado

- probing exaustivo obrigatório para toda explicação;
- dependência de pi;
- tmux/subagents;
- popup UI;
- quiz extension específica;
- regra de “researcher subagent” substituída por verificação factual com ferramentas disponíveis.

## Segurança e portabilidade

Verdict geral: **CAUTION**.

Superfícies observadas:
- OpenShorts: Docker, API keys, external publishing, AI actors, voice cloning;
- LatticeDB: curl-pipe-shell installer, native libraries/bindings;
- Buzz: private keys, shell/file-edit MCP, Postgres/Redis/S3, workflows;
- walgit: bearer/OIDC tokens, S3/GCS, installer scripts, Git write surface;
- Ambient Context: Accessibility permission e capture de informação altamente sensível;
- Learn: subagents, shell extensions and third-party pi runtime.

Política aplicada:
- nenhum installer ou runtime foi executado;
- metodologia separada de infraestrutura;
- approval preservado para external writes;
- credentials never assumed;
- local-first não foi confundido com private-by-default;
- identity/voice/capture boundaries permanecem explícitos.

## Materialização

Atualizados e publicados:
- `skills/short-form-video-engineering/SKILL.md`
- `skills/vertical-video-reframing/SKILL.md`
- `stacks/ai-reels-production/STACK.md`
- `skills/agent-memory-engineering/SKILL.md`
- `stacks/ai-workspace-operating-cycle/STACK.md`
- `skills/multi-agent-orchestration/SKILL.md`
- `skills/system-design-engineering/SKILL.md`
- `skills/teach/SKILL.md`

Nenhum novo owner ou stack foi necessário.

## Limites

- avaliação baseada em README/documentos centrais e arquitetura representativa;
- não foi feita auditoria linha-a-linha dos seis repositórios;
- benchmarks declarados pelos projetos não foram reproduzidos;
- custos/free tiers de APIs externas podem mudar;
- features marcadas pelos próprios projetos como incompletas não foram tratadas como garantidas.
