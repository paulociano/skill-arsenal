# Avaliação: vllm-project/vllm e Mapika/decider

Data: 2026-09-27. Método: `evaluate-and-import-skill` com `skill-security-review`, `skill-builder` e verificação documental. Fontes consultadas no GitHub: [vLLM](https://github.com/vllm-project/vllm), commit `924707f1bf94ff583d89bff7522ee12ff032c286`; [decider](https://github.com/Mapika/decider), commit `a5120cce45b9ff70964fac54ea6e8c1ac5b08c7f`.

## vLLM

O vLLM é um runtime/servidor de inferência de alto throughput, com continuous batching, gerenciamento eficiente de KV cache por PagedAttention, prefix caching, CUDA/HIP graphs, quantização, paralelismo e APIs compatíveis com OpenAI. A documentação atual também descreve structured outputs por choice, regex, JSON, grammar e structural tags.

**Classificação: D — skill técnica.** Não criar uma skill vLLM: a implementação depende de GPU/CPU, versão do PyTorch, modelo, tokenizer, backend e configuração de serving. O valor incremental entra nos owners existentes:

- `ml-production-engineering`: warmup, buckets, separação de load/prefill/decode, métricas de throughput e latência, admission control, backpressure, cancelamento e limites de fila;
- `model-routing-gateway`: vLLM como deployment possível, batching/prefix cache, compatibilidade de API, ambientes separados e hardening de servidor;
- `structured-output-contract`: structured output do provider continua sujeito a validação semântica e verificação por versão.

A documentação oficial alerta que API key não protege todos os endpoints do servidor. Portanto, um servidor vLLM deve ficar atrás de autenticação/reverse proxy adequada e passar por teste de exposição de endpoints.

## decider

O decider é um decision engine baseado em modelo causal/gerativo que responde `choice`, `score` e `noul` em uma passagem, com distribuição por opções e calibração. O repositório acrescenta:

- calibração por tipo via NLL e `temperature_by_type`;
- validação de registros de calibração, incluindo shape, `gold`, NaN, probabilidades e scores isolados;
- gates de release com holdout, regressões, ECE/NLL, slices e resultados de jogo/browser;
- servidor com limites de filas, tokens, linhas e request, respostas 413/503, batching, cache de prefixo e warmup;
- adapter `serve_vllm` que reconstrói distribuição por logprobs, temperatura e IDs de opções.

**Classificação: D — skill técnica, com valor metodológico A.** Não instalar pesos ou criar uma skill duplicada: Laya e `structured-output-contract` já cobrem decisões tipadas. Incorporar a disciplina de calibração, release gates e serving nos owners existentes.

## Segurança e portabilidade

**Metodologia adaptada: APPROVE. Produtos/runtime: CAUTION.** A avaliação não executou código, instaladores, servidores, pesos ou kernels dos repositórios. vLLM e decider podem baixar modelos, reservar grande memória de GPU e expor APIs HTTP. O adapter de logprobs exige teste de normalização, temperatura, cardinalidade de opções e arredondamento no runtime efetivo.

Structured output garante forma sintática, não verdade semântica. Confidence calibrada ordena decisões, mas não cria autorização para uma ação externa. Promover automação apenas após shadow, holdout rotulado, canary, fallback e rollback.

## Mudanças aplicadas

- `skills/ml-production-engineering/SKILL.md`: serving de alto throughput e gates de benchmark comparável;
- `skills/model-routing-gateway/SKILL.md`: vLLM como deployment, prefix cache, backpressure, compatibilidade e hardening;
- `skills/structured-output-contract/SKILL.md`: calibração por tipo e compatibilidade de APIs;
- este registro em `evaluations/`.

Não foram criadas novas skills, não foram adicionadas dependências globais e não houve instalação de vLLM ou decider no ambiente atual.
