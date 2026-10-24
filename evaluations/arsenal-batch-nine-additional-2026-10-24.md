# Avaliação: segundo lote de nove repositórios (2026-10-24)

Fonte: índice oficial e stack arsenal-autopilot, READMEs e metadados dos repositórios públicos. Avaliação documental sem executar código nem instalar aplicativos.

| Projeto | Classe | Decisão / Owner | Razão |
|---|---|---|---|
| https://github.com/OthmanAdi/planning-with-files | A/D | UPDATE_EXISTING skills/project-planning/SKILL.md | Recuperação entre sessões por três artefatos versionáveis, sem hooks obrigatórios. |
| https://github.com/Muesli-HQ/muesli | D | KEEP_EXTERNAL_REFERENCE | Transcrição e ditado local macOS com interface/plugin próprios; já existe meeting-to-actions e voz/transcript nativo; o app requer macOS e permissões. |
| https://github.com/vorssaint/vorssaint-utils | D | KEEP_EXTERNAL_REFERENCE | Utilitários macOS menu bar, fora do âmbito de metodologia de agentes. Permissões de sistema e licença GPL merecem revisão antes de adoção. |
| https://github.com/pgrundev/pgterm | D | KEEP_EXTERNAL_REFERENCE | Diagnóstico PostgreSQL e SQL TUI com ferramenta externa; skills de observabilidade e banco já cobrem metodologia geral. Sem conexão/consulta a DB. |
| https://github.com/nyblnet/bento | D | KEEP_EXTERNAL_REFERENCE | Projeto especializado; requer avaliação de execução/caso de uso antes de adicionar metodologia genérica. |
| https://github.com/ChartGPU/ChartGPU | B/D | UPDATE_EXISTING skills/dashboard-design/SKILL.md | WebGPU para grandes séries/streaming com gate explícito de compatibilidade e fallback. |
| https://github.com/shader-effects-inc/shaders | B/D | UPDATE_EXISTING skills/shader-graphics-engineering/SKILL.md | Component tree GPU, SSR/lifecycle, performance, fallback e QA. |
| https://github.com/BIT-DataLab/Edit-Banana | A/D | UPDATE_EXISTING skills/interactive-system-diagram/SKILL.md | Reconstrução semântica e QA de topologia para figura raster → diagrama editável. |
| https://github.com/jub0t/concat | B/D | UPDATE_EXISTING skills/video-editing-pipeline/SKILL.md | Plano EDL, ferramentas MCP/RPC e verificação do estado/export real. |

## Segurança e portabilidade
Não executar scripts de instalação, ferramentas de agente/hook, editores, mecanismos GPU nem upload a serviços de terceiros só para avaliar. Voz, vídeo, documentação privada, gravações e controles de máquina exigem consentimento, autorização e proteção dos dados. AGPL/GPL/arquivos de modelos devem ter licença e dependências revisadas no uso comercial. Benchmarks dos autores não são prova de desempenho local. Nenhum runtime externo foi afirmado como instalado.

Should-trigger: projeto com sessões longas e recuperação, dashboard denso com WebGPU, shaders funcionais, diagramas convertidos editáveis ou edição de vídeo com RPC. Near-miss: conversa curta, gráfico pequeno, diagrama textual com topologia já explícita, filme sem mídia executável. Evidência futura: replay do plano, teste em browser real, comparação visual/topológica e arquivo renderizado verificado.

Sem criação de skill nem mudança de índice: owners existentes foram atualizados; demais permanecem referências externas.
