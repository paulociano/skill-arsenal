# Triagem do registro AutoSkills (11/10/2026)

Fonte: https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry

## Escopo e método

- Foram identificadas **219** entradas SKILL.md na árvore da branch main por API GitHub.
- O catálogo foi cruzado com o índice canônico do Arsenal, com a stack `arsenal-autopilot` e com o critério de não duplicar owners.
- **Limite essencial:** somente 8 SKILL.md de amostra foram lidos integralmente nesta rodada. As demais 211 entradas têm **triagem de metadados, não avaliação semântica nem auditoria de segurança individual**. Classificações abaixo são **provisórias** para triagem, não vereditos de adoção.
- Classes: B = metodologia potencialmente absorvível; D = dependência técnica/ecossistema; A/D = possível fluxo útil dependente de validação técnica. Não se atribuiu classe C sem exame de conteúdo.
- Decisão geral: **não importar nenhuma skill automaticamente**. Não foi demonstrado ganho incremental suficiente em uma skill nova, e a licença-raiz do repositório é CC BY-NC 4.0; arquivos individuais podem ter licenças distintas. Checar licença e origem antes de qualquer reutilização textual.
- Não foi executado `npx autoskills`, instalador, código de terceiros ou scanner. Sem execução = nenhuma garantia de segurança.

## Achados dos oito arquivos efetivamente lidos

| Skill | Resultado | Direção |
|---|---|---|
| accessibility | B: WCAG 2.2, princípios POUR, checks operacionais | Comparar ao owner atual de acessibilidade antes de acrescentar critérios |
| agents-sdk | D: Cloudflare Agents SDK, runtime e APIs específicas | Referência externa quando houver projeto Cloudflare Agents |
| gsap-performance | B/D: transform/opacity, layout thrashing | Coberto pelo ciclo de motion/web; não duplicar |
| react-best-practices | B/D: regras de performance React/Next | Comparar owner de performance frontend; priorização de regras como referência |
| web-perf | D/B: exige Chrome DevTools MCP para medições; fonte documental útil | Nunca prometer métricas medidas sem ferramenta/trace |
| rails-migration-safety | A/D: rollout em fases, backfill e locking | Aprofundar apenas diante de projeto Rails/produção real |
| clerk-webhooks | D: Clerk, verificação de assinatura e secret | Consultar documentação atual e exigir verificação em projetos Clerk |
| threejs-shaders | D: GLSL, ShaderMaterial e pipeline Three.js | Referência sob demanda para shaders; evitar skill horizontal |

## Catálogo de triagem individual (provisório)

| # | Skill | Classe inicial | Ação provisória | Profundidade |
|---:|---|---|---|---|
| 1 | [accessibility](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/accessibility) | B | Comparar metodologia com owner atual | Lida |
| 2 | [adev-writing-guide](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/adev-writing-guide) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 3 | [agents-sdk](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/agents-sdk) | A/D | Candidata condicional; aprofundar somente em uso real | Lida |
| 4 | [android-architecture-clean](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/android-architecture-clean) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 5 | [android-compose-foundations](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/android-compose-foundations) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 6 | [android-coroutines-flow](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/android-coroutines-flow) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 7 | [android-di-hilt](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/android-di-hilt) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 8 | [android-gradle-build-logic](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/android-gradle-build-logic) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 9 | [android-kotlin-core](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/android-kotlin-core) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 10 | [android-networking-retrofit-okhttp](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/android-networking-retrofit-okhttp) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 11 | [android-testing-unit](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/android-testing-unit) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 12 | [angular-developer](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/angular-developer) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 13 | [aspnet-core](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/aspnet-core) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 14 | [aspnet-minimal-api-openapi](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/aspnet-minimal-api-openapi) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 15 | [astro](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/astro) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 16 | [azure-ai](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/azure-ai) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 17 | [azure-cost](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/azure-cost) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 18 | [azure-deploy](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/azure-deploy) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 19 | [azure-diagnostics](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/azure-diagnostics) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 20 | [bash-defensive-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/bash-defensive-patterns) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 21 | [best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/best-practices) | B | Comparar metodologia com owner atual | Metadados |
| 22 | [building-native-ui](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/building-native-ui) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 23 | [bun](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/bun) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 24 | [chrome-extension-development](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/chrome-extension-development) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 25 | [clerk-android](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-android) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 26 | [clerk-astro-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-astro-patterns) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 27 | [clerk-backend-api](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-backend-api) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 28 | [clerk-chrome-extension-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-chrome-extension-patterns) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 29 | [clerk-custom-ui](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-custom-ui) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 30 | [clerk-expo-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-expo-patterns) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 31 | [clerk-nextjs-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-nextjs-patterns) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 32 | [clerk-nuxt-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-nuxt-patterns) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 33 | [clerk-orgs](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-orgs) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 34 | [clerk-react-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-react-patterns) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 35 | [clerk-react-router-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-react-router-patterns) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 36 | [clerk-setup](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-setup) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 37 | [clerk-swift](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-swift) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 38 | [clerk-tanstack-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-tanstack-patterns) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 39 | [clerk-testing](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-testing) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 40 | [clerk-vue-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-vue-patterns) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 41 | [clerk-webhooks](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk-webhooks) | D | Referência técnica sob demanda; não importar em massa | Lida |
| 42 | [clerk](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/clerk) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 43 | [cloudflare-deploy](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/cloudflare-deploy) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 44 | [cloudflare](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/cloudflare) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 45 | [composition-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/composition-patterns) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 46 | [containerize-aspnetcore](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/containerize-aspnetcore) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 47 | [core-data-expert](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/core-data-expert) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 48 | [csharp-async](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/csharp-async) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 49 | [csharp-docs](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/csharp-docs) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 50 | [csharp-mstest](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/csharp-mstest) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 51 | [csharp-nunit](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/csharp-nunit) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 52 | [csharp-tunit](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/csharp-tunit) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 53 | [csharp-xunit](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/csharp-xunit) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 54 | [dart-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/dart-best-practices) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 55 | [deno-deploy](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/deno-deploy) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 56 | [deno-expert](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/deno-expert) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 57 | [deno-frontend](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/deno-frontend) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 58 | [deno-guidance](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/deno-guidance) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 59 | [deno-sandbox](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/deno-sandbox) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 60 | [deno-typescript](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/deno-typescript) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 61 | [deploy-to-vercel](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/deploy-to-vercel) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 62 | [design-mobile-apps](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/design-mobile-apps) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 63 | [django-expert](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/django-expert) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 64 | [django-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/django-patterns) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 65 | [django-security](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/django-security) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 66 | [dotnet-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/dotnet-best-practices) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 67 | [dotnet-design-pattern-review](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/dotnet-design-pattern-review) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 68 | [dotnet-upgrade](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/dotnet-upgrade) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 69 | [drizzle](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/drizzle) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 70 | [durable-objects](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/durable-objects) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 71 | [elevenlabs-music](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/elevenlabs-music) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 72 | [elevenlabs-tts](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/elevenlabs-tts) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 73 | [elysiajs](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/elysiajs) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 74 | [emailAndPassword](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/emailAndPassword) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 75 | [expo-api-routes](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/expo-api-routes) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 76 | [expo-cicd-workflows](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/expo-cicd-workflows) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 77 | [expo-deployment](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/expo-deployment) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 78 | [expo-dev-client](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/expo-dev-client) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 79 | [expo-tailwind-setup](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/expo-tailwind-setup) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 80 | [fastapi-python](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/fastapi-python) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 81 | [fastapi-templates](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/fastapi-templates) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 82 | [fastmcp](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/fastmcp) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 83 | [flask-api-development](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/flask-api-development) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 84 | [fluentui-blazor](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/fluentui-blazor) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 85 | [flutter-animations](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/flutter-animations) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 86 | [flutter-expert](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/flutter-expert) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 87 | [flutter-testing](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/flutter-testing) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 88 | [frontend-design](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/frontend-design) | B | Comparar metodologia com owner atual | Metadados |
| 89 | [generating-sorbet-inline](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/generating-sorbet-inline) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 90 | [generating-sorbet](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/generating-sorbet) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 91 | [golang-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/golang-patterns) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 92 | [golang-testing](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/golang-testing) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 93 | [gsap-core](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/gsap-core) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 94 | [gsap-frameworks](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/gsap-frameworks) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 95 | [gsap-performance](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/gsap-performance) | D | Referência técnica sob demanda; não importar em massa | Lida |
| 96 | [gsap-plugins](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/gsap-plugins) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 97 | [gsap-react](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/gsap-react) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 98 | [gsap-scrolltrigger](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/gsap-scrolltrigger) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 99 | [gsap-timeline](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/gsap-timeline) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 100 | [gsap-utils](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/gsap-utils) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 101 | [hono](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/hono) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 102 | [instantdb](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/instantdb) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 103 | [java-coding-standards](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/java-coding-standards) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 104 | [java-docs](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/java-docs) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 105 | [java-springboot](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/java-springboot) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 106 | [kotlin-tooling-agp9-migration](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/kotlin-tooling-agp9-migration) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 107 | [kotlin-tooling-cocoapods-spm-migration](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/kotlin-tooling-cocoapods-spm-migration) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 108 | [laravel-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/laravel-patterns) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 109 | [laravel-specialist](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/laravel-specialist) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 110 | [machine-learning](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/machine-learning) | B | Comparar metodologia com owner atual | Metadados |
| 111 | [migrate-to-vinext](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/migrate-to-vinext) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 112 | [minimal-api-file-upload](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/minimal-api-file-upload) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 113 | [native-data-fetching](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/native-data-fetching) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 114 | [neon-postgres](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/neon-postgres) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 115 | [nestjs-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/nestjs-best-practices) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 116 | [next-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/next-best-practices) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 117 | [next-cache-components](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/next-cache-components) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 118 | [next-upgrade](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/next-upgrade) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 119 | [nodejs-backend-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/nodejs-backend-patterns) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 120 | [nodejs-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/nodejs-best-practices) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 121 | [nodejs-express-server](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/nodejs-express-server) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 122 | [nuxt](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/nuxt) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 123 | [organization](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/organization) | B | Comparar metodologia com owner atual | Metadados |
| 124 | [oxlint](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/oxlint) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 125 | [pandas-data-analysis](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/pandas-data-analysis) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 126 | [pandas-pro](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/pandas-pro) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 127 | [php-pro](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/php-pro) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 128 | [playwright-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/playwright-best-practices) | B | Comparar metodologia com owner atual | Metadados |
| 129 | [pr_review](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/pr_review) | B | Comparar metodologia com owner atual | Metadados |
| 130 | [prisma-cli](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/prisma-cli) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 131 | [prisma-client-api](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/prisma-client-api) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 132 | [prisma-database-setup](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/prisma-database-setup) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 133 | [prisma-postgres](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/prisma-postgres) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 134 | [pydantic](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/pydantic) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 135 | [python-background-jobs](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/python-background-jobs) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 136 | [python-executor](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/python-executor) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 137 | [python-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/python-patterns) | B | Comparar metodologia com owner atual | Metadados |
| 138 | [python-testing-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/python-testing-patterns) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 139 | [rails-background-jobs](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rails-background-jobs) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 140 | [rails-bug-triage](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rails-bug-triage) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 141 | [rails-code-review](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rails-code-review) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 142 | [rails-guides](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rails-guides) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 143 | [rails-migration-safety](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rails-migration-safety) | D | Referência técnica sob demanda; não importar em massa | Lida |
| 144 | [rails-security-review](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rails-security-review) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 145 | [rails-stack-conventions](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rails-stack-conventions) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 146 | [rails-tdd-slices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rails-tdd-slices) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 147 | [rails-upgrade](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rails-upgrade) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 148 | [react-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/react-best-practices) | B | Comparar metodologia com owner atual | Lida |
| 149 | [react-hook-form](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/react-hook-form) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 150 | [react-three-fiber](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/react-three-fiber) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 151 | [redis-development](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/redis-development) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 152 | [refactor-module](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/refactor-module) | B | Comparar metodologia com owner atual | Metadados |
| 153 | [reference-compiler-cli](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/reference-compiler-cli) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 154 | [reference-core](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/reference-core) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 155 | [reference-signal-forms](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/reference-signal-forms) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 156 | [remotion](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/remotion) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 157 | [rspec-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rspec-best-practices) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 158 | [rspec-service-testing](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rspec-service-testing) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 159 | [ruby-on-rails-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/ruby-on-rails-best-practices) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 160 | [ruby](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/ruby) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 161 | [rust-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/rust-best-practices) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 162 | [sandbox-sdk](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/sandbox-sdk) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 163 | [scikit-learn](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/scikit-learn) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 164 | [senior-data-scientist](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/senior-data-scientist) | B | Comparar metodologia com owner atual | Metadados |
| 165 | [seo](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/seo) | B | Comparar metodologia com owner atual | Metadados |
| 166 | [shadcn](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/shadcn) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 167 | [sqlalchemy-alembic-expert-best-practices-code-review](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/sqlalchemy-alembic-expert-best-practices-code-review) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 168 | [sqlalchemy](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/sqlalchemy) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 169 | [stripe-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/stripe-best-practices) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 170 | [supabase-postgres-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/supabase-postgres-best-practices) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 171 | [svelte-code-writer](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/svelte-code-writer) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 172 | [svelte5-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/svelte5-best-practices) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 173 | [swift-concurrency](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/swift-concurrency) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 174 | [swift-testing-expert](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/swift-testing-expert) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 175 | [swiftui-expert-skill](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/swiftui-expert-skill) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 176 | [tailwind-css-patterns](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/tailwind-css-patterns) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 177 | [tailwind-v4-shadcn](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/tailwind-v4-shadcn) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 178 | [tanstack-start](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/tanstack-start) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 179 | [tauri-v2](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/tauri-v2) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 180 | [terraform-module-library](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/terraform-module-library) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 181 | [terraform-stacks](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/terraform-stacks) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 182 | [terraform-style-guide](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/terraform-style-guide) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 183 | [test-driven-development](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/test-driven-development) | B | Comparar metodologia com owner atual | Metadados |
| 184 | [threejs-animation](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-animation) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 185 | [threejs-fundamentals](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-fundamentals) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 186 | [threejs-geometry](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-geometry) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 187 | [threejs-interaction](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-interaction) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 188 | [threejs-lighting](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-lighting) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 189 | [threejs-loaders](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-loaders) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 190 | [threejs-materials](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-materials) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 191 | [threejs-postprocessing](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-postprocessing) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 192 | [threejs-shaders](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-shaders) | D | Referência técnica sob demanda; não importar em massa | Lida |
| 193 | [threejs-textures](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/threejs-textures) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 194 | [turborepo](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/turborepo) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 195 | [twoFactor](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/twoFactor) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 196 | [typescript-advanced-types](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/typescript-advanced-types) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 197 | [upgrade-stripe](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/upgrade-stripe) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 198 | [upgrading-expo](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/upgrading-expo) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 199 | [use-ai-sdk](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/use-ai-sdk) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 200 | [use-dom](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/use-dom) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 201 | [vite](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/vite) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 202 | [vitest](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/vitest) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 203 | [vue-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/vue-best-practices) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 204 | [vue-debug-guides](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/vue-debug-guides) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 205 | [vue-pinia-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/vue-pinia-best-practices) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 206 | [vue](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/vue) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |
| 207 | [web-perf](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/web-perf) | B | Comparar metodologia com owner atual | Lida |
| 208 | [wordpress-router](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/wordpress-router) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 209 | [workers-best-practices](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/workers-best-practices) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 210 | [wp-block-development](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/wp-block-development) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 211 | [wp-block-themes](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/wp-block-themes) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 212 | [wp-performance](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/wp-performance) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 213 | [wp-plugin-development](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/wp-plugin-development) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 214 | [wp-project-triage](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/wp-project-triage) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 215 | [wp-rest-api](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/wp-rest-api) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 216 | [wp-wpcli-and-ops](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/wp-wpcli-and-ops) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 217 | [wrangler](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/wrangler) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 218 | [xcode-build-orchestrator](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/xcode-build-orchestrator) | D | Referência técnica sob demanda; não importar em massa | Metadados |
| 219 | [zod](https://github.com/midudev/autoskills/tree/main/packages/autoskills/skills-registry/zod) | A/D | Candidata condicional; aprofundar somente em uso real | Metadados |

## Próxima decisão técnica

Não converter automaticamente catálogo de terceiros em skills do Arsenal. Quando uma implementação demandar uma tecnologia listada, ler o SKILL.md e suas referências na versão fixada, resolver owner canônico, revisar segurança e licença, testar ganho incremental e só então adaptar ou criar recurso com índice sincronizado. Esta avaliação é uma **triagem completa das 219 entradas**, não uma auditoria aprofundada de 219 skills.
