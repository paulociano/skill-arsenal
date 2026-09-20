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
