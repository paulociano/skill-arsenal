# Avaliação — Top 20 repositórios mais estrelados do GitHub

Data: 2026-10-03

Fonte de descoberta: https://viktorkav.com.br/top-github/
Fonte canônica do Arsenal: https://github.com/paulociano/skill-arsenal

## Escopo

O lote foi tratado como radar de descoberta, não como autorização para importar catálogos em massa. A comparação foi feita por capability e ownership contra o ARSENAL INDEX atual.

Nenhum installer, setup script, plugin ou binário das fontes foi executado.

## Resultado executivo

- 20 repositórios triados.
- 6 fontes aprofundadas por potencial metodológico: obra/superpowers, affaan-m/ECC, openclaw/openclaw, NousResearch/hermes-agent, codecrafters-io/build-your-own-x e practical-tutorials/project-based-learning.
- 1 nova skill criada: git-worktree-lifecycle.
- 2 owners existentes refinados: skill-builder e session-learn.
- Nenhum runtime externo foi instalado.
- Catálogos e grandes codebases permaneceram como referência, não como skills.

## Ledger

| # | Repositório | Classe | Decisão | Razão |
|---|---|---|---|---|
| 1 | codecrafters-io/build-your-own-x | B | KEEP_EXTERNAL_REFERENCE | Método aprender reconstruindo já está absorvido por teach; sem capability nova suficiente. |
| 2 | sindresorhus/awesome | B | KEEP_EXTERNAL_REFERENCE | Excelente radar de fontes, mas não é workflow operacional. |
| 3 | freeCodeCamp/freeCodeCamp | B/D | KEEP_EXTERNAL_REFERENCE | Currículo/plataforma útil; teach já referencia a fonte e possui progressão pedagógica própria. |
| 4 | public-apis/public-apis | D | KEEP_EXTERNAL_REFERENCE | Catálogo de dados/APIs, útil como fonte pontual; não é skill. |
| 5 | EbookFoundation/free-programming-books | B | KEEP_EXTERNAL_REFERENCE | Biblioteca de aprendizagem; sem comportamento operacional incremental. |
| 6 | openclaw/openclaw | A/D | KEEP_EXTERNAL_REFERENCE | Arquitetura de gateway, tools, channels e segurança é relevante, mas depende de runtime amplo e já há owners como agent-action-governance, agent-memory-engineering e computer-use-agent-engineering. |
| 7 | developer-roadmap | B | KEEP_EXTERNAL_REFERENCE | Boa metodologia de trilhas; teach já cobre progressão por domínio e múltiplas sessões. |
| 8 | donnemartin/system-design-primer | B | KEEP_EXTERNAL_REFERENCE | Conteúdo de system design; owner existente é system-design-engineering. |
| 9 | jwasham/coding-interview-university | B | KEEP_EXTERNAL_REFERENCE | Plano de estudos útil; owner existente é teach. |
| 10 | vinta/awesome-python | B/D | KEEP_EXTERNAL_REFERENCE | Catálogo técnico, não metodologia autônoma. |
| 11 | awesome-selfhosted/awesome-selfhosted | B/D | KEEP_EXTERNAL_REFERENCE | Radar de software self-hosted; usar por pesquisa, não importar como skill. |
| 12 | 996icu/996.ICU | C | REJECT | Repositório histórico/manifesto sem capability reutilizável para o Arsenal. |
| 13 | practical-tutorials/project-based-learning | B | ABSORB_METHOD_ONLY | Reforça aprender construindo, já coberto por teach; nenhuma mudança necessária. |
| 14 | obra/superpowers | A/B/D | CREATE_NEW + UPDATE_EXISTING | Maior delta do lote. Worktree/branch lifecycle justificou owner novo; writing-skills trouxe refinamento de metadata/trigger para skill-builder. TDD, debugging, review, planning e verification já tinham owners. |
| 15 | facebook/react | D | KEEP_EXTERNAL_REFERENCE | Codebase/framework, não skill. Consultar apenas quando tarefa React exigir fonte técnica. |
| 16 | torvalds/linux | D | KEEP_EXTERNAL_REFERENCE | Kernel/codebase, não metodologia de agente. |
| 17 | trimstray/the-book-of-secret-knowledge | B/D | KEEP_EXTERNAL_REFERENCE | Runbook e coleção de comandos; alto risco de copiar snippets fora de contexto. Usar como fonte sob demanda. |
| 18 | affaan-m/ECC | A/B/D | UPDATE_EXISTING + KEEP_EXTERNAL_REFERENCE | Arsenal já absorvia ECC em surgical-engineering. continuous-learning-v2 acrescentou regra útil de escopo antes de promoção para session-learn; git-workflow serviu como contraste para a nova skill de worktree. Runtime/hooks permanecem externos. |
| 19 | TheAlgorithms/Python | B | KEEP_EXTERNAL_REFERENCE | Código didático; teach já referencia TheAlgorithms. |
| 20 | NousResearch/hermes-agent | A/D | KEEP_EXTERNAL_REFERENCE | Learning loop, memória, automações e delegação são relevantes, porém runtime-heavy e amplamente cobertos por session-learn, agent-memory-engineering, automations e multi-agent-orchestration. |

## Superpowers — capability mapping

| Fonte | Owner no Arsenal | Decisão |
|---|---|---|
| brainstorming | idea-refine / to-spec / project-planning | Não importar. O hard-gate universal de aprovação é mais rígido que o necessário no ambiente atual. |
| systematic-debugging | diagnosing-bugs | Overlap forte. |
| test-driven-development | tdd | Overlap forte. |
| verification-before-completion | verify-before-claim | Overlap forte. |
| requesting/receiving-code-review | code-review | Overlap forte. |
| dispatching-parallel-agents / subagent-driven-development | multi-agent-orchestration / software-factory-operations | Overlap forte e dependente de ferramentas reais de delegação. |
| writing-plans | project-planning / to-tickets | Overlap forte. |
| executing-plans | surgical-engineering / software-factory-operations | Método útil, mas não suficiente para novo owner separado neste lote. |
| using-git-worktrees + finishing-a-development-branch | git-worktree-lifecycle | Novo owner criado. |
| writing-skills | skill-builder | Absorção metodológica: metadata deve favorecer trigger/when-to-use e não substituir o corpo da skill. |

## ECC — capability mapping

- git-workflow: referência complementar para branching e integração; não importado como skill ampla.
- strategic-compact/context-budget: forte dependência do runtime Claude/ECC; overlap com response-latency-optimization e codex-cost-efficiency.
- continuous-learning-v2: projeto-local versus global é um bom princípio; absorvido em session-learn sem hooks, background agents ou promoção automática.
- hooks, agents, installers e packages: não portados sem equivalente real.

## OpenClaw e Hermes

Ambos são sistemas técnicos completos, não skills portáveis. Há valor arquitetural em:
- gateway/control plane;
- memória e continuidade;
- delegação;
- scheduling;
- isolamento e policy;
- ferramentas e channels.

Esse valor já possui owners no Arsenal. Não foi encontrada uma capability suficientemente nova para justificar importação direta.

## Segurança e portabilidade

- obra/superpowers, ECC, OpenClaw e Hermes oferecem installers/plugins/hooks ou runtimes próprios.
- OpenClaw e Hermes documentam instalação por scripts remotos; esses installers não foram executados.
- A avaliação preservou somente metodologia portável.
- Nenhuma credencial, hook, daemon, background learner ou auto-modificação foi habilitado.
- Worktree lifecycle foi escrito de forma tool-neutral e exige capacidades Git reais.
- Promoção automática de padrões pessoais entre projetos foi rejeitada; session-learn mantém revisão e escopo explícitos.

## Mudanças adotadas

1. CREATE_NEW — skills/git-worktree-lifecycle/SKILL.md
2. UPDATE_EXISTING — skills/skill-builder/SKILL.md
3. UPDATE_EXISTING — skills/session-learn/SKILL.md
4. UPDATE_EXISTING — stacks/software-engineering-cycle/STACK.md
5. UPDATE_EXISTING — ARSENAL INDEX.md e README.md

## Critério de parada

O lote encerra com todas as 20 fontes classificadas, owners definidos para o valor adotado e sem runtime externo prometido como disponível.
