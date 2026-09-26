---
name: arsenal-autopilot
description: Evoluir o Skill Arsenal a partir de uma ou mais fontes externas, detectando capacidades, overlap e ownership, avaliando segurança e portabilidade, adotando apenas valor incremental e publicando mudanças verificadas com trilha de auditoria.
---

# Arsenal Autopilot

## Objetivo
Transformar avaliação de skills externas em um pipeline repetível de evolução do Arsenal, sem importar catálogos em massa, duplicar owners ou confundir infraestrutura de terceiros com capacidades realmente disponíveis.

## Trigger
Use quando o usuário:
- enviar um ou vários repositórios/skills para avaliação;
- pedir para incorporar, absorver ou comparar coleções de skills;
- pedir "faça o mesmo com essas";
- pedir evolução automática do próprio Arsenal;
- usar `arsenal autopilot` ou equivalente.

Para uma única skill simples, `evaluate-and-import-skill` continua sendo suficiente. O Autopilot é preferível para lotes, ecossistemas grandes ou manutenção recorrente do Arsenal.

## Fontes canônicas
1. GitHub do Skill Arsenal.
2. `ARSENAL INDEX.md` como router inicial.
3. Arquivos específicos apontados pelo índice.
4. Fonte externa original em sua branch/default ref atual.

Não usar cópias antigas em Drive/Notion como autoridade.

## Pipeline

### 0. Ground
Leia:
- `ARSENAL INDEX.md`;
- esta stack;
- somente as skills/stacks canônicas necessárias para comparação.

Não carregue todo o Arsenal.

### 1. Discover
Para cada fonte externa:
1. confirme repositório, branch e estrutura;
2. leia README/root;
3. localize SKILL.md, manifests ou documentos centrais;
4. abra somente os candidatos que parecem materialmente novos.

Não execute installers, setup, scripts ou binários da fonte para descobrir valor.

### 2. Extract capabilities
Crie mentalmente ou materialmente um capability ledger usando `references/CAPABILITY-LEDGER.md`.

A unidade de comparação é **capability**, não nome de skill.

Separe:
- metodologia;
- runtime/tooling;
- dados/credenciais;
- assets;
- branding;
- convenções do agente de origem.

### 3. Resolve ownership
Para cada capability:
1. encontre owner existente pelo índice;
2. compare contrato, trigger, workflow e guardrails;
3. decida uma ação:
   - `KEEP_EXTERNAL_REFERENCE`;
   - `UPDATE_EXISTING`;
   - `CREATE_NEW`;
   - `ABSORB_METHOD_ONLY`;
   - `REJECT`.

Prefira `UPDATE_EXISTING` quando um owner canônico já cobre o mesmo trabalho.

### 4. Classify
Classifique a fonte:
- **A** — skill realmente útil: muda comportamento de forma clara;
- **B** — boa metodologia: vale absorver, mas pode não justificar skill própria;
- **C** — prompt sofisticado: pouco ganho incremental;
- **D** — skill/sistema técnico: depende de runtime, scripts, apps, integrações ou infraestrutura externa.

Classes podem ser combinadas, como A/D, quando a metodologia é forte mas a implementação não é portátil.

### 5. Security and portability gate
Aplique `skill-security-review` proporcionalmente ao risco.

Verifique:
- installers e supply chain;
- shell/subprocess;
- rede;
- credenciais;
- persistência/hooks;
- auto-modificação;
- ações externas;
- permissões;
- prompt injection;
- dependências sem equivalente.

Nunca trate ferramenta da fonte como disponível apenas porque aparece no README.

### 6. Adapt
Quando houver valor:
1. preserve objetivo, invariantes, failure modes e acceptance checks;
2. substitua mecanismos Claude/Codex/outro agente por capacidades reais;
3. remova dependências sem equivalente;
4. mantenha approval gates;
5. reduza permissões;
6. escreva trigger estreito e description roteável;
7. use progressive disclosure quando a skill crescer;
8. mantenha provenance da origem adaptada.

### 7. Prove incremental value
Antes de criar uma nova skill, responda:
- Qual comportamento novo ela produz?
- Por que uma skill existente não resolve isso?
- Qual cenário should-trigger demonstra o ganho?
- Qual near-miss não deve ativá-la?
- Qual evidência provaria que ela funciona?

Quando o ganho não for demonstrável, não crie a skill.

### 8. Materialize
Quando autorizado pelo escopo permanente do Arsenal:
- crie ou atualize `skills/<nome>/SKILL.md`;
- crie referências apenas quando reduzirem contexto ou duplicação;
- atualize `ARSENAL INDEX.md`;
- registre a avaliação em `evaluations/`;
- crie/atualize stack somente quando houver fluxo recorrente real.

Preserve mudanças concorrentes e nunca use force-push.

### 9. Verify
Depois da última escrita:
1. releia cada arquivo publicado da branch canônica;
2. confirme frontmatter, nomes e rotas;
3. confirme que o índice aponta para a capacidade;
4. confirme que a avaliação registra adotados e descartados;
5. verifique que nenhum runtime inexistente foi prometido;
6. use `verify-before-claim` para limitar a conclusão ao que foi realmente publicado.

### 10. Learn
Use `golden-path-capture` apenas quando a execução revelar um processo novo e comprovado.

Não transforme cada lote em novas regras. Atualize o Autopilot somente quando a evidência mostrar que o pipeline atual perdeu um caso importante ou gerou erro recorrente.

## Política de lote
Para muitos repositórios:
- faça triagem ampla por README/root;
- aprofunde somente candidatos com novidade plausível;
- agrupe avaliações relacionadas em um único registro quando isso melhorar rastreabilidade;
- não crie uma skill por repositório;
- uma única fonte pode originar zero, uma ou várias capabilities;
- várias fontes podem justificar uma única skill consolidada.

## Critério de parada
O lote termina quando:
- todas as fontes têm classificação e decisão;
- todas as capabilities adotadas têm owner;
- segurança/portabilidade foram avaliadas;
- mudanças justificadas foram publicadas;
- índice e avaliação estão sincronizados;
- leitura pós-escrita confirma o estado canônico.

## Saída ao usuário
Informe de forma compacta:
- o que entrou;
- o que atualizou;
- o que ficou apenas como referência;
- principais razões;
- commits/publicação verificados;
- limitações reais.

## Integração
Esta stack governa e compõe, conforme necessário:
- `evaluate-and-import-skill`;
- `skill-security-review`;
- `skill-builder`;
- `source-to-skill`;
- `project-skill-architecture`;
- `functional-skill-architecture`;
- `golden-path-capture`;
- `verify-before-claim`.

Esses recursos são candidatos, não etapas obrigatórias em toda execução.


## Referências internas
- `references/CAPABILITY-LEDGER.md` — schema de comparação, ownership e prova.
- `references/ACCEPTANCE-CASES.md` — should-trigger, near-miss e critérios de conclusão para regressão do Autopilot.
