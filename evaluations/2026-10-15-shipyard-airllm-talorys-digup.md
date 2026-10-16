# Avaliação consolidada: Shipyard, AirLLM, Talorys e DigUp

Data: 2026-10-15. Fonte oficial do Arsenal: https://github.com/paulociano/skill-arsenal; índice lido antes da seleção. Fontes externas consultadas em seus repositórios originais, incluindo README e documentação complementar indicada abaixo.

## 1. Shipyard
Fonte: https://github.com/cosscom/shipyard (main); docs/concepts/security.mdx e docs/guides/offline-queue.mdx.

- **Faz:** orquestra agents/terminais/worktrees em máquinas remotas, com pareamento e filas duráveis.
- **Quando usar:** engenharia de sistemas de agentes remotos, especialmente desconexão, segurança da configuração do repo e revisões humanas.
- **Classe:** B/D. Há método portátil valioso, mas produto exige daemon, cliente, rede e autenticação locais.
- **Risco:** instalação por shell, configuração de repo/plugins executáveis e poderes do usuário remoto; não instalar.
- **Decisão:** UPDATE_EXISTING em skills/agent-action-governance/SKILL.md. Separação entre indisponibilidade antes de envio e falha depois de possível envio; idempotência, não repetição cega e trust de config por versão/hash.
- **Commit:** 8b1e0c26e5f5df851632cf26f9a31400c4ff7d68.

## 2. AirLLM
Fonte: https://github.com/lyogavin/airllm (main); README.md.

- **Faz:** streaming de camadas/experts de modelos LLM para inferência em VRAM pequena; documentação recente também descreve fine-tuning de base congelada com adapters.
- **Quando usar:** comparação de métodos de inferência/treinamento sob orçamento de memória.
- **Classe:** B/D. Implementação requer Python, modelos, hardware, drivers, armazenamento e versões compatíveis.
- **Risco:** benchmarks divulgados não foram reproduzidos; baixa VRAM não implica baixa latência ou pouco disco; opções de remoção de checkpoints devem ser revistas antes de qualquer teste.
- **Decisão:** UPDATE_EXISTING em skills/local-llm-inference-engineering/SKILL.md; acrescentar custo completo de I/O, armazenamento/checkpoints e treino com adapters, mantendo comparações com mesma qualidade.
- **Commit:** 7264a1791b927214e01b01ee40b09da01e1e0248.

## 3. Talorys
Fonte: https://github.com/rociiu/talorys (main); README.md, docs/memory-history.md e docs/security.md.

- **Faz:** assistente pessoal de instância única hospedado na conta Cloudflare, com memória, tarefas, rotinas e backup.
- **Quando usar:** design de memória temporal, segurança em restaurações e agentes persistentes.
- **Classe:** B/D. Requer Cloudflare Workers/Pages/Durable Objects, runtime e credenciais.
- **Risco:** importações podem introduzir instruções, rotinas ou estado indevido; cobranças e limites reais do provedor não são comprovados por estimativas locais.
- **Decisão:** UPDATE_EXISTING em stacks/ai-workspace-operating-cycle/STACK.md. Revisão de conflitos, vigência temporal, automações importadas desativadas e preservação de limites de segurança.
- **Commit:** ad049588896eaee32c64b8169fe9a8842c0b4f9f.

## 4. DigUp
Fonte: https://github.com/ARahim3/DigUp (main); README.md.

- **Faz:** busca semântica local multimodal em arquivos, com mistura de embeddings e pesquisa literal e localizadores por página, instante e linha.
- **Quando usar:** recuperação em corpus heterogêneo, principalmente quando buscas literais e semânticas são complementares.
- **Classe:** B/D. Modelo local, indexação e app específicos não estão disponíveis automaticamente.
- **Risco:** indexar caminhos privados, chaves ou outros arquivos excluídos; deriva de embeddings após atualização do modelo; resultados semânticos não devem virar prova sem localizador.
- **Decisão:** UPDATE_EXISTING em skills/kb-retriever/SKILL.md com busca híbrida, localizadores tipados, índice versionado, scope opt-in de código e regressão de ranking.
- **Commit:** bd82ec48cf18cac8a27c341e22e6cfd0f79648d6.

## Decisão agregada

Quatro fontes **B/D**, quatro melhorias incorporadas a owners existentes, nenhuma nova skill ou stack. Nenhum instalador ou código terceiro foi executado, nem foram feitos testes reais das aplicações ou de suas alegações de performance. Limite: revisão de documentação pública original, não auditoria completa de código de produção. Os arquivos alterados foram relidos após commit e o índice permaneceu sem alterações de rota.
