# Avaliação: GitHub Stars Leaderboard — tópico ChatGPT

Data: 2026-09-23. Método: `evaluate-and-import-skill` + `skill-security-review`, com triagem por utilidade antes de leitura profunda.

Fonte de descoberta: https://githublb.vercel.app/topic/chatgpt

A página consultada informava 39 repositórios no tópico `chatgpt` e mostrava snapshot "Updated: Aug 23, 2026". Estrelas foram usadas apenas para descoberta, nunca como proxy de qualidade ou adequação ao Arsenal.

## Decisão

**Não criar nova skill ou stack a partir deste leaderboard.**

Os candidatos tecnicamente interessantes são majoritariamente runtimes, frameworks, aplicações completas ou bibliotecas. As metodologias reutilizáveis mais valiosas já possuem owners canônicos no Arsenal. A ação útil desta rodada é registrar a avaliação e evitar duplicação.

## Triagem

| Fonte | Classe | Decisão | Owner existente / motivo |
|---|---|---|---|
| NousResearch/hermes-agent | D | não importar | `session-learn`, `retrospective-codify`, `skill-builder`, `graph-engineering`, `loop-engineering` já cobrem learning loop, skills, delegação e scheduling |
| langflow-ai/langflow | D | não importar | runtime visual de agentes/flows; `graph-engineering`, `structured-output-contract`, `llm-observability-evaluation` cobrem a metodologia |
| langchain-ai/langgraph | D | não importar | framework de agentes stateful; durable execution, HITL e graph orchestration já estão cobertos por `graph-engineering` e `loop-engineering` |
| microsoft/autogen | D | não importar | framework multiagente em maintenance mode; conceitos já cobertos e upstream direciona novos usuários para Microsoft Agent Framework |
| code-yeongyu/oh-my-openagent | D | não importar | plugin/harness opinionado para OpenCode/Codex; especialistas, fallback e tooling já mapeiam para `graph-engineering`, `model-routing-gateway`, `code-review` e skills de engenharia |
| mem0ai/mem0 | D | não importar | camada de memória; níveis de memória e provenance já em `session-learn`; hybrid retrieval/entity matching pertencem a `retrieval-quality-engineering` |
| Aider-AI/aider | D | não importar | coding agent completo; repo map, git, lint/test e edição assistida já têm owners separados no Arsenal |
| harry0703/MoneyPrinterTurbo | D | já absorvido | já é referência explícita de `video-editing-pipeline` para tema → roteiro → assets → voz → legendas → música → composição |
| f/prompts.chat | C/B | não importar | coleção de prompts; útil como corpus de referência, mas não muda comportamento operacional por si só |
| dair-ai/Prompt-Engineering-Guide | B | não importar como skill | boa base educacional; usar como fonte quando uma tarefa de prompting exigir pesquisa, sem criar owner paralelo |
| openai/openai-cookbook | B/D | não importar | cookbook técnico e version-sensitive; consultar sob demanda em vez de congelar como skill |
| rasbt/LLMs-from-scratch | B | não importar | material educacional, não workflow operacional |
| NextChat / LibreChat / Chatbox / Jan / LobeHub / Khoj / Quivr | D | não importar | aplicações/interfaces completas; avaliar como produto apenas quando houver tarefa específica |
| Flowise | D | não importar | builder/runtime visual; sobreposição alta com Langflow/LangGraph no nível metodológico |
| system_prompts_leaks / awesome prompt collections | C | descartar como skill | corpus/prompt dump, sem processo operacional suficiente |
| GPT_API_free / gpt4free e equivalentes | D | não adotar | gateways/proxies externos com risco e pouca relevância para a arquitetura canônica do Arsenal |

## Leitura aprofundada dos candidatos

### Hermes Agent

Revisão observada: `9fe737aef2dd18a351dff3c4de608d63879a6524`.

O diferencial declarado é um closed learning loop: memória persistente, criação/ajuste de skills, busca de sessões, scheduling, delegates paralelos e múltiplos backends. Isso é infraestrutura real, não uma skill textual.

O Arsenal já mantém separação mais segura entre:
- captura de aprendizado: `session-learn`;
- decisão sobre promoção: `retrospective-codify`;
- construção: `skill-builder`;
- paralelismo: `graph-engineering`;
- recorrência: `loop-engineering`.

A autonomia de autoeditar skills silenciosamente não deve ser importada. O Arsenal exige promoção supervisionada e auditável.

**Segurança:** CAUTION para execução. O README recomenda installer remoto via curl/PowerShell, instala dependências, habilita gateways e ferramentas e pode operar em vários canais. Nenhum installer foi executado.

### MoneyPrinterTurbo

Revisão observada: `3d5f4e421927d61f3eac729cf4b711ac0b69d688`.

Gera vídeo do tema até roteiro, assets, TTS, legendas, música, composição e publicação. O Arsenal já absorveu exatamente o pedaço metodológico útil em `video-editing-pipeline`, cuja seção "Modo de produção generativa" referencia MoneyPrinterTurbo explicitamente.

Não há delta suficiente para nova atualização nesta rodada.

### Oh My OpenAgent

Revisão observada: `ea4269ae59e3075af966a5c4ed342559cc850bc7`.

Traz orquestrador principal, especialistas, background agents, LSP/AST, edição ancorada, injeção de contexto, fallback de modelos e hooks. É um harness complexo e opinionado.

Os blocos portáveis já estão separados no Arsenal:
- especialistas/paralelismo: `graph-engineering`;
- roteamento/fallback: `model-routing-gateway`;
- edição/revisão: skills de engenharia existentes;
- contexto canônico: `project-skill-architecture`.

**Segurança:** CAUTION. A instalação modifica configurações, injeta MCPs/hooks e possui ampla superfície operacional. Não foi executada.

### Mem0

Revisão observada: `f8082a7345dadd9e042ebbc40b57b1498c8f6d63`.

A versão descrita em 2026 destaca extração ADD-only, entity linking, busca semântica + BM25 + entidades e temporal reasoning.

O Arsenal já cobre:
- memória em níveis, provenance, conflitos e validade temporal em `session-learn`;
- dense/sparse/hybrid, filtros e avaliação em `retrieval-quality-engineering`.

A ideia de "ADD-only" não deve virar regra universal no Arsenal: append-only é uma escolha de arquitetura, enquanto o Arsenal precisa suportar correção, revalidação e remoção controlada conforme o sistema real.

**Segurança:** CAUTION para integrar o produto, especialmente em memória pessoal/sensível. Não foi instalado.

### LangGraph

Revisão observada: `1211af45b18cab9c0a7efe366ba12f51ad2a9996`.

Durable execution, HITL, memória e stateful graphs são fortes como runtime. O Arsenal já separa topologia (`graph-engineering`), loops/state (`loop-engineering`) e observabilidade (`llm-observability-evaluation`). Não importar dependência nem criar skill paralela.

### AutoGen

Revisão observada: `027ecf0a379bcc1d09956d46d12d44a3ad9cee14`.

O commit observado atualiza o README para maintenance mode e direciona novos usuários ao Microsoft Agent Framework. Isso reforça a decisão de não congelar AutoGen como owner ou dependência do Arsenal.

### Aider

Revisão observada: `5dc9490bb35f9729ef2c95d00a19ccd30c26339c`.

Repo map, Git, lint/test automático e edição orientada por contexto são boas práticas, mas já aparecem de forma mais modular nas skills de entendimento de código, TDD, revisão e verificação. Não criar skill "aider".

### Langflow

Revisão observada: `df9711c952a8e798e8fbbad8f25fe60be5ff6018`.

É plataforma/runtime visual para construir e operar fluxos. Metodologia de DAG, tool boundaries, structured outputs e observabilidade já está distribuída entre owners próprios no Arsenal.

## Segurança

A avaliação foi **documental e read-only**. Nenhum installer, pacote, binário, serviço, hook ou código externo foi executado.

Verdict geral:
- metodologia selecionada: **APPROVE quando já representada pelos owners existentes**;
- execução/importação dos runtimes: **CAUTION**;
- prompt dumps e proxies de API: **não adotar como skills** sem caso de uso específico e nova revisão.

## Resultado para o Arsenal

- nenhuma nova skill;
- nenhuma nova stack;
- nenhuma alteração no `ARSENAL INDEX.md`;
- nenhum runtime externo adicionado;
- nenhuma dependência nova;
- este registro documenta a triagem para evitar reavaliação redundante do leaderboard.

A popularidade do GitHub continua útil como radar de descoberta, não como critério de promoção.
