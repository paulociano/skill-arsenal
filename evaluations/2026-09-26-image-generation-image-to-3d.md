# Avaliação — geração de imagem de alta fidelidade e image-to-3D

Data: 2026-09-26

## Escopo
Avaliar fontes externas para melhorar geração/edição de imagens detalhadas e conversão de imagens em assets 3D, consolidando somente capacidades incrementais no Arsenal.

## Fontes avaliadas
- OpenAI Skills — `imagegen`: https://github.com/openai/skills/blob/main/skills/.system/imagegen/SKILL.md
- Microsoft TRELLIS.2: https://github.com/microsoft/TRELLIS.2
- VAST-AI-Research / TripoSR: https://github.com/VAST-AI-Research/TripoSR
- TencentARC / InstantMesh: https://github.com/TencentARC/InstantMesh
- halldm2000 / image-to-3d: https://github.com/halldm2000/image-to-3d

## Capability ledger

### Structured raster generation/editing
**Fonte principal:** OpenAI imagegen  
**Classe:** A  
**Decisão:** CREATE_NEW → `high-fidelity-image-generation`

Valor incremental:
- contrato visual estruturado;
- distinção clara entre geração e edição;
- invariantes explícitos;
- iteração dirigida por inspeção;
- preparação específica para downstream 3D.

Adaptação:
- manter uso da ferramenta de geração disponível no ChatGPT;
- remover políticas de paths/CLI específicas do Codex;
- não importar scripts nem exigir API key.

### Neural image-to-3D routing
**Fontes:** TRELLIS.2, TripoSR, InstantMesh e arquitetura multi-backend  
**Classe:** A/D  
**Decisão:** CREATE_NEW → `image-to-3d`

Valor incremental:
- owner separado da reconstrução procedural Three.js;
- seleção por requisitos reais;
- capability gate antes de prometer execução;
- QA multi-view;
- distinção entre evidência observada e geometria inferida.

### Procedural reconstruction
**Owner existente:** `procedural-3d-reconstruction`  
**Decisão:** KEEP

A skill existente continua owner do caminho imagem → Three.js procedural. Não foi expandida com backends neurais para evitar misturar contratos e runtimes diferentes.

### Multi-backend orchestration
**Fonte de referência:** halldm2000/image-to-3d  
**Classe:** D/B  
**Decisão:** ABSORB_METHOD_ONLY

Foi absorvida a ideia de roteamento por qualidade/velocidade/hardware e inspeção do resultado. Scripts, setup automático, servidor, SSH e dependências GPU não foram importados.

## Stack criada
`concept-to-3d-asset` coordena o fluxo recorrente:
brief/conceito → imagem 3D-ready → reconstrução neural ou procedural → QA.

A stack não obriga todas as skills e evita executar dois caminhos de reconstrução quando um basta.

## Segurança e portabilidade
- nenhuma dependência externa foi instalada;
- nenhum script de setup externo foi executado;
- backends GPU permanecem dependências externas;
- requisitos devem ser verificados na fonte corrente antes de execução;
- TRELLIS.2, TripoSR e InstantMesh não são tratados como ferramentas nativas do ChatGPT;
- credenciais e downloads de pesos não são presumidos.

## Limites da validação
A avaliação foi documental. Não houve benchmark local dos modelos nem validação em GPU. Claims de requisitos e capacidades foram ancorados nos READMEs oficiais consultados; comparações de terceiros foram usadas apenas como referência arquitetural.

## Resultado
Adotado:
- `high-fidelity-image-generation`;
- `image-to-3d`;
- stack `concept-to-3d-asset`.

Preservado:
- `procedural-3d-reconstruction` como caminho procedural independente.

Descartado:
- importação de CLIs, installers, servidores, SSH helpers e runtimes GPU externos.
