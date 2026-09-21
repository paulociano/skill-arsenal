# Avaliação em lote — segurança, design editável, design systems e runtimes especializados

Data: 2026-09-20

## Fontes

anthropics/uplifting-biomolecular-modeling
dmtrKovalenko/bashka
coldteadotai/abide
shadcn-ui/lint
anmolkapil/plexo
pizza-bot-app/pizza-bot
opencoredev/bg0
yejy53/Editable-Design
nilbuild/page-mascot
bestagentkits/design-studio-ai
kazdenc/regen-icons
haplollc/Minted
sindresorhus/awesome

Fluxo aplicado: evaluate-and-import-skill + skill-security-review.

Nenhum installer, package, binary, model, hook, browser runtime ou código externo foi executado.

## Resumo

Nova skill: editable-visual-design.

Melhorias: skill-security-review, project-skill-architecture, design-system-governance, shadcn-ui-engineering, sprite-sheet-pipeline e experiment-design.

Sem nova importação para Plexo, Pizza Bot, BG0, Design Studio AI, Minted e Awesome por sobreposição ou por serem produtos/bibliotecas.

## Avaliações

### uplifting-biomolecular-modeling
Classificação B/D. Kits de otimização com stock pinado e modos off, exact, fast e big. Valor alto para experimentos reproduzíveis e no-silent-fallback. Segurança CAUTION por startup hooks, upstream code, kernels e weights. Metodologia incorporada em experiment-design.

### bashka
Classificação B/D. Scanner de installers shell e cadeia de scripts. Valor alto para revisar curl-pipe-shell, exfiltration, credential theft, reverse shell, TLS e hooks. Segurança CAUTION porque o próprio produto instala/self-updates. Metodologia incorporada em skill-security-review.

### abide
Classificação A metodológica / D operacional. Compila instruções em rubric rastreável e separa lint, checks mecânicos, semânticos, repository-context e process. Segurança CAUTION por hooks, envio de diffs e API keys. Metodologia incorporada em project-skill-architecture sem Jev/hooks.

### shadcn-ui/lint
Classificação A/B. Linter agent-first com component contracts e diagnostics corretivos. Segurança APPROVE metodologicamente. Metodologia incorporada em design-system-governance e shadcn-ui-engineering.

### plexo
Classificação D. Download manager multi-interface. Sem workflow novo útil para o Arsenal. Segurança CAUTION por rede/downloads. Não importado.

### pizza-bot
Classificação B/D. Inbox de tarefas longas, checkpointing, approvals e skills tool-scoped. Bom valor, mas sobrepõe graph-engineering, loop-engineering e handoff já fortalecidos por Herdr. Segurança CAUTION por plugins/processos/providers. Sem mudança adicional.

### bg0
Classificação B/D. Background removal local com WebGPU e WASM fallback, modelo pinado e zero upload. Boa arquitetura local-first, mas não justifica skill isolada. Segurança APPROVE arquitetural, com weights/runtime de terceiros. Não importado.

### Editable-Design
Classificação A. Skill real para fixed-canvas design com fonte editável, asset architecture, evidence boundaries, reference modes e revisão do render. Cobre espaço distinto de web-design-engineer. Segurança CAUTION por editor/scripts/assets/generation na implementação original. Adaptada como editable-visual-design sem dependências específicas.

### page-mascot
Classificação B/D. Skill estreita mas útil para sheets directions/reactions, alignment e transparência. Segurança CAUTION por OpenAI API e scripts opcionais. Metodologia incorporada em sprite-sheet-pipeline.

### design-studio-ai
Classificação B/D. Workspace estruturado para múltiplos formatos, revisões, MCP/CLI e providers BYOK. Alta sobreposição com skills existentes e editable-visual-design. Segurança CAUTION alto por keys, publicação e operações pagas. Usado apenas como referência complementar.

### regen-icons
Classificação B/D. Source canônico por ícone, compiler para derivados, spec e visual matrix review. Segurança APPROVE metodologicamente. Metodologia incorporada em design-system-governance.

### Minted
Classificação D. Biblioteca Swift/SceneKit para medalhões 3D derivados de SVG. Técnica específica, já próxima de capacidades Swift/3D. Segurança APPROVE na leitura limitada. Não importado.

### awesome
Classificação B/C. Índice curado de recursos. Útil como discovery, não como skill operacional nem fonte autoritativa. Links externos continuam exigindo avaliação própria. Não importado.

## Mudanças aplicadas

- nova editable-visual-design;
- índice atualizado;
- installer-chain security review;
- enforceability buckets para regras de projeto;
- contratos executáveis e governança de ícones;
- design-system lint para shadcn;
- alpha e alignment para sprite sheets;
- tiers reproduzíveis para experimentos de performance.

## Limites

Revisão manual, sem scanner estático automatizado. Claims de benchmark dos autores não foram reproduzidos. Nenhum código externo foi executado.
