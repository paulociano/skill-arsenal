# Avaliação — CopilotKit/OpenDots

Data: 2026-10-02  
Fonte: https://github.com/CopilotKit/OpenDots  
Branch avaliada: `main`  
Decisão: **adaptar parcialmente, sem importar o runtime**  
Classificação: **D — referência técnica dependente de ferramentas e infraestrutura externa**

## O que é

OpenDots é um template open source para coworkers/agentes persistentes que combinam workspace documental, especialistas configuráveis, conversas persistentes, Slack, voz, trabalho agendado e computadores isolados por agente. A arquitetura usa CopilotKit/AG-UI, TanStack AI, Intelligence/Threads, Channels SDK, SQLite, OpenBot, Node.js e serviços externos configuráveis.

Não é uma Agent Skill portável. É uma aplicação completa, com runtime, UI, persistência, credenciais, containers e integrações.

## Valor incremental para o Arsenal

Grande parte dos princípios já estava coberta por:
- `ai-workspace-operating-cycle`: workspace persistente, artifacts, fontes, decisões, estado e retomada;
- `agent-memory-engineering`: memória durável, provenance, promoção, retrieval e gestão;
- `agent-action-governance`: least privilege, approvals, credenciais, ações agendadas e human takeover;
- `computer-use-agent-engineering`: computadores isolados, browser, filesystem, shell e takeover;
- `multi-agent-orchestration`: especialistas/workers com ownership e contratos claros;
- `session-learn` e `golden-path-capture`: extração e promoção de aprendizado reutilizável.

O incremento mais útil está no desenho do **ciclo de aprendizagem e entrega de skills**:
1. conversas elegíveis enviam evidência a um container de aprendizagem explícito;
2. a aprendizagem pode propor skills, mas publicação exige revisão;
3. ingestão de evidência e entrega de skills são controles independentes;
4. uma conversa mantém o container de aprendizagem que recebeu na criação, evitando troca retroativa silenciosa;
5. skills publicadas são carregadas sob demanda no runtime;
6. configuração não prova uso: o uso real deve ser verificado por traces/tool calls;
7. falha de entrega configurada deve ser explícita, não degradar silenciosamente para comportamento diferente.

Esse padrão melhora `session-learn` sem justificar uma skill nova.

## Adaptação aplicada

`skills/session-learn/SKILL.md` foi enriquecida com uma seção de **pipeline de aprendizagem contínua**, mantendo a implementação agnóstica:
- evidence routing por workflow/escopo;
- separação entre ingestão, proposta, review/publish e delivery;
- versionamento/binding por conversa ou episódio;
- publicação humana antes de skill canônica;
- verificação de uso real;
- falha explícita quando delivery configurado não está disponível.

Nenhuma dependência CopilotKit, Intelligence, AG-UI ou OpenBot foi adotada.

## Segurança

Veredito: **CAUTION para execução do produto; APPROVE para absorção metodológica**.

Pontos positivos observados:
- credenciais mantidas no servidor;
- browser de pesquisa separado e read-only;
- redirects e private addresses bloqueados no browser de pesquisa;
- allowlist explícita para Slack;
- per-Dot permissions para browser/files/shell;
- human-in-the-loop antes de certas gravações;
- revision checks contra stale writes;
- documentação reconhece limites de single-owner e integrações não verificadas.

Riscos/limites:
- exige múltiplos segredos e serviços externos;
- computador por agente amplia blast radius e inclui shell;
- deployment remoto exige autenticação/HTTPS;
- identidade multiusuário não está pronta;
- o próprio projeto declara não ser um agente autônomo security-audited;
- dependências npm usam mistura de versões exatas e ranges;
- avaliação foi estática: nenhum installer, serviço, container ou código do projeto foi executado.

## Portabilidade

**Baixa para o runtime; alta para os princípios.**

O Arsenal não deve importar:
- CopilotKit-specific tool names;
- Intelligence containers como requisito;
- OpenBot services;
- Docker/Node stack;
- Slack/voice adapters.

Deve preservar:
- learning scopes explícitos;
- review/publish gate;
- binding estável de evidência a contexto;
- delivery separado de ingestion;
- observabilidade do uso de skill;
- fail-explicit quando a skill configurada não puder ser entregue.

## Resultado

- Nova skill: **não criada**.
- Skill existente atualizada: `session-learn`.
- Índice: **sem alteração**, porque nome e descrição de roteamento permanecem adequados.
- Runtime externo: **não instalado nem executado**.

## Fontes revisadas

- `README.md`
- `docs/SETUP.md`
- `SECURITY.md`
- `.env.example`
- `package.json`
- documentação e trechos de Automatic Learning, background work e review-before-save encontrados no repositório.
