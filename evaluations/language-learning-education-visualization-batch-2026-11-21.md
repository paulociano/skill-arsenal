# Avaliação: nove fontes de aprendizagem, Anki e diagramas (2026-11-21)

## Escopo e evidência
Fontes: READMEs da branch padrão dos nove repositórios listados abaixo; leitura adicional de `education-agent-skills/skills/memory-learning-science/{retrieval-practice-generator,spaced-practice-scheduler}/SKILL.md`. Comparação com `ARSENAL INDEX.md`, `skills/teach/SKILL.md`, `skills/source-to-skill/SKILL.md`, `skills/architecture-visualization/SKILL.md`, `skills/interactive-system-diagram/SKILL.md`, `stacks/japanese-learning-cycle/STACK.md`.

**Validação:** static_only (documentação e instruções; sem instalar, rodar, testar endpoints, auditar árvore de dependências ou confirmar qualidade pedagógica empiricamente). Veredito de portabilidade da **metodologia adaptada**, não declaração de segurança ou funcionamento do aplicativo externo. Classes A=skill útil, B=metodologia boa, C=prompt com pouco ganho, D=sistema técnico dependente de runtime.

| Fonte | Classe | Decisão | Owner e motivo |
|---|---|---|---|
| [artcc/freelingo](https://github.com/artcc/freelingo) | B/D | UPDATE_EXISTING | `teach`: combinação missão, currículo por competência, avaliação, revisão, roleplay e progresso; app Next.js/FastAPI/Postgres/Redis, provedores de voz e infraestrutura não importados |
| [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | A/D | UPDATE_EXISTING | `source-to-skill`: capítulo/section coverage, fonte literal por item, auditoria de questões e exportação desacoplada; CLI/cache/API não importados |
| [ZackAkil/immersive-language-learning-with-live-api](https://github.com/ZackAkil/immersive-language-learning-with-live-api) | B/D | UPDATE_EXISTING | `teach`: roleplay com objetivo e modos guiado/imersivo; interação ao vivo e Gemini Live dependem de runtime ausente |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | D | KEEP_EXTERNAL_REFERENCE | Integração MCP e addon Anki dependem de Anki em funcionamento, conexão autorizada e ferramentas específicas. Sem presumir conexão ou escrever em decks |
| [PaoloJN/recap](https://github.com/PaoloJN/recap) | B/D | UPDATE_EXISTING | `source-to-skill`: referência navegável a momentos de transcrição e capítulos quando timestamps existem; extensão e APIs não importadas |
| [thiswillbeyourgithub/AnkiAIUtils](https://github.com/thiswillbeyourgithub/AnkiAIUtils) | B/D | UPDATE_EXISTING | `teach`: reensino após erros, mnemônicos pessoais e revisão dirigida; sem scripts que modificam cards automaticamente |
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | B/D | UPDATE_EXISTING | `teach`: personalização apoiada em evidência observável; não importar perfilamento do aluno, alteração automática de prompts ou dependências de Honcho/Supabase |
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | A/B | UPDATE_EXISTING | `teach`: diferenciação de retrieval livre/com pista/reconhecimento e revisão espaçada flexível; coleção de 165 skills não importada em massa |
| [LingyiChen-AI/DeepDiagram](https://github.com/LingyiChen-AI/DeepDiagram) | B/D | KEEP_EXTERNAL_REFERENCE | Routing entre diagramas/infográficos, seleção da gramática visual e verificação estrutural já cobertos por `architecture-visualization` e `interactive-system-diagram`; multiagentes, LangGraph, React e renderers específicos não necessários para essas skills |

## Ganho incremental adotado
- `skills/teach/SKILL.md`: ciclo de diagnóstico por tipo de erro, remediação, transição guided/immersive, transferência e registro autorizado; distingue domínio de métricas de engajamento.
- `skills/source-to-skill/SKILL.md`: cobertura por seção, verificação de citação, QA de itens, saídas portáteis e restrições de privacidade.
- Não há skill nova, stack nova, instalação ou atualização do INDEX porque o roteamento canônico permanece.
- O caso do Anki é uma referência a um conector externo, não uma skill operacional do Arsenal. A disponibilidade de um servidor MCP em um README não significa que esteja conectado neste ChatGPT.

## Segurança, licenças e limites
**CAUTION / static_only** para execução dos sistemas externos: incluem potenciais acessos a chaves de LLM, microfone, transcrições, arquivos, decks Anki, perfilamento e dados de aprendizagem; há também superfícies de Docker, npm/Python, extensões browser, automação e SaaS. Não foram executados scripts nem lidas todas as dependências, logo nenhuma aplicação foi aprovada para instalação ou produção. Evitar transmissão de conteúdo sensível a provedores externos, log de dados pessoais desnecessários, sincronização sem aprovação e autoedição de prompts que ultrapasse governança humana. Verificar licenças separadamente antes de reutilizar código ou distribuir conteúdo; as alterações presentes são metodologia própria, não cópias de implementação.

## Critérios de aceitação de comportamento (não executados)
- **teach should-trigger:** pedido de trilha contínua de idioma com erro recorrente e roleplay -> incluir objetivo, breve diagnóstico, prática, feedback, transferência e revisão.
- **teach near-miss:** tradução isolada -> responder sem abrir trilha.
- **source-to-skill should-trigger:** guia, quiz e cards derivados de livro -> cada item suporta locator e QA de cobertura.
- **source-to-skill near-miss:** resumo de um único parágrafo -> não sobrecarregar com pipeline.
- **Anki:** sem conector autorizado, não declarar sincronização nem edição de cards.
- **DeepDiagram:** não criar skill duplicada; usar owners existentes.

## Publicação
Owners alterados nesta avaliação:
- `skills/teach/SKILL.md` (commit `410412f1a0689b379822a347b4ff36f04972f375`)
- `skills/source-to-skill/SKILL.md` (commit `d70b50d2972b7a8d30c215171e37d94dcde83bd3`)

Registrar o commit deste relatório após sua publicação.