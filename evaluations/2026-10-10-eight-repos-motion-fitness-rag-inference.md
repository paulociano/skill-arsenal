# Avaliação: oito repositórios externos (2026-10-10)

## Escopo e fontes
Triagem pela stack `arsenal-autopilot`, após leitura do `ARSENAL INDEX.md` canônico, README de cada fonte (branch principal na data) e comparação por capacidade. Nenhum instalador, binário ou script externo foi executado. Segurança avaliada preliminarmente por descrição/README, não por auditoria aprofundada do código.

## Capability ledger e decisões

| Fonte | Classe | Capacidade verificada | Owner existente | Decisão |
|---|---|---|---|---|
| [howseen-ai/claude-motion-design](https://github.com/howseen-ai/claude-motion-design) | A/D | Engine HTML `seek(t)` determinístico, Playwright/ffmpeg, beat map, motion blur por subframes, áudio por picos medidos, inspeção de flashes, aprovação de stills | `explainer-video-production`, `video-editing-pipeline`, `ui-motion-design` | ABSORB_METHOD_ONLY; referência para render reproduzível; dependências locais não são ferramentas nativas |
| [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | D | App fitness self-hosted com planejamento semanal, logging, histórico de cargas, RPE/RIR, progressão, mapa muscular, import/export, passkeys e PWA | `pwa-engineering`, `improve-existing-web-app`; projeto consumidor fitness fora do Arsenal | KEEP_EXTERNAL_REFERENCE; útil como benchmark, não copiar código AGPL inadvertidamente |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | A/D | Bases de conhecimento com RAG híbrido, citations, agentes, wiki, memória, permissões de workspace e integrações | `retrieval-quality-engineering`, `agent-memory-engineering`, `system-design-engineering` | ABSORB_METHOD_ONLY; não confundir infraestrutura externa com integração conectada |
| [JustVugg/colibri](https://github.com/JustVugg/colibri) | D | Engine C de inferência MoE com experts transmitidos do disco, cache dependente do hardware | `system-design-engineering`, `software-engineering-cycle` | KEEP_EXTERNAL_REFERENCE; exige engine e modelos locais |
| [BlueHeisenberg/SCSKiller](https://github.com/BlueHeisenberg/SCSKiller) | D | Precompilação de shaders e pipelines para cache de driver de GPU em games Windows | `game-development-cycle` / owners de performance | KEEP_EXTERNAL_REFERENCE; uso técnico estreito, requer Windows/jogos/GPU e validação |
| [GTKottman/mortiflix-oss](https://github.com/GTKottman/mortiflix-oss) | A/D | Produção de motion por etapas, gates humanos, anotações em frame/tempo, handoff e checks auditáveis | `ai-reels-production`, `explainer-video-production`, `video-editing-pipeline` | ABSORB_METHOD_ONLY; não portar harness Claude Code como se nativo |
| [Mapika/decider](https://github.com/Mapika/decider) | A/D | Escolhas tipadas (Choice/Score/Noul) com distribuições de probabilidade, avaliação de calibração e modelos especializados | `decision-analysis`, `experiment-design`, `llm-observability-evaluation` | ABSORB_METHOD_ONLY; representação tipada e calibração são transferíveis, pesos/servidor não |
| [CAPCOM-TD-OSS/REDox](https://github.com/CAPCOM-TD-OSS/REDox) | D | DOM/token IR comum, conversores multifomato e serialização rápida para .NET | `software-engineering-cycle`, `system-design-engineering` | KEEP_EXTERNAL_REFERENCE; pacote .NET, sem skill portátil independente |

## Valor incremental
- **Motion design:** documentar `seek(t)`, beat map medido, stills antes de render completo, QA de frames e cortes dentro de owners existentes quando aparecer tarefa de vídeo renderizado por código.
- **Governança audiovisual:** aplicar revisões por gates, feedback vinculado a frame/timestamp e registro de decisões em fluxos longos. Não pressupor persistência automática.
- **RAG:** recomendar arquitetura com rastreabilidade, versionamento de chunks, busca híbrida, RBAC e avaliação de recuperação apenas quando o produto justificar.
- **Decisões tipadas:** separar alternativas admissíveis de probabilidades produzidas por modelo; calibrar com exemplos rotulados; não atribuir probabilidades numéricas a texto livre sem medição.
- **Fitness:** usar apenas referência de UX e produto, sem alterar aplicação consumidora ou copiar componentes licenciados sem revisão.

## Portabilidade e segurança
- Executáveis e runtimes necessários (Playwright, ffmpeg, Node, Docker, C, CUDA, .NET, dados locais e chaves de API) não se tornam automaticamente capacidades do ChatGPT.
- `openGym` indica licença AGPL-3.0; avaliar obrigações antes de reutilizar código. `mortiflix-oss` requer Claude Code ou API Anthropic para execução real conforme README.
- Inferência local (`colibri`), modelos de decisão (`decider`) e precompilação de shaders (`SCSKiller`) exigem ambiente e critérios operacionais específicos.
- `WeKnora` requer atenção a credenciais, ingestão de documentos, permissões, sandbox, retenção, sincronização e fronteiras de confiança.
- `claude-motion-design` menciona download de assets e modo remake: verificar licenças, direitos de imagem, marcas e áudio de origem.
- Não instalar ou executar código externo apenas para avaliar. Não prometer segurança ou benchmarks sem testes independentes.

## Conclusão
Não criar oito skills redundantes. Os owners canônicos já abrangem as metodologias centrais. Guardar as fontes como referências técnicas e atualizar skills existentes somente quando um caso de uso demonstrar lacuna concreta. Nenhuma alteração foi feita em projetos consumidores. Avaliação baseada em README e metadados, não em execução ou auditoria integral.
