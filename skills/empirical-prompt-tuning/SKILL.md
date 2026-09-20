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

## Ferramentas e dependências

Usar execuções independentes apenas quando disponíveis e autorizadas; não criar novas tarefas do usuário para simular testes. Sem contexto fresco e execução real, entregar revisão estrutural e não alegar validação empírica. Otimização paga exige orçamento autorizado.

## Referências

Adaptada de [mizchi/skills · empirical-prompt-tuning](https://github.com/mizchi/skills/tree/main/empirical-prompt-tuning).

Origem local: [empirical-prompt-tuning.docx](../empirical-prompt-tuning.docx).
