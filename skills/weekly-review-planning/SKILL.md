---
name: weekly-review-planning
description: "Executar revisão semanal baseada em calendário, compromissos, projetos, pendências e capacidade para fechar loops e definir poucos outcomes realistas para a próxima semana."
---

# weekly-review-planning

## Objetivo

Executar um reset semanal verificável que reconcilia o que aconteceu, o que continua aberto e o que realmente cabe na próxima semana.

## Quando usar

- revisão de sexta, domingo ou segunda;
- planejamento semanal a partir de agenda, tarefas, notas e projetos;
- identificação de compromissos esquecidos, projetos parados e follow-ups;
- preparação de uma semana com capacidade limitada ou muitos conflitos.

## Workflow

1. Definir período revisado, horizonte de planejamento, timezone e fontes de verdade.
2. Revisar a semana concluída: eventos relevantes, entregas, decisões, compromissos assumidos e follow-ups implícitos.
3. Revisar o horizonte de 1–2 semanas: compromissos fixos, prazos, preparação necessária, conflitos e carga.
4. Reconciliar projetos ativos. Para cada um, identificar outcome, próxima ação, owner, prazo, blocker, último movimento e fonte.
5. Revisar itens aguardando terceiros e promessas feitas pelo usuário. Silêncio não significa conclusão.
6. Classificar loops abertos em próxima ação, projeto, aguardando, agendado, referência, adiado ou descarte proposto.
7. Selecionar poucos outcomes semanais por consequência, prazo, dependência, esforço e capacidade real.
8. Explicitar o que ficou de fora ou foi adiado.
9. Propor mudanças em tarefas, agenda ou mensagens antes de executá-las.
10. Quando houver autorização para escrever em sistemas externos, ler de volta os registros alterados e verificar.

## Output

- ganhos e concluídos;
- atrasados ou em risco;
- aguardando / follow-ups;
- projetos parados ou ambíguos;
- restrições de agenda e capacidade;
- 3–5 outcomes da próxima semana;
- mudanças propostas;
- lacunas de cobertura.

## Regras

- Não planejar a semana olhando apenas tarefas; considerar calendário e capacidade.
- Não carregar automaticamente tudo que ficou incompleto.
- Projeto ativo precisa de próxima ação observável ou motivo explícito para pausa.
- Toda sinalização de atraso, risco ou espera deve rastrear a uma evidência.
- Não alterar agenda, mensagens ou registros sem autorização correspondente.
- Não preencher todo espaço livre: preservar margem para transição, preparação e imprevistos.

## Integração

agenda-operations, prioritization-engine, loop-engineering, project-health-review, meeting-to-actions e conectores reais quando disponíveis.

## Origem metodológica

Adaptada principalmente de NousResearch/hermes-agent `weekly-review-planning`, com práticas convergentes em borghei/Claude-Skills, SkillMedev/skills, alirezarezvani/claude-skills e jugbandman/todays-plan. Dependências específicas de Hermes, cron e stores locais foram removidas.

## Agenda executiva semanal por sinais (modo opcional)

Quando o objetivo for preparar uma reunião de liderança, e não apenas planejar tarefas pessoais:

1. Examinar follow-ups da reunião anterior e temas ainda sem resolução.
2. Selecionar fontes realmente acessíveis da semana: reuniões, e-mails enviados, mensagens relevantes, projetos e registros de decisões; declarar fontes ausentes.
3. Extrair temas com link/trecho de evidência, domínio impactado, decisão requerida, prazo e owner quando confirmados.
4. Filtrar assuntos resolvidos, genéricos, sensíveis inadequados ao grupo e temas de um único domínio que cabem em 1:1.
5. Priorizar por impacto, urgência, alcance entre áreas e tensão não resolvida, exibindo os critérios sem transformar soma arbitrária em verdade.
6. Produzir de 3 a 10 tópicos conforme evidência, separados por **decidir / discutir / informar / acompanhar**, com motivo, fonte e pergunta de abertura. Destacar carry-forwards e itens abaixo do corte.
7. Se a semana estiver vazia, não fabricar temas para completar quota; relatar cobertura e lacunas.

Essa variante não altera calendário nem envia mensagens automaticamente. Provenance: https://github.com/zapier/wade-skills/tree/main/skills/exec-weekly-agenda-generator .
