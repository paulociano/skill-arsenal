---
name: architecture-visualization
description: "Criar diagramas de arquitetura, sequência, estados e fluxos a partir de descrições ou código com topologia rastreável."
---

# architecture-visualization

## Objetivo

Transformar uma descrição de sistema ou evidência de repositório em um diagrama técnico confiável, legível e verificável, separando fatos de topologia, apresentação visual, comportamento interativo e claims de impacto.

## Quando usar

- arquitetura de sistemas e serviços;
- workflows/runbooks/CI-CD;
- sequence diagrams e request lifecycles;
- dataflow, ETL/ELT e lineage;
- state/lifecycle maps;
- visualização de relações reais em um repositório;
- conversão de Mermaid para um artefato mais explicativo, sem tratar o estilo Mermaid como autoridade.

## Tipos

1. **Architecture** — componentes, serviços, boundaries e infraestrutura.
2. **Workflow** — processo, gates, tool calls e runbooks.
3. **Sequence** — participantes, requests, returns e async traces.
4. **Dataflow** — produtores, transformações, stores e consumidores.
5. **Lifecycle** — estados, eventos, retries e terminais.

## Princípios

1. **Truth before spectacle.** Relações e labels precisam vir da descrição do usuário ou de evidência verificável.
2. **One spatial narrative first.** A rota principal deve ser compreensível antes de branches secundários.
3. **Progressive disclosure.** Detalhes, metadados e evidência entram sob foco, não como chrome permanente.
4. **Semantic labels are data.** Protocolo, direção, sync/async e ações não devem ser apagados só para facilitar layout.
5. **Static meaning first.** Motion é opcional, finito e não pode carregar significado ausente do frame estático.
6. **Canonical artifact vs viewer state.** Zoom, foco, highlights e animação exploratória não alteram a verdade canônica do diagrama.
7. **Reachability is not impact.** Um caminho no grafo não prova blast radius, causalidade ou breakage sem evidência adicional.

## Workflow

1. **Ground source** — decidir se a autoridade é briefing, spec, código ou outra fonte.
2. **Choose diagram type** — arquitetura, workflow, sequence, dataflow ou lifecycle.
3. **Extract facts first** — nodes, edges, labels, boundaries, states e evidence locators.
4. **Define typed spec** — IDs estáveis, categorias, relações e campos relevantes.
5. **Author primary path** — construir a história principal antes de adicionar branches.
6. **Validate semantics** — IDs, endpoints, labels, states, cardinalidade e evidence links.
7. **Validate composition** — overlap, crossings, ambiguous corridors, clipped labels e excesso de densidade.
8. **Render** — produzir artefato no formato realmente disponível.
9. **Runtime check** — quando houver HTML/interação, verificar comportamento e viewport reais.
10. **Perceptual review** — revisar legibilidade, hierarquia, densidade e equilíbrio visual.
11. **Freeze after acceptance** — não editar após a última validação sem invalidar o receipt.
12. **Handoff** — reportar separadamente validação estrutural, runtime evidence e revisão visual.

## Evidence discipline

Quando o diagrama deriva de código:

- cada claim importante deve apontar para arquivo/símbolo/linha ou outra evidência adequada;
- diferenciar relação explicitamente encontrada de interpretação;
- se a evidência não sustentar direção, protocolo ou ownership, marcar como unknown em vez de inventar;
- viewer highlights nunca contam como nova evidência.

## Layout discipline

- remover edges de baixo valor antes de criar rotas manuais complexas;
- corrigir uma falha geométrica por vez;
- preservar labels semanticamente importantes;
- evitar crossings em nodes opacos e corridors ambíguos;
- não corrigir overflow escondendo conteúdo ou diminuindo texto até ficar ilegível;
- conteúdo visual deve continuar compreensível sem animação.

## Visual semantics

- cor saturada deve ter significado, não ser decoração gratuita;
- estado não deve depender somente de cor;
- keyboard/focus/reduced-motion importam em artefatos interativos;
- temas diferentes devem preservar identidade semântica das categorias.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Para páginas web, usar o navegador controlável disponível e sua API documentada; separar inspeção de DOM, evidência visual e estado de aplicação. Controle de navegador não implica controle de aplicativos nativos ou dispositivos móveis. Produzir Mermaid, SVG ou HTML conforme o pedido; não exigir archify.mjs. Separar validação estrutural, visual e interativa.

## Referências

Adaptada de tt-a1i/archify.

Origem local: [architecture-visualization.docx](../architecture-visualization.docx).
