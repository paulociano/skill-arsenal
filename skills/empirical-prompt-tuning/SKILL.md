---
name: empirical-prompt-tuning
description: "Avaliar e melhorar prompts ou skills mediante pedido de otimização empírica, com cenários fixos, baseline e holdout."
---

# empirical-prompt-tuning

## Objetivo

Melhorar empiricamente skills e prompts importantes através de cenários fixos, executores independentes, critérios pré-definidos e iteração até convergência.

## Quando usar

Avaliar e melhorar prompts ou skills mediante pedido de otimização empírica, com cenários fixos, baseline e holdout.

## Workflow

1. Verificar consistência entre trigger/description e o que o corpo realmente cobre.
2. Definir 2–3 cenários realistas, incluindo edge cases.
3. Fixar checklist de requisitos antes da avaliação, com pelo menos um requisito crítico.
4. Quando o ambiente permitir independência real, executar o prompt/skill em contexto fresco, evitando autoavaliação do próprio autor.
5. Medir sucesso, cobertura de requisitos, passos/retrabalho e pontos ambíguos.
6. Para cada falha, registrar `Issue → Cause → General Fix Rule`.
7. Aplicar o menor ajuste que resolva uma classe de falha por vez.
8. Reavaliar com contexto fresco e manter um ledger de padrões recorrentes.
9. Parar quando novas ambiguidades zerarem e melhorias estabilizarem; usar cenário hold-out para detectar overfitting.

## Convergência das avaliações

Em loops de melhoria:

- Gen 1 estabelece baseline completo.
- Após a avaliação, reabrir somente critérios/acceptance nodes que falharam ou regrediram.
- Congelar critérios PASS e apenas re-verificá-los nas bordas; não reescrevê-los sem nova evidência.
- Se a melhoria estagnar por várias rodadas, parar e mudar hipótese em vez de gastar até o limite.
- "estrutura/ontology estável" não equivale a sucesso: ainda precisa passar pelo executor/verifier real.
- working-set menor é observação de eficiência, não prova de economia sem medição comparável.

## Otimização de programas LLM

Quando a skill/prompt fizer parte de um programa LLM repetível:

- separar **program/module**, **metric**, **train inputs** e **eval/holdout**;
- definir a métrica antes de otimizar;
- registrar baseline do programa não otimizado;
- otimizar instruções, demonstrações/few-shot ou pesos como mecanismos diferentes, nunca como um pacote indistinto;
- aceitar bootstrapping somente quando as demonstrações geradas passam pelo verifier/metric;
- usar busca de candidatos orientada pela métrica em vez de reescrita intuitiva infinita;
- preservar dev/holdout para detectar overfitting;
- comparar ganho de qualidade com custo de otimização e custo de inferência;
- ao comparar harnesses/agentes, manter modelo, task set, recursos e policy de ambiente constantes; pin de commit/configuração e fresh restore por caso melhoram atribuição;
- mudança de provider, egress policy, hardware/runtime ou corpus deve ser registrada como diferença metodológica; sem matched control, não apresentar o resultado como diretamente comparável;
- salvar a versão otimizada e manter o programa original reproduzível;
- quando houver módulos múltiplos, avaliar se o ganho veio de uma parte específica antes de recompilar tudo.

Uma métrica ruim otimiza a coisa errada com eficiência. Metric design é parte da especificação.

## Avaliação de workflows completos

Para agentes/workflows completos, separar explicitamente:

1. **Prepare data** — começar com poucos casos representativos e crescer depois.
2. **Generate traces** — executar o agente e registrar trajetória real.
3. **Grade** — aplicar métricas adequadas ao tipo de caso.
4. **Analyze failures** — agrupar modos de falha antes de editar prompts.
5. **Fix/optimize** — alterar a menor causa plausível.
6. **Compare** — baseline vs candidate com as mesmas métricas.
7. **Holdout** — manter casos fora do loop para detectar overfitting.

Métricas devem corresponder ao que se quer medir: task success, trajectory, tool use, final response, grounding, safety ou checks determinísticos. Não baixar a barra para fazer o agente passar, não deletar caso “flaky” sem investigar a não-deterministicidade e não ajustar continuamente expected outputs quando o problema está no agente.

LLM-as-judge precisa de rubric explícita e, quando possível, checks determinísticos/human labels. Otimização automática cara deve vir depois de fixes manuais e com autorização explícita.

## Session-evidence tuning

Quando prompts, AGENTS.md, CLAUDE.md ou skills já foram usados em trabalho real:
- coletar sessões atribuíveis ao projeto/escopo;
- excluir sessões produzidas pelo próprio tuner para evitar self-training contamination;
- agrupar falhas recorrentes antes de editar memória/instruções;
- exigir evidência de múltiplas sessões distintas antes de add/rewrite/remove durável;
- limitar cada rodada a um pequeno gradient step;
- propostas são diffs revisáveis, não writes automáticos;
- separar escopo de projeto de escopo de usuário;
- manter ledger de evidência e decisões aceitas/rejeitadas;
- quotes/samples podem conter segredos, então redaction e boundary local importam.

A metáfora de gradient descent é útil apenas se o loop continuar empiricamente mensurável.


## Protocolo Autoresearch controlado (quando houver iterações mensuráveis)

Adaptar apenas os invariantes portáteis de Karpathy/autoresearch, uditgoenka/autoresearch, crashcartlabs/autoresearch-agent e darkroomengineering/cc-settings. Não presumir scripts, comandos slash, GPU, Claude subprocess, agentes independentes, avaliações pagas ou loops persistentes.

1. **Contrato selado antes do baseline:** registrar objetivo, arquivo(s) editáveis, versões, casos de teste, métrica primária e direção, avaliador imutável, guardrails de segurança/correção, limites de custo/tempo/rodadas e critérios de interrupção. Modificação do avaliador, corpus, modelo ou critério invalida a série e exige novo baseline; nunca otimizar alterando o juiz.
2. **Baseline repetido e ruído:** executar mais de uma amostra idêntica quando possível; estimar variabilidade de pontuação. Definir ganho mínimo superior ao ruído e à relevância prática. Se não houver amostragem independente, rotular apenas como revisão estrutural, não ganho empírico.
3. **Controle de valor incremental:** além do baseline original, comparar, quando executável em condições equivalentes, uma instrução simples de mesma intenção sem a skill. Não alegar valor da skill apenas por superar um prompt vazio.
4. **Blindagem train/holdout:** separar casos usados para diagnóstico de casos reservados para decisão. O otimizador não recebe textos, respostas ou justificativas do holdout; o resultado agregado é revelado somente no gate de decisão. Não ajustar cases ou checklist para acomodar a candidata; mudanças exigem nova série.
5. **Juiz auditável:** rubric binária ou métrica mecânica previamente definida; verificar ambiguidades com dupla avaliação do mesmo output quando possível. Isolar executor e avaliador, fixar configuração/modelo e comparar condições pareadas. Uma opinião na mesma sessão não equivale a benchmark cego.
6. **Mudança mínima e decisão:** uma hipótese por rodada; checar métrica, holdout, corretude, segurança e custo de complexidade. Preservar somente ganho acima do limiar e sem regressões críticas. Empate com simplificação pode ser aceito apenas sob critérios de equivalência predefinidos, nunca ignorando guardrails.
7. **Trilha reversível:** registrar run ID, base commit/hash, candidato, diff, seed/config, score baseline/candidato, desvio/ruído, holdout agregado, veto, decisão (keep/discard/crash/overfit), tempo/custo e limites. Fazer mudanças via patches revisáveis; nunca usar `git reset --hard`, exclusão ampla ou reescrita de histórico em workspace compartilhado. Reverter somente arquivos do escopo com estado anterior verificado.
8. **Parada segura:** teto finito de iterações e orçamento, interrupção em falha de teste, acesso inesperado a segredos, alteração fora do escopo, ruído dominante ou estagnação. Loops ininterruptos e execução em background não são capacidades implícitas do ChatGPT.

**Casos de aceitação:** should-trigger: "otimize esta skill em cinco experimentos com pontuação e holdout"; near-miss: "melhore a redação deste parágrafo" (edição única sem benchmark); veto: aumento de score com quebra de segurança ou piora relevante no holdout. Quando ferramentas para execução independente não existirem, entregar protocolo, diff e limites sem inventar resultados.

**Proveniência:** princípios de escopo, orçamento fixo, métrica congelada e registro de [karpathy/autoresearch](https://github.com/karpathy/autoresearch); métrica genérica e mínima alteração de [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch); bounds, snapshots e guardrails de [crashcartlabs/autoresearch-agent](https://github.com/crashcartlabs/autoresearch-agent); ruído, blindagem do holdout e controle de instrução simples de [darkroomengineering/cc-settings](https://github.com/darkroomengineering/cc-settings/blob/main/skills/autoresearch/SKILL.md). Adaptação metodológica, não instalação dos executores originais.


## Otimização em lote de um catálogo de skills

Quando o pedido envolver **todas** as skills, não interpretar "cinco experimentos" como autorização para reescrever o catálogo de uma vez. Trabalhar por skill e registrar o estado de cada owner, podendo agrupar hipóteses globais somente quando o efeito for mensurável individualmente.

1. Fixar inventário canônico do GitHub, commit base, lista completa de `skills/*/SKILL.md` e divisão reproduzível em cohort de diagnóstico e holdout por casos de teste (não por nome de arquivo apenas). Não confundir revisão de frontmatter com execução comportamental.
2. Para cada skill: estabelecer cenários should-trigger, near-miss e adversarial; verificar baseline no runtime realmente disponível e com settings constantes. Ausência de executor isolado, credenciais, dados ou ferramenta necessária = `blocked_unmeasured`, não zero nem PASS.
3. Definir até cinco **experimentos de hipótese/candidata por skill** quando o pedido especificar cinco. Não contar leitura, lint, análise estática ou cinco checklists como cinco experimentos de melhoria. Uma rodada requer candidata material, teste sobre baseline e decisão.
4. Registrar por rodada: fonte/ref base, hipótese, diff permitido, entrada train, métrica e direção, repetição/ruído, holdout oculto, regressões críticas, custo, decisão, evidência e commit (se promovido).
5. Não fazer modificação homogênea em massa sem falha compartilhada evidenciada; preferir fixes por família de falha com owner específico. Sem prova de valor e regressão, manter o texto original.
6. Guardrail global: comparabilidade de métricas por domínio é limitada; agregar cobertura (`measured / total`), `kept`, `reverted`, `blocked` e não um score subjetivo único para todas as skills. Revalidar referências de índice e portabilidade após publicação.
7. Encerrar informando exatamente quantas skills tiveram baseline real, cinco experimentos completos, holdout executado e publicação verificada. Nunca declarar "todas otimizadas" com amostra ou plano.

## Ferramentas e dependências

Usar execuções independentes apenas quando disponíveis e autorizadas; não criar novas tarefas do usuário para simular testes. Sem contexto fresco e execução real, entregar revisão estrutural e não alegar validação empírica. Otimização paga exige orçamento autorizado.

## Referências

Adaptada de [mizchi/skills · empirical-prompt-tuning](https://github.com/mizchi/skills/tree/main/empirical-prompt-tuning).

kunchenguid/backpass acrescentou tuning baseado em sessões reais, evidence-gated edits de múltiplas sessões, small bounded steps e human apply gate. O Arsenal não presume stores/harnesses específicos nem acpx.

Origem local: [empirical-prompt-tuning.docx](../empirical-prompt-tuning.docx).
