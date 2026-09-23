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

Esse padrão é especialmente útil para projetos, políticas, preferências e sistemas que evoluem. Graphiti inspira a noção de fatos temporais com provenance, mas não é dependência do Arsenal.

## Integração com Arsenal

- `session-learn` captura o delta da sessão.
- `retrospective-codify` decide se algum delta deve virar regra, checklist, teste ou skill.
- `skill-builder` constrói a skill quando esse for o destino correto.
- Não transformar conversa comum automaticamente em memória/skill sem autorização ou mecanismo explícito.

## Referências

Adaptada de Mark393295827/third-brain-v7-skills · session-learn (V8.1).

Validade temporal, supersession e provenance por episódio refinados a partir de https://github.com/getzep/graphiti.

Origem local: [session-learn.docx](../session-learn.docx).
