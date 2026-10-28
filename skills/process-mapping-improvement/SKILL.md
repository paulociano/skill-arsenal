---
name: process-mapping-improvement
description: "Mapear e melhorar processos operacionais com baseline antes de mudar: SIPOC, mapa de fluxo de valor, desperdícios Lean, causa raiz, capacidade e gargalos, SOP e riscos de dependência de uma só pessoa, sem declarar ganho que não foi medido."
---

# Process Mapping & Improvement

## Objetivo

Entender como o trabalho realmente flui, medir onde espera ou retrabalha e melhorar o que importa, com padronização e medição antes e depois.

Origem metodológica: agente `operations-manager` de msitarzewski/agency-agents (MIT), adaptado. Foram removidos persona, memória fictícia e o arsenal estatístico pesado (Cp/Cpk, Gage R&R, DPMO) que não se justifica para processos de pequeno volume.

## Quando usar

- mapear um fluxo recorrente (atendimento, rotina de acompanhamento, relatório semanal);
- achar o gargalo, o retrabalho ou a espera;
- documentar um processo em SOP;
- estimar capacidade (quanto o time absorve) e identificar dependência de uma pessoa;
- planejar uma melhoria com prova de efeito.

Não usar para:
- gestão do fluxo de itens, WIP e prazos no dia a dia: `work-delivery-flow`;
- causa raiz de um problema pontual: `root-cause-analysis`;
- retrospectiva de evento concluído: `after-action-review`;
- saúde e coordenação de equipe: `team-health-management`.

## Regras de fundo

- **Meça antes de mudar e depois de mudar.** Sem linha de base, não há melhoria comprovada, só impressão.
- **Padronize antes de otimizar.** Processo instável e sem dono não escala.
- **Ache a causa raiz antes de propor solução.** Acrescentar gente, passos ou conferências para esconder defeito é sintoma, não solução.
- **Otimize o sistema, não o silo.** Melhorar a métrica local de uma área às custas do fluxo ponta a ponta é ganho falso.
- **Sem ponto único de falha.** Processo crítico que só uma pessoa, um fornecedor ou um sistema não documentado sabe fazer é risco a registrar e mitigar.

## Workflow

1. **Delimitar** com SIPOC: fornecedores, entradas, 5 a 7 etapas macro, saídas e clientes (internos e externos). Definir o gatilho e o que é "pronto".
2. **Mapear o estado atual, andando o processo real** (não o desenhado): etapas, quem faz, tempo de execução, tempo total decorrido, filas de espera entre etapas, retrabalho e pontos de decisão.
3. **Medir:** tempo de ciclo, tempo total (lead time), parcela de tempo que agrega valor ao cliente, taxa de retrabalho ou erro, volume. Declarar a fonte de cada número e a amostra.
4. **Identificar desperdícios** (esperas, retrabalho, excesso de processamento, deslocamento de informação, estoque de pendências, produção além da necessidade, talento subaproveitado).
5. **Causa raiz** dos principais (cinco porquês, diagrama de causa e efeito, Pareto quando houver contagem). Distinguir problema de capacidade, de transferência entre etapas e de variação.
6. **Desenhar o estado futuro:** eliminar etapas sem valor, nivelar o fluxo, reduzir lotes, criar sinais de puxada, prevenir erro na origem. Priorizar por efeito e esforço, uma mudança por vez quando possível para saber o que funcionou.
7. **Capacidade:** demanda esperada, tempo disponível por etapa, utilização realista, gargalo (a etapa que limita o fluxo total). Mostrar o ponto em que o processo deixa de escalar.
8. **SOP e continuidade:** documentar o procedimento, dono, versão, treinamento e substituto; listar dependências críticas e plano de contingência.
9. **Verificar:** repetir as medições depois da mudança e reportar o efeito com o mesmo método.

## Saída padrão

SIPOC, mapa atual com tempos, tabela de desperdícios e causas, proposta futura com impacto esperado e como será medido, riscos de dependência, SOP em rascunho e plano de verificação.

## Limites

- Não afirmar ganho percentual sem medição antes e depois.
- Não tratar o mapa desenhado pela gestão como o processo real sem observar.
- Mudanças que removem controles ou fallbacks exigem decisão humana explícita.
- Metodologias formais (Six Sigma completo) só quando volume e dados justificarem.
