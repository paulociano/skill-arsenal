---
name: agenda-operations
description: "Auditar e operar a agenda por capacidade, preparação, conflitos, dívida de reuniões e blocos de foco, propondo alterações seguras antes de executar mudanças."
---

# agenda-operations

## Objetivo

Transformar calendário em instrumento de capacidade e execução, não apenas registro de reuniões.

## Quando usar

- auditoria semanal de agenda;
- busca de conflitos, back-to-back excessivo ou dias fragmentados;
- preparação de reuniões importantes;
- criação de blocos de foco, buffers e janelas de follow-up;
- redução de reuniões sem objetivo, owner ou preparação.

## Workflow

1. Definir janela, timezone, calendários relevantes e restrições fixas.
2. Mapear carga por dia: horas ocupadas, blocos contínuos, fragmentação, transições e janelas reais de foco.
3. Detectar dívida de reunião:
   - convite sem objetivo ou resultado esperado;
   - duração padrão excessiva;
   - participantes sem papel claro;
   - back-to-back sem buffer;
   - recorrência sem evidência de necessidade;
   - assunto melhor resolvido de forma assíncrona.
4. Detectar necessidades de preparação, deslocamento, pós-reunião e follow-up.
5. Relacionar a agenda aos outcomes prioritários da semana e identificar trabalho importante sem espaço protegido.
6. Propor ajustes em ordem de menor impacto: encurtar, adicionar pauta/resultado, mover, agrupar, criar buffer, criar foco, converter em async ou cancelar como proposta.
7. Mostrar consequências e conflitos antes de qualquer mutação.
8. Executar apenas alterações autorizadas e verificar o estado final no calendário.

## Heurísticas

- Reunião deve existir para produzir decisão, coordenação ou trabalho conjunto que não seja melhor resolvido de forma assíncrona.
- Bloco de foco precisa de objetivo e definição de concluído.
- Preparação e follow-up consomem capacidade mesmo quando não aparecem no convite.
- Um dia 100% ocupado não representa 100% de capacidade útil.
- Mudanças em eventos compartilhados têm custo social maior que mudanças em blocos pessoais.

## Regras

- Não inferir que um compromisso pode ser cancelado apenas porque parece pouco importante.
- Não responder convites, mover ou cancelar eventos sem autorização explícita.
- Não otimizar agenda sacrificando prazos, deslocamentos ou compromissos fixos conhecidos.
- Quando houver múltiplos calendários, declarar cobertura e conflitos de fonte.

## Integração

weekly-review-planning, meeting-to-actions, meeting-knowledge-capture, prioritization-engine e Google Calendar quando conectado.

## Origem metodológica

Adaptada de padrões de calendar-concierge em megandmartin/agent-skills-repo, meeting hygiene em alirezarezvani/claude-skills e revisão de capacidade em NousResearch/hermes-agent. Dependências específicas de outros agentes foram substituídas por conectores reais quando disponíveis.
