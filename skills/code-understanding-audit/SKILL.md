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

## Grafo de evidência para codebases grandes

Quando o alvo cruza muitos arquivos, serviços, schemas ou documentos, pode ser útil construir mentalmente ou materializar um grafo de conceitos antes de explicar:

- nós representam símbolos, módulos, entidades, documentos ou conceitos relevantes;
- edges devem carregar relação semântica, não apenas proximidade;
- rotular cada edge como **EXTRACTED**, **INFERRED** ou **AMBIGUOUS**;
- manter locator de origem para relações extraídas;
- relações inferidas devem ter justificativa e nunca ser apresentadas como fatos;
- usar comunidades/subgrafos para reduzir o corpus antes de responder;
- path entre dois conceitos é evidência de conectividade, não prova automática de causalidade ou impacto;
- preservar um artefato persistente do mapa somente quando ele reduzir releitura futura de forma material.

Ferramentas de knowledge graph podem acelerar esse processo quando já existem no ambiente, mas não são requisito. Se forem usadas, validar pelo menos uma amostra de nós/edges contra o código-fonte antes de confiar em queries derivadas.

## Impact analysis e memória arquitetural

Quando a pergunta for "o que esta mudança afeta?" ou "por que isso existe?":

- partir do diff/símbolos alterados e expandir por callers, imports, contracts, routes, data flows e dependências cross-service;
- distinguir **direct impact** de **transitive candidate impact**;
- marcar risco maior quando a mudança cruza boundary de serviço, schema, API pública, fila/evento ou persistência;
- verificar uma amostra dos paths de impacto no código antes de reportá-los;
- ADRs, RFCs, comentários WHY e histórico de commits podem explicar intenção, mas não substituem estado runtime atual;
- quando decisões arquiteturais precisarem sobreviver sessões, manter registro canônico separado do grafo/índice derivado;
- índice/grafo é cache reconstruível; decisão/ADR é conhecimento autoral e precisa de provenance.

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

Proveniência de edges e consultas por subgrafo adaptadas de https://github.com/Graphify-Labs/graphify, sem exigir Graphify, hooks, pacote Python ou backend semântico.

Impact mapping, cross-service linking e separação entre índice reconstruível e ADR persistente adaptados de https://github.com/DeusData/codebase-memory-mcp, sem executar binários, installers, daemon ou hooks da fonte.

Origem local: [code-understanding-audit.docx](../code-understanding-audit.docx).
