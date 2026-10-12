# Triagem Arsenal Autopilot: 14 repositórios externos (2026-10-12)

## Escopo e método
Fontes: READMEs oficiais das branches padrão dos 14 projetos e `ARSENAL INDEX.md`, `AGENTS.md`, `stacks/arsenal-autopilot/STACK.md`, `stacks/evaluate-and-import-skill/STACK.md`, `skills/skill-security-review/SKILL.md`, `skills/prose-lint/SKILL.md` do Arsenal. Inspeção estática preliminar, sem executar installers, avaliar binários ou testar runtime. A classificação representa portabilidade/valor, não um atestado de segurança do projeto.

| Fonte | Classe | Capability observada | Owner / decisão | Limites e riscos |
|---|---|---|---|---|
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | D | LMS, cursos, avaliações, AI, editor | `functional-web-app-builder`; KEEP_EXTERNAL_REFERENCE | Plataforma completa, requer hospedagem, DB, identidade e manutenção. |
| [glideapps/glide-data-grid](https://github.com/glideapps/glide-data-grid) | D | grid canvas React virtualizado e editável | `functional-web-app-builder`; KEEP_EXTERNAL_REFERENCE | Biblioteca de UI, sem benefício como skill independente; verificar acessibilidade e API na implementação. |
| [IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge) | A/D | registry, gateway MCP/A2A, ACL, routing, observability | `developer-platform-engineering`, `agent-action-governance`; KEEP_EXTERNAL_REFERENCE | Serviço externo e credenciais; risco de centralizar permissões; requer revisão de deploy e policy. |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | D | vetores PostgreSQL, busca ANN/exata | `software-engineering-cycle`; KEEP_EXTERNAL_REFERENCE | Extensão DB; tuning, migrations e avaliação de retrieval dependem de contexto real. |
| [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | A/D | sandbox multiagente de cenários | `business-decision-intelligence`; KEEP_EXTERNAL_REFERENCE | Saídas simuladas não são previsões validadas; exige dados e avaliação empiricamente ancorada. |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | A/D | launch-video storytelling, ritmo, motion, copy | `content-production`, `ai-reels-production`; KEEP_EXTERNAL_REFERENCE | Pipeline original exige FFmpeg, Node e Hyperframes; não importar dependências sem controle. |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | D | múltiplos backends de fontes web e diagnósticos | `research-and-synthesize`; KEEP_EXTERNAL_REFERENCE | Instalação, autenticação/cookies, scraping, termos dos serviços e rede; não executar setup. |
| [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | B/D | compressão e continuidade de contexto | `ai-workspace-operating-cycle`; ABSORB_METHOD_ONLY como possível melhoria futura | Alegações de economia de tokens não foram benchmarkadas; plugin runtime externo. |
| [EpicGames/raddebugger](https://github.com/EpicGames/raddebugger) | D | debugger nativo Windows x64/PDB, formato RDI | `debug-and-fix`; KEEP_EXTERNAL_REFERENCE | Escopo Windows x64 e release alpha conforme README; não disponível nativamente no ChatGPT. |
| [flutter/flutter](https://github.com/flutter/flutter) | D | SDK multiplataforma Dart | `software-engineering-cycle`; KEEP_EXTERNAL_REFERENCE | Toolchain, build e emuladores exigem ambiente real. |
| [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) | A/B | linguagem técnica controlada, precisão para instruções inter-agentes | `prose-lint`; UPDATE_EXISTING | Inspirado em padrão industrial; evitar alegação de conformidade oficial; regras de inglês não passam ao português. |
| [cursor/plugins](https://github.com/cursor/plugins) | A/D | marketplace de workflows de desenvolvimento | `arsenal-autopilot`; KEEP_EXTERNAL_REFERENCE | Catálogo heterogêneo; auditar plugins individualmente; evitar importar comandos Cursor como nativos. |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | A/D | CAD paramétrico, STEP/STL/GLB, DFM | `architectural-design-cycle`; KEEP_EXTERNAL_REFERENCE | Runtime CAD externo, downloads e telemetria declarada; QA geométrico requer ferramentas reais. |
| [tester-army/e2e](https://github.com/tester-army/e2e) | A/D | E2E em linguagem natural com assertions e replay | `software-testing-engineering`; KEEP_EXTERNAL_REFERENCE | Browser/emulador, provedor LLM e runner externos; assertions verificáveis continuam indispensáveis. |

## Decisão de lote
Atualizar somente `prose-lint` para incorporar regras verificáveis de linguagem técnica controlada, evitando criar nova skill sobreposta. Preservar os outros 13 como referências e candidatos à seleção por necessidade real; não instalar bibliotecas, nem assumir disponibilidade de serviços. A triagem por README não comprova funcionalidade, licenças detalhadas, riscos transitivos ou desempenho.

## Segurança e portabilidade
Veredito sobre **importação de executáveis**: CAUTION, nenhuma instalação autorizada por esta avaliação. Fontes com setup/CLI/MCP/credenciais exigem revisão específica de installer-chain, pins, segredos, rede, persistência e permissões antes de uso real. O método extraído para `prose-lint` é textual e não executa código externo. Recomendação de revisão futura: examinar código/configuração dos candidatos no momento de implementação, versões fixadas e verificações no runtime.

## Acceptance checks
- Instrução ambígua de agente deve resultar em sujeito, condição e fallback explícitos sem perda de modalidade.
- Texto explicativo ou português comum não deve ser rigidamente reescrito para inglês controlado.
- Nenhuma biblioteca de terceiros deve ser apresentada como ferramenta pronta sem instalação e verificação.
