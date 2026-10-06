---
name: 2d-mesh-avatar-rigging
description: "Transformar uma ilustração 2D em avatar animável por layers, mesh, pivots, face/mouth/eye rig, corrective variants e pose QA antes de uso ao vivo."
---

# 2D Mesh Avatar Rigging

## Objetivo
Converter uma ilustração em asset 2D rigado e deformável, validando coordenadas, layers, mesh e amplitude de movimento antes de considerar o avatar pronto.

## Workflow
1. Source contract: direitos, resolução, fundo, pose e oclusões.
2. Vision calibration: testar precisão em targets conhecidos antes de confiar em coordenadas.
3. Survey: localizar head/face/eyes/mouth/hair/body/acessórios e limites do rig.
4. Zoomed measurement: medir landmarks finos em crops/grids.
5. Draft rig: pivots, polygons/ellipses, strands, influence areas e mesh bounds.
6. Overlay QA: sobrepor rig à arte e corrigir olhos, mouth line, hair e boundaries.
7. Build layers: separar/maskear após o draft passar.
8. Pose suite: rest, blink, mouth, turns, tilts, gaze e sway.
9. Corrective variants: sprites para olhos/fonemas quando necessários, preservando pixels fora da região autorizada.
10. Iterate bounded: corrigir causa dominante, limitar loops e reportar falhas restantes.

## Regra central
Um rig não é validado pela rest pose. QA precisa percorrer o deformation space que será usado.

## Segurança e privacidade
- imagem do usuário permanece no escopo autorizado;
- envio a gerador externo para variants exige autorização;
- não afirmar tracking/live sem runtime disponível.

## Provenance
Adaptada de https://github.com/shinshin86/mesh-avatar-studio, preservando vision calibration, zoomed measurement, overlay checks, fixed-pose review e corrective variants sem exigir seus scripts, editor ou MediaPipe.
