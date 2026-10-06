---
name: product-management-cycle
description: "Conduzir decisões recorrentes de produto conectando contexto estratégico, evidência de descoberta, especificação, priorização, métricas e revisão de resultados sem misturar frameworks incompatíveis."
---

# Product Management Cycle

## Objetivo
Conectar estratégia → descoberta → decisão → execução → medição em um ciclo coerente, usando owners especializados do Arsenal em vez de uma mega-skill de produto.

## Skills candidatas
- founder-diagnose
- stakeholder-strategy
- jtbd-framing
- customer-interview
- discovery-research-synthesis
- idea-refine
- to-spec
- prioritization-engine
- product-metrics-diagnostics
- experiment-design
- decision-analysis
- after-action-review
- product-lifecycle-transition

## Workflow
1. **Context gate** — confirmar usuário/ICP, outcome estratégico, evidência disponível, horizonte e capacidade. Reutilizar contexto atual confiável; não interrogar novamente o que já está resolvido.
2. **Evidence** — quando a decisão depende de necessidade real, usar discovery/interviews/telemetry antes de detalhar solução. Pedido de stakeholder é sinal, não validação automática. Quando alinhamento, poder ou impacto entre grupos puder mudar a decisão, usar `stakeholder-strategy`.
3. **Opportunity** — separar problema/oportunidade de feature; usar JTBD/idea-refine somente quando a forma da solução ainda estiver aberta.
4. **Decision** — explicitar riscos de valor, usabilidade, viabilidade e feasibility relevantes. Para apostas grandes sem evidência, propor discovery/experimento ou marcar assumptions, não fabricar certeza.
5. **Spec** — usar `to-spec` quando a decisão estiver suficientemente resolvida. Manter outcomes, non-goals e critérios verificáveis.
6. **Priority & capacity** — priorizar considerando estratégia, impacto, urgência, dependências, risco, esforço e capacidade real. Frameworks como RICE são heurísticas, não autoridade.
7. **Measure** — definir métrica/guardrails antes do resultado quando isso for material; diagnosticar tracking antes de explicar movimento.
8. **Review** — comparar outcome com previsão/assumptions e registrar aprendizado. Atualizar decisão, não reescrever retrospectivamente a previsão. Quando o produto estiver maduro, em declínio ou sob pressão de substituição/EOL, rotear para `product-lifecycle-transition` em vez de tratar o problema como backlog comum.

## Conflitos metodológicos
Não misturar frameworks apenas para parecer abrangente. Quando dois métodos impõem regras incompatíveis, escolher o que corresponde ao contexto e declarar a escolha. Um ciclo Shape Up, um PRD detalhado e Continuous Discovery podem coexistir na organização, mas não precisam governar a mesma decisão simultaneamente.

## Regra de evidência proporcional
Não impor números universais de entrevistas, percentuais ou duração de ciclo. A força necessária depende de custo, reversibilidade, risco e evidência já disponível. Threshold quantitativo precisa de baseline/anchor ou deve ser marcado como hipótese.

## Estado e decision journal
Quando houver workspace persistente e o ciclo for recorrente, manter um decision journal leve:
- decisão e data;
- evidência/assumptions;
- outcome previsto e métrica;
- kill/revisit condition quando útil;
- confiança qualitativa ou quantitativa apenas quando calibrável;
- status e outcome observado posteriormente.

Não criar arquivo persistente sem necessidade/autorização. Draft exploratório não vira compromisso automaticamente.

## Parcimônia
Pedidos isolados de entrevista, métrica, PRD ou priorização usam somente o owner correspondente. Esta stack entra quando duas ou mais fases do ciclo precisam permanecer coerentes.

## Origem metodológica
Composição original do Arsenal, refinada a partir de `rajann44/pm-skills`: context gate, license-to-say-no, conflitos entre metodologias e decision journal. Rejeita thresholds universais e dependência de arquivos/comandos específicos da fonte.
