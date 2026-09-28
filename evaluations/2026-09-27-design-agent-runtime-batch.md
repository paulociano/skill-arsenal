# Avaliação de repositórios externos — lote 2026-09-27-d

## Escopo

Fontes:
- qybaihe/mu
- kishormorol/cli-faq-shortcuts
- alexgreensh/anidoodle
- kaolti/phantomat
- Rieranthony/product-film-skill
- fzakaria/omnibin
- byalex33/changelog.earth
- bjarneo/flux
- Badtheorylabs/interference-search
- bridge-mind/bridgeclip
- reco-tools/ritridata
- Owl-Listener/designer-skills
- emilkowalski/skills
- ConardLi/garden-skills
- elayadesign/ai-design-skills
- MengTo/Skills
- jakubkrehel/skills
- codeswithroh/tastemaker

Router: ARSENAL INDEX.md.
Stack: arsenal-autopilot.
Gate: revisão estática proporcional via skill-security-review; nenhum installer, script, binário, modelo, package manager ou runtime externo foi executado.

## Decisões

### qybaihe/mu
Classificação: A/D.
Decisão: UPDATE_EXISTING.
Owner: loop-engineering.
Valor incremental:
- decision points bounded ao longo do ciclo agentic;
- modos active/shadow/off;
- ledger por decisão;
- regras determinísticas como piso de segurança;
- separação entre judge semântico e approval humano.
Adaptação:
- absorvido o contrato metodológico;
- não importados judges, desktop app, pi runtime, permissões ou claims de performance.

### kishormorol/cli-faq-shortcuts
Classificação: A/B/D.
Decisão: UPDATE_EXISTING.
Owner: project-skill-architecture.
Valor incremental:
- descobrir workflows recorrentes pelo histórico real;
- cluster por intenção/outcome;
- usar erros/correções anteriores como sinal de valor;
- ligar atalho ao tooling existente;
- separar report/dry-run de ações com efeitos.
Adaptação:
- não ler diretórios privados de Claude/Codex/Cursor por padrão;
- coleta depende de fonte autorizada e realmente disponível.

### alexgreensh/anidoodle
Classificação: A/D.
Decisão: UPDATE_EXISTING / KEEP_EXTERNAL_REFERENCE.
Owner: procedural-film.
Valor:
- pure-frame deterministic contract;
- craft bar explícito;
- provar look em um still antes de escalar;
- coerência entre still, timelapse e filme.
Motivo:
- engine, estilos, Node/browser/FFmpeg e tooling são runtime externo.

### Rieranthony/product-film-skill
Classificação: A/D.
Decisão: UPDATE_EXISTING.
Owner: procedural-film.
Valor incremental:
- design system do produto como autoridade visual;
- brand kit/film kit persistente;
- claims reais antes de roteiro;
- reutilização de componentes reais ou twins frame-driven;
- verificação do deliverable final por decode quando suportado.
Adaptação:
- não exigir Remotion, Bun, uv ou scripts da fonte.

### codeswithroh/tastemaker
Classificação: A/D.
Decisão: UPDATE_EXISTING.
Owner: design-direction.
Valor incremental:
- referência visual aterrada em pixels para propriedades objetivas;
- separação entre project style lock e preferência cross-project;
- precedence explícita de memória de gosto;
- registrar keep/reject sem promover pending como preferência.
Adaptação:
- scripts, diretórios locais, perfis e MCPs externos não são presumidos;
- checks de contraste provam legibilidade, não “bom gosto”.

### elayadesign/ai-design-skills
Classificação: B/C.
Decisão: ABSORB_METHOD_ONLY.
Owner: web-design-engineer.
Valor:
- uma oferta/audiência/ação primária;
- message match;
- prova próxima ao claim;
- objeções como parte da arquitetura da página.
Rejeitado como default:
- listas universais de fontes proibidas;
- spacing/radius fixos;
- proibição universal de gradientes;
- presets de layout sem contexto.

### emilkowalski/skills
Classificação: A/B.
Decisão: KEEP_AS_EXISTING_PROVENANCE.
Owners existentes: ui-motion-design, interaction-polish e web-design-engineer.
Observação:
- o Arsenal já havia incorporado gate de necessidade/frequência e motion com propósito a partir desta fonte;
- nenhum owner novo necessário neste lote.

### ConardLi/garden-skills
Classificação: A/B/D.
Decisão: KEEP_EXTERNAL_REFERENCE.
Overlap forte:
- web-video-presentation;
- web-design-engineer;
- high-fidelity-image-generation;
- beautiful-web-article.
Valor adicional não justificou duplicação de owners.

### MengTo/Skills
Classificação: A/B/D.
Decisão: KEEP_EXTERNAL_REFERENCE.
Overlap forte:
- ui-motion-design;
- web-design-engineer;
- 3D/media/game owners já existentes.
Observação:
- já aparece na provenance de ui-motion-design e skill-builder.

### jakubkrehel/skills
Classificação: B.
Decisão: KEEP_EXTERNAL_REFERENCE.
Overlap:
- accessibility, color, layout, typography, interface review e variants já possuem owners canônicos no Arsenal.

### Owl-Listener/designer-skills
Classificação: A/B/D.
Decisão: KEEP_EXTERNAL_REFERENCE.
Valor:
- catálogo amplo e roteamento por situação.
Motivo:
- capability coverage amplamente existente no Arsenal;
- importar 273 skills aumentaria duplicação e custo de roteamento sem ganho proporcional.

### bridge-mind/bridgeclip
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.
Valor:
- pipeline source → transcript → moment selection → render;
- model capability gates;
- queue/status/retry;
- privacy boundary explícita.
Overlap:
- video-editing-pipeline, model-routing-gateway, social workflows.

### reco-tools/ritridata
Classificação: D.
Decisão: KEEP_EXTERNAL_REFERENCE.
Valor:
- read-only disk image inspection;
- strict scope boundaries;
- synthetic fixtures.
Produto técnico específico; não muda metodologia geral do Arsenal.

### kaolti/phantomat
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.
Valor:
- spatial window management e infinite canvas.
Sem capability nova relevante para o Arsenal atual.

### fzakaria/omnibin
Classificação: D.
Decisão: KEEP_EXTERNAL_REFERENCE.
Runtime/infra técnica específica. Sem owner metodológico novo demonstrável.

### byalex33/changelog.earth
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.
Produto/aplicação específica; sem ganho metodológico suficiente para owner novo.

### bjarneo/flux
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.
Produto/runtime específico; overlap com workflows técnicos existentes.

### Badtheorylabs/interference-search
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.
Pesquisa/modelo técnico com weights/experiments. Qualquer adoção exigiria avaliação empírica e serving real.

## Mudanças publicadas

1. Atualizada `skills/loop-engineering/SKILL.md` com judgment points bounded, shadow mode e ledger.
2. Atualizada `skills/project-skill-architecture/SKILL.md` com mineração de workflows recorrentes por histórico.
3. Atualizada `skills/procedural-film/SKILL.md` com product-film mode e reforço de determinismo/craft.
4. Atualizada `skills/design-direction/SKILL.md` com reference grounding e taste memory em camadas.
5. Atualizada `skills/web-design-engineer/SKILL.md` para distinguir metodologia útil de dogma/presets rígidos.

## Segurança e portabilidade

- nenhum código externo foi executado;
- nenhuma dependência foi instalada;
- nenhum runtime de judge, Remotion, FFmpeg, Hyprland plugin, modelo ou MCP foi tratado como capability nativa;
- diretórios de histórico local, perfis de gosto e credenciais mencionados pelas fontes não foram acessados;
- claims de benchmark/performance permaneceram claims das fontes;
- catálogos grandes foram tratados como radar, não importados em massa.

## Limites

- triagem ampla foi baseada em README/root e arquivos centrais;
- aprofundamento foi feito somente onde havia novidade plausível;
- projetos técnicos específicos precisariam de auditoria própria antes de implantação;
- esta avaliação não é um parecer de segurança integral dos runtimes externos.
