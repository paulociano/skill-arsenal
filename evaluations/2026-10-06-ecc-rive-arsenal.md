# Avaliação — ECC + Rive para o Skill Arsenal

**Data:** 2026-10-06  
**Fontes principais:** https://github.com/affaan-m/ECC · https://ecc.tools/ · https://rive.app/  
**Referência adicional fornecida:** https://x.com/MotionLonelines/status/2102984935141437951

## Decisão

**Classificação: A — adotar padrões seletivamente, sem importar o framework inteiro.**

ECC e Rive acrescentam valor real ao Arsenal, mas em camadas diferentes:

- **ECC**: disciplina operacional para agentes — planejamento, teste, implementação, revisão independente, verificação, memória, aprendizado e controle de contexto.
- **Rive**: camada de experiência interativa — state machines, Data Binding/View Models e, no fluxo atual, CLI + RML textual para criação e revisão por agentes.
- **Arsenal** permanece o router/governança: usa owners existentes e carrega a menor combinação necessária.

Não foi criada uma nova "Arsenal v2" paralela. Os padrões foram incorporados nos owners já existentes.

## Evidência observada no ECC

O repositório ECC organiza um ciclo explícito:

`plan → test → implement → review → verify → remember → improve`

Elementos com maior valor incremental para o Arsenal:

1. **Unified memory / handoff portátil**
   - scopes de projeto/equipe/usuário;
   - recall-before-write;
   - memória recuperada tratada como evidência, não como verdade;
   - handoff com fonte, estado observado, mudança, pendência e próximo passo.

2. **Continuous learning v2**
   - unidades pequenas de comportamento;
   - confidence/evidence como sinais;
   - isolamento project-scoped antes de promoção global.

3. **Independent review**
   - reviewer separado do writer;
   - reviewers especializados por domínio quando o risco justificar.

4. **Context budget**
   - não carregar dezenas de agentes, skills, rules e MCPs sem necessidade;
   - capability on demand.

5. **Silent failure thinking**
   - procurar fluxos em que a UI/ação aparenta sucesso mas estado, persistência, navegação ou side effects não convergem.

## O que não foi importado do ECC

- coleção inteira de agents/skills/commands;
- hooks automáticos;
- runtime de Memory Vault;
- promoção automática de learned instincts;
- configuração específica de Claude/Codex/Cursor;
- reviewers de stacks/linguagens sem uso corrente.

Motivo: o Arsenal já possui owners equivalentes e sua regra principal é parcimônia.

## Evidência observada no Rive

A direção atual do Rive amplia seu papel de asset animado para componente interativo:

- State Machines controlam lógica visual;
- Data Binding/View Models ligam dados e comportamento;
- runtimes suportam web/mobile e outros hosts;
- Rive CLI + RML permitem representar e editar cenas como texto, favorecendo diff/versionamento e trabalho com agentes;
- builds e state-machine traces podem fazer parte do ciclo de verificação.

Isso sugere um padrão novo para o Arsenal:

`plan → state contract → RML/design → build → preview/trace → runtime verify → commit`

## Regra de adoção para Rive

Use Rive quando:
- estado e transição visual são parte real da interação;
- o mesmo componente precisa responder a inputs/dados;
- Data Binding reduz duplicação de estado;
- uma state machine melhora clareza do comportamento.

Não use Rive como substituto padrão de:
- DOM semântico;
- navegação;
- formulários;
- listas/conteúdo textual;
- layout comum;
- animações simples resolvidas por CSS/WAAPI.

## Referência MotionLonelines

A URL do post foi fornecida como referência para esta avaliação. O conteúdo específico do post não foi tratado como evidência canônica porque não pôde ser recuperado de forma confiável pelo ambiente de avaliação. Nenhuma regra do Arsenal depende de uma interpretação não verificada dessa publicação.

## Mudanças aplicadas

- `agent-memory-engineering`: handoff portátil, scopes e recall como evidência.
- `session-learn`: reforço de units/instincts atômicos sem promoção automática.
- `software-engineering-cycle`: revisão independente, silent-failure hunt, Definition of Done proporcional, memory/learning e context budget.
- `motion-asset-engineering`: Rive Data Binding, state-machine test matrix e fluxo RML/CLI.
- `ui-motion-design`: interactive state machine como paradigma explícito.
- `creative-web-engineering`: Rive como interactive experience layer, mantendo DOM/React para semântica/layout.

## Resultado arquitetural

O Arsenal passa a operar com três papéis claros:

1. **Think / Govern** — router, planejamento, arquitetura e contexto.
2. **Build / Verify / Learn** — implementação, testes, revisão independente, runtime verification, memória e codificação de aprendizados.
3. **Experience** — motion e Rive quando interação visual justifica uma state machine.

A síntese adotada é: **resolver → verificar → aprender**, sem transformar toda tarefa em pipeline pesado.
