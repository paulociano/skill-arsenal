# Avaliação: BuilderIO/agent-native

Data: 2026-10-15
Fonte: https://github.com/BuilderIO/agent-native
Fontes inspecionadas: README.md do repositório; ARSENAL INDEX.md e stacks/evaluate-and-import-skill/STACK.md do Arsenal.

## Resultado
- Classificação: **D — framework técnico** para implementação; **B — boa metodologia** para a arquitetura proposta.
- Decisão: **adotar os princípios de actions compartilhadas como referência para engenharia de apps com agentes; não importar o framework nem criar skill redundante neste momento**.

## O que faz
Framework open-source TypeScript para aplicações agentic com UI dedicada. A mesma action tipada/validada é invocada pelo agente como ferramenta e pelo frontend via código, compartilhando autorização e implementação. O README descreve dados e estado compartilhados, React, interface de chat, autenticação, permissões, skills/memória, automações e múltiplas interfaces (HTTP/MCP/A2A/CLI).

## Valor incremental
- Actions reutilizadas entre UI e agente, evitando duplicação de regras de negócio.
- Estado da aplicação contextualiza o agente (página atual, seleção, visualização ativa).
- Trabalho do agente permanece inspecionável e editável na UI.
- Capacidades programáticas devem ser preferidas a clique simulado quando houver API de ações segura.

## Sobreposição e ownership
Já existem no Arsenal `functional-web-app-builder`, `software-engineering-cycle`, `ai-workflow-automation-engineering`, `agent-action-governance` e `computer-use-agent-engineering`. A arquitetura pode influenciar esses owners quando houver implementação agentic concreta; não criar nova skill só para reembalar a documentação da Builder.io.

## Dependências, segurança e limites
- Implementação concreta depende do ecossistema TypeScript/React e seus pacotes, versões e runtime.
- Não assumir que o framework é executável dentro desta conversa.
- Actions compartilhadas aumentam a importância de autorização por usuário/tenant, validação server-side, idempotência, logs e revisões para operações irreversíveis.
- Estado de UI enviado ao agente deve ser filtrado para evitar exposição desnecessária de dados.
- Não executar comandos npx nem instalar dependências do README sem revisão de supply chain.
- Sem verificação de testes, segurança operacional, release/licença por arquivos ou implantação de runtime neste ciclo; documentação da fonte não constitui teste independente.

## Decisão de manutenção
Registrar referência arquitetural. Aplicar a metodologia em uma tarefa de build agentic quando relevante e validar efeito sobre UX, permissões e manutenção. Sem alteração de ARSENAL INDEX porque nenhuma skill/stack foi criada.
