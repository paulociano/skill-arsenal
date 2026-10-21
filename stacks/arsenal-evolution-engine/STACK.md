---
name: arsenal-evolution-engine
description: "Reavaliar periodicamente skills, avaliações e repositórios já analisados à luz de novas capacidades, contexto e resultados; descobrir combinações úteis, testar hipóteses e evoluir o Arsenal com evidência, segurança e controle de regressão."
---

# Arsenal Evolution Engine

## Objetivo
O Arsenal não é um arquivo morto de decisões. Esta stack reabre decisões antigas **quando uma mudança verificável de contexto ou de capacidade altera a relação valor/risco**, inclusive decisões de KEEP_EXTERNAL_REFERENCE, ABSORB_METHOD_ONLY e REJECT. Descobre sinergias entre owners sem presumir que a origem externa está instalada. Não substitui o `arsenal-autopilot`: este último avalia e incorpora fontes, enquanto este mecanismo **seleciona quando e por que reavaliar fontes já conhecidas**.

## Triggers
- `arsenal: auto otimizar`, `arsenal: evolução`, `arsenal: reavaliar o histórico`;
- novos conectores, ferramentas, ambientes, skills e stacks que desbloqueiam dependências antigas;
- regressões, gaps de execução, feedback do usuário e custos observados;
- release/versionamento de fonte previamente avaliada, nova necessidade ou owner alterado;
- revisão agendada executada **somente** por um scheduler/automação real que leia esta stack.

Não executar uma varredura profunda de todas as avaliações a cada mensagem. Não declarar que existe execução contínua/background sem uma automação realmente criada e confirmada.

## Autoridade e dependências
1. Ler `ARSENAL INDEX.md` atual do GitHub canônico.
2. Ler esta stack e `references/REASSESSMENT-CONTRACT.md`.
3. Para candidatas selecionadas, consultar o registro original em `evaluations/`, owner atual e **fonte original atual**; usar GitHub como autoridade do Arsenal.
4. Rotear adoção para `arsenal-autopilot` / `evaluate-and-import-skill`; aplicar `skill-security-review`, `agent-action-governance`, `verify-before-claim` conforme risco.
5. Usar `agent-memory-engineering` apenas para memória/proveniência e `llm-observability-evaluation` se houver experimento quantitativo. Estes são owners opcionais, não obrigatórios.

## Fluxo operacional

### 1. Indexar o passivo sem reprocessá-lo por inteiro
- Enumerar avaliações do GitHub em `evaluations/`, paginando quando necessário, e extrair **somente** registros/trechos necessários.
- Construir/atualizar `stacks/arsenal-evolution-engine/references/REASSESSMENT-REGISTER.md` como **fila de decisões revisitáveis**, não duplicação literal de 209 arquivos.
- Cada candidato tem referência canônica ao arquivo de avaliação, fonte externa, decisão anterior, owner, hipótese de desbloqueio, estado e próxima condição de revisão.
- Não usar nome de arquivo como inferência de capacidade, classe, estado ou motivo; ler o conteúdo antes de classificar.
- Registro é índice derivado e reconstruível; `evaluations/`, `skills/`, `stacks/` e índice permanecem fontes de verdade.

### 2. Detectar eventos que mudam a decisão
Tratar como sinais, nunca como prova:
- **TOOL_UNLOCK:** integração/connector ou runtime foi realmente conectado e testado;
- **SOURCE_CHANGED:** houve alteração de versão, licença, workflow, API ou dependência na fonte externa;
- **OWNER_CHANGED:** owner/stack local ganhou ou perdeu capacidade;
- **NEED_CHANGED:** novos objetivos do usuário, demandas recorrentes, lacunas vistas nas tarefas;
- **EVIDENCE_CHANGED:** teste/benchmark, falha, custo, manutenção, segurança, qualidade;
- **COMPOSITION_UNLOCK:** duas ou mais capacidades antes isoladas formam fluxo recorrente verificável;
- **RISK_CHANGED:** vulnerabilidade, permissão, dependência ou requisito regulatório materialmente novo.

Detectar deltas pelo estado recuperável da fonte; timestamps, stars e hype não justificam promoção.

### 3. Gerar e priorizar hipóteses
Para cada evento: `antes → mudança verificável → nova capacidade plausível → owner afetado → caso de uso → métrica de sucesso`.
Priorizar impacto observável, frequência/reuso, dependência efetivamente desbloqueada, confiança, esforço e risco, com rationale explícito. Não reduzir a uma nota pseudo-objetiva nem permitir que quantidade de fontes vire incentivo de importação.
Selecionar um lote pequeno, com teto padrão de **3 candidatos aprofundados por ciclo**; os demais ficam pendentes. Encontrar sinergias por **contratos de entrada/saída**, não por semelhança de nomes.

### 4. Reavaliar com falsificação
- Consultar avaliação anterior, ler versão canônica do owner e apenas os arquivos da fonte necessários.
- Formular hipótese do ganho incremental e alternativa de não fazer nada.
- Criar casos `should-trigger`, `near-miss`, `failure-path` e, para composição, `integration` com outputs e oracles observáveis.
- Comparar baseline x candidata sob tarefas equivalentes, custo, tempo, precisão/segurança e clareza de roteamento quando os dados existirem.
- Sem sandbox/teste disponível, registrar **design validado documentalmente**, nunca alegar benchmark runtime.
- Decisão: `RETAIN`, `RECLASSIFY`, `UPDATE_EXISTING`, `CREATE_NEW`, `COMPOSE_STACK`, `ARCHIVE_REFERENCE` ou `REJECT`.
- `REJECT` por ameaça atual não pode ser reaberto só por conveniência; exige evidência que tenha removido o risco.

### 5. Materializar apenas ganho provado
- Preferir enriquecer owner existente; criar stack somente se houver fluxo composto recorrente; atualizar índice se houver owner/roteamento novo.
- Passar por security review e limites reais das tools: metodologia disponível não implica runtime disponível.
- Preservar decisões anteriores no arquivo original; escrever nova avaliação de reanálise que aponta para a anterior em vez de reescrever a história.
- Gravar commit(s) no GitHub canônico dentro da autorização do Arsenal, reler cada arquivo e comparar should-trigger / near-miss.
- Em mudança de comportamento de alto impacto, fazer piloto reversível antes de promoção; definir rollback.
- Não criar loops de autoedição ou autoaprovação: a proposta e a verificação podem ser automáticas quando tools permitirem, mas nenhum agente amplia suas próprias permissões, autoriza efeitos externos ou ignora gates.

### 6. Aprender sem deriva
Registrar por rodada: timestamp, trigger, fontes inspecionadas, candidatos adiados, decisão anterior/nova, evidência, owner, artifacts/commits, riscos, casos de aceitação, próxima reabertura e validade temporal.
Medir `novas capacidades efetivamente usadas`, `reutilização`, `regressões`, `tempo de execução`, `custo de leitura/revisão` e `reversões`; não otimizar por quantidade de skills.
Se não houver delta convincente, publicar **no-change audit** resumida quando solicitada; não editar owners artificialmente.
Evitar reabrir o mesmo candidato sem mudança material, usando condição e data de último exame como cooldown, não prazo de descarte definitivo.

## Modos
- **`scan`**: leitura leve de avaliação/registro + sinais recentes; devolve shortlist sem writes.
- **`reassess`**: aprofunda até 3 candidatas, aplica teste de hipótese, registra veredito.
- **`evolve`**: inclui implementação e verificação via Autopilot quando justificado.
- **`retro`**: analisa incidentes/reversões e atualiza critérios/guardrails sem autojustificar mudanças.

Quando o pedido disser `arsenal: auto otimizar`, usar `evolve` por padrão, mas respeitar o custo real e o limite por ciclo.

## Critérios de sucesso
- nenhuma decisão anterior é tratada como eterna;
- nenhuma origem rejeitada é instalada sem nova evidência;
- uma reabertura tem evento material e proveniência;
- ganho é demonstrável e com owner claro;
- melhorias não degradam roteamento de casos próximos;
- arquivos publicados são relidos e os limites do ambiente são explícitos.

## Limites
Este arquivo define o procedimento, não cria um daemon autônomo, watcher de GitHub, acesso permanente a máquina, timers invisíveis ou agente que roda sozinho. Agendamento exige ferramenta de automação explícita e ações executadas em cada disparo. Não prometer leitura de dados privados ou execução de testes inexistentes.
