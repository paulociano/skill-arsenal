# Avaliação de repositórios para personagens e sets — 2026-10-10

## Método
Pesquisa documental de onze projetos, comparando capacidades, owners do Arsenal, dependências externas e riscos. Foram consultados diretamente READMEs de ComfyUI, InstantID, IP-Adapter, Nerfstudio e Hunyuan3D-2. Os demais são triagem inicial: exigem leitura adicional de licença e documentação antes de operação. Não houve instalação, inferência ou benchmark próprio.

## Avaliações e decisões

| Repositório | Classe | Capacidade | Decisão e owner |
|---|---|---|---|
| [InstantID](https://github.com/instantX-research/InstantID) | D/B | Identidade de rosto | ABSORB_METHOD_ONLY em character-continuity |
| [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) | D/B | Referência de imagem | ABSORB_METHOD_ONLY em character-continuity |
| [ControlNet](https://github.com/lllyasviel/ControlNet) | D/B | Pose, profundidade e estrutura | ABSORB_METHOD_ONLY em character-continuity, cinematic-visual-direction e set-continuity |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | D | Grafo de geração multimodal | KEEP_EXTERNAL_REFERENCE |
| [Blender](https://github.com/blender/blender) | D/B | Cenas, câmeras e geometria | ABSORB_METHOD_ONLY em set-continuity |
| [Nerfstudio](https://github.com/nerfstudio-project/nerfstudio) | D/B | Reconstrução neural de cenas | ABSORB_METHOD_ONLY em set-continuity |
| [Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | D | Geração 3D | KEEP_EXTERNAL_REFERENCE em concept-to-3d-asset |
| [InstantMesh](https://github.com/TencentARC/InstantMesh) | D | Imagem para mesh | KEEP_EXTERNAL_REFERENCE em concept-to-3d-asset |
| [LivePortrait](https://github.com/KlingAIResearch/LivePortrait) | D | Animação de retrato | KEEP_EXTERNAL_REFERENCE em ai-reels-production |
| [CogVideo](https://github.com/zai-org/CogVideo) | D | Vídeo generativo | KEEP_EXTERNAL_REFERENCE em ai-reels-production |
| [FaceFusion](https://github.com/facefusion/facefusion) | D | Edição facial | KEEP_EXTERNAL_REFERENCE; considerar privacidade e autorização |

## Adoção
Criada skill `set-continuity`, com owner novo para persistência de landmarks, layout, câmera, iluminação e estado de objetos entre cenas. Não duplicar `character-continuity` nem `concept-to-3d-asset`.

Should-trigger: storyboard com dez planos do mesmo ambiente, pedindo continuidade entre frente e contraplano.
Near-miss: imagem isolada ou planta técnica arquitetônica.
Aceitação: bíblia de cenário, mapa de câmera, variáveis autorizadas e QA identificam drift sem confundir rotação de câmera com alteração espacial.

## Portabilidade e segurança
- Não há integração nem runtime instalado por esta avaliação.
- O README de InstantID descreve código Apache-2.0, mas checkpoints de pesquisa e modelos de face com condições próprias; não presumir licença comercial geral.
- Hunyuan3D-2 usa licença comunitária com restrições territoriais e comerciais; conferir termo vigente para cada uso.
- Em ComfyUI, revisar extensões, nós, dependências e permissões antes de executar.
- Para imagens identificáveis, observar consentimento, privacidade e direitos aplicáveis.
- Verificar licença de código, pesos, dados e saídas separadamente.

## Evidência e limites
Popularidade por estrelas não é avaliação independente de qualidade. Nenhum benchmark controlado de fidelidade facial, geometria, consistência de cenário, GPU, velocidade ou custos foi executado. Revisar READMEs, licenças e versões de cada candidato no momento de implementação.
