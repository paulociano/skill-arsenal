# Avaliação em lote — sistemas Jev, browser agents, code mode e ferramentas especializadas

Data: 2026-09-20

## Escopo

Fontes avaliadas:

- https://github.com/tamaratran/fast-jev-compaction
- https://github.com/robbietilton/Compositor
- https://github.com/TheoLeeCJ/SemIf
- https://github.com/jarrodwatts/jev-trader
- https://github.com/browser-use/jev-ultrafast
- https://github.com/amap-cvlab/ABot-Recon
- https://github.com/MaxGramser/homeassistant_espscreen
- https://github.com/lidge-jun/aside-codemode
- https://github.com/NandhaKishorM/laya

Fluxo aplicado: `evaluate-and-import-skill`, com revisão proporcional de segurança por `skill-security-review`.

Nenhum installer, setup script ou código arbitrário dessas fontes foi executado. A análise foi feita por leitura do repositório, README, manifests e arquivos operacionais selecionados.

## Resumo da decisão

O lote contém projetos tecnicamente interessantes, mas a maior parte é software especializado, não Agent Skills portáveis. A decisão é **não importar nenhuma das nove fontes como nova skill**.

Há valor metodológico real em quatro frentes, absorvido por skills já existentes:

1. compactação seletiva de contexto sem reescrever evidência importante;
2. browser automation com action space observado, alvo indexado e freshness guards;
3. execução/search em lote com filtragem antes de devolver resultados ao contexto do modelo;
4. decisão semântica tipada como classe distinta de geração textual, com gates de capacidade, calibração e validação.

## Avaliações individuais

### fast-jev-compaction

**Classificação:** D — skill/projeto técnico dependente de Jev, TypeSafe API e hooks do Claude Code.

**O que faz:** compacta histórico preservando mensagens de texto e decidindo quais tool calls/results manter, truncar ou remover. O foco é evitar resumos lossy quando paths, erros, restrições ou outputs exatos podem ser necessários mais tarde.

**Valor incremental:** alto como metodologia de contexto. O princípio de separar informação em preservação verbatim, compactação e descarte é útil para handoffs e sessões longas.

**Sobreposição:** `handoff` já possui KEEP / SUMMARIZE / DROP / RETRIEVE.

**Decisão:** adaptar a metodologia em `handoff`; não importar plugin nem dependência Jev.

**Segurança:** CAUTION. O projeto envia estado da conversa a um serviço externo quando configurado com TypeSafe API. Credenciais são esperadas por variável de ambiente. Não foi executado.

### Compositor

**Classificação:** D — aplicação nativa macOS.

**O que faz:** editor de imagens em camadas, máscaras, transforms, seleções, pintura, filtros e export.

**Valor incremental para o Arsenal:** baixo. É uma aplicação completa, não um procedimento reutilizável de agente.

**Decisão:** não importar e não adaptar.

**Segurança:** APPROVE para a finalidade declarada na revisão limitada do README, mas sem auditoria completa do código. O processo de release envolve assinatura/notarização e ferramentas externas, irrelevantes ao Arsenal.

### SemIf

**Classificação:** D — engine/modelo técnico.

**O que faz:** decisões semânticas tipadas por leitura direta de logits de modelos abertos, evitando geração autoregressiva para pequenos `if` semânticos.

**Valor incremental:** útil como arquitetura de referência para routing/classificação de baixa latência, não como skill operacional.

**Sobreposição:** `model-routing-gateway` e `structured-output-contract`.

**Decisão:** incorporar em `model-routing-gateway` a distinção entre decision engine e modelo generativo; não importar runtime Python/GPU.

**Segurança:** CAUTION. Depende de PyTorch, Transformers, Hugging Face e downloads de modelos; possui dependência Git pinada para MLX em modo opcional. Nenhuma instalação foi executada.

### jev-trader

**Classificação:** D — sistema de trading on-chain.

**O que faz:** lê order book, obtém decisão buy/sell e pode publicar ordens reais a cada bloco.

**Valor incremental para o Arsenal:** muito específico e fortemente acoplado a exchange, blockchain, carteira e modelo externo.

**Decisão:** não importar e não adaptar como skill genérica.

**Segurança:** CAUTION alto. Suporta `PRIVATE_KEY`, transações reais, depósitos/margem e ordens financeiras. O dry-run é um controle útil, mas a versão live possui efeito financeiro externo. Nenhum segredo foi fornecido ou executado.

### jev-ultrafast

**Classificação:** D — agente técnico com metodologia B reutilizável.

**O que faz:** observa controles visíveis, constrói action space dinâmica, escolhe operação e alvo compatível, gera texto apenas quando necessário e revalida freshness/geometry antes de executar.

**Valor incremental:** alto para browser automation. O desenho reduz ações inválidas e stale actions sem depender de selectors inventados pelo modelo.

**Sobreposição:** `runtime-ui-verification` e ferramentas reais de browser disponíveis no ambiente.

**Decisão:** adaptar action-space indexada, consume-once e freshness guards em `runtime-ui-verification`. Não importar Jev, Browser Harness ou OpenRouter.

**Segurança:** CAUTION. Controla navegador e pode usar APIs externas. O código revisado possui budgets, stale-page checks e alvo derivado de nós observados, bons controles. Adoção nativa ainda exigiria credenciais e dependências externas.

### ABot-Recon

**Classificação:** D — modelo de visão/reconstrução 3D.

**O que faz:** reconstrução 3D streaming de longo horizonte com contexto local fixo e composição sequencial de poses.

**Valor incremental para o Arsenal:** baixo no estado atual. Pode ser referência futura para pipelines 3D, mas não corresponde a um workflow recorrente do Arsenal.

**Decisão:** não importar e não adaptar agora.

**Segurança:** CAUTION. Exige stack pesada CUDA/PyTorch, checkpoints externos e opcionalmente extensões compiladas. Nenhuma dependência foi instalada.

### homeassistant_espscreen

**Classificação:** D — integração técnica de domínio com uma Agent Skill gerada.

**O que faz:** gerencia telas ESP32 pelo Home Assistant e inclui gerador determinístico de `SKILL.md` para operar tiles, alertas e standby.

**Valor incremental:** real apenas para usuários que possuem essa integração. A skill gerada é específica ao dispositivo e ao Home Assistant, não uma competência geral.

**Decisão:** não importar para o Arsenal global sem um workflow real do usuário que use ESP Screens. Se esse contexto existir no futuro, preferir uma skill de projeto/domínio estreita.

**Segurança:** CAUTION. A skill pode disparar eventos/ações em Home Assistant e acender/controlar dispositivos físicos. O próprio texto exige leitura do estado e confirmação antes de mudanças sensíveis, o que é um bom approval gate. Também referencia token do Supervisor para chamadas locais; credenciais não devem ser copiadas para o Arsenal.

### aside-codemode

**Classificação:** D — ferramenta técnica com metodologia B reutilizável.

**O que faz:** expõe busca, leitura, filtragem e browsing em lote por uma única camada de code mode, devolvendo apenas resultados selecionados ao contexto do modelo.

**Valor incremental:** alto como princípio de economia de contexto e redução de round-trips. O ambiente atual já possui Code Mode, busca e ferramentas equivalentes, então importar o pacote seria redundante.

**Sobreposição:** `kb-retriever` e `web-extraction-pipeline`.

**Decisão:** adaptar o princípio “processar perto da fonte e retornar apenas resposta + evidência necessária” nessas skills; não instalar MCP/npm externo.

**Segurança:** CAUTION. A ferramenta expõe execução em sandbox, browser automation e registro MCP/CLI. A revisão do package manifest mostra scripts de instalação/registro; eles não foram executados.

### Laya

**Classificação:** D — modelo/engine técnico.

**O que faz:** decisão tipada não autoregressiva (`choice`, `score`, `noul`) com roteamento de checkpoints e foco em baixa latência.

**Valor incremental:** útil como referência para classificadores/decision engines especializados, sobretudo ao mostrar que confidence, idioma, cardinalidade de labels e fine-tuning mudam a validade do roteamento.

**Sobreposição:** `model-routing-gateway` e `structured-output-contract`.

**Decisão:** incorporar critérios de seleção e validação em `model-routing-gateway`; não importar runtime/modelos.

**Segurança:** CAUTION. Depende de PyTorch, Transformers e modelos Hugging Face. O próprio README documenta limites de calibração e generalização, portanto confidence não deve ser tratada como garantia sem validação no domínio.

## Mudanças aplicadas ao Arsenal

- `handoff`: distinguir evidência que deve permanecer verbatim de material que pode ser resumido ou descartado; tool call e tool result podem ter valores de retenção diferentes.
- `runtime-ui-verification`: adicionar action space observada, targets compatíveis, freshness/fingerprint guard, consume-once e reobservação após mutação.
- `web-extraction-pipeline`: processar/batchear próximo da fonte e devolver apenas campos/evidência necessários, sem despejar HTML/DOM bruto no contexto.
- `kb-retriever`: preferir busca/agregação em lote e deduplicação antes de transportar conteúdo para o modelo.
- `model-routing-gateway`: reconhecer decision engines/classificadores tipados como uma classe de deployment distinta de modelos gerativos e exigir validação de calibração, domínio, idioma e cardinalidade.

Nenhuma description mudou materialmente e nenhuma skill/stack foi criada, removida ou renomeada; portanto `ARSENAL INDEX.md` não precisa de alteração.

## Limites da validação

- Não houve scanner estático automatizado dedicado.
- Não houve instalação de dependências, execução de modelos, browser harness, trading, firmware ou Home Assistant.
- Benchmarks publicados pelos próprios autores foram tratados como claims das fontes, não reproduzidos.
- A revisão de segurança foi proporcional ao que seria incorporado: metodologia e arquitetura, não dependências executáveis.
