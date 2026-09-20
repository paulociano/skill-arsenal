---
name: material-design-3
description: "Implementar ou auditar interfaces Material Design 3 em Compose, Flutter ou web conforme a plataforma e versão reais."
---

# material-design-3

## Objetivo

Projetar, implementar e auditar interfaces segundo Material Design 3, com foco principal em Jetpack Compose e suporte secundário a Flutter e web quando apropriado.

## Quando usar

- Material Design 3 / Material You;
- Jetpack Compose Material3;
- temas e ColorScheme;
- componentes MD3;
- layouts adaptativos;
- acessibilidade;
- auditoria de conformidade MD3;
- Flutter com Material 3;
- web que use tokens Material.

## Princípios

1. **Material é um sistema, não um kit de componentes.**
2. Tokens semânticos vencem cores/tamanhos hardcoded.
3. Layout precisa responder a janela/form factor, não apenas “telefone”.
4. Componentes e motion precisam respeitar a plataforma real.
5. Guidance de versão/API precisa ser verificado na documentação oficial atual.

## Workflow

1. Detectar plataforma e versão instalada.
2. Aplicar `library-version-grounding`.
3. Identificar objetivo:
   - componente;
   - tema;
   - navegação;
   - layout;
   - scaffold;
   - audit.
4. Usar tokens semânticos:
   - color roles;
   - typography roles;
   - shapes;
   - elevation/surface;
   - motion.
5. Verificar adaptive layout, insets, dark mode, contrast e accessibility.
6. No Compose, preferir APIs Material3 compatíveis com a BOM/versão real.
7. No Flutter, usar Material 3 conforme a versão real do Flutter.
8. Na web, tratar suporte como específico do ecossistema atual; não assumir paridade com Compose.
9. Auditar contra implementação real.
10. Verificar visual/runtime antes de afirmar conformidade.

## Auditoria

Avaliar, quando aplicável:

- color tokens;
- typography;
- shape;
- elevation/surfaces;
- components;
- layout/adaptivity;
- navigation;
- motion;
- accessibility;
- theming/dark mode.

Não transformar o audit em score teatral. Findings precisam apontar evidência e fix.

## Expressive / mudanças recentes

Material 3 evolui. Conceitos como expressive motion, adaptive scaffolds e componentes novos podem variar por plataforma e versão. Consultar documentação oficial atual quando a resposta depender disso.

## Regras

- não impor valores de snapshot antigo quando a API/spec mudou;
- não usar componentes Material fora de contexto apenas para “parecer Material”;
- não confundir design guideline com API disponível;
- não afirmar suporte Web/Flutter/Compose sem verificar a plataforma;
- preservar identidade da marca dentro dos roles/tokens do sistema quando possível.

## Ferramentas e dependências

Não depender do plugin/CLI original. Usar código, screenshots, browser e ferramentas disponíveis. Para Android/Flutter específicos, combinar com `compose-performance-audit` ou `crossplatform-mobile-engineering`.

## Integração

- `design-system-governance`
- `crossplatform-mobile-engineering`
- `compose-performance-audit`
- `runtime-ui-verification`
- `library-version-grounding`

## Referências

Adaptada de hamen/material-3-skill.

Origem local: [material-design-3.docx](../material-design-3.docx).
