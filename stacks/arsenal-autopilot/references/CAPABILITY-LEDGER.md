# Capability Ledger

Use este template quando um lote for grande, houver overlap relevante ou a decisão de ownership não for óbvia.

| Source | Fragment | Capability | Existing owner | Novelty | Portability | Security | Decision | Proof |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| repo/path | SKILL.md seção X | comportamento reutilizável | skill existente / none | high/med/low | high/med/low | approve/caution/reject | CREATE_NEW / UPDATE_EXISTING / ABSORB_METHOD_ONLY / KEEP_EXTERNAL_REFERENCE / REJECT | cenário/check |

## Perguntas de decisão

### Novelty
- muda comportamento ou só muda wording?
- existe owner que já executa o mesmo contrato?
- o novo método resolve um failure mode não coberto?

### Portability
- depende de CLI, app, MCP, hook, runtime ou API externa?
- há equivalente real no ambiente atual?
- a metodologia continua útil sem a ferramenta original?

### Security
- lê credenciais?
- envia dados?
- executa código?
- persiste hooks/configuração?
- faz ações externas?
- exige permissões maiores que o propósito?

### Ownership
Uma capability deve ter um owner canônico sempre que possível.

Se dois recursos disputam o mesmo trigger:
1. generalize ou atualize o owner existente;
2. estreite o trigger do novo recurso;
3. se ainda forem equivalentes, não crie duplicata.

## Proof
Uma adoção deve ter pelo menos uma forma de prova proporcional:
- should-trigger + expected behavior;
- near-miss should-not-trigger;
- input/output representativo;
- teste/check determinístico;
- comparação baseline vs candidate quando o ganho for incerto;
- read-after-write para publicação.
