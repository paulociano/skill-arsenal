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

## Busca estrutural e empacotamento de contexto

Para codebases grandes, subir a potência da busca apenas quando necessário:

1. **text search** para nomes, strings, paths e indícios rápidos;
2. **symbol/AST search** para padrões sintáticos e relações estruturais;
3. **semantic/static analysis** para regras, dataflow ou findings que texto/AST local não resolvem;
4. **manual source verification** antes de transformar hit de ferramenta em conclusão arquitetural.

Ferramentas como ast-grep e Semgrep são linhas de evidência, não oracles. Regra que casa código não prova bug nem impacto sem confirmar contexto.

Ao empacotar um repositório para análise por LLM:

- aplicar include/exclude explícito;
- respeitar secrets, binaries, generated files e licensing boundaries;
- medir token budget por arquivo/área;
- preferir mapa/índice + leitura progressiva a despejar o repo inteiro;
- manter ponteiros para arquivos originais para que conclusões possam ser reabertas e verificadas.

Repomix pode acelerar empacotamento quando disponível, mas o princípio canônico é reduzir contexto sem perder provenance.

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

## Investigação de artefatos distribuídos sem fonte (REA)

Quando a pergunta depender de um executável, APK, pacote Electron/ASAR, assembly .NET, firmware ou comportamento que o source disponível não comprova:

1. Identificar o artefato exato, versão/hash, plataforma, escopo e autorização. Não escolher aplicativos locais arbitrários.
2. Roteá-lo ao método mais restrito e observável: inventário estático primeiro; runtime somente se realmente necessário e autorizado.
3. Quando REA MCP ou CLI estiver de fato conectado, usar ferramentas anunciadas por esse runtime, não nomes presumidos de uma skill. Para fontes normais e completas, permanecer na análise convencional de repositório.
4. Começar por overview resumido; descer a módulos, símbolos, imports, IPC, traces ou chamadas ligados à pergunta, reutilizando sessões e evidence IDs quando disponíveis.
5. Construir um ledger de achados com **observação**, **derivação**, **inferência** e **desconhecido**, fonte/localizador, alvo/versão, cobertura e grau de confiança. Não transformar strings, pseudocódigo ou análise estática em prova de execução.
6. Se o usuário pedir reconstrução, usar interfaces e testes próprios; comparar comportamento externamente por `behavior-contract-validation`. Distinguir equivalência demonstrada de semelhança visual ou hipótese.
7. Se REA ou um provedor necessário não estiver disponível, declarar bloqueio e continuar com as ferramentas realmente existentes. Não simular decompilação ou resultados MCP.

**Limites e segurança:** análise somente de targets autorizados; não instalar REA, abrir portas de depuração, executar aplicações, alterar configurações ou expor capturas/segredos como efeito implícito. O projeto externo exige infraestrutura própria, potencialmente Node/npm e Hopper/Ghidra/IDA, JADX ou navegador. Qualquer setup exige revisão de supply chain, permissões e aprovação aplicável. Fonte: https://github.com/morluto/rea e https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/SKILL.md; avaliação: `evaluations/2026-10-11-morluto-rea.md`.

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

Busca estrutural e empacotamento de contexto refinados a partir de https://github.com/ast-grep/ast-grep, https://github.com/semgrep/semgrep e https://github.com/yamadashy/repomix, sem exigir esses CLIs.

Origem local: [code-understanding-audit.docx](../code-understanding-audit.docx).

## Reconhecimento estático eficiente de binários e pacotes (leanrea)

Para artefatos distribuídos sem fonte e com análise autorizada:

1. Trabalhar numa cópia, identificando versão, hash, plataforma e tipo por assinatura/magic bytes, não apenas pela extensão.
2. Fazer um inventário de menor custo primeiro: metadados, dependências, símbolos, imports/exports e strings. Agrupar probes independentes, limitar saída e registrar origem; não despejar bundles minificados ou disassembly inteiro no contexto.
3. Roteamento por formato: Electron/ASAR → entrypoint, preload, IPC e módulos nativos; Mach-O/ELF/PE → símbolos e bibliotecas; Go → build info; .NET/APK/WASM → descompiladores especializados se realmente disponíveis; SQLite → cópia consistente (inclusive WAL) e consultas read-only; pcap/HAR → inventário de tráfego com dados sensíveis protegidos.
4. Em árvores extraídas, não ignorar caminhos ocultos relevantes; preferir pequenos trechos em torno de strings e referências. Comparar inventários entre versões antes do diff completo.
5. Classificar evidência como observado, inferido ou desconhecido, com caminho, símbolo, offset ou localização. Busca negativa parcial não demonstra ausência de funcionalidade; leitura estática não é execução verificada.
6. Escalar para instrumentação dinâmica só com autorização e isolamento; não instalar ou executar ferramentas simplesmente porque aparecem na referência.

Síntese de https://github.com/aicodeking/leanrea/blob/main/leanrea/SKILL.md (2026-10-18). Sem executar a ferramenta nem extrapolar benchmarks de Claude Code para o ChatGPT.

## Memória persistente e diff estrutural de achados (REAgraph)

Quando uma investigação autorizada cruzar sessões ou comparar versões de artefatos, use um ledger persistente de descobertas antes de repetir probes:

1. Identifique cada artefato por hash, versão, plataforma e escopo da análise. Preserve os localizadores e a proveniência de cada achado.
2. Registre nós e relações com estado epistêmico (observado/extraído, inferido, ambíguo, não verificado). Mescle achados repetidos por identidade estável e promova confiança apenas quando houver nova evidência observável.
3. Para comparação de builds, não use endereços, offsets ou IDs temporários como única identidade. Alinhe símbolos, papéis e vizinhança estrutural; diferencie adição, remoção, alteração de relações e mera relocação. Em empates, abstenha-se em vez de afirmar correspondência.
4. Resuma o subgrafo necessário para a pergunta em vez de recarregar todo o corpus. Reutilize análises previamente verificadas apenas quando hash e escopo forem compatíveis; invalide o cache quando mudarem.
5. Ao comparar fonte e artefato distribuído, reporte elementos sem correspondência como **não explicados**, não como automaticamente maliciosos. Atribua cobertura e confiança; ausência de achado não comprova ausência do comportamento.
6. Verifique manualmente amostras de alinhamentos e mudanças de alto risco antes de declarar equivalência, regressão ou integridade.

**Portabilidade e segurança:** REAgraph é referência técnica, não runtime nativo do ChatGPT. Só invoque seu CLI/MCP se efetivamente disponível e autorizado. Não instale dependências, não execute binários desconhecidos, não acione REA, Docker, npx, servidores ou cache remoto como efeito implícito. Dados privados não devem ser publicados em cache compartilhado. Não extrapole benchmarks sintéticos ou exemplos específicos para precisão universal.

Origem complementar: https://github.com/Graphify-Labs/REAgraph (README, 2026-10-21). O Graphify já fundamenta as regras de grafo de evidência desta skill; portanto não criar owner duplicado.
