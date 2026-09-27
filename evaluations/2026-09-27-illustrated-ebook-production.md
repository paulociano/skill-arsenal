# Avaliação: produção de ebooks ilustrados

Data: 2026-09-27

## Objetivo
Ampliar o Arsenal para criação de personagens persistentes, histórias em quadrinhos, livros infantis e guias educativos/saúde.

## Fontes avaliadas
- GenielabsOpenSource/style-consistency-ai
- kart-io/picture-skills
- JimLiu/baoyu-skills (baoyu-comic)
- jmilinovich/comicgen
- jakerains/StoryFox

## Capability ledger

| Fonte | Capability | Classe | Decisão | Owner |
|---|---|---|---|---|
| style-consistency-ai | escada de consistência, atlas, closest reference, delta prompting | A | CREATE_NEW + ABSORB | character-continuity |
| picture-skills | age-driven picture book + consistency lock | A/D | ABSORB_METHOD_ONLY | stack + writing owners |
| baoyu-comic | análise → storyboard → personagens → prompts → páginas | A/D | CREATE_NEW | educational-comic |
| comicgen | estrutura por projeto, character refs, páginas, PDF | A/D | ABSORB_METHOD_ONLY | educational-comic + stack |
| StoryFox | geração em duas passagens, character sheet, export | B/D | ABSORB_METHOD_ONLY | illustrated-ebook-production |

## Overlap resolvido
high-fidelity-image-generation continua owner da execução de imagens e de invariantes dentro de uma geração. character-continuity mantém estado, referências e QA entre gerações.

explanation-architecture, eli5, plain-writing, editable-visual-design e evidence-claim-verification permanecem owners de arquitetura explicativa, adaptação de linguagem, clareza, composição visual e verificação de claims. Por isso não foi criada uma skill genérica de livro ilustrado nem uma skill médica editorial.

## Segurança e portabilidade
Não foram importados installers, Bun/Node/Python dos projetos, chaves Gemini/Hugging Face, scripts de merge, Claude Code/EXTEND.md, backends/modelos externos ou treinamento/fine-tuning como capacidade presumida.

## Prova incremental
Should trigger:
1. Crie um ebook infantil de 16 páginas mantendo os mesmos personagens.
2. Transforme a história do Césio-137 em HQ educativa para crianças.
3. Os personagens mudaram de rosto entre as páginas, corrija a continuidade.
4. Faça um guia ilustrado de saúde para leigos com fontes verificadas.

Near miss:
1. Gere uma imagem de uma menina astronauta → high-fidelity-image-generation.
2. Explique radiação para uma criança → eli5/explanation-architecture.
3. Crie a capa de um ebook → editable-visual-design/high-fidelity-image-generation.

## Acceptance case
Césio-137 infantil foi escolhido porque exige simultaneamente fidelidade histórica, adaptação etária, narrativa, personagens recorrentes, sensibilidade visual e composição editorial.

## Resultado
- CREATE_NEW: character-continuity
- CREATE_NEW: educational-comic
- CREATE_NEW stack: illustrated-ebook-production
- ABSORB_METHOD_ONLY: picture-skills, comicgen, StoryFox
- REJECT runtime assumptions: ferramentas, instaladores, APIs e scripts externos não disponíveis por padrão.
