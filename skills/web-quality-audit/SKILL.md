---
name: web-quality-audit
description: "Auditar qualidade web em runtime com performance, acessibilidade, best practices e evidência reproduzível."
---

# web-quality-audit

## Objetivo

Auditar páginas e aplicações web em execução usando evidência reproduzível de performance, acessibilidade, comportamento e boas práticas, separando métricas de laboratório, padrões normativos e preferências de design.

## Quando usar

- auditoria de performance web;
- acessibilidade e navegação por teclado;
- revisão de componentes interativos;
- regressões após redesign;
- qualidade técnica de landing pages e web apps;
- preparação para release com budget/threshold explícito.

Não usar apenas para criar a interface. Para implementação e direção visual, usar `web-design-engineer`.

## Workflow

1. **Define surface** — páginas, fluxos, devices/viewports e condições de rede relevantes.
2. **Baseline** — registrar versão, ambiente e métricas antes de alterar.
3. **Automated audit** — usar Lighthouse ou ferramenta equivalente quando disponível.
4. **Accessibility semantics** — verificar HTML nativo, names/roles/states, focus, keyboard e padrões ARIA aplicáveis.
5. **Runtime flows** — executar interações críticas; combinar DOM, screenshot, network/state quando necessário.
6. **Performance diagnosis** — localizar causa de métricas ruins em network, JS, rendering, images, fonts, layout ou third parties.
7. **Prioritize findings** — impacto no usuário, evidência e custo de correção.
8. **Fix proportionally** — corrigir causa, não perseguir score isolado.
9. **Re-run same conditions** — comparar baseline vs candidate.
10. **Report limits** — distinguir lab result, field evidence ausente e itens não testados.

## Acessibilidade

- preferir HTML semântico nativo antes de ARIA;
- ARIA não corrige comportamento ausente;
- componentes interativos precisam de keyboard behavior coerente com seu padrão;
- focus order e focus visibility fazem parte da funcionalidade;
- accessible name, role e state devem corresponder ao que o controle realmente faz;
- testar reduced motion quando houver motion relevante;
- automated checks detectam parte dos problemas, não substituem interação manual.

Quando existir um padrão no WAI-ARIA Authoring Practices Guide, usar sua interação esperada como referência, mas não copiar ARIA quando um elemento HTML nativo resolve melhor.

## Performance

Separar:

- **lab metrics**: execução controlada, útil para regressão e diagnóstico;
- **field metrics**: comportamento observado por usuários reais, quando disponível;
- **synthetic score**: sinal agregado, nunca objetivo em si.

Ao comparar versões, manter condições equivalentes de device, viewport, cache, throttling e rota. Não vender variação de uma única execução como ganho estável.

## Evidência e findings

Cada finding deve incluir:

- superfície afetada;
- evidência observável;
- impacto;
- regra/contrato quando houver;
- correção provável;
- como verificar depois.

Separar:
- violação normativa;
- regressão mensurável;
- best-practice técnica;
- preferência estética.

## Ferramentas e dependências

Usar Lighthouse, DevTools, axe ou ferramentas já disponíveis quando adequadas. Não exigir instalação. Para comportamento real, combinar com navegador controlável e `runtime-ui-verification`.

## Integração

Combina com `web-design-engineer`, `runtime-ui-verification`, `seo-research-audit`, `gsap-animation` e `verify-before-claim`.

## Referências

Adaptada de:
- https://github.com/GoogleChrome/lighthouse
- https://github.com/w3c/aria-practices

Preserva a distinção entre auditoria automatizada, padrões de interação e verificação manual.
