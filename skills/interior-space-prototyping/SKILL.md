---
name: interior-space-prototyping
description: "Prototipar interiores a partir de uma planta estrutural única, conectando paredes, aberturas, dimensões, mobiliário, circulação e projeções 2D/3D sem confundir visualização decorativa com precisão arquitetônica."
---

# Interior Space Prototyping

## Objetivo
Transformar requisitos de um ambiente em um protótipo espacial editável no qual planta, paredes, aberturas, mobiliário e visualização 3D derivam do mesmo modelo.

## Quando usar
- decoração/interiores com layout espacial;
- planta baixa interativa;
- testar mobiliário e circulação;
- converter planta 2D em preview 3D;
- room planner;
- explorar alternativas de layout antes de render final.

Não usar como substituto automático de projeto arquitetônico/estrutural/instalações assinado por profissional.

## Record espacial
Preservar como dados:
- corners/vertices;
- walls/segments;
- rooms/zones;
- openings;
- levels/heights;
- furniture/assets;
- transforms;
- dimensions/units;
- materials/finishes;
- constraints/clearances quando conhecidos.

2D e 3D devem ser views do mesmo record sempre que possível.

## Workflow
1. Confirmar envelope, unidade, pé-direito e aberturas conhecidas.
2. Construir wall/corner graph e fechar rooms.
3. Validar dimensões antes de decorar.
4. Inserir portas/janelas e elementos fixos.
5. Definir zonas funcionais e caminhos de circulação.
6. Posicionar mobiliário por footprint real quando houver medidas.
7. Testar alternativas por mudanças pequenas e comparáveis.
8. Aplicar materiais/iluminação somente depois do layout estrutural.
9. Produzir 2D cotado + 3D/axonometric/perspective conforme necessidade.
10. Declarar dimensões assumidas e verificar collisions/clearances observáveis.

## Regras
- render fotorealista não corrige planta errada;
- imagem de referência pode orientar estilo, não medidas ausentes;
- asset 3D precisa carregar footprint/escala coerente;
- snapping ajuda edição, mas não substitui constraint/dimension;
- não inventar paredes, instalações ou medidas ocultas;
- diferenciar decoração conceitual de desenho técnico executável.

## Interação
Quando implementado em editor:
- grid/snapping;
- wall chaining;
- dimensions em tempo real;
- undo/redo;
- 2D↔3D sincronizado;
- transform controls;
- lock de elementos;
- save/load serializado;
- layers/categories;
- seleção e inspeção do objeto.

## Integração
parametric-cad-drawing, design-direction, high-fidelity-image-generation, procedural-3d-reconstruction, editable-visual-design, verify-before-claim.

## Origem metodológica
Generalizada de Blueprint3D/blueprint-js, Interior3D e práticas de CAD/BIM observadas em FreeCAD e ferramentas paramétricas, sem depender desses runtimes.
