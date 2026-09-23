# Avaliação: freeCodeCamp/freeCodeCamp

Data: 2026-09-23. Método: `evaluate-and-import-skill` + `skill-security-review`.

Fonte: https://github.com/freeCodeCamp/freeCodeCamp  
Revisão observada: `d220f1834638e4fcb0013323a9e4ffd1026100e4`.

## Classificação

**B — boa metodologia.**

O repositório é principalmente uma plataforma educacional e um currículo massivo, não uma skill reutilizável pronta. A parte de maior valor para o Arsenal é pedagógica: progressão por múltiplos formatos de prática e avaliação, culminando em projetos e exames antes de certificações.

Não foi criada uma nova skill `freecodecamp`. O ganho foi incorporado à skill canônica `teach`.

## O que faz de verdade

O freeCodeCamp combina:

- currículo self-paced;
- milhares de coding challenges;
- lições interativas;
- workshops e labs;
- páginas de revisão;
- quizzes;
- projetos obrigatórios;
- exames;
- certificações verificáveis.

No código, o currículo possui estrutura própria, schemas de challenges, challenge types e testes/linters para validar conteúdo e comportamento.

## Valor adicional para o Arsenal

A skill `teach` já cobria missão, retrieval practice, spacing, interleaving, reconstrução de sistemas e prática algorítmica.

O delta útil do freeCodeCamp é reforçar a diferença entre:

- completar conteúdo;
- praticar;
- recuperar conhecimento;
- demonstrar domínio por avaliação;
- integrar competências em projeto;
- emitir claims fortes de progresso/certificação apenas com evidência compatível.

Isso foi incorporado como **Progressão por domínio demonstrado**, com escada adaptável:

`lesson → practice → review/retrieval → quiz/check → lab/project → assessment → progression`.

A sequência não é obrigatória em toda sessão; deve ser usada proporcionalmente ao objetivo.

## Mudança aplicada

Atualizada:

- `skills/teach/SKILL.md`

Adicionado:

- gate explícito de evidência antes de marcos importantes;
- distinção entre “completou atividades” e “demonstrou domínio”;
- projeto integrador com critérios observáveis;
- revisão direcionada após erros de avaliação;
- regra de que quiz e projeto medem competências diferentes;
- claim forte de certificação exige evidência mais forte.

A `description` da skill não mudou materialmente, então o `ARSENAL INDEX.md` não precisou ser alterado.

## Segurança e portabilidade

**Metodologia: APPROVE.  
Execução da plataforma/repositório: CAUTION, desnecessária para esta adoção.**

Não foi executado código do freeCodeCamp, não foram instaladas dependências e nenhum conteúdo curricular foi copiado.

A revisão foi read-only e focada em:

- README;
- estrutura de `curriculum/`;
- schemas;
- challenge types e testes localizados via busca;
- commit mais recente observado.

O software do projeto usa BSD-3-Clause, enquanto os recursos educacionais em `/curriculum` têm termos próprios de copyright. Por isso, o Arsenal absorveu apenas a metodologia abstrata e registrou provenance, sem redistribuir conteúdo didático.

## Decisão final

Adotar a metodologia como melhoria de `teach`, não como nova skill.

O freeCodeCamp permanece uma excelente fonte de referência para desenho curricular, exercícios e progressão baseada em evidência, mas não vira dependência nem fonte canônica do Arsenal.
