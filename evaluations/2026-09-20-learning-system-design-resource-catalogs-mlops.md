# Avaliação em lote — algoritmos, learning-by-building, system design, diretórios de recursos e MLOps

Data: 2026-09-20

## Fontes

- https://github.com/thealgorithms
- https://github.com/codecrafters-io/build-your-own-x
- https://github.com/ripienaar/free-for-dev
- https://github.com/donnemartin/system-design-primer
- https://github.com/public-apis/public-apis
- https://github.com/btw-so/open-source-alternatives
- https://github.com/GokuMohandas/Made-With-ML

Fluxo: evaluate-and-import-skill + skill-security-review.

Nenhum tutorial, installer, serviço externo, API ou código das fontes foi executado.

## Decisão

- Criar system-design-engineering.
- Criar ml-production-engineering.
- Atualizar teach com reconstruction-based learning e prática algorítmica.
- Tratar free-for-dev, public-apis e open-source-alternatives apenas como diretórios de discovery.
- O link TheAlgorithms aponta para uma organização; TheAlgorithms/Python foi usado como amostra representativa, sem assumir que um único repo representa integralmente a organização.

## Avaliações

### TheAlgorithms
Classificação B/C como fonte pedagógica agregada. Coleção ampla de implementações de algoritmos em vários idiomas. Valor maior como exercícios, exemplos e comparação de complexidade do que como skill operacional. Segurança APPROVE para leitura; código individual ainda deve ser tratado como fonte externa. Decisão: reforçar teach, não importar código.

### build-your-own-x
Classificação B. Curadoria de tutoriais de reconstrução de tecnologias como databases, browsers, VMs, shells e renderers. Valor pedagógico alto: compreender abstrações pela implementação mínima e aumentar fidelidade progressivamente. Segurança APPROVE como índice, mas links são terceiros e exigem avaliação própria. Decisão: adaptar em teach.

### free-for-dev
Classificação C/B. Diretório curado de serviços com free tiers. Útil para discovery, mas preços, quotas, termos e disponibilidade mudam e precisam ser verificados na fonte oficial antes de recomendação. Não vira skill nem autoridade.

### system-design-primer
Classificação A/B. Metodologia clara de requirements → high-level design → core components → scale, com trade-offs de sistemas distribuídos. O Arsenal tinha visualização e complexidade, mas não uma skill operacional de system design. Decisão: criar system-design-engineering, atualizando o método com SLOs, failure modes e operação.

### public-apis
Classificação C/B. Catálogo comunitário de APIs públicas. Útil para descoberta inicial, mas auth, CORS, pricing, SLA, terms e status precisam ser confirmados na documentação oficial. Não vira skill.

### open-source-alternatives
Classificação C/B. Catálogo de alternativas open source a produtos SaaS. Útil para ampliar candidates, não para seleção final. Stars e presença na lista não provam adequação, manutenção ou segurança. Não vira skill.

### Made-With-ML
Classificação A/B. Curso + implementação end-to-end de sistemas de ML com data, training, evaluation, serving, testing, CI/CD e continual learning. O Arsenal possuía experiment-design e observability específica de LLM, mas faltava workflow geral de ML production. Decisão: criar ml-production-engineering adaptada e vendor-neutral.

## Segurança

Não foram identificados motivos para executar código durante a avaliação. Made-With-ML inclui dependências, cloud/Anyscale e credentials de ambiente; nenhuma foi usada. Diretórios de links não transferem confiança para os destinos listados.

## Mudanças aplicadas

- nova skill system-design-engineering;
- nova skill ml-production-engineering;
- teach atualizado com learning-by-building e algoritmo como prática;
- ARSENAL INDEX atualizado;
- registro desta avaliação.

## Limites

- revisão manual;
- nenhum tutorial ou benchmark foi reproduzido;
- condições de serviços/free tiers não foram validadas porque não são incorporadas como comportamento operacional do Arsenal.
