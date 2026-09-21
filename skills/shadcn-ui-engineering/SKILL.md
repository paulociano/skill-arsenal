---
name: shadcn-ui-engineering
description: "Implementar, atualizar e depurar componentes em projetos shadcn/ui preservando configuração, composição acessível e personalizações locais."
---

# shadcn-ui-engineering

## Quando usar

Projetos com shadcn/ui ou pedido explícito para adotá-lo. Não introduzir a biblioteca apenas para melhorar aparência.

## Processo

1. Ler components.json, manifesto, lockfile e componentes existentes.
2. Confirmar framework, Tailwind, aliases, package manager, icons e primitivas.
3. Usar CLI/documentação compatíveis com a versão real.
4. Reutilizar componentes, variants e tokens existentes.
5. Verificar contratos de composição e acessibilidade.
6. Antes de atualizar, examinar dry-run/diff e preservar customizações locais.
7. Ler arquivos adicionados e testar teclado, foco, validação e responsividade.

## Design-system lint

Quando o projeto já usa ou autoriza um linter capaz de expressar contratos visuais:

- codificar somente regras objetivas do sistema;
- permitir layout local onde o contrato permitir sem liberar restyle total;
- fazer diagnostics explicarem o que usar no lugar: size, variant, token, margin/gap no parent ou mudança no owner;
- combinar component ownership com theme scale quando necessário;
- custom messages devem apontar para o contrato real;
- lint green prova apenas conformidade com essas regras, não acessibilidade ou qualidade visual total.

Não instalar shadcn lint automaticamente. Se estiver presente, ler a configuração antes de alterá-la.

## Dependências e limites

Ler esta skill não instala pacotes. Confirmar origem e versão antes de executar CLI remoto. Não forçar latest. Não transformar convenções Tailwind em requisitos universais de acessibilidade.

## Fonte

https://github.com/shadcn-ui/ui/blob/main/skills/shadcn/SKILL.md

Contratos de lint agent-first adaptados de https://github.com/shadcn-ui/lint, sem dependência obrigatória.
