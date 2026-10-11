---
name: improve-existing-web-app
description: Melhora uma aplicação web existente preservando funcionalidades, refinando design e validando o resultado no runtime.
---

# Improve Existing Web App

## Objetivo
Melhorar uma aplicação web existente sem reconstruí-la desnecessariamente.

## Skills candidatas
- design-system-extraction
- design-principles-audit
- web-quality-audit
- web-design-engineer
- shadcn-ui-engineering
- ui-ux-catalog
- gsap-animation
- runtime-ui-verification
- verify-before-claim

As skills são candidatas, não obrigatórias.

## Workflow
1. Entenda a estrutura, framework, componentes e restrições atuais. Para melhoria decorrente de auditoria, mapear jornadas, estados críticos e baseline antes de editar.
2. Use `design-system-extraction` quando for importante compreender o sistema visual existente.
3. Se o pedido envolver auditoria ou redesign motivado por problemas de uso, aplique `design-principles-audit` para gerar findings com evidência, severidade, confiança e critérios de aceite; use `web-quality-audit` apenas para acessibilidade, performance e critérios técnicos aplicáveis. Não fingir observação de runtime a partir de screenshot ou código.
4. Use `web-design-engineer` para implementar melhorias de UI, layout, responsividade e experiência.
   Acione `shadcn-ui-engineering` somente em projetos shadcn, `ui-ux-catalog` quando faltar referência de design e `gsap-animation` quando a animação exigir essa biblioteca. Não instale dependências apenas porque a skill está listada.
5. Use `runtime-ui-verification` quando a aplicação puder ser executada e inspecionada.
6. Use `verify-before-claim` quando houver afirmações de conclusão, correção ou qualidade.

## Regra de parcimônia
Não execute todas as skills automaticamente. Use somente as necessárias para a tarefa atual.

## Gate de reauditoria

Quando a tarefa incluir correção de findings, mantenha IDs, baseline e critérios de aceite. Após as mudanças, reexecute jornadas e estados equivalentes (incluindo mobile, teclado, loading, erro e empty quando material); registre PASS/FAIL/UNKNOWN/NA por finding, novas regressões e pendências. Não declarar a auditoria concluída sem acesso/teste adequado. Testes automatizados e snapshots são complementares a inspeção e pesquisa com usuários.
