# Avaliação: image-to-svg-vectorization (2026-10-12)

## Decisão
**D — skill técnica com implementação própria e dependências externas opcionais. ADOTAR** como capability independente, especializada em raster de logos/ícones para paths SVG. `brand-logo-exploration` cria/explora logo, `brand-asset-production` exporta variantes de master: nenhuma é substituto para raster tracing com verificações de furos e XML.

## Fontes analisadas
- https://github.com/visioncortex/vtracer — tracing raster->SVG, colorido/binário, CLI.
- https://potrace.sourceforge.net/ — tracing de silhuetas e curvas.
- https://github.com/svg/svgo — otimização opcional de SVG.
- https://github.com/jankovicsandras/imagetracerjs — alternativa JavaScript, não incluída no runtime mínimo.

## Valor incremental
Roteamento por engine, fallback executável sem dependências dos motores externos, teste automatizado de vazados, rejeição de raster embutido e orientação de validação visual nos tamanhos de favicon.

## Validação
Ambiente Python com OpenCV, Pillow, NumPy, pytest e CairoSVG; Potrace e VTracer **não disponíveis**. Quatro testes automatizados do helper passaram localmente em 2026-10-12: ícone anelar com furo, rejeição de máscara vazia, limiar de imagem opaca, rejeição de SVG com bitmap embutido. Ainda não há teste de fidelidade perceptiva com logos reais; não tratar a conversão como aprovada por design humano.

## Segurança
**CAUTION** condicional: código local processa arquivos raster com Pillow/OpenCV, executa binários locais conhecidos sem shell e cria SVG. Riscos remanescentes: parser de imagens malformadas, consumo de recursos, binários instalados pelo operador e entrada não confiável. Limite de 20 MP; timeout 45 s por execução de motor; não usar instaladores externos, URLs ou upload remoto. SVG precisa revisão se for usado em HTML não isolado.

## Portabilidade
A instrução é nativa de Agent Skills, mas executabilidade depende do ambiente. Sem Python/libs ou motor local, não afirmar que converteu. O fallback OpenCV gera linhas e não substitui tracing Bézier de produção.
