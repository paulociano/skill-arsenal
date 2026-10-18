# Avaliação de 11 repositórios: agentes, modelos, design e pesquisa (2026-10-18)

## Grounding
Fonte canônica: `ARSENAL INDEX.md`, stack `stacks/arsenal-autopilot/STACK.md` e skills canônicas específicas. Fontes externas: metadados e READMEs das branches default de cada repositório, consultados em 2026-10-18. A revisão de segurança foi **estática e inicial**, não exame exaustivo de instaladores/scripts/binários. Nenhum software externo foi executado.

## Classificação, capabilities, owners e implementação

| Fonte | Classe | Decisão | Owner | Commit | Evidência/limite |
|---|---|---|---|---|---|
| [google-research/harness2](https://github.com/google-research/harness2) | A/D | UPDATE_EXISTING | skills/coding-agent-engineering/SKILL.md | [c14818c0](https://github.com/paulociano/skill-arsenal/commit/c14818c068537d7cfacdc175937b4bc98134b3b) | Harness Propose–Probe–Compose; benchmarks requerem Linux e executores com permissões amplas; não instalar. |
| [showheyohtaki/motion-prompt](https://github.com/showheyohtaki/motion-prompt) | B | UPDATE_EXISTING | skills/ui-motion-design/SKILL.md | [265ad422](https://github.com/paulociano/skill-arsenal/commit/265ad42269a94b89bf08c10f591ff626cc0941da) | Vocabulário de movimentos e amostras; skill Node externa não instalada. |
| [mistralai/timestral](https://github.com/mistralai/timestral) | A/D | UPDATE_EXISTING | skills/scenario-forecasting/SKILL.md | [3e636650](https://github.com/paulociano/skill-arsenal/commit/3e63665024fd7e58094604fdd5a22e6b7afe7730) | Backtesting, covariáveis e quantis; requer pesos, PyTorch, licença separada. |
| [reason-machines/reason-network](https://github.com/reason-machines/reason-network) | A/D | UPDATE_EXISTING | skills/multi-agent-orchestration/SKILL.md | [ea8098b6](https://github.com/paulociano/skill-arsenal/commit/ea8098b62a6dc9c1f9075b8e054fc6b2342e4007) | Mensageria, identidade e aprovação; serviço P2P, hooks e instalador remoto não executados. |
| [caveman-ai/trim-1](https://github.com/caveman-ai/trim-1) | B/D | UPDATE_EXISTING | skills/llm-observability-evaluation/SKILL.md | [e49793ab](https://github.com/paulociano/skill-arsenal/commit/e49793abaf2d9dd59418b0094cab784adf594db0) | Compressão de linhas com texto exato; modelo Go e métricas do autor não verificados. |
| [chekusu/yomado](https://github.com/chekusu/yomado) | B/D | UPDATE_EXISTING | skills/computer-use-agent-engineering/SKILL.md | [0b476acd](https://github.com/paulociano/skill-arsenal/commit/0b476acddb0aa9c5c47c70a56b240ef184bba98e) | Display virtual e retorno de janelas; APIs privadas macOS, foco compartilhado; não instalado. |
| [Tencent-Hunyuan/Hy-Memory](https://github.com/Tencent-Hunyuan/Hy-Memory) | A/D | UPDATE_EXISTING | skills/agent-memory-engineering/SKILL.md | [d4daa155](https://github.com/paulociano/skill-arsenal/commit/d4daa155417872ea255cf83557f6f2bf440203c6) | Memória de chat, trabalho e coding, provenance; SDK, model e MemHub externos. |
| [LiCinCan/blender-ai-mcp-addon](https://github.com/LiCinCan/blender-ai-mcp-addon) | A/D | UPDATE_EXISTING | skills/procedural-3d-reconstruction/SKILL.md | [1b75e807](https://github.com/paulociano/skill-arsenal/commit/1b75e80700773f90e187bb6f9386f54de69ba995) | Scene inspection, undo, visual QA e cautela com execução Python arbitrária; Blender e MCP não instalados. |
| [Seokwoooo/lucian-uxui-prompt](https://github.com/Seokwoooo/lucian-uxui-prompt) | B | UPDATE_EXISTING | skills/ui-ux-catalog/SKILL.md | [40fddada](https://github.com/paulociano/skill-arsenal/commit/40fddadade823b72a648ccb2307fbd647e3fb504) | Catálogo de componentes interativos; exemplos não auditados individualmente. |
| [SakanaAI/AI-Scientist-v3](https://github.com/SakanaAI/AI-Scientist-v3) | A/D | UPDATE_EXISTING | skills/academic-paper-orchestration/SKILL.md | [471a75aa](https://github.com/paulociano/skill-arsenal/commit/471a75aafca9c2e4b6d94e9f5c9fc8023f80f81b) | Investigação, ablation, sealed holdout, paper; executor headless com permissões elevadas não instalado. |
| [andunieee/flipflop](https://github.com/andunieee/flipflop) | D | KEEP_EXTERNAL_REFERENCE | — | — | Transferência de arquivos via Iroh, com binário Rust e pareamento; nenhuma nova capacidade de skill; não instalado. |

## Delimitação de segurança e portabilidade

- `Harness²` documenta executor com sandbox desabilitado/rede irrestrita: **CAUTION** para execução; adotado somente processo experimental controlado.
- `AI-Scientist-v3` usa agentes com amplos poderes de execução e credenciais em containers: **CAUTION**; não executar no host nem importar essas permissões.
- `reason-network` instala daemon persistente, hooks e conexões P2P; **CAUTION** para instalação/identidade/mensagens não confiáveis.
- `Hy-Memory` usa armazenamento/memória persistente e possíveis LLM/embedding endpoints externos: **CAUTION** para autorização, privacy e retenção.
- `yomado` usa APIs privadas e compartilha teclado/foco: **CAUTION**; não garante trabalho com monitores desligados.
- `blender-ai-mcp-addon` expõe execute_code e edição de cenas: **CAUTION**; validação declarada de Python não substitui sandbox.
- `Timestral` necessita runtime e pesos de terceiros: verificação de licença/modelo; resultados do autor não devem ser extrapolados.
- `trim-1` faz filtragem que pode eliminar evidências decisivas: original recuperável e gate de recall.
- `motion-prompt` e `Lucian` oferecem galerias e exemplos, não garantias de código seguro e acessível sem testes.
- `flipflop` usa comunicação P2P para arquivos, que exige controle de pareamento e autorização. Mantido como referência, não transformado em skill.

## Incremento demonstrável e restrições

Cada melhoria foi incorporada em owner existente, sem criar novo trigger ou mudar description. Portanto, `ARSENAL INDEX.md` já roteia corretamente e não precisa de alteração. Os itens adicionados incluem limites de execução, necessidade de evidência e guardrails; são **métodos**, não ferramentas instaladas. O ganho em benchmarks e runtime das fontes externas **não foi reproduzido**.

## Estado de publicação

As dez alterações de owners estão documentadas com links de commits acima. A revisão pós-escrita de cada arquivo permanece como verificação necessária; esta avaliação registra os commits e os riscos. Sem alteração de dependências ou credenciais.
