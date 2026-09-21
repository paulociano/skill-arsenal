# Avaliação — Repositórios de skills, pesquisa, vídeo, memória de codebase e PM

Data: 2026-09-20

## Fontes avaliadas

- https://github.com/saasscaleup/20-superpowers-github-repositories
- https://github.com/MengTo/Skills
- https://github.com/harry0703/MoneyPrinterTurbo
- https://github.com/DeusData/codebase-memory-mcp
- https://github.com/calesthio/OpenMontage
- https://github.com/mvanhorn/last30days-skill
- https://github.com/Panniantong/Agent-Reach
- https://github.com/microsoft/markitdown
- https://github.com/lfnovo/open-notebook
- https://github.com/phuryn/pm-skills

Fluxo: evaluate-and-import-skill + skill-security-review.

Nenhum installer, binary, Docker image, hook, scraper, browser-cookie reader, provider API, MCP server ou script externo foi executado.

## Decisão resumida

Nenhuma nova skill foi criada.

Mudanças aplicadas:
- MengTo/Skills → skill-builder;
- MoneyPrinterTurbo + OpenMontage → video-editing-pipeline;
- codebase-memory-mcp → code-understanding-audit;
- last30days-skill → niche-research;
- Agent-Reach → web-extraction-pipeline;
- MarkItDown → document-extraction-pipeline;
- Open Notebook → kb-retriever;
- pm-skills → idea-refine.

20-superpowers-github-repositories foi mantido apenas como catálogo de discovery.

O ARSENAL INDEX não foi alterado porque nenhuma skill foi criada, removida, renomeada ou teve description materialmente modificada.

## 1. saasscaleup/20-superpowers-github-repositories

### Classificação

C/B.

### O que faz

Lista curada de 20+ repositórios populares para desenvolvimento, estudo, APIs, system design e ferramentas.

### Valor

Serve como catálogo de descoberta, não como procedimento operacional. Vários itens já haviam sido avaliados separadamente pelo Arsenal, incluindo build-your-own-x, free-for-dev, public-apis e system-design-primer.

### Segurança

APPROVE como lista estática. Cada destino continua exigindo avaliação própria.

### Decisão

Não importar metodologia nem criar skill.

## 2. MengTo/Skills

### Classificação

A/B/D por skill.

### O que faz

Grande biblioteca de Agent Skills para UI, web design, vídeo, 3D, game development, automação e transformação de referências em prompts/workflows reutilizáveis.

### Valor reutilizável

A biblioteca traz uma disciplina forte de:
- skills pequenas por capability;
- source-to-skill ledger;
- portable contract separado de brand/layout incidentais;
- referências longas fora do SKILL principal;
- demos executáveis como evidência quando a skill é visual/interativa;
- input + expected-output para workflows não visuais;
- validação proporcional ao artefato.

Isso reforça skill-builder, que já cobre portabilidade, overlap, security review e baseline.

### Segurança

CAUTION.

A coleção inclui scripts, browsers, APIs, TTS, assets, automações, Three.js e integrações variadas. A segurança deve ser avaliada por skill; não é seguro instalar a biblioteca inteira apenas para consulta metodológica.

### Decisão

Atualizar skill-builder com extraction ledger e proof-oriented demos. Não importar a coleção em bloco.

## 3. harry0703/MoneyPrinterTurbo

### Classificação

B/D.

### O que faz

Pipeline completo de geração de vídeo a partir de tema ou roteiro: script, busca/seleção de materiais, voiceover, subtitles, music e composição/render.

### Valor reutilizável

A principal contribuição é tratar geração de vídeo como pipeline por estágios, permitindo usar roteiro pronto, material local, diferentes fontes/providers e parar/reusar etapas.

### Segurança

CAUTION alto.

Usa múltiplos providers de LLM, TTS, imagem/vídeo, uploads de mídia, API keys e processamento local/externo. Alguns providers têm custo e enviam dados para serviços de terceiros.

### Decisão

Absorver somente a estrutura tema → roteiro → assets → voz → legendas → música → composição em video-editing-pipeline, sem importar providers ou preços.

## 4. DeusData/codebase-memory-mcp

### Classificação

A/B/D.

### O que faz

Motor local de code intelligence que indexa codebases como knowledge graph, com AST/tree-sitter, LSP-like resolution, cross-service links, impact analysis, ADRs e MCP.

### Valor reutilizável

Além do graph analysis já incorporado ao Arsenal via Graphify, acrescenta:
- diff/symbol impact mapping;
- direct vs transitive impact;
- cross-service route/call linking;
- ADR persistente separado do índice derivado;
- índice como cache reconstruível, decisão arquitetural como conhecimento autoral.

### Segurança

CAUTION alto.

Distribui binário nativo, installer shell/PowerShell, configuração de MCP, skills, hooks, daemon, watchers e modificação de config de agentes. O README também documenta manipulação de quarantine/execution policy e tolerância específica de antivírus. Nada disso foi executado.

### Decisão

Incorporar apenas metodologia de impact analysis e architectural memory em code-understanding-audit.

## 5. calesthio/OpenMontage

### Classificação

A/B/D.

### O que faz

Studio agentic de produção audiovisual: research, scripting, asset generation/retrieval, editing e composição, com seleção entre FFmpeg, Remotion, HyperFrames e outros runtimes/providers.

### Valor reutilizável

Padrões fortes:
- runtime escolhido pelo tipo de composição;
- separação templated vs atelier/custom;
- composition runtime como decisão explícita;
- provider-specific prompting carregado só quando provider realmente é usado;
- produção de vídeo com footage real, não apenas animação de stills.

### Segurança

CAUTION alto.

Inclui grande superfície de tools/providers, geração de mídia, APIs pagas, execução de Node/FFmpeg, assets e skills vendorizadas.

### Decisão

Absorver runtime routing e templated/atelier em video-editing-pipeline. Não importar a stack nem as skills vendorizadas.

## 6. mvanhorn/last30days-skill

### Classificação

A/B/D.

### O que faz

Pesquisa assuntos recentes em múltiplas superfícies: Reddit, X, YouTube, TikTok, Hacker News, GitHub, web e outras, com comentários/transcripts, ranking e diagnostics.

### Valor reutilizável

O Arsenal já tinha niche-research, mas faltava distinguir:
- fact/news research;
- discourse/reaction research;
- mixed mode;
- engagement como sinal de saliência, não credibilidade;
- janela temporal exata;
- source health e cobertura real;
- busca em body/comments/transcripts em modo de discurso.

### Segurança

CAUTION alto.

O projeto pode ler cookies do navegador para X, usar auth tokens, APIs externas, yt-dlp e múltiplos CLIs. Essas dependências não foram importadas.

### Decisão

Atualizar niche-research com modos fact/discourse/mixed e health-aware coverage.

## 7. Panniantong/Agent-Reach

### Classificação

B/D.

### O que faz

Camada de acesso a plataformas sociais/nicho para agentes, com vários backends, fallback por plataforma e comando doctor para diagnóstico.

### Valor reutilizável

Padrão útil para web-extraction-pipeline:
- capability adapters por plataforma;
- primary + fallback legítimo;
- diagnostics available/degraded/unavailable;
- fallback não pode esconder cobertura parcial;
- health check separado de coleta.

### Segurança

CAUTION alto.

A ferramenta agrega acessos a plataformas com diferentes autenticações e restrições. Fallback não deve virar mecanismo de bypass de controles.

### Decisão

Incorporar apenas adapter/fallback/diagnostics em web-extraction-pipeline.

## 8. microsoft/markitdown

### Classificação

A/B/D.

### O que faz

Conversor de múltiplos formatos para Markdown, incluindo Office, PDF, formatos textuais, ZIP, YouTube e outros; pode usar plugins, LLMs e serviços Azure opcionais.

### Valor reutilizável

O ganho é um fast path de conversão:
- tentar primeiro converter formatos estruturados de forma determinística;
- ativar OCR/VLM/document intelligence somente onde necessário;
- plugins opcionais ficam off quando não necessários;
- serviços remotos precisam de boundary explícito de custo/upload/dados.

### Segurança

CAUTION moderado.

Core local é relativamente simples, mas plugins e integrações LLM/Azure ampliam rede, upload e custos. Plugins não devem ser habilitados automaticamente.

### Decisão

Atualizar document-extraction-pipeline com format router e lightweight conversion path.

## 9. lfnovo/open-notebook

### Classificação

B/D.

### O que faz

Workspace de pesquisa self-hosted com notebooks, sources, notes, transformations, full-text/vector search, citations, context selection, podcasts e múltiplos providers.

### Valor reutilizável

Metodologia útil:
- separar source, note, transformation e chat answer;
- permitir context selection por source;
- full-text e vector search como rotas complementares;
- derivação rastreável de transformations;
- citações devem apontar ao source original quando possível.

### Segurança

CAUTION alto.

Self-hosting envolve Docker, banco, encryption key, credenciais default para local, API keys e múltiplos providers. O README alerta para alterar secrets antes de exposição em rede.

### Decisão

Atualizar kb-retriever com modelo source/note/transformation e context selection. Não importar runtime.

## 10. phuryn/pm-skills

### Classificação

A/B/C/D conforme skill.

### O que faz

Marketplace amplo de skills e workflows de Product Management: discovery, strategy, PRD, metrics, launch, analytics, GTM, execution e AI shipping.

### Valor reutilizável

A coleção é ampla demais para importação em bloco e possui forte overlap com customer-interview, jtbd-framing, experiment-design, to-spec, founder-diagnose, discovery-research-synthesis e outras.

O ganho mais claro foi:
- assumption mapping por Value, Usability, Viability e Feasibility;
- categorias adicionais para novas iniciativas: ethics/safety, GTM, strategy e team;
- outcome → opportunities → solutions → experiments;
- priorizar assumptions críticas antes de investir em solução.

Não foi importada a fórmula de Risk/ICE da fonte como verdade automática, porque os inputs podem ser arbitrários e uma matriz qualitativa/evidência costuma ser mais segura.

### Segurança

APPROVE metodologicamente; CAUTION operacional para instalação de marketplace/plugins Claude/Codex e workflows com integrações.

### Decisão

Atualizar idea-refine com assumption mapping e opportunity-before-solution. Não criar PM mega-skill.

## Mudanças aplicadas

- skills/skill-builder/SKILL.md
- skills/video-editing-pipeline/SKILL.md
- skills/code-understanding-audit/SKILL.md
- skills/niche-research/SKILL.md
- skills/web-extraction-pipeline/SKILL.md
- skills/document-extraction-pipeline/SKILL.md
- skills/kb-retriever/SKILL.md
- skills/idea-refine/SKILL.md
- este registro de avaliação

## Limites

- revisão manual/semântica de segurança;
- nenhuma dependência ou installer externo foi executado;
- benchmarks e claims promocionais dos repositórios não foram reproduzidos;
- catálogos grandes foram avaliados como coleções e aprofundados somente onde havia ganho material;
- integrações, preços e disponibilidade de providers podem mudar e precisam de verificação atual quando forem usados de verdade.
