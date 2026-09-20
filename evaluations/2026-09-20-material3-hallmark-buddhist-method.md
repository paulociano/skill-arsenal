# Avaliação: Material 3, Hallmark e Buddhist Method

Data: 2026-09-20. Workflow evaluate-and-import-skill, revisão manual conforme skill-security-review e adaptação segundo skill-creator. Fonte canônica do Arsenal consultada antes da seleção. Publicação autorizada pelo AGENTS.md.

## Decisão e rastreabilidade

| Fonte | Classe | Aplicação |
|---|---|---|
| [hamen/material-3-skill](https://github.com/hamen/material-3-skill/blob/14385f2bf3804d8779f8b4db2604211f1e70b4c1/skills/material-3/SKILL.md) | D — técnica | Atualizar material-design-3, já derivada da mesma fonte |
| [nutlope/hallmark](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/SKILL.md) | A — workflow útil | Adaptar seleção estrutural em referência de web-design-engineer e ajustar landing-craft |
| [nai0om/buddhist-method](https://github.com/nai0om/buddhist-method/blob/745caa74ef27fce7c57cbdbf27af5add3de884d7/SKILL.md) | B — boa metodologia | Incorporar incrementalmente a diagnosing-bugs; sem skill separada |

Revisões observadas:
- hamen/material-3-skill: commit `14385f2bf3804d8779f8b4db2604211f1e70b4c1`; blob principal `7619bf0720dfafd2e7f422f00ad442c85c2abb6a`.
- nutlope/hallmark: commit `13ac0ec7e148655948100b6396439e481361d690`; blob principal `645221da63743de870501760a48694acdf7aef10`.
- nai0om/buddhist-method: commit `745caa74ef27fce7c57cbdbf27af5add3de884d7`; blob principal `6f8dd2956739c5da8e567a6382ba7596eecb204f`.

## Material 3

A skill existente material-design-3 já declara hamen/material-3-skill como origem. Não há justificativa para duplicar. O upstream acrescenta uma biblioteca longa de tokens, componentes, exemplos e roteamento por tema/plataforma; é útil em implementação MD3, sobretudo quando já há projeto e versão identificados. Depende do SDK/biblioteca da plataforma para executar interfaces, não do plugin de Claude.

Preservado o método: papéis semânticos pareados, tema dinâmico com fallback, adaptação de janela/navegação e distinção entre guideline e API disponível. Adicionado contrato de evidência de auditoria, separando não aplicável, não verificado e falha. Não copiadas tabelas estáticas de suporte/valores, tags web sem verificar pacote, opt-ins ou afirmações sobre updates recentes. Cada uso concreto deverá verificar documentação oficial da versão. Auditoria numérica 0–100 rejeitada como substituto de evidência.

Escopo lido: SKILL.md completo e licença; árvore para verificar dependências. Referências extensas e scripts de CI não auditados nem executados. Combina com library-version-grounding, runtime-ui-verification e skills nativas já roteadas.

## Hallmark

É uma skill de design com quatro modos (construir, auditar, redesenhar, estudar), catálogo documental de estruturas/temas e revisão. Não é um gerador de logos nem um runtime obrigatório. O ganho real sobre instruções estéticas genéricas é escolher forma de página conforme o conteúdo antes de escolher a superfície visual, e distinguir trabalho de componente de trabalho de página. Classificação A pelo processo; boa parte do catálogo e das regras de gosto continua dispensável no Arsenal.

Adotada referência compacta com escopo, escolha estrutural, estados pertinentes e evidências. landing-craft deixa de impor 6–8 seções e passa a dimensionar o storyboard pelo conteúdo. Mantidos os donos existentes web-design-engineer e landing-craft, sem instalar toda a biblioteca ou criar outra stack.

Retirados: pergunta obrigatória mesmo com briefing completo; rotação automática de navegação/tema entre páginas do mesmo produto; proibições universais de fontes/itálicos; oito estados para qualquer componente; overflow global recortado como garantia de responsividade; CSS append-only; memória e exports obrigatórios; score subjetivo como prova; falsas equivalências entre fonte declarada e fonte renderizada. A fonte tem inconsistências de contagem/ordem de gates (57/58 e resultado de QA solicitado no preview anterior ao build), que não foram transpostas.

Dependências: instruções e referências em Markdown; ferramentas de edição/browser conforme tarefa. package.json lido não instala motor de design, e seu script serve o site de demonstração com Python. Serviços externos citados em referências não são requisitos da adaptação. Não importados exemplos de site, imagens, catálogos, scripts ou API keys.

Escopo lido: README, SKILL.md completo, structure.md, contract.md, package.json e licença. As demais referências do catálogo foram inventariadas, não auditadas integralmente. Combina com extração/governança de design e runtime UI já presentes.

## Buddhist Method

A fonte usa conceitos budistas como mnemônicos para verificar fatos, buscar causas, atualizar estado, rever uma abordagem e manter critério sob contestação. Funciona como disciplina textual, sem ferramentas ou dependências externas. Sua utilidade está no checklist operacional, não em comprovação religiosa ou superioridade empírica demonstrada.

O Arsenal já possui diagnosing-bugs e verify-before-claim. O valor incremental adotado em diagnosing-bugs é detectar retries sem informação, diferenciar mitigação de correção causal e reavaliar evidências sob contestação. Mantida atribuição da origem, sem tornar terminologia religiosa obrigatória ou adicionar gatilho global a toda tarefa.

Não importados: releitura ritual de todo estado, proibição absoluta de tratamento defensivo, varredura de bugs fora do escopo, número rígido de tentativas ou insistência contra o usuário sem reavaliar contexto. Os limites da hipótese e da mitigação devem ser explícitos.

Escopo lido: SKILL.md e as duas referências ariyasacca-debug.md e extended-principles.md, mais LICENSE. Comparação com as skills atuais de diagnóstico e verificação. Classificação B; não criada skill duplicada.

## Segurança, licenças e validação

APPROVE para as adaptações documentais. Não identificadas instruções de exfiltração nos textos lidos; essa conclusão é limitada ao escopo examinado. Nenhum instalador ou código upstream executado, nenhuma API de geração externa acionada. Revisão manual/semântica, sem scanner automatizado. Todas as três fontes têm licença MIT lida e preservada junto aos recursos adaptados, com aviso de modificação e links de origem.

Sem novas skills, renomeações ou mudanças de description: o índice continua correto. Foram alterados quatro SKILL.md existentes, acrescentada uma referência metodológica, preservadas três licenças e criado este registro (nove arquivos). Validação estrutural dos frontmatters e links novos, conferência de alterações concorrentes e leitura após publicação. Não há aplicativo alterado nem alegação de teste visual/SDK nesta entrega.
