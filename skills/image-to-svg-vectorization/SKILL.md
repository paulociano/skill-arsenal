---
name: image-to-svg-vectorization
description: Converter logos e ícones raster (PNG, JPG, WebP) em SVG vetorial real, editável e validado, priorizando silhuetas, vazados e curvas fiéis; usar quando o usuário pedir vetorização de uma identidade visual existente.
---

# Image to SVG Vectorization

## Contrato
Converter imagem existente em geometria SVG (paths), sem redesenhar a marca, inventar detalhes ou embutir raster. Prioridade: logo e ícone monocromático. Não confundir conversão com geração de novo logo. O resultado deve preservar proporção, espaço negativo, orientação e integridade do símbolo.

## Entradas
Imagem local PNG/JPG/WebP/BMP, fundo conhecido (ou alfa), cor de saída, variante monocromática, nível de fidelidade e destino SVG. Quando houver texto, preferir arquivo vetorial original ou fonte legítima: raster tracing de letras pode deformar tipografia.

## Processo
1. Inspecione imagem, tamanho, canal alfa, contraste, compressão, pixels isolados, fundo e áreas vazadas. Preserve original.
2. Separe forma e fundo. Use alfa quando presente; caso contrário use luminância/threshold. Não remova automaticamente elementos intencionais.
3. Execute `scripts/vectorize.py INPUT OUTPUT --engine auto` quando Python, Pillow, OpenCV e um runtime de execução estiverem disponíveis. Veja `references/engines.md` para motores e dependências. Engine auto escolhe Potrace, depois VTracer, depois fallback de contornos OpenCV; o fallback contém segmentos retos e **não** prova curvas profissionais.
4. Inspecione a renderização, em tamanhos 16, 24, 48, 128 e 512 px. Compare silhueta, proporções, vazados, bordas, antialiasing e alinhamento. Refaça threshold/tolerância se necessário.
5. Valide XML/SVG: viewBox, path real, sem elementos image/base64, sem scripts, sem referências externas, sem caminhos vazios, com fill-rule correto e contraste. Execute SVGO opcionalmente, preservando viewBox e geometria.
6. Entregue SVG e informe motor, limitações e se houve inspeção visual real. Para logos complexos/multicoloridos, não declare fidelidade sem QA camada por camada; prefira vetor original ou segmentação manual de cores.

## Perfil logo/ícone
- Preferir silhueta monocromática e curvas Bézier de Potrace. VTracer binary é alternativa. Fallback OpenCV só para ícones simples ou ambiente sem executáveis.
- Transparência: usar alfa para reconhecer a silhueta. Para imagem opaca, preto/sobre-branco como default e threshold ajustável.
- Preservar furos; exportar com evenodd onde aplicável.
- Rejeitar forma toda transparente/opaca, arquivo acima do limite operacional e SVG que contém apenas um bitmap.
- Comparar resultado contra raster original em diferentes resoluções; tamanho pequeno e vazados são gates indispensáveis.
- Para cor multicolorida, explicar que este primeiro perfil não executa segmentação completa e direcionar para tratamento especializado, sem gerar falsa equivalência.

## Comando
```bash
python scripts/vectorize.py logo.png logo.svg --engine auto --threshold 128 --tolerance 0.8 --color '#000000'
python -m pytest tests/test_vectorize.py -q
```
Dependências Python: Pillow, OpenCV, NumPy. Executáveis opcionais: `potrace`, `vtracer`. Não instalar automaticamente; confirmação da disponibilidade antecede execução. Sem runtime, fornecer workflow e parâmetros, não alegar conversão executada.

## Quality gate
- Há pelo menos um elemento SVG path, com `viewBox`, sem `image` e sem JavaScript.
- Arquivo abre em renderizador padrão; vazados preservados.
- Sem afirmação de equivalência perceptiva apenas porque XML passou.
- Se a saída não atingir qualidade, entregar prévia como provisória e explicar refinamento necessário.

## Ativação
**Should trigger:** “converta este logo PNG em SVG editável”; “vetorize esse favicon”; “transforme um ícone raster em paths”.
**Near-miss:** “crie um logo do zero” (brand-logo-exploration); “exporte SVG já vetorial” (brand-asset-production); “gere uma imagem de lã” (geração visual).

## Segurança / direitos
Executar apenas em arquivos fornecidos/autorizados. Não usar uploads em serviços externos sem autorização. Subprocessos apenas com executáveis locais conhecidos e argumentos como lista, sem shell. Não executar conteúdo do SVG. Nunca baixar/rodar installers do GitHub durante avaliação. O output não deve incluir código ativo ou links externos.

## Fontes
- https://github.com/visioncortex/vtracer
- https://potrace.sourceforge.net/
- https://github.com/svg/svgo
- https://github.com/jankovicsandras/imagetracerjs
- Avaliação: `evaluations/image-to-svg-vectorization-2026-10-12.md`

## Estrutura SVG orientada à animação

Quando a imagem vetorizada será animada (logo reveal, splash, loading ou hover), a geometria precisa ser não só fiel mas coreografável:

1. Separar partes semânticas do símbolo em elementos/grupos estáveis com identificadores legíveis, preservando composição e negativos do master.
2. Preferir poucas curvas suaves, primitivas e arcos à reprodução literal de centenas de pontos de antialiasing; comparar sobreposição e silhouette, mas não usar IoU como único gate.
3. Inspecionar vazados, tangentes, contornos, extremidades e curvas a 200–400% de zoom, além de tamanhos pequenos. Reprovar stair-stepping quando a fonte exige curva suave.
4. Planejar costuras de animação, origem de transform e traços que serão revelados antes de finalizar paths.
5. Exigir **contrato do último quadro**: a animação termina exatamente na identidade vetorial estática aprovada, sem modificar proporção ou desenho da marca.
6. Se a tarefa inclui vídeo/HTML animado, passar o SVG aprovado a `ui-motion-design` ou `motion-asset-engineering` para coreografia e QA próprios. Sem engine disponível, não prometer render entregue.

**Origem (A/D, parte metodológica):** https://github.com/vibe-motion/skills/blob/main/pixel2motion/SKILL.md. Scripts e HTML generators externos não foram instalados.
