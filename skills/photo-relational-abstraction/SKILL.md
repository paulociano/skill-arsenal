---
name: photo-relational-abstraction
description: "Analisar uma fotografia fornecida, extrair relações visuais observáveis e reconstruí-las como composição abstrata não literal, preservando invariantes espaciais sem aplicar style transfer à foto original."
---

# photo-relational-abstraction

## Objetivo

Transformar uma fotografia do usuário em uma abstração editorial não literal baseada em evidência visual: massas, eixos, contagens, intervalos, direções, profundidade, cores funcionais e espaço negativo.

## Quando usar

- quando o usuário quer uma abstração visual derivada de uma fotografia;
- quando é importante preservar relações e ritmo espacial sem redesenhar literalmente a cena;
- para estudos editoriais, pôsteres, painéis ou composições minimalistas guiadas por uma foto real.

Não usar para simples filtro, posterização, vetorização ou style transfer. Para edição fotográfica direta, usar `high-fidelity-image-generation`.

## Princípio central

A abstração deve carregar a **identidade relacional** da fotografia, não sua superfície.

## Workflow

1. **Lock source** — tratar a foto fornecida pelo usuário como única fonte factual da cena.
2. **Deconstruct** — inventariar somente evidência observável:
   - massa dominante;
   - axes e direções;
   - bordas/horizontes;
   - contagens e grupos;
   - intervalos e densidade;
   - overlaps e ordem de profundidade;
   - assimetrias;
   - papéis de cor;
   - vazios significativos.
3. **Distill** — eliminar textura fotográfica, detalhe menor e contorno literal. Para cada fato retido, escolher o menor mark capaz de preservá-lo.
4. **Reconstruct** — reorganizar os marks em uma composição nova, não literal, mantendo as relações que definem a foto.
5. **Generate** — usar a ferramenta de imagem disponível apenas para a abstração ou composição solicitada.
6. **Inspect** — verificar que cada elemento importante da abstração pode ser explicado por evidência da foto.
7. **Reject generic drift** — revisar se a saída virou ícone genérico, mini-ilustração da cena, filtro ou decoração sem fonte.
8. **Finalize** — quando a entrega combinar foto original + painel abstrato, preservar a foto original sem alteração e compor deterministicamente quando o ambiente permitir.

## Invariantes relacionais

Preservar quando relevantes:

- dominante vs secundário;
- esquerda/direita e acima/abaixo;
- direção de fluxo;
- grupos de contagem;
- gaps e clusters;
- overlap;
- profundidade;
- assimetria;
- proporções relativas;
- posição de grandes vazios.

Coordenadas exatas não são obrigatórias. Compressão, deslocamento, sobreposição e escala podem mudar se tornarem as relações mais legíveis.

## Regra evidence-to-mark

Para cada mark relevante, conseguir formular:

`evidência observada → relação preservada → mark escolhido`

Se não houver origem visual clara, remover o elemento.

## Negative space

Espaço vazio é parte da composição. Não preencher automaticamente áreas livres com textura, ornamento, labels ou efeitos. Preservar grandes vazios quando eles forem estruturais na foto ou necessários para manter hierarquia.

## Referências de estilo

Referências externas podem orientar linguagem de marks, densidade e composição, mas:

- não substituem a foto como fonte factual;
- não autorizam copiar objetos ou conteúdo;
- não devem alterar a fotografia original;
- devem ser usadas pela lógica estrutural, não por imitação literal.

## QA

Verificar:

- fidelidade às relações observadas;
- ausência de conteúdo inventado;
- contagens e grupos importantes;
- direções;
- dominância e escala relativa;
- uso intencional do espaço negativo;
- abstração suficientemente não literal;
- ausência de style transfer acidental;
- coerência de cor quando cores da fonte carregam informação.

## Limites

- uma abstração não preserva todo o conteúdo da fotografia;
- relações ocultas ou objetos ocluídos não devem ser reconstruídos por suposição;
- geração visual pode introduzir elementos não pedidos; inspecionar e iterar;
- composição pixel-exata exige ferramenta determinística real, não apenas geração de imagem.

## Integração

Combina com `high-fidelity-image-generation`, `design-direction`, `editable-visual-design`, `typographic-composition` e `verify-before-claim`.

## Origem metodológica

Adaptada de https://github.com/Evianis/travel-photo-abstraction, preservando deconstruct → distill → reconstruct e source-evidence-to-mark. A versão do Arsenal remove scripts, layouts, microtipografia, biblioteca visual e restrições de distribuição específicas da fonte.
