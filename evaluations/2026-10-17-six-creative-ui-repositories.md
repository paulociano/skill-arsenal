# Avaliação de seis repositórios para UI, design systems e vídeo de lançamento — 2026-10-17

## Método e alcance
Índice canônico `ARSENAL INDEX.md` e stack `arsenal-autopilot` lidos antes da comparação. Inspecionados READMEs upstream e SKILL.md selecionados; revisão estática documental, sem executar CLIs, apps Electron, Chromium, crawling, MCPs, geradores ou testes de runtime. Dembrandt-skills: triagem das 45 skills pelo catálogo, com aprofundamento de capacidades diferenciadas, não auditoria linha a linha de todos os scripts.

| Fonte | Classe | Capacidade e dependência | Decisão / owner |
|---|---|---|---|
| [Awwwards-mcp](https://github.com/INSANE0777/Awwwards-mcp) | A/D | Pesquisa de referências premiadas, design DNA, brief com evidência, motion DNA, comparação de estruturas; servidor MCP, Node, índice/crawl e Playwright opcionais | UPDATE_EXISTING `skills/design-direction/SKILL.md` (metodologia sem ferramenta) |
| [Responsively App](https://github.com/responsively-org/responsively-app) | B/D | Previews multi-device, interações espelhadas, screenshots, MCP e Electron | UPDATE_EXISTING `skills/runtime-ui-verification/SKILL.md`; app não instalado |
| [Genjutsu](https://github.com/AThevon/genjutsu) | B/D | cast/paint/bunshin: escalas de intervenção, teses, preview, auditoria e limites de custo; ferramentas/scripts de Claude | UPDATE_EXISTING `stacks/creative-web-engineering/STACK.md`; não importar orchestration de agente |
| [Dembrandt](https://github.com/dembrandt/dembrandt) | A/D | Computed styles, inventário e confiança em tokens, DTCG, drift gate e CI; Node/Chromium/MCP/Action | UPDATE_EXISTING `skills/design-system-extraction/SKILL.md` e `skills/design-system-governance/SKILL.md` |
| [Dembrandt-skills](https://github.com/dembrandt/dembrandt-skills) | A/B/D | 45 skills; grande maioria dos padrões já presente no Arsenal; diferenciais: operacional expert UI, coordinated views, marketing vs product tokens | UPDATE_EXISTING `skills/dashboard-design/SKILL.md` e `skills/design-system-governance/SKILL.md`; sem 45 clones |
| [Brag](https://github.com/latent-spaces/brag) | B/D | Storyboard e demonstração real em vídeo curto, share copy; renderização depende de FFmpeg/Hyperframes ou outro motor | UPDATE_EXISTING `stacks/ai-reels-production/STACK.md`; não importar assets ou CLIs |

## Capability ledger e razão de ownership
- Inspiração com evidências: design-direction já possui brief e references, faltava protocolo de comparação explícita por captura, estrutura e motion.
- Responsividade: runtime-ui-verification cobre estados e viewports, faltava matriz de sequências equivalentes entre dispositivos.
- Tokens: design-system-extraction cobre observação/derivação, faltava inventário por confiança/frequência; governance já gerencia owners, faltava gate reproduzível de drift.
- Direção criativa: creative-web-engineering já abrange a construção; a escala interação/página/site e preview-vs-build acrescentam triagem prática.
- UX de especialistas: dashboard-design já cobre ações/exceções, faltavam filtros scope-vs-search e sincronização entre vistas.
- Vídeo: ai-reels-production já cobre reels, mas modo promocional do software com UI demonstrada e privacy gate acrescenta comportamento próprio.

## Segurança e portabilidade
Veredito **CAUTION** para integração binária de todas as fontes: não houve auditoria exaustiva de executáveis, scripts, npm dependency trees ou arquivos gerados. A metodologia documental incorporada é **APPROVE com limites**: nunca instalar ou executar `npx skills add`, `npx dembrandt`, `awwwards-mcp`, `@responsively/mcp`, Hyperframes ou hooks automaticamente; não passar cookies, headers, tokens, capturas privadas ou sites autenticados a serviços externos sem escopo e autorização. Considerar licença, direitos de marcas/assets, prompt injection da página, limites de crawl, supply chain e custos de browser/render. MCP mencionado em README não é ferramenta disponível por definição.

## Testes de aceite conceituais
1. Design premium com referências: citar 2–5 exemplos e distinguir motion observado de inferido; near-miss: reproduzir asset de marca sem licença.
2. QA responsive: mesma sequência e estados em 3 viewports; near-miss: declarar mobile aprovado só por screenshot desktop.
3. Drift: comparar token baseline com estado equivalente, bloquear regressão objetiva, nunca reaprovar baseline para silenciar falha; near-miss: bloquear densidade diferente legitimamente no app.
4. Especialistas: selecionar item tabela/visual sincroniza ambas; near-miss: adicionar gráfico decorativo.
5. Vídeo lançamento: features demonstradas e sem dados privados; near-miss: alucinar métrica ou alegar MP4 sem render.
6. Genjutsu: pequeno hover não dispara orquestração de site; preview não conta como QA.

## Arquivos implementados
- `skills/design-direction/SKILL.md`
- `skills/runtime-ui-verification/SKILL.md`
- `skills/design-system-extraction/SKILL.md`
- `skills/design-system-governance/SKILL.md`
- `stacks/creative-web-engineering/STACK.md`
- `skills/dashboard-design/SKILL.md`
- `stacks/ai-reels-production/STACK.md`
- `evaluations/2026-10-17-six-creative-ui-repositories.md`

Sem nova skill ou mudança no roteamento do índice, pois os owners já existiam. Publicar a avaliação e os updates em commit único; a confirmação é o SHA retornado pelo GitHub e a releitura pós-publicação.
