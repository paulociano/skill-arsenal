---
name: set-continuity
description: Manter cenários, sets e ambientes recorrentes visual e espacialmente coerentes entre shots, páginas ou vídeos por bíblia do set, mapa de câmeras, âncoras e QA de continuidade.
---

# Set Continuity

## Objetivo
Preservar continuidade de cenário entre imagens, vídeos e sequências, separando invariantes espaciais das variações intencionais de câmera, iluminação e estado narrativo. Esta skill **não** executa Blender, Nerfstudio ou ComfyUI por si só.

## Quando usar
- mesmo ambiente reaparece em múltiplas cenas/ângulos;
- objetos, portas, janelas, materiais ou proporções mudam sem intenção;
- produção precisa de set bible, shot map ou referência espacial;
- cenas geradas em etapas apresentam drift de layout.

Não usar para cenário isolado sem reutilização nem substituir `architectural-design-engineering` em projeto técnico de arquitetura.

## Contrato do set
Registrar em uma **set bible**:
1. identificador, uso, escala aproximada e planta/esquema de adjacências;
2. pontos fixos: portas, janelas, pilares, circulação, landmarks e mobiliário ancorado;
3. materiais, paleta, texturas e iluminação-base;
4. posições orientadas de câmera e eixos da cena (front, reverse, 3/4, wide, close);
5. props permanentes e variáveis autorizadas;
6. estado narrativo por cena: horário, clima, objetos movidos, alterações planejadas.

Separar **geometria/layout** de **estilo**, **luz**, **câmera** e **ação**.

## Escada de controle
Escolher o menor mecanismo suficiente:
1. texto curto com invariantes espaciais explícitos;
2. imagem-mestra + vistas de referência próximas da câmera alvo;
3. mapa/blueprint simplificado, âncoras e atlas multi-view;
4. composição em estágios: fundo/set, personagem, props e ajustes localizados;
5. se disponível, reconstrução/ambiente 3D persistente e render por câmera;
6. pipelines externos de condicionamento ou treinamento somente se executáveis e licenciados.

## Workflow
1. Inventariar as imagens, vídeos ou modelos de origem, sem regenerar assets válidos.
2. Criar set bible mínima, distinguindo fatos observados de decisões novas.
3. Definir câmera, enquadramento, landmarks visíveis e estado de cada shot.
4. Escolher referência próxima e produzir somente a mudança necessária.
5. Revisar geometria, escala, posições relativas, superfícies, reflexos, sombras, iluminação e continuidade entre shots.
6. Registrar drift e corrigir primeiro a causa dominante (referência, câmera, composição, edição localizada, só então pipeline).
7. Versionar set bible e estado de cena quando houver alterações intencionais.

## QA verificável
- Porta/janela e landmarks do mesmo lado e posição relativa quando camera flip não explica a mudança.
- Escala e profundidade plausíveis entre planos.
- Objetos persistentes não aparecem/desaparecem sem motivo.
- Lighting continuity coerente com horário/ângulo proposto.
- Vistas reversas consistentes com mapa de câmeras.
- Alterações narrativas registradas; mudanças intencionais não contam como erro.

## Limites e segurança
Blender e Nerfstudio são referências de implementação para 3D/reconstrução, não ferramentas assumidas. ComfyUI e ControlNet são referências de pipeline. Não instalar nós, checkpoints, extensões, scripts ou pacotes automaticamente; exigir revisão de código, origem, licença, privacidade e permissões. Para reconstrução de locais privados, exigir fontes autorizadas. Render estático não prova editabilidade 3D.

## Integrações
- `character-continuity`: identidade de pessoas, mantida separada do set.
- `cinematic-visual-direction`: enquadramento, câmera, narrativa e movimento.
- `concept-to-3d-asset`: objetos/props 3D, quando necessário.
- `high-fidelity-image-generation`: geração/edição de frames quando disponível.

## Critério de conclusão
Os elementos invariantes do cenário são reconhecíveis entre todos os shots avaliados, com câmera, iluminação e alterações autorizadas documentadas. Declarar explicitamente shots não verificados.

## Origem e avaliação
Metodologia inspirada por Blender (https://github.com/blender/blender), Nerfstudio (https://github.com/nerfstudio-project/nerfstudio), ComfyUI (https://github.com/Comfy-Org/ComfyUI) e condicionamento estrutural de ControlNet (https://github.com/lllyasviel/ControlNet). A avaliação detalhada está em `evaluations/2026-10-10-character-set-production-repositories.md`. Nenhum runtime desses projetos foi incorporado.
