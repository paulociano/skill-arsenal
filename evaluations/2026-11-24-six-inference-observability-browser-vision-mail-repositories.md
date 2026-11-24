# Avaliação de seis repositórios externos — 2026-11-24

Stack: arsenal-autopilot. Índice canônico consultado; decisões por capability. Evidência: inspeção estática de root/README e documentos centrais indicados abaixo; sem testes de runtime, scanner, execução de código ou auditoria integral de supply chain. Nenhum runtime foi aprovado para instalação.

| Fonte | Classe | Decisão | Owner / motivo |
|---|---|---|---|
| [inference-optimisation-skill](https://github.com/sybil-solutions/inference-optimisation-skill) | A/D | UPDATE_EXISTING | local-llm-inference-engineering: ceilings, controles intercalados, ledger, gates de contexto e rebuild |
| [DataCat](https://github.com/replit/datacat) | D | UPDATE_EXISTING | software-observability-engineering: matriz de compatibilidade e fixtures known-answer, contabilidade de ingestão e freshness |
| [Obscura](https://github.com/h4ckf0r0day/obscura) | D | UPDATE_EXISTING | computer-use-agent-engineering: paridade semântica/visual e gate de troca de engine, sem stealth |
| [Tamserve](https://github.com/aryamandarda/tamserve) | D | UPDATE_EXISTING | ml-production-engineering: estado temporal limitado, batch dinâmico, freshness e lifecycle de objetos |
| [Zigzag](https://github.com/ZigaoWang/zigzag) | D | KEEP_EXTERNAL_REFERENCE | computer-use-agent-engineering já cobre fronteiras de sessão/abas privadas, pareamento e MCP; browser nativo macOS é ferramenta externa |
| [OpenWren](https://github.com/VinceGHER/openwren) | D | KEEP_EXTERNAL_REFERENCE | personal-inbox-triage cobre triagem; cliente IMAP/SMTP local não adiciona ferramenta ao ChatGPT, padrões de privacidade úteis como referência de arquitetura |

## Evidências e riscos
- Inference: README e skills/inference-optimisation/SKILL.md; MIT declarado. Scripts, controle de processos, alterações de energia, watchdog, GPU e endpoint externo exigem autorização e inspeção própria. Não importar comandos nem resultados publicados. CAUTION (static_only).
- DataCat: README e diretório bench/; Apache-2.0 declarado. Docker, DB, chaves, bootstrap admin, telemetria sensível e agentes de host exigem revisão operacional. Não presumir backend ou conexão. CAUTION (static_only).
- Obscura: README e skills/obscura/SKILL.md; Apache-2.0 declarado. Browser Rust/V8, CDP/MCP e renderização são externos; recursos anti-detection e flexibilização de acesso a rede interna não são adotados. Validar somente em escopo autorizado. CAUTION (static_only).
- Tamserve: README, docs/how-it-works.md; Apache-2.0 declarado para projeto, termos dos modelos separados. GPU, PyTorch e pesos baixados exigem verificação; dados de câmeras e finalidade de uso precisam de controles. CAUTION (static_only).
- Zigzag: README e docs/automation.md. Swift/WebKit, macOS 15.4+, MCP local opt-in autenticado; o próprio README declara exclusão de janelas privadas. Acesso a abas autenticadas continua sensível; token não deve ir para chat. Sem integração disponível. CAUTION (static_only). Valor incremental insuficiente diante do owner atual.
- OpenWren: README e PRIVACY.md; Apache-2.0 declarado. Rust/Tauri, SQLite/SQLCipher e keyring são arquitetura de aplicativo, não skill; OAuth Gmail com escopo amplo, sync e envio são sensíveis, instaladores Windows/macOS declarados sem assinatura de plataforma. Não contornar avisos, conceder credenciais ou instalar. CAUTION (static_only). Telemetria opt-in e atualização separável são referências, não provas de privacidade.

## Publicação e aceitação
Quatro owners existentes alterados nesta mesma mudança: skills/local-llm-inference-engineering/SKILL.md, skills/software-observability-engineering/SKILL.md, skills/computer-use-agent-engineering/SKILL.md e skills/ml-production-engineering/SKILL.md. Triggers atuais abrangem os casos, portanto índice e stacks não precisam de alteração; nenhuma skill nova. Cada adição contém caso should-trigger e near-miss. Testes comportamentais e benchmarks não executados; verificação de publicação por leitura pós-escrita. Nenhum script, binário, modelo ou credencial foi importado. 
