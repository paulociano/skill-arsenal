# Avaliação de sete fontes externas — 2026-10-17

## Escopo e método
Fontes consultadas na branch padrão dos repositórios abaixo; triagem de README e, quando pertinente, SKILL.md, em comparação com o `ARSENAL INDEX.md` e a stack `arsenal-autopilot`. Revisão estática seletiva: não foram executados installers, scripts, testes, Cloudflare Containers, MCP servers ou apps. Portanto, segurança e alegações de desempenho permanecem limitadas ao material inspecionado.

| Fonte | Classe | Capacidade identificada | Decisão | Owner/limites |
|---|---|---|---|---|
| [ResiMind](https://github.com/1105216375-alt/resimind) | A/D | Admission independente de regras, reparo residual, rechecagem e memória verificável | **UPDATE_EXISTING** | `skills/agent-memory-engineering/SKILL.md`; não importar MCP/Lean; domínio formal do projeto é experimental e estreito |
| [Desigma](https://github.com/deepfounder-ai/desigma) | D | Editor nativo Rust, arquivo Figma, variantes, auto layout, prototype, Dev Mode e decks | **KEEP_EXTERNAL_REFERENCE** | Aplicativo desktop, não metodologia nova superior a `design-system-extraction`/`design-system-governance`; alfa; requer runtime próprio |
| [Armada](https://github.com/AshishKumar4/armada) | D | Execução map paralela em Cloudflare Containers, snapshots, fila dinâmica e retry | **KEEP_EXTERNAL_REFERENCE** | Infraestrutura, não disponível automaticamente; Cloudflare pago, Worker, R2, secrets; padrões já cobertos por `durable-workflow-engineering` |
| [Machine Skill](https://github.com/AirsupHQ/machine-skill) | A/D | Simulação mecânica explicativa com escala, partes, solver, leitura e corte | **CREATE_NEW** (consolidado) | `skills/evidence-driven-interactive-explainers/SKILL.md`; kits Three.js/captura não são portáveis por pressuposição |
| [Anima](https://github.com/Garinmckayl/anima) | A/D | Anatomia fiel, fontes por valor, graus de evidência, modelo único e acessibilidade | **CREATE_NEW** (consolidado) | Mesmo owner da Machine; sem importar ferramentas Claude/Node, validação biológica externa requerida |
| [Gloss](https://github.com/Nutlope/gloss) | D/B | Leitura contextual de artigos/PDF com seleção de trecho e resposta marginal citada | **KEEP_EXTERNAL_REFERENCE** | Produto Next.js + Together AI, Exa, Clerk, Neon; padrão já atendido em leitura com ancoragem de fontes, sem integração nesta avaliação |
| [GPT with Taste](https://github.com/NB-Corp/gpt-with-taste) | C/B | Julgamento, execução sem cerimônia, síntese e craft por instruções e hooks | **KEEP_EXTERNAL_REFERENCE** | Sobreposição com `design-direction`, `writing-quality`, `verify-before-claim` e governança do host; hooks Codex/Claude não disponíveis por padrão |

## Ganho incremental e ownership
1. **Novo owner:** `evidence-driven-interactive-explainers` combina estrutura fiel e modelo causal computável de máquinas com proveniência, separação de evidência e acessibilidade para biologia. Contrato transversal ausente no índice e mais específico que visual explanation ou web-design.
2. **Owner atualizado:** `agent-memory-engineering` agora explicita gate para admissão de regra verificada, contraexemplos, reuso revalidado e avaliação contra baseline.
3. As demais fontes permanecem referências, sem instalar produtos ou replicar princípios genéricos em novas skills.

## Segurança e portabilidade
- **CAUTION:** ResiMind utiliza executáveis/verificadores e servidor MCP opcional. O método foi incorporado sem executar os componentes ou confiar na exatidão de claims do README.
- **CAUTION:** Machine Skill e Anima utilizam scripts de construção/captura, biblioteca própria e dependências do host; apenas metodologia foi portada, não código.
- **CAUTION:** Armada documenta installer remoto `curl | sh` e execução de tarefas em contêineres com credenciais Cloudflare; não executar sem auditoria própria do deploy, isolamento e custos.
- **CAUTION:** Gloss depende de múltiplas credenciais externas e persistência de documentos; avaliar fluxo de privacidade antes de uso com informação sensível.
- **CAUTION:** GPT with Taste modifica prompts e hooks do agente, incluindo comportamento persistente; não instalar em um ambiente que não tenha esse contrato.
- **CAUTION:** Desigma é software desktop alfa, com importação/exportação; não confundir documentação e screenshots com prova de maturidade ou testes locais.

## Testes de aceite
- **Should-trigger do novo owner:** HTML interativo demonstrando mecanismo de motor ou receptor, com entrada que altera modelo e leitura derivada.
- **Near-miss:** pôster estático de motor ou diagrama de processo sem dinâmica quantitativa.
- **Memória:** regra proposta rejeitada pelo checker não deve ser admitida; reuso exige nova verificação, com condições do domínio.
- **Limitação:** não foram construídos artefatos de exemplo nem executados testes de runtime dos projetos externos.

## Publicação
Arquivos alterados:
- `skills/evidence-driven-interactive-explainers/SKILL.md`
- `skills/agent-memory-engineering/SKILL.md`
- `ARSENAL INDEX.md`
- `evaluations/2026-10-17-seven-external-repositories.md`

Commits de implementação:
- `963cef008a7af1535499d19d7eed8bb4cd33d63b`
- `fc27ab25a1db42a0aaa345cefefed822587938f3`
- `2bc7316601d28444d5a9dbde31b3a222ecd8fa06`

Registro de avaliação criado por commit próprio. A avaliação é de metodologia/portabilidade; não certificação de segurança dos repositórios.
