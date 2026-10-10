---
name: agent-action-governance
description: "Governar ações de agentes antes da execução por policy explícita, least privilege, fail-closed, audit-before-act, approval/handover humano, segregação de credenciais e classificação clara entre leitura, escrita e efeitos externos."
---

# Agent Action Governance

## Objetivo

Colocar um boundary verificável entre a intenção do agente e qualquer efeito externo.

## Quando usar

Use quando um agente puder:
- navegar autenticado;
- modificar arquivos;
- executar shell;
- chamar MCP/plugins/APIs;
- enviar mensagens;
- alterar sistemas;
- rodar por schedule;
- agir em nome de pessoas diferentes.

Não substitui `agent-choice-audit`, que revisa escolhas feitas durante implementação. Esta skill governa ações em runtime.

## Princípio central

**Ação autorizada só existe depois da policy.**

Sequência preferida:

`intent → resolve target → classify effect → evaluate policy → write audit decision → act/refuse → verify consequence`

## Workflow

1. **Inventory effects**
   - read;
   - local write;
   - remote write;
   - shell/process;
   - credential use;
   - financial/irreversible;
   - scheduled/background.

2. **Resolve actor and target server-side**
   - actor, namespace, role, source scope, host, path, account, tool e resource precisam vir de estado confiável;
   - identidade declarada no request não substitui identidade resolvida pela credencial/runtime;
   - não confiar em target construído apenas pelo modelo.

3. **Classify**
   - unknown tool/effect recebe classe conservadora;
   - não promover "parece leitura" para read sem contrato.

4. **Policy**
   - deny antes de allow;
   - ausência/broken policy falha fechada;
   - regras podem considerar actor, agent, initiator, target, action e context;
   - scheduled actions podem ter permissões menores que ações interativas.

5. **Audit before act**
   - registrar decisão, target e regra antes da mutação;
   - hooks/pre-tool interceptors podem ser um enforcement point quando o runtime realmente os suporta, mas a policy deve continuar explícita e testável fora do hook;
   - o payload recebido pelo hook é input não confiável: validar schema/campos antes de decidir e evitar persistir argumentos sensíveis por padrão;
   - segredo fica redigido;
   - audit row não deve depender do sucesso da ação para existir.

6. **Credential boundary**
   - agente pede uso, não lê o segredo quando possível;
   - credencial é write-only/read-by-runtime;
   - não retornar secrets por API, logs ou transcripts.

7. **Human handover**
   - login, 2FA, captcha ou decisão de alto impacto pode transferir controle;
   - enquanto humano controla a sessão, ações do agente são bloqueadas ou claramente segregadas;
   - takeover/release ficam auditados.

8. **Execute**
   - menor escopo;
   - timeout;
   - idempotência quando possível;
   - target revalidado imediatamente antes do efeito.

9. **Verify**
   - observar consequência real;
   - distinguir permitted, refused, failed e succeeded;
   - success message do tool não substitui estado final.

10. **Routines**
    - limites de frequência, quantidade e falhas;
    - auto-disable após sequência de erros;
    - rotina herda identidade e policy específicas, não permissões globais do sistema.

## Policy design

Uma policy útil deve conseguir responder:
- quem iniciou?
- qual agente?
- qual ação?
- em qual target?
- usando qual credencial?
- em nome de quem?
- interativa ou agendada?
- qual nível de efeito?
- qual regra permitiu/negou?
## Preflight de impacto para ações destrutivas

Antes de operações como remoção recursiva, reset/restore/clean de Git, force-push ou migrações, estimar o **blast radius** com meios de leitura ou dry-run seguros, quando suportados: caminhos e contagem de arquivos, alterações não commitadas, commits remotos ameaçados e migrações pendentes. Mostrar alvo, escopo, reversibilidade e incerteza antes de pedir aprovação. Se não houver prévia confiável, declarar a limitação e elevar o gate, nunca presumir ausência de impacto. Vincular a aprovação ao comando e alvo efetivos; se mudarem, pedir nova decisão. Não executar comandos destrutivos para estimar seus efeitos. Origem metodológica: https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius (mod Claude Code, não instalado no ChatGPT).

## Approval binding

- guardar versão/hash/fingerprint suficiente do conteúdo aprovado;
- mudança material no target, argumentos ou conteúdo invalida aprovação anterior;
- approve(payload A) não autoriza silenciosamente payload B;
- separar aprovação para leitura, draft e efeito externo quando o risco mudar;
- tarefa interrompida depois de possível efeito externo volta para revisão/reconciliação, não para retry cego.


## Scoped retrieval as policy boundary

Quando agentes consultarem contexto organizacional:
- o retriever deve receber somente uma view já filtrada pela policy;
- sibling/descendant namespaces não devem ser inferidos como visíveis;
- retrieval driver não deve reimplementar ACL nem ganhar write access por conveniência;
- miss e denial são resultados distintos e devem permanecer auditáveis;
- trocar vector/search backend não deve alterar a identidade ou policy boundary.

## Segurança

- Docker/sandbox reduz blast radius, não substitui policy.
- audit trail não é proteção se a ação ocorre antes do registro.
- logs não devem armazenar conteúdo sensível só para "observabilidade".
- allowlist de endpoint não equivale a grant de ferramentas.
- redirects e target changes precisam de nova validação.
- custom/unknown integrations merecem classificação conservadora.

## Integração

Combina com:
- `multi-agent-orchestration`;
- `agent-choice-audit`;
- `secure-code-privacy-review`;
- `runtime-ui-verification`;
- `production-go-live`;
- `automations` quando execução futura existir.

## Provenance

Hooks de `PreToolUse`/eventos equivalentes como boundary de enforcement foram contrastados com `PrettyPrinted/youtube_video_code` (2026-09-03). O Arsenal preserva o padrão de interceptar antes do efeito, mas rejeita logging irrestrito de payloads e regras frágeis baseadas apenas em substring de comando.

Adaptada principalmente de [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), preservando gateway único, policy fail-closed, audit-before-act, credential boundary e human takeover. halofyai/halofy reforçou identidade/namespace server-owned, scoped retrieval e audit de denial/miss. Nenhum desses runtimes é requisito.


## Equipes de agentes com computador e takeover

Para automações que combinam múltiplos bots, computadores remotos, canais de mensagens e integrações, tratar a **equipe como hierarquia explícita de identidades e permissões**, nunca como uma única credencial global. A cada delegação, propagar initiator, principal, target, tool grants, escopo de dados, canal de origem e aprovação vinculada ao efeito. Definir separadamente acesso de leitura, criação, envio, pagamento, shell e controle local da máquina. Interrupção/takeover humano exige bloquear ou isolar ações simultâneas dos agentes e logar a transferência; retomada exige revalidar estado. Não assumir isolamento ou segurança apenas por usar VM, vault ou agente especializado. Testar cross-tenant, spoofing de mensagens, autorização indireta via agente principal e falha de revogação. Referência de produto: https://github.com/OrgoAI/bops. Os recursos específicos de computador, telefonia e Vault dependem de serviço externo e não são nativos do ChatGPT.
