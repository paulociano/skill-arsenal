---
name: shadcn-ui-engineering
description: "Implementar, atualizar e depurar componentes em projetos shadcn/ui preservando configuração, composição acessível e personalizações locais."
---

# shadcn-ui-engineering

## Quando usar

Projetos com shadcn/ui ou pedido explícito para adotá-lo. Não introduzir a biblioteca apenas para melhorar aparência.

## Processo

1. Leia `components.json`, manifesto, lockfile e componentes existentes. Determine aliases, framework, versão de Tailwind, gerenciador de pacotes, biblioteca de ícones e base de primitivas. Não suponha Radix nem caminhos `@/`.
2. Use o CLI disponível e compatível para obter contexto e URLs da documentação dos componentes; leia a documentação relevante antes de escolher APIs. Comandos como `info --json`, `docs`, `search`, `view` e `add --diff` dependem da versão: confirme suporte. Sem CLI, inspecione arquivos e documentação oficial e declare a limitação.
3. Reutilize componentes instalados, variantes e tokens semânticos. Consulte o registry configurado antes de criar equivalentes; resolva ambiguidade de origem somente quando houver escolhas materialmente diferentes.
4. Verifique o contrato de composição da base instalada: títulos acessíveis em overlays, grupos obrigatórios, associação de labels, validação e estados disabled/loading. Não importe componentes citados na documentação que ainda não existem no projeto.
5. Antes de atualizar, examine dry-run/diff e preserve alterações locais. Não execute atualização em massa ou troca de preset como efeito colateral de um ajuste pontual.
6. Leia os arquivos adicionados: confira aliases, imports, ícones, subcomponentes e dependências. Teste o fluxo afetado por teclado, abertura/fechamento, foco, validação e responsividade no runtime disponível.

## Dependências e limites

Node e gerenciador do projeto, CLI quando necessário e acesso à documentação/registry. Não use metadados `allowed-tools` de outro agente nem presuma execução de comandos embutidos em Markdown. Ler esta skill não instala pacotes. Antes de executar um CLI remoto, confira origem e versão; não force `latest` em um projeto cuja compatibilidade exija outra versão.

Adapte orientações estéticas ao design system existente. Não transforme convenções de classes Tailwind em requisitos universais de acessibilidade.

## Fonte

[shadcn/ui — skill oficial](https://github.com/shadcn-ui/ui/blob/main/skills/shadcn/SKILL.md). Adaptação metodológica própria; consulte as referências da fonte somente conforme o componente ou operação.
