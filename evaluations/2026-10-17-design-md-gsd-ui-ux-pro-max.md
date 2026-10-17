# Avaliação: VoltAgent DESIGN.md, GSD Core, UI UX Pro Max (2026-10-17)

## Grounding
Índice canônico: `ARSENAL INDEX.md`; stack aplicada: `arsenal-autopilot`. Consulta documental nos repositórios, sem executar instaladores/scripts. Repositórios originais e reposicionamento de GSD verificados.

| Fonte | Classe | Diagnóstico | Decisão/owner |
|---|---|---|---|
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | B | Biblioteca curada de DESIGN.md de marcas/produtos. Padrões de referência úteis, mas os documentos são análises secundárias e não fontes oficiais das marcas. | UPDATE_EXISTING: `skills/design-system-extraction/SKILL.md`. Uso como catálogo de exemplares com provenance, seleção pequena, reconciliação com implementação e respeito a marcas/licenças. |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) → [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | A/D | Repo original anuncia migração; versão ativa define Discuss → Plan → Execute → Verify → Ship, context engineering e artefatos de retomada; runtime de hooks/subagentes específico. | UPDATE_EXISTING: `stacks/software-engineering-cycle/STACK.md`. Fases e gates com contexto proporcional sem importar runtime. |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | A/D | Sistema de busca e recomendações por categoria, estilo, paleta, tipo e stack; CLI Python/Node e datasets externos. | UPDATE_EXISTING: `skills/ui-ux-catalog/SKILL.md` (já era owner canônico). Melhor discriminação entre catálogo, heurística, norma e síntese documental, com contrato de saída. |

## Segurança e portabilidade
- **VoltAgent: CAUTION como fonte de design.** Não copiar identidade, branding ou assets de terceiros; verificar contra originais e implementação.
- **GSD Core: CAUTION para runtime.** Installer cross-harness, prompts, hooks e coordenação de subagentes não foram executados. Sem supor contexts novos de 200k tokens ou workers persistentes.
- **UI UX Pro Max: CAUTION.** CLI, search.py, datasets e integradores não foram instalados. Documentação é uma entrada, não prova de qualidade estética ou conformidade WCAG.
- Sem auditoria completa de supply chain ou testes dinâmicos. Nenhuma credencial externa usada.

## Valor incremental
- Biblioteca de design como **fonte secundária** explicitamente verificada, em vez de clonar DESIGN.md.
- Fluxo de engenharia por milestones com discuss/plan/execute/verify/ship e orçamento de contexto; sem forçar cerimônia em tarefas pequenas.
- UI UX Pro Max v2 usado de maneira contextual, separando critérios objetivos de estilo/opinião e evitando falsos claims de execução do motor.

## Aceitação
- Should trigger DESIGN.md: pedido para documentar ou derivar referência visual de site existente. Near miss: inventar identidade de marca sem referência.
- Should trigger GSD phases: implementação extensa com entregas progressivas e retomada. Near miss: bug de uma linha.
- Should trigger UI UX catalog: escolher linguagem visual com direção ainda indefinida. Near miss: ajuste localizado mantendo sistema atual.
- QA dinâmico não realizado; a incorporação é metodológica.

## Publicação
Arquivos atualizados:
- `skills/design-system-extraction/SKILL.md` (commit `2805acd98b191760f448366f604ee534aed5d4ee`)
- `skills/ui-ux-catalog/SKILL.md` (commit `8de36d57dd379bdfbfd05df78d6410a1a466f279`)
- `stacks/software-engineering-cycle/STACK.md` (commit `f793e715a1b8f4105923fe69c9466e397fb315f6`)

O índice não mudou porque os owners e suas descriptions permanecem válidos. Este documento registra avaliação e limitações, sem alegar instalação dos runtimes de origem.
