---
name: llm-observability-evaluation
description: "Instrumentar e avaliar aplicações LLM com traces, datasets, métricas e comparações reproduzíveis entre versões."
---

# llm-observability-evaluation

## Objetivo

Instrumentar, observar e avaliar aplicações LLM com traces, datasets, métricas e experimentos reproduzíveis, conectando falhas de produção a ciclos de melhoria pré-deploy e pós-deploy.

## Princípio central

**Sem traces e datasets, debugging de LLM vira anedota.**

## Quando usar

- agentes ou workflows com múltiplos passos;
- produção com custo/latência/qualidade variável;
- necessidade de debugging;
- comparação de prompts/modelos;
- criação de evals;
- regressão pré-deploy;
- feedback humano/usuário;
- rastreabilidade de retrieval, tool calls e model calls.

## Modelo de observação

Cada execução relevante deve, quando o ambiente permitir, conectar:

- input;
- prompt/version;
- model/provider/config;
- retrieval context;
- tool/action spans;
- output;
- latency;
- token/cost metadata;
- error;
- user/session;
- evaluation score/feedback.

## Workflow

1. **Instrument** — definir traces/spans nos boundaries que ajudam a explicar comportamento.
2. **Capture version** — registrar versão de prompt, workflow e modelo/config relevantes.
3. **Build datasets** — transformar casos reais representativos em datasets de avaliação.
4. **Define metrics** — separar métricas objetivas, code evaluators, human labels e LLM-as-judge.
5. **Baseline** — medir versão atual antes de alterar.
6. **Experiment** — comparar mudanças com o mesmo dataset/metric.
7. **Slice failures** — agrupar por modelo, versão, tipo de query, ferramenta, tenant, idioma ou outra dimensão relevante.
8. **Production feedback** — incorporar exemplos ruins de traces reais ao dataset.
9. **Gate** — só promover mudança quando o ganho é material e não há regressão crítica.
10. **Monitor drift** — observar mudanças de distribuição, custo, latência e qualidade ao longo do tempo.

## Precommit de previsões e settlement

Quando o sistema faz uma previsão, score de confiança ou recomendação que só poderá ser julgada depois:

- registrar **antes do outcome** a previsão, probabilidade/confidence, timestamp e versão do sistema;
- tornar esse registro append-only ou pelo menos auditável, sem sobrescrever a chamada original após conhecer o resultado;
- liquidar/avaliar o outcome em evento separado usando uma regra definida previamente;
- manter casos ainda abertos separados de wins/losses; não escolher retrospectivamente a melhor janela de avaliação;
- quando houver probabilidade, preferir proper scoring rules como Brier/log loss além de hit rate;
- publicar misses e denominador completo, não apenas exemplos positivos;
- distinguir o fato observado que disparou a chamada da previsão inferida sobre o que acontecerá depois.

Esse padrão reduz hindsight bias e métricas que ficam melhores apenas porque o sistema escolheu retrospectivamente como se avaliar.

## Regras para evals

- LLM-as-a-judge é uma métrica, não verdade absoluta;
- quando possível, combinar judge com checks determinísticos e/ou labels humanos;
- o judge precisa de rubric explícita;
- não avaliar com exatamente o mesmo contexto que contaminou a geração quando isso cria leakage;
- separar offline eval de online/user feedback;
- uma média boa pode esconder um segmento ruim: usar slices;
- dataset de avaliação deve incluir edge cases e failures reais, não só exemplos felizes.

## Prompt management

Se prompts forem versionados:

- vincular trace à versão usada;
- não alterar prompt de produção sem conseguir comparar antes/depois;
- separar conteúdo estável de configuração dinâmica;
- cache/registry não substitui source control quando o prompt faz parte do comportamento crítico.

## Privacidade e segurança

- traces podem conter PII, secrets e conteúdo sensível;
- redigir/maskear antes de exportar;
- definir retenção;
- limitar acesso por projeto/tenant;
- não enviar traces a SaaS externo sem política de dados compatível;
- self-hosting reduz alguns riscos de transferência, não elimina governança.

## Artefatos de avaliação

Um eval operacional deve manter artefatos separados:

- **dataset input**;
- **trace gerado**;
- **grade/result**;
- **analysis/failure cluster**;
- **candidate change**;
- **comparison baseline vs candidate**.

Para multi-turn agents, avaliar resultado e trajetória separadamente. Tool-use quality não é equivalente a final-response quality. Grounding/safety também devem permanecer eixos independentes.

Depois de uma correção, comparar resultados novos com baseline e verificar regressões em métricas não-alvo. Casos reais de produção com falha devem alimentar o dataset, mas sem contaminar o holdout.

## Ferramentas e dependências

Usar Langfuse, OpenTelemetry, tracing próprio ou outro sistema real quando conectado ao projeto. Não presumir que esta conversa tem acesso a traces de produção. Sem instrumentação, fornecer plano de observabilidade/evals e não inventar métricas.

## Integração

Combina com `empirical-prompt-tuning`, `model-routing-gateway`, `retrieval-quality-engineering`, `structured-output-contract` e `verify-before-claim`.

## Avaliar compressão de contexto

Quando testar filtros de saída de ferramentas ou compressão de prompts:
1. Definir o denominador: bytes de uma saída, tokens de entrada completos, tokens de saída ou custo total da sessão. Não converter redução de bytes em economia de faturamento.
2. Comparar os mesmos casos, modelo e configuração; medir qualidade da resposta e das ações, latência total, chamadas de recuperação, retries e custo, além da taxa de compressão.
3. Incluir casos com falha rara no meio do log, negações, números exatos, dados repetitivos, código sob revisão e conteúdo já compacto. Verificar que a evidência decisiva sobrevive.
4. Preservar original recuperável com origem e versão, retenção e acesso definidos quando o sistema suportar. Testar recuperação real, inclusive cache expirado; um identificador sem original disponível não torna a compressão reversível.
5. Manter conteúdo original quando houver erro de parsing, ganho insignificante ou risco de remover informação necessária. Não descartar instruções, restrições ou exceções para melhorar uma métrica.
6. Separar efeito de compressão, cache, redução de verbosidade e alteração de esforço do modelo. Não mudar vários fatores e atribuir o ganho a apenas um.
7. Reportar estimativas como estimativas; usar contagem do provedor/tokenizador adequado quando disponível. Isolar baseline de hooks, plugins ou regras da candidata para evitar comparação contaminada.

Compressão local não elimina exposição por proxy upstream, telemetria, memória compartilhada ou armazenamento de logs. Avaliar esses fluxos separadamente. Não instalar wrappers, modificar arquivos de instruções, registrar MCP global ou mudar endpoint/esforço por padrão. Esta skill avalia uma integração real do projeto; não reconfigura a conversa atual.

Síntese de [RTK](https://github.com/rtk-ai/rtk/blob/b748a5f75563f410103551689097650be7210d99/docs/guide/resources/savings-explained.md), [Headroom](https://github.com/headroomlabs-ai/headroom/blob/89a58fd1526ba158a1614c35e455e1af0a7033c0/README.md) e da [disciplina de comparação de i-have-adhd](https://github.com/ayghri/i-have-adhd/blob/839872f9d1cd634fed642b4589ce7226199cc15f/evals/README.md). Não depende desses runtimes nem adota seus percentuais como garantia.

## Referências

Adaptada de langfuse/langfuse.

Precommit e settlement de previsões adaptados de [dealerdefi/FLYON](https://github.com/dealerdefi/FLYON), usando a metodologia de scoreboard auditável sem incorporar lógica financeira ou on-chain.

Origem local: [llm-observability-evaluation.docx](../llm-observability-evaluation.docx).
