---
name: image-to-3d
description: Preparar, rotear e validar conversões de imagens em assets 3D por modelos de reconstrução externos, escolhendo backend por fidelidade, velocidade, hardware, materiais e formato sem fingir execução indisponível.
---

# Image To 3D

## Objetivo
Conduzir imagem → asset 3D com um contrato explícito de entrada, seleção de backend, execução somente quando houver runtime real e QA geométrico/material.

## Quando usar
- converter uma ou mais imagens em mesh/asset 3D;
- escolher entre backends de image-to-3D;
- preparar imagens para TRELLIS.2, TripoSR, InstantMesh ou pipeline equivalente;
- produzir ou planejar GLB/OBJ com textura ou materiais;
- comparar velocidade, VRAM, topologia, textura e fidelidade.

Para reconstrução manual/procedural em Three.js, use `procedural-3d-reconstruction`. Esta skill é owner de reconstrução neural/external-backend.

## Princípio central
Uma imagem 2D contém evidência parcial. Separe sempre:
- **observado** na imagem;
- **inferido** pelo modelo;
- **não verificável** sem vistas adicionais.

Não descreva regiões ocultas geradas como reconstrução factual.

## Workflow

### 1. Define target
Determine:
- uso final: preview, web, game, render, protótipo, fabricação ou outro;
- formato desejado;
- necessidade de textura/PBR;
- orçamento de polígonos;
- prioridade entre velocidade e fidelidade;
- hardware/runtime realmente disponível.

### 2. Audit input
Verifique:
- objeto completo;
- silhouette;
- oclusões;
- fundo;
- perspectiva;
- iluminação;
- transparência/reflexos;
- detalhes finos;
- presença de múltiplos objetos.

Se a entrada puder ser melhorada antes da reconstrução, use `high-fidelity-image-generation` para gerar/editar uma versão 3D-ready quando isso respeitar a intenção do usuário.

### 3. Route backend
Escolha por requisitos e capacidade real, não por ranking fixo.

**TRELLIS.2**
- candidato quando alta fidelidade, topologia complexa e materiais PBR importam;
- fonte oficial declara image-to-3D de alta resolução, atributos Base Color/Roughness/Metallic/Opacity e exportação GLB;
- implementação oficial requer Linux, CUDA e GPU NVIDIA com pelo menos 24 GB de memória.

**TripoSR**
- candidato para preview e reconstrução rápida de uma única imagem;
- fonte oficial reporta execução sub-segundo em A100 e cerca de 6 GB VRAM no fluxo padrão;
- suporta baking opcional de textura.

**InstantMesh**
- candidato para mesh a partir de single-image com reconstrução sparse-view;
- exporta OBJ com vertex colors por padrão e pode exportar texture map;
- depende de ambiente Python/PyTorch/CUDA compatível.

**Outros backends**
- Hunyuan3D, TripoSG, SPAR3D ou futuros modelos podem ser considerados somente após verificar fonte atual, licença, requisitos e interface.
- tabelas de terceiros são sinais de descoberta, não autoridade sobre benchmarks.

### 4. Capability gate
Antes de executar:
1. confirme que o runtime/backend está realmente acessível;
2. confirme hardware, dependências e credenciais necessárias;
3. não instale scripts externos automaticamente;
4. não solicite segredo que não seja necessário;
5. se execução não estiver disponível, entregue preparação, comando/spec ou plano reproduzível e declare o limite.

### 5. Reconstruct
Quando houver ambiente autorizado:
- preserve a imagem original;
- faça preprocessing mínimo e rastreável;
- registre backend e parâmetros relevantes;
- gere o asset;
- mantenha outputs intermediários somente quando úteis para diagnóstico.

### 6. Validate
Inspecione em múltiplas vistas:
- silhouette;
- proporções;
- buracos e superfícies abertas inesperadas;
- regiões finas;
- self-intersections/non-manifold quando relevante;
- UV/textura;
- PBR/material;
- artefatos nas regiões ocultas;
- contagem de faces/vertices e tamanho do arquivo;
- escala/orientação quando o destino exigir.

Uma renderização frontal não prova qualidade 3D.

### 7. Correct or reroute
Se a falha vier da entrada, melhore a imagem.
Se vier do backend, ajuste parâmetros ou troque de backend.
Se for estrutural e o usuário precisar de controle por código, considere `procedural-3d-reconstruction`.

Limite ciclos de correção e registre por que o backend foi trocado.

## Saída
Informe:
- input usado e eventuais preprocessamentos;
- backend escolhido e razão factual;
- formato produzido ou planejado;
- validações executadas;
- limitações observadas;
- regiões inferidas/incertas quando relevantes.

## Segurança e portabilidade
TRELLIS.2, TripoSR, InstantMesh e pipelines multi-backend são software externo. Trate-os como dependências, não como ferramentas nativas do ChatGPT. Não execute installers ou scripts de setup sem ambiente e autorização apropriados. Verifique licenças e requisitos na versão corrente antes de uso produtivo.

## Fontes de referência
- https://github.com/microsoft/TRELLIS.2
- https://github.com/VAST-AI-Research/TripoSR
- https://github.com/TencentARC/InstantMesh
- https://github.com/halldm2000/image-to-3d

O último é referência de arquitetura multi-backend; claims sobre modelos devem ser confirmados nas fontes oficiais correspondentes.
