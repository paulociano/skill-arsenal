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


## Fechamento do lote de 30 candidatos — 2026-10-19

Todos os 30 endereços foram consultados individualmente via metadados oficiais do GitHub (existência, descrição, estrelas, último push e licença quando declarada). As classificações são **triagem de adequação e portabilidade**, não auditoria completa de código, segurança ou benchmark. Aprofundamento de conteúdo: SKILL.md de awesome-skills/code-review-skill e vikingmute/review-forge; README de amElnagdy/guard-skills e google/mantis; descrição oficial dos demais. Licença não confirmada significa que o campo de licença não foi identificado nos metadados consultados.

| Repositório | Estrelas | Licença declarada | Classe | Decisão | Fundamentação resumida |
|---|---:|---|---|---|---|
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 32175 | MIT | A/D | UPDATE_EXISTING | Audit phases; independent verification |
| [awesome-skills/code-review-skill](https://github.com/awesome-skills/code-review-skill) | 2118 | MIT | B | KEEP_EXTERNAL_REFERENCE | Language-specific checklists overlap with owners |
| [JeremyMorgan/code-review-skills](https://github.com/JeremyMorgan/code-review-skills) | 17 | CC0-1.0 | B | KEEP_EXTERNAL_REFERENCE | Modular reviews; incremental delta unproven |
| [getsentry/skills](https://github.com/getsentry/skills) | 1066 | Apache-2.0 | B | KEEP_EXTERNAL_REFERENCE | Broad team skill collection; selective future evaluation |
| [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | 1536 | MIT | A/D | UPDATE_EXISTING | Architecture decay diagnostics |
| [nathankim0/clean-architecture-skills](https://github.com/nathankim0/clean-architecture-skills) | 100 | MIT | B | KEEP_EXTERNAL_REFERENCE | Clean architecture overlap |
| [amElnagdy/guard-skills](https://github.com/amElnagdy/guard-skills) | 1272 | MIT | A | UPDATE_EXISTING | Test-guard second-pass quality |
| [vikingmute/review-forge](https://github.com/vikingmute/review-forge) | 223 | não confirmado | A | UPDATE_EXISTING | Human-selected fix and verify stages |
| [khasky/awesome-agent-skills](https://github.com/khasky/awesome-agent-skills) | 14 | MIT | B | KEEP_EXTERNAL_REFERENCE | General collection; no unique owner identified |
| [hannsxpeter/auditor-suite](https://github.com/hannsxpeter/auditor-suite) | 0 | MIT | B | KEEP_EXTERNAL_REFERENCE | Multi-domain audit; low adoption signal and overlap |
| [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent) | 13456 | MIT | D | KEEP_EXTERNAL_REFERENCE | Automated PR service |
| [vercel-labs/openreview](https://github.com/vercel-labs/openreview) | 1693 | não confirmado | D | KEEP_EXTERNAL_REFERENCE | Hosted/self-hosted PR bot |
| [mattzcarey/shippie](https://github.com/mattzcarey/shippie) | 2512 | MIT | D | KEEP_EXTERNAL_REFERENCE | Review agent runtime |
| [sourcery-ai/sourcery](https://github.com/sourcery-ai/sourcery) | 1877 | MIT | D | KEEP_EXTERNAL_REFERENCE | AI code review tooling |
| [greptileai/skills](https://github.com/greptileai/skills) | 422 | MIT | B | KEEP_EXTERNAL_REFERENCE | PR status/comment checks |
| [chorus-codes/chorus](https://github.com/chorus-codes/chorus) | 534 | Apache-2.0 | D | KEEP_EXTERNAL_REFERENCE | Multiple model CLI dependency |
| [spencermarx/open-code-review](https://github.com/spencermarx/open-code-review) | 379 | Apache-2.0 | D | KEEP_EXTERNAL_REFERENCE | Multi-agent orchestration |
| [codexstar69/bug-hunter](https://github.com/codexstar69/bug-hunter) | 526 | MIT | A/D | KEEP_EXTERNAL_REFERENCE | Adversarial hunt with auto-fix; execution risk |
| [kodustech/kodus-ai](https://github.com/kodustech/kodus-ai) | 1502 | NOASSERTION | D | KEEP_EXTERNAL_REFERENCE | Self-hosted service; license review needed |
| [Agent-Field/pr-af](https://github.com/Agent-Field/pr-af) | 655 | não confirmado | D | KEEP_EXTERNAL_REFERENCE | Benchmark claim not independently validated |
| [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | 6440 | MIT | D | KEEP_EXTERNAL_REFERENCE | Claude-specific GitHub Action |
| [google/mantis](https://github.com/google/mantis) | 2473 | Apache-2.0 | A/D | KEEP_EXTERNAL_REFERENCE | Security reproduction pipeline; isolated runtime required |
| [lintsinghua/DeepAudit](https://github.com/lintsinghua/DeepAudit) | 7179 | AGPL-3.0 | D | KEEP_EXTERNAL_REFERENCE | Multi-agent sandbox, license/runtime requirements |
| [yldgio/codereview-skills](https://github.com/yldgio/codereview-skills) | 0 | MIT | B | KEEP_EXTERNAL_REFERENCE | No verified incremental capability |
| [tysoncung/awesome-devsecops](https://github.com/tysoncung/awesome-devsecops) | 2 | CC0-1.0 | B | KEEP_EXTERNAL_REFERENCE | Curated list, not operational skill |
| [marv-devops/awesome-static-analysis](https://github.com/marv-devops/awesome-static-analysis) | 0 | MIT | B | KEEP_EXTERNAL_REFERENCE | Stale catalog (last push 2022) |
| [semgrep/semgrep](https://github.com/semgrep/semgrep) | 17133 | LGPL-2.1 | D | KEEP_EXTERNAL_REFERENCE | SAST engine |
| [github/codeql](https://github.com/github/codeql) | 10213 | MIT | D | KEEP_EXTERNAL_REFERENCE | Semantic query engine |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | 38515 | Apache-2.0 | D | KEEP_EXTERNAL_REFERENCE | Supply-chain scanner |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | 30126 | MIT | D | KEEP_EXTERNAL_REFERENCE | Secret scanner |

### Implementações efetivas
- `skills/code-review/SKILL.md`: gates de evidência, arquitetura e ciclo review→fix→verify. Commits `02c8adafad9e6b9015bf4e191977e2f2ae895a49` e `e6fcf1843abf83419eefb5854a1b138268ca068c`.
- `skills/software-testing-engineering/SKILL.md`: gate para testes gerados por IA. Commit `b2fb24c47aa37de4a2f3a648fdf43e60ae0fb4d8`.
- Nenhuma stack duplicada ou runtime externo instalado. Não houve alteração de consumidores.

### Segurança, manutenção e limitações
- Não executar auto-fix, instaladores, GitHub Actions de terceiros ou PoCs sem ambiente isolado e autorização de alvo. O README do Google Mantis alerta que sua ação de PR não foi testada end-to-end e não deve bloquear merges.
- Licenças de repositório não significam automaticamente permissão para incorporar trechos sem observar atribuições; só princípios reescritos foram absorvidos.
- Estrelas e atividade são sinais de adoção/manutenção, não avaliações qualitativas. `hannsxpeter/auditor-suite`, `yldgio/codereview-skills` e `marv-devops/awesome-static-analysis` têm zero estrelas no snapshot; não devem ser descritos como altamente avaliados.
- As 26 fontes não incorporadas permanecem referências ou descartes de adoção nesta rodada, não pendências de publicação. Nova análise profunda é necessária antes de instalar qualquer uma.
