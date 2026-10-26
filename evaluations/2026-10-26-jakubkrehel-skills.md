# Avaliação: jakubkrehel/skills (2026-10-26)

- Fonte: https://github.com/jakubkrehel/skills
- Arsenal: https://github.com/paulociano/skill-arsenal
- Router: ARSENAL INDEX.md
- Stack: arsenal-autopilot
- Escopo: catálogo com 14 skills; README e aprofundamento dos candidatos de maior valor incremental.

## Inventário e decisões

| Skill externa | Classe | Decisão | Justificativa |
| --- | --- | --- | --- |
| better-interface | B | KEEP_EXTERNAL_REFERENCE | Orquestração e auditoria por domínio já cobertas por design-principles-audit e web-quality-audit. |
| better-ui | B | KEEP_EXTERNAL_REFERENCE | Overlap com ui-motion-design, interaction-polish e web-design-engineer. |
| better-typography | B | KEEP_EXTERNAL_REFERENCE | Tipografia já tratada em visual-composition-fundamentals e web-design-engineer; regras numéricas não devem virar dogmas universais. |
| better-colors | B | KEEP_EXTERNAL_REFERENCE | Sistema de cores/contraste já coberto por design-system-governance e auditoria de qualidade web. |
| better-accessibility | B | KEEP_EXTERNAL_REFERENCE | WCAG e verificações existentes; usar requisitos aplicáveis, sem alegar certificação automatizada. |
| better-layout | B | KEEP_EXTERNAL_REFERENCE | Sobreposição de layout e responsividade. |
| better-writing | B | KEEP_EXTERNAL_REFERENCE | Microcopy é metodologia válida, sem ganho incremental isolado comprovado. |
| interface-review | A/D | KEEP_EXTERNAL_REFERENCE | Revisão de mudanças demanda diff e runtime; workflows de code-review e runtime-ui-verification já cobrem. |
| explain-interface | B/D | KEEP_EXTERNAL_REFERENCE | Diagnóstico a partir de URL/screenshot depende da observabilidade realmente disponível. |
| break | A/D | UPDATE_EXISTING | Stress visual dirigido pelas props e cenários que o componente realmente pode receber; incorporado ao runtime-ui-verification. |
| build-design | B/D | KEEP_EXTERNAL_REFERENCE | Implementação fiel a Figma/screenshot já tratada por owners de web/design; integração Figma não pressuposta. |
| teardown | D | KEEP_EXTERNAL_REFERENCE | Artefatos SVG/PNG/PDF e UI específica são tarefa técnica distinta, sem demanda incremental demonstrada aqui. |
| state-machine | A/D | UPDATE_EXISTING | Exercitar cada branch real com fixtures e seletor sem alterar lógica de produção; incorporado ao runtime-ui-verification. |
| variant | A/D | UPDATE_EXISTING | Três alternativas em um eixo, comparação no contexto real e cleanup; incorporado ao design-direction. |

## Mudanças efetivamente feitas

- skills/runtime-ui-verification/SKILL.md: protocolo de matriz de estados, stress test isolado, dados simulados, evidência e limpeza.
- skills/design-direction/SKILL.md: protocolo de variantes com eixo controlado, critérios mínimos comuns, comparabilidade e promoção.
- ARSENAL INDEX.md: sem mudança; os owners já estavam indexados.
- evaluations/2026-10-26-jakubkrehel-skills.md: registro de decisões, segurança e procedência.

## Segurança / Portabilidade

Nenhum instalador npx, plugin Claude, script ou binário externo foi executado ou importado. As adaptações são instruções metodológicas, não garantia de navegador, Figma, Storybook ou Playwright. Fixtures não devem acessar serviços, credenciais ou dados de produção. Inspeção visual não verificada é UNKNOWN, nunca PASS.

## Critério de valor

- Should-trigger: ao testar um componente existente em vários estados ou conteúdo extremo, aplicar o laboratório temporário e repetir casos após correção.
- Should-trigger: quando o usuário pede três direções para um card no contexto da página, variar um eixo e comparar trade-offs.
- Near-miss: auditoria geral de uma página sem necessidade de harness isolado; seguir auditoria por jornada, não acionar automaticamente os laboratórios.

## Limites

A revisão foi detalhada nas skills break, state-machine, variant, better-interface, better-typography e better-writing. As demais foram triadas pelo README do repositório, não representam auditoria linha a linha. Nenhum teste de UI real foi executado nesta avaliação, pois não foi fornecida aplicação alvo.
