---
name: coaching-development-loop
description: "Transformar evidências de desempenho ao longo do tempo em coaching longitudinal, distinguindo melhoria, regressão e padrão estável e fechando o ciclo com prática observável e nova verificação."
---

# Coaching Development Loop

## Objetivo
Converter feedback episódico em desenvolvimento verificável: **baseline → comportamento-alvo → prática → nova observação → tendência → próximo ajuste**.

## Quando usar
- acompanhar evolução de vendedor, consultor ou liderado ao longo de semanas;
- comparar calls, reuniões ou entregas antigas e recentes;
- preparar 1:1 de desenvolvimento baseado em evidência;
- verificar se um feedback anterior mudou comportamento;
- escolher uma prioridade de coaching em vez de entregar uma lista de correções.

Para feedback de um evento isolado, use `golden-circle-feedback`. Para pontuar uma ligação específica contra o Card, use `call-evaluation`.

## Inputs
- pessoa e papel;
- comportamento/outcome a desenvolver;
- evidência anterior e recente comparável;
- feedback/acordo anterior quando existir;
- contexto de tarefa, estágio e expectativa;
- métricas de resultado somente como contexto, não substituto de comportamento observado.

## Workflow
1. **Definir comparação** — explicitar períodos/conjuntos e garantir comparabilidade suficiente de tarefa, estágio, canal ou tipo de interação.
2. **Construir baseline** — extrair poucos comportamentos observáveis da evidência antiga. Não transformar impressão do gestor em baseline factual.
3. **Ler período recente** — procurar os mesmos comportamentos e também mudanças não previstas.
4. **Classificar por comportamento**:
   - `improved`: mudança direcional sustentada por evidência comparável;
   - `regressed`: piora sustentada;
   - `stable`: padrão repetido sem direção clara;
   - `inconsistent`: sinais mistos;
   - `insufficient evidence`: amostra/cobertura não permite tendência.
5. **Separar outcome de execução** — resultado comercial pode melhorar/piorar por fatores externos. Use-o para priorizar investigação, não para inventar comportamento.
6. **Escolher foco** — selecionar normalmente uma prioridade principal de coaching por ciclo, considerando impacto, frequência, capacidade de prática e dependências.
7. **Desenhar prática curta**:
   - comportamento específico;
   - sinal `if` que deve dispará-lo;
   - ação `then`;
   - drill/role-play curto quando útil;
   - evidência observável que indicará aplicação.
8. **1:1 / feedback** — comunicar fato, impacto, perspectiva da pessoa e acordo. Usar `golden-circle-feedback` quando precisar redigir a devolutiva.
9. **Recheck** — definir a próxima amostra/janela antes de concluir o ciclo. Comparar novamente sem mover a barra depois de ver o resultado.
10. **Update** — preservar histórico: o que foi observado, combinado, praticado e posteriormente confirmado/refutado.

## Peer exemplars
Comparar com pares somente quando:
- tarefas/motions forem comparáveis;
- o objetivo for extrair comportamento replicável, não ranquear pessoas;
- houver evidência observável do exemplar.

Extrair o movimento útil e adaptá-lo ao contexto da pessoa. Não exigir imitação de personalidade, estilo ou frase literal.

## Evidência
- tendência exige comparação temporal; uma call recente não prova evolução;
- resumo gerencial pode orientar busca, mas não substitui evidência do comportamento quando a fonte primária existe;
- amostra enviesada ou pequena deve produzir `limited readout`;
- não inferir personalidade, motivação ou intenção;
- resultado agregado e comportamento são sinais diferentes.

## Saída padrão
1. cobertura e limites;
2. o que melhorou;
3. o que regrediu ou segue como risco;
4. o que permaneceu estável/inconsistente;
5. prioridade de coaching;
6. prática `if/then` + drill;
7. sinal a observar na próxima amostra;
8. data/janela ou condição de recheck quando conhecida.

## Guardrails de gestão
- não usar coaching longitudinal como ranking oculto;
- feedback disciplinar, PIP, remuneração ou desligamento exigem processo e evidência próprios;
- preservar contexto da tarefa: maturidade é específica à tarefa, não rótulo global da pessoa;
- registrar fatos e acordos duráveis, não frustrações transitórias;
- desenvolvimento deve aumentar autonomia; monitoramento não deve virar vigilância.

## Integração
`call-evaluation`, `golden-circle-feedback`, `after-action-review`, `meeting-knowledge-capture`, `prioritization-engine`, `gestao-comercial-da-semana`.

## Origem metodológica
Síntese adaptada de `openai/role-specific-plugins · review-rep-call-trends` e `get-rep-call-feedback`, combinada com princípios de feedback/1:1 de `manager-dot-dev/manager-skills` e task-relevant maturity de `wondelai/skills · high-output-management`. Remove dependência de conectores específicos e evita score/ranking de pessoas.
