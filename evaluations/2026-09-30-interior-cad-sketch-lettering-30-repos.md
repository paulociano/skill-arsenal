# Avaliação — interiores, CAD, sketch técnico e lettering

Data: 2026-09-30

## Objetivo
Pesquisar repositórios úteis para decoração/interiores, programação 3D de esboços, desenho técnico, vetorização e lettering, procurando capabilities incrementais para o Arsenal.

## Radar de 30 repositórios/projetos
1. FreeCAD/FreeCAD — modelador paramétrico 3D/BIM/CAD.
2. CadQuery/cadquery — CAD paramétrico por Python, B-rep e export STEP/DXF/STL.
3. solvespace/solvespace — sketch paramétrico 2D/3D com constraints.
4. openscad/openscad — 3D compiler por script, CSG e extrusão de outlines.
5. microsoft/maker.js — geometria 2D programável, paths/models/layers/chains e DXF/SVG/PDF.
6. LibreCAD/LibreCAD — CAD 2D e conversão DXF/PDF/PNG/SVG.
7. materializr-cad/materializr — CAD paramétrico experimental.
8. tommasobbianchi/Orca-Cad — CAD/sketch paramétrico experimental.
9. Tibiaworx/HCAD — CAD/sketch candidate.
10. Artis-98/datum — parametric CAD candidate.
11. flowful-ai/cad-skill — workflow agentic CadQuery; metodologia de requisitos→passes→preview→review.
12. charmlinn/blueprint3d-modern — floorplan record, wall/corner graph, 2D planner e Three.js 3D.
13. aalavandhaann/blueprint-js — interior floorplanner 2D/3D e export GLTF.
14. apexerainc/floorplan — WebGL interior design com 2D floorplanner.
15. arturwyroslak/interior3d — grid snapping, dimensioning, wall chaining, assets e transforms.
16. arkegeomatica/archimesh — Blender architectural addon reference.
17. lilacsky824/YingzaoFashi-Blender-Procedural-Model — arquitetura procedural com Geometry Nodes.
18. FreeCAD ecosystem BIM examples — referência de semântica arquitetônica, não runtime adotado.
19. paperjs/paper.js — vector graphics scripting e path manipulation.
20. rambip/sketch-vectorization — hand sketch→SVG, denoise/vectorization.
21. William-Yeh/diagram-to-vector — diagram/vectorization candidate.
22. fskpf/vue-sketch-svg — sketch/SVG candidate.
23. abey79/vpype — pipelines de geometria vetorial, layers, layout e plotter optimization.
24. opentypejs/opentype.js — letterforms como Bézier paths, metrics, kerning e glyph construction.
25. googlefonts/fontmake — UFO/Glyphs/designspace→OTF/TTF/variable fonts.
26. techninja/hersheytextjs — Hershey/single-line text→SVG paths.
27. msurguy/stroke-font-studio — editor de single-stroke glyphs, métricas, snapping, underlay e kerning.
28. martenjacobs/LineFont — Hershey SVG text creator.
29. mew-cx/inkscape_hershey_text — Hershey/stroke lettering reference.
30. philipp-lehmann/hershey-txt-figma-plugin — single-line/Hershey text workflow reference.

## Síntese
### A. CAD paramétrico é uma capability diferente de reconstrução 3D
Modelo técnico precisa separar intent, parameters, constraints, geometry, operations, annotations e outputs. Parametricidade significa propagação coerente de mudança, não simplesmente números em código.

### B. Planta 2D e cena 3D devem compartilhar record
Blueprint3D e Interior3D reforçam wall/corner graph + scene/assets como fonte estrutural. 2D e 3D são views. Isso evita drift entre planta e visualização.

### C. Desenho técnico não é ilustração técnica
Cotas precisam referenciar geometria e unidades reais. Layers, construction geometry, tolerâncias e export formats têm semânticas próprias. Render bonito não prova dimensão correta.

### D. Lettering pode ser engenharia de paths
opentype.js e Stroke Font Studio mostram a separação entre outline, skeleton, metrics, advance width, kerning e contours. Single-stroke tem contrato diferente de outline fonts e é especialmente relevante para plotter/CNC/gravação.

### E. Sketch→vector precisa preservar gesto e simplificar ruído
Vectorização útil não é apenas tracing pixel-a-pixel: denoise, inferência de curves/strokes, simplificação de nós e overlay de comparação são parte do QA.

## Decisões Arsenal
### CREATE_NEW — parametric-cad-drawing
Classe A/B/D. Gap real entre desenho técnico paramétrico e procedural-3d-reconstruction.

### CREATE_NEW — interior-space-prototyping
Classe A/B/D. Owner para planta estrutural única→layout/mobiliário→views 2D/3D.

### CREATE_NEW — lettering-path-engineering
Classe A/B/D. Fecha o gap explicitamente deixado por typographic-composition entre composição e desenho/engenharia de glyphs.

### KEEP_EXTERNAL_REFERENCE
FreeCAD, CadQuery, SolveSpace, OpenSCAD, LibreCAD, Maker.js, Paper.js, vpype, opentype.js, fontmake, Blueprint3D e demais runtimes continuam ferramentas externas. O Arsenal absorve metodologia, não presume instalação.

## Segurança/portabilidade
- nenhum installer/script/binário foi executado;
- nenhuma dependência CAD/Blender/font tool foi instalada;
- nenhuma API key foi usada;
- nenhuma licença de fonte foi ignorada;
- arquivos/renderizações não foram tratados como geometricamente corretos sem validação;
- outputs de arquitetura/interiores não são apresentados como projeto profissional executável sem o escopo/evidência necessários.

## Materialização
- skills/parametric-cad-drawing/SKILL.md
- skills/interior-space-prototyping/SKILL.md
- skills/lettering-path-engineering/SKILL.md
- ARSENAL INDEX.md atualizado.