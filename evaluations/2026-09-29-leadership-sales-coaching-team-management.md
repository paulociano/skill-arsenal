# Avaliação em lote — liderança, sales coaching e produtividade de gestão

Data: 2026-09-29

## Escopo
Aprofundamento da shortlist prioritária após discovery de repositórios para feedback de liderança, gestão comercial e produtividade de equipes. Fluxo: `arsenal-autopilot`.

Nenhum installer, script, extensão, CRM connector ou automação externa das fontes foi executado.

## Fontes resolvidas

| Fonte | Classe | Decisão | Owner |
|---|---|---|---|
| manager-dot-dev/manager-skills | A/B | UPDATE_EXISTING + SOURCE | feedback/1:1/performance informam `coaching-development-loop` e owners de feedback |
| wondelai/skills · high-output-management | A/B | UPDATE_EXISTING | `agenda-operations` + `coaching-development-loop` |
| openai/role-specific-plugins · review-rep-call-trends | A/B/D | CREATE_NEW | `coaching-development-loop` |
| openai/role-specific-plugins · get-rep-call-feedback | A/B/D | CREATE_NEW / MERGE | `coaching-development-loop` |

## Fontes prioritárias não resolvidas de forma canônica nesta rodada
- stephenrogan/leadership-skills
- kindel/sbi
- Autter-dev/agentic-sales-skills
- zarif3624/gtm-skills
- smbochkarev1/performance-review-skill

A busca GitHub disponível não confirmou esses repositórios/paths como fontes canônicas. Resultados de terceiros que apenas os mencionam não foram usados como autoridade. Permanecem pendentes, não rejeitados.

## Capability ledger

### Feedback pontual
Já pertence a `golden-circle-feedback`. Manager Skills reforça precisão comportamental, proximidade temporal, perspectiva do liderado e evitar compliment sandwich mecânico. Não justifica owner duplicado.

### Coaching longitudinal
Lacuna real: o Arsenal avaliava calls isoladas e redigia feedback, mas não possuía owner explícito para provar mudança comportamental entre períodos e fechar o loop de prática/reobservação.

Decisão: criar `coaching-development-loop`.

Contrato:
baseline → comparação temporal → improved/regressed/stable/inconsistent → prioridade → if/then practice → recheck.

### Gestão do tempo do líder
High Output Management reforça que output gerencial é efeito sobre a organização, não volume de atividade. Absorvido em `agenda-operations`: tempo de alto leverage e capacidade abaixo de 100% quando interrupções são parte real do papel.

Não importado:
- score 0–10 de qualidade gerencial;
- thresholds universais de carga/reuniões;
- aplicação literal de um único livro como sistema completo.

### Gestão comercial semanal
`gestao-comercial-da-semana` passa a poder carregar `coaching-development-loop` quando houver histórico entre semanas. Isso permite verificar se feedback anterior mudou comportamento antes de gerar nova devolutiva.

## Segurança, privacidade e fairness
- transcrições e notas de 1:1 podem conter dados pessoais/confidenciais; usar somente fontes autorizadas e minimizar retenção;
- não inferir personalidade, intenção, saúde ou motivação;
- peer exemplars servem para extrair comportamento replicável, não ranking;
- performance review, PIP, remuneração e desligamento não devem ser decididos por score automático de coaching;
- conectores específicos de Meeting Transcripts das fontes OpenAI não foram copiados como dependência;
- contexto persistente sugerido por Manager Skills foi adaptado para preservar apenas fatos/acordos úteis, nunca frustração transitória como perfil durável.

## Mudanças publicadas
- CREATE `skills/coaching-development-loop/SKILL.md`
- UPDATE `skills/golden-circle-feedback/SKILL.md`
- UPDATE `skills/agenda-operations/SKILL.md`
- UPDATE `stacks/gestao-comercial-da-semana/STACK.md`
- UPDATE `ARSENAL INDEX.md`

## Limites
As cinco fontes não resolvidas continuam pendentes de URL/path canônico. Não foram feitas alegações de eficácia de coaching nem reproduzidos benchmarks das fontes.
