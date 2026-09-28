# Avaliação de repositórios externos — lote 2026-09-27-c

## Escopo

Fontes:
- vectorize-io/hindsight
- reladraw/reladraw
- tobi/disktree
- devdotfast/whiteboard
- TokenRhythm/NeoHorse
- supermemoryai/company-brain
- Contrastive-LM/CLM
- mikehasa/golive-skill
- deepakness/cogsend
- jaydendavisnc/inkwave

Router: ARSENAL INDEX.md.
Stack: arsenal-autopilot.
Gate: revisão estática proporcional via skill-security-review, sem executar installers, setup scripts, modelos, CLIs, binários ou infraestrutura externa.

## Decisões

### vectorize-io/hindsight
Classificação: A/D.
Decisão: KEEP_EXTERNAL_REFERENCE / ABSORB_METHOD_ONLY.
Valor:
- retain / recall / reflect;
- memory banks isolados;
- retrieval híbrido;
- mental models;
- documentação com progressive disclosure.
Motivo:
- runtime próprio com servidor, storage, modelos e configuração;
- Memory do ChatGPT não deve ser simulada nem substituída;
- conceitos de memória persistente já se conectam a loop-engineering, handoff, kb-retriever e golden-path-capture.

### supermemoryai/company-brain
Classificação: A/D.
Decisão: KEEP_EXTERNAL_REFERENCE / ABSORB_METHOD_ONLY.
Valor:
- memória organizacional com escopo por permissão;
- writes sob identidade/conexão do usuário;
- proatividade configurável;
- automações e sandbox.
Motivo:
- produto completo em Slack/Cloudflare com Supermemory e integrações;
- capacidade não é nativa do Arsenal sem runtime/connector real.
Padrão preservado:
- contexto/memória deve respeitar o mesmo boundary de acesso do solicitante;
- ações em ferramentas devem usar autorização e conexão apropriadas.

### reladraw/reladraw
Classificação: A/B/D.
Decisão: UPDATE_EXISTING.
Owner: architecture-visualization.
Valor incremental:
- layout relativo como meio-termo entre auto-layout e coordenadas absolutas;
- preservação explícita de intenção espacial.
Adaptação:
- metodologia incorporada sem exigir CLI, sintaxe ou renderer do projeto.

### devdotfast/whiteboard
Classificação: A/D.
Decisão: UPDATE_EXISTING.
Owner: code-review.
Valor incremental:
- semantic diff;
- decision log para escolhas autônomas;
- visualizações navegáveis de volta ao código.
Adaptação:
- método incorporado sem depender do app desktop, SDK ou fork de Code OSS.

### mikehasa/golive-skill
Classificação: A/D.
Decisão: CREATE_NEW.
Owner criado: production-go-live.
Valor incremental:
- detect → plan → approve → apply → verify;
- handoff;
- drift check;
- teardown com ownership comprovável;
- approval vinculado a plano/destino;
- distinção entre verificado, não verificável e pendente.
Adaptação:
- runtime GoLive, npm package e provider adapters não são presumidos;
- providers específicos são exemplos, não dependências.

### TokenRhythm/NeoHorse
Classificação: D/B.
Decisão: UPDATE_EXISTING / KEEP_EXTERNAL_REFERENCE.
Owner: model-routing-gateway.
Valor:
- decision engine tipado Choice/Noul/Score;
- roteamento e agentic post-training;
- checkpoints locais.
Motivo:
- exige weights, serving e avaliação própria;
- benchmarks publicados não transferem automaticamente para workload do usuário.

### Contrastive-LM/CLM
Classificação: D/B.
Decisão: UPDATE_EXISTING / KEEP_EXTERNAL_REFERENCE.
Owner: model-routing-gateway.
Valor:
- ranking de candidatos e decisões tipadas;
- embeddings de estado/ação reaproveitáveis;
- uso como verifier.
Motivo:
- exige encoder/serving/GPU e runtime próprio;
- qualidade e calibração precisam ser medidas no domínio real.

### deepakness/cogsend
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.
Valor:
- composer multicanal;
- overrides por plataforma;
- scheduling, retries e delivery insights;
- MCP/API.
Overlap:
- social-growth-engine, content-production, loop-engineering.
Motivo:
- produto self-hosted completo, não uma metodologia que justifique owner novo.

### tobi/disktree
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.
Valor:
- treemap para uso de disco;
- marcação reversível;
- review antes de deleção;
- visualização de espaço recuperável e free-space projected.
Motivo:
- aplicação desktop específica;
- padrão de approval antes de deleção já coberto por guardrails gerais.

### jaydendavisnc/inkwave
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.
Valor:
- simulação determinística;
- freeze/step tooling;
- smoke/net tests headless;
- arquitetura event-driven;
- assets procedurais e rendering Three.js.
Overlap:
- procedural-film, creative-web-effects, behavior-contract-validation, runtime-ui-verification.
Motivo:
- projeto de jogo completo; não há capability única nova que justifique skill separada.

## Mudanças publicadas

1. Criada `skills/production-go-live/SKILL.md`.
2. Atualizada `skills/architecture-visualization/SKILL.md` com layout relativo.
3. Atualizada `skills/code-review/SKILL.md` com decision log, semantic diff e ligações visual→código.
4. Atualizada `skills/model-routing-gateway/SKILL.md` com NeoHorse-Jev e CLM como referências de decision engines.
5. Atualizado `ARSENAL INDEX.md` com `production-go-live`.

## Segurança e portabilidade

- nenhum installer, setup script, model weight, MCP server, CLI ou binário externo foi executado;
- nenhuma credencial foi solicitada;
- nenhum runtime externo foi tratado como capability nativa;
- claims de benchmark foram mantidos como claims dos projetos e não como garantias do Arsenal;
- produtos self-hosted permaneceram referências quando a metodologia já tinha owner canônico.

## Limites

- esta avaliação foi baseada na documentação e arquivos centrais necessários para triagem;
- não houve execução funcional dos projetos externos;
- segurança do runtime de cada projeto exigiria auditoria separada antes de implantação real.
