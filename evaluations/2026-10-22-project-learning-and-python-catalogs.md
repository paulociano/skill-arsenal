# Avaliação de quatro catálogos de aprendizagem e engenharia (2026-10-22)

## Escopo e fontes
Avaliação de READMEs da branch padrão consultados pelo conector GitHub em 2026-10-22, comparados com `ARSENAL INDEX.md`, `skills/teach/SKILL.md` e `skills/system-design-engineering/SKILL.md`.

- https://github.com/codecrafters-io/build-your-own-x
- https://github.com/donnemartin/system-design-primer
- https://github.com/vinta/awesome-python (o usuário encaminhou a visualização https://www.star-history.com/vinta/awesome-python/)
- https://github.com/practical-tutorials/project-based-learning

## Decisões por fonte

| Fonte | Classe | Ação | Motivo |
| --- | --- | --- | --- |
| build-your-own-x | B | UPDATE_EXISTING (já referenciada, refinamento) | Catálogo de tutoriais de reconstrução de tecnologias; `teach` já usa a abordagem, faltava triagem formal de projetos. |
| system-design-primer | B | KEEP_EXTERNAL_REFERENCE | `system-design-engineering` já declara adaptação direta desta fonte e cobre requisitos, escala, trade-offs, falhas e operações. Sem lacuna incremental evidente após confronto. |
| awesome-python | B/D | UPDATE_EXISTING (descoberta de ferramentas) | Índice de bibliotecas Python, não skill executável. Adicionar gate de seleção/segurança ao contexto de aprendizado; não instalar nenhum pacote ou assumir compatibilidade. |
| project-based-learning | B | UPDATE_EXISTING | Índice de tutoriais de aplicação por linguagem. Complementa reconstrução de fundamentos com projetos ponta a ponta e checkpoints verificáveis. |

## Capability ledger e ownership
- **Seleção de projetos por objetivo, pré-requisitos, granularidade e teste**: owner `skills/teach/SKILL.md`, seção "Seleção de projetos e bibliotecas de referência". Adição incremental publicada nesta branch.
- **Diferenciar reconstrução didática de aplicação ponta a ponta**: mesmo owner e seção.
- **Curadoria de frameworks/bibliotecas a partir de catálogo**: mesmo owner para contexto educacional; engenharia de produção continua com owners técnicos existentes, não com o catálogo.
- **System design com estimativas e trade-offs**: owner existente `skills/system-design-engineering/SKILL.md`; nenhuma edição necessária.

## Segurança, licença e portabilidade
Leitura estática de READMEs como material de referência, sem executar tutoriais, instaladores, scripts, pacotes ou downloads de terceiros. As páginas compilam links externos de manutenção, segurança e licença heterogêneas; presença numa lista não atesta qualidade. Revisar licença, atualidade, dependências e comandos na fonte primária **para cada projeto selecionado**, antes de executar ou redistribuir. Nenhum conector, runtime ou ferramenta externa é pressuposto. A classificação D parcial de awesome-python reflete que cada biblioteca concreta pode exigir ambiente e permissões não disponíveis.

**Veredito:** APPROVE como referências de descoberta e metodologia de curadoria; CAUTION para execução futura de qualquer projeto ou pacote apontado. Revisão não constitui auditoria individual de todos os links.

## Implementação e verificação
- Arquivo alterado: `skills/teach/SKILL.md`.
- Arquivo de avaliação: `evaluations/2026-10-22-project-learning-and-python-catalogs.md`.
- Não criar nova skill nem alterar o índice, pois nenhuma description/rota canônica mudou.
- Branch de trabalho: `eval/project-learning-catalogs-20261022`; `master` não é alvo desta avaliação.
- Verificação planejada: reler arquivos na branch e comparar com master; validação estática do frontmatter e dos links internos. Não há teste de runtime a executar para mudanças documentais.
