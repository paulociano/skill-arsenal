---
name: ai-3d-asset-factory
description: Produzir kits modulares de assets 3D para jogos e web com contratos de encaixe, geometria procedural ou neural, materiais, colisões, GLB, manifestos e validação no runtime; priorizar backends gratuitos realmente disponíveis.
---

# AI 3D Asset Factory

## Escopo e ownership

Use para famílias recorrentes de peças conectáveis (terreno, plataformas, bordas, rampas, pontes, arquitetura, props) e não para um asset isolado. `concept-to-3d-asset` continua owner da conversão de um conceito ou imagem em um asset; esta stack coordena padronização, montagem e integração de um kit. Categoria técnica D: scripts e runtimes são dependências opcionais, não capacidades implícitas do ChatGPT.

## Skills candidatas

- `procedural-3d-reconstruction`: forma, volumes, materiais, pivots, reconstrução por código.
- `image-to-3d`: backend neural quando realmente acessível.
- `high-fidelity-image-generation`: referência 3D-ready somente quando necessária.
- `procedural-game-content`: regras de adjacência, continuidade e jogabilidade.
- `game-performance-engineering`: perfil e orçamento quando existe runtime.
- `verify-before-claim`: gates de evidência quando necessário.

## Workflow e gates

| Etapa | Depende de | Entrega esperada / verificação |
|---|---|---|
| 1. Contrato | Brief/projeto | Engine, eixo/unidades, câmera, biome, grid, escala, perf target, player bounds, formatos e budget de custo; confirmar os fatos do projeto antes de integrar. |
| 2. Kit e interfaces | 1 | IDs estáveis, dimensões nominais, sockets, frames locais, perfis de borda, superfícies caminháveis e collider proxy; desenhar famílias e variações sem romper o contrato. |
| 3. Roteamento | 1–2 | Backend disponível e autorizado, licença, custo, hardware e formato confirmados; não cobrar sem autorização; fallback reproduzível. |
| 4. Produção | 2–3 | Gerar um vertical slice mínimo, meshes fechados quando aplicável, material coerente, seed e fonte versionáveis; preservar referências e geometria jogável. |
| 5. Exportação | 4 | GLB, manifesto e colisões separadas; registrar triângulos, escala, materiais, arquivos, provenance e status; exportar em pasta nova. |
| 6. QA estrutural e visual | 5 | Reabrir GLB, checar índices/bounds/normais, seams, escala, transparência, UV/PBR quando houver, vistas frontal, lateral e oblíqua. Testar ao menos duas peças adjacentes, não só isoladas. |
| 7. Integração opcional | 6 | Com autorização no repo consumidor: mapear render e physics, montar trecho jogável, verificar deslocamento/pulos/colisões, culling, draw calls e frame budget no runtime. |
| 8. Publicar | 6; 7 se for game-ready | Versionar código, manifesto e assets aceitos em destino autorizado; documentar QA executado, pendências e limitações. Não confundir export válido com aprovação visual ou gameplay. |

## Roteamento de backends

- **Procedural puro (JS/Three.js ou Python)**: preferir para superfícies contínuas, dimensões precisas, âncoras e colisões. Pode funcionar localmente sem GPU/API. O MVP nesta pasta usa Node.js e gera GLB por código sem instalar bibliotecas.
- **Blender local**: usar scripts bpy ou Blender MCP quando Blender/servidor compatível estiver instalado e autorizado. Blender não é uma conexão automática do ChatGPT; MCP exige host compatível, transporte/autenticação reais e permissões. Não expor serviço local sem segurança; não executar Python remoto arbitrário.
- **TRELLIS.2 / TripoSR**: opções neural image-to-3D para props orgânicos e decoração. Verificar requisitos e licenças na fonte atual; cota de demo não equivale a API gratuita. Usar `image-to-3d` para seleção e QA. Não inventar integração ou credenciais.
- **Serviços comerciais**: só quando explicitamente aceitos e custo confirmado; sem fallback pago silencioso.

Referências: https://github.com/microsoft/TRELLIS.2 ; https://github.com/VAST-AI-Research/TripoSR ; https://github.com/LiCinCan/blender-ai-mcp-addon ; https://www.blender.org/ ; https://threejs.org/ .

## Contrato modular

- GLB em metros, Y-up e frames locais declarados; adaptar e testar na engine de destino.
- Manifesto versionado com id, arquivo, dimensões, placement, anchors/perfis, collider proxy, seed, generator, material/origem e status. O manifesto não cria colisão automaticamente na engine.
- Separar superfície visual orgânica de superfície caminhável; nenhuma irregularidade decorativa pode quebrar a navegação. Perfis coincidentes nas costuras, sem frestas, interseções visíveis ou mudanças bruscas de altura.
- Evitar planos transparentes e imagens billboard como substitutos de volume jogável. Texturas e detalhes devem acompanhar a geometria; decoração pode usar técnicas distintas quando justificado.
- Reusar material/atlas quando adequado, instancing apenas onde suportado, e limitar variantes por orçamento medido.
- Neural: normalizar pivots/escala, reparar malhas, simplificar e gerar colisão apropriada. Não usar mesh neural bruto como piso crítico sem QA.

## MVP gratuito (executável por código)

Em `stacks/ai-3d-asset-factory/`:

```sh
node generate-terrain.mjs --test
node generate-terrain.mjs ./terrain-demo 42
```

Requer Node.js 18+ disponível. O destino precisa ser novo; não sobrescreve. Produz dois módulos de terreno de 4 m com perfis laterais compatíveis, volume fechado, material PBR por fatores e cores de vértice (não inclui mapas de textura), manifesto JSON e caixas de colisão propostas. É protótipo procedural low-poly, não reconstrução neural e não asset aprovado para produção. O teste interno cobre cabeçalhos/chunks GLB, seam, normais, bordas fechadas e determinismo; usar validador glTF e importador real para QA externo. Não confundir status prototype com game-ready.

## Integração ChatGPT

- Chat com execução de código/arquivos: gerar por código somente se runtime existir, entregar GLB verificável ou código e instruções.
- Codex/local: executar gerador em workspace autorizado; Blender/Three.js como opcionais. Não presumir que o ambiente possui Node/Blender/GPU.
- Chat com conectores: verificar capacidade real do plugin e plano; uma skill não cria acesso ao motor.
- GitHub: armazenar fonte e manifesto; binários apenas se houver caminho de upload verificado. Não declarar upload ou integração com jogo sem evidência.
- Se não houver backend neural gratuito acessível, manter procedural como opção e entregar referência/handoff para a parte neural.

## Parcimônia e limites

Começar com dois blocos conectáveis, validar em contexto e só então expandir a biblioteca. Não carregar todas as skills, gerar imagens desnecessárias, instalar MCP ou modificar projeto consumidor por padrão. Evidência distingue: especificado, gerado, estruturalmente verificado, visualmente aprovado e integrado ao runtime.
