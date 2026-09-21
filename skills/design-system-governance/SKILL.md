---
name: design-system-governance
description: "Criar ou evoluir design systems rastreando princípios, decisões, tokens, contratos de componentes e implementação."
---

# design-system-governance

## Objetivo

Criar e manter um sistema de design rastreável, em que princípios geram decisões, decisões geram tokens e contratos, e a implementação pode ser auditada contra essa cadeia.

## Workflow

1. Contexto: produto, público, stack, componentes e assets.
2. Filosofia: 3 a 7 princípios com trade-offs explícitos.
3. Decision table com ids estáveis.
4. Tokens derivados das decisões.
5. Component contracts com anatomia, estados, acessibilidade e slots.
6. Layout grammar.
7. Build usando o sistema como autoridade.
8. Audit da implementação.
9. Change governance: mudar contrato antes de propagar implementação.

## Contratos executáveis e diagnósticos

Quando o stack permitir lint/static enforcement, transformar apenas partes objetivas do design system em contratos:

- propriedades que consumidores podem alterar;
- propriedades que pertencem ao componente, como padding, shape e height;
- tokens e escalas válidas;
- arbitrary values proibidos;
- variants e states que devem ser usados em vez de restyle local.

Um erro deve ensinar o caminho correto: variant, token, parent layout ou owner do componente. Não transformar preferência estética subjetiva em lint rígido.

## Subsistema de ícones

Para famílias de ícones mantidas pelo produto:

- manter um source canônico por ícone;
- gerar SVG, React component, sprite e catálogo a partir dele;
- nunca editar artefatos gerados manualmente;
- definir grid, stroke, joins, optical balance, forms e naming em uma spec;
- buscar ícone existente ou neighbor antes de criar outro;
- validar a fonte e comparar visualmente com vizinhos em tamanhos e temas relevantes;
- build verde não substitui inspeção ótica;
- preservar licença e proveniência.

## Princípios

- decisão visual importante deve ser rastreável a uma razão;
- token sem decisão por trás é suspeito;
- não inventar componente quando já existe contrato equivalente;
- schema green não prova acessibilidade, factualidade, licença ou qualidade visual;
- autorização do design system continua pertencendo ao usuário/proprietário.

## Modelo de design

Ao materializar um design system de referência:
1. distinguir primitives de semantic tokens;
2. manter um design model como fonte única;
3. fazer component contracts apontarem para tokens e princípios;
4. justificar derived components;
5. validar contraste, token references e previews;
6. não afirmar que um fallback pertence à marca original sem evidência.

## Ferramentas e dependências

Não exigir oh-my-design, shadcn lint, Regen Icons ou formato compilado específico. Preservar decisões e rastreabilidade.

## Referências

Adaptada de https://github.com/kwakseongjae/oh-my-design.

Contratos agent-first inspirados em https://github.com/shadcn-ui/lint.

Governança de source e derivados para ícones inspirada em https://github.com/kazdenc/regen-icons.

Origem local: [design-system-governance.docx](../design-system-governance.docx).
