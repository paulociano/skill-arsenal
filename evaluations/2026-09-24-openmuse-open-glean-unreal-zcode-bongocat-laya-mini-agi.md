# Avaliação de oito repositórios: agentes, busca, interfaces e modelos locais

Data: 2026-09-24. Método: `evaluate-and-import-skill` com revisão documental de segurança conforme `skill-security-review`. Fontes canônicas: os repositórios vinculados abaixo, lidos no GitHub. A classificação A/B/C/D descreve o valor para o **Arsenal como skill**; não é nota de qualidade do produto.

| Fonte | O que faz e dependências reais | Classe e decisão |
| --- | --- | --- |
| [CopilotKit/openmuse](https://github.com/CopilotKit/openmuse) | App de agente pessoal com chat móvel/web, worker de tarefas, navegador Chromium persistente, container Linux opcional, documentos, Google OAuth e CopilotKit Intelligence. Exige Node/pnpm, chave de projeto, servidor; outros recursos exigem Docker, modelo, credenciais e serviços. | **D** como software. **B** para contrato de tarefa durável, revisão vinculada a alvo/versão, leases, receipts e resultado externo incerto. Incorporado em `loop-engineering`, sem instalar o produto. |
| [hydra-db/open-glean](https://github.com/hydra-db/open-glean) | Workspace Next.js sobre Hydra DB: retrieval com citações, escopo por coleção, pesquisa em DAG, conectores e respostas por modelo externo. Requer chave Hydra para dados reais, modelo para respostas; MongoDB opcional. | **D**. Não criar skill: `kb-retriever`, `graph-engineering` e `research-and-synthesize` já cobrem recuperação, subperguntas, fontes e síntese. Endpoint de modelo vinculado à chave é uma boa prática de implementação, sem motivo para nova skill. |
| [unreallabsai/unreal-agent](https://github.com/unreallabsai/unreal-agent) | Biblioteca Go de harness assíncrono: inbox por sessão, histórico persistido/forkável, coordinator, tool translators, operações serializáveis, manager e benchmarks. Exige implementação/execução do runtime Go. | **D**. **B** para IDs estáveis, deduplicação, separação de validação e execução e gravação atômica de status/operações. Incorporado em `loop-engineering`. |
| [zai-org/ZCode](https://github.com/zai-org/ZCode) | Plataforma de programação assistida com app Electron, web, TUI, CLI, servidor, plugins, MCP, hooks, sessões e ambientes remotos. Precisa de Node/pnpm, dependências nativas/ativos e configuração de provedores. | **D**. Não incorporar: é um runtime alternativo; padrões de ferramentas, permissões, workflows e verificação já têm owners no Arsenal. |
| [vladelaina/BongoCat](https://github.com/vladelaina/BongoCat) | Pet de desktop em C/SDL3/OpenGL que reage a input local; renderização Live2D completa exige Cubism SDK; build CMake baixa dependências por padrão. | **D**. Não criar skill. É produto/implementação de interface e input, não método reutilizável para tarefas de agente. |
| [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | Port MLX para Apple Silicon de modelo de decisões tipadas (choice, score e booleano) com probabilidades, sem geração de texto; requer macOS/MLX e pesos. | **D**. Não instalar nem criar skill: `structured-output-contract` e `ml-production-engineering` já cobrem contrato, validação e calibração; o ganho de latência depende do hardware, pesos, tarefa e benchmark. |
| [volotat/mini-AGI](https://github.com/volotat/mini-AGI) | Experimento de modelo byte-level com pool de experts em disco, paginação, crescimento/poda e aprendizagem contínua em GPU; README declara modelo ainda pequeno e pesos ainda não publicados. | **D**. Não importar. Hipóteses de pesquisa e resultados declarados pelo autor não viram procedimento geral de produção; `ml-production-engineering` já exige holdout, comparação e gate de promoção. |
| [mizorewww/laya-coreml](https://github.com/mizorewww/laya-coreml) | Port Core ML do Laya, incluindo opção ANE para decisões curtas; requer Apple Silicon, macOS e checkpoints; há limites específicos de tokens e hardware. | **D**. Mesma decisão do MLX: alternativa técnica de inferência, sem nova skill. Os benchmarks são do cenário documentado, não promessa geral de desempenho. |

## Valor incremental e aplicação

A única mudança no Arsenal foi em `skills/loop-engineering/SKILL.md`: adicionado contrato específico para inputs repetidos, operação persistida antes do despacho, leases, estados de recuperação, aprovação vinculada à ação, resultado externo incerto e limites do cancelamento. O conteúdo é metodológico e condicional à existência de storage/executor real. Nenhum runtime externo, checkpoint, asset, serviço ou dependência foi instalado. `ARSENAL INDEX.md` permanece válido: não surgiu skill/stack nem mudou description.

Os demais padrões úteis já estão representados em owners existentes: retrieval e citações em `kb-retriever`, grafo em `graph-engineering`, decisões tipadas em `structured-output-contract` e avaliação/continual learning em `ml-production-engineering`. Não transplantar benchmarks ou capacidades particulares para o ChatGPT.

## Segurança e portabilidade

**Parecer para importar código/instalar estes produtos como skill: CAUTION. Parecer para o pequeno método adaptado: APPROVE.** Não há indício demonstrado de comportamento malicioso nesta revisão documental, mas ela não é auditoria completa de código, dependências ou binários.

- OpenMuse pode operar email/calendário e navegador com perfis persistentes; suas aprovações e isolamento declarados dependem da configuração. O próprio documento de verificação separa testes com fixtures da aceitação de Google/modelo ao vivo.
- Open Glean usa chaves de Hydra/modelo no servidor e busca em fontes externas. Seu SECURITY.md declara que o assunto anônimo do navegador não é autenticação e que `HYDRA_API_KEY` de deployment seria compartilhada com visitantes; o operador precisa controlar acesso. URL de LLM associada à chave evita encaminhamento de credencial a endpoint trocado.
- Unreal Agent, ZCode e OpenMuse podem traduzir pedidos em ferramentas, arquivos, rede e processos; ZCode documenta hooks, MCP, ambientes remotos, uploads e modos permissivos sem sandbox de sistema por padrão. Revisar credenciais, contas e escopo antes de execução real.
- BongoCat processa eventos de teclado/mouse; o opt-in evdev no Linux pode observar entrada de outros apps, inclusive campos de senha. Seu runtime é AGPL-3.0-only; assets padrão têm licença MIT separada.
- Laya MLX/Core ML baixam pesos e dependem de plataformas/modelos específicos; resultados de fidelidade de conversão não demonstram acurácia geral. mini-AGI depende de corpus, GPU, treinamento e estado de pesos; ainda não há pesos publicados no README lido.

Nenhum installer, script, modelo, download de pesos ou binário foi executado. Não houve scanner estático nem teste de runtime; a revisão ficou em README e documentos selecionados. Portanto `CAUTION` indica superfície a revisar antes de adoção técnica, não uma acusação de vulnerabilidade.

## Evidência lida

- OpenMuse: [README](https://github.com/CopilotKit/openmuse/blob/main/README.md) (blob `1d4bd700e136c5b23d755b71528ef0445b32e405`) e [verificação](https://github.com/CopilotKit/openmuse/blob/main/docs/VERIFICATION.md).
- Open Glean: [README](https://github.com/hydra-db/open-glean/blob/main/README.md) (`cfa550f7ebdb25f18d7e31e152f97f6093948020`) e [SECURITY](https://github.com/hydra-db/open-glean/blob/main/SECURITY.md).
- Unreal Agent: [README](https://github.com/unreallabsai/unreal-agent/blob/main/README.md) (`47e6a5661859880fb9b87035430afef29d7a4a76`) e `go.mod`.
- ZCode: [README.en](https://github.com/zai-org/ZCode/blob/main/README.en.md), [README](https://github.com/zai-org/ZCode/blob/main/README.md) (`bd6247f26035e27ffb5f6c908d736c1c4c82fca7`) e [NOTICE](https://github.com/zai-org/ZCode/blob/main/NOTICE.md).
- BongoCat: [README](https://github.com/vladelaina/BongoCat/blob/main/README.md) (`2d92b558c953a5cb3ca8db33820ff966cc32c94a`) e [PRIVACY](https://github.com/vladelaina/BongoCat/blob/main/PRIVACY.md).
- Laya MLX: [README](https://github.com/mizorewww/laya-mlx/blob/main/README.md) (`2364a382cda161b92e4afc0a719bcb5619d1e6a8`).
- mini-AGI: [README](https://github.com/volotat/mini-AGI/blob/main/README.md) (`d387f42cea98186f406742dc805f50ab6a45b313`).
- Laya Core ML: [README](https://github.com/mizorewww/laya-coreml/blob/main/README.md) (`c7d2f92271086147095e863e40104517ac15b4f9`).
