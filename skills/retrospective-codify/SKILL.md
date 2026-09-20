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
