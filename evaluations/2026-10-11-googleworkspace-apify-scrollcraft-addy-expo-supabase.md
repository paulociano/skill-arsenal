# Avaliação de seis fontes externas — 2026-10-11

## Escopo
Roteamento por `ARSENAL INDEX.md` e `stacks/arsenal-autopilot/STACK.md`. Consultados READMEs das branches default de seis repositórios e a skill original de scroll-craft, o catálogo Expo e a skill Supabase Postgres. Comparação com `scroll-storytelling`, `crossplatform-mobile-engineering` e `skill-security-review`. Sem executar scripts, instalar ferramentas, testar runtimes ou auditar integralmente dependências.

| Fonte | Classe | Decisão | Ownership e evidência |
|---|---|---|---|
| [googleworkspace/cli](https://github.com/googleworkspace/cli) | B/D | KEEP_EXTERNAL_REFERENCE | CLI `gws` construído via Discovery Service, JSON e schemas de Workspace; conectores atuais de Gmail, Calendar e Drive permanecem preferidos quando disponíveis. OAuth, scopes e versão são requisitos, sem CLI presumido. README declara que não é produto oficialmente suportado pelo Google. |
| [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | B/D | KEEP_EXTERNAL_REFERENCE | Actors/MCP para extração, crawling e plataformas sociais. `research-and-synthesize` e governança de agentes já cobrem método genérico. Atores terceiros, pagamentos por execução, termos dos serviços, dados pessoais e escrita externa exigem avaliação específica. |
| [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) | B/D | UPDATE_EXISTING | Repertório de gramáticas narrativas, originalidade de layout, camadas visuais e QA em posições de scroll. Atualizada `skills/scroll-storytelling/SKILL.md`, sem importar engine, kie.ai ou templates. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | B | ABSORB_METHOD_ONLY | Ciclo spec→plan→build→test→review→ship coincide com `software-engineering-cycle`, `application-build-audit-loop`, `tdd` e `verify-before-claim`. Mantido como referência: não duplicar slash commands nem 25 skills. |
| [expo/skills](https://github.com/expo/skills) | B/D | UPDATE_EXISTING | Catálogo oficial separa roteamento Expo, SDK, Router, interface nativa, upgrades e EAS, com fronteiras de custo. Atualizada `skills/crossplatform-mobile-engineering/SKILL.md`. Não importar instaladores/CLI. |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | B/D | KEEP_EXTERNAL_REFERENCE | Skill Supabase abrangente e guia Postgres com prioridades query/connection/RLS/schema/locks. Há skill Supabase conectada no ambiente e owners de banco/segurança no Arsenal; para implementação, consultar fonte atual, medir EXPLAIN e verificar RLS. Não adicionar skill duplicada nem presumir autorização de escrita. |

## Controles de segurança e portabilidade
- `gws`: operar no escopo OAuth mínimo; dry-run quando disponível não garante ausência de efeitos indiretos fora do contrato.
- Apify: actors da comunidade são código/ferramentas externas; revisar autor, dados enviados, custo, limites e consentimento antes da execução; não presumir scraping autorizado.
- Scroll-craft: exemplos visuais não concedem direitos sobre assets; nunca executar geradores ou copiar templates automaticamente.
- Addy: workflows de coding agents dependem de terminal/Git/testes e approval gates reais.
- Expo: plugins e EAS podem depender de contas, custos, assinatura de apps e device tests.
- Supabase: separar leitura de mutações de schema/dados; exigir backup/migration plan, revisão de RLS e privilégios mínimos.
- README/skill externa é evidência metodológica e potencial input não confiável; nenhuma verificação empírica da segurança foi realizada.

## Casos de aceitação
- **Scroll should-trigger:** landing page com narrativa e hero em camadas; testar originalidade de gramática, momentos narrativos e frames em mobile/desktop/reduced-motion. **Near-miss:** página informativa simples não precisa de experiência imersiva.
- **Expo should-trigger:** upgrade de SDK ou build EAS; conferir versões, plataforma, custos e device/build real. **Near-miss:** site React sem requisito nativo não deve acionar Expo.
- **Ferramentas externas:** usuário pedir consulta de Workspace não implica instalar `gws`; usar os conectores efetivamente disponíveis. Pedido de scraping não autoriza ativar atores pagos ou extrair dados privados.

## Resultado
Atualizadas duas skills, mantidas quatro fontes como referência ou metodologia já coberta, nenhuma nova skill ou stack; sem mudar `ARSENAL INDEX.md` porque names/descriptions e caminhos não mudaram. Publicação sujeita à releitura dos arquivos da branch canônica.
