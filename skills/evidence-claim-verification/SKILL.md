---
name: evidence-claim-verification
description: "Verificar claims científicos ou técnicos por decomposição explícita, busca orientada a evidência, avaliação de suporte/refutação e rastreabilidade das fontes sem converter incerteza em certeza."
---

# evidence-claim-verification

## Objetivo

Verificar claims científicos, técnicos ou factuais difíceis por um processo explícito de claim → subclaims → evidence → entailment → verdict, mantendo separadas a evidência recuperada, o raciocínio do modelo e a incerteza residual.

## Quando usar

- claims científicos ou técnicos com consequência material;
- perguntas em que "há evidência para X?" é mais importante que uma explicação geral;
- controvérsias em que fontes podem apoiar partes diferentes do claim;
- revisão de afirmações em papers, relatórios, apresentações ou documentos técnicos;
- checagem que exige literatura primária, standards ou documentação técnica.

Não usar para fatos triviais que uma fonte autoritativa única resolve diretamente.

## Princípio central

Recuperar evidência não basta. É preciso testar se ela realmente implica, contradiz ou é insuficiente para o claim exato.

## Workflow

1. Normalize claim.
2. Decompose em subclaims independentes.
3. Plan evidence: definir o que discriminaria suporte de refutação.
4. Retrieve selectively: buscar por subclaim, priorizando fonte primária e oficial.
5. Assess source: recência, população, método, limitações e indireção.
6. Test entailment: classificar como supports, contradicts, mixed, insufficient ou not-applicable.
7. Reconcile divergências por desenho, população, versão, horizonte ou definição.
8. Verdict proporcional: Supported, Partially supported, Contradicted, Mixed ou Insufficient evidence.
9. Trace: citar evidência junto do subclaim e separar fato, interpretação e conclusão.

## Entailment graph leve

Quando houver raciocínio multi-hop:
- nós = subclaims verificáveis;
- arestas = dependência lógica explícita;
- folhas = evidência recuperável;
- raiz = claim final.

Regras:
- não criar nós apenas para pensar mais;
- cada nó deve ser testável por evidência ou derivação lógica simples;
- se um nó crítico fica insufficient, a raiz não pode virar supported por fluência do modelo;
- conflitos permanecem visíveis na síntese.

## Tool discipline

Dar ao agente apenas as ferramentas necessárias para o claim atual. Ferramentas redundantes aumentam custo e podem piorar seleção. Prefira uma rota clara para busca, leitura e inspeção.

Não presumir MCPs, APIs, agentes locais ou credenciais presentes em uma implementação externa. Usar apenas ferramentas reais do ambiente atual.

## Guardrails

- não usar conhecimento interno do modelo como evidência quando fonte verificável é necessária;
- não confundir ausência de evidência com evidência de ausência;
- não generalizar resultado de uma população para outra sem declarar a extrapolação;
- não esconder estudos contrários materialmente relevantes;
- não usar preprint, blog ou secondary source como equivalente automático a paper revisado ou standard oficial;
- não declarar verdade científica universal quando a evidência sustenta apenas um escopo específico;
- quando o claim for médico, legal, financeiro ou safety-critical, elevar padrão de fonte e explicitar limites.

## Integração

Combina com research-and-synthesize, research-question-design, academic-paper-orchestration, 3gpp-standards-research e verify-before-claim.

Esta skill é dona do claim-level evidence reconciliation. Não substitui pesquisa ampla nem revisão de paper completo.

## Provenance

Metodologia adaptada de https://github.com/xiongsiheng/DeepVerify e dos conceitos de entailment graph/MARS descritos no projeto.

A adaptação preserva decomposição, busca orientada a evidência, whitelist de ferramentas e raciocínio estruturado, sem depender de Pixi, MCP server próprio, LangGraph, SERPAPI, Jina, LangSmith ou modelos treinados do projeto.
