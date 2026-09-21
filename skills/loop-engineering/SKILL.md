---
name: loop-engineering
description: "Projetar trabalho recorrente ou iterativo com trigger, execução, verificação, estado persistido e limites de parada."
---

# loop-engineering

## Objetivo

Transformar trabalho repetível em um loop limitado e recuperável: **Trigger → Execute → Verify → State**, com orçamento finito, stop conditions e verificação independente.

## Quando usar

- automações recorrentes;
- monitoramento/polling;
- tarefas que repetem até atingir uma condição;
- ciclos de pesquisa/otimização orientados por métrica;
- manutenção recorrente com estado.

## Admission gate

Usar loop somente se:

- o trabalho for realmente repetível;
- outputs/estado forem inspecionáveis;
- existir um verificador;
- falhas forem recuperáveis;
- a autonomia justificar custo de coordenação.
Caso contrário, usar workflow one-shot.

## Contrato mínimo

Antes de executar, explicitar:

- objetivo e não-objetivos;
- trigger;
- owner;
- inputs;
- estado/artifacts;
- métrica ou critério de sucesso;
- verifier;
- limite de iterações/tempo/custo;
- stop condition;
- permission boundary;
- recuperação/rollback;
- write-back.

## Workflow

1. **Observe** — carregar estado e evidência fresca.
2. **Orient** — escolher uma hipótese/diagnóstico.
3. **Decide** — selecionar a menor ação capaz de mudar o resultado.
4. **Act** — executar uma ação limitada.
5. **Verify** — medir resultado e guardrails.
6. **State** — persistir diagnóstico, evidência, orçamento e próximo passo.
7. **Stop/continue** — parar por sucesso, limite, permissão, regressão ou falta de progresso.

## Estado canônico e action space limitada

Para loops em tempo real ou controle contínuo:

- transformar telemetry/raw state em um **estado canônico estruturado** antes de pedir decisão ao modelo;
- fazer aritmética exata, deadlines, colisões, limites e invariantes em código determinístico quando isso puder ser calculado;
- oferecer ao modelo apenas ações legais para o estado atual, preferencialmente como macros de duração/efeito conhecidos;
- registrar decisão, confidence/probabilidades quando existirem, estado canônico e outcome observado;
- evitar duplicar no prompt dados brutos que já foram convertidos em features úteis, mas manter raw/debug state fora do caminho crítico quando for necessário para auditoria;
- medir observation-to-action delay quando latência puder alterar a decisão;
- não permitir que o modelo invente uma ação fora do executor autorizado.

O modelo interpreta o estado; código continua dono de matemática exata e enforcement de limites.

## Mandato de autonomia para ações consequenciais

Quando um loop puder causar efeito financeiro, publicar, deletar, enviar, alterar produção ou agir em nome do usuário, um simples nível de autonomia pode ser insuficiente. Definir um **mandato explícito** antes da execução:

- recursos/alvos autorizados;
- tipos de ação permitidos;
- teto por ação e teto agregado por período, quando aplicável;
- condições de expiração;
- ambientes/contas permitidos;
- ações proibidas;
- mecanismo de halt/kill switch independente do modelo.

O executor deve **fail closed** quando não consegue provar que a ação cabe no mandato. Antes de agir, validar estado atual + mandato + target. Depois, escrever um ledger auditável com intent, parâmetros relevantes, decisão do guard, resultado e correlation id quando disponível.

Se a plataforma não oferece distinção estrutural confiável entre sandbox/paper e produção/live, limitar o agente ao nível mais seguro que pode ser comprovado. Nunca inferir que um ambiente é de teste apenas pelo nome.

## Correção focada

Para loops de correção:

- primeira rodada pode avaliar o grafo/escopo inteiro;
- rodadas seguintes devem atuar apenas nos nós/critério que falharam ou reabriram;
- partes PASS ficam congeladas e são re-verificadas, não regeneradas;
- falta de progresso por rodadas sucessivas é stop condition, não convite a continuar indefinidamente.

## Regras de execução

- Para execução futura ou recorrente, usar automation_update disponível no Codex; esta skill define a lógica do loop.
- Trigger não é evidência de sucesso.
- Toda recorrência tem orçamento finito.
- `NO_OP` só é válido quando uma consulta comprova que não havia trabalho elegível e não ocorreu efeito proibido.
- Ações externas relevantes precisam de permissões e approvals reais do ambiente.
- Verificar executores e dependências antes de configurar o loop; a existência do agendamento não prova execução.

## Níveis de autonomia

Para loops que aumentam autonomia, definir nível explícito proporcional ao risco:

- suggest;
- draft;
- act with approval;
- act within bounded pre-approval;
- self-repair/modify somente quando rollback, audit e autorização cobrirem a ação.

Capacidade deve carregar confidence, evidence freshness e max risk boundary. Autonomia não aumenta só porque um loop “funcionou uma vez”. Experimentos sobre o próprio workflow precisam de baseline, min samples/stop criteria e approval para promoção.

## Referências

Adaptada de Mark393295827/third-brain-v7-skills · loop-engineering (V8.1).

Estado canônico, macros legais e timing adaptados de [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario), sem depender de Jev, emulator ou ROM.

Mandato bounded-autonomy, fail-closed guard, kill switch e audit ledger adaptados de https://github.com/HKUDS/Vibe-Trading. A metodologia foi generalizada; nenhuma lógica de trading ou broker foi importada.

Origem local: [loop-engineering.docx](../loop-engineering.docx).
