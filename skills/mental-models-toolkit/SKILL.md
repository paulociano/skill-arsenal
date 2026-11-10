---
name: mental-models-toolkit
description: "Escolher e aplicar o modelo mental certo (ou nenhum) para diagnosticar, decidir, entender, criar, avaliar, prever ou otimizar: pre-mortem, reversibilidade, custo de oportunidade, segunda ordem, Cynefin, teoria das restrições, jobs-to-be-done, steel-manning e outros, com roteador que devolve NENHUM, um ou no máximo três."
---

# mental-models-toolkit

## Objetivo

Melhorar raciocínio em decisões, diagnósticos e análises escolhendo o enquadramento pelo **mecanismo** que ele oferece, não por hábito, e aplicá-lo de forma verificável. O padrão é **nenhum ou um** modelo.

## Quando usar

- Uma decisão, diagnóstico ou análise em que o enquadramento certo não é óbvio e um erro de enquadramento custa caro (decisão de carreira, contratação, estratégia comercial, investimento, priorização de time).
- O usuário pede "me ajuda a pensar", "qual modelo mental", "pre-mortem", "segunda ordem" etc.

## Quando não usar

- Execução rotineira de um plano já decidido; sintaxe de código; tarefa sem incógnita analítica → raciocinar direto.
- O modelo já é óbvio pelo pedido ("onde está o gargalo?" → teoria das restrições): aplicar direto, sem rotear para mostrar.
- Decisão estruturada com alternativas, critérios e evidências → `decision-analysis` (pode usar um modelo daqui como lente).

## Roteador

1. **Atalho.** Se um modelo claramente serve pelo mecanismo, usar só ele. Se nenhum melhora o trabalho, responder **NENHUM** e raciocinar direto.
2. **Caracterizar.** Domínio (negócio, carreira, produto, finanças, time, técnico, pessoal) e tipo de problema (diagnosticar, decidir, entender, criar, avaliar, prever, otimizar). Anotar tempo, informação disponível, risco e reversibilidade.
3. **Padrão por tipo** (mudar quando as restrições pedirem):
   - Diagnosticar → cinco porquês+ ou método científico (Kepner-Tregoe se precisar separar onde o problema É e NÃO É)
   - Decidir → reversibilidade primeiro; depois custo de oportunidade ou probabilístico
   - Entender → sistemas (mapa × território se o modelo diverge da realidade; Cynefin se não está claro que tipo de situação é)
   - Criar → primeiros princípios (effectuation quando se parte dos meios disponíveis; via negativa para tirar antes de pôr)
   - Avaliar um argumento → steel-manning (socrático se o problema são definições e premissas)
   - Prever → probabilístico
   - Otimizar → teoria das restrições (OODA sob pressão de tempo; racionalidade limitada para saber quando parar de buscar)
   - Risco / "o que pode dar errado?" → pre-mortem ou red team; margem de segurança para colchões
   - "O que construir/oferecer?" → jobs-to-be-done
   - Competência e durabilidade → círculo de competência, efeito Lindy
4. **Segundo ou terceiro modelo só por exceção**, quando cada um responde uma pergunta que o primeiro deixa aberta. Máximo três; preferir em sequência; sinônimos não se somam.
5. **Saída.** Se o enquadramento está forçado, ignora fatores importantes ou não gera percepção nova em pouco tempo, trocar uma vez ou voltar para NENHUM.

Registrar a escolha em poucas linhas: modelo, papel, pergunta que só ele responde, ponto cego que sobra, quando abandonar.

## Catálogo (pergunta central → como aplicar → sinal de parada)

- **Reversibilidade** — dá para desfazer, a que custo e em quanto tempo? → separar decisões de mão dupla (decidir rápido, testar) de mão única (mais evidência, mais gente). → parar se tudo foi classificado como irreversível por medo.
- **Custo de oportunidade** — qual o melhor uso alternativo do mesmo tempo, dinheiro ou atenção? → comparar com a melhor alternativa concreta, não com "não fazer nada". → parar se a alternativa é imaginária.
- **Probabilístico** — qual a taxa-base e a faixa plausível? → partir da taxa-base de casos parecidos, ajustar com evidência específica, dar faixa, dizer o que mudaria a estimativa. → nunca inventar número com falsa precisão.
- **Segunda ordem** — e depois? → seguir efeitos atrasados, incentivos criados e reações de outras pessoas por duas ou três rodadas. → parar quando os efeitos ficam especulativos demais para mudar a decisão.
- **Pre-mortem** — imagine que deu errado daqui a seis meses: por quê? → listar causas plausíveis de fracasso, priorizar por probabilidade × impacto, transformar as principais em ações ou gatilhos de alerta. → não vira lista infinita de medos: manter as que mudam o plano.
- **Red team** — como um adversário ou concorrente exploraria isso? → atacar o plano pelos pontos mais fracos, com mandato de achar falha. → separar crítica fundamentada de pessimismo genérico.
- **Margem de segurança** — quanto colchão existe se as premissas errarem? → dimensionar folga em prazo, caixa, capacidade ou preço contra o erro plausível das premissas. → folga excessiva também tem custo de oportunidade.
- **Steel-manning** — qual a versão mais forte do argumento contrário? → reconstruir o melhor caso do outro lado antes de responder. → se não consegue formulá-lo de forma que o outro lado aceitaria, ainda não entendeu.
- **Socrático** — o que exatamente queremos dizer com isso, e como sabemos? → perguntar por definições, premissas, evidência e implicações, uma de cada vez. → parar quando as premissas críticas estão explícitas.
- **Primeiros princípios** — o que é verdade de forma independente da convenção? → decompor até restrições físicas, econômicas ou legais reais e remontar. → evitar reinventar o que a convenção já resolveu bem.
- **Via negativa** — o que tirar melhora mais do que acrescentar? → listar o que remover (etapas, reuniões, regras, produtos) antes de propor adições.
- **Effectuation** — com o que eu já tenho (quem sou, o que sei, quem conheço), o que dá para fazer agora? → partir dos meios, perda aceitável e parcerias, não de previsão. → útil em incerteza alta; ruim quando a previsão é confiável.
- **Sistemas** — quais estoques, fluxos e ciclos de reforço ou equilíbrio explicam o comportamento? → desenhar as relações e procurar o ciclo dominante e os atrasos. → não confundir diagrama bonito com explicação testada.
- **Mapa × território** — onde o modelo, a planilha ou o relatório diverge da realidade? → checar a premissa contra dado de campo antes de agir no modelo.
- **Cynefin** — a situação é clara, complicada (especialista resolve), complexa (só experimentando) ou caótica (agir para estabilizar)? → escolher o modo de agir pelo tipo de situação.
- **Cinco porquês+** — qual a causa sistêmica por trás da causa imediata? → perguntar "por quê" com evidência em cada nível e parar numa causa que dá para corrigir. → não usar antes de localizar o problema.
- **Método científico** — qual hipótese explica, e qual o teste mais barato que as diferencia? → ranquear causas e rodar o discriminador mais barato primeiro.
- **Kepner-Tregoe** — onde, quando e em quem o problema acontece, e onde não acontece? → a diferença entre É e NÃO É aponta a causa.
- **Teoria das restrições** — qual é o único gargalo que limita o resultado? → identificar, explorar, subordinar o resto, elevar e repetir. → melhorar fora do gargalo não aumenta o resultado.
- **OODA** — observar, orientar, decidir, agir, em ciclos curtos, quando o ambiente muda rápido.
- **Racionalidade limitada** — quando parar de buscar? → definir antes o critério de "bom o suficiente" e parar ao atingi-lo.
- **Jobs-to-be-done** — que progresso a pessoa está tentando fazer, em que situação? → descrever o "trabalho" do cliente, os concorrentes reais (inclusive não fazer nada) e o que provoca a troca.
- **Círculo de competência** — isso está dentro do que eu (ou o time) sei avaliar de verdade? → fora do círculo: buscar quem sabe, reduzir aposta ou não decidir sozinho.
- **Efeito Lindy** — para coisas não perecíveis (ideias, práticas, tecnologias), o que dura há mais tempo tende a durar mais. → usar como prior, não como prova.
- **Experimento mental** — se isso fosse verdade, o que mais teria de ser verdade? → montar o cenário hipotético controlado e checar consequências.

## Guardrails

- Modelo é ferramenta de raciocínio, não evidência. Conclusões continuam precisando de dados quando o tema é factual.
- Não empilhar modelos para parecer rigoroso; "NENHUM" é uma resposta correta.
- Em finanças, carreira ou decisões de terceiros, preservar a decisão humana e explicitar incerteza.

## Integração

`decision-analysis` (lentes adversariais), `root-cause-analysis`, `scenario-forecasting`, `prioritization-engine`, `experiment-design`.

## Origem

Roteador e catálogo adaptados de [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) (MIT; `skills/thinking-model-router/SKILL.md` e lista de 28 skills), avaliado em 2026-11-10. Textos reescritos e condensados em português; não foram importados os evals do repositório, que não foram executados (garantia `static_only`).
