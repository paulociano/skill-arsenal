# Avaliação — Heatcheck GitHub Hot Repos 2026-07-14

Data da avaliação: 2026-09-20

Fonte fornecida:
https://github-hot-repos-20260714.heatcheck.workers.dev/

## Recuperação da lista

O endpoint Heatcheck fornecido não estava acessível pelos mecanismos de fetch disponíveis durante a avaliação. A lista de 2026-07-14 foi reconstruída por arquivos históricos independentes de GitHub Trending e então cada candidato relevante foi inspecionado no GitHub canônico.

Lista avaliada:

- moeru-ai/airi
- Shubhamsaboo/awesome-llm-apps
- hasaneyldrm/exercises-dataset
- Graphify-Labs/graphify
- Nutlope/hallmark
- coreyhaines31/marketingskills
- OpenCut-app/OpenCut
- github/spec-kit
- HKUDS/Vibe-Trading
- Raphire/Win11Debloat

Fluxo: evaluate-and-import-skill + skill-security-review.

Nenhum installer, package, hook, binary, script de sistema, broker connector ou código externo foi executado.

## Decisão resumida

Nenhuma skill nova.

Mudanças úteis:
- Graphify → code-understanding-audit;
- Hallmark → web-design-engineer;
- Spec Kit → to-spec + to-tickets;
- Vibe-Trading → loop-engineering.

Os demais foram registrados sem importação por serem dataset, produto, catálogo amplo, implementação ainda em rewrite ou ferramenta de sistema altamente específica.

## Avaliações

### moeru-ai/airi

Classificação D/B.

Plataforma complexa de personagem/companheiro multimodal com browser, desktop, PWA, WebGPU/WebAudio/WebAssembly, modelos locais e integrações de jogos/voz.

Valor metodológico real existe em lifecycle multimodal e capability fallback, mas já há sobreposição relevante com crossplatform-mobile-engineering, realtime voice patterns, model routing e UI runtime.

Segurança: CAUTION alto. Downloads executáveis, modelos, plugins, rede, áudio, integrações externas e ações sobre jogos/sistemas.

Decisão: não importar nesta rodada.

### Shubhamsaboo/awesome-llm-apps

Classificação B/C/D conforme subprojeto.

É uma coleção extensa de agentes, RAG apps e Agent Skills. O repositório afirma gates de segurança/eval para sua coleção, mas isso não substitui avaliação individual de cada skill.

Valor: forte como fonte de discovery.

Segurança: CAUTION por installers e dezenas de apps/providers/dependências diferentes.

Decisão: não importar a coleção como autoridade. Skills individuais podem ser avaliadas separadamente quando trouxerem ganho específico.

### hasaneyldrm/exercises-dataset

Classificação D.

Dataset de exercícios com schema, instruções multilíngues e mídia.

Valor: útil como dado para produtos fitness, não como metodologia operacional do Arsenal.

Segurança/licença: CAUTION de provenance de mídia. Código/dados são apresentados sob termos próprios e a mídia tem atribuição/termos separados.

Decisão: não criar skill.

### Graphify-Labs/graphify

Classificação A/B/D.

Transforma code/docs/media em knowledge graph consultável. O padrão mais valioso é distinguir relações EXTRACTED, INFERRED e AMBIGUOUS e manter locators/audit trail.

Segurança: CAUTION. Instala pacote, skills e hooks; extras podem usar APIs, transcrição e bancos externos. Strict mode pode bloquear a primeira leitura direta de fonte.

Decisão: absorver apenas provenance-aware graph analysis em code-understanding-audit.

### Nutlope/hallmark

Classificação A/B.

Skill de design com macrostructure, audit/redesign/study e anti-pattern checks. O ponto útil não é sua lista estética, mas a ideia de fingerprint estrutural e estudo de referência por DNA/estrutura sem pixel-cloning.

Segurança: APPROVE metodologicamente na parte importada. Ferramentas/assets externos continuam sujeitos a revisão própria.

Decisão: reforçar web-design-engineer. Não importar temas nem gates subjetivos como regras universais.

### coreyhaines31/marketingskills

Classificação B/C por coleção, com várias skills potencialmente A individualmente.

Biblioteca ampla de marketing skills com product-marketing context compartilhado, CRO, SEO, analytics, email, pricing, launch e outros.

Valor: alto como catálogo, mas grande sobreposição com skills já presentes no Arsenal.

Segurança: CAUTION moderado. Inclui tool integrations, partners e opções de instalação; integrações patrocinadas são declaradas separadamente.

Decisão: não importar em bloco. Avaliar skills individuais quando houver lacuna concreta.

### OpenCut-app/OpenCut

Classificação D/B.

Editor de vídeo open source em rewrite, com planos para Editor API, plugins, MCP, headless rendering e scripting.

Valor: arquitetura promissora, mas o README declara rewrite em andamento; não há contrato estável suficiente para mudar video-editing-pipeline agora.

Segurança: CAUTION por scripts de instalação/toolchain e futura superfície de plugins/MCP.

Decisão: registrar e reavaliar quando a nova arquitetura estiver estabilizada.

### github/spec-kit

Classificação A.

Metodologia de Spec-Driven Development com constitution, specify, plan, tasks, implement, converge, clarify e análise de consistência.

Valor: material, mas não exige nova skill porque o Arsenal já separa to-spec, to-tickets, tdd e diagnóstico.

Segurança: CAUTION operacional por CLI/extensions/workflows; metodologia documental aprovada.

Decisão: incorporar spec → plan → tasks → implement → converge e rastreabilidade cruzada em to-spec/to-tickets.

### HKUDS/Vibe-Trading

Classificação B/D, domínio de alto risco.

Sistema agentic de pesquisa/trading com brokers, paper/live separation e ações live sob mandato limitado.

Valor reutilizável: user-committed mandate, caps, structural environment guard, fail-closed order gate, independent kill switch e audit ledger.

Segurança: CAUTION alto. Pode realizar ações financeiras reais, OAuth/broker connectors e execução autônoma persistente.

Decisão: importar somente o padrão genérico de bounded autonomy para loop-engineering. Nenhuma estratégia, broker ou lógica financeira foi incorporada.

### Raphire/Win11Debloat

Classificação D.

Script PowerShell de administração do Windows para remover apps e alterar dezenas de configurações do sistema.

Segurança: CAUTION alto por execução como administrador, irm/scriptblock, execution policy e alterações amplas do SO, ainda que o projeto documente reversão.

Decisão: não importar nem executar. O Arsenal já possui security review capaz de tratar esse tipo de installer/system script.

## Mudanças aplicadas

- code-understanding-audit: grafo de evidência com EXTRACTED/INFERRED/AMBIGUOUS;
- web-design-engineer: fingerprint estrutural e estudo de referência sem pixel clone;
- to-spec: cadeia spec → plan → tasks → implementation → verification/convergence;
- to-tickets: rastreabilidade de tickets para requisitos/contratos e convergence gaps;
- loop-engineering: mandato explícito, caps, fail-closed guard, kill switch e audit ledger;
- registro desta avaliação.

## Limites

- o endpoint Heatcheck original estava indisponível para fetch;
- a lista foi reconstruída usando snapshots históricos e validada no GitHub dos projetos;
- revisão de segurança foi manual/semântica;
- nenhuma dependência externa foi executada;
- benchmarks e claims promocionais não foram reproduzidos.
