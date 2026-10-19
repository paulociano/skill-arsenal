# Arsenal Autopilot: CSS Protips, dzhng Skills, vibe-motion e Web Skills (2026-10-19)

## Fonte e procedimento
- Fonte oficial e canônica: https://github.com/paulociano/skill-arsenal (branch master). Lidos primeiro `ARSENAL INDEX.md`, `AGENTS.md` e `stacks/arsenal-autopilot/STACK.md`.
- Fontes externas lidas diretamente nos respectivos repositórios, ramo padrão: https://github.com/AllThingsSmitty/css-protips (master), https://github.com/dzhng/skills (main), https://github.com/vibe-motion/skills (main), https://github.com/andreasbm/web-skills (master).
- Revisão seletiva de README, árvores e SKILL.md candidatos. Não afirma inspeção exaustiva dos arquivos, scripts ou dependências de terceiros.

## Avaliações e decisões
1. **AllThingsSmitty/css-protips — B; ABSORB_METHOD_ONLY / UPDATE_EXISTING.** Catálogo de dicas CSS, não Agent Skill. Valor: checklist contextual de box sizing, aspect ratio, propriedades lógicas, selectors e focus visível. **Publicado em `skills/modern-css-practices/SKILL.md`.** Descartados resets universais, manipulação de conteúdo semântico com pseudo-elementos e hacks antigos como regras automáticas. Manter fonte como referência histórica, verificar compatibilidade atual e browser alvo.
2. **dzhng/skills — A/B/D; UPDATE_EXISTING seletivo.** Biblioteca real de skills. Lidos `skills/engineering/ratchet-files/SKILL.md`, `skills/engineering/explore-unknowns/SKILL.md`, `skills/visual/compare-screenshots/SKILL.md` e outros candidatos por árvore. Incrementos: ratchet mensurável para arquivos grandes, splitting semântico sob testes, governança de hooks; comparação visual com referência aprovada, landmarks e metricas não decisórias. **Publicados em `skills/software-factory-operations/SKILL.md` e `skills/runtime-ui-verification/SKILL.md`.** `explore-unknowns` permanece referência externa: fluxo de entrevista longa é excessivo como padrão em tarefas que podem ser resolvidas com contexto e evidência direta. Não copiar dependências ou subagentes da origem.
3. **vibe-motion/skills — A/B/D; UPDATE_EXISTING seletivo.** Coleção de skills e geradores de motion. Lidos `disney-animation-rule-skill/SKILL.md`, `pixel2motion/SKILL.md`, `remotion-candlestick/SKILL.md`, além de README e estrutura. Incrementos: fases funcionais de movimento e frame determinístico; vetor semanticamente segmentado para animação e final-frame contract. **Publicados em `skills/ui-motion-design/SKILL.md` e `skills/image-to-svg-vectorization/SKILL.md`.** Skills específicas de Remotion, Puppeteer, Three.js ou dependências externas só podem ser usadas se projeto e runtime as suportarem. Código e assets externos não importados.
4. **andreasbm/web-skills — B/C; KEEP_EXTERNAL_REFERENCE.** Mapa de estudos de desenvolvimento web, não coleção de Agent Skills. Cobre HTML, CSS, JavaScript, acessibilidade, PWA, performance, frameworks, testes, arquitetura e aprendizado. O Arsenal já tem owners específicos (`modern-css-practices`, `web-quality-audit`, `pwa-engineering`, `web-design-engineer`, entre outros). **Nenhuma nova skill criada**, por ausência de comportamento operacional incremental demonstrado. Útil como trilha educacional, sem autoridade normativa e com itens históricos.

## Capability ledger
| Capacidade | Owner canônico | Ação |
|---|---|---|
| Micro-padrões CSS filtrados por semântica e browser | modern-css-practices | UPDATE_EXISTING |
| Ratchet e decomposição semântica de source oversized | software-factory-operations | UPDATE_EXISTING |
| Comparação de screenshots com visual approved target | runtime-ui-verification | UPDATE_EXISTING |
| Fases de animação, peso, follow-through e frame determinístico | ui-motion-design | UPDATE_EXISTING |
| Vetor estruturado para movimento e último quadro fiel ao master | image-to-svg-vectorization | UPDATE_EXISTING |
| Quadrant walk de descoberta | já coberto por discovery/spec workflows sob demanda | KEEP_EXTERNAL_REFERENCE |
| Catálogo de competências web | owners web existentes | KEEP_EXTERNAL_REFERENCE |

## Publicação
Alterações no GitHub canônico:
- `skills/modern-css-practices/SKILL.md`
- `skills/software-factory-operations/SKILL.md`
- `skills/runtime-ui-verification/SKILL.md`
- `skills/ui-motion-design/SKILL.md`
- `skills/image-to-svg-vectorization/SKILL.md`
- Este registro de avaliação.

Nenhum frontmatter, owner ou descrição de índice alterado materialmente, então `ARSENAL INDEX.md` não exigiu atualização. Publicado via GitHub Contents API com SHA de cada arquivo, sem force-push.

## Segurança, portabilidade e verificação
Nenhum installer, script externo, biblioteca ou hook executado; nenhuma integração suposta disponível; nenhum asset licenciado copiado. QA de runtime dos workflows futuros permanece a cargo dos projetos consumidores. Fazer leitura pós-escrita para verificar os arquivos publicados e não confundir alteração de instruções com prova de execução de softwares futuros.
