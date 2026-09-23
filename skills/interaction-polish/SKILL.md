---
name: interaction-polish
description: "Refinar o último nível de qualidade de uma interface por microinterações, feedback, estados, tipografia animada e comportamento contextual sem transformar polish em decoração excessiva."
---

# interaction-polish

## Objetivo

Fazer a passagem final de qualidade percebida depois que estrutura, conteúdo e design system já estão corretos. Foca nos pequenos comportamentos que tornam a interface clara, responsiva e intencional.

## Quando usar

- interface funcional que ainda parece rígida ou incompleta;
- revisão final de landing pages, dashboards e produtos;
- hover/press/focus, disclosure, menus, tooltips, dialogs, counters e text transitions;
- pedido de "mais premium", "mais fluido", "mais contemporâneo" quando o problema não exige redesign estrutural.

## Inventário de polish

Revisar apenas os grupos relevantes:

1. **Input feedback** — hover, press, focus, drag, selected, disabled.
2. **State change** — loading, success, error, empty, optimistic, save/undo.
3. **Disclosure** — accordion, popover, menu, tooltip, dialog, drawer.
4. **Navigation continuity** — tabs, route changes, breadcrumbs, back/forward.
5. **Data change** — números, charts, counters, progress.
6. **Typography motion** — line/word/character transitions quando têm função narrativa.
7. **Contextual positioning** — floating UI, collision, viewport boundaries.
8. **Ambient detail** — texture, background motion, cursor/spotlight somente quando suportam a direção.

## Workflow

1. Confirmar que hierarquia, conteúdo e layout já estão resolvidos.
2. Mapear interações mais frequentes e mais críticas.
3. Garantir primeiro clareza de estado e acessibilidade sem animação.
4. Adicionar feedback imediato a ações.
5. Preservar continuidade entre estados relacionados.
6. Para overlays/floating UI, verificar foco, escape, outside-click, collision e retorno de foco.
7. Para dados mutáveis, animar mudança sem atrasar compreensão ou criar falsa precisão.
8. Para tipografia, escolher nível de split apenas quando o efeito justifica custo e complexidade.
9. Aplicar motion consistente via ui-motion-design e biblioteca já presente.
10. Revisar densidade de efeitos: remover os que competem entre si.
11. Testar teclado, toque, reduced motion e latência percebida.
12. Comparar antes/depois no runtime.

## Regras

- Polish não corrige arquitetura ruim.
- Hover nunca pode ser a única forma de descobrir uma ação essencial.
- Focus visível não deve ser removido em nome de estética.
- Tooltips não devem carregar informação indispensável que usuários touch não conseguem acessar.
- Microinteração boa reduz ambiguidade, confirma causalidade ou preserva continuidade.
- Não aplicar glow, blur, marquee, cursor customizado, animated border ou text reveal como checklist universal.
- Usar Radix/Floating UI/primitivas equivalentes como referência comportamental quando o projeto já adota essas famílias; não introduzir dependências sem necessidade.

## Integração

web-design-engineer, ui-motion-design, shadcn-ui-engineering, runtime-ui-verification e web-quality-audit.

## Origem metodológica

Adaptada de Motion Primitives, Animate UI, React Bits, Magic UI, Kokonut UI, Radix Primitives, Floating UI e Number Flow. O Arsenal importa padrões de comportamento e revisão, não catálogos visuais inteiros.
