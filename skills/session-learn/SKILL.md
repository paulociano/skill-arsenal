---
name: session-learn
description: "Extrair aprendizados duráveis de uma sessão quando solicitado ou autorizado, com deduplicação e rastreabilidade."
---

# session-learn

## Objetivo

Fechar uma sessão de trabalho extraindo apenas aprendizados duráveis e reutilizáveis, com rastreabilidade e deduplicação.

## Quando usar

Extrair aprendizados duráveis de uma sessão quando solicitado ou autorizado, com deduplicação e rastreabilidade.

## Sinais a procurar

1. **Conceito** — mecanismo estável e reutilizável.
2. **Entidade** — projeto, sistema, ferramenta ou ator que merece contexto durável.
3. **Correção** — crença ou procedimento desmentido pela evidência.
4. **Padrão** — sequência reutilizável Trigger → Execute → Verify → State.
5. **Ideia** — possibilidade não testada, claramente provisória.
6. **Decisão** — escolha, racional, alternativas e condição de revisão.
7. **Gap** — desconhecido com probe ou próximo passo.

## Workflow

1. Delimitar a sessão e comparar objetivo versus resultado observado.
2. Separar evidência de execução de interpretação retrospectiva.
3. Extrair candidatos nos sete tipos acima.
4. Manter somente itens novos, reutilizáveis, rastreáveis e decision-relevant.
5. Deduplicar contra conhecimento/skills existentes.
6. Aplicar Closure Protocol: **Format → Link → Log**.
7. Verificar a gravação quando houver write-back.

## Camadas de memória

Quando um aprendizado virar memória durável, separar camadas em vez de achatar tudo:

- **L0 Raw** — conversa/fonte original para auditoria e wording exato;
- **L1 Atom** — fatos, preferências, constraints, eventos e decisões discretas;
- **L2 Scenario** — bloco contextual por projeto/situação;
- **L3 Core** — padrão estável de longo prazo, somente quando realmente sustentado.

Além do conteúdo, manter quando aplicável:

- owner;
- source/provenance;
- version/status;
- visibility;
- revisão/validade;
- bindings/loadout: quem realmente precisa receber aquela memória.

Princípios:

- private by default para memória pessoal/sensível;
- compartilhar é ação explícita;
- conflito entre memórias deve ser registrado, não silenciosamente reconciliado;
- memória velha não vence evidência nova apenas porque já estava salva;
- armazenar menos, mas com melhor provenance e retrieval target.

## Temporalidade e supersession

Quando um fato ou decisão muda ao longo do tempo, não sobrescrever a história sem rastro:

- registrar quando a informação passou a valer e, se aplicável, quando deixou de valer;
- manter o fato antigo como superseded quando ele for relevante para explicar decisões anteriores;
- ligar fatos derivados ao episódio/fonte que os originou;
- distinguir event time, ingestion time e review time quando essa diferença afetar interpretação;
- consultas sobre “o que era verdade naquela época?” precisam usar a validade temporal, não apenas o valor mais recente.

Esse padrão é especialmente útil para projetos, políticas, preferências e sistemas que evoluem. Graphiti inspira a noção de fatos temporais com provenance, mas não é dependência do Arsenal. O pipeline de aprendizagem contínua foi refinado a partir de CopilotKit/OpenDots, preservando separação entre ingestão, proposta, publicação e delivery sem adotar seu runtime.

## Memória como fonte de verdade + índice derivado

Quando o ambiente suportar memória persistente própria do projeto, preferir uma arquitetura em que:

- o conteúdo canônico permaneça em formato humano-editável e versionável;
- índices de busca, embeddings, grafos e caches sejam derivados e reconstruíveis;
- handoffs sejam objetos explícitos com ownership e estado, não apenas texto solto;
- retenção e compactação preservem provenance e reversibilidade;
- fatos frios possam ser compactados sem apagar a fonte original quando o storage permitir;
- contradições sejam sinalizadas, não silenciosamente fundidas;
- memória usada recentemente possa receber maior prioridade de retenção, desde que isso não apague informação só por falta de acesso.

Não presumir que a Memory do ChatGPT, um MCP externo ou um servidor local oferece essas garantias. Esta seção descreve um contrato desejável para sistemas que realmente possuam storage, versionamento e retrieval próprios.

## Pipeline de aprendizagem contínua

Quando o ambiente oferecer aprendizagem automática a partir de múltiplas conversas, separar explicitamente quatro estágios:

1. **Ingest**
   - rotear evidência apenas para um escopo/workflow conhecido;
   - registrar qual escopo recebeu cada conversa ou episódio;
   - mudança de configuração não deve reclassificar retroativamente evidência antiga sem migração explícita.

2. **Propose**
   - gerar candidatos de aprendizado/skill a partir de evidência suficiente;
   - proposta automática não é conhecimento canônico;
   - manter exemplos, provenance e sinais de suporte acessíveis para revisão.

3. **Review / publish**
   - skill reutilizável precisa de revisão/publicação antes de entrar no catálogo canônico;
   - publicação deve produzir versão/revisão identificável;
   - ingestão pode continuar mesmo quando delivery estiver desligado, desde que isso seja intencional e visível.

4. **Deliver / use**
   - carregar apenas skills publicadas e relevantes ao contexto;
   - manter binding estável entre conversa/episódio e o escopo de aprendizagem originalmente atribuído quando isso evitar mudanças silenciosas de comportamento;
   - configuração de delivery não prova uso: verificar traces, tool calls, citations ou outro sinal observável de que a skill foi realmente carregada;
   - se delivery foi configurado como requisito e estiver indisponível, preferir falha explícita a continuar silenciosamente com comportamento diferente.

Esse pipeline é um contrato arquitetural. Não pressupõe CopilotKit, containers específicos, serviços cloud ou aprendizagem autônoma disponível no ChatGPT.

## Integração com Arsenal

- `session-learn` captura o delta da sessão.
- `retrospective-codify` decide se algum delta deve virar regra, checklist, teste ou skill.
- `skill-builder` constrói a skill quando esse for o destino correto.
- Não transformar conversa comum automaticamente em memória/skill sem autorização ou mecanismo explícito.

## Referências

Adaptada de Mark393295827/third-brain-v7-skills · session-learn (V8.1).

Validade temporal, supersession e provenance por episódio refinados a partir de https://github.com/getzep/graphiti.

Origem local: [session-learn.docx](../session-learn.docx).