# Avaliacao de lote: OpenMAIC, OpenClaude, MiniMind

Data: 2026-10-18
Metodo: stacks/arsenal-autopilot/STACK.md, com triagem de seguranca proporcional e comparacao pelo ARSENAL INDEX.md.
Fonte canônica: repositorios nas branches padrao, READMEs consultados por GitHub. Auditoria estatica focada em documentacao, nao auditoria integral de codigo ou instalacao.

## OpenMAIC
Fonte: https://github.com/THU-MAIC/OpenMAIC (main)
Categoria: A/D. Plataforma educativa multiagente com salas interativas, professores e colegas de IA, quiz, slides, simulacoes, projetos, quadro e voz. Versao 1.2.0 descrita em 2026-10-16 usa geracao server-first, PostgreSQL e servidor persistente; exportacao PPTX/HTML e configuracao de provedores por slots.
Novidade: contratos pedagogicos por papel, feedback formativo e checkpoint com progressao. A infraestrutura de geracao multimodal e runtime externo, nao skill nativa ChatGPT.
Decisao: UPDATE_EXISTING em skills/multi-agent-orchestration/SKILL.md. Sem instalar servidor, banco ou agent workbench. Manter plataforma como referencia externa.
Riscos: rede, API keys, materiais de alunos, armazenamento e cadeia de dependencias; README documenta historico de correcao de vulnerabilidades SSRF. Status: CAUTION para adocao do runtime, metodologia segura com limites descritos.

## OpenClaude
Fonte: https://github.com/Twigpine/openclaude (main)
Categoria: D com metodologia B. CLI de coding agent para diversos provedores com tools, agentes, MCP, sessoes, comandos e processos em background. Depende de Node.js, instalacao de pacote, credenciais e CLI. README especifica que fork de conversa nao isola arquivos/worktrees e que processos longos podem terminar stale.
Novidade: estados de processos desacoplados de sucesso, fronteiras entre fork/sessao e isolamento real, configuracao explicita de provedores.
Decisao: UPDATE_EXISTING em skills/coding-agent-engineering/SKILL.md. Nao importar a CLI, credenciais, shell nem processos background como capacidades atuais.
Riscos: shell, edicao de repos, credenciais, MCP, persistencia e instalacao npm; status CAUTION para runtime, metodologia portavel.

## MiniMind
Fonte: https://github.com/jingyaogong/minimind (master)
Categoria: D com metodologia B. Projeto PyTorch para treino de LLM pequeno (modelo principal de 64M parametros), dados de pretreino, SFT, preferencias/RLAIF, agent RL, avaliacao e checkpoints. Tem dataset e requisitos de GPU externos.
Novidade: fluxo didatico reproducivel de treinamento do zero, com dados e checagens entre fases.
Decisao: UPDATE_EXISTING em skills/local-llm-inference-engineering/SKILL.md somente para fronteira metodologica de treino e inferencia, sem transformar este owner em runtime de treinamento. Manter codigo/datasets como referencia externa.
Riscos: direitos dos datasets, dependencia GPU/PyTorch e ausencia de reproducao dos benchmarks; status CAUTION para executar, metodologia portavel.

## Resultado
Tres owners existentes atualizados, sem criacao de skill redundante. Indice: descricoes e rotas existentes permanecem adequadas; nenhuma mudanca necessaria.
Arquivos modificados:
- skills/multi-agent-orchestration/SKILL.md
- skills/coding-agent-engineering/SKILL.md
- skills/local-llm-inference-engineering/SKILL.md
- evaluations/2026-10-18-openmaic-openclaude-minimind.md

Limites: revisao documental e de arquitetura de alto nivel, sem executar fontes, instalar dependencias, realizar testes de integracao, validar benchmarks publicados ou concluir seguranca integral do codigo.