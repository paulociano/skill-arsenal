# Avaliação do ecossistema ruvnet — 2026-10-24

## Escopo e método
Fontes originais: READMEs públicos de ruvnet/ruflo, ruvnet/RuVector, ruvnet/RuView, ruvnet/metaharness, ruvnet/rvm e README de crates/rvf no RuVector, que aponta para @ruvector/rvf. Comparação com ARSENAL INDEX.md e stack arsenal-autopilot. Revisão documental estática; **não** houve instalação, execução, scanner de segurança, reprodução de benchmark nem validação funcional do software externo.

## Capability ledger e decisões

| Fonte | Classe | Capacidade | Owner e decisão | Limitação |
| --- | --- | --- | --- | --- |
| [Ruflo](https://github.com/ruvnet/ruflo) | D/B | Coordenação, plano de controle, estados e recuperação de tarefas | UPDATE_EXISTING: skills/multi-agent-orchestration/SKILL.md | MCP/CLI/hooks/swarms não disponíveis automaticamente |
| [RuVector](https://github.com/ruvnet/RuVector) | D/B | Memória persistente, híbrida, grafos, feedback e avaliação | UPDATE_EXISTING: skills/agent-memory-engineering/SKILL.md | requer backend, embeddings, medições locais |
| [RuView](https://github.com/ruvnet/RuView) | D | Sensoriamento de presença, movimento e sinais Wi-Fi/IoT | KEEP_EXTERNAL_REFERENCE | hardware, ambiente físico, calibração e consentimento; não é capacidade geral de agentes |
| [MetaHarness](https://github.com/ruvnet/metaharness) | A/D | Experimentos contrastivos, evidência, rollback, governança de harness | UPDATE_EXISTING: skills/llm-observability-evaluation/SKILL.md | geração/execução de harness e Darwin/AVO são externos |
| [RVF npm](https://www.npmjs.com/package/@ruvector/rvf) e [README](https://github.com/ruvnet/RuVector/tree/main/crates/rvf) | D/B | Formato portátil para vetores/estado e integridade | ABSORB_METHOD_ONLY: owner agent-memory-engineering; implementação realizada | compatibilidade binária, assinatura e portabilidade requerem testes de runtime |
| [RVM](https://github.com/ruvnet/rvm) | D | Isolamento por capacidades, testemunhos, checkpoints e recuperação | KEEP_EXTERNAL_REFERENCE | runtime bare-metal/Rust não disponível neste ChatGPT |

## Ganho incremental incorporado
- Memória: decisão por benchmark comparando lexical/híbrido, ACL, reconstrução, tombstones, correções e testes de export/restauração.
- Orquestração: leases, reconciliação antes de retry, rastreabilidade de ownership e conclusão verificada.
- Avaliação: congelamento de baseline e holdout, proposta motivada por falha, experimentos pareados, bloqueio de autovalidação e rollback.

## Segurança e portabilidade
Status **CAUTION para instalação/execução de todos os runtimes**: ampla superfície de dependências, rede, processos, credenciais, código próprio, hooks e possíveis mutações. Somente princípios textuais independentes foram importados; nenhum código ou instalador externo foi executado. Requer pinning de commit/release, revisão de manifests e transitive dependencies, isolamento de secrets, ensaios de permissões, integridade, custos e regressões antes de implementar runtime. Badges e claims de desempenho dos READMEs não constituem comprovação independente.

## Prova mínima de utilidade
Should trigger: projeto com memória vetorial sujeita a correções, swarm real com worker timeout, ou harness com mudanças autônomas. Near-miss: resposta casual sem estado, agentes fictícios apenas como papéis editoriais, ou aplicativo sem ferramenta real de delegação. Aceite futuro: suíte reproduzível de recall/ACL/restore; fault injection com idempotência; avaliação pareada com holdout.

## Publicação
Arquivos de owners atualizados:
- skills/agent-memory-engineering/SKILL.md
- skills/multi-agent-orchestration/SKILL.md
- skills/llm-observability-evaluation/SKILL.md

Nenhuma skill nova, stack nova ou alteração de roteamento foi necessária; portanto ARSENAL INDEX.md permanece inalterado. Esta avaliação registra evidência documental e decisões, não certificação de segurança/benchmarks externos.
