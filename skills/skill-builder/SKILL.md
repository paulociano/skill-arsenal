---
name: skill-builder
description: "Criar ou atualizar skills reutilizáveis a partir de workflows recorrentes, com gatilhos claros, dependências reais e validação."
---

# skill-builder

## Objetivo

Transformar um workflow repetitivo do usuário em uma skill reutilizável, com gatilhos claros, escopo estreito, dependências explícitas, aprovações e verificação final.

## Quando usar

- O usuário repete um processo em várias conversas.
- Existe uma sequência estável de passos.
- O workflow usa arquivos, plugins, apps ou ferramentas de forma recorrente.
- Vale transformar decisões e aprovações em procedimento reutilizável.

## Descoberta

Capturar somente o que muda materialmente o workflow:

- resultado e gatilhos;
- entradas e fontes;
- passos em ordem;
- ferramentas e dependências;
- decisões autônomas versus decisões que exigem o usuário;
- approval gates;
- saída final e critérios de verificação;
- falhas comuns e proibições;
- regras de privacidade e credenciais.

## Workflow

1. Restatar o workflow proposto em ordem.
2. Separar passos read-only de ações que alteram sistemas externos.
3. Resolver ambiguidades relevantes.
4. Se a fonte foi escrita para Claude, Claude Code ou outro agente, converter a skill para capacidades reais do ambiente antes de salvá-la.
5. Mapear cada dependência da fonte para uma destas categorias: equivalente nativo do ambiente, plugin, terminal ou conector disponível, adaptação metodológica sem ferramenta, ou dependência sem equivalente.
6. Remover comandos e convenções específicas do agente de origem (`Skill tool`, slash commands, `.claude/`, `CLAUDE.md`, hooks, background agents etc.) quando não forem suportados aqui.
7. Criar uma skill focada, sem placeholders e sem prometer capacidades indisponíveis.
8. Manter credenciais fora das instruções compartilháveis.
9. Preservar approval gates e critérios de conclusão da metodologia original.
10. Fazer threat-surface review proporcional ao poder da skill: files, network, credentials, shell, persistence, MCP/tools, outward-facing actions e broad triggers.
11. Reduzir permissões e ferramentas ao mínimo necessário; não copiar permissões do agente de origem por conveniência.
12. Para código/fonte externa não confiável, não executar installer/setup apenas para construir ou avaliar a skill.
13. Testar com exemplo seguro e não destrutivo.
14. Verificar resultado e dependências.
15. Validar trigger boundaries com dois conjuntos: **should-trigger** e **near-miss should-not-trigger**.
16. Quando possível, comparar **with-skill vs baseline without-skill** em cenários realistas para provar valor incremental.
17. Se uma skill crescer demais, aplicar progressive disclosure: metadata pequena, corpo operacional focado e referências carregadas somente quando necessárias.
18. Antes de criar nova skill, verificar overlap semântico com skills existentes e preferir generalizar/atualizar a duplicar.
19. Quando a mesma lógica determinística aparecer repetidamente nos testes, considerar helper/script reutilizável somente se o runtime real suportar isso.

## Source-to-skill ledger e prova

Ao extrair múltiplas capacidades de artigo, tutorial, coleção ou prompt pack, criar antes um ledger simples:

| Source fragment | Reusable capability | Keep | Remove | Existing owner/new skill | Proof |
| --- | --- | --- | --- | --- | --- |

Regras:
- uma capability reutilizável por skill, salvo quando separar destrói o workflow;
- atualizar owner existente quando ele já cobre o contrato;
- remover brand, copy, assets e layout incidentais;
- manter mechanics, state transitions, defaults, accessibility, failure modes e acceptance checks quando forem portáveis;
- para skill visual/interativa, uma demo executável pode ser melhor prova que uma descrição;
- para workflow não visual, usar input + expected-output ou cenário equivalente;
- screenshot sozinho não prova interação;
- demo não é requisito universal: só criar quando reduz ambiguidade ou prova comportamento relevante.

## Versionamento e validação de evolução

- criar mentalmente ou materialmente uma **candidate version** antes de substituir a canônica;
- registrar qual evidência motivou a mudança;
- distinguir melhoria de conteúdo de mudança de trigger/permissão;
- reexecutar trigger tests, baseline e security review quando a mudança for material;
- detectar conflito/duplicação antes de merge;
- preservar rollback quando o ambiente de armazenamento suportar histórico;
- não promover automaticamente uma lição de uma única sessão para todos os usuários/contextos.

## Regra de portabilidade

O Arsenal guarda a **versão nativa de Agent Skills** da skill. A fonte externa serve como referência metodológica. Se houver divergência entre a implementação original e as capacidades atuais do ambiente, registrar explicitamente a adaptação em vez de reproduzir instruções incompatíveis.

## Formato nativo

Criar `<nome-em-kebab-case>/SKILL.md` com frontmatter YAML contendo `name` igual ao diretório e `description` curta que explique quando usar. Manter detalhes extensos em `references/` e ligar cada arquivo ao ponto de uso. Validar nomes únicos, YAML, links e conteúdo antes de concluir.

## Referências

Documento avaliado: **The 7 ChatGPT Work Skills I Use Every Day — Copy-and-Paste Setup Prompts**.

Ledger de extração, portable contract e proof-oriented demos adaptados de https://github.com/MengTo/Skills, especialmente article-prompts-to-skills, sem exigir seu initializer, gallery ou estrutura de agentes específica.

Origem local: [skill-builder.docx](../skill-builder.docx).
