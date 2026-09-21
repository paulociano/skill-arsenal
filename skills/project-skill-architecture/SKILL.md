---
name: project-skill-architecture
description: "Organizar ou migrar regras e workflows de projetos em skills pequenas, com proprietários canônicos e rotas sem duplicação."
---

# project-skill-architecture

## Objetivo

Organizar regras, workflows e conhecimento operacional em uma arquitetura pequena, roteável e verificável, preservando significado e evitando duplicação entre AGENTS.md, CLAUDE.md e outros shells.

## Princípio central

Uma regra importante deve ter um owner canônico; shells específicos só carregam o mínimo necessário para chegar nele.

## Workflow

1. Inventariar entradas e owners.
2. Separar intenção do usuário, regra de negócio, contrato arquitetural, fato de implementação, evidência runtime e conclusão histórica.
3. Detectar duplicações e conflitos.
4. Escolher a menor forma física suficiente.
5. Mapear cada cláusula para preserve, merge, move ou exclude com justificativa.
6. Fazer preview read-only antes de escrever.
7. Materializar owners e routes apenas quando justificados.
8. Preservar semanticamente instruções existentes.
9. Verificar coverage, reachability, source-to-destination mapping e behavior quando possível.
10. Registrar learning reutilizável somente quando muda ação futura.

## Compilar regras em checks

Antes de automatizar uma regra, classificar como ela pode ser verificada:

1. lint/static: AST, regex ou linter detecta deterministicamente;
2. mechanical/deferred: exige contagem, medição ou script;
3. semantic/model: o diff ou artefato contém contexto suficiente para uma pergunta estreita;
4. repository-context/deferred: exige conhecer o restante do codebase;
5. process/unenforceable: regra é sobre conversa, aprovação ou processo, não sobre o código isolado.

Regras:
- extrair somente instruções realmente presentes;
- manter source path/line ou locator equivalente;
- não fundir regras diferentes em uma pergunta vaga;
- para semantic/model, perguntar sobre evidência observável;
- escolher o momento correto: edit/hunk ou diff final;
- calibrar checks semânticos com exemplos reais quando houver histórico;
- check fraco ou noisy deve ser reescrito ou desativado;
- judge não substitui linter para o que pode ser checado deterministicamente.

## Regras gerais

- estrutural green não prova preservação semântica;
- não forçar arquitetura em pastas num projeto pequeno;
- plano não pode expandir o escopo pedido;
- commit não é push; push não é PR; PR aprovado não é merge;
- se a evidência muda a premissa, replanejar;
- usar preview e rollback quando possível.

## Ferramentas e dependências

Usar arquivos, terminal e conectores reais disponíveis. Adaptadores específicos de agentes devem apontar para conteúdo canônico. Não exigir Abide, Jev ou scaffolds externos.

## Integração

skill-builder, graph-engineering, to-spec, verify-before-claim, retrospective-codify.

## Referências

Adaptada de WoJiSama/skill-based-architecture.

Classificação de enforceability e rastreabilidade de regras adaptadas de https://github.com/coldteadotai/abide, especialmente abide-compile, sem hooks ou dependência de Jev.

Origem local: [project-skill-architecture.docx](../project-skill-architecture.docx).
