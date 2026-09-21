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

## Skills canônicas, adapters e distribuições

Quando uma mesma coleção de skills precisa funcionar em vários harnesses ou plugins:

- manter uma única árvore canônica de skills e referências;
- manter conteúdo reutilizável e metodologia harness-neutral;
- colocar configuração específica de cada host em adapters, manifests ou wrappers separados;
- tratar dist, bundles e branches geradas como artefatos derivados, não como fonte de verdade;
- reconstruir distribuições a partir da origem canônica em vez de editar cópias geradas;
- separar famílias por audiência real, por exemplo: desenvolver extensão, operar ambiente existente, contribuir no produto ou usar uma skill embarcada;
- não expor a mesma skill a todas as audiências só porque ela existe no mesmo repositório;
- usar rotas explícitas para impedir que uma skill de desenvolvimento seja chamada para leitura de dados ou que uma skill de leitura altere configuração.

Para integrações com workspace ou sistemas externos:

- separar operação read/inspect de customize/write quando isso reduzir risco;
- URLs, tokens e credenciais específicas do usuário ficam em configuração privada, não em distribuição compartilhada;
- destructive/deploy/production actions precisam de boundary explícito de aprovação;
- um alvo self-hosted ou custom domain é válido quando o contrato do produto permite; não hardcode o SaaS do fornecedor como único destino.

## Regras gerais

- estrutural green não prova preservação semântica;
- não forçar arquitetura em pastas num projeto pequeno;
- plano não pode expandir o escopo pedido;
- commit não é push; push não é PR; PR aprovado não é merge;
- se a evidência muda a premissa, replanejar;
- usar preview e rollback quando possível.

## Ferramentas e dependências

Usar arquivos, terminal e conectores reais disponíveis. Adaptadores específicos de agentes devem apontar para conteúdo canônico. Não exigir Abide, Jev, Twenty, Codex plugin ou scaffolds externos.

## Integração

skill-builder, graph-engineering, to-spec, verify-before-claim, retrospective-codify.

## Referências

Adaptada de WoJiSama/skill-based-architecture.

Classificação de enforceability e rastreabilidade de regras adaptadas de https://github.com/coldteadotai/abide, especialmente abide-compile, sem hooks ou dependência de Jev.

Separação entre skills canônicas, distribuições geradas, adapters de harness e audiências adaptada de https://github.com/twentyhq/twenty, especialmente SKILLS.md e packages/twenty-agent-skills, sem importar o CLI, MCP ou runtime do Twenty.

Origem local: [project-skill-architecture.docx](../project-skill-architecture.docx).
