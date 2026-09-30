---
name: parametric-cad-drawing
description: "Projetar geometria 2D/3D técnica por parâmetros, constraints e operações geométricas, preservando dimensões, unidades, relações e exportabilidade em vez de tratar desenho técnico como ilustração."
---

# Parametric CAD Drawing

## Objetivo
Transformar requisitos dimensionais, esboços ou especificações em um modelo geométrico técnico reproduzível, onde medidas e relações são fonte de verdade e vistas/renders são projeções.

## Quando usar
- desenho técnico 2D;
- peça ou mobiliário paramétrico;
- planta cotada;
- sketch com constraints;
- geometria para DXF/SVG/STEP/STL;
- variações de um mesmo projeto por parâmetros.

Não usar para ilustração livre ou reconstrução visual aproximada.

## Modelo
Separar:
1. intent: função, envelope, interfaces e invariantes;
2. parameters: dimensões, unidades, tolerâncias;
3. constraints: coincidência, paralelo, perpendicular, tangência, simetria, distância, ângulo;
4. geometry: lines, arcs, curves, profiles, solids;
5. operations: transform, boolean, extrusion, loft, fillet etc.;
6. annotations: dimensions, labels, layers;
7. outputs: vistas e formatos derivados.

## Workflow
1. Definir unidade e datum/origin.
2. Registrar dimensões dirigidas e derivadas.
3. Construir primeiro a geometria mínima que satisfaz o intent.
4. Adicionar constraints explícitas antes de detalhes cosméticos.
5. Manter nomes semânticos para parâmetros/features importantes.
6. Separar construction geometry de geometria exportável.
7. Produzir vistas/sections/dimensions a partir do mesmo modelo quando o runtime permitir.
8. Exportar no formato adequado ao próximo sistema.
9. Verificar medidas, topology, interferências e formato exportado; render bonito não prova correção dimensional.

## Desenho técnico
- cotas devem apontar para geometria real;
- não duplicar medidas conflitantes;
- distinguir dimensão nominal, tolerância e clearance;
- preservar escala/unidade no intercâmbio;
- usar layers/classes para separar estrutura, mobiliário, annotation, construction e corte quando aplicável;
- SVG/PDF podem comunicar; DXF/STEP/IFC podem carregar semântica/geometry diferente. Não tratá-los como equivalentes.

## Parametricidade
Um modelo é paramétrico quando mudar um parâmetro relevante atualiza coerentemente as features dependentes. Ter números no código não basta.

Evitar:
- coordenadas mágicas espalhadas;
- duplicação da mesma dimensão;
- constraints redundantes/contraditórias;
- detalhes antes do envelope;
- converter cedo demais para mesh quando B-rep/curves ainda são necessários.

## Ferramentas
CadQuery, OpenSCAD, FreeCAD, SolveSpace, Maker.js e LibreCAD são referências de runtime/tooling. Usá-los somente quando realmente disponíveis. Não presumir instalação.

## Integração
procedural-3d-reconstruction, concept-to-3d-asset, architecture-visualization, verify-before-claim.

## Origem metodológica
Generalizada de CadQuery, FreeCAD, SolveSpace, OpenSCAD, Maker.js e LibreCAD, sem importar seus runtimes.
