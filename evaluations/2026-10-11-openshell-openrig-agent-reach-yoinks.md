# Avaliação: OpenShell, OpenRig, Agent-Reach e yoinks | 2026-10-11

## Método e escopo
Aplicada a stack `arsenal-autopilot`, após leitura de `ARSENAL INDEX.md`, `stacks/arsenal-autopilot/STACK.md`, `stacks/evaluate-and-import-skill/STACK.md` e READMEs atuais dos quatro repositórios. Comparadas as capacidades com `agent-action-governance`, `ai-workflow-automation-engineering` e a avaliação anterior de Agent-Reach (`evaluations/2026-10-11-raddebugger-agent-reach-cua-agentmemoryrepo-hairline.md`). Não houve instalação, auditoria integral de código ou testes de runtime.

| Fonte | Classe | Decisão | Owner / valor incremental |
| --- | --- | --- | --- |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | D | KEEP_EXTERNAL_REFERENCE | Isolamento de agentes com enforcement de kernel, políticas para arquivos/rede/processos e controle de credenciais, além de revisão de políticas. `agent-action-governance` já incorpora o padrão portátil de menor privilégio, política fail-closed e auditoria; enforcement real depende de infraestrutura OpenShell, não presente por implicação no ChatGPT. |
| [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | B/D | ABSORB_METHOD_ONLY | Equipes de coding agents persistentes, papéis, filas, contexto e revisão. Metodologia coberta por `multi-agent-orchestration` e `ai-workspace-operating-cycle`; integração de Claude Code, Codex, tmux, hooks e daemon depende de runtime externo. Sem nova skill. |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | B/D | KEEP_EXTERNAL_REFERENCE | Roteamento por canal, fallback e diagnóstico de fontes web/RSS/vídeo/sociais; avaliação prévia em 2026-10-11 decidiu corretamente pela referência externa. Reafirmada para evitar duplicação com pesquisa e conectores autorizados. |
| [pablostanley/yoinks](https://github.com/pablostanley/yoinks) | D | KEEP_EXTERNAL_REFERENCE | TUI para download local usando yt-dlp e ffmpeg, com seleção de resolução/áudio. Não introduz metodologia distinta para Arsenal. Referência somente se um workflow legal e autorizado exigir download no host; não presumir execução em ChatGPT. |

## Segurança e portabilidade
- **OpenShell:** a alegação de verificação formal e enforcement é propriedade do produto, não prova de segurança do ChatGPT; validar plataforma, versões, policy efetiva e bypasses no deployment real. Instalador remoto `curl | sh` não foi executado.
- **OpenRig:** setup pode alterar trust settings, hooks executáveis e permissões do workspace. Evitar configurações não-interruptivas/amplas sem avaliação independente. Node, tmux e harnesses são dependências reais.
- **Agent-Reach:** cuidado com cookies, sessões autenticadas, termos de plataformas e risco de bloqueio. Instaladores de shell e bibliotecas sociais não foram executados.
- **Yoinks:** executa/obtém binários externos e grava downloads locais; verificar licença, direitos sobre mídia, integridade de dependências e restrições de plataforma. Não presumir suporte nativo à transferência para ChatGPT.

## Critérios de adoção e near misses
- **Should-trigger OpenShell:** projeto real precisa isolar execução autônoma com acesso controlado a filesystem/network/credenciais, com host e deployment compatíveis. **Near miss:** apenas escrever prompts mais seguros.
- **Should-trigger OpenRig:** equipe de coding agents persistente operando no host com contas e ferramentas instaladas. **Near miss:** tarefa curta resolvida por um agente.
- **Should-trigger Agent-Reach:** projeto externo com múltiplas fontes e diagnóstico de conectores locais já autorizado. **Near miss:** pesquisa web comum no ChatGPT.
- **Should-trigger yoinks:** baixar mídia própria/autorizada numa máquina com Node e armazenamento. **Near miss:** resumir um vídeo ou criar um roteiro sem download.

## Resultado
Nenhuma nova skill ou stack. Esta avaliação consolida a decisão e preserva as fronteiras de runtime. Não alterar `ARSENAL INDEX.md`: owners, nomes, descrições e rotas permanecem válidos. As fontes externas ficam como referências, não como pacotes instalados ou promessas de capacidade disponível.
