# Avaliação — StykAnimate-App e block/buzz

Data: 2026-10-20

## Fontes e escopo
- https://github.com/filippocalippo/StykAnimate-App (branch main, README e metadados)
- https://github.com/block/buzz (branch main, README e metadados)
- Índice canônico: `ARSENAL INDEX.md`
- Histórico relevante: `evaluations/2026-10-03-six-repos-openshorts-latticedb-buzz-walgit-ambient-learn.md`

Aplicada a triagem da stack `arsenal-autopilot`. Nenhum código, installer ou binário externo foi executado. Avaliação documental, não auditoria integral de código.

## StykAnimate-App
**Classe:** D (aplicação técnica externa).

**Capacidades:** editor de animação 2D de stick figures; rig articulado/IK, timeline simples e avançada, onion skin, movimentos de câmera, partículas, exportação MP4/WebM/GIF/APNG/SVG e compatibilidade com projetos Pivot/Stick Nodes. Web e Electron, com componentes JavaScript/WebGPU e backend Python. Licença GPL-3.0.

**Sobreposição:** `explainer-video-production`, `procedural-film`, `sprite-sheet-pipeline`, `game-animation-engineering`, `motion-asset-engineering` e `ai-reels-production`.

**Decisão:** KEEP_EXTERNAL_REFERENCE, sem nova skill. O produto oferece um editor utilizável, não um contrato metodológico novo que altere verificavelmente um owner. Pode ser ferramenta opcional em fluxos de animação; não assumir acesso programático, execução automática nem 3D nativo para personagens de estilo cinematográfico. Não incorporar código GPL ao Arsenal sem revisão específica de compatibilidade.

**Segurança/portabilidade:** CAUTION para instalação/execução não auditada; app local com serviços auxiliares, atualizações e exportação multimídia. O README menciona diagnósticos opcionais com consentimento; essa declaração não foi verificada por inspeção dinâmica. Nenhuma credencial ou instalação necessária para manter referência.

## block/buzz
**Classe:** A/D (metodologia de colaboração humano-agente associada a uma infraestrutura específica).

**Capacidades:** workspace autohospedado baseado em relay Nostr, identidade separada por agente, eventos assinados e auditáveis, canais, discussão de patches e CI, automações YAML, busca e integração Git. Stack Rust, Tauri/React, Postgres, Redis, object storage e ferramentas CLI/ACP/MCP. Licença Apache-2.0.

**Verificação de novidade:** o Arsenal já avaliou esta fonte em 2026-10-03. Os princípios incrementais foram materializados em `ai-workspace-operating-cycle` e `multi-agent-orchestration`: identidade de agente, membership explícita, trilha de auditoria e vínculo patch/CI/revisão/aprovação.

**Decisão:** KEEP_EXTERNAL_REFERENCE; nenhuma atualização duplicativa justificada nesta revisão. A documentação atual distingue funcionalidades operacionais de recursos em desenvolvimento, sobretudo gates de aprovação e apps móveis. Não pressupor runtime Buzz ou permissões de agentes no ChatGPT.

**Segurança/portabilidade:** CAUTION; chaves privadas, shell/file edits, triggers, armazenamento persistente, hospedagem e deployment demandam escopo de permissões, aprovação humana e revisão independente. Nenhum ambiente foi inicializado.

## Resultado
- Novas skills: 0.
- Owners existentes atualizados: 0; nenhum ganho incremental metodológico comprovado além do já documentado.
- Referências externas: 2 (Buzz já avaliado).
- Registro de avaliação: este arquivo.
- Limite: leitura de README e metadados, sem testes, reprodução de benchmarks ou auditoria completa de dependências.
