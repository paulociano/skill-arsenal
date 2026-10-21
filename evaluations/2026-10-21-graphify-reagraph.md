# Avaliação: Graphify + REAgraph (2026-10-21)

## Fontes
- https://github.com/Graphify-Labs/graphify (branch padrão `v8`): README.md, ARCHITECTURE.md, metadados.
- https://github.com/Graphify-Labs/REAgraph (branch padrão `main`): README.md, metadados.
- Fonte canônica Arsenal: `ARSENAL INDEX.md`, `stacks/arsenal-autopilot/STACK.md`, `stacks/evaluate-and-import-skill/STACK.md`, `skills/code-understanding-audit/SKILL.md`, `skills/repository-evidence-docs/SKILL.md`, `AGENTS.md`.

## Classificação e decisão

### Graphify: A/D; KEEP_EXTERNAL_REFERENCE (metodologia já absorvida)
- **Função real:** extração AST local de repositórios e ingestão multimodal opcional; modelagem de nós/arestas com proveniência; caminhos e consultas por subgrafo; comunidades e exports.
- **Ganho:** navegação arquitetural e seleção de contexto em projetos grandes. Requer pacote Python `graphifyy`, parsers, opcionais semânticos e integração para consultas reais.
- **Overlap:** `code-understanding-audit` já incorpora explicitamente relações EXTRACTED/INFERRED/AMBIGUOUS, proveniência e subgrafos, com referência a Graphify. `repository-evidence-docs` já prevê mapa de dependências e refresh incremental. Não criar skill separada nem alegar runtime instalado.
- **Cautelas:** marketing de economia de tokens/benchmarks não é garantia generalizável; extrações inferidas não comprovam causalidade; processamento semântico pode enviar dados ao backend configurado.
- **Decisão:** nenhuma alteração adicional no owner por ausência de ganho metodológico novo claramente incremental.

### REAgraph: A/D; UPDATE_EXISTING
- **Função real:** merge/dedup de findings num grafo persistente; confidence upgrade, resumo limitado, diff de versões por identidade estrutural independente de offsets/IDs de build; cache content-addressed; integração opcional com REA; alinhamento entre source graph e shipped graph.
- **Ganho incremental:** memória e diff estrutural dos achados autorizados, distinguindo artefato realocável de mudança funcional, com abstention nos matches incertos. Não coberto com essa especificidade no owner atual.
- **Destino:** `skills/code-understanding-audit/SKILL.md` (nova seção “Memória persistente e diff estrutural de achados (REAgraph)”).
- **Não criar skill própria:** análise de código/binário e gestão de evidências já têm owner canônico; REAgraph é implementação técnica externa que não deve ser confundida com ferramenta nativa.
- **Cautelas:** execução de binários, `npx`/Node, REA, Docker, MCP e caches compartilhados demandam permissão e revisão específica. Não conectar sem consentimento e sem verificar a disponibilidade. Um residual não explicado não comprova malware. Benchmarks do próprio projeto, alguns sintéticos, não validados aqui.

## Segurança e portabilidade
Análise documental, sem instalar nem executar Graphify/REAgraph/REA; sem acessar binários alvo, credenciais, ambientes de usuário ou cache externo. O fluxo adaptado funciona com inspeção de GitHub e comparação fundamentada de evidências; operações automatizadas de grafo somente com runtime de fato acessível. Nenhum script externo incorporado.

## Acceptance cases
- **Should-trigger:** auditoria de versões de APK/ASAR/binário autorizado com muitas descobertas e IDs voláteis; alinhar por estrutura e registrar incerteza.
- **Near-miss:** explicar uma função isolada em um único arquivo; usar leitura direta, não criar ou exigir grafo persistente.
- **Verificação necessária:** demonstrar em dois builds controlados que relocação não aparece como mudança real e que mutações reais são identificadas com evidência; sem runtime não alegar prova empírica.

## Materialização
- UPDATE_EXISTING: `skills/code-understanding-audit/SKILL.md`.
- KEEP_EXTERNAL_REFERENCE: Graphify, já presente no mesmo owner.
- Sem novo índice/stack, pois não houve criação nem alteração material de description.
- Commit de owner: `c88a60b49312690ee899413f32732bc16da22033`.
- Registro desta avaliação publicado separadamente. Verificação final deve reler os dois arquivos publicados.

## Limitação
A metodologia foi adaptada por leitura de README e arquitetura, não por execução de testes nem auditoria profunda do código-fonte de terceiros.
