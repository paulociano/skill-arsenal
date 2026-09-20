---
name: code-understanding-audit
description: "Explicar código ou auditar decisões arquiteturais com evidências, ajustando profundidade ao conhecimento do leitor."
---

# code-understanding-audit

## Objetivo

Explicar código para aprendizagem ou auditar decisões arquiteturais de acordo com o nível do leitor, focando em what, why, when, alternatives e prerequisites em vez de apenas resumir linhas.

## Quando usar

Explicar código ou auditar decisões arquiteturais com evidências, ajustando profundidade ao conhecimento do leitor.

## Modos

- **Learn** — entender código e conceitos.
- **Audit** — examinar decisões, trade-offs, edge cases e testabilidade.
- **Compact** — visão curta e componentes/conceitos centrais.
- **Full** — walkthrough, prerequisites e recursos quando realmente pedidos.

## Níveis

### Junior
Definir termos, usar exemplos/analogias e explicar linguagem/framework.

### Mid
Pular fundamentos comuns e focar em decisões, responsabilidades e trade-offs.

### Senior
Focar em choices não óbvias, constraints, coupling, failure modes, testability e alternativas.

## Workflow

1. Identificar arquivos/módulo/commit alvo.
2. Se o usuário não apontou alvo, usar contexto já conhecido; só pedir escopo quando realmente impossível localizar.
3. Mapear responsabilidades, fluxo de dados, interfaces e dependências.
4. Para cada conceito importante:
   - **What**;
   - **Why here**;
   - **When useful**;
   - **Alternatives**;
   - **Trade-offs**;
   - **Prerequisites**.
5. Distinguir:
   - fato visível no código;
   - intenção documentada;
   - inferência do reviewer.
6. No modo audit, conectar findings a evidência concreta.
7. Buscar documentação externa só quando o modo/tarefa pedir atualização ou aprofundamento.
8. Encerrar com mapa mental do sistema ou decisões centrais, sem recap redundante.

## Profundidade e crítica

Antes de explorar, classificar a pergunta como **simples** ou **complexa**:

- simples: um módulo/função/fluxo estreito → uma exploração end-to-end;
- complexa: subsistema cross-file/cross-service → decompor em 2–4 ângulos não redundantes e sintetizar depois.

Formato de explicação preferido quando útil:

- Overview;
- Key Concepts;
- How It Works;
- Where Things Live;
- Gotchas.

Para modo **Critique**:

1. explicar primeiro;
2. só depois criticar;
3. usar revisores independentes apenas quando a arquitetura justificar;
4. reconciliar findings como lead pragmático:
   - **Act on**;
   - **Consider**;
   - **Noted**;
   - **Dismissed**.

Diversidade de modelos pode ampliar cobertura, mas não é requisito nem prova de independência. Se não houver subagentes/modelos adicionais, fazer uma segunda passagem deliberadamente adversarial sobre a explicação já fundamentada.

## Known concepts

Quando o usuário já domina determinado conceito, mencioná-lo brevemente e investir contexto no que é novo. Não presumir nível com base apenas em cargo/título.

## Regras

- “por que” inferido precisa ser rotulado como inferência se não há ADR/comentário/issue;
- evitar walkthrough linha por linha quando estrutura explica melhor;
- não elogiar pattern só porque ele é conhecido;
- mostrar alternativa só quando ela realmente ajuda a entender a escolha;
- resources devem ser oficiais/fortes e atuais quando externos;
- audit não vira refactor automático sem pedido.

## Integração

- `teach`
- `library-version-grounding`
- `code-review`
- `architecture-visualization`
- `diagnosing-bugs`

## Referências

Adaptada de mohi-devhub/antivibe.

Origem local: [code-understanding-audit.docx](../code-understanding-audit.docx).
