# Avaliação — 30 repositórios de web design, landing pages, social media, UI/UX e creative web

Data: 2026-09-23

## Escopo

Avaliação comparativa contra o Arsenal canônico após leitura do ARSENAL INDEX e da stack evaluate-and-import-skill. O objetivo foi identificar valor incremental, evitar duplicação e adaptar apenas metodologia portátil.

## Critérios

- **A** — skill/processo realmente útil com mudança relevante de comportamento.
- **B** — boa metodologia para incorporar a owner existente.
- **C** — pouco ganho sobre instruções/skills atuais.
- **D** — valor técnico dependente de ferramentas, scripts, bibliotecas ou integrações externas.

## Resultado

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 1 | dawitlabs/ui-skills | A | Adotar parcialmente: direção explícita, tokens/a11y/landing como processos compostos. |
| 2 | mblode/agent-skills | A | Incorporar modos direction/extract/build/audit em owners web existentes. |
| 3 | Firzus/agent-skills | A | Incorporar pipeline design system → greybox → conteúdo real. |
| 4 | PracticalSwan/agent-skills | B | Absorver boas práticas de responsividade/estados/verificação. |
| 5 | PaulRBerg/agent-skills | B | Absorver preservação de stack e prova renderizada. |
| 6 | nolly-studio/agent-skills | A | Adotar conceito de DESIGN.md downstream do código. |
| 7 | AgentsORG/DESIGN | A | Adotar contrato visual persistente sem criar segunda fonte de verdade. |
| 8 | elayadesign/ai-design-skills | A | Incorporar message match, proof placement, objeções e CRO em landing-craft. |
| 9 | wshobson/agents | D | Não importar dependências; preservar apenas entrevista/brand discovery útil. |
| 10 | Spotlight-Revenue/social-content-planner | A | Adaptar ciclo pesquisa → calendário → produção → medição sem exigir Sheets/API. |
| 11 | social-media-skills/skills | A | Criar instagram-growth-diagnostics e usar como router por gargalo. |
| 12 | thatrebeccarae/claude-marketing | B | Usar como referência de estratégia multicanal; não importar benchmarks rígidos. |
| 13 | borghei/Claude-Skills | B | Fonte ampla de referência; sem skill nova. |
| 14 | shalintripathi/saas-marketing-agents | A | Incorporar content operations em content-production. |
| 15 | mahirautela2020-design/claude-skills-ux | B | Biblioteca metodológica; owners atuais já cobrem grande parte. |
| 16 | travisjneuman/.claude | A | Incorporar research-first design e asset grounding em design-direction/web-design-engineer. |
| 17 | kopplin-co/claude-web-design-skill | C | Redundante com web-design-engineer. |
| 18 | jiji262/claude-design-skill | B | Aproveitar direção criativa e variações como método, sem skill separada. |
| 19 | MengTo/Skills | A/D | Usar como fonte técnica de creative web; não criar stack nova sem demanda recorrente. |
| 20 | greensock/gsap-skills | A | Atualizar gsap-animation a partir da fonte oficial. |
| 21 | rbaumier/skills | A | Criar ui-motion-design como camada de intenção acima das bibliotecas. |
| 22 | app-builders-club/design-builder | D | Adaptar padrões quando úteis; não importar toolchain. |
| 23 | podo/design-agent-skills | A/D | Fonte técnica para motion/WebGL/Remotion; owner conforme tecnologia. |
| 24 | GOODMAN-PRO/prism | D | Creative engineering avançado; manter como referência, não skill genérica. |
| 25 | magnus919/agent-skills | A/B | Branding útil, mas voice-builder/design-system já possuem owners próximos; adiar skill nova. |
| 26 | seb1n/awesome-ai-agent-skills | B | Agregador de boas metodologias; evitar duplicação. |
| 27 | MPSQUARK/AgentSkills | B | Absorver discovery proporcional; não impor gates rígidos. |
| 28 | pengGgxp/skills | B | Incorporar princípios de hierarquia/sistema antes de decoração. |
| 29 | tech-leads-club/agent-skills | C | Agregador redundante; usar somente como radar. |
| 30 | NousResearch/hermes-agent | A/D | Conceito de DESIGN.md/tokens é útil; toolchain específica não foi importada. |

## Mudanças adotadas

### Novas skills
- instagram-growth-diagnostics
- design-direction
- ui-motion-design

### Nova stack
- social-growth-engine

### Owners atualizados
- landing-craft
- design-system-extraction
- design-system-governance
- gsap-animation
- web-design-engineer
- content-production

## Decisões de arquitetura

1. **Social**: separar diagnóstico de crescimento da produção. O novo router identifica reach, conversão, retenção/compartilhamento e sustentabilidade antes de acionar content skills.
2. **Web design**: estabelecer pipeline research → direction → contract → greybox → build → motion → runtime verification.
3. **Design system**: DESIGN.md é opcional e downstream da implementação; não deve competir com tokens/código.
4. **Landing**: incorporar message match, prova próxima ao claim, objeções e risco sem inventar métricas ou fórmulas universais.
5. **Motion**: ui-motion-design decide função e linguagem; gsap-animation implementa quando GSAP é apropriado.
6. **Content operations**: ownership, review, capacidade e freshness entram apenas quando recorrência/escala justificam.

## Segurança e portabilidade

- Nenhum installer, setup script ou código arbitrário dos repositórios externos foi executado.
- Dependências específicas de Claude Code, slash commands, subagentes, Playwright instalado pela fonte, APIs obrigatórias e toolchains externas foram removidas ou tratadas como opcionais.
- Integrações externas continuam sujeitas às ferramentas realmente disponíveis e à autorização necessária.
- Claims de algoritmo, benchmarks e performance não foram importados como fatos universais.
- Repositórios técnicos classificados D foram usados apenas como fonte metodológica/técnica, sem copiar permissões ou execução.

## Fontes principais usadas na adoção

- https://github.com/dawitlabs/ui-skills
- https://github.com/mblode/agent-skills
- https://github.com/Firzus/agent-skills
- https://github.com/nolly-studio/agent-skills
- https://github.com/AgentsORG/DESIGN
- https://github.com/elayadesign/ai-design-skills
- https://github.com/Spotlight-Revenue/social-content-planner
- https://github.com/social-media-skills/skills
- https://github.com/shalintripathi/saas-marketing-agents
- https://github.com/travisjneuman/.claude
- https://github.com/MengTo/Skills
- https://github.com/greensock/gsap-skills
- https://github.com/rbaumier/skills
- https://github.com/podo/design-agent-skills

## Veredito

A leva gerou valor real, mas não justifica 30 novas skills. A adoção consolidada foi deliberadamente pequena: 3 skills novas, 1 stack nova e 6 upgrades de owners existentes.
