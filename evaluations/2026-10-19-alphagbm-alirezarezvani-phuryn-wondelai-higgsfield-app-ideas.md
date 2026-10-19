# Arsenal Autopilot: seis fontes externas (2026-10-19)

## Escopo e fonte canônica
Consulta inicial a `ARSENAL INDEX.md`, `AGENTS.md`, `stacks/arsenal-autopilot/STACK.md` e `stacks/evaluate-and-import-skill/STACK.md` da branch `master` do repositório `paulociano/skill-arsenal`. Fontes externas examinadas em seus respectivos branches padrão, usando GitHub metadata, README, tree e SKILL.md seletivos. A avaliação não é auditoria exaustiva de todas as centenas de arquivos de cada catálogo (muitos são mirrors de agentes).

## Decisões por fonte
1. **AlphaGBM/skills — A/D; UPDATE_EXISTING**. https://github.com/AlphaGBM/skills. Pesquisa de equities/options e revisão de snapshots; README e `skills/core/alphagbm-investment-review/SKILL.md`, `alphagbm-news-impact`, `alphagbm-stock-research`. Valor incremental: comparação temporal exigindo mesma identidade/versão/unidade, separação entre notícia, inferência e tese, checkpoint futuro. **Implementado em** `skills/investment-portfolio-analysis/SKILL.md`. **Não adotado**: API/runner proprietários, API key, gasto de cota, workflows de backend em preview. Sem presumir disponibilidade dos scores ou dados.
2. **alirezarezvani/claude-skills — A/B/D; UPDATE_EXISTING seletivo**. https://github.com/alirezarezvani/claude-skills. Biblioteca multifuncional e mirrors para vários agentes. Foram lidos `marketing-skill/skills/aeo/SKILL.md` e `marketing-skill/skills/business-name-fit/SKILL.md`. **Implementado em** `skills/seo-research-audit/SKILL.md` (AEO com observações reais e ledger de citações) e `skills/brand-strategy/SKILL.md` (fit intercultural do naming). **Não adotado**: install scripts, badges como evidência de eficácia, alegações causais sobre ranking de LLM sem teste, agentes/companions específicos de Claude.
3. **phuryn/pm-skills — A/B; UPDATE_EXISTING**. https://github.com/phuryn/pm-skills. README e `pm-product-discovery/skills/opportunity-solution-tree/SKILL.md`, `prioritize-assumptions`, `pm-execution/skills/strategy-red-team/SKILL.md`. **Implementado em** `skills/idea-refine/SKILL.md`: outcome → oportunidade → soluções → experimento, ataques honestos a premissas críticas, kill criteria e testes baratos. **Não adotado**: score arbitrário, importação dos plugins e comandos Claude, criação de owners duplicados.
4. **wondelai/skills — A/B/C; UPDATE_EXISTING**. https://github.com/wondelai/skills. README, `plugins/product-strategy/skills/mom-test/SKILL.md` e `plugins/marketing-cro/skills/scorecard-marketing/SKILL.md`. **Implementado em** `skills/discovery-research-synthesis/SKILL.md`: evidência de comportamento passado, alternativas, compromisso real, classificação distinta de intenção vs fato. **Não adotado**: scoring mecânico 7/7, promessas de conversão não sustentadas e captura de email antes de entregar valor como regra universal.
5. **higgsfield-ai/skills — A/D; UPDATE_EXISTING seletivo**. https://github.com/higgsfield-ai/skills. README, `higgsfield-soul-id/SKILL.md`, `higgsfield-generate/SKILL.md`, `higgsfield-youtube-thumbnail/SKILL.md`. **Implementado em** `skills/character-continuity/SKILL.md` (gates de consentimento, modelo de identidade vs atlas, verificação de backend) e `skills/high-fidelity-image-generation/SKILL.md` (capas/miniaturas legíveis e honestas). **Não adotado**: `curl|sh`, CLI pressuposta, treino facial sem plano/autorização, nomes de modelos não verificados ou dependências de custo.
6. **florinpop17/app-ideas — B; ABSORB_METHOD_ONLY**. https://github.com/florinpop17/app-ideas. Coleção educacional em Markdown, não uma Agent Skill. README e `Projects/1-Beginner/Calculator-App.md` lidos. **Implementado em** `skills/idea-refine/SKILL.md`: distinguir exercício de portfólio de empreendimento real, especificar objetivo, user stories essenciais, restrições, edge cases, bônus e níveis. **Não adotado**: importação de listas de projetos como skills, ou atribuir demanda comercial a exercícios.

## Capability ledger e ownership

| Incremento | Owner | Decisão |
|---|---|---|
| Comparação longitudinal verificável de análise de investimentos | `investment-portfolio-analysis` | UPDATE_EXISTING |
| AEO e observação de citações de LLMs | `seo-research-audit` | UPDATE_EXISTING |
| Naming intercultural | `brand-strategy` | UPDATE_EXISTING |
| Opportunity Solution Tree e red team de premissas | `idea-refine` | UPDATE_EXISTING |
| Discovery baseado em comportamento e compromisso | `discovery-research-synthesis` | UPDATE_EXISTING |
| Identidade facial externa vs atlas, consentimento e validação | `character-continuity` | UPDATE_EXISTING |
| Capas/miniaturas com hierarquia e promessa verdadeira | `high-fidelity-image-generation` | UPDATE_EXISTING |
| Exercícios progressivos de desenvolvimento | `idea-refine` | ABSORB_METHOD_ONLY (incorporado) |

## Segurança e limites
Nenhum instalador externo foi executado; nenhuma API key coletada; nenhuma trade/ordem, compra de análise ou treino de rosto submetido; nenhum modelo proprietário ou servidor suposto disponível. Conteúdo externo tratado como documentação não confiável. Validar runtimes reais e consentimento antes de usar APIs ou fotos. O Arsenal foi adaptado metodologicamente, não recebeu integrações externas automáticas.

## Materialização
Foram modificados e publicados diretamente na branch canônica:
- `skills/investment-portfolio-analysis/SKILL.md`
- `skills/idea-refine/SKILL.md`
- `skills/discovery-research-synthesis/SKILL.md`
- `skills/brand-strategy/SKILL.md`
- `skills/seo-research-audit/SKILL.md`
- `skills/character-continuity/SKILL.md`
- `skills/high-fidelity-image-generation/SKILL.md`
- este registro em `evaluations/`.

Nenhuma nova skill ou mudança material de descrição/frontmatter; o `ARSENAL INDEX.md` mantém roteamento válido, sem necessidade de edição. Validação de publicação: confirmar arquivos via releitura remota após escrita. Não executados testes funcionais de apps externos.
