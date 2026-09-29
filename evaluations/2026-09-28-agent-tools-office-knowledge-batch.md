# Avaliação — ferramentas de agentes, Office e conhecimento

Data: 2026-09-28, America/Sao_Paulo. Fonte canônica: GitHub. Stack: arsenal-autopilot, após ARSENAL INDEX.md.
Escopo: 23 projetos distintos; Magnitude apareceu duas vezes e foi deduplicado. Pesquisa documental, sem instalar ou executar fontes.

## Resolução de links

Links truncados resolvidos no GitHub pelo owner e nome: vectorize-io/hindsight, NVIDIA/Model-Optimizer, zhaoxuya520/reverse-skill, alibaba/open-code-review, bilawalsidhu/gods-eye-view, melgarafael/DeskcommCRM e robbietilton/Compositor. Magnitude corresponde ao link completo fornecido.

**Mobile Next permanece uma correspondência provável**, avaliada como mobile-next/mobile-mcp pelo nome e finalidade. O prefixo enviado também pode designar mobilewright ou mobilecli. Não declarar resolução inequívoca nem instalar; pedir URL completa se o usuário quiser adotar a ferramenta específica.

Os timestamps vieram do usuário; o vídeo não foi fornecido nem assistido. Não atribuir funcionalidades ao vídeo. A descrição atual de Magnitude é inferência local, não browser automation.

## Resultado por projeto

A = método que muda comportamento; B = metodologia absorvível; C = prompt sem ganho; D = sistema técnico. Classes combinadas separam método e runtime. Nenhuma fonte foi classificada C apenas por não ser adotada.

### dream-num/univer

- Fonte: https://github.com/dream-num/univer
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: SDK Office embutível, modelo de documentos e planilhas, fórmulas e plugins; útil em SaaS e ferramentas internas.
- Owner/correspondência no Arsenal: web-design-engineer.
- Dependências, limites e segurança: JS/TS, browser/Node, plugins e serviços por feature. Core Apache-2.0; Pro comercial separado, incluindo import/export e colaboração. Não tratar como geração simples de XLSX.

### Forward-Future/loopy

- Fonte: https://github.com/Forward-Future/loopy
- Classe: **A (absorção B)**. Decisão: **UPDATE_EXISTING**.
- Capacidade e uso: Descoberta de recorrência, ciclos com feedback e recibo reproduzível; ganho em diagnóstico de execuções.
- Owner/correspondência no Arsenal: loop-engineering.
- Dependências, limites e segurança: Método portátil; catálogo online e instalação Node opcionais. MIT. Não importar site, publicar loops ou criar agendas.

### DeusData/codebase-memory-mcp

- Fonte: https://github.com/DeusData/codebase-memory-mcp
- Classe: **D/B**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Índice estrutural persistente, consultas de grafo e impacto cross-service; método já presente.
- Owner/correspondência no Arsenal: code-understanding-audit.
- Dependências, limites e segurança: Binário nativo e assets, MCP, índice local; instalação altera configuração e inicia processos. SECURITY registra checagem externa de release. MIT; benchmarks não reproduzidos.

### magnitudedev/magnitude

- Fonte: https://github.com/magnitudedev/magnitude
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Motor atual de inferência local com seleção de modelos por hardware; útil ao estudar serving local.
- Owner/correspondência no Arsenal: ml-production-engineering.
- Dependências, limites e segurança: App/CLI, pesos, RAM/GPU e licenças dos modelos. Apache-2.0 no repo. Não é ferramenta de browser segundo o README atual; duplicata da lista consolidada.

### vectorize-io/hindsight

- Fonte: https://github.com/vectorize-io/hindsight
- Classe: **A/D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Retain/recall/reflect e bancos de memória para agentes; avaliação anterior mantida.
- Owner/correspondência no Arsenal: loop-engineering / kb-retriever.
- Dependências, limites e segurança: Servidor/embedded, storage e LLM conforme configuração; MIT declarada. Não substitui nem instala a memória nativa do ChatGPT.

### NVIDIA/Model-Optimizer

- Fonte: https://github.com/NVIDIA/Model-Optimizer
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Quantização, pruning, distillation, NAS e speculative decoding; útil para otimizar modelos realmente operados.
- Owner/correspondência no Arsenal: ml-production-engineering.
- Dependências, limites e segurança: Python, modelos e backends/hardware compatíveis, dados de calibração/treino conforme técnica; Apache-2.0 declarada. Medir qualidade e desempenho antes/depois.

### openbao/openbao

- Fonte: https://github.com/openbao/openbao
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Gestão de segredos, certificados e chaves para infraestrutura de aplicações.
- Owner/correspondência no Arsenal: production-go-live / system-design-engineering.
- Dependências, limites e segurança: Serviço, storage, autenticação, políticas, backup e operação; MPL-2.0 nos metadados. Registrar referência, não provisionar cofre nem mover credenciais.

### zhaoxuya520/reverse-skill

- Fonte: https://github.com/zhaoxuya520/reverse-skill
- Classe: **A/D**. Decisão: **REJECT como importação ampla; KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Router técnico para APK/binário/JS/CTF e testes autorizados. Não é extração de regras de negócio de legado.
- Owner/correspondência no Arsenal: skill-security-review; sem owner novo.
- Dependências, limites e segurança: Depende de ferramentas/MCP/scripts específicos. MIT declarada. RULES exige ativação/escopo; não importar gatilhos amplos, bootstrap ou instruções de obediência. Inspeção documental não autoriza atividade contra alvos.

### mobile-next/mobile-mcp

- Fonte: https://github.com/mobile-next/mobile-mcp
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE (correspondência provável)**.
- Capacidade e uso: Automação Android/iOS por árvore de acessibilidade e screenshots; método já coberto.
- Owner/correspondência no Arsenal: mobile-device-automation.
- Dependências, limites e segurança: MCP, dispositivo/simulador, ADB/Xcode ou serviço cloud conforme target. Link enviado mobile... é ambíguo: existem mobilewright e mobilecli. Não instalar com base nesta resolução provável.

### Tencent/WeKnora

- Fonte: https://github.com/Tencent/WeKnora
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Plataforma de RAG, agente e wiki; candidata para conhecimento documental corporativo.
- Owner/correspondência no Arsenal: retrieval-quality-engineering / kb-retriever.
- Dependências, limites e segurança: Modelos, storage/search, conectores e sandboxes conforme função. LICENSE declara MIT com termos de componentes terceiros. Exigir ACL, proveniência e testes de retrieval; não executar skills remotas automaticamente.

### alibaba/open-code-review

- Fonte: https://github.com/alibaba/open-code-review
- Classe: **A/D**. Decisão: **UPDATE_EXISTING**.
- Capacidade e uso: Seleção verificável de arquivos, agrupamento por relação e posicionamento separado de findings.
- Owner/correspondência no Arsenal: code-review.
- Dependências, limites e segurança: CLI e endpoint LLM para runtime; código pode ser enviado ao provedor. Adaptar método sem CLI, sem importar alegações de redução de tokens ou delegação obrigatória.

### bilawalsidhu/gods-eye-view

- Fonte: https://github.com/bilawalsidhu/gods-eye-view
- Classe: **D/B**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Globo 3D com camadas públicas, exploração espacial e direção de cenas; referência para dashboards geográficos.
- Owner/correspondência no Arsenal: web-design-engineer / creative-web-effects.
- Dependências, limites e segurança: Browser/render 3D, feeds, rede e chaves opcionais. Dados/imagery têm termos próprios; README informa tráfego simulado e poses estimadas. Não chamar todo dado de live nem confundir estilo visual com medição real.

### Lakr233/vphone-cli

- Fonte: https://github.com/Lakr233/vphone-cli
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE com restrição forte**.
- Capacidade e uso: iPhone virtual para pesquisa em Apple Silicon; não necessário para automação móvel comum.
- Owner/correspondência no Arsenal: mobile-device-automation.
- Dependências, limites e segurança: Mac físico Apple Silicon, macOS compatível, firmware, disco e rede; README 2.x exige relaxar restrições de debug/SIP e habilitar research guests, helper privilegiado. Não executar nem recomendar como instalação padrão.

### melgarafael/DeskcommCRM

- Fonte: https://github.com/melgarafael/DeskcommCRM
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: CRM de WhatsApp com agentes, atendimento e automações; referência para gestão comercial.
- Owner/correspondência no Arsenal: web-design-engineer; gestao-comercial-da-semana para requisitos.
- Dependências, limites e segurança: Next.js/TS, Supabase, Docker/VPS, canal WhatsApp e LLM. MIT declarada. Instalador cria cron/agente de atualização e altera banco/servidor. Canal QR/WAHA e canal oficial Meta são opções distintas; avaliar integração e custos reais antes de adoção.

### MakazhanAlpamys/Soup

- Fonte: https://github.com/MakazhanAlpamys/Soup
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Fine-tuning configurável com YAML, ferramentas de treino e layer streaming experimental.
- Owner/correspondência no Arsenal: ml-production-engineering.
- Dependências, limites e segurança: Python, stack de treino, pesos/dados e hardware. Apache-2.0. README ressalva que números de 4 GB precedem correção e aguardam nova medição; não transformar em garantia.

### robbietilton/Compositor

- Fonte: https://github.com/robbietilton/Compositor
- Classe: **D/B**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Editor de imagem em camadas e formato .comp gravável por scripts/agentes; útil para artefatos editáveis.
- Owner/correspondência no Arsenal: editable-visual-design.
- Dependências, limites e segurança: macOS 26+ Apple Silicon, Xcode para build; MIT declarada. Não confundir com componente web ou substituto disponível neste ambiente. Ler schema .comp e validar abertura/export no app antes de produzir esse formato.

### driceroland/Search

- Fonte: https://github.com/driceroland/Search
- Classe: **D**. Decisão: **REJECT como skill; referência de produto**.
- Capacidade e uso: Navegador WebKit minimalista para macOS; não é mecanismo de busca/RAG.
- Owner/correspondência no Arsenal: sem novo owner.
- Dependências, limites e segurança: macOS 14+, projeto nativo; MIT nos metadados. Não acrescenta capacidade operacional ao Arsenal sem runtime; baixa prioridade.

### yc-software/qm

- Fonte: https://github.com/yc-software/qm
- Classe: **D/B**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Agente organizacional em Slack/web com escopos pessoais e compartilhados.
- Owner/correspondência no Arsenal: loop-engineering / system-design-engineering.
- Dependências, limites e segurança: Node/TS, Postgres para durabilidade, sandboxes, modelos e conectores. MIT. Posturas de execução e de compartilhamento são diferentes; configuração padrão não equivale a revisão humana de cada ação.

### herdrdev/herdr

- Fonte: https://github.com/herdrdev/herdr
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Runtime de terminais de agentes, panes, SSH e retomada de sessões.
- Owner/correspondência no Arsenal: multi-agent-orchestration.
- Dependências, limites e segurança: Binário Rust e agentes externos; Apache-2.0. Detach não encerra processo, mas reboot não preserva processos originais. Este repo não é eliasstravik/herdr-projects, avaliado antes.

### CopilotKit/openmuse

- Fonte: https://github.com/CopilotKit/openmuse
- Classe: **D/B**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Aplicação de agente pessoal com tarefas, workers, arquivos e browser; método durável já absorvido.
- Owner/correspondência no Arsenal: loop-engineering.
- Dependências, limites e segurança: Node/pnpm, workers e CopilotKit Intelligence project key; README atual diz que serviço Intelligence separado é obrigatório para persistência/replay e não está incluído na licença MIT do repo. Atualizar a leitura prática da avaliação anterior sem duplicar método.

### hydra-db/open-glean

- Fonte: https://github.com/hydra-db/open-glean
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE**.
- Capacidade e uso: Busca e conhecimento conectados ao Hydra DB; referência para experiência de busca corporativa.
- Owner/correspondência no Arsenal: kb-retriever / retrieval-quality-engineering.
- Dependências, limites e segurança: Next.js/React, Hydra API e configuração LLM; MongoDB quando usado. Apache-2.0. Não presumir operação totalmente local/autônoma nem acesso a fontes conectadas deste usuário.

### vladelaina/BongoCat

- Fonte: https://github.com/vladelaina/BongoCat
- Classe: **D**. Decisão: **REJECT como skill**.
- Capacidade e uso: Pet nativo reativo ao input; valor de produto/asset, sem método novo para tarefas do Arsenal.
- Owner/correspondência no Arsenal: sem novo owner.
- Dependências, limites e segurança: C/C++, SDL3/OpenGL; SDK Cubism opcional. Runtime AGPL-3.0-only e assets padrão MIT separados. Não equivale ao formato de pets do ChatGPT.

### volotat/mini-AGI

- Fonte: https://github.com/volotat/mini-AGI
- Classe: **D**. Decisão: **KEEP_EXTERNAL_REFERENCE apenas pesquisa; não adotar em produção**.
- Capacidade e uso: Experimento byte-level de aprendizagem contínua com pesos paginados e arquitetura adaptativa.
- Owner/correspondência no Arsenal: ml-production-engineering.
- Dependências, limites e segurança: GPU/corpus/tempo de treino; MIT nos metadados. Autor chama de toy-level e informa pesos ainda não publicados. Não é agente geral pronto.

## Mudanças justificadas

1. **loop-engineering:** distinguir recorrência observada de oportunidade inferida; guardar versão exata e critérios do loop no recibo; separar falha de design, execução, ambiente e objetivo antes de alterar o método. Fonte: Loopy, SKILL.md e references/run.md/debrief.md.
2. **code-review:** inventário de cobertura com exclusões explícitas, grupos de arquivos relacionados, regras pertinentes e validação separada de localização/conteúdo do finding. Fonte: OpenCodeReview, seção Deterministic Engineering × Agent Hybrid.
3. **web-design-engineer:** rota sob demanda para Univer, WeKnora, DeskcommCRM, God's Eye View e qm, com requisitos e limites específicos.
4. **Referência central de produtos web** criada, sem cópia de implementações.
5. Este registro consolida decisões para todos os projetos.

Nenhuma skill ou stack nova. Nomes e descriptions existentes preservados; ARSENAL INDEX.md já aponta aos owners e não requer alteração. As demais fontes permanecem referências ou rejeições como skill, sem instalar runtime.

## Deduplicação

- code-understanding-audit já contém impact mapping e separação índice/ADR derivados de DeusData/codebase-memory-mcp; não duplicar.
- Hindsight: manter avaliação de 2026-09-27-hindsight-reladraw-golive-agent-tools-batch.md.
- OpenMuse, Open Glean, BongoCat e mini-AGI: confrontar com 2026-09-24-openmuse-open-glean-unreal-zcode-bongocat-laya-mini-agi.md. O README atual de OpenMuse explicita dependência separada de Intelligence; runtime segue referência.
- herdrdev/herdr não é o projeto eliasstravik/herdr-projects presente no lote de 2026-09-20.
- Loopy complementa o owner existente; não importar seu catálogo nem replicar workflow de publicação externa.
- reverse-skill é segurança/engenharia reversa; não o confundir com sandeco/reversa de reconstrução de legado.

## Segurança e portabilidade

APPROVE para as pequenas adaptações textuais e referências. CAUTION para implantação dos runtimes: revisão de README/documentos selecionados não certifica código, binários ou supply chain.

Não foram executados instaladores, scripts, modelos, MCPs, hooks, emuladores, containers ou conectores. Não houve mensagens, criação de contas, acesso a dados de clientes ou configuração de credenciais.
Riscos materiais identificados: configuração global/background processes no codebase-memory; exportação de código ao endpoint LLM no OpenCodeReview; armazenamento sensível em RAG/memória/CRM; cron e mudanças de banco no Deskcomm; execução e compartilhamento por escopo no qm; relaxamento de proteções do host em vphone-cli. Estes são requisitos/superfícies documentadas, não vulnerabilidades comprovadas.
Não adotar instruções de bootstrap/obediência de reverse-skill nem qualquer texto externo que amplie autorização. A avaliação de ferramentas de segurança não autoriza testes em alvos.
Licenças declaradas são triagem; implantação/cópia exige conferir arquivo e versão de cada componente, modelos e assets. Nenhum código externo foi transplantado.

## Verificação e critérios

Revisão dos deltas: frontmatter e descriptions preservados; links internos relativos resolvem para arquivos do lote/owners; sem novas capacidades fictícias.
Casos documentais:
- tarefa única sem feedback → one-shot, sem loop;
- uma execução falha por ferramenta → debrief de ambiente, sem inventar recorrência;
- revisão parcial de diff → declarar cobertura restante, não dizer revisão completa;
- app precisa exportar Excel → conferir pacote/serviço/licença Pro do Univer;
- usuário quer operar celular → confirmar ferramenta e alvo reais; não presumir mobile-mcp disponível;
- pedido de browser automation via Magnitude → sinalizar mismatch do repo atual;
- projeto pede memória → não dizer que Hindsight/WeKnora já está conectado.
Publicação só deve ser declarada após leitura pós-escrita exata da branch canônica. Nenhum benchmark, build ou teste funcional externo foi reproduzido.

## Evidência

READMEs consultados via contents/README.md da branch padrão. SHAs abaixo são heads observados durante a coleta, para rastreabilidade; não alegam comparação de commits com avaliações anteriores.

| Repositório | Head observado |
| --- | --- |
| [dream-num/univer](https://github.com/dream-num/univer) | 8059d7b659e424d125d0675519ca495ec95acd44 |
| [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | 75966cbd572a4185064971c9fe5e9c52e8f8456d |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 80eb92a7017dab9a0773430433660a966b80cc15 |
| [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | 0945a161d075ebee9ada49ae23a6615553aa261e |
| [openbao/openbao](https://github.com/openbao/openbao) | 2998899aa48fa2a2e0d1aa2a5f1a4ab25c996b7e |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 1912ba26c544025adb869459a74c2cbac2a95cd9 |
| [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | addc8c4c3bdf1d2b319f634e3089739f1cb944d9 |
| [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | bb709b6723468c3dd2138ffc0b055095116f16a5 |
| [driceroland/Search](https://github.com/driceroland/Search) | 1ec28a0d7cae049adc637c9013fd80bce06fc053 |
| [yc-software/qm](https://github.com/yc-software/qm) | 6b6a54cd87b0f6cc5484dd73aee71734385c12dc |
| [herdrdev/herdr](https://github.com/herdrdev/herdr) | 9dc3a1df2b563df0637264fc0dffcd607c324ac5 |
| [CopilotKit/openmuse](https://github.com/CopilotKit/openmuse) | 34b15bc80340e582fb8c25573646cfb0bbc5184d |
| [hydra-db/open-glean](https://github.com/hydra-db/open-glean) | eee8cffd19e37c875d0f5fd854da7db530e6a6a6 |
| [vladelaina/BongoCat](https://github.com/vladelaina/BongoCat) | 3fa24ad1e160a7068b439899937cd17053fc2851 |
| [volotat/mini-AGI](https://github.com/volotat/mini-AGI) | f932ff8d0903ff12f4f55e3e23c554b89e33dad6 |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 1e427025b4d4c01e8ad6385dd04e02102886a5c4 |
| [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer) | be740012568eb2ff97af1c08f7a283c5edd766c2 |
| [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | cab634bd855fc287f6e420c1f36fd1a6b9245960 |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | 18d0e8c44ef4dbc4113d57ee917c51f2da5678d4 |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | ebb69835a3a2d25468b6a68ba6092b9b8fe6bcb0 |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | e7707d9a0f34d9fbffc300023c319f95caa5be30 |
| [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) | 5eb942a6d810137af08b75c26640325e7f077083 |
| [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | de442f245401e47a7eddae4b83c32737352a0b4d |

Leituras adicionais: Forward-Future/loopy/skills/loopy/SKILL.md e references/run.md/debrief.md; DeusData/codebase-memory-mcp/SECURITY.md; zhaoxuya520/reverse-skill/RULES.md; Tencent/WeKnora/LICENSE. Owners e avaliações anteriores foram lidos no GitHub. Não houve auditoria completa das 23 bases.
