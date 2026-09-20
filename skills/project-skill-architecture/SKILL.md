---
name: project-skill-architecture
description: "Organizar ou migrar regras e workflows de projetos em skills pequenas, com proprietários canônicos e rotas sem duplicação."
---

# project-skill-architecture

## Objetivo

Organizar regras, workflows e conhecimento operacional de um projeto em uma arquitetura de skills pequena, roteável e verificável, preservando significado e evitando duplicação entre AGENTS.md, CLAUDE.md, Cursor rules e outros shells.

## Quando usar

- regras espalhadas ou contraditórias;
- SKILL.md grande demais;
- vários harnesses repetindo a mesma regra;
- workflows recorrentes sem owner claro;
- necessidade de migrar regras para skills sem perder semântica.

## Princípio central

**Uma regra importante deve ter um owner canônico; shells de ferramenta só carregam o mínimo necessário para chegar nele.**

## Workflow

1. Inventariar entradas existentes e seus owners.
2. Separar:
   - intenção do usuário;
   - regra de negócio;
   - contrato arquitetural;
   - fato de implementação;
   - evidência runtime;
   - conclusão histórica.
3. Detectar duplicações e conflitos.
4. Escolher a menor forma física suficiente:
   - single-file;
   - folder-light;
   - routed/broad somente quando pressão real justificar.
5. Mapear cada cláusula de origem para:
   - preserve;
   - merge;
   - move;
   - exclude com justificativa.
6. Fazer preview read-only de CREATE / PRESERVE / CONFLICT antes de escrever.
7. Materializar owners e routes somente quando admitidos pela evidência.
8. Preservar semanticamente instruções existentes.
9. Verificar:
   - inventory coverage;
   - route reachability;
   - source→destination mapping;
   - completion criteria;
   - behavior/runtime quando possível.
10. Registrar learning reutilizável somente quando muda ação futura.

## Regras

- estrutural green não prova semantic preservation;
- não forçar folder architecture em projeto pequeno;
- não pedir ao usuário para escolher tiers internos;
- plano não pode expandir o escopo pedido;
- commit não é push; push não é PR; PR aprovado não é merge;
- se evidência muda a premissa, replanejar em vez de manter aparência linear;
- preview e rollback quando o runtime permitir.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Usar Agent Skills em pastas com SKILL.md como conteúdo canônico; adaptadores específicos de agentes só apontam para esse conteúdo. Não exigir scaffolds do repositório original.

## Integração

- skill-builder
- graph-engineering
- to-spec
- verify-before-claim
- retrospective-codify

## Referências

Adaptada de WoJiSama/skill-based-architecture.

Origem local: [project-skill-architecture.docx](../project-skill-architecture.docx).
