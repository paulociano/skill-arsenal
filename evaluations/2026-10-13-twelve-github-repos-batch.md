# Avaliação em lote — 12 fontes externas (2026-10-13)

## Escopo e método

Roteamento: `ARSENAL INDEX.md` → `arsenal-autopilot` → `evaluate-and-import-skill`. Foram consultados os READMEs da branch HEAD de cada repositório via GitHub e comparados com owners existentes no índice; aprofundamento em `plain-writing`, `ui-motion-design`, `computer-use-agent-engineering`, `agent-memory-engineering` e `skill-security-review`. **Esta é uma triagem fundamentada em documentação de topo, não uma auditoria de código-fonte completo ou prova de runtime.**

## Ledger e decisões

| Fonte | Classe | Owner/decisão | Segurança e portabilidade |
|---|---|---|---|
| [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | B/D | UPDATE_EXISTING candidate: ui-motion-design, cinematic visual; runtime Node/Chrome/ffmpeg not imported | CAUTION runtime, generated media and supply chain |
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | A/D | KEEP_EXTERNAL_REFERENCE: interactive isometric explanatory SVG/WebGL/3D; consider new skill only after inspecting SKILL.md and reproducible use case | CAUTION executable renderer; no runtime verified |
| [rociiu/talorys](https://github.com/rociiu/talorys) | D | KEEP_EXTERNAL_REFERENCE: Cloudflare-hosted personal agent product; memory and automations overlap with existing Arsenal methods | CAUTION owner credentials, Workers, persistence and hosted services |
| [marclou/mailcheap](https://github.com/marclou/mailcheap) | D | KEEP_EXTERNAL_REFERENCE: self-host newsletter product using SES/MongoDB/QStash; relevant to email-campaign-engineering architecture, not a skill import | CAUTION mailing-list data, credentials, deliveries, compliance |
| [academa-labs/manimgx](https://github.com/academa-labs/manimgx) | D | KEEP_EXTERNAL_REFERENCE: Rust/wgpu animation engine, Manim-compatible API; use only if installed and tested | CAUTION executable package and renderer |
| [shaongitbd/doory](https://github.com/shaongitbd/doory) | D | KEEP_EXTERNAL_REFERENCE: full browser visual editor/self-host stack; no direct runtime from README | CAUTION hosting/storage/licensing and dependency review |
| [fayazara/robot-heads](https://github.com/fayazara/robot-heads) | D/B | KEEP_EXTERNAL_REFERENCE: React canvas robot status component; possible pattern for visible agent-state feedback | CAUTION package version, accessibility, animation load |
| [aindeev/agent-chrome-relay](https://github.com/aindeev/agent-chrome-relay) | D | KEEP_EXTERNAL_REFERENCE: Chrome extension/relay with existing logged-in session; do not imply ChatGPT connection | HIGH CAUTION live logged-in sessions, 1Password, permissions and unattended actions |
| [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | D/B | KEEP_EXTERNAL_REFERENCE: CLI/plugin context-compression system; conceptual overlap with agent-memory-engineering/handoff | CAUTION external install, hooks and potential retention/exposure of sensitive context |
| [EpicGames/raddebugger](https://github.com/EpicGames/raddebugger) | D | KEEP_EXTERNAL_REFERENCE: native Windows x64 debugger, not agent skill; tool-specific when installed | CAUTION binaries/build and local debug data |
| [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) | B | UPDATE_EXISTING: plain-writing add controlled-language guidance for agent-facing specs and handoffs | APPROVE method only; no certified STE vocabulary implied |
| [cursor/plugins](https://github.com/cursor/plugins) | D/B | KEEP_EXTERNAL_REFERENCE: large plugin catalog; do not mass-import or claim Cursor-native runtime; shortlist by concrete capability later | CAUTION marketplace manifests, hooks, tool permissions and vendor-specific flows |

## Mudança material implementada

`skills/plain-writing/SKILL.md`: adicionado subtipo de linguagem controlada para comunicação entre agentes: agente/ator explícito, uma ação por frase, preconditions/postconditions, modalidade e distinção entre sintaxe imutável e prosa revisável, inspirado em `asd-ste100-skill`. Não declara conformidade ASD-STE100 nem substitui documentação normativa.

## Overlap e limites

- motionmaxxing, robot-heads, anatomy e ManimGX oferecem exemplos expressivos/engines, mas não justificam copiar código ou duplicar `ui-motion-design`, `motion-asset-engineering`, `visual-explanation-sketch`, `interactive-system-diagram` ou a stack de vídeo antes de uma necessidade concreta.
- Talorys, billion-context e agent-chrome-relay são infraestrutura para agentes ou hosts específicos. Seus mecanismos não estão disponíveis automaticamente no ChatGPT; eventuais integrações exigem autenticação, permissões e ferramentas compatíveis.
- Mailcheap e Doory são produtos completos, não skills. RAD Debugger exige runtime local Windows x64 de depuração. Cursor/plugins é catálogo, não endosso coletivo.
- Alegações de performance, suporte, preços, compatibilidade e segurança são afirmações dos projetos, não verificações independentes.
- Nenhuma dependência externa foi instalada ou executada. Análise de segurança preliminar por README, com maior alerta para browser autenticado, credenciais, extensões, scripts de instalação e serviços de email.

## Triggers e near-misses

**Should trigger:** pedir revisão de mensagem de erro, tool contract ou handoff para consumo por agente → `plain-writing` e linguagem controlada. **Near miss:** prosa criativa ou e-mail promocional não ativa estilo STE estrito. **Should trigger futura avaliação:** usuário pedir engine ManimGX ou componente RobotHead em app existente, inspecionar versão, licença, dependências e executar smoke tests no ambiente alvo. **Near miss:** link do produto isolado não constitui autorização para instalá-lo.

## Verificação

Mudança documental publicada na branch principal; execução de código dos repositórios, auditoria profunda, performance, licenças completas, testes visuais e integração funcional **não verificados**. As 11 fontes restantes ficam registradas como referências/candidatas, sem falsa adoção.
