---
name: patent-strategy-review
description: "Auditar e pressionar pedidos de patente utilitária dos EUA com gates de completude, suporte, prior art, claim coverage e design-around, separando análise técnica de aconselhamento jurídico."
---

# patent-strategy-review

## Objetivo

Revisar pedidos de patente utilitária dos EUA com disciplina de evidência, versionamento e escopo, cobrindo três modos:

1. pre-filing audit;
2. simulated examination;
3. design-around challenge.

## Quando usar

- auditoria de draft antes de depósito;
- revisão de claims, specification, drawings e filing packet;
- simulação de Office Action;
- stress test de novelty, nonobviousness, enablement ou definiteness;
- design-around e gap analysis de claim scope.

Não usar como substituto de advogado de patentes, opinião de infringement/FTO, validade, enforceability ou garantia de patenteabilidade.

## Princípio central

A intenção do inventor não expande o disclosure, e disclosure suficiente não prova patenteabilidade.

Manter separadas:
- claim coverage;
- disclosure support;
- technical plausibility;
- prior art;
- patentability;
- commercial relevance;
- legal conclusion.

## Intake mínimo

Identificar, quando aplicável:
- specification completa;
- claims e dependências;
- abstract;
- drawings;
- prioridade, benefício e continuidade;
- inventorship;
- disclosures/public use/sale;
- prior art e search history;
- prosecution history;
- objetivos comerciais e mecanismos essenciais.

Informação faltante vira missing/cannot assess, nunca fato favorável.

## Modo 1 — Pre-filing audit

1. Fazer pre-pass para inventário de seções, dependência de claims, referências cruzadas, antecedent basis e inconsistências mecânicas.
2. Rodar gates de completude, prioridade/deadlines, inventorship, §§101/102/103/112 conforme aplicável, written description, enablement, definiteness, drawings/support e filing mechanics atuais.
3. Separar findings fatais, materiais e menores.
4. Findings críticos exigem fonte primária atual e suporte textual concreto.

## Modo 2 — Simulated examination

Manter:
- ground truth;
- candidate completa com emendas propostas;
- record de actions, responses, search logs, referências e hashes.

Workflow:
1. congelar versão;
2. construir packet com prioridade e prior art;
3. produzir Office Action simulada com claim-by-claim status;
4. validar referências e mappings;
5. responder com argumento e/ou emenda suportada;
6. promover candidate somente após revisão explícita;
7. repetir com revisão independente quando o risco justificar.

Nunca chamar isso de allowance real ou garantia de validade.

## Modo 3 — Design-around challenge

Para cada challenge:
1. decompor claims em limitações;
2. procurar alternativas tecnicamente plausíveis que preservem o valor principal;
3. testar se evitam alguma limitação, se continuam comercialmente relevantes, se pertencem à tese estratégica, se são suportadas e se uma captura por claim resistiria a new-matter, prior-art e §112;
4. classificar como covered hypothesis, credible gap, outside strategic umbrella, unsupported by disclosure, high-risk/unclaimable ou unresolved.

Não ampliar claims apenas para pegar tudo.

## Pesquisa e fontes

Para claims legais materiais:
- priorizar 35 U.S.C., 37 CFR, MPEP, USPTO e guidance/decisões oficiais atuais;
- registrar data e versão;
- preservar identidade, publication date, trechos relevantes e contexto de prior art;
- exigir claim mapping, não apenas citação.

Sempre re-verificar filing mechanics, fees, forms e guidance vigente.

## Versionamento e integridade

Mudanças substantivas em claims, specification, evidence packet ou priority facts invalidam revisão anterior da versão antiga.

Quando houver arquivos:
- preservar original;
- editar candidate separada;
- usar hashes quando possível;
- promover somente a versão realmente revisada;
- verificar que o ground truth corresponde ao candidate aprovado.

## Guardrails

- não declarar legal advice;
- não prometer allowance, validade, enforceability ou FTO;
- não esconder incerteza;
- não tratar ausência de prior art encontrado como prova de novidade;
- não inventar suporte de disclosure;
- quando a análise depender de lei/prática atual, pesquisar fontes oficiais antes de concluir.

## Integração

Combina com evidence-claim-verification, research-and-synthesize, document-extraction-pipeline, academic-paper-orchestration e verify-before-claim.

## Provenance

Adaptada de https://github.com/gfodor/legal-skills, especialmente patent-audit, patent-examine e patent-workaround. Foram preservados gates, versionamento, separação entre disclosure/coverage/patentability e adversarial design-around, sem depender dos scripts ou subagent runtime da fonte.
