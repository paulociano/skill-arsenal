# Avaliação: OpenChatCut (2026-10-18)

- Fonte: https://github.com/0xsline/OpenChatCut
- Skill analisada: https://github.com/0xsline/OpenChatCut/blob/main/skills/openchatcut/SKILL.md
- Referência: skill versão 2026-09-04.1 (consultada em 2026-10-18).
- Método interno: `stacks/evaluate-and-import-skill/STACK.md`, `skills/skill-security-review/SKILL.md`.
- Classificação: **D — skill técnica dependente de aplicativo e ferramentas externas**.
- Decisão: **REFERENCE_ONLY / não importar** a skill como nativa do Arsenal.

## O que realmente faz
OpenChatCut é um editor local-first de vídeo com timeline multifaixa, Remotion, Electron, interface de IA e um servidor MCP local. A skill externa não fornece um método geral de edição: roteia agentes conectados ao aplicativo para documentação de instalação, edição e erros; exige servidor MCP em `http://localhost:5199/api/external-mcp/mcp`, `openchatcut_status`, `list_projects`, `load_skill`, `begin_edit_session`, `review_edit_session` e `get_edit_session`.

## Comparação com o Arsenal
O Arsenal já possui `video-editing-pipeline`, `short-form-video-engineering`, `explainer-video-production`, e `ai-reels-production`. A skill externa não adiciona uma metodologia independente dessas capacidades. O diferencial reside no runtime OpenChatCut, seu editor e seu servidor MCP. Sem esse runtime e conexão efetiva, reproduzir o protocolo seria enganar o usuário; o conteúdo existente do Arsenal continua canônico para tarefas de edição.

## Segurança e portabilidade
Veredito estático: **CAUTION**. A skill instrui instalar pacotes via `npx skills`, iniciar um servidor local e dar ao agente poder de editar/exportar projetos. Ela estabelece sessão de edição e aprovação manual como default, reutilização controlada, e verificação de estado aplicado. São bons controles, porém o aplicativo instalado e suas dependências não foram auditados nem executados; não há conexão OpenChatCut MCP nesta sessão. A origem é distribuída sob AGPL-3.0; revisar obrigações de licença antes de redistribuição/serviço. Não executar comandos de setup a partir deste registro. Não assumir que endpoint localhost de uma máquina é acessível pelo ChatGPT hospedado.

## Adoção
Não criar skill duplicada, nem modificar o índice: nenhuma competência portátil nova foi identificada. Manter o OpenChatCut como opção de runtime externo a avaliar quando houver solicitação concreta para instalar, integrar ou editar nele. Nesse caso verificar disponibilidade real do conector e permissões antes de operar. Adaptação futura poderia mapear seu approval gate para a EDL + verificação do `video-editing-pipeline`, mas essa exigência já consta do owner.

## Limites da revisão
Foram lidos README, metadados e SKILL.md da origem; não foi realizada auditoria exaustiva de código, dependências, instaladores, execução, render ou testes de segurança. Esta é avaliação documental da integração, não certificação de segurança do aplicativo.
