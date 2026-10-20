---
name: bim-ifc-engineering
description: "Criar, consultar, validar e coordenar modelos BIM/IFC com entidades semânticas, propriedades, relações espaciais, classifications, IDS/BCF, clash/change workflows e exports preservando modelo de informação."
---

# BIM & IFC Engineering

## Objetivo

Tratar edifícios como modelos semânticos e interoperáveis, não apenas geometria 3D.

## Quando usar

- IFC;
- BIM;
- Bonsai/Blender BIM;
- IFC viewer/editor;
- BIM coordination;
- model validation;
- IDS;
- BCF;
- clash/change review.

## Princípio central

**Geometria representa; IFC também descreve o que o elemento é e como se relaciona.**

## Workflow

1. **Schema/version**
   - IFC2x3/IFC4/IFC4x3 explicit;
   - authoring/target tool compatibility.

2. **Spatial structure**
   - project;
   - site;
   - building;
   - storeys;
   - spaces;
   - containment.

3. **Elements**
   - walls/slabs/doors/windows/columns/beams/etc;
   - type vs occurrence;
   - geometry;
   - placement;
   - material;
   - property sets.

4. **Classification/metadata**
   - stable IDs;
   - classifications;
   - quantities;
   - naming conventions;
   - custom properties only when necessary.

5. **Requirements**
   - IDS/other information requirements;
   - required properties;
   - cardinality;
   - allowed values.

6. **Coordination**
   - model federation;
   - clash detection;
   - issue creation;
   - BCF topics/viewpoints;
   - owner/status/resolution.

7. **Change**
   - diff models;
   - additions/deletions/modified properties;
   - provenance/revision;
   - never silently overwrite baseline.

8. **Interop**
   - IFC read/write;
   - geometry conversion only when needed;
   - preserve semantic source of truth;
   - visualization formats are derivatives.

9. **QA**
   - schema validity;
   - spatial containment;
   - required properties;
   - orphan elements;
   - duplicate GUIDs;
   - geometry/placement;
   - export/readback in another compatible viewer when possible.

## Security / actions

IFC editing via MCP/API is an external mutation:
- inspect first;
- scope changes;
- approval before consequential model writes;
- retain original/revision;
- verify changed model after write.

## Regras

- a 3D mesh alone is not BIM;
- valid IFC syntax does not prove model quality;
- IFC version and MVD/exchange requirement matter;
- custom properties should not replace standard semantics without reason;
- BCF issue is coordination record, not geometry mutation.

## Integração

`architectural-design-engineering`, `floor-plan-technical-drawing`, `cad-parametric-modeling`, `building-performance-analysis`, `structural-analysis-modeling`.

## Provenance

Consolidada de IfcOpenShell/Bonsai, BIMserver, web-ifc, xeokit, Speckle, buildingSMART IDS/BCF e COMPAS IFC. Não presume IFC runtime ou MCP instalado.

## pyRevit 7: automação de modelo Revit com agente guardado

Quando o trabalho envolver Autodesk Revit em uma sessão real com pyRevit 7.0 ou mais recente, separar três modos de execução:
- **Consulta**: inspecionar contexto e elementos sem alterar o modelo. Uma query deve ser efetivamente read-only; qualquer tentativa de alteração invalida a execução e deve provocar rollback.
- **Modificação proposta**: executar código Python contra a API Revit em transação guardada, com alvo/documento explícito, diff de elementos afetados e aprovação dentro do Revit. No modo padrão `ask`, o usuário decide Keep ou Discard; o resultado aprovado forma um único item de Undo.
- **Efeito externo**: salvar, exportar, sincronizar, modificar outro documento ou acessar arquivos/serviços fora do contrato exige operação separada e permissão explícita; não tratar essas ações como equivalentes a uma edição local guardada.

### Contrato de execução recomendado
1. Descobrir host, versão do Revit/pyRevit, documento ativo, permissão e ferramentas MCP realmente expostas. Não presumir instalação/conexão do pyRevit nesta conversa.
2. Descrever a mudança pretendida e seus invariantes BIM: elementos, tipos/instâncias, parâmetros, relações, unidades, constraints, worksets e escopo do documento.
3. Preferir inspeção primeiro. Se existir runtime pyRevit, operações típicas disponíveis incluem `get_context`, `inspect_elements`, `lookup_revit_api`, `show_elements`, `capture_view`, `run_query`, `run_modify`, `get_run` e `get_skill`, sujeitos à versão real.
4. Para modificação, executar somente no documento autorizado com transação, timeout, rollback, bloqueio de saves/exports/sync durante execução, verificação de transações abertas e prévia da alteração.
5. Submeter ao gate humano dentro do aplicativo; diferenciar run iniciada, rollback, aprovada e persistida. Um retorno de agente não prova que a modificação foi aceita.
6. Reinspecionar o modelo e verificar parâmetros, geometria, quantidades e elementos alterados. Preservar possibilidade de Undo e registrar versão e evidências, evitando scripts de repetição cega.

### Portabilidade e segurança
O pyRevit 7 trouxe runtime de agente com MCP por stdio e shell IronPython interativo. A habilidade transferível é o padrão **query read-only + mutação transacional + preview/approval nativo + rollback/undo + postcondition**, não a instalação automática de um host Windows/Revit. Não executar Python sugerido por modelos ou obtido em documentos não confiáveis sem revisão de escopo. O controle aplicado pelo host precisa ser verificado na versão implantada; fluxos fora dele não herdam seus bloqueios.

Referência oficial: [pyRevit v7.0.0.26278+2233](https://github.com/pyrevitlabs/pyRevit/releases/tag/v7.0.0.26278%2B2233), publicado em 2026-10-06. Complementa `agent-action-governance` e `verify-before-claim`; não requer instalar pyRevit para tarefas BIM/IFC gerais.
