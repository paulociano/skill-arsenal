# Avaliação de cinco repositórios | 2026-10-11

## Método
Triagem pelo `ARSENAL INDEX.md`, seguida de `stacks/arsenal-autopilot/STACK.md`. Consultados os READMEs das branches default de cada fonte e owners relevantes. Não houve instalação, análise integral de código nem teste empírico dos produtos.

| Fonte | Categoria | Decisão | Justificativa / owner |
| --- | --- | --- | --- |
| [EpicGames/raddebugger](https://github.com/EpicGames/raddebugger) | D | KEEP_EXTERNAL_REFERENCE | Depurador gráfico nativo para Windows x64/PDB, em estágio alpha segundo o README. Pode servir em projetos C/C++ com ambiente compatível; `debug-and-fix` já cobre metodologia de diagnóstico e não há runtime do debugger presumido. |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | B/D | KEEP_EXTERNAL_REFERENCE | Roteamento de fontes web, plataformas sociais, vídeos e RSS com canais primários/fallback e diagnóstico; exige ferramentas CLI, sessões, cookies ou autenticação conforme plataforma. `research-and-synthesize` já cobre método; conectar somente meios autorizados, sem instruções de instalação automáticas. |
| [trycua/cua](https://github.com/trycua/cua) | B/D | KEEP_EXTERNAL_REFERENCE | Automação de computador, VMs e drivers; ação em máquina externa e permissões são parte do contrato. O Arsenal não deve afirmar controle de desktop ou sandbox fora das ferramentas realmente disponíveis. |
| [AgentMemoryRepo/agentmemoryrepo](https://github.com/AgentMemoryRepo/agentmemoryrepo) | B/D | UPDATE_EXISTING | Memória em repositório Git privado com índice pequeno, links e provenance; atualizada `agent-memory-engineering`, com fronteiras de escopo e correções. Não habilitar push automático ou usar conteúdo sensível sem autorização. |
| [lucasmarkes/hairline](https://github.com/lucasmarkes/hairline) | B/D | UPDATE_EXISTING | Biblioteca de figuras isométricas reativas; enriquecida `interaction-polish` com acessibilidade, fallback, cleanup e reduced motion. Pacote não instalado. |

## Portabilidade, segurança e licenças
- Todos são fontes técnicas, não permissões nem recursos instalados neste ChatGPT.
- Não executar instaladores remotos, scripts, extensões, drivers, VMs ou agentes para avaliá-los.
- Agent-Reach: credenciais, cookies, contas sociais, proxies e limites dos serviços são fronteiras de confiança; não contornar autenticação.
- CUA: mouse/teclado/desktop podem causar efeitos externos; usar autorização, isolamento e verificação visual adequados.
- AgentMemoryRepo: exclusão e ACL devem cobrir histórico e backups; Git não é substituto de política de privacidade.
- RAD: depuração de processos requer host, símbolos e autorização; não reivindicar suporte Linux do debugger com base na toolchain de build.
- Hairline: confirmar licença/versão para uso concreto; não garantir a11y por descrição do README.
- Nenhum código externo foi copiado, nenhuma instalação foi feita.

## Aceitação e near misses
- **Memória, deve acionar:** projeto pede lembranças auditáveis e retomada entre sessões em sistema com Git persistente; verificar índice, provenance, permissão, conflito e leitura posterior. **Não acionar:** pergunta pontual sem necessidade de retenção.
- **UI, deve acionar:** projeto solicita microfigura reativa em landing page existente; validar teclado/toque/reduced-motion/cleanup. **Não acionar:** relatório estático sem interface.
- **Ferramentas externas:** sempre verificar a existência concreta do runtime antes de sugerir execução, sem instalar automaticamente.

## Resultado
Duas skills existentes enriquecidas, três fontes mantidas como referência, nenhuma skill/stack nova. O índice permanece inalterado porque nomes, rotas e descriptions não mudaram.
