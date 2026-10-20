# HumanLayer + SlopCodeBench: qualidade evolutiva de coding agents (2026-10-20)

## Escopo, autoridade e fontes

- Fonte canônica interna: [Skill Arsenal](https://github.com/paulociano/skill-arsenal), branch `master`. Lidos antes da avaliação: `ARSENAL INDEX.md`, `AGENTS.md`, `stacks/arsenal-autopilot/STACK.md` e `stacks/evaluate-and-import-skill/STACK.md`.
- Fontes fornecidas:
  1. [HumanLayer: benchmarking-new-models-on-slop-code-bench.md](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md), publicado em 2026-10-15.
  2. [humanlayer/skills](https://github.com/humanlayer/skills), branch `main`; README e SKILL.md dos sete plugins.
- Referência científica: [SlopCodeBench / arXiv:2603.24755](https://arxiv.org/abs/2603.24755) e [repositório do benchmark](https://github.com/SprocketLab/slop-code-bench).
- Continuidade: [avaliação anterior da HumanLayer (2026-10-19)](./2026-10-19-scientific-humanlayer-agentskills-personas-ui.md). Ela já tinha adotado RPI e feedback-control; não duplicar esses owners.
- Método: descobrir capabilities, comparar com owners existentes, revisar riscos e incorporar apenas diferenciais portáveis. Nenhum instalador, runner, benchmark ou script de terceiros foi executado.

## 1. Evidência e limites do artigo SlopCodeBench

**Classificação: B (metodologia de avaliação), com runtime D apenas se alguém quiser reproduzir o benchmark integral.**

No estudo de outubro, as campanhas completas de modelos/effort cobriram **36 problemas e 196 checkpoints por configuração**, com **uma campanha por setting**. O protocolo usa a solução produzida pelo agente como base para requisitos adicionais.

- **Strict**: aprovação de todas as categorias relevantes, inclusive testes de regressão.
- **Core**: aprovação dos testes centrais da etapa, mesmo que alguma regressão de etapas anteriores persista.
- **Não confundir** proporção de checkpoints aprovados com proporção de problemas completos que funcionam no checkpoint terminal.
- Strict no relato: **12,24%–16,33%** entre dez campanhas completas; melhor contagem observada: GPT-6 Astra XHigh, **32/196**, versus GPT-6 SOL Medium, **30/196**. Isso não prova liderança universal do modelo.
- Nos três pares Medium/XHigh disponíveis, XHigh custou aproximadamente **2,11–4,22 vezes** Medium e nem sempre elevou Strict. Uma observação por setting não identifica causalidade ou variação estatística.
- A inspeção comparável de resíduos, duplicação e complexidade cobriu **28 problemas** comuns, não os 36 de cada campanha. Percentual de linhas sinalizadas depende de heurísticas e política de filtros; não equivale a contagem de defeitos nem medida direta de manutenibilidade.
- Falhas individuais de testes nos snapshots finais também não são número de bugs distintos.
- O artigo científico e seus catálogos passaram por versões; fixar versão de catálogo/protocolo ao reproduzir. Não misturar taxas de subconjuntos de campanhas anteriores com o experimento atual.

**Valor incremental:** incorporar gates de Core versus Strict, regressão cumulativa, avaliação terminal, resíduos não ocultos, orçamento/replicabilidade e honestidade de métricas no projeto real.

**Decisão:** `UPDATE_EXISTING` em `coding-agent-engineering` e `software-testing-engineering`. Não criar uma skill específica de SlopCodeBench nem afirmar que a suíte foi executada.

## 2. Revisão da coleção humanlayer/skills

**Classificação geral: A/B/D (metodologias úteis; algumas implementações dependem de runners externos).**

| Fonte | Capability e decisão | Owner |
| --- | --- | --- |
| `rpi` | Pesquisa, design, PRD/TDD e implementação em fases, com handoffs documentais; **já incorporado em 2026-10-19** | `project-planning` |
| `design-control-loop` | Set point, sensor, controller, actuator, disturbance e dampener; **já incorporado**. Reforço de limite por loop | `software-factory-operations` |
| `build-iterated-agentic-loop` | **B/D**: limite explícito de PRs pendentes por loop, reuso do PR para iteração e feedback estável não redundante; **UPDATE_EXISTING** | `software-factory-operations` |
| `narrow-react-prop-types` | **B**: contratos de props derivados de usos reais, callbacks não inertes e typecheck dos consumers; **UPDATE_EXISTING**, sem skill própria | `codebase-design` |
| `show-me` | **B/C**, método visual já coberto por explicação/diagramas; **KEEP_EXTERNAL_REFERENCE** | nenhum novo |
| `visual-pr` | **B/D**, representação estrutural do diff útil mas sobreposta a revisão e handoff; **KEEP_EXTERNAL_REFERENCE** | nenhum novo |
| `improve-claude-md` | **B/C/D**, sintaxe e host específicos; métodos gerais de escopo contextual já cobertos; **KEEP_EXTERNAL_REFERENCE** | nenhum novo |

**Ressalva sobre props:** call sites locais não revelam obrigatoriamente todos os consumidores externos de uma API pública. Refatoração não deve quebrar compatibilidade ou remover estados de produto válidos apenas porque stories e mocks os exercitam.

**Ressalva sobre loops:** teto de um PR aberto por loop é heurística inicial, não limite universal. Manual dispatch não deve ser usado para burlar policy de aprovação. A operação requer integração de CI, permissões, secrets e observabilidade que não estão presumidas no ChatGPT.

## 3. Segurança e portabilidade

**Veredito: APPROVE para absorção exclusivamente metodológica; CAUTION para instalar/rodar as automações originais.**

- README da HumanLayer sugere instalação com `npx skills add`; ela **não foi executada**.
- Templates de coding agents usam GitHub Actions, runners headless, tokens/secrets e comandos de shell; a existência no repositório externo não os torna disponíveis no ambiente local ou no ChatGPT.
- Triggers como `issue_comment` e comando `/iterate` exigem controle de identidade do ator, permissão de escrita, branch/PR visado, prevenção de injeção em texto não confiável e escopo mínimo das credenciais.
- Loops agendados podem produzir custos, PRs redundantes e alterações em cadeia; impor orçamento, limites de fila, evidência de validação e revisão humana.
- Não houve inspeção exaustiva de cada arquivo de workflow ou payload executável; por isso esta avaliação **não certifica segurança de instalação** de qualquer template/runner.
- Protocolo do benchmark depende de dataset, Docker/Python e infraestrutura própria para reprodução integral. Apenas princípios independentes do runner foram incorporados.

## 4. Ownership, implementação e commits publicados

| Ação | Owner/arquivo | Commit |
| --- | --- | --- |
| UPDATE_EXISTING | [skills/coding-agent-engineering/SKILL.md](../skills/coding-agent-engineering/SKILL.md): medição longitudinal, Strict/Core, resíduos, custo e replicabilidade | [4617ddac](https://github.com/paulociano/skill-arsenal/commit/4617ddac01cd867feb90f726a6e315bf3af6eac5) |
| UPDATE_EXISTING | [skills/software-testing-engineering/SKILL.md](../skills/software-testing-engineering/SKILL.md): suíte cumulativa e aceitação do checkpoint final | [abf6bb01](https://github.com/paulociano/skill-arsenal/commit/abf6bb01cdf8a96ed26591b00729baef30e97981) |
| UPDATE_EXISTING | [skills/software-factory-operations/SKILL.md](../skills/software-factory-operations/SKILL.md): back-pressure por loop, memória de feedback e autenticação de iteração | [7266f51d](https://github.com/paulociano/skill-arsenal/commit/7266f51d8f101d813bafaaea69a2d7dceea18245) |
| UPDATE_EXISTING | [skills/codebase-design/SKILL.md](../skills/codebase-design/SKILL.md): API de props baseada em callers de produção com ressalvas para consumers públicos | [cba223d1](https://github.com/paulociano/skill-arsenal/commit/cba223d19b4adec27a5f3559f7846e4c857e87d2) |

Sem novo owner e sem mudança material nas descriptions. Portanto **não foi necessário editar `ARSENAL INDEX.md`**. Não houve alteração em projetos consumidores nem instalação de tools externos.

## 5. Verificação e limites reais

- As quatro escritas foram publicadas via GitHub Contents API com SHA do blob lido no momento da mudança e commits separados, sem force-push.
- A verificação pós-escrita deve conferir marcadores e trechos relevantes nos quatro owners e a publicação deste registro.
- Isto é validação de **documentação metodológica publicada**, não prova de melhoria empírica em código real. Para demonstrar ganhos, aplicar a um projeto autorizado, executar testes Core/Strict em alterações sucessivas e comparar regressões, diff e custos contra baseline.
