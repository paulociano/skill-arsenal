# Creative AI open-source radar — imagem, vídeo, áudio, 3D, apresentações e UI

Data: 2026-09-30

## Objetivo

Continuar a pesquisa de ferramentas inovadoras/open-source, priorizando creative AI, workstations locais, alternativas a SaaS pagos e metodologias que acrescentem valor incremental ao Skill Arsenal.

Fluxo: `arsenal-autopilot`.

Nenhum installer, modelo, checkpoint, Docker image, CLI, plugin, MCP, API key ou runtime externo foi executado.

## Radar pesquisado

### Imagem e creative workstations
1. `Comfy-Org/ComfyUI` / ecossistema oficial — pipelines visuais por graph/nodes, execução parcial e composição modular.
2. `invoke-ai/InvokeAI` — creative engine para geração/refino/workflows.
3. `Acly/krita-ai-diffusion` — AI integrada ao fluxo de pintura: seleção, inpaint/outpaint, referências, sketch, line art, depth e controles localizados.
4. `ace-step/ACE-Step` — geração musical open-source com text/audio conditioning e integração de workflow.
5. `Stability-AI/stable-audio-tools` — toolkit técnico para modelos de geração de áudio condicional.
6. `SWivid/F5-TTS` — TTS/voice generation research/runtime; código MIT, modelos com licença distinta.
7. `fishaudio/fish-speech` — TTS/voice generation; licença de pesquisa atual exige verificação específica.

### 3D
8. `microsoft/TRELLIS`
9. `microsoft/TRELLIS.2`
10. `Tencent-Hunyuan/Hunyuan3D-1`
11. ecossistema Hunyuan3D posterior encontrado na pesquisa.
Esses projetos reforçam reconstrução neural image-to-3D já roteada por `image-to-3d`; não criam novo owner.

### AI video / filmmaking
12. `LudwigKienle/ai-video-production-editor` — script→director→storyboard→filming→review→edit→color→deliver; model routing por shot; continuity/re-film queue.
13. `headline-design/seq` — storyboard + multi-model video + first/last-frame bridging + NLE timeline.
14. `openslop/openslop` — scene-card workflow para script, narration, character, image, animation, clip, sound e music.
15. `dseditor/AI-storyboard-generator` — storyboard cuts, image regeneration e video transitions.

### Web/UI/design-to-code
16. `onlook-dev/onlook` — visual-first editor sobre codebase, DOM editing, components, tokens, branching/checkpoints.
17. `buildingopen/openpage` — JSON-first website model compartilhado entre humano, visual editor e agente; diffable/versionable.
18. `SandeepBaskaran/design-mode` — browser visual surface que comunica mudanças ao coding agent.
19. `heldernoid/openstitch` — text/screenshot/sketch→interactive frontend em infinite canvas.
20. `Kalmuraee/OpenMagic` — selecionar elemento→descrever mudança→review diff→editar source→type/lint/runtime verification.
21. `winchxyz/loupe` — AI + live design canvas + apontar elemento + verificação contra render.
22. `NowSquare/VoxelSite` — site graph, impact/blast-radius, visual editing, snapshots e transactional review/apply.
23. `OpsinTech/PowerPM` — AI-native vector/design-as-code direction encontrada no radar.

### Presentations
24. `erickittelson/slidemason` — apresentações locais com brief JSON, TSX/CSS, primitives, live preview e export.
25. `Mgregchi/inpresenton` / Presenton ecosystem — geração/editing/export de apresentações self-hosted, múltiplos providers, PPTX editável.
26. forks/variants de Presenton foram descartados como duplicatas de discovery.

### Outros candidatos de creative tooling
27. ComfyUI forks/wrappers — discovery only; fonte canônica deve prevalecer.
28. Krita AI workflow packs — discovery only; owner metodológico é o projeto principal.
29. TRELLIS wrappers/Comfy nodes — discovery only; modelos oficiais prevalecem.
30. F5/Fish/voice wrappers — discovery only; upstream/licença prevalecem.

## Achados incrementais

### A. Controle espacial vence prompt monolítico

`Acly/krita-ai-diffusion` mostra um padrão altamente portátil:
`evidência visual + região/máscara + mudança localizada + invariantes`.

Isso reduz drift em edição criativa e foi absorvido em `high-fidelity-image-generation`.

Não presumir que image tool expõe depth, pose, line art, ControlNet ou strength. Usar somente controles reais.

### B. Creative graph como pipeline explícito

ComfyUI/InvokeAI reforçam:
- stages explícitos;
- nós com entradas/saídas;
- execução parcial;
- reuso de subfluxos;
- inspeção intermediária.

A metodologia já pertence a `graph-engineering` e aos workflows visuais existentes. Não foi criado runtime/skill ComfyUI.

### C. Shot ledger em vídeo generativo

Os melhores film workstations não usam um único prompt para um filme inteiro. Eles tratam cada shot como unidade de produção.

Contrato portátil:
`narrative function → camera → subject/location → references → motion → backend → status → review → targeted rework`.

Continuity review ocorre entre shots. Falha em um shot não obriga regenerar o filme inteiro.

Absorvido em `video-editing-pipeline`.

### D. Visual editing deve convergir para código/modelo canônico

Onlook/OpenMagic/Design Mode/Loupe/OpenPage convergem em:
`select real element → express intent → map to canonical source → small diff → review → apply → validate → inspect render`.

OpenPage acrescenta uma ideia forte: humano e agente editam a mesma representação estruturada/diffable em vez de manter dois mundos paralelos.

Absorvido em `web-design-engineer`.

### E. Presentation-as-code/local-first

Slidemason e Presenton mostram alternativas abertas a Gamma/Beautiful.ai/Tome:
- local/self-hosted;
- structured brief;
- templates/themes;
- live preview;
- export PDF/PPTX;
- provider choice.

O Arsenal já tem `research-to-presentation`, `cinematic-presentation`, skills nativas de slides e artifact tooling. Manter como referências externas.

### F. Áudio generativo

ACE-Step, stable-audio-tools, F5-TTS e Fish Speech são tecnicamente fortes, mas dependem de modelos, GPU/runtime e licenças específicas.

Não criar uma skill genérica de voice cloning. Para qualquer trabalho de voz:
- consentimento/uso autorizado importa;
- licença do código e do modelo são separadas;
- identidade vocal não deve ser inferida como livre para clonagem;
- não fingir que os modelos estão disponíveis no ChatGPT.

### G. 3D

TRELLIS/TRELLIS.2/Hunyuan3D confirmam o valor do owner atual `image-to-3d`:
- input quality;
- single vs multi-view;
- hidden geometry remains inferred;
- export/material/topology vary by backend;
- hardware and model availability are decisive.

Nenhuma nova skill.

## Mudanças canônicas publicadas

### `high-fidelity-image-generation`
Adicionado controle espacial/localizado:
- máscara/seleção;
- referência;
- invariantes fora da região;
- guides somente quando suportados pela ferramenta real.

### `video-editing-pipeline`
Adicionado shot ledger:
- função narrativa;
- duração;
- câmera;
- subjects/location;
- references;
- motion;
- backend;
- lifecycle status;
- targeted rework;
- continuity review.

### `web-design-engineer`
Adicionado loop visual sobre código real:
- element ownership;
- design intent;
- small reviewable diff;
- lint/type/build;
- runtime render verification;
- checkpoint/rollback quando disponível;
- visual editor não vira segunda source of truth.

## Classificação resumida

- Krita AI Diffusion — **A/B/D → UPDATE_EXISTING**
- ComfyUI — **A/B/D → ALREADY_COVERED / EXTERNAL RUNTIME**
- InvokeAI — **B/D → EXTERNAL REFERENCE**
- AI Video Production Editor — **A/B/D → UPDATE_EXISTING**
- Seq — **A/B/D → UPDATE_EXISTING**
- OpenSlop — **B/D → UPDATE_EXISTING / REFERENCE**
- Onlook — **A/B/D → UPDATE_EXISTING**
- OpenPage — **A/B/D → UPDATE_EXISTING**
- OpenMagic — **A/B/D → UPDATE_EXISTING**
- Design Mode / Loupe / OpenStitch — **B/D → EXTERNAL REFERENCE + methodological support**
- Slidemason — **B/D → EXTERNAL REFERENCE**
- Presenton — **B/D → EXTERNAL REFERENCE**
- ACE-Step — **D/B → EXTERNAL REFERENCE**
- stable-audio-tools — **D → EXTERNAL REFERENCE**
- F5-TTS — **D/B → EXTERNAL REFERENCE**
- Fish Speech — **D/B → EXTERNAL REFERENCE, license-sensitive**
- TRELLIS family / Hunyuan3D — **A/D → ALREADY OWNED BY image-to-3d**

## Segurança e portabilidade

- Nenhum setup/install foi executado.
- Nenhuma chave/API/provider foi conectado.
- Nenhum modelo/checkpoint foi baixado.
- Nenhuma voz foi clonada.
- Nenhuma imagem/vídeo foi enviada a serviço externo.
- Claims de qualidade/benchmark das fontes não foram reproduzidos.
- Código e model weights podem ter licenças diferentes.
- "local" e "self-hosted" não provam privacidade sem inspeção de telemetria/dependências.
- wrappers/forks não substituem upstream canônico.

## Conclusão

O lote reforça um padrão transversal para creative AI:

`brief → estrutura intermediária controlável → geração localizada → inspeção → targeted rework → artifact canônico`.

O ganho está menos em adicionar mais geradores e mais em evitar o modelo `prompt gigante → resultado opaco`.
