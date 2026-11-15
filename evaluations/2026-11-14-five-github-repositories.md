# Avaliação: cinco repositórios externos (2026-11-14)

## Fonte oficial e execução

Consultados `ARSENAL INDEX.md` (master), `stacks/arsenal-autopilot/STACK.md`, os owners canônicos relevantes e os READMEs atuais dos cinco projetos. Aprofundados `SKILL.md` de ztd-charts, ste80-humanizer e cinematic-film; documentação do WebsiteBench e arquitetura do Persona. Referência: branches `main` dos projetos externos no dia da avaliação. Nenhuma instalação, script remoto, dataset, pacote npm/pip, container ou engine externa foi executado. **Veredito de segurança limitado à leitura estática; não equivale a auditoria exaustiva de código.**

## Classificação, overlap, decisão

| Projeto | Capacidades observadas | Classe | Decisão/owner | Portabilidade, riscos e dependências |
| --- | --- | --- | --- | --- |
| [Junhan2/ztd-charts](https://github.com/Junhan2/ztd-charts) | Biblioteca React de 44 gráficos SVG, cartão com takeaway, interação, acessibilidade, JSON schema, CLI e MCP | A/D | **UPDATE_EXISTING** em `skills/dashboard-design/SKILL.md`: pergunta → visual → validação → preview, destaque seletivo, acessibilidade e takeaway factual | React, npm, CLI, MCP e compatibilidade de schema são externos; não presumir instalação. Payload com URLs e dados reais exige validação; schema específico não é universal. |
| [TIGER-AI-Lab/WebsiteBench](https://github.com/TIGER-AI-Lab/WebsiteBench) | Benchmark de reconstrução full-stack de sites com exploração em browser, checks funcionais e visual checkpoints; README indica 70 sites, 46.916 casos e SSIM normalizado 0,99 para passar checkpoint | B/D | **UPDATE_EXISTING** em `skills/runtime-ui-verification/SKILL.md`: exigir **funcional e visual**, casos com condições reproduzíveis e UNKNOWN | Docker/Harbor, dataset e páginas de terceiros. Conteúdo de referência é descrito para pesquisa não comercial; não importar sites/ativos nem adotar threshold como padrão universal. Sem benchmark executado. |
| [Dodaios/ste80-humanizer](https://github.com/Dodaios/ste80-humanizer) | Revisão em duas passagens: resíduos de escrita artificial, depois clareza estrutural inspirada em STE80, preservação factual, modos light/strict | B | **UPDATE_EXISTING** em `skills/writing-quality/SKILL.md`: modo de revisão contextual em duas passagens com inventário de fatos | Não usar como detector de IA nem promessa de autoria humana; cuidado com perda de qualificador, voz, estilo e requisito técnico. Nenhum linter externo necessário. `plain-writing` já cobre linguagem controlada, por isso sem nova skill. |
| [Moh4696/cinematic-skill](https://github.com/Moh4696/cinematic-skill) | Pipeline de filmes narrados por código com câmera sobre cena contínua, sync por palavra, mapa de beats, voz retimável, arquivos licenciados e verificação de stills/contact sheets | A/D | **UPDATE_EXISTING** em `skills/procedural-film/SKILL.md`: sync lexical, fact/rights ledger, geografia de cena e gates | Skia/Python, ffmpeg, TTS, fontes, downloads e `install.sh` não estão presumidos disponíveis. Nunca `curl | bash` na avaliação. Timings requerem áudio e ferramentas reais. |
| [nwverse/persona](https://github.com/nwverse/persona) | Produto superagent multiplataforma com hub, nós SSH, runtime bridge, approvals em telefone, extensão, inbox, conhecimento e dados pessoais de dispositivos | D | **KEEP_EXTERNAL_REFERENCE**; owners `multi-agent-orchestration` e `agent-action-governance` já cobrem delegação, sessões, approval e identity boundaries | Hub sempre ligado, acesso SSH, tokens de dispositivos, sincronização, push, dados pessoais/saúde/localização, plugins externos; grande superfície de ataque. Não instalar nem tratar como conector ChatGPT. Ganho metodológico incremental insuficiente para outra skill. |

## Prova incremental e gatilhos

1. **ztd:** should-trigger dashboard com gráficos de dados reais e interpretação. Near-miss tabela de tarefas simples. Ganho: contrato verificável de question/encoding/takeaway/acessibilidade além de mera escolha visual. Evidência desejada: preview e reconciliação de métricas.
2. **WebsiteBench:** should-trigger reconstrução visual e funcional autorizada. Near-miss auditoria de performance isolada. Ganho: par de oráculos de render e postcondition com casos reproduzíveis. Evidência: matriz funcional/visual com runtime real; não reproduzidos testes ou SSIM do benchmark.
3. **STE80:** should-trigger revisão de texto robótico sem alterar fatos. Near-miss pedido de escrita literária em voz expressiva. Ganho: duas passagens com fidelity gate, não lista prescritiva de palavras proibidas. Evidência: diff sem perda de escopo/certeza.
4. **Cinematic:** should-trigger filme documental narrado com highlights sincronizados a palavras. Near-miss edição de video existente. Ganho: timing lexical e câmera/spotlight geograficamente coerentes. Evidência: cue sheet de voz real e checagem audiovisual.
5. **Persona:** should-trigger apenas como produto específico caso o usuário venha a querer instalar/avaliar sistema autohospedado. Near-miss planejamento genérico de agentes, já coberto pelos owners existentes. Sem mudança neste lote.

## Segurança e verificação

**CAUTION / static_only** para as quatro absorções metodológicas. Não foi feita inspeção de todas as dependências e scripts da origem nem scanner de malware. Toda eventual adoção de runtimes requer revisão de instalação e controle de rede/credenciais/privacidade; Voice/VM e dados de dispositivos exigem autorização e least privilege. Sem execução, desempenho do README é alegação da origem, não resultado validado.

Arquivos modificados na branch canônica `master`:
- `skills/dashboard-design/SKILL.md`;
- `skills/runtime-ui-verification/SKILL.md`;
- `skills/writing-quality/SKILL.md`;
- `skills/procedural-film/SKILL.md`;
- `evaluations/2026-11-14-five-github-repositories.md` (este registro).

Nenhuma nova skill ou stack criada, portanto o `ARSENAL INDEX.md` mantém as rotas existentes. Releitura pós-publicação obrigatória antes de alegar conclusão. O registro classifica todas as cinco fontes, inclusive a não adotada.
