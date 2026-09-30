---
name: viral-motion-explainer
description: "Criar vídeos explicativos verticais curtos como pipeline de hook, roteiro, direção mixed-media, keyframes e prompts de motion por cena, com execução por etapas ou ponta a ponta."
---

# Viral Motion Explainer

## Objetivo

Transformar um tema curto em um explainer vertical de 10–30 segundos com narrativa de alta retenção, direção visual editorial mixed-media, keyframes por cena e especificação de motion suficientemente precisa para geração ou produção posterior.

## Quando usar

Use quando o pedido envolver criar um Reel/Short/TikTok explicativo com linguagem visual de motion design, especialmente quando o usuário quiser o pacote completo: ideia, roteiro, direção visual, imagens-chave e animação.

Não use apenas para editar um vídeo existente; nesse caso prefira `video-editing-pipeline`. Para apenas escrever um Reel, `reels-scripting` pode bastar. Para direção cinematográfica sem este formato editorial específico, use `cinematic-visual-direction`.

## Pipeline

### 1. Ideia e hook

Quando o tema ainda não estiver definido, proponha poucas ideias fortes. Prefira ângulos como verdade escondida, contraste, erro comum, mecanismo invisível, custo oculto ou reframe contraintuitivo.

Se o tema já estiver definido, não force uma etapa de ideação.

### 2. Roteiro

Produza narração de 10–30 segundos, normalmente em segunda pessoa ou enquadramento direto ao assunto.

Estrutura recomendada:
1. hook curto;
2. contraste ou quebra da interpretação óbvia;
3. mecanismo central em linguagem simples;
4. exemplo, metáfora ou consequência concreta;
5. insight;
6. fechamento memorável que ecoe o hook.

Use frases curtas. Quebre sentenças longas em beats. Evite jargão sem explicação.

### 3. Direção visual

Defina uma direção visual única antes de gerar cenas. A referência-base desta skill é editorial mixed-media de alto contraste:
- fundo neutro dominante;
- grid modular discreto;
- um accent color dominante por sequência;
- objetos 3D/fotográficos combinados com recortes halftone, vetores e planos 2.5D;
- tipografia cinética com sans-serif bold e contraste editorial serif/italic quando útil;
- profundidade por sombras, parallax e planos Z;
- composição 9:16 com safe zone central.

Não trate esses elementos como checklist obrigatório. Preserve coerência e legibilidade acima da ornamentação.

### 4. Storyboard / keyframes

Converta cada beat relevante do roteiro em uma cena. Para cada cena, defina:
- linha de narração;
- função narrativa;
- hero object principal;
- no máximo poucos accents de apoio;
- texto de impacto, preferencialmente 1–4 palavras;
- composição e profundidade;
- transição de entrada e saída.

Quando imagens forem realmente geradas, use `high-fidelity-image-generation` e preserve invariantes visuais entre cenas.

### 5. Motion specification

Para cada cena, escreva uma especificação temporal. A referência original usa cenas de 6 segundos; adapte a duração quando o roteiro ou ferramenta exigir.

Modelo de 6 s:
- 0.0–0.5 s: base limpa, ambiente já vivo;
- 0.5–3.5 s: entrada cinética, construção de hierarquia e texto;
- 3.5–4.7 s: hold com micro-motion e profundidade;
- 4.7–6.0 s: saída e preparação da próxima transição.

Preferir ease-out pesado, pequeno settling/overshoot, motion blur natural, parallax discreto e câmera estável com push/pull sutil. Evitar transições lineares, shake caótico e movimento decorativo sem função.

### 6. Som

Quando aplicável, especifique SFX discretos ligados às ações: whoosh de papel, UI click, thud suave, air swell. Não invente trilha ou voice-over quando o pedido explicitamente excluir esses elementos.

## Modos de execução

### Guided
Use quando o usuário quiser escolher direção em cada etapa. Pare somente nos gates que mudam materialmente o resultado, por exemplo escolha do tema, roteiro ou direção visual.

### End-to-end
Se o usuário pedir "faça completo", "execute tudo" ou equivalente, percorra o pipeline sem exigir confirmações intermediárias. Tome decisões reversíveis e entregue o pacote final.

## Contrato de saída

Quando útil, entregue por cena:
- `Scene N`
- `Narration`
- `Narrative purpose`
- `Keyframe prompt`
- `Typography`
- `Motion`
- `Camera`
- `Transition`
- `SFX`

Não prometa render ou execução em ferramenta externa sem capacidade real disponível.

## Combinações

- `reels-scripting`: roteiro quando a narrativa precisar de refinamento específico.
- `cinematic-visual-direction`: composição, câmera e continuidade.
- `high-fidelity-image-generation`: geração/edição real dos keyframes.
- `typographic-composition`: hierarquia tipográfica mais sofisticada.
- `procedural-film`: quando a entrega deve ser um filme procedural reproduzível.
- `video-editing-pipeline`: quando já existe footage a editar.

## Critérios de qualidade

- o hook cria tensão ou curiosidade sem clickbait enganoso;
- cada cena tem função narrativa clara;
- texto na tela é curto e legível em mobile;
- visual e motion reforçam a ideia, não competem com ela;
- continuidade de palette, grid, tipografia e profundidade;
- prompts não dependem de ferramentas inexistentes;
- duração total e número de cenas são compatíveis.

## Proveniência

Adaptada do documento fornecido pelo usuário **“Aiplaybook: How to Create Viral Motion Explainer Videos Using AI (Free)”**. A fonte original permanece como referência metodológica privada; o Arsenal contém somente a adaptação operacional, não uma reprodução integral.
