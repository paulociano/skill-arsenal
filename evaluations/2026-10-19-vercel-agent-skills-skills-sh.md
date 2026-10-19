# Inventário e avaliação: vercel-labs/agent-skills + skills.sh (2026-10-19)

## Escopo e cobertura
- Fonte canônica Arsenal: https://github.com/paulociano/skill-arsenal/blob/master/ARSENAL%20INDEX.md
- Repositório inspecionado: https://github.com/vercel-labs/agent-skills (main); árvore GitHub recursiva, 9 arquivos `SKILL.md` enumerados. A leitura foi de todos os nove `SKILL.md`; não constitui auditoria profunda de cada arquivo auxiliar/script.
- Diretório de descoberta: https://skills.sh/ e https://skills.sh/docs/api . Catálogo dinâmico com grande número de skills e origens. **Não há evidência de leitura/auditoria individual de todas as entradas do Skills.sh**; é tecnicamente uma superfície aberta, incompatível com declarar cobertura total num lote finito. Ranking não certifica segurança ou ganho.
- Stack usada: `arsenal-autopilot`, com critérios `skill-security-review` e `verify-before-claim`.

## Matriz das 9 skills do repositório
| Fonte | Classificação | Decisão | Owner |
|---|---|---|---|
| react-best-practices | A/B | CREATE_NEW | skills/react-next-performance/SKILL.md |
| vercel-optimize | A/D | CREATE_NEW | skills/vercel-platform-optimization/SKILL.md |
| composition-patterns | B | UPDATE_EXISTING | skills/codebase-design/SKILL.md |
| react-native-skills | B | UPDATE_EXISTING | skills/crossplatform-mobile-engineering/SKILL.md |
| react-view-transitions | A/B | UPDATE_EXISTING | skills/ui-motion-design/SKILL.md |
| web-design-guidelines | B | UPDATE_EXISTING | skills/web-quality-audit/SKILL.md |
| writing-guidelines | B | UPDATE_EXISTING | skills/writing-quality/SKILL.md |
| deploy-to-vercel | D | KEEP_EXTERNAL_REFERENCE | Vercel deployment connector + vercel deployments-cicd existente |
| vercel-cli-with-tokens | D | KEEP_EXTERNAL_REFERENCE | Vercel deployment connector + segurança de credenciais |

## Evidência de publicação
- react-next-performance: https://github.com/paulociano/skill-arsenal/commit/ef090d3a240adfdde704e9f1a3a16f127275463e
- vercel-platform-optimization: https://github.com/paulociano/skill-arsenal/commit/0e966704eaa2af81f83319d84aef857826827475
- codebase-design: https://github.com/paulociano/skill-arsenal/commit/3f288c756f1bb6362bc36caf583519249c03be2f
- crossplatform-mobile-engineering: https://github.com/paulociano/skill-arsenal/commit/fa11fabb8c240acfacd0d03b2f98279ef4ea4224
- ui-motion-design: https://github.com/paulociano/skill-arsenal/commit/da98ea06c9fee08063415cdcafb4c68af5afef17
- web-quality-audit: https://github.com/paulociano/skill-arsenal/commit/86b0bbd50276875dc4a729469e0c7343e1578aa9
- writing-quality: https://github.com/paulociano/skill-arsenal/commit/50c61067d7d5c1b8444014cab4e84be8927b920a
- index: https://github.com/paulociano/skill-arsenal/commit/7e905195656fa36a2ffe11e5b6ce8a13cbe543a5

## Fit e redução de sobreposição
- Performance React/Next não tinha owner específico identificado; skill nova é estreita e medida.
- Vercel Optimize tem hipótese diferencial "métricas primeiro, candidatos filtrados, código depois"; skill nova é para auditoria específica de plataforma.
- Os outros cinco métodos incrementais foram absorvidos por owners existentes para evitar skills redundantes.
- Deploy/CLI/token dependem de ferramenta real e privilégios; preservar como referência externa, preferindo conector Vercel atual. Não copiar scripts de upload anônimo, nem orientar impressão de tokens.

## Segurança
**CAUTION** (revisão documental e parcial de scripts, sem instalação/runtime). Riscos materiais: scripts de deploy/upload, tokens de API, mudanças de configuração, custos por ações de billing, CLI e publicação em ambiente errado. `vercel-cli-with-tokens` sugere comandos `printenv VERCEL_TOKEN` e `grep` em `.env` que podem ecoar segredos; estes passos **não** foram adotados. O guia `deploy-to-vercel` inclui scripts de fallback com upload e publicação externos; não foram executados ou incorporados. Acesso a métricas de produção/Observability Plus precisa de permissões reais. Nenhuma skill externa foi instalada.

## Skills.sh: resultado restrito à triagem
- O catálogo é descoberta e não fonte canônica; os exemplos em destaque incluem skills já avaliadas anteriormente pelo Arsenal (mattpocock/skills, anthropics/skills, remotion-dev/skills, expo/skills).
- Uma cobertura integral exigiria enumerar a API autenticada e resolver cada origem/revisão, auditar conteúdo + dependências + licença e manter inventário versionado. Não foi executado, e não se afirma conclusão.
- Não promover popularidade e contagens de instalação a qualidade, segurança, compatibilidade ou benchmark.
