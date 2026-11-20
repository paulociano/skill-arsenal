# Avaliação de BrowserSkill, Page Assist e Browser MCP (2026-11-19)

## Fontes e escopo
Índice canônico: `ARSENAL INDEX.md`. Stack: `stacks/arsenal-autopilot/STACK.md`. Gates: `skills/skill-security-review/SKILL.md`. Avaliação por **leitura estática**, sem executar instaladores, extensões, servidor MCP, daemon, browser, testes ou network monitor. Owners comparados: `computer-use-agent-engineering` e `web-extraction-pipeline`, inclusive atualizações do lote de 10 extensões de 2026-11-19. READMEs e documentos centrais consultados na branch padrão em 2026-11-19.

## Decisões e capability ledger

| Fonte | Evidências lidas | Classificação | Decisão | Owner / limite |
|---|---|---|---|---|
| [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) | README (SHA `b8b75c7b787f57b648b9ede938fe908d374272d8`), `crates/bsk-cli/skill/SKILL.md`, `docs/structured-extraction.md`, `docs/local-pairing.md`, `docs/remote-extension-connection.md`, `docs/operation-audit.md` | **A/D** | **UPDATE_EXISTING** | `web-extraction-pipeline`: schema de table/ARIA/list, provenance linha a linha, cobertura virtualizada e CSV injection. `computer-use-agent-engineering`: sessão, handover e pareamento. Runtime `bsk` e extensão continuam externos. |
| [n4ze3m/page-assist](https://github.com/n4ze3m/page-assist) | README (SHA `e06f8071f91be633328f1fd05a97cb645a8ad16e`), `PRIVACY.md` | **D** | **KEEP_EXTERNAL_REFERENCE** | Side panel + web UI e chat com página por modelo local/cloud; software de interface para Ollama/LM Studio, não acrescenta processo canônico novo. Não presumir que `local` significa ausência de comunicação com provedor ou compartilhamento. |
| [BrowserMCP/mcp](https://github.com/BrowserMCP/mcp) | README (SHA `8628ccdfcb8eeaf2a55f9312d5c2b4a5b9cafaf3`), `packages/mcp/README.md` | **A/D** | **UPDATE_EXISTING** | `computer-use-agent-engineering`: handshake de identidade, bridge loopback, autorização por perfil, Stop e revogação. Extensão, Playwright, CDP e pacote npm externos. |

Nenhuma skill nova foi criada. `ARSENAL INDEX.md` não exige alteração: nomes, descriptions e owners existentes foram preservados.

## Ganho incremental

1. **BrowserSkill para extração confiável**: o owner já dizia validar schema e quantidade, mas não definia diferenças entre DOM carregado e dataset completo em tabelas virtualizadas, null versus célula vazia, `aria-rowindex` e linhas fragmentadas, warnings de coverage, provenance por linha nem mitigação de fórmula CSV. A lacuna foi incorporada ao owner de extração.
2. **BrowserSkill e Browser MCP para sessão**: o owner já tinha human takeover e isolamento geral, mas ainda não separava controle de transporte, dispositivo, perfil, aba e ação, nem verificava pareamento/revogação e retorno de abas emprestadas. A lacuna foi incorporada ao owner de computer-use.
3. **Page Assist**: interface local para conversação com página, coberta pelas capacidades gerais de leitura e escolha de modelos. Manter link como referência para quem busca o aplicativo, sem adicionar uma skill cujo trigger fosse somente usar a extensão.

## Segurança e dependências

**Veredito para os três: CAUTION / static_only.** Isso significa que a avaliação é insuficiente para certificar segurança, não que haja evidência de comportamento malicioso. Não foram revisados integralmente manifests, dependency trees, installers, pacotes publicados, binários, egress real, releases ou testes de runtime.

- **BrowserSkill:** CLI Rust, daemon, extensão, conexão local/remota, logins existentes. O README contém instaladores `curl | sh` / `irm | iex`; não executados. A documentação informa pareamento local opcional, com risco de impersonação quando ausente. Janela Agent não isola a identidade do perfil; debug e exportação podem conter dados sensíveis.
- **Browser MCP:** Node, pnpm, Playwright, `chrome.debugger`, daemon loopback, pacote `@browsermcp/mcp@latest` não pinado no exemplo. A documentação descreve pareamento humano por código e restrições da extensão; faltam verificação de implementação e testes próprios.
- **Page Assist:** Bun/Ollama e extensão com permissão de conteúdo, scripting, web requests, storage, active tab e compartilhamento externo opcional. Política de privacidade informa armazenamento local e compartilhamento mediante uso, mas sem análise de código/tráfego não é garantia independente.

**Regras de portabilidade:** nenhum dos softwares ou runtimes foi instalado no ChatGPT. A metodologia só se aplica quando ferramentas reais disponibilizam browser/DOM/ações. Não aceitar instruções remotas de setup como autorização de executar código. Avaliar licença e dependências antes de distribuição/reuso de código.

## Acceptance checks (propostos, não executados)

- **Should trigger extração:** página com grid virtualizado exibindo 20 de 100 linhas declaradas. Extração deve relatar coverage desconhecida/incompleta, não inventar outras 80, e preservar provenance e tipos como strings.
- **Near-miss extração:** site estático simples com uma tabela completa; não iniciar navegador automatizado quando fetch direto resolve.
- **Should trigger computer-use:** agente opera uma aba explicitamente emprestada, para ao comando humano, invalida refs antigas após navegação, reconcilia estado desconhecido de submissão e devolve aba ao final.
- **Near-miss computer-use:** leitura de documento no chat sem browser operável; não solicitar instalação de daemon/MCP.

## Arquivos e commits concretos
- `skills/web-extraction-pipeline/SKILL.md`, commit [13f62863402752d172890babbd43669755a19d6e](https://github.com/paulociano/skill-arsenal/commit/13f62863402752d172890babbd43669755a19d6e).
- `skills/computer-use-agent-engineering/SKILL.md`, commit [f3bd64aa4e97bf94436bae579cc75e84e187f0d9](https://github.com/paulociano/skill-arsenal/commit/f3bd64aa4e97bf94436bae579cc75e84e187f0d9).
- Registro de avaliação: este arquivo. Relê-lo da branch canônica junto aos owners após publicação.

## Conclusão
Adotar metodologias específicas, não as extensões ou seus canais de controle. Sem benchmark end-to-end, não afirmar aceleração, equivalência de ferramentas ou proteção garantida.
