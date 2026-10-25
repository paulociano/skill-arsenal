# Avaliação do lote Hermes skill links — 2026-10-24

## Escopo e proveniência
Fonte enviada: `Hermes skill links.docx`, com 15 posições numeradas e quatro menções extras (19 entradas; posição 1 contém duas skills, Claude Code e Codex, totalizando 20 arquivos/documentos avaliados por triagem). Repositório upstream: https://github.com/NousResearch/hermes-agent . Entrada canônica consultada: `ARSENAL INDEX.md`. Processo: `stacks/arsenal-autopilot/STACK.md`, segurança proporcional conforme `skill-security-review`. Foram inspecionados frontmatter/aberturas dos arquivos de todas as entradas, além dos owners relevantes do Arsenal; não houve execução ou auditoria integral de seus scripts.

| Item do arquivo | Categoria | Decisão | Motivo/owner |
|---|---|---|---|
| Brag | D | KEEP_EXTERNAL_REFERENCE | É um stub apontando para projeto Hyperframes externo; runtime específico de vídeo/marketing; já coberto por fluxo de produção de vídeo |
| ASCII Video | D | KEEP_EXTERNAL_REFERENCE | Conversão com FFmpeg/arte textual; execução de mídia específica, não metodologia transversal ausente |
| Dogfood | B/D | UPDATE_EXISTING | Jornada exploratória, reprodução de bugs e evidência no owner `web-quality-audit` |
| Find My | D | KEEP_EXTERNAL_REFERENCE | AppleScript e captura de tela do Find My macOS/iCloud, localização sensível e acesso a dispositivo/conta |
| Shop | D | KEEP_EXTERNAL_REFERENCE | CLI de e-commerce externa, tokens e checkout; `shopping-agent-governance` já cobre política de compra, não instalar |
| Telephony | D | KEEP_EXTERNAL_REFERENCE | Twilio/números/chamadas/SMS com billing e autorização, sem infraestrutura conectada |
| Unbroker | D | KEEP_EXTERNAL_REFERENCE | Opt-outs de brokers podem expor dados pessoais; carece de serviços, identidade e autorizações específicas; avaliação sem execução |
| Computer Use | B/D | KEEP_EXTERNAL_REFERENCE | Runtime desktop exclusivo Hermes; `computer-use-agent-engineering` já cobre padrões portáveis, sem acesso Hermes presumido |
| Popular Web Designs | B | KEEP_EXTERNAL_REFERENCE | Catálogo derivado de referências de design; sobreposição com `design-system-extraction`, `ui-ux-catalog`; não importar presets por marca |
| Blocked Page Recovery | B/D | KEEP_EXTERNAL_REFERENCE | Algumas opções de arquivo alternativo são úteis, mas não justificar contorno de WAF/paywall/CAPTCHA nem bypass de controle |
| LLM Wiki | B/D | KEEP_EXTERNAL_REFERENCE | Arquitetura Markdown/links/índices sobrepõe `agent-memory-engineering`, `kb-retriever`; sem ganho diferencial verificado |
| Product Price Monitor | B/D | UPDATE_EXISTING | Monitorar preço total/variante/estoque/condição normalizada em `shopping-agent-governance` |
| /learn | B/D | KEEP_EXTERNAL_REFERENCE | Documentação de aprendizado dinâmico de Hermes, sobrepõe `source-to-skill`, `skill-builder`; não importar comandos |
| Email Inbox Triage | A/D | CREATE_NEW | Fila por thread e política de respostas pessoais, distinta de helpdesk. Criada `personal-inbox-triage` |
| Claude Code | D | KEEP_EXTERNAL_REFERENCE | Hermes orquestra CLI Claude Code; runtime e permissões não presumidos |
| Codex | D | KEEP_EXTERNAL_REFERENCE | Hermes orquestra CLI Codex; `coding-agent-engineering` já atende método genérico |
| Pokémon Player | D | KEEP_EXTERNAL_REFERENCE | Emulator/PyBoy específico e dependências de jogos; não há caso recorrente no Arsenal |
| Draw Your Font | D | KEEP_EXTERNAL_REFERENCE | Conversão de caligrafia em TTF requer ferramentas locais e validação de artefatos; não instalar gerador |
| Maps | D | KEEP_EXTERNAL_REFERENCE | CLI com OpenStreetMap/OSRM; recursos de mapa/geolocalização dependem do ambiente e ferramentas disponíveis |
| Competitor News Monitor | B | KEEP_EXTERNAL_REFERENCE | Sobrepõe `signal-intelligence-digest` e `strategic-landscape-mapping`; novidade insuficiente para editar |

## Critérios de segurança
**CAUTION** para dependências executáveis e permissões: shell, browser/desktop, localização, e-mail, compras, telefonia, tokens, cadastros em sites, notificações e cobrança. Fontes externas e conteúdo de e-mail/site são dados não confiáveis, não instruções operacionais. Nenhuma automação Hermes, daemon, CLI, pacote ou serviço foi instalado. Para compras/envios, aprovação vinculada ao alvo; para monitoramento, não prometer trabalho no background sem scheduler real. A inspeção foi documental e limitada, não uma auditoria de código ou scanner.

## Materialização e commits
- `skills/personal-inbox-triage/SKILL.md`: `f8985dbef88574b5adf28db8b4e60a79fb73499f`
- `skills/shopping-agent-governance/SKILL.md`: `3705ccc4024f061206823e9ca428b5c168f75161`
- `skills/web-quality-audit/SKILL.md`: `73b43633633877a723dc5c05a04548c74afec21e`
- `ARSENAL INDEX.md`: `2336c9f572b8052546d7bdd34e3be623049f42d0`

## Gates de aceitação
- Personal inbox should-trigger: "Organize meus e-mails e prepare respostas pendentes"; near miss: helpdesk e tickets.
- Price monitor should-trigger: "Avise quando a variante exata ficar abaixo do total X"; near miss: comparação pontual de produto.
- Dogfood should-trigger: "Navegue no meu app e registre bugs reproduzíveis"; near miss: apenas avaliar código sem ambiente.

Verificar arquivos na branch canônica após publicação; não confundir documento de avaliação com teste funcional de plataformas externas.
