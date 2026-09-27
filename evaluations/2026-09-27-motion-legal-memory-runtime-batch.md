# Avaliação de repositórios externos — lote 2026-09-27-b

## Escopo

Fontes:
- gvzdv/claudish-to-english
- emilkowalski/skills
- elie222/rakazo
- gfodor/legal-skills
- p2r3/ha.mr
- Makio64/threejs-cinematic-world-zoom
- omacom/ttfx
- fellowgeek/mcp-memory
- bikeshaving/termdom
- lajosdeme/mole
- activeing123/mcptoon
- Comfy-Org/ComfyUI
- DietrichGebert/ponytail

Router: ARSENAL INDEX.md.
Stack: arsenal-autopilot.
Gate: revisão estática proporcional via skill-security-review, sem executar código, installers ou binários externos.

## Decisões

### emilkowalski/skills
Classificação: A/B.
Decisão: UPDATE_EXISTING.
Owner: ui-motion-design.

Valor incremental:
- gate explícito para decidir quando não animar;
- frequência de uso como critério;
- propósito obrigatório;
- rejeição explícita de candidatos;
- foco em interrupção e custo temporal.

Adaptação:
- metodologia absorvida sem importar presets numéricos rígidos como verdade universal.

### gfodor/legal-skills
Classificação: A/D.
Decisão: CREATE_NEW.
Owner criado: patent-strategy-review.

Valor incremental:
- pre-filing audit;
- simulated examination com versionamento;
- adversarial design-around;
- separação rigorosa entre disclosure, claim coverage, commercial relevance e patentability.

Adaptação:
- scripts e runtime multiagente da fonte não são presumidos;
- fonte oficial atual deve ser consultada em claims jurídicos materiais.

### DietrichGebert/ponytail
Classificação: A/B.
Decisão: UPDATE_EXISTING.
Owner: surgical-engineering.

Valor incremental:
- delete-list para over-engineering;
- dívida explícita de shortcuts;
- proibição de declarar percentuais de economia sem baseline real.

Benchmarks publicados pelo projeto não foram promovidos a garantia do Arsenal.

### elie222/rakazo
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- arquitetura de agentes persistentes;
- separação frontend/backend para orchestration, authorization, retries e recovery;
- self-hosting e runtimes de computer use.

Overlap:
- loop-engineering, graph-engineering, multi-agent-orchestration e system-design-engineering já possuem ownership conceitual.

### fellowgeek/mcp-memory
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- namespaces;
- checkpoints;
- provenance/sources em objetos de memória;
- estrutura de knowledge objects.

Motivo:
- implementação é servidor MCP/storage;
- Memory do ChatGPT é capability própria e não deve ser simulada;
- conceitos já se conectam a session-learn, handoff e golden-path-capture.

### activeing123/mcptoon
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- medição de custo/token de MCPs e skills;
- benchmark com denominadores explícitos.

Overlap:
- codex-cost-efficiency e llm-observability-evaluation já são owners do método.
- claims de savings do projeto não foram importados como universais.

### lajosdeme/mole
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- research runtime com budgeting, status e structured extraction.

Overlap:
- research-and-synthesize, web-extraction-pipeline, evidence-claim-verification e loop-engineering.

### Comfy-Org/ComfyUI
Classificação: D.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- node-graph workflow de geração multimodal;
- ecossistema de custom nodes.

Risco/portabilidade:
- custom nodes são código Python arbitrário;
- modelos, CUDA/PyTorch e assets são dependências reais;
- não tratar ComfyUI ou seus nodes como disponíveis sem runtime.

Owner conceitual futuro, quando conectado: high-fidelity-image-generation / image-to-3d / graph-engineering.

### Makio64/threejs-cinematic-world-zoom
Classificação: D/B.
Decisão: ABSORB_METHOD_ONLY, sem nova skill.

Valor:
- camera flight cinematográfico;
- Three.js + photorealistic 3D tiles;
- gravação de flight.

Overlap:
- scroll-storytelling, creative-web-effects, shader-graphics-engineering e procedural-film já cobrem a maioria dos princípios.
- referência útil para cenas geoespaciais/3D específicas.

### bikeshaving/termdom
Classificação: D.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- DOM/CSS-like model em terminal;
- renderer TUI e testes de TTY/static output.

Não altera metodologia geral do ChatGPT.

### omacom/ttfx
Classificação: D.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- terminal text effects;
- forte disciplina de parity tests e benchmark.

Overlap:
- behavior-contract-validation e performance engineering.
- produto específico, sem owner novo.

### p2r3/ha.mr
Classificação: D.
Decisão: REJECT como skill; referência técnica opcional.

É compressor estático de URLs/otimizador de QR. Capability estreita e de produto.

### gvzdv/claudish-to-english
Classificação: D/C.
Decisão: REJECT como skill.

Produto/plugin de reescrita display-only para Claude Code com estilo/linguagem configuráveis.
Overlap total com plain-writing, locale-adapter e preferências de estilo do próprio ChatGPT.

### ComfyUI security note
Custom nodes devem ser tratados como software arbitrário de terceiros e passar revisão separada antes de uso em ambientes sensíveis.

## Mudanças publicadas

1. Atualizada skills/ui-motion-design/SKILL.md com gate de necessidade/frequência.
2. Criada skills/patent-strategy-review/SKILL.md.
3. Atualizada skills/surgical-engineering/SKILL.md com delete-list e ledger de shortcuts.
4. Atualizado ARSENAL INDEX.md com patent-strategy-review.

## Segurança

Nenhum installer, setup script, model weight, custom node, MCP server ou binário externo foi executado.
Nenhum runtime externo foi tratado como capability nativa do ChatGPT.
