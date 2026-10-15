# Inventário individual verificável: antfu/skills

Data: 2026-10-15. Total: 11 SKILL.md. Base: main. Árvore truncada: false.

**Importante:** todas as linhas são triagem automática por caminho, NÃO leitura ou aprovação de cada arquivo. Classes e flags são provisórias; cada documento precisa ser aberto e avaliado antes de importar. 'REVIEW_HIGH_RISK' exige autorização/controles adicionais. 'REVIEW_OVERLAP' não equivale a duplicata confirmada.

| # | Skill / origem | Classe preliminar | Gate pendente | Hipótese para revisão |
|---:|---|---|---|---|
| 1 | [antfu-create-pr](https://github.com/antfu/skills/blob/main/skills/antfu-create-pr/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |
| 2 | [antfu](https://github.com/antfu/skills/blob/main/skills/antfu/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |
| 3 | [nitro](https://github.com/antfu/skills/blob/main/skills/nitro/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |
| 4 | [nuxt](https://github.com/antfu/skills/blob/main/skills/nuxt/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |
| 5 | [pinia](https://github.com/antfu/skills/blob/main/skills/pinia/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |
| 6 | [pnpm](https://github.com/antfu/skills/blob/main/skills/pnpm/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |
| 7 | [unocss](https://github.com/antfu/skills/blob/main/skills/unocss/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |
| 8 | [vite](https://github.com/antfu/skills/blob/main/skills/vite/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |
| 9 | [vitepress](https://github.com/antfu/skills/blob/main/skills/vitepress/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |
| 10 | [vitest](https://github.com/antfu/skills/blob/main/skills/vitest/SKILL.md) | B/D | REVIEW_OVERLAP | overlap likely with existing quality/security capabilities |
| 11 | [vue](https://github.com/antfu/skills/blob/main/skills/vue/SKILL.md) | B/D | REVIEW_CONTENT | content and dependency verification needed |

## Leitura de conteúdo individual e decisão (11 skills)

Cada SKILL.md abaixo foi aberto e inspecionado em seu conteúdo principal, incluindo description, workflow e dependências declaradas. Isso **não** equivale a inspeção completa de todos os arquivos references/scripts, nem teste de execução; veredito de segurança da fonte: CAUTION para adoção com runtime externo até revisão específica.

| Skill | Classe | Decisão | Owner | Razão específica |
|---|---|---|---|---|
| antfu-create-pr | B | REFERENCE | code-review / software-engineering-cycle | PR evidenciado e screenshots; depende de Git/gh no runtime |
| antfu | B | REFERENCE | coding-agent-engineering | Convenções TS opinativas; específicas de stack |
| nitro | D | REFERENCE | software-engineering-cycle | Nitro 3 beta: confirmar versão do projeto |
| nuxt | D | REFERENCE | functional-web-app-builder | Nuxt 5 prerelease; documentação sujeita a mudanças |
| pinia | D | REFERENCE | functional-web-app-builder | Guia Pinia 4: usar apenas em projetos compatíveis |
| pnpm | D | REFERENCE | software-engineering-cycle | Gestão de monorepo e resolução de pacotes, dependente do projeto |
| unocss | D | REFERENCE | web-design-engineer | Presets e configuração locais definem comportamento |
| vite | D | REFERENCE | software-engineering-cycle | Vite e bundler: checar versão e projeto |
| vitepress | D | REFERENCE | web-design-engineer | Documentação de sites VitePress |
| vitest | D | REFERENCE | software-testing-engineering | Testes Vitest, dependente de runtime Node |
| vue | D | REFERENCE | functional-web-app-builder | Vue 3 e Composition API, referência condicionada à versão |
