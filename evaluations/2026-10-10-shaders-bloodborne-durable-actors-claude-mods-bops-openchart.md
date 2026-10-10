# Avaliação em lote: seis repositórios (2026-10-10)

Fonte canônica: `ARSENAL INDEX.md` em https://github.com/paulociano/skill-arsenal. Stack: `arsenal-autopilot`. Seis URLs únicas (OpenChart repetido na solicitação).

## Matriz de capacidades, classificação e decisão

| Origem | Classe | Decisão | Owner |
|---|---|---|---|
| [shader-effects-inc/shaders](https://github.com/shader-effects-inc/shaders) | A/D | UPDATE_EXISTING: componentes GPU declarativos, ordem de camadas e fallback; manter biblioteca/CLI/MCP como opção externa | `shader-graphics-engineering` |
| [deadinside28/bloodborne_pc](https://github.com/deadinside28/bloodborne_pc) | D | KEEP_EXTERNAL_REFERENCE: portabilidade experimental de um título proprietário, tradução PS4/Vulkan, upscaling, sincronização e benchmarking. Especialidade estreita e sem uso automático justificável | `game-performance-engineering` / `shader-graphics-engineering` |
| [TerseAI/durable-actors](https://github.com/TerseAI/durable-actors) | A/D | UPDATE_EXISTING: ator persistente por chave, serialização/interleaving de mensagens, segurança de effects e recovery | `durable-workflow-engineering` |
| [hamzafer/claude-code-mods](https://github.com/hamzafer/claude-code-mods) | B/D | KEEP_EXTERNAL_REFERENCE: status de contexto, review-watch, blast-radius e observabilidade de subagentes são específicos de hooks do Claude Code; os padrões de preflight e audit já existem | `agent-action-governance`, `codex-cost-efficiency`, `coding-agent-engineering` |
| [OrgoAI/bops](https://github.com/OrgoAI/bops) | A/D | UPDATE_EXISTING: limite de autoridade por agente, autorização em canais, integração, computador, tomada de controle e revogação | `agent-action-governance` |
| [longsurf-ai/openchart](https://github.com/longsurf-ai/openchart) | A/D | KEEP_EXTERNAL_REFERENCE: workspace de mercado, gráficos, indicadores Tea, monitores, alertas e pesquisa agentic; sem recomendar automação de negociação ou executar linguagem/script não auditado | `financial-analysis-cycle`, `ai-workflow-automation-engineering`, `dashboard-design` |

## Critérios e segurança

Pesquisa documental baseada nos README e metadados atuais de cada repositório e no skill original do Shaders, confrontados com owners selecionados do Arsenal. Não houve execução dinâmica, instalação, compilação, nem teste de códigos, downloads ou serviços de terceiros. Esses limites impedem atestar alegações de desempenho, segurança e estabilidade dos produtos.

- Shaders: biblioteca MIT WebGPU; validar suporte browser/dispositivos, SSR e fallback, efeitos reduzidos e licenças de presets antes do consumo.
- Bloodborne PC: README informa port experimental Linux com dump próprio do jogo, sem arquivos proprietários incluídos, e testes limitados. Não incorporar arquivos do jogo, patches proprietários nem resultados autorreportados como benchmarks universais. Repositório GPL-2.0, diferentemente da maior parte das skills.
- Durable Actors: SDK/runtime MIT com estado e chamadas serializadas; validar transações, reentrância, concorrência e efeito externo, sem assumir exactly-once.
- Claude Code Mods: marketplace de plugins/hooks que podem inspecionar prompts, operações, métricas e comandos; evitar executar scripts e injetar hooks sem análise de privilégio, privacidade e supply chain. Não converter recursos de Claude Code em alegações de capacidade ChatGPT.
- Bops: licença FSL-1.1-ALv2 com restrições de serviço concorrente; integrações e computadores podem acessar dados e agir externamente. Usar apenas princípios de governança, não copiar produto nem chamar recursos inexistentes.
- OpenChart: dados de mercado e estratégia automatizada exigem provenance, qualidade temporal, permissões de negociação, sandbox de script e revisão humana. A aplicação não substitui validação de orientação financeira nem plataforma de execução autorizada. Licença a verificar no arquivo para qualquer reutilização.
- Nenhuma credencial, instalador, binário, VM, hook, middleware, biblioteca de terceiros ou serviço externo foi habilitado.

## Incremento demonstrado

1. Shader web declarativo, fallback e semântica de camadas entrou em `skills/shader-graphics-engineering/SKILL.md`.
2. Modelo durable actor entrou em `skills/durable-workflow-engineering/SKILL.md`.
3. Delegação entre bots e handover humano entrou em `skills/agent-action-governance/SKILL.md`.
4. Outros três produtos permanecem referências, não skills copiadas.

Teste de ativação: frontend solicitando efeitos GPU, app colaborativo com estado por entidade, ou bot executando tarefas com contas e computador externo. Near-miss: CSS estático sem GPU; script sequencial sem concorrência; texto informativo sem ações em serviços. Critérios: nenhuma ferramenta presumida, estados/falhas testáveis, least privilege, preservação de UX e integração proporcional ao escopo.

Sem novas skills/stacks ou alteração material de description; `ARSENAL INDEX.md` permanece válido. Mudanças restritas a documentos de skills e avaliação.
