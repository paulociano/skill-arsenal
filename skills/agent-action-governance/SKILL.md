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

2. **Resolve target server-side**
   - host, path, account, tool e resource precisam vir de estado confiável;
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

Adaptada principalmente de [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), preservando gateway único, policy fail-closed, audit-before-act, credential boundary e human takeover sem exigir AG-UI, CopilotKit Intelligence, Docker, CEL ou qualquer connector específico.
