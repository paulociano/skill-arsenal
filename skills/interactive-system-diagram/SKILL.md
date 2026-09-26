---
name: interactive-system-diagram
description: Criar diagramas interativos de arquitetura, workflow, sequência, dataflow ou lifecycle com topologia verificável, artefato HTML explorável e separação explícita entre validação estrutural, verificação no browser e revisão perceptual.
---

# Interactive System Diagram

## Objetivo
Transformar sistemas, fluxos ou estados em um diagrama interativo que seja semanticamente correto, legível e verificável como artefato.

## Tipos
Escolha um tipo principal:
- **architecture**: componentes, serviços, boundaries;
- **workflow**: processo, aprovações, runbooks;
- **sequence**: chamadas, mensagens e retornos;
- **dataflow**: pipelines, lineage e consumidores;
- **lifecycle**: estados, retries e transições.

## Workflow
1. Derive a topologia mínima a partir do pedido ou de evidência do repositório.
2. Preserve nomes, protocolos, APIs e relações relevantes.
3. Defina um main path claro antes de adicionar branches.
4. Limite nós principais ao necessário para leitura.
5. Use labels apenas quando carregarem semântica real.
6. Gere o artefato em um formato editável ou HTML autocontido quando possível.
7. Faça validação estrutural:
   - nós conectados;
   - labels legíveis;
   - relações válidas;
   - sem colisões óbvias;
   - semantic types consistentes.
8. Verifique o HTML em browser real quando houver ferramenta:
   - overflow;
   - legibilidade;
   - interação;
   - tema;
   - pan/zoom;
   - viewport.
9. Separe as claims:
   - validação estrutural;
   - comportamento no browser;
   - qualidade perceptual.
10. Quando o diagrama refletir um repositório real, cite ou registre a evidência de origem.

## Regras de autoria
- Não use decoração para compensar topologia ruim.
- Não remova labels semanticamente importantes só para resolver geometria.
- Não invente relações que o código ou a descrição não sustentam.
- Não trate um screenshot bonito como prova de correção.
- Para input Mermaid, preserve significado e refaça a composição em vez de copiar styling mecanicamente.

## Relação com outras skills
Use `architecture-visualization` para diagramas gerais e `editable-visual-design` quando o objetivo for uma peça gráfica editável. Esta skill entra quando a interação e a validação do artefato são centrais.

## Origem adaptada
Metodologia inspirada em `tt-a1i/archify`, abstraindo schemas, CLI, presets e validadores específicos.
