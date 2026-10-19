---
name: legacy-system-reconstruction
description: "Reconstruir documentação, regras e arquitetura de sistemas legados em descoberta somente leitura antes de planejar modernização."
---

# legacy-system-reconstruction

## Objetivo

Reconstruir conhecimento operacional de um sistema legado a partir do código e artefatos existentes, produzindo specs rastreáveis, arquitetura, regras de negócio, gaps e um mapa de modernização sem alterar o sistema de origem durante a fase de descoberta.

## Quando usar

- sistema legado sem documentação confiável;
- migração/rewrite;
- aquisição ou takeover de codebase;
- necessidade de descobrir regras de negócio implícitas;
- criação de specs antes de modernização;
- comparação entre comportamento legado e implementação nova.

## Princípio central

**Descoberta é read-only. Primeiro reconstruir o que o sistema é; depois decidir o que deve mudar.**

## Workflow

1. **Reconnaissance**
   - linguagens, frameworks, módulos, entry points, dependências, integrações, bancos e surfaces.
2. **Excavation**
   - algoritmos, control flow, data structures, state transitions e contratos.
3. **Business interpretation**
   - regras implícitas, permissões, invariantes, workflows, exceptions e terminology.
4. **Architecture synthesis**
   - containers/components, integration map, data model, state machines e technical debt.
5. **Spec generation**
   - specs por módulo/use case/feature com source anchors.
6. **Gap review**
   - contradições, comportamento não explicado e decisões que exigem humano.
7. **Human validation**
   - confirmar pontos inferidos e lacunas materiais.
8. **Modernization planning**, somente após discovery:
   - migrate / discard / preserve / human decision;
   - target architecture;
   - data migration;
   - behavioral parity plan;
   - staged strategy quando aplicável.

## Escala de confiança

Para cada finding/spec relevante:

- **CONFIRMADO** — diretamente sustentado por código, schema, teste, runtime ou documento autoritativo.
- **INFERIDO** — melhor explicação a partir de padrões/evidência indireta.
- **LACUNA** — não há evidência suficiente; precisa de validação.

Confidence nunca substitui locator/provenance.

## Artefatos úteis

Gerar somente os necessários:

- inventory;
- dependencies;
- module/code analysis;
- domain glossary;
- business rules;
- state machines;
- permission matrix;
- architecture/C4;
- ERD/data dictionary;
- integration map;
- gaps/questions;
- specs executáveis;
- source→spec traceability;
- regression watch / parity checklist para modernização.

## Organização de specs

Escolher a unidade que minimiza confusão:

- módulo;
- caso de uso;
- endpoint;
- feature;
- híbrida.

Não impor uma taxonomia única se a arquitetura real pedir outra.

## Regra de não-mutação

Durante reconstruction:

- não refatorar;
- não corrigir;
- não “limpar” código;
- não sobrescrever docs legadas;
- outputs ficam separados da origem quando possível.

Mudanças no sistema só começam numa fase posterior, com escopo e approval próprios.

## Modernização

Quando o objetivo for migração:

1. separar equivalência comportamental de melhoria;
2. identificar contratos que precisam permanecer;
3. classificar cada regra/feature: PRESERVE / MIGRATE / DISCARD / HUMAN DECISION;
4. escolher estratégia proporcional: strangler, parallel run, branch-by-abstraction, big-bang somente quando justificado;
5. definir oracle/parity tests antes da troca;
6. registrar regressions to watch.

## Re-extração / convergência

Após mudanças no sistema:

- não reexecutar o pipeline inteiro automaticamente;
- preferir sync/addendum para mudanças localizadas;
- re-extração completa só quando drift estrutural justificar;
- manter histórico de quais specs foram superseded.

## Regras

- source code não é automaticamente business truth; pode conter bug/legado acidental;
- docs antigas não vencem runtime/code atual sem evidência de autoridade;
- inferência nunca vira confirmação por repetição;
- spec gerada precisa apontar para fonte;
- screens/screenshot podem documentar UI, mas não provam regra interna;
- modernização não autoriza “melhorar” comportamento sem decisão explícita;
- estimativa/pricing é fase separada de reconstruction.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Usar o repositório e artefatos acessíveis em modo de leitura durante a descoberta. Não exigir comandos /reversa ou instaladores. Executar fases sequencialmente; delegação é opcional quando autorizada.

## Integração

- `code-understanding-audit`
- `architecture-visualization`
- `to-spec`
- `project-skill-architecture`
- `handoff`
- `verify-before-claim`

## Referências

Adaptada metodologicamente de sandeco/reversa.

Origem local: [legacy-system-reconstruction.docx](../legacy-system-reconstruction.docx).

## Contratos de evolução e rastreabilidade bidirecional (Reversa, revisão 2026-10-19)

Aplicar somente quando a tarefa passar da documentação legada à evolução verificável:

1. Registrar, por funcionalidade, a cadeia **evidência original → regra/invariante → requisito e spec → plano de implementação → código → teste → bug/regressão**. O sentido inverso importa: uma implementação deve apontar para a decisão/spec que a autorizou, e cada spec deve apontar para evidência, não só para prosa gerada.
2. Fazer um diagnóstico/briefing curto antes da orquestração; escolher módulos prioritários e uma unidade estável de feature. Gerar IDs de specs, registrar revisão do repositório, responsáveis e lacunas. Evitar equipes fictícias de agentes quando uma análise sequencial do ChatGPT resolve o caso.
3. Na **descoberta**, manter código original intocado; armazenar inventário, findings e specs em área separada, sob versionamento e sem credenciais. Registrar checkpoints/handoff para retomada, mas não alegar processos autônomos ou estado persistente quando não existem.
4. Antes de implementar, produzir **requirements → actions → acceptance tests** vinculados à spec. Distinguir aprovação de requisitos, autorização de escrita e verificação final. Só editar código em fase posterior expressamente solicitada.
5. **Caracterização/paridade:** capturar entradas, saídas, efeitos e erros do comportamento anterior quando observáveis. Estabelecer oráculo e testes de regressão antes de modernizar ou refatorar. Se não houver oráculo, classificar equivalência como não demonstrada.
6. Depois da implementação, acrescentar um **addendum/sync** com comportamento realmente entregue, bugs conhecidos e testes observados; não reescrever silenciosamente a especificação de origem nem declarar que uma inferência antiga foi confirmada.
7. Para migração, fazer triagem regra a regra (PRESERVE/MIGRATE/DISCARD/HUMAN DECISION), escolher estratégia de corte explícita e conectar testes de paridade ao plano. Em defeitos, manter triagem/diagnóstico separados de correção e rastrear BUG ↔ SPEC ↔ CODE ↔ TEST.
8. Separar modos: descoberta read-only, evolução com escrita controlada, migração e documentação derivada. A promessa de imutabilidade se limita à fase de descoberta; ferramentas/instaladores externos não substituem permissões e backups verificáveis.

**Fonte e portabilidade:** https://github.com/sandeco/reversa (README consultado em 2026-10-19). Origem de padrões de pipeline reverso, sync por addendum, trilha causal de bugs, gates de caracterização e distinção entre discovery e forward. O projeto externo usa Node.js 18+, `npx reversa install`, múltiplos agentes e comandos `/reversa*`; nada disso é pré-requisito nem deve ser anunciado como instalado ou executado no ChatGPT. O modo externo `/reversa-forward-autonomous` modifica código deliberadamente e exige cautela específica. A metodologia já integrava esta skill; este bloco incorpora os detalhes incrementais relevantes da versão inspecionada.
