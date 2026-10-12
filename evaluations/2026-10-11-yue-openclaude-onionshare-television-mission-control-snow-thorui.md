# Avaliação de sete projetos externos — 2026-10-11

## Escopo e método
Fontes: READMEs e metadados do GitHub nas branches padrão de 7 repositórios, consultados em 2026-10-11. Router: `ARSENAL INDEX.md`; stack: `arsenal-autopilot`; owners existentes verificados: `music-generation-engineering` e `multi-agent-orchestration`. Não houve execução de binários, instaladores, testes de runtime ou auditoria exaustiva de código. Stars e popularidade não constituem comprovação de qualidade ou segurança.

| Fonte | Evidência | Classe | Decisão e owner | Risco/portabilidade |
|---|---|---|---|---|
| [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | YuE2: letra/prompt → plano simbólico de melodia/acordes → áudio; edição e covers; skill/weights externos | A/D | **UPDATE_EXISTING** `music-generation-engineering`: edição de score antes do render e QA de transcrição | Pesos/compute/serviço, licenças e direitos musicais; nenhuma inferência nativa presumida |
| [Twigpine/openclaude](https://github.com/Twigpine/openclaude) | CLI coding agent com múltiplos provedores, tools/MCP e sessões | D | **KEEP_EXTERNAL_REFERENCE**; owners `coding-agent-engineering` e `multi-agent-orchestration` já cobrem contratos/limites | Tokens, execução de ferramentas e acesso a arquivos; não migrar APIs/credenciais por analogia |
| [onionshare/onionshare](https://github.com/onionshare/onionshare) | Compartilhamento, hospedagem e chat via Tor | D | **KEEP_EXTERNAL_REFERENCE**; software útil, sem skill genérica nova | Depende de app/Tor; anonimato não elimina riscos de metadados, destinatário ou endpoint |
| [alexpasmantier/television](https://github.com/alexpasmantier/television) | Fuzzy finder terminal com channels e ações configuráveis | B/D | **ABSORB_METHOD_ONLY** como padrão de busca/preview/ação contextual; sem owner novo | CLI e comandos customizados executam processos locais; proibir execução cega de snippets |
| [builderz-labs/mission-control](https://github.com/builderz-labs/mission-control) | Plano de controle self-hosted: task lifecycle, recibos, aprovações, custo, auditoria | A/D | **UPDATE_EXISTING** `multi-agent-orchestration`: controle separado de runtime e evidence receipts | Software alfa, chaves API, webhooks e superfície de rede; exige hardening e operadores |
| [mg-chao/snow-apps](https://github.com/mg-chao/snow-apps) | Apps desktop de captura e imagem; licenças por subprojeto | D | **KEEP_EXTERNAL_REFERENCE**; sem capacidade nova de agent workflow que justifique skill | Dependência nativa e permissões de tela; screenshot pode incluir dados sensíveis; GPL de alguns apps |
| [dingyong0214/ThorUI-uniapp](https://github.com/dingyong0214/ThorUI-uniapp) | Componentes mobile para uni-app/mini programs, última atualização em 2024 | B/D | **KEEP_EXTERNAL_REFERENCE** para `design-system-governance` quando target for uni-app; não importar catálogo | Tecnologia específica, evolução/compatibilidade a validar; licença MIT verificada nos metadados |

## Prova de valor incremental
- YuE2 acrescenta uma etapa operacional *score-first* editável, mais precisa do que blueprints textuais genéricos. Should-trigger: pedido de editar acordes/melodia antes de gerar uma nova versão; near miss: apenas escrever letra de música.
- Mission Control reforça a distinção entre status/log de agente e evidência de entrega aceita. Should-trigger: gestão de vários agentes/runtimes com revisão e custo; near miss: uma única conversa sem workers observáveis.
- Demais projetos não demonstraram workflow repetível novo para o ChatGPT que justifique skill dedicada.

## Gate de segurança
**CAUTION** para execução/instalação de todos os softwares externos. Observados pontos de atenção: credenciais e subprocessos (OpenClaude), Tor e distribuição de links (OnionShare), comandos de canais (Television), API keys, painéis de administração e alfa (Mission Control), captura de dados de tela (Snow), compatibilidade de componentes (ThorUI), compute, pesos e direitos de música (YuE). Nenhum script ou instalador foi executado. Não é certificação de segurança.

## Resultado
Atualizados somente `skills/music-generation-engineering/SKILL.md` e `skills/multi-agent-orchestration/SKILL.md`. Sem novas skills/stacks, pois owners já existentes atendem; `ARSENAL INDEX.md` não precisa mudar, já que nomes/descriptions não foram modificados. As demais fontes permanecem referências documentadas.
