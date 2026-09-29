# Avaliação em lote — procedural audio, WebGL studies, design systems, hardware status e Flutter morphs

Data: 2026-09-29

## Escopo

Fontes:
- https://github.com/m1ckc3s/procedural-sounds
- https://github.com/DenisSergeevitch/desktop-fly
- https://github.com/niclasvestlund-YT/vibepulse
- https://github.com/Yousuf-developer/Viscose-carousel
- https://github.com/MengTo/sylva
- https://github.com/CoreBunch/Core-Framework
- https://github.com/KickNext/morphnext

Fluxo aplicado: `arsenal-autopilot` com comparação por capability e revisão de segurança/portabilidade proporcional.

Nenhum installer, build script, firmware, browser runtime, código externo ou hardware das fontes foi executado.

## Resumo executivo

- `m1ckc3s/procedural-sounds`: **A/B/D** — metodologia forte para áudio procedural de interface; runtime Web Audio e app são técnicos. **UPDATE_EXISTING** em `creative-web-effects`.
- `Yousuf-developer/Viscose-carousel`: **B/D** — estudo WebGL/SDF com boas decisões de data/layout/atlas. **UPDATE_EXISTING** em `shader-graphics-engineering`.
- `MengTo/sylva`: **B/D** — estudo Three.js/procedural scene com seed determinística, isolamento e reduced-motion. **UPDATE_EXISTING** em `shader-graphics-engineering`.
- `CoreBunch/Core-Framework`: **A/B/D** — ferramenta técnica de design tokens com metodologia útil de sistema visual portátil. **UPDATE_EXISTING** em `design-system-governance`.
- `KickNext/morphnext`: **B/D** — biblioteca Flutter de morphs interruptíveis. **UPDATE_EXISTING** em `ui-motion-design`.
- `niclasvestlund-YT/vibepulse`: **B/D** — hardware/runtime para status de coding agents com disciplina forte de claims por evidência. **KEEP_EXTERNAL_REFERENCE**; `verify-before-claim` já cobre o comportamento relevante.
- `DenisSergeevitch/desktop-fly`: **D/B** — aplicação técnica neuro-simulation + desktop overlay; metodologia científica/provenance interessante, mas sem capability nova roteável. **KEEP_EXTERNAL_REFERENCE**.

## Avaliações

### m1ckc3s/procedural-sounds

**Classificação:** A/B/D.

**O que faz:** sintetiza interface sounds no browser a partir de recipes, com múltiplos generators, biblioteca curada, human verdicts, ear-safety clamps e export de WAV/JS.

**Valor incremental:** forte no princípio de separar `Patch`/recipe, player e curation/training. Também é valiosa a distinção entre geradores independentes e um downstream comum de segurança/loudness/perceptual distance.

**Segurança:** CAUTION baixo para metodologia. A implementação depende de Web Audio, filesystem local no modo dev e Node/Next. Não importar runtime.

**Decisão:** absorver procedural audio em `creative-web-effects`, incluindo limites de loudness/frequência e human taste como sinal, não verdade universal.

### DenisSergeevitch/desktop-fly

**Classificação:** D/B.

**O que faz:** overlay desktop com corpo procedural e circuitos neurais simulados usando dados FlyWire/MaleCNS, com checks de locomotion e separação explícita entre measured anatomy e modeled physiology.

**Valor incremental:** bons exemplos de provenance, distinction measured-vs-modeled e reproducible extraction, mas esses princípios já pertencem a `evidence-claim-verification`, `verify-before-claim` e pesquisa técnica.

**Segurança:** CAUTION. Build nativo, Electron/Three.js, datasets científicos e runtime gráfico. Não executar/importar.

**Decisão:** manter como referência externa.

### niclasvestlund-YT/vibepulse

**Classificação:** B/D.

**O que faz:** painel ESP32 para quotas/status de Claude Code/Codex, incluindo interação opcional, relays e simulator.

**Valor incremental:** excelente disciplina de claim freshness: a fonte distingue release tag, CI/build, simulator e physical verification, e evita promover evidência antiga para hardware novo.

**Segurança:** CAUTION alto. Firmware, Wi-Fi, USB flash, relays, tokens, Chrome extension e hardware físico.

**Decisão:** manter como referência externa. A metodologia central já está coberta por `verify-before-claim`, especialmente stale evidence e escopo da afirmação.

### Yousuf-developer/Viscose-carousel

**Classificação:** B/D.

**O que faz:** carousel WebGL renderizado como um único fragment shader/SDF, com atlas, metadata e interação sincronizados.

**Valor incremental:** forte na ideia de uma única fonte de dados controlar ordem no ring, atlas packing, numbering e metadata; também mostra quando single-pass shader reduz divergência visual.

**Segurança:** APPROVE para metodologia, CAUTION de assets/licença. O README alerta que uma fonte comercial e imagens de terceiros não fazem parte da licença MIT do código.

**Decisão:** absorver em `shader-graphics-engineering`, sem copiar assets/fontes.

### MengTo/sylva

**Classificação:** B/D.

**O que faz:** estudo Three.js com root/moss procedural, seed determinística, pointer response, instancing, isolated WebGL controls e reduced-motion.

**Valor incremental:** seed para reproducibility e isolamento de contextos WebGL são bons padrões. O fallback preserva layout/conteúdo quando a cena principal não inicia.

**Segurança:** CAUTION de licença. O repositório declara que não concede licença para reutilização do código/design/artwork, embora componentes terceiros mantenham suas próprias licenças.

**Decisão:** absorver apenas metodologia em `shader-graphics-engineering`; não copiar código/arte.

### CoreBunch/Core-Framework

**Classificação:** A/B/D.

**O que faz:** editor visual de design tokens e framework CSS para web, WordPress e Figma, com escalas fluidas, selectors, components, utilities e projeto portátil.

**Valor incremental:** bom padrão de design model como fonte única, editor visual como interface e CSS gerado como output; export/import portátil e escalas derivadas de poucas restrições reduzem drift.

**Segurança:** APPROVE para metodologia. O runtime usa Bun/WordPress/Figma integrations e não é necessário no Arsenal.

**Decisão:** atualizar `design-system-governance` com portabilidade, escalas fluidas e coerência entre tokens, components e CSS produzido.

### KickNext/morphnext

**Classificação:** B/D.

**O que faz:** morph vectorial entre Flutter `IconData`, interruptível e dirigido por spring, com fallback para ícones comuns quando a fonte não pode ser resolvida.

**Valor incremental:** dois princípios portáveis: transições interruptíveis devem continuar da forma atualmente renderizada, e falha do asset/morph deve preservar função/layout.

**Segurança:** APPROVE para metodologia. É package Flutter com caches e parsing de fonts; não importar a implementação.

**Decisão:** atualizar `ui-motion-design`.

## Mudanças aplicadas

- `creative-web-effects`: procedural interface audio, separação recipe/player/curation e safety rails de áudio.
- `ui-motion-design`: continuidade de morph interruptível e fallback funcional.
- `design-system-governance`: editor visual sobre design model, export/import portátil, escalas fluidas e contrato do CSS gerado.
- `shader-graphics-engineering`: single-pass/SDF carousel, single source de ordem/atlas/metadata, seed determinística e isolamento de contextos WebGL.
- este registro em `evaluations/`.

## Decisões de não-criação

Nenhuma nova skill foi criada:
- procedural audio cabe como família de `creative-web-effects`;
- Viscose/Sylva são implementações de `shader-graphics-engineering`;
- morphnext é repertório/metodologia de `ui-motion-design`;
- Core Framework fortalece `design-system-governance`;
- VibePulse e DesktopFly são runtimes especializados, não owners genéricos.

## Limites

- Nenhum benchmark, firmware, browser demo, hardware ou build foi reproduzido.
- A revisão foi estática e focada nas capabilities importadas.
- Assets, fontes e código com licença específica não foram copiados.
- Claims de hardware das fontes foram tratados como claims dos autores, não revalidados pelo Arsenal.
