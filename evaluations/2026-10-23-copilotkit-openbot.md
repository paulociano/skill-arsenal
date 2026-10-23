# Avaliação: CopilotKit/OpenBot

- Data: 2026-10-23
- Fonte: https://github.com/CopilotKit/OpenBot (branch main; README, package.json, docker-compose.yml, scripts/start.sh, docs/deployment.md, docs/routines.md, docs/configuration.md)
- Fonte canônica Arsenal: https://github.com/paulociano/skill-arsenal/blob/master/ARSENAL%20INDEX.md
- Categoria: **D — sistema técnico/runtime de agentes**, com metodologia **B** já absorvida.
- Decisão: **KEEP_EXTERNAL_REFERENCE**. Não importar código nem criar skill duplicada. **CAUTION** para implantação; piloto isolado condicionado a testes.

## O que faz

OpenBot é um template alpha MIT auto-hospedável de coworkers IA via AG-UI, com canais, bots, componentes, computadores/navegadores, política de ações, auditoria, credenciais, integrações MCP e rotinas. É produto/runtime, não SKILL.md portátil. Exige Docker, Bun (desenvolvimento), banco PostgreSQL, CopilotKit Intelligence/licenciamento apropriado e chave de modelo. A imagem única não inclui supervisor de computadores separados nem worker de rotinas: precisam de infraestrutura adicional.

## Capabilities e ownership

| Capability | Owner existente | Decisão |
|---|---|---|
| Policy fail-closed, audit-before-act, credenciais e takeover humano | skills/agent-action-governance | Já incorporado com referência explícita a CopilotKit/OpenBot; sem delta metodológico demonstrado |
| Agendamento, worker, retries, credenciais e observabilidade | skills/ai-workflow-automation-engineering | Referência externa; sem nova skill |
| Operação multiagente e delegação | skill multi-agent-orchestration (router) | Referência externa; runtime não é metodologia portátil |
| Computador/navegador por bot, AG-UI, canais e componentes executáveis | Runtime externo | **KEEP_EXTERNAL_REFERENCE**; dependência real de implantação e testes |
| Persistência e integração corporativa | owners de memória e integrações | Não presumir que OpenBot oferece capacidade nativa neste ChatGPT |

## Prova de valor incremental

Valor real potencial: executar agentes próprios em infraestrutura gerenciada, com navegador isolado, auditoria e tarefas recorrentes, além do que uma skill textual pode fazer. Não há evidência de incremento de instrução portátil sobre os owners existentes. Não criar nova skill nem alterar o índice.

Cenário should-trigger para piloto: empresa exige agente com navegador autenticado, isolamento por agente, trilha de execução e aprovação. Near-miss: simples pesquisa, redação ou automação com conectores disponíveis no ChatGPT. Critério de aceitação: ambiente de teste reproduzível, isolamento confirmado, policy denies testados, auditoria precedendo efeito, aprovação vinculada ao payload, segurança de credenciais, rotina com worker, restauração e upgrade testados.

## Segurança e portabilidade

**CAUTION**: projeto alpha com execução shell/browser, credenciais, integrações, acesso web e efeitos externos. A imagem única compartilha navegador entre bots sem supervisor, logo não fornece isolamento entre tenants. `OPENBOT_SINGLE_USER=true` admite solicitações como administrador, somente aceitável em localhost/laboratório. Defaults conhecidos de tokens e senha local do compose não devem ir para produção. Separar egress, rede de banco, socket Docker e volume; usar SSO/identidades individuais, TLS, policies deny-by-default, segregação de credenciais, revisão de MCP e bloqueio de escrita sem aprovação. Avaliar prompt injection, SSRF, vazamento de credenciais e acesso cruzado. Pin por digest/commit, não `:latest`; SBOM/vulnerability scan e backup criptografado. O README afirma controle e auditoria, mas a leitura estática não demonstra ausência de bypass.

Revisão apenas estática e parcial (README, config, deployment, routines, package, compose, inicialização); **não** houve instalação, execução de testes, pentest, scanner CVE, análise completa de dependências ou verificação de supply chain. Sem licença especial de OpenBot, mas Intelligence e chamadas a modelos podem ter custos/licenças.

## Plano de integração recomendado (fora do Arsenal, não executado)

1. PoC Windows com WSL2/Docker Desktop, projeto de teste e dados sintéticos.
2. Fixar versão/digest, pin de dependências e segredos próprios; habilitar autenticação antes de acesso externo.
3. Subir supervisor/containers por Bot e worker separado; verificar explicitamente os dois (ausentes na imagem all-in-one).
4. Criar agente somente leitura para gestão/agenda usando integrações autorizadas; adicionar write grants apenas mediante testes de autorização.
5. Executar suíte de testes de boundaries, auditoria, egress/SSRF, cross-agent, restore, custos e latência.
6. Decidir ADOPT_RUNTIME / REJECT_RUNTIME com evidências; manter skills canônicas como metodologia independente.

## Resultado de publicação

Somente este registro de avaliação. Não há owner novo, portanto não atualizar ARSENAL INDEX. Não foi implantado OpenBot.
