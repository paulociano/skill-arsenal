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

### Judgment points estreitos

Em workflows agentic complexos, não delegar todas as microdecisões ao mesmo modelo principal nem espalhar heurísticas vagas pelo fluxo. Identificar **decision points** estreitos e observáveis, por exemplo: admitir contexto, decidir se um resultado ainda é relevante, detectar drift, triagem de finding, verificar completion ou escolher se uma memória vale persistir.

Para cada decision point:
- formular uma pergunta bounded sobre um estado pequeno;
- preferir resposta tipada como yes/no, choice ou score quando suficiente;
- manter regras determinísticas como piso de segurança e usar julgamento semântico apenas onde regra fixa perde qualidade;
- permitir modo `shadow` quando um novo judge/classificador estiver sendo comparado antes de ganhar efeito;
- registrar decisão, confidence/probabilidade quando houver, estado relevante e consequência no ledger;
- não usar um judge para retirar approval humano exigido nem para contornar constraints explícitas;
- promover um decision point para automação ativa somente depois de comparar qualidade no workload real.

Esse padrão reduz contexto e custo apenas quando a decisão pode ser isolada sem perder informação essencial. Não quebrar decisões abertas ou criativas em microclassificações artificiais.

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

## Tarefas duráveis e efeitos externos

Para loops que retomam trabalho após interrupção ou recebem eventos repetidos:

- atribuir a cada entrada externa um ID estável fornecido na origem; deduplicar dentro do escopo declarado antes de iniciar trabalho;
- persistir histórico aceito, plano/etapa e estado da operação antes de despachar o efeito; registrar status da chamada e operações criadas de forma atômica quando o storage permitir;
- separar a tradução/validação da chamada de ferramenta, que deve ser limitada e sem I/O bloqueante, da execução assíncrona com timeout, receipt e correlation ID;
- usar leases ou mecanismo equivalente para recuperar workers interrompidos, impedindo que um executor antigo grave resultado depois de perder ownership;
- distinguir `pending`, `running`, `waiting-for-input`, `waiting-for-review`, `completed`, `failed` e `outcome-unknown` quando esses estados mudarem a recuperação;
- ligar aprovação ao alvo, parâmetros, versão e validade da ação; alterações de conta ou contexto invalidam a revisão pendente;
- quando um provedor puder ter concluído uma escrita cuja resposta se perdeu, consultar o estado/receipt do provedor antes de tentar de novo; não tratar retry como seguro por padrão;
- cancelamento impede etapas futuras, mas não promete desfazer uma requisição externa já despachada; expor essa condição no estado;
- manter schema/versionamento do estado persistido e falhar explicitamente em retomadas incompatíveis; testar entrega duplicada, crash entre persistência e despacho, lease expirado e resultado externo incerto.

Essas garantias dependem de storage e executor reais. Em uma conversa sem runtime persistente, usar apenas como contrato de projeto, sem alegar execução durável.


## Learning loop por experiência

Quando um agente ou workflow precisa melhorar com base em execuções anteriores:

- capturar apenas experiências diagnosticáveis: input relevante, decisão, resultado, falha e contexto suficiente para explicar o caso;
- avaliar antes de aprender: sucesso aparente sem critério independente não vira estratégia;
- refletir em uma hipótese operacional curta, não em narrativa extensa;
- atualizar uma base de estratégias versionada, com provenance e escopo;
- deduplicar estratégias semanticamente equivalentes antes de persistir;
- manter estratégias contraditórias separadas até existir evidência para resolver o conflito;
- limitar promoção automática a mudanças reversíveis e de baixo risco; mudanças de prompt, regra ou comportamento consequencial exigem comparação com baseline e approval apropriado;
- medir se a estratégia nova melhora casos futuros e não apenas o caso que a originou;
- remover ou rebaixar estratégias que causam regressão recorrente.

Pipeline de referência: Execute → Evaluate → Reflect → Update → Deduplicate → Re-evaluate.

Esse padrão descreve a metodologia. Em ambientes sem runtime persistente, traces, storage e executor real, não alegar aprendizado autônomo contínuo.

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

Contratos de operação durável, deduplicação e resultado incerto adaptados de https://github.com/CopilotKit/openmuse (README e docs/VERIFICATION.md) e https://github.com/unreallabsai/unreal-agent (README), sem importar seus runtimes.

Learning loop por experiência adaptado de https://github.com/kayba-ai/agentic-context-engine, preservando Execute → Evaluate → Reflect → Update → Deduplicate, sem depender do runtime, CLI ou serviço Kayba.

Decision points estreitos, modos active/shadow/off e ledger de julgamentos adaptados de [qybaihe/mu](https://github.com/qybaihe/mu), sem importar seu runtime, judges, desktop app ou mecanismos de aprovação.

Origem local: [loop-engineering.docx](../loop-engineering.docx).
