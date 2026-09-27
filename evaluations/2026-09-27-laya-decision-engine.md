# Avaliação: NandhaKishorM/laya

Data: 2026-09-27. Fonte canônica consultada: [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya), commit `4066d5d5fbf08b66c6757ddeedbd797bd7655bc0`. Método: `evaluate-and-import-skill` com `skill-security-review`, `skill-builder` e validação real proporcional.

## O que a fonte faz

Laya é um motor de decisões tipadas, não autoregressivo, que responde em uma passagem a perguntas `choice`, `score` e `noul` (probabilidade de sim). Expõe `Router` para escolher checkpoint por idioma e oferece projeção de JSON Schema/Pydantic em `laya/structured.py`. O repositório também documenta hooks, calibração, batching, serving HTTP/MCP e adoção gradual em modo shadow antes de promover decisões.

Dependências reais observadas: Python >=3.10, PyTorch, Transformers, safetensors, Hugging Face Hub e pesos de checkpoint. Os resultados e a velocidade dependem de hardware, dtype, tamanho do estado, número de perguntas e aquecimento.

## Classificação e decisão

**Classe D — skill técnica**, com **valor metodológico A/B** para o Arsenal.

Não importar o runtime como dependência global nem transformar o Arsenal em um classificador autônomo. Incorporar o núcleo útil em owners existentes:

- `decision-analysis`: via curta de decisões tipadas, critérios, desconhecido, evidência, trade-offs e escalonamento para análise completa;
- `structured-output-contract`: domínio fechado, enum/escala/booleano, validação após projeção, incerteza e runtime opcional;
- `arsenal-router`: triagem de candidatas sem carregar o catálogo inteiro, com fallback para raciocínio do assistente e regra de que decisão do modelo não autoriza execução.

Criar uma nova skill separada duplicaria esses owners. O runtime fica disponível como referência e script opcional quando o usuário pedir instalação ou benchmark.

## Segurança e portabilidade

**Parecer para a metodologia adaptada: APPROVE.** **Parecer para instalação do produto: CAUTION.** A revisão foi documental e não executou instaladores ou código arbitrário do repositório; o benchmark usou o pacote publicado e um snapshot de pesos identificado.

A instalação baixa dependências grandes e pesos externos. O modelo retorna evidência probabilística, não autorização para executar ações. Adoção segura exige shadow, comparação com dados revisados, limiar validado, fallback, canary e rollback. Não registrar PII em benchmarks ou hooks sem política própria.

## Validação real realizada

Ambiente temporário: Python 3.12.14, x86_64, CPU, sem GPU NVIDIA detectável. Pacote instalado: `laya==0.3.20`, `torch==2.14.0`, `transformers==5.17.0`, `huggingface-hub==1.33.0`; `pip check` passou. Checkpoint: `convaiinnovations/laya-multilingual`, revisão Hugging Face `e4e9ddf21a7b1903b7acffd8814ad4307bf63a67`.

Benchmark smoke com três frases sintéticas em português, uma pergunta por request, batch 1, duas rodadas de aquecimento e 15 requests medidos:

| Threads CPU | Mediana | P95 | Acertos nos 3 casos |
| ---: | ---: | ---: | ---: |
| 4 | 107,1 ms | 123,9 ms | 10/15 |
| 8 | 89,4 ms | 111,2 ms | 10/15 |

A carga inicial foi aproximadamente 40,2 s na primeira execução e 9,0 s na segunda, com cache local. O terceiro caso foi classificado como `other` em vez de `decision`, mostrando que confiança/latência não substituem conjunto avaliado. Este teste não é uma avaliação de acurácia nem autoriza roteamento autônomo.

## Arquivos alterados

- `skills/decision-analysis/SKILL.md` e `references/typed-decisions.md`;
- `skills/structured-output-contract/SKILL.md`, `references/laya-runtime.md` e `scripts/laya_decisions.py`;
- `skills/arsenal-router/SKILL.md`;
- `ARSENAL INDEX.md` e este registro.

Nenhuma dependência, checkpoint, servidor ou integração externa é adicionada ao Arsenal publicado. O script opcional cria ambiente e execução somente quando chamado pelo usuário ou por uma tarefa autorizada.
