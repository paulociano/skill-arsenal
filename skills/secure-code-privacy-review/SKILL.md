---
name: secure-code-privacy-review
description: "Revisar código e diffs por vulnerabilidades de segurança e violações de privacidade com trust boundaries, data flows, validação de findings e baixa tolerância a falsos positivos."
---

# Secure Code & Privacy Review

## Objetivo
Revisar implementação, diff ou PR por duas superfícies relacionadas mas distintas: **security weakness** e **privacy/data-flow violation**, sustentando cada finding por caminho concreto e contexto real do framework.

## Quando usar
- revisão de código com risco de segurança ou privacidade;
- auth/authz, injection, SSRF, secrets, deserialization ou unsafe redirects;
- código que coleta, armazena, transmite ou registra dados pessoais/sensíveis;
- PRs em que um finding precisa ser validado antes de ser reportado.

Não usar para avaliar se uma skill/plugin externa é segura para instalar; use `skill-security-review`. Para red team de aplicações LLM, use `llm-red-team-evaluation`. Para testar controles de um web app/API em runtime autorizado, use `web-application-security-audit`.

## Workflow
1. **Context** — identificar frameworks/proteções reais, trust boundaries e superfícies alteradas.
2. **Inventory** — mapear entradas não confiáveis e classes de dados relevantes sem copiar valores sensíveis.
3. **Detect** — enumerar candidatos em security e privacy separadamente.
4. **Trace** — provar source → transformations/guards → sink ou data field → storage/log/processor/retention boundary.
5. **Validate** — tentar refutar cada candidato com sanitização, parametrização, auth middleware, ownership check, auto-escape, allowlist, encryption/redaction ou outro controle realmente presente.
6. **Impact** — avaliar exploitability/impact para segurança e exposição/propagação/retention para privacidade.
7. **Report** — retornar apenas findings sustentados com localização, consequência, evidência e remediação concreta.
8. **Retest** — após correção, repetir o caminho original e verificar regressão proporcional ao risco.

## Privacy data-flow
Quando código novo tocar dados pessoais ou confidenciais, registrar antes da implementação material:
- classificação do dado;
- origem;
- storage/cache/log;
- transmissão e terceiros;
- retenção/deleção;
- backup/replicação;
- redaction/tokenization/encryption;
- controles e perguntas abertas.

Mapear obrigação regulatória somente quando jurisdição, papel da organização e contexto estiverem estabelecidos. Não inferir automaticamente que uma lei se aplica a toda ocorrência de um campo.

## Precision gate
- finding precisa de caminho concreto, não apenas padrão textual;
- configuração/admin data pode ser semi-trusted, não trusted por default;
- framework protection real pode suprimir finding;
- ausência de evidência suficiente vira `needs verification`, não vulnerabilidade;
- para categorias críticas, preferir confirmação independente ou teste seguro quando disponível;
- não usar threshold numérico de confiança como substituto de evidência.

## Guardrails
- nunca incluir secret/PII real no relatório;
- não executar exploit destrutivo;
- não tratar compliance mapping como aconselhamento jurídico;
- privacy e security podem compartilhar fluxo, mas não são a mesma finding;
- não afirmar cobertura completa se parte do diff/flow não foi revisada.

## Integração
`code-review`, `behavior-contract-validation`, `web-application-security-audit`, `skill-security-review`, `llm-red-team-evaluation`, `verify-before-claim`.

## Origem metodológica
Síntese adaptada de `facebookresearch/secpriv-skill` e `Clear-Capabilities/agentic-security · privacy-data-flow`. Preserva detector→validator, trust boundaries e data-flow preflight sem exigir scanners, scratchpads, slash commands ou regras jurídicas absolutas das fontes.
