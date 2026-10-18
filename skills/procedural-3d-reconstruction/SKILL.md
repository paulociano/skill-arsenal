---
name: procedural-3d-reconstruction
description: "Reconstruir objetos de imagens como modelos procedurais Three.js por estágios e comparação visual com a referência."
---

# procedural-3d-reconstruction

## Objetivo

Reconstruir um objeto ou personagem de uma imagem de referência como modelo 3D procedural em Three.js, usando um pipeline por estágios, evidência visual e gates de qualidade.

## Quando usar

- image → Three.js procedural;
- prop/game object/character reconstruído por código;
- necessidade de hierarquia animável, pivots, sockets, materiais e interação;
- reconstrução que precisa preservar silhouette, proporções e detalhes identificadores.

## Princípios

- reconstrução por código, não fotogrametria ou mesh extraction;
- uma única imagem não revela geometria oculta: marcar baixa confiança em vez de inventar;
- observação antes de inferência;
- qualidade definida antes de gerar código;
- construir em passes, não one-shot;
- revisão visual precisa comparar o render com a referência.

## Workflow

1. **Validate** — verificar se a referência é adequada ao objetivo 3D.
2. **Analyze** — decompor macro → meso → micro, materiais, silhouette, relações e áreas invisíveis.
3. **Quality contract** — declarar fidelidade esperada, complexidade, orçamento e features críticas.
4. **Spec** — componentes, hierarquia, materiais, pivots, sockets, anchors e topology rationale. Para objetos físicos/fabricáveis, separar intent imutável de uma cena semântica mutável e registrar ownership de features, interfaces, dimensões e materiais antes de compilar geometria.
5. **Build passes** — blockout → structural → form → material → surface → lighting → interaction → optimization.
6. **Review** — capturar viewpoints, comparar silhouette/proporções/materiais/detalhes e registrar correções.
7. **Bounded correction loop** — corrigir apenas falhas observadas; limitar iterações e preservar evidência.
8. **Verify final** — validar artefato, comportamento, performance e aproximações declaradas. Quando o destino for fabricação, incluir checks pertinentes de espessura real, conectividade, interferência/clearance, orientação de impressão, fit e readback do formato exportado; uma preview renderizada não substitui esses checks.

## Regras

- textura/material convincente não substitui geometria estrutural ausente;
- para superfícies específicas da referência, preferir evidência/projeção real quando o ambiente permitir;
- uma única câmera frontal não prova qualidade 3D: usar múltiplos viewpoints;
- declarar quando o resultado é aproximado, stylized ou low-poly;
- manter state/artifacts fora da conversa quando o ambiente de projeto permitir retomada multi-sessão.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Para páginas web, usar o navegador controlável disponível e sua API documentada; separar inspeção de DOM, evidência visual e estado de aplicação. Controle de navegador não implica controle de aplicativos nativos ou dispositivos móveis. Verificar Three.js e suporte gráfico do projeto. Não exigir scripts forge/; quando não houver render executável, entregar spec/código e separar isso de validação visual.

## Referências

Adaptada de img2threejs/img2threejs v2.0.0.

Origem local: [procedural-3d-reconstruction.docx](../procedural-3d-reconstruction.docx).

## Blender como runtime editável de cenas (blender-ai-mcp-addon)

Se o projeto usa Blender, tratar a cena como estado observável e mutável, e não apenas script gerador: (1) inspecionar objects, hierarquia, transform, materiais e câmera antes de alterar; (2) especificar operações pequenas, ordem, snapshot/undo e resultado visual esperado; (3) para workflows de agentes, separar manager, executor e reviewer com checks após cada mutação e limite de retries; (4) validar screenshots reais de mais de uma perspectiva e reabrir arquivo/export final; (5) exigir aprovação antes de executar Python arbitrário, imports remotos, apagar objetos ou exportar dados externos. Código Python do addon não equivale a sandbox, mesmo com validação. Usar integração MCP somente se realmente instalada e autenticada; caso contrário, entregar scripts Blender e instruções de testes, sem afirmar execução na UI. Fonte: https://github.com/LiCinCan/blender-ai-mcp-addon (2026-10-18), Windows/Blender 4.2+ e serviços opcionais externos.
