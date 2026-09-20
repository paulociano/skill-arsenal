---
name: design-system-governance
description: "Criar ou evoluir design systems rastreando princípios, decisões, tokens, contratos de componentes e implementação."
---

# design-system-governance

## Objetivo

Criar e manter um sistema de design rastreável, em que princípios geram decisões, decisões geram tokens e contratos, e a implementação pode ser auditada contra essa cadeia.

## Quando usar

- criação ou evolução de design system;
- produtos com várias telas/componentes que precisam de consistência;
- redesign em que decisões visuais precisam ser explicáveis e reutilizáveis;
- handoff entre sessões, pessoas ou agentes.

## Workflow

1. **Contexto:** entender produto, público, tarefas primárias, stack, componentes existentes e assets reais.
2. **Filosofia:** declarar 3–7 princípios de design, cada um com trade-off explícito; princípio sem sacrifício vira decoração.
3. **Decision table:** registrar decisões importantes com id estável e racional curto.
4. **Tokens:** derivar cor, tipografia, spacing, radius, motion e demais tokens a partir dessas decisões, evitando valores sem justificativa.
5. **Component contracts:** para cada componente, registrar anatomia, estados aplicáveis/não aplicáveis, acessibilidade e slots de tokens.
6. **Layout grammar:** documentar padrões de composição e regras responsivas.
7. **Build:** implementar usando o sistema como autoridade local.
8. **Audit:** comparar implementação real com decisões, tokens, estados, acessibilidade e comportamento.
9. **Change governance:** quando uma preferência ou necessidade nova mudar o sistema, atualizar primeiro a decisão/contrato relevante e só então propagar para implementação.

## Princípios

- Toda decisão visual importante deve ser rastreável a uma razão.
- Um token sem decisão por trás é suspeito.
- Um componente não deve ser inventado do zero quando já existe contrato ou padrão equivalente aprovado.
- Estados não aplicáveis devem ser explicitamente marcados como tal, com motivo.
- Mudanças de autoridade/design system devem respeitar as decisões e a autorização do usuário/proprietário; o agente não pode conceder a si mesmo autorização adicional.
- Verificação de schema/compilação não prova acessibilidade, factualidade, licença ou qualidade visual; essas dimensões precisam de evidência própria.

## Modelo de design

Ao materializar um design system a partir de referência:

1. distinguir primitives de semantic tokens;
2. manter um **design model** como fonte única das decisões antes dos artefatos derivados;
3. component contracts devem apontar para tokens e princípios;
4. derived components precisam de justificativa explícita quando não foram observados;
5. validar contraste, token references, placeholders e consistência entre modelo e previews quando o runtime permitir;
6. brand inspiration não autoriza afirmar que o kit/icon/font fallback é usado pela marca original.

## Ferramentas e dependências

Manter decisões, tokens e contratos em arquivos do projeto ou destino conectado escolhido pelo usuário. Não exigir CLI oh-my-design, .omd, hooks ou formato compilado. Preservar a rastreabilidade e decisões do proprietário, respeitando a autorização já dada.

## Referências

Adaptada de [oh-my-design](https://github.com/kwakseongjae/oh-my-design), especialmente `omd-init`, `omd-autopilot`, `DESIGN.md` Core v2 e a cadeia philosophy → decisions → tokens → component contracts → layout grammar → build → critique.

Origem local: [design-system-governance.docx](../design-system-governance.docx).
