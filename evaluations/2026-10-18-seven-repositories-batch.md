# Avaliação em lote: 7 repositórios (2026-10-18)

Método: `stacks/arsenal-autopilot/STACK.md`; fonte oficial `ARSENAL INDEX.md`. Revisão documental de metadados, READMEs e owners específicos; nenhum instalador, daemon, proxy, hook ou código externo foi executado. Classificação D significa dependência técnica, não reprovação automática. A/B indicam metodologia incremental absorvida, não certificação do produto.

| Fonte | Capability observada | Classificação | Decisão | Owner |
|---|---|---|---|---|
| [chekusu/yobiru](https://github.com/chekusu/yobiru) | Mensagens, anexos e wake-up entre agentes sobre Tailscale com identidade, ACL, timeout e recibos | D | KEEP_EXTERNAL_REFERENCE | `graph-engineering` e `agent-action-governance` já cobrem contratos/controle conceitual; implementação exige Tailscale, listener, CLI e agentes acessíveis |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Respostas concisas, filtro de outputs, roteamento de modelos, blocos executáveis e proxy | B/D | UPDATE_EXISTING: reduzir ruído de tool outputs com fidelidade e teste | `skills/coding-agent-engineering/SKILL.md` |
| [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | Compressão hierárquica incremental reversível; search/decompress; proxy de API e métodos MITM | B/D | UPDATE_EXISTING: checkpoints restauráveis, medição de cache e proibição de MITM implícito | `skills/coding-agent-engineering/SKILL.md` |
| [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | Plataforma self-hosted multiuser/multiagent, ACP bidirecional, canais e controle persistente | D | KEEP_EXTERNAL_REFERENCE; forte dependência de runtime, dados, credenciais e infraestrutura | `graph-engineering`, `agent-memory-engineering` e `ai-workflow-automation-engineering` já abordam método |
| [chenglou/handwired](https://github.com/chenglou/handwired) | Conversão experimental de lógica JavaScript para operações tensor/ReLU diferenciáveis | D | KEEP_EXTERNAL_REFERENCE para casos de compilação/ML; não é skill operacional genérica; requer Bun/WebGPU para reproduzir exemplos | sem owner novo |
| [tamagui/tamagui](https://github.com/tamagui/tamagui) | Componentes e estilo universal React/React Native com compilador otimizador | B/D | UPDATE_EXISTING: critérios de seleção, sem importação de framework | `skills/crossplatform-mobile-engineering/SKILL.md` |
| [Graphicle-AI/graphicle](https://github.com/Graphicle-AI/graphicle) | Grafo de código + memória vinculada a símbolos, trechos citáveis e invalidação localizada | B/D | UPDATE_EXISTING: memória com símbolo/versionamento e invalidação proporcional | `skills/agent-memory-engineering/SKILL.md` |

## Ledger incremental e evidência de ganho

- **Memory anchored to code** (Graphicle): comportamento novo e portátil: marcar memórias de funções alteradas como potencialmente obsoletas sem invalidar memórias não relacionadas. Should-trigger: agente explicando decisão antiga de função modificada. Near-miss: nota pessoal sem ligação com código. Gate: mudança de símbolo dispara revalidação e cita código atual.
- **Loss-bounded context economy** (Caveman e billion-context): filtrar logs/tool outputs, preservar diagnósticos e capacidade de expansão, snapshots hierárquicos reversíveis; custo e acurácia devem ser mensurados. Should-trigger: longa sessão de coding com outputs volumosos. Near-miss: alterar payload técnico literal. Gate: resposta com evidência e checks equivalentes ao baseline, custo medido.
- **Universal UI selection** (Tamagui): critério condicional para projetos web/native e verificação de otimização real. Should-trigger: projeto React Native + web avaliando compartilhamento de tokens/componentes. Near-miss: web app sem mobile. Gate: teste de build, acessibilidade e runtime por plataforma.

## Segurança e portabilidade

Veredito de triagem: CAUTION para os sete como **runtimes**, sem certificação de segurança. Yobiru envolve rede privada, listeners, anexos temporários e wake de agente; configurar ACL, identidade real e allowlist. Caveman mexe em instalação, ferramentas e possivelmente tráfego/model choice; revisar diffs, credenciais e integridade de logs antes de habilitar. billion-context intercepta tráfego de modelos e em alguns modos usa certificados/MITM; não inserir proxy sem threat model, revisão de credenciais e consentimento. Octop expõe painéis, canais, execução shell/browser e acesso multiusuário; separar control plane, RBAC e isolamento. Handwired é experimental e code execution de terceiros não foi auditada. Tamagui adiciona pacotes/compilador ao supply chain; verificar compatibilidade de versões e licença. Graphicle pode modificar AGENTS.md, hooks e configurações de clientes e capturar sessões; exigir preflight, redaction e opt-in antes de executar setup. Licenças indicadas pela API GitHub: MIT (Yobiru, Octop, Handwired, Tamagui), Apache-2.0 (Caveman, Graphicle); billion-context tem `NOASSERTION` na metadata e depende de revisão específica dos arquivos LICENSE/componentes.

## Materialização

Publicadas alterações em:
- `skills/coding-agent-engineering/SKILL.md` (Caveman e billion-context);
- `skills/crossplatform-mobile-engineering/SKILL.md` (Tamagui);
- `skills/agent-memory-engineering/SKILL.md` (Graphicle);
- `evaluations/2026-10-18-seven-repositories-batch.md` (esta avaliação).

Nenhuma nova skill, stack ou alteração ao índice, pois descriptions e rotas canônicas não mudaram. Yobiru, Octop e Handwired continuam como referências externas, não instalados.

Limites: revisão focada em README e owners, sem testes benchmark independentes, code audit exaustivo, avaliação de manifests transitivos, setup, execução real, compatibilidade de clientes ou prova empírica de economias alegadas. Implementação aqui é atualização de procedimento do Arsenal, não instalação de produtos.
