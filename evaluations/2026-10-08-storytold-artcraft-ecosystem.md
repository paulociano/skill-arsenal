# Avaliação externa — Storytold / ArtCraft ecosystem

- Data: 2026-10-08
- Fonte: https://github.com/storytold
- Fontes inspecionadas: `storytold/artcraft`, `photocraft`, `designcraft`, `pdfcraft`, `deckcraft` (README e/ou metadados atuais); visão da organização com aplicações irmãs.
- Roteamento: `ARSENAL INDEX.md` → `stacks/arsenal-autopilot/STACK.md` → `stacks/evaluate-and-import-skill/STACK.md`; comparação com `skills/editable-visual-design/SKILL.md`, `skills/design-system-governance/SKILL.md`, `skills/skill-security-review/SKILL.md`.

## Resultado

**Classificação: D (ecossistema técnico), com metodologia B aproveitável. Decisão: KEEP_EXTERNAL_REFERENCE + ABSORB_METHOD_ONLY.**

Não se trata de um catálogo de skills de agentes. Trata-se de um ecossistema de aplicativos criativos open source, principalmente em Rust, com fluxos nativos para imagem, vídeo, desenho, PDF, slides e outros formatos. Sua utilidade ao Arsenal é como referência de interoperabilidade e produção editável, não como instalação automática.

## Capacidades e ownership

| Evidência / capacidade | Ganho para o Arsenal | Owner e decisão |
| --- | --- | --- |
| DeckCraft anuncia comandos estáveis compartilhados entre GUI, CLI, JSON e MCP, com ações undoable | Padrão valioso de **contrato de ações** unificado para apps controláveis por humanos e agentes | `coding-agent-engineering`, `agent-action-governance`, `ai-workflow-automation-engineering`: referência, sem skill nova |
| Documentos criativos com representação editável, render/export, undo e formatos de intercâmbio | Reforça validação separada de documento editável, export e render final | `editable-visual-design`, `design-system-governance`, `verify-before-claim`: absorção metodológica |
| PDFCraft anuncia gravar sem substituir bytes originais e workflows de páginas | Inspiração para operações não destrutivas em documentos; alegações específicas precisam teste | fluxos de PDF/documentos: referência externa, sem trocar ferramentas nativas |
| PhotoCraft/ArtCraft e família Craft em Rust | Potenciais engines especializadas para estudo futuro | `software-engineering-cycle`, `creative-web-engineering`: referência técnica |

## Condições para aproveitamento

1. Primeiro escolher **artefato e semântica**: PSD/SVG/PDF/PPTX, layers, fontes, propriedades editáveis e formatos de exportação necessários.
2. Separar **modelo-fonte** (editável), **comandos** (GUI/CLI/API/MCP) e **render** (evidência visual). Não confundir preview com fonte final.
3. Para apps controlados por agentes, exigir catálogo de comandos, schema de entrada, preconditions, undo/idempotência quando apropriado e confirmação humana para mudanças destrutivas.
4. Validar no runtime real importação, edição, round-trip, export, perda de estilos e fontes, acessibilidade e fidelidade do render.
5. Tratar números de paridade e funcionalidades apresentados nos READMEs como afirmações do projeto, não como validação independente.

## Segurança e portabilidade

- **Parecer: CAUTION para executar/instalar; APPROVE apenas para uso como referência metodológica.**
- Não foram executados binários, installers, scripts ou MCPs da fonte.
- Ferramentas Rust CLI/MCP citadas no repositório não passam a estar disponíveis no ChatGPT; requerem instalação, conexão, ambiente e análise independente.
- Examinar cadeia de dependências, supply chain, permissões de filesystem e credenciais antes de integrar qualquer engine.
- Verificar licenças por repositório e por diretório, especialmente identidade visual e assets: não presumir que código permissivo licencia marcas.
- Não inserir software experimental na stack obrigatória do Arsenal.

## Prova de valor e decisão

- **Should trigger:** usuário pede avaliação de uma ferramenta criativa open source com interface GUI/CLI/MCP e quer um fluxo editável, reversível e verificável.
- **Near miss:** usuário pede simplesmente criar ou editar uma imagem, PDF ou slide. Usar capacidades nativas disponíveis, sem exigir Storytold.
- **Critério de adoção futura:** integração real demonstrando round-trip editável e export fiel para um caso concreto, com custo, licença, segurança e testes documentados.
- **Sem CREATE_NEW:** índice já contém owners adequados; adotar aplicações Craft como skills separadas agora criaria entradas sem ferramentas operacionais.
- **Sem alteração no índice:** nenhuma nova rota foi criada e nenhuma description material mudou.

## Fontes
- https://github.com/storytold
- https://github.com/storytold/artcraft
- https://github.com/storytold/photocraft
- https://github.com/storytold/designcraft
- https://github.com/storytold/pdfcraft
- https://github.com/storytold/deckcraft

## Limitações
Triagem documental seletiva (README/metadados), sem executar software, auditar bases de código inteiras, testar MCP ou comprovar métricas de qualidade e paridade. Esta avaliação não certifica segurança operacional.

## Implementação posterior (2026-10-08)

- **UPDATE_EXISTING concluído:** `skills/editable-visual-design/SKILL.md` recebeu contrato de editabilidade, reversibilidade, pipeline fonte/render/export, interoperabilidade e cinco critérios de aceitação observáveis.
- Commit da atualização: [`baec6984`](https://github.com/paulociano/skill-arsenal/commit/baec6984f44b3731bada05229beaae745a4e626d).
- **Sem skill nova e sem alteração no índice:** owner e rota permanecem os mesmos.
- **Limite da validação:** revisão estática do conteúdo publicado; nenhum round-trip de PhotoCraft/DeckCraft/PDFCraft foi executado, pois as engines externas não foram integradas.
