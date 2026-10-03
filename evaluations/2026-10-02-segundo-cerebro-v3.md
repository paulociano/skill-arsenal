# Avaliação: Segundo Cérebro v3

Data: 2026-10-02

## Fonte avaliada

Pacote local enviado pelo usuário: `segundo-cerebro.zip`.

SHA-256 do ZIP: `e473e91650a56efd72c4b3f1d445125f4beb44ecf2e96315654ad5934d508add`.

Arquivos principais inspecionados estaticamente:
- `SKILL.md`
- `INSTALL.md`
- `templates/CLAUDE-template.md`
- `templates/pasta-CLAUDE-template.md`
- `templates/save-SKILL.md`
- `templates/hooks/captura.sh`
- `templates/hooks/painel.sh`
- `templates/hooks/settings.json`
- templates de memória, pessoas, clientes, foco e tarefas

Nenhum installer, hook ou script da fonte foi executado durante a avaliação.

## O que faz de verdade

A skill monta um vault Obsidian operado pelo Claude Code como um sistema de memória pessoal/operacional. O fluxo combina:

1. briefing guiado;
2. definição de uma árvore de pastas adaptada ao perfil;
3. criação de uma constituição global `.claude/CLAUDE.md`;
4. criação de um `CLAUDE.md` por pasta como índice/context map local;
5. hooks de `SessionStart` e `UserPromptSubmit` para injetar painel e regra de captura;
6. captura de pessoas, empresas, clientes, tarefas e fatos em arquivos Markdown;
7. skill `/save` para fechamento da sessão, atualização de tarefas, foco e índices;
8. teste ao vivo de captura e recuperação.

A proposta central é "falar normalmente e materializar fatos no objeto certo", evitando um inbox genérico.

## Classificação

**D — Skill técnica.**

Motivo: o comportamento integral depende explicitamente de Obsidian, Claude Code, convenções `.claude/CLAUDE.md`, hooks de eventos, shell scripts, filesystem local e uma skill `/save`. Sem esse runtime, uma parte relevante do mecanismo de enforcement e carregamento automático não existe.

A metodologia contém elementos úteis, mas não justifica importar esta skill como nova capacidade independente no Arsenal.

## Overlap com o Arsenal

### agent-memory-engineering

Overlap alto. O Arsenal já cobre:
- captura e distilação;
- memória semântica, procedural, episódica e de decisão;
- source of truth legível;
- índices reconstruíveis;
- retrieval progressivo;
- correção, supersession e retenção;
- segurança e privacidade.

Valor incremental aproveitado:
- bootstrap inicial usando o próprio briefing como primeira carga real;
- context maps hierárquicos locais por pasta/domínio, sempre subordinados ao arquivo fonte;
- checkpoint explícito no fechamento de blocos substanciais.

### kb-retriever

Overlap médio. O padrão "ler índice antes de varrer a pasta" é uma especialização prática da recuperação progressiva e da navegação por estrutura já previstas em `kb-retriever`.

Não foi criada uma skill separada para isso.

### ai-workspace-operating-cycle

Overlap alto. O Arsenal já trata workspace persistente, record canônico, capture, focus, materialize, persist e resume. A implementação do Segundo Cérebro é uma concretização opinionada em filesystem/Obsidian/Claude Code.

### meeting-knowledge-capture e session-learn

Há sobreposição parcial na materialização de reuniões e no fechamento/aprendizado por sessão. O `/save` agrega essas ideias, mas não cria uma capacidade nova suficiente para justificar owner próprio.

## Pontos fortes

- O briefing já produz dados reais e evita um sistema vazio no primeiro uso.
- A regra "pasta só nasce se tiver uso" reduz taxonomia decorativa.
- O índice local por pasta é uma boa técnica para limitar leitura e custo em árvores grandes.
- O princípio "índice é mapa, arquivo é verdade" é correto e portátil.
- O fechamento de sessão procura lacunas sem depender apenas da memória do agente.
- O código dos dois hooks é curto, legível e sem rede própria.

## Limitações metodológicas

1. **Captura excessivamente ampla.** A regra "todo fato novo deve ser gravado" conflita com governança de memória. Nem todo fato merece retenção permanente.
2. **Sem contrato explícito de sensibilidade/retention.** Há categorias pessoais, financeiras e de saúde possíveis, mas a skill não define política robusta de retenção, escopo ou exclusão.
3. **"Nunca deletar" é forte demais.** Arquivar para sempre entra em conflito com minimização, correção, pedidos de remoção e dados que devem expirar.
4. **Índices manuais podem gerar drift.** O `/save` mitiga, mas não prova consistência.
5. **Uma pergunta por mensagem** é adequada para uma mentoria específica, não como regra universal de operação.
6. **Acoplamento de marca/pessoa.** O material contém referências ao "Felipe", ao "vault do Felipe" e a uma arquitetura proprietária de mentoria. Isso não pertence ao núcleo portátil do Arsenal.
7. **Naming e estrutura muito opinionados.** Pastas como `pessoas/`, `clientes/`, `negocio/` e a proibição absoluta de inbox funcionam para alguns contextos, mas não são universais.

## Revisão de segurança

**Verdict: CAUTION.**

### Findings

- `INSTALL.md` recomenda `curl -fsSL https://claude.ai/install.sh | bash`. A avaliação não executou esse comando. Curl-pipe-shell aumenta risco de supply chain e deve ser substituído por instalação oficial verificada/pinada quando a skill for portada.
- Os hooks persistem dentro de `.claude/settings.json` e executam shell em eventos do host. O propósito é coerente e os scripts avaliados são locais e simples, mas continuam sendo persistência/execução automática.
- Não foram encontrados comandos destrutivos, privilege escalation, exfiltração, raw IPs, credenciais embutidas ou envio de dados à rede nos hooks inspecionados.
- O principal risco é de **dados**, não de malware: captura automática pode gravar informação sensível sem filtro suficiente.
- A regra "nunca deletar" aumenta blast radius e é incompatível com uma política saudável de memória quando houver dados que precisem expirar ou ser removidos.

### Adaptação segura

Ao reutilizar os padrões:
- tratar captura automática como opt-in por escopo;
- excluir segredos, autenticação e dados sensíveis sem finalidade clara;
- definir retention e deletion/supersession;
- manter mapas/índices como cache, nunca como fonte autoritativa;
- usar apenas hooks ou automações que o runtime realmente oferece;
- não transportar comandos `curl | bash` para o Arsenal.

## Decisão

**Não importar `segundo-cerebro` como skill nova.**

O valor incremental foi absorvido em `agent-memory-engineering`:
- bootstrap pelo briefing;
- mapas hierárquicos locais para retrieval;
- checkpoint de sessão;
- restrição explícita contra transformar toda mensagem em memória permanente.

Não houve necessidade de alterar `ARSENAL INDEX.md`, pois nenhuma nova skill/stack foi criada e a descrição canônica de `agent-memory-engineering` continua válida.

## Mudanças aplicadas

- Atualizada `skills/agent-memory-engineering/SKILL.md` com os padrões portáveis acima.
- Nenhum script, template de Claude Code ou estrutura Obsidian foi importado.

## Limites da validação

- A avaliação foi estática e local.
- Não foi executado Claude Code, Obsidian, hooks, installer ou `/save`.
- Não foi validada a alegação de que `CLAUDE.md` por pasta "carrega sozinho" em todas as versões/ambientes.
- Não foi feita avaliação empírica de custo ou qualidade de retrieval contra baseline.

## Resultado

Boa implementação específica de um "segundo cérebro" em Claude Code + Obsidian, com padrões úteis de arquitetura de memória. Como candidata ao Arsenal, o melhor tratamento é **adaptar o método dentro do owner existente**, não duplicar a capacidade.
