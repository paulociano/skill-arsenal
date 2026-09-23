---
name: visual-explanation-sketch
description: "Transformar conceitos, processos e relações em esboços visuais simples com caixas, setas, agrupamentos, anotações e destaques para facilitar compreensão."
---

# visual-explanation-sketch

## Objetivo

Criar explicações visuais leves, mais próximas de quadro branco ou caderno do que de diagrama técnico formal, para tornar relações e progressões compreensíveis rapidamente.

## Quando usar

- explicar conceitos, decisões, trade-offs ou sequências;
- esboçar uma ideia antes de um artefato final;
- materiais educacionais e posts;
- quando um diagrama formal seria pesado demais;
- quando o usuário pede sketch, rascunho visual, mapa simples ou explicação desenhada.

## Vocabulário visual

- caixas para entidades/ideias;
- setas para fluxo ou relação;
- agrupamentos para afinidade;
- brackets para escopo;
- círculos/sublinhados para foco;
- pequenos ícones quando reduzem texto;
- notas marginais para ressalvas;
- numeração para progressão;
- contraste de peso/tamanho antes de cor.

## Workflow

1. Definir a ideia central em uma frase.
2. Extrair 3–7 elementos indispensáveis.
3. Escolher uma narrativa espacial:
   - esquerda → direita para processo;
   - cima → baixo para hierarquia/progressão;
   - centro → bordas para mapa conceitual;
   - antes/depois para comparação.
4. Desenhar o caminho principal primeiro.
5. Adicionar apenas relações secundárias necessárias.
6. Usar anotações para chamar atenção, não para preencher espaço.
7. Se o sketch virar técnico, encaminhar para architecture-visualization.
8. Se virar peça final de campanha/social, encaminhar para editable-visual-design.
9. Verificar se o sketch continua compreensível em preto e branco e sem animação.

## Hand-drawn style

Uma aparência de traço livre pode ser usada para:
- comunicar rascunho/processo;
- reduzir formalidade;
- destacar partes;
- diferenciar anotação de conteúdo principal.

Não usar hand-drawn automaticamente. O estilo deve servir à intenção.

## Implementação

Quando o ambiente permitir, o sketch pode ser produzido em SVG/HTML/canvas ou ferramenta visual disponível. Rough.js/Rough Notation/Perfect Freehand são referências técnicas possíveis, não dependências obrigatórias.

## Regras

- Não usar setas sem direção/semântica clara.
- Não colocar texto longo dentro de shapes pequenos.
- Não transformar toda relação em linha.
- Um sketch explica uma ideia; não precisa capturar o sistema inteiro.
- A estética "desenhada à mão" não substitui hierarquia.

## Integração

explanation-architecture, eli5, teach, editable-visual-design, architecture-visualization e presentation workflows.

## Origem metodológica

Adaptada de Excalidraw, tldraw, Rough.js/Rough Notation e perfect-freehand, preservando princípios de sketching e anotação visual sem exigir seus editores ou runtimes.
