# Avaliação: ecossistema Karpathy Autoresearch (2026-10-12)

## Escopo e fonte
- Canonical Arsenal: https://github.com/paulociano/skill-arsenal (branch master, índice `ARSENAL INDEX.md`, regras `AGENTS.md`).
- Fontes examinadas em suas branches default:
  - https://github.com/karpathy/autoresearch (master, README.md e program.md, último push observado 2026-03-26)
  - https://github.com/uditgoenka/autoresearch (master, README.md, COMPARISON.md, estrutura de scripts, último push observado 2026-08-12)
  - https://github.com/crashcartlabs/autoresearch-agent (main, SKILL.md, README.md e estrutura de scripts, último push observado 2026-08-02)
  - https://github.com/darkroomengineering/cc-settings (main, skills/autoresearch/SKILL.md e raiz, último push observado 2026-10-12)
- Profundidade: avaliação documental, arquitetura e superfícies de execução; não executamos scripts externos nem instaladores. Não equivale a auditoria linha a linha de cada script nem a ensaio empírico.
- Owners existentes comparados: `skills/empirical-prompt-tuning/SKILL.md`, `skills/experiment-design/SKILL.md`, `skills/skill-security-review/SKILL.md`, `skills/verify-before-claim/SKILL.md`, `stacks/evaluate-and-import-skill/STACK.md` e `stacks/arsenal-autopilot/STACK.md`.

## Veredito por fonte

| Fonte | Classificação | Ganho incremental | Decisão | Segurança / portabilidade |
|---|---|---|---|---|
| karpathy/autoresearch | B/D | Separação invariável entre agente editando `train.py`, avaliador em `prepare.py`, budget fixo, TSV e critério de simplicidade | ABSORB_METHOD_ONLY na skill existente | CAUTION para execução: instalador curl-pipe-shell no README, download de dataset, PyTorch + GPU NVIDIA, loops sem limite e git reset; não executar/importar |
| uditgoenka/autoresearch | A/D | Generalização de metas mensuráveis, thresholds de ruído, análise de estagnação e verificadores | ABSORB_METHOD_ONLY | CAUTION: scripts shell, plugins/hooks Claude, comandos de instalação, automação de ship/segurança e subprocess dependentes de runtime; não instalar |
| crashcartlabs/autoresearch-agent | A/D | Runs limitados, verifier congelado, guardrails, snapshots estritos, score privado, status/log de lineage, stop rules | ABSORB_METHOD_ONLY | CAUTION: `autoresearch_loop.py` executa verificadores fornecidos por quem configura, reescreve/restaura targets; precisa sandbox, allowlist, version pin, owner approval; não copiar |
| darkroomengineering/cc-settings (subskill autoresearch) | A/D | Calibração de judge e noise floor, holdout oculto ao otimizador, controle comparando skill vs instrução mínima, veto por segurança/correção | UPDATE_EXISTING com ideias portáveis | CAUTION: pressupõe `claude -p`, config isolation e `git reset --hard`; risco de sobrescrever mudanças externas e custo de modelos. Não instalar workflow |

## Capability ledger e ownership
- **Experimentos mensuráveis com baseline e holdout**: já pertenciam a `empirical-prompt-tuning` e `experiment-design`. UPDATE_EXISTING, sem nova skill.
- **Calibração do ruído e do próprio juiz**: novidade incremental significativa; UPDATE_EXISTING `empirical-prompt-tuning`.
- **Holdout verdadeiramente oculto e regra de rebaseline**: novidade incremental; UPDATE_EXISTING.
- **Controle contra instrução simples e benefício marginal de skill**: novidade incremental; UPDATE_EXISTING.
- **Contrato selado, lineage, checkpoints/reversão escopada e budgets**: UPDATE_EXISTING; integração de método, sem copiador de snapshots, hooks ou agent CLI.
- **Loop indefinido, deploy, security swarm, instalação, subprocess Claude e execução overnight**: REJECT como padrão não-portável/permissivo.
- **GPU training com `train.py` específico**: KEEP_EXTERNAL_REFERENCE; é aplicação de ML, não habilidade universal do Arsenal.
- **Marketing, vendas, debug, security e shipping subcomandos**: REJECT como pacote genérico; owners existentes no Arsenal e ausência de prova incremental.

## Gates de segurança
1. Não executar scripts, curl-install, `uv sync`, hooks, CLIs de modelo ou download de dependências somente para avaliação.
2. Fontes remotas contêm código e instruções de agente não confiáveis. Não incorporar instrução `NEVER STOP`, autoaprovação, ferramenta shell sem confirmação ou reset destrutivo.
3. Congelar avaliador, inputs, custo e guardrails antes das mudanças. Mudança exige nova série.
4. Acesso a segredos, rede, produção, dados privados ou alterações fora de allowlist: veto e interrupção; sem execução automática.
5. Os arquivos do Arsenal adotam apenas texto metodológico. Não criam subprocess, hooks, cron, dependências ou acesso externo.
6. Parecer global: **APPROVE para adaptação textual limitada; CAUTION para executar implementações externas**. Sem scanner estático dedicado e sem teste de execução: ausência de evidência de ameaça não constitui certificação de segurança.

## Prova de valor incremental (design, não benchmark executado)
- **Should-trigger**: `arsenal: otimize uma skill em cinco rodadas com baseline medido, holdout e teto de custo`; agora define gates de ruído, julgamento, decisão, rollback e parada.
- **Near-miss**: `reformule esta frase`; não deve disparar otimização experimental.
- **Adversarial**: candidata melhora score público e piora segurança ou holdout; veto, sem promoção.
- **Condição de aceitação real**: medir saídas de baseline e candidata com mesma configuração e um avaliador fixo, pelo menos uma repetição para estimar ruído e casos realmente reservados; registrar decisão e verificar reversão.
- **Status**: melhoria contratual/estrutural verificada pela leitura de arquivos e diff; não houve executor isolado nem provas de uplift medidas. Nenhuma afirmação de ganho estatístico.

## Alterações realizadas
- UPDATE_EXISTING: `skills/empirical-prompt-tuning/SKILL.md`, seção `Protocolo Autoresearch controlado`.
- Sem nova skill, sem nova stack, índice preservado porque name/description não mudaram.
- Registro desta avaliação para rastreabilidade das quatro fontes e decisões.

## Limitações e próximos checks
- Revisão documental parcial das dependências de fontes externas; para instalar qualquer runtime, fazer revisão dos scripts completos, testes e hashes do commit pinado.
- Para comprovar benefício prático, rodar benchmark supervisionado em casos independentes com custo autorizado; não confundir checklist proposto com resultado.
- Verificar após o commit esta avaliação e o corpo da skill na branch oficial; rechecagem de frontmatter, heading e ausência de nomes adicionais no índice.
