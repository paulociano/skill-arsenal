---
name: project-complexity-management
description: "Diagnosticar focos de complexidade técnica, organizacional e externa e definir intervenções proporcionais às evidências."
---

# project-complexity-management

## Objetivo

Diagnosticar hotspots de complexidade de um projeto e transformar o diagnóstico em intervenções proporcionais, sem reduzir tudo a uma nota média ou a um checklist genérico.

## Quando usar

Diagnosticar focos de complexidade técnica, organizacional e externa e definir intervenções proporcionais às evidências.

## Modelo

Complexidade é analisada por:

- Technical;
- Organizational;
- External.

E por dois eixos:

- **detail complexity**: quantidade de partes, interfaces, dependências;
- **dynamic complexity**: incerteza, mudança, atores e previsibilidade.

## Workflow

1. Definir escopo e lifecycle stage.
2. Mapear hotspots, não médias.
3. Para cada hotspot registrar:
   - TOE category;
   - detail/dynamic complexity;
   - severity;
   - evidence;
   - uncertainty.
4. Classificar management fit:
   - simple → keep simple;
   - complicated → control/clarify;
   - complex → connect/learn;
   - mixed → combinar.
5. Converter hotspots em poucas intervenções de alto leverage.
6. Sequenciar por urgência, dependência e fase.
7. Declarar assumptions e decision gates.
8. Definir reassessment triggers, porque complexidade muda.
9. Evitar over-control e over-interaction.
10. Passar execução detalhada para to-tickets/wayfinder quando necessário.

## Regras

- toda ação precisa rastrear a um hotspot;
- não achatar o projeto em uma única score;
- controlar interfaces estáveis antes de ampliar coordenação quando isso reduzir ambiguidade;
- conectar/descobrir antes de controlar quando fatos, objetivos ou atores estiverem instáveis;
- owner sugerido é role, não pessoa inventada;
- não criar Gantt automaticamente;
- hipóteses devem ser marcadas.

## Integração

- wayfinder
- to-spec
- to-tickets
- graph-engineering
- after-action-review

## Referências

Adaptada de maiobarbero/my-ai-workflow, especialmente project-complexity-mapper e project-complexity-action-planner.

Origem local: [project-complexity-management.docx](../project-complexity-management.docx).
