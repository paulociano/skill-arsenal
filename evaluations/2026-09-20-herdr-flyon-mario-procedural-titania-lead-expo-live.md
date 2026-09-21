# Avaliação em lote — coordenação multiagente, procedural film, evals e runtimes especializados

Data: 2026-09-20

## Escopo

Fontes:

- https://github.com/eliasstravik/herdr-projects
- https://github.com/dealerdefi/FLYON
- https://github.com/fhshaik/typesafe-mario
- https://github.com/kuhnhomeuk-cell/procedural-film
- https://github.com/penberg/titania
- https://github.com/planetscale/lead
- https://github.com/davidmokos/expo-gpt-live

Fluxo aplicado: `evaluate-and-import-skill` + `skill-security-review`.

Nenhum installer, package script, emulator, model, database extension, browser runtime ou código externo foi executado.

## Decisão resumida

- **Adotar como nova skill adaptada:** `procedural-film`.
- **Absorver metodologia em skills existentes:** Herdr Projects, FLYON, TypeSafe Mario, Titania, Lead e Expo GPT Live.
- **Não importar runtimes/dependências externas:** Herdr, Jev/TypeSafe, ROM/emulator, foundation assets, Rust GPU stack, pgrx/Postgres extension ou app Expo de referência.

## Avaliações

### eliasstravik/herdr-projects

**Classificação:** B/D — metodologia forte de coordenação, implementação acoplada a Herdr.

**O que faz:** coordenador permanente que delega tarefas a workers isolados, mantém estado em arquivos, usa worktrees/branches, inbox/ticker e grupos operacionais como waiting/ready-for-review.

**Valor:** alto para `graph-engineering`: record persistente em vez de prompts efêmeros, ownership por branch, estados de revisão e approvals explícitos.

**Segurança:** CAUTION. Usa shell, worktrees, SSH, rotinas e memória compartilhada. A própria documentação reconhece prompt injection via reports/memory e que guards são soft. Não importar daemon nem allow-lists.

**Decisão:** adaptar princípios em `graph-engineering`.

### dealerdefi/FLYON

**Classificação:** B/D — metodologia de avaliação auditável dentro de uma ferramenta on-chain read-only.

**O que faz:** registra cada call antes do outcome, liquida depois com regra fixa e expõe hit rate/Brier incluindo misses e casos abertos.

**Valor:** alto para avaliação temporal de previsões e confidence.

**Segurança:** APPROVE com escopo limitado. README declara apenas RPC reads e ausência de signing; ainda assim é software financeiro e seus resultados não devem ser tratados como aconselhamento.

**Decisão:** adaptar precommit + settlement em `llm-observability-evaluation`.

### fhshaik/typesafe-mario

**Classificação:** B/D — controlador técnico dependente de Jev/emulator.

**O que faz:** converte RAM/telemetry em estado JSON canônico, calcula timing exato em código e deixa o modelo escolher apenas entre ações legais.

**Valor:** forte para loops de controle: structured state, macros legais, observation-to-action delay e logs de outcome.

**Segurança:** CAUTION. Depende de serviço externo, emulator e game setup. A fonte não inclui ROM e explicita responsabilidade legal.

**Decisão:** adaptar metodologia em `loop-engineering`.

### kuhnhomeuk-cell/procedural-film

**Classificação:** A com dependências D na implementação original.

**O que faz:** pipeline completo de brief → research → art bible → storyboard → timeline → stubs → cenas → áudio → critic waves → render, com Canvas/Web Audio e gates determinísticos.

**Valor incremental:** materialmente diferente de edição de vídeo e de apresentações HTML. A disciplina de beat grid, timeline única, tracer bullet, contact sheets e audiovisual QA justifica skill separada.

**Segurança:** CAUTION. Original instala npm/Playwright/Chromium, usa FFmpeg e subagents. A versão Arsenal remove instalação automática, foundation assets e dependência de Claude Code.

**Decisão:** criar `skills/procedural-film/SKILL.md` e adicionar ao índice.

### penberg/titania

**Classificação:** B/D — sistema técnico completo de modelo/compiler/ISA/simulator/GPU.

**O que faz:** usa um simulador de ISA como definição executável do comportamento e exige que camadas futuras convirjam ao mesmo contrato.

**Valor:** princípio útil de executable reference/oracle para conformance.

**Segurança:** CAUTION alto. O README informa que o modelo possui tool `bash` e executa comandos sem confirmação. Esse comportamento não é importado.

**Decisão:** adaptar somente o conceito de reference oracle em `formal-methods-reconciler`.

### planetscale/lead

**Classificação:** B/D — implementação de teste/compatibilidade de Postgres, explicitamente não-production.

**O que faz:** substituto lento mas semanticamente correto para exercitar SQL compatível com TIN em dev/test/CI.

**Valor:** padrão forte para test doubles de compatibilidade que priorizam semântica observável sobre performance.

**Segurança:** APPROVE para metodologia; código é AGPL-3.0-or-later, portanto não copiar implementação para o Arsenal.

**Decisão:** adaptar metodologia em `tdd`.

### davidmokos/expo-gpt-live

**Classificação:** B/D — app Expo técnico com voice/WebRTC/tools.

**O que faz:** sessão realtime de voz com tools server-side, cancelamento, background iOS e separação entre secret do servidor e token do app.

**Valor:** útil para lifecycle de realtime voice/tool calls em Expo/React Native.

**Segurança:** CAUTION. Usa OpenAI API key, token local, WebRTC/background e backend potencialmente publicável. O README exige auth antes de exposição pública e tools consequenciais com confirmação.

**Decisão:** adaptar princípios em `crossplatform-mobile-engineering`, sem fixar modelo/API/version specifics.

## Mudanças aplicadas

- nova skill `procedural-film`;
- `graph-engineering`: coordinator/worker isolation, persistent record, review states e trust boundary;
- `llm-observability-evaluation`: precommit de previsões e settlement posterior;
- `loop-engineering`: estado canônico, cálculo determinístico e legal action space;
- `tdd`: test doubles de compatibilidade semanticamente fiéis;
- `formal-methods-reconciler`: executable reference como oracle;
- `crossplatform-mobile-engineering`: lifecycle de realtime voice/tools, abort e credential boundaries;
- `ARSENAL INDEX.md`: entrada para `procedural-film`.

## Limites

- Não houve scanner estático automatizado dedicado.
- Benchmarks/claims dos autores não foram reproduzidos.
- Nenhum código das fontes foi executado.
- Revisão de segurança focou a superfície metodológica importada e riscos declarados das implementações.
