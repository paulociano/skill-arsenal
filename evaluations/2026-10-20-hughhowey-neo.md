# Avaliação externa: hughhowey/neo (2026-10-20)

## Fonte e escopo

- [NEO](https://github.com/hughhowey/neo), branch principal `main`, commit observado [2a4dee282f2e7b4a76294c998071280e0d74aa7d](https://github.com/hughhowey/neo/commit/2a4dee282f2e7b4a76294c998071280e0d74aa7d).
- Arquivos consultados: `README.md`, `TUTORIAL.md` (estrutura), `CONTRIBUTING.md`, `AGENTS.md`, `package.json`, `LICENSE` e listagem de diretório.
- Fonte canônica de destino: [paulociano/skill-arsenal](https://github.com/paulociano/skill-arsenal), branch `master`; leitura inicial de `ARSENAL INDEX.md` e `AGENTS.md`. Aplicado `stacks/evaluate-and-import-skill/STACK.md` com revisão de `skill-security-review`.
- O NEO **não é uma skill de IA**: é um editor de livros e roteiros local-first, construído com Electron e JavaScript, licenciado sob MIT. O valor extraído é de **metodologia de produto/editorial**, não de importação de software.

## O que faz de verdade

- Escrita de manuscritos com biblioteca de livros e representação familiar de páginas e capítulos.
- Planejamento e reorganização por index cards conectados ao texto, inclusive cartões soltos ainda sem destino.
- Notas de pendência (placeholders) para não interromper o fluxo de redação; passagens retiradas passam a `Darlings` para recuperação.
- Interfaces com modo simples e revelação progressiva; ortografia por demanda; ações de foco; metas de palavras opcionais.
- Persistência em HTML/JSON legíveis, snapshots e backups; arquitetura de escrita durável, estratégia de sincronização sem *last write wins* silencioso; import/export em formatos editoriais.
- Aplicativo contém recursos opcionais de API externa para imagens de capa e rotinas de atualização, mas não há necessidade de reproduzir esses recursos no Arsenal.

## Classificação e capacidade incremental

**Classificação geral: B/D.**
- **B — boa metodologia:** rotina criativa sem interrupção, placeholders estruturados, notas ligadas ao manuscrito, descarte recuperável, revisão reversível e auditoria de UX de foco profundo.
- **D — aplicação técnica:** Electron, arquivos locais, sincronização/cloud, rotinas de backup, impressão, APIs e integrações não constituem uma Agent Skill portável por si sós.
- **C — não adotável como regra:** estéticas de folha/capa, atalhos específicos, modo somente hover, limiares de produto e preferências particulares do autor. São escolhas contextuais, não prescrições globais.

## Capability ledger e ownership

| Capacidade | Situação anterior | Decisão | Owner |
| --- | --- | --- | --- |
| Revisão não destrutiva de manuscritos longos, placeholders e organização por cenas/capítulos | `writing-quality` já cobre outline, draft e revisão mas sem contrato específico para manter descartes recuperáveis | **UPDATE_EXISTING** | `skills/writing-quality/SKILL.md` |
| UX de concentração, disclosure reversível, ausência de interrupções e recuperação de erro | `design-principles-audit` já cobre heurísticas de cognição/erro, mas não protocoliza o contexto de trabalho profundo | **UPDATE_EXISTING** | `skills/design-principles-audit/SKILL.md` |
| Persistência local, sync concorrente, backups, Electron e APIs | Requer runtime e uma tarefa concreta de engenharia; não é ganho universal de escrita | **KEEP_EXTERNAL_REFERENCE** | sem owner novo |
| Instalar o NEO como ferramenta mandatória para autores | Software opcional, não infraestrutura do Arsenal | **REJECT** | não aplicável |
| UI invisível até hover como prescrição | Pode comprometer descoberta e acessibilidade | **REJECT** | não aplicável |

**Casos should-trigger:** projeto de romance/roteiro com capítulos reordenáveis e revisões destrutivas; auditoria UX de editor de texto que interrompe redação. **Near-miss:** resposta curta por e-mail; dashboard de operações de segurança que exige alertas constantes; pedido de instalar o aplicativo NEO (tratar como software, não skill).

## Portabilidade, segurança e limites

**Veredito:** APPROVE para adaptação da metodologia em arquivos Markdown internos; CAUTION para executar/instalar o software externo sem revisão operacional do ambiente.

- Nenhum instalador `.dmg`, `.exe`, `.AppImage`, `npm install`, script ou workflow externo foi executado.
- `package.json` declara Electron, electron-builder, electron-updater, bibliotecas de dicionário e pacotes auxiliares. Dependências devem ser avaliadas e fixadas se o usuário futuramente pedir implantação/uso real.
- O aplicativo menciona armazenamento de chave de API para geração opcional de capas e chamadas remotas. Manuscritos podem ser sensíveis: sem consentimento e contrato de dados não autorizar envio externo.
- `AGENTS.md` declara bridge `preload.js` entre renderer e filesystem e persistência via escrita temporária + fsync/rename. Isso descreve *design intent* e não é prova de que implementação, testes de segurança, backup ou sync foram auditados e aprovados.
- O código e comportamento da aplicação **não** foram testados no runtime. Não declarar app seguro, armazenamento infalível, execução de backups, sincronização perfeita nem melhoria empírica de UX.
- Em ChatGPT, persistência, arquivos e ações externas exigem ferramentas concretas e verificação; não alegar salvamento automático de textos apenas por descrever a metodologia.
- Não reproduzir materiais de obra/arte/fonts do projeto; a adaptação é de princípios e workflow, não importação de código/assets.

## Implementação e publicação verificável

1. **UPDATE_EXISTING** `skills/writing-quality/SKILL.md`: seção "Fluxo de manuscritos longos e revisão reversível", com mapa narrativo, placeholders, salvamento de descartes, etapas independentes, QA de continuidade e export verificável. Commit: [571b6e788bb79742b865ef72a70f1a4553a3b5f6](https://github.com/paulociano/skill-arsenal/commit/571b6e788bb79742b865ef72a70f1a4553a3b5f6).
2. **UPDATE_EXISTING** `skills/design-principles-audit/SKILL.md`: seção "Auditoria de fluxo profundo e interfaces sem interrupções", com custo da interrupção, progressive disclosure acessível, feedback sobre falhas de salvamento, recuperação, portabilidade e testes. Commit: [6481b2b786afa8233037470d97566b41a008f4bd](https://github.com/paulociano/skill-arsenal/commit/6481b2b786afa8233037470d97566b41a008f4bd).

Nenhum owner novo, frontmatter ou description alterados. Portanto `ARSENAL INDEX.md` não precisa ser modificado. Não foi criada uma stack artificial de redação nem um clone do NEO.

## Protocolo de validação futura

A leitura remota pós-escrita deve confirmar os marcadores de seção, unicidade, frontmatter e a presença desta avaliação.

Para medir ganho real: aplicar ao menos a uma tarefa autorizada de escrita longa com mudança/reordenação de cenas e a uma auditoria de editor em runtime; observar se houve perda de texto, recuperação correta de cortes, acessibilidade dos controles e export completo. A existência de metodologia documentada **não** prova melhora de produto sem teste.
