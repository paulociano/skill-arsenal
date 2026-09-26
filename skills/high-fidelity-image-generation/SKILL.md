---
name: high-fidelity-image-generation
description: Gerar ou editar imagens raster com direção visual estruturada, preservação explícita de invariantes e ciclos curtos de inspeção, incluindo preparação de imagens adequadas para reconstrução 3D.
---

# High Fidelity Image Generation

## Objetivo
Transformar pedidos visuais em imagens mais controladas e detalhadas usando o gerador de imagens realmente disponível, com especificação proporcional ao pedido, preservação de referências e revisão por critérios observáveis.

## Quando usar
- geração ou edição de fotos, ilustrações, concept art, mockups, texturas e assets raster;
- pedidos em que composição, câmera, luz, materiais ou microdetalhes importam;
- edição que precisa preservar identidade, pose, layout, produto ou outros invariantes;
- criação de uma imagem-base destinada a reconstrução image-to-3D.

Não use para SVG/código vetorial determinístico, diagramas exatos ou quando outra skill visual especializada for owner mais direto.

## Contrato visual
Antes de gerar, extraia somente os campos que mudam materialmente o resultado:
- **objetivo/uso**;
- **sujeito** e atributos essenciais;
- **composição/câmera**;
- **iluminação/atmosfera**;
- **materiais/texturas**;
- **paleta**, quando relevante;
- **texto verbatim**, se houver;
- **invariantes**;
- **evitar**, apenas para falhas prováveis.

Não transforme todo pedido em um formulário. Se o briefing já for específico, normalize sem inventar detalhes criativos.

## Workflow
1. **Classify** — distinguir geração nova de edição de imagem existente.
2. **Inspect references** — identificar o papel de cada imagem: alvo de edição, referência de sujeito, estilo, composição ou material.
3. **Build prompt spec** — converter o pedido em instrução visual curta, espacialmente explícita e orientada ao uso final.
4. **Generate/Edit** — usar a ferramenta de geração de imagem disponível no ambiente. Para editar uma imagem específica, exigir que o alvo esteja realmente acessível no contexto.
5. **Inspect** — verificar sujeito, silhouette, proporções, composição, iluminação, materiais, texto e invariantes relevantes.
6. **Targeted iteration** — se necessário, fazer uma alteração principal por iteração em vez de reescrever toda a direção.
7. **Stop** — encerrar quando os critérios do briefing estiverem satisfeitos ou quando nova iteração depender de informação ausente.

## Direção de detalhe
Para aumentar fidelidade, prefira relações concretas a adjetivos genéricos:
- descreva posição relativa e enquadramento;
- descreva propriedades de superfície observáveis, como fosco, polido, translúcido, gasto ou escovado;
- descreva fonte, direção e dureza da luz quando isso afeta forma;
- para realismo, peça variação natural e imperfeições coerentes em vez de "ultra detailed" repetido;
- mantenha o foco no detalhe que será visível na escala final.

## Edição e invariantes
Em edições:
1. declare o que muda;
2. declare o que permanece;
3. preserve geometria, identidade, texto ou composição quando forem invariantes;
4. não trate referência de estilo como autorização para alterar o sujeito;
5. prefira edição não destrutiva quando houver escolha de artefatos.

## Modo 3D-ready
Quando a imagem será entrada para reconstrução 3D:
- priorize um único objeto completo, sem cortes;
- silhouette clara e separada do fundo;
- fundo simples ou transparente quando suportado;
- perspectiva moderada que revele frente e lateral;
- iluminação suficiente para ler volume sem sombras destrutivas;
- evitar oclusões desnecessárias, motion blur e depth of field que esconda bordas;
- tornar materiais e transições de superfície legíveis;
- não inventar vistas ocultas como se fossem conhecidas.

Quando múltiplas vistas forem aceitas pelo pipeline downstream, priorize consistência de identidade, proporção, materiais e detalhes entre elas.

## QA
Avalie somente dimensões relevantes:
- fidelidade ao sujeito;
- silhouette/proporções;
- hierarquia e composição;
- coerência de luz;
- leitura de materiais;
- microdetalhes úteis;
- texto, quando houver;
- preservação de invariantes;
- adequação ao próximo estágio.

Para 3D-ready, acrescente:
- objeto inteiro visível;
- bordas separáveis;
- ausência de elementos flutuantes ambíguos;
- superfícies importantes visíveis;
- perspectiva sem distorção extrema.

## Limites
- O gerador de imagens não garante geometria 3D consistente em regiões não observadas.
- Mais palavras no prompt não equivalem a mais fidelidade.
- Não prometa parâmetros ou modos que a ferramenta real não exponha.
- Não use CLIs, APIs ou chaves externas apenas porque aparecem nas fontes de origem.

## Origem adaptada
Metodologia consolidada principalmente de:
- OpenAI Skills `imagegen`;
- princípios portáveis de workflows externos de geração visual avaliados pelo Arsenal.

Foram removidas dependências específicas de CLI, APIs externas e runtimes não disponíveis por padrão.
