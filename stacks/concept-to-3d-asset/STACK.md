---
name: concept-to-3d-asset
description: Converte uma ideia ou referência visual em asset 3D por um fluxo recorrente de direção visual, imagem 3D-ready, reconstrução neural ou procedural e QA multi-view.
---

# Concept To 3D Asset

## Objetivo
Orquestrar concept → imagem controlada → reconstrução 3D → validação, escolhendo o menor caminho capaz de entregar o asset desejado.

## Skills candidatas
- high-fidelity-image-generation
- image-to-3d
- procedural-3d-reconstruction
- design-direction
- verify-before-claim

## Roteamento
Use apenas as etapas necessárias.

### Caminho A — ideia/texto → asset 3D
1. definir uso final e critérios;
2. gerar imagem 3D-ready com `high-fidelity-image-generation`;
3. reconstruir com `image-to-3d`;
4. validar múltiplas vistas, geometria e materiais.

### Caminho B — imagem existente → asset 3D
1. auditar a referência;
2. editar/preparar somente se a entrada prejudicar reconstrução;
3. executar ou especificar `image-to-3d`;
4. validar.

### Caminho C — controle por código
Quando o usuário precisa de Three.js procedural, pivots, sockets, hierarquia animável ou geometria explicitamente construída por código, use `procedural-3d-reconstruction` em vez de reconstrução neural.

### Caminho D — personagem rigável/animável
Quando o asset final precisa ser um personagem humanoide jogável, animável ou retargetable:
1. definir skeleton/runtime alvo, escala e conjunto mínimo de animações antes da geração;
2. preparar concept/reference em pose que preserve separação de membros, preferindo A-pose ou T-pose quando o backend de rigging exigir;
3. evitar props soltos, capas extensas, membros sobrepostos e silhuetas que confundam skinning quando isso não for parte essencial do design;
4. reconstruir o mesh e validar geometria/material antes de gastar em rig/animation;
5. executar rigging somente em backend realmente disponível;
6. validar skeleton, weights, escala, root/origin e pelo menos idle + locomoção + uma animação extrema;
7. verificar transições/blending no runtime de destino, porque clips válidos isoladamente não provam integração correta.

A imagem pose-controlled é uma técnica para melhorar a entrada, não garantia de rig limpo. Quando o usuário já possui um mesh adequado, pule a geração e comece no estágio de rig/validation.

## Workflow

### 1. Target contract
Defina o mínimo necessário:
- finalidade;
- formato;
- fidelidade esperada;
- textura/PBR;
- performance/poly budget;
- necessidade de edição/rig/partes separadas;
- runtime disponível.

### 2. Visual source
Se não houver imagem adequada, crie uma referência que favoreça leitura volumétrica. Se houver, preserve-a e só corrija problemas que prejudiquem o próximo estágio.

### 3. Reconstruction strategy
Escolha neural/external-backend ou procedural conforme o contrato. Não execute ambos por padrão.

### 4. Produce
Execute somente ferramentas e runtimes realmente disponíveis. Se o backend 3D não estiver acessível, pare no handoff reproduzível em vez de afirmar que um mesh foi criado.

### 5. QA loop
Compare referência e asset por:
- silhouette;
- proporções;
- volumes;
- detalhes identificadores;
- materiais;
- artefatos em vistas não frontais;
- requisitos do destino.

Corrija a causa dominante por vez.

### 6. Stop
Termine quando:
- o asset atende aos critérios observáveis;
- limitações estão declaradas;
- formato/artefato está validado quando execução ocorreu;
- ou o próximo passo depende de runtime/hardware não disponível.

## Regra de parcimônia
Não gere uma imagem nova se a referência atual já for adequada. Não use reconstrução procedural quando um backend neural satisfaz o objetivo. Não use backend pesado para preview quando uma opção leve atende ao contrato.

## Handoff
Quando a reconstrução ocorrer fora do ambiente atual, entregue:
- imagem de entrada selecionada;
- backend recomendado;
- requisitos verificados;
- parâmetros/objetivo de exportação;
- checklist de QA;
- incertezas que exigem inspeção humana.

## Origem metodológica

O caminho de personagem rigável/animável foi refinado a partir de [blendi-remade/fal-3d-unreal](https://github.com/blendi-remade/fal-3d-unreal), preservando pose-controlled concept → mesh → rig → animation e QA de integração sem assumir fal.ai, Meshy, Unreal, glTFRuntime ou seus IDs de animação como capacidades disponíveis.
