---
name: retrospective-codify
description: "Codificar aprendizados recorrentes quando solicitado, escolhendo entre atualizar skill, regra, checklist, teste ou documentação."
---

# retrospective-codify

## Objetivo

Converter tentativa-e-erro recorrente em conhecimento operacional reutilizável, escolhendo o menor artefato capaz de prevenir o mesmo desvio no futuro.

## Quando usar

Codificar aprendizados recorrentes quando solicitado, escolhendo entre atualizar skill, regra, checklist, teste ou documentação.

## Workflow

1. Registrar primeira tentativa, como falhou, solução final e insight que ligou as duas.
2. Reescrever o insight como `o que deveríamos ter sabido antes` em forma de instrução futura.
3. Fazer dedup obrigatório no Arsenal e nas regras existentes.
4. Escolher destino mínimo: atualização de skill existente, nova skill, regra de projeto, checklist, teste/lint automatizado ou documentação.
5. Preferir mecanismo verificável/automatizado quando o padrão puder ser detectado por máquina.
6. Evitar criar skill nova para lição pontual ou específica demais.

## Integração

Complementa `skill-builder`: `retrospective-codify` decide **o que merece ser codificado e onde**; `skill-builder` constrói a skill quando esse for o destino correto.

## Critérios de promoção

Antes de promover uma lição para skill/automação/loop:

- exigir evidência concreta de repetição ou padrão;
- separar `SKILL_CANDIDATE`, `AUTOMATION_CANDIDATE`, `LOOP_CANDIDATE` e `KEEP_MANUAL`;
- registrar owner, verifier, stop condition e permission boundary;
- tratar promoção como ação supervisionada separada da auditoria;
- não transformar uma sessão silenciosa ou um único exemplo em prova de recorrência.

## Evolução supervisionada

Quando houver muitas sessões/evidências recorrentes, usar um ciclo supervisionado:

1. **Collect evidence** — registrar sessões/erros/sucessos relevantes.
2. **Summarize** — extrair o padrão sem transformar toda conversa em skill.
3. **Aggregate** — juntar ocorrências equivalentes e contradições.
4. **Candidate** — produzir versão candidata da skill/regra/checklist.
5. **Deduplicate** — comparar com Arsenal atual.
6. **Validate** — baseline vs candidate, trigger boundaries e security review.
7. **Promote** — atualizar skill canônica somente após evidência suficiente.
8. **Version / rollback** — manter provenance e capacidade de voltar à versão anterior.

No Arsenal, evolução **não é silenciosa**: interação do usuário não autoriza autoedição invisível do repositório. Promoção de conhecimento durável continua sendo uma ação explícita/verificável.

Compartilhamento entre usuários/agentes também não é automático. Experiência pessoal, dados de cliente e contexto privado não devem alimentar uma skill compartilhada sem base e autorização apropriadas.

## Maturidade do conhecimento

Conhecimento/skills podem usar maturidade:

- draft → beta → stable → deprecated;
- promoção exige evidência de uso/sucesso suficiente, não apenas uma reflexão;
- memória/conclusão antiga pode perder confiança e pedir revalidação quando envelhece;
- propostas de self-improvement devem ser apresentadas como diff/impact e aprovadas antes de mudar comportamento canônico;
- toda autonomia relevante deve deixar audit trail.

Não inferir preferências sensíveis ou criar “world model” pessoal sem necessidade explícita.

## Referências

Adaptada de [mizchi/skills · retrospective-codify](https://github.com/mizchi/skills/tree/main/retrospective-codify).

Origem local: [retrospective-codify.docx](../retrospective-codify.docx).

## Retrospectiva de ambiente de agentes (mattpocock/retro, 2026-10-23)

Quando a retrospectiva for sobre uma sessão de programação assistida por agente, auditar **também o ambiente**, não apenas o código entregue:

1. Examinar evidências acessíveis da sessão, logs fornecidos, diffs e configuração real do repositório. Se estiverem ausentes, registrar a lacuna; não presumir acesso a sessões ou logs locais.
2. Verificar gargalos de navegação, referências a arquivos, padrões repetidos de chamadas caras, falta de informação, instruções sem efeito e excesso de contexto injetado.
3. Antes de recomendar um check novo, conferir scripts já existentes de lint, typecheck, testes, hooks e CI. Check existente mas não acionado ou quebrado é um problema diferente de check inexistente.
4. Separar **violações mecânicas** (preferir linter, teste ou gate determinístico) de **decisões de julgamento** (padrões de revisão/documentação). Não adicionar uma regra de texto quando uma verificação objetiva resolve melhor.
5. Priorizar recomendações por severidade, recorrência e custo, com evidência, owner, ação mínima e como verificar. Para uma única sessão, propor melhorias como candidatas, sem promover automaticamente regras globais.
6. Alterações em CI, hooks, regras globais e credenciais exigem escopo e aprovação adequados; não executar tooling, instalar pacotes ou editar o ambiente implicitamente.

**Should-trigger:** usuário pede retrospectiva de uma sessão em que o agente repetiu um erro que poderia ter sido pego por typecheck já disponível, mas ausente de CI. **Near-miss:** usuário pede somente revisão do diff atual; usar `code-review`, sem iniciar auditoria do ambiente. **Aceitação:** distinguir check ausente de check desconectado, recomendar conserto verificável e não confundir proposta com execução.

**Fonte metodológica:** https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md. Adaptação sem presumir subagentes, shell, arquivos locais ou acesso a histórico não fornecido.
