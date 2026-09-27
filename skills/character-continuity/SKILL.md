---
name: character-continuity
description: Manter personagens recorrentes visualmente on-model ao longo de páginas, cenas ou séries usando bíblia de identidade, atlas/referências, seleção da referência mais próxima e QA de continuidade.
---

# Character Continuity

## Objetivo
Controlar continuidade de personagens em produção visual seriada. Esta skill é dona do estado de identidade entre imagens; high-fidelity-image-generation continua dona da execução de cada geração/edição.

## Quando usar
- ebook, HQ, storybook ou série com personagem recorrente;
- personagem muda rosto, proporção, roupa, cores ou marcas entre cenas;
- criação de character bible, reference sheet ou atlas;
- revisão de continuidade entre páginas já geradas.

Não use para uma única imagem sem continuidade futura.

## Contrato de identidade
Registre somente traços observáveis que precisam persistir:
- silhueta e proporções;
- rosto/cabelo ou anatomia;
- cores e materiais;
- roupa e acessórios persistentes;
- marcas distintivas;
- escala relativa entre personagens;
- elementos variáveis autorizados;
- falhas históricas conhecidas.

Separe identidade de estilo, pose e cenário.

## Escada de controle
Comece no mecanismo mais leve suficiente:
1. regras corretivas curtas;
2. imagem mestre ou atlas;
3. pequena biblioteca de referências por pose/ângulo/expressão;
4. pipeline em estágios quando composição complexa derruba identidade;
5. treinamento/fine-tuning apenas quando houver infraestrutura real e os níveis anteriores falharem.

Nunca prometa dataset, LoRA, fine-tune ou roteamento externo sem runtime disponível.

## Workflow
1. Inventariar assets existentes.
2. Criar ou atualizar a bíblia de identidade.
3. Se houver referências suficientes, montar um atlas com frente, 3/4, perfil, corpo inteiro e expressões úteis ao projeto.
4. Para cada cena, selecionar a referência mais próxima em pose, enquadramento e expressão. Não usar todas por padrão.
5. Delegar a geração para high-fidelity-image-generation, descrevendo principalmente o delta da referência.
6. Comparar o resultado com a bíblia e com páginas adjacentes.
7. Registrar drift observado.
8. Corrigir no nível mais barato: regra → referência melhor → edição localizada → mudança de pipeline.
9. Só escalar a complexidade quando a falha for repetível.

## Continuity QA
Verifique identidade, proporções, roupa/acessórios, cores, marcas distintivas, lateralidade quando importante, escala entre personagens e coerência com páginas adjacentes.

Mudanças narrativamente intencionais não são drift. Registre-as como estado da história.

## Estado narrativo
Quando aparência muda durante a história, mantenha uma linha do tempo simples: personagem → página/cena → mudança autorizada → novo estado.

## Critério de conclusão
Os traços invariantes permanecem reconhecíveis nas cenas necessárias e qualquer mudança relevante pode ser explicada pelo estado narrativo, não por drift do gerador.

## Origem adaptada
Metodologia consolidada de GenielabsOpenSource/style-consistency-ai, kart-io/picture-skills, jmilinovich/comicgen e StoryFox. Foram preservados atlas, closest-reference, character sheets, delta prompting e continuity checks; dependências específicas de modelos, APIs, scripts, Claude Code e treinamento foram removidas.
