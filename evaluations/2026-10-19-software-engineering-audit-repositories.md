# Avaliação incremental: auditoria de engenharia (2026-10-19)

## Escopo e evidência
Continuação da triagem de 30 candidatos da conversa. A lista inicial era exploratória e **não** constituiu verificação individual de 30 repositórios; notas preliminares não são benchmarks. A verificação atual de metadados oficiais confirmou oito repositórios abaixo. A análise profunda foi limitada às capacidades descritas no GitHub de Cloudflare e Brooks Lint e ao owner canônico do Arsenal. Não foram executados scanners, instaladores ou testes dos projetos externos.

| Fonte | Estrelas (snapshot 2026-10-19) | Classe | Decisão | Justificativa |
|---|---:|---|---|---|
| https://github.com/cloudflare/security-audit-skill | 32171 | A/D | UPDATE_EXISTING | Auditoria em fases, achados verificáveis; metodologia portátil, runtime externo não adotado |
| https://github.com/hyhmrright/brooks-lint | 1536 | A/D | UPDATE_EXISTING | Diagnóstico de deterioração estrutural, sem importar auto-fix |
| https://github.com/getsentry/skills | 1066 | B | KEEP_EXTERNAL_REFERENCE | Práticas de engenharia potencialmente úteis, sem delta comprovado nesta rodada |
| https://github.com/JeremyMorgan/code-review-skills | 17 | B | KEEP_EXTERNAL_REFERENCE | Modularidade interessante, mas sem evidência de novidade diante dos owners atuais |
| https://github.com/amElnagdy/guard-skills | 1272 | B | KEEP_EXTERNAL_REFERENCE | Quality gates de código gerado por IA, requer inspeção mais profunda |
| https://github.com/semgrep/semgrep | 17133 | D | KEEP_EXTERNAL_REFERENCE | Scanner técnico, não skill portátil por si só |
| https://github.com/github/codeql | 10213 | D | KEEP_EXTERNAL_REFERENCE | Análise semântica exige engine e ambiente |
| https://github.com/aquasecurity/trivy | 38515 | D | KEEP_EXTERNAL_REFERENCE | Scanner de supply chain, já coberto pelo roteamento existente |

## Ownership e implementação
- Owner: `skills/code-review/SKILL.md`.
- Decisão: absorver somente gate adversarial, inventário de cobertura, confiança e teste de refutação, e sinais de deterioração arquitetural com evidência.
- Não criar stack `software-engineering-audit`: `stacks/web-app-engineering-audit/STACK.md` e `stacks/software-engineering-cycle/STACK.md` já cobrem o roteamento.
- Índice inalterado: nome, description e rota não mudaram.
- Commit da implementação: `02c8adafad9e6b9015bf4e191977e2f2ae895a49`.

## Segurança e portabilidade
Não instalar binários, hooks, extensões ou ferramentas externas; não enviar código de terceiros a serviços sem autorização. Nenhum scanner ou subagente é pressuposto. Findings exigem evidência, versão/commit, limites de cobertura e classificação de confiança. Mudanças de código do consumidor não foram realizadas.

## Limitações e pendências
Os demais 22 candidatos da lista inicial não foram revalidados individualmente nesta rodada; nenhum deles está classificado definitivamente ou adotado. Para concluir avaliação de 30, validar existência, README/SKILL, licença, manutenção, dependências, riscos, delta incremental e resultado por candidato. Estrelas são sinais de adoção, não qualidade comprovada. Sem benchmark prático da metodologia incorporada em repositório consumidor.
