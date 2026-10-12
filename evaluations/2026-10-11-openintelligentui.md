# Avaliação: CopilotKit/OpenIntelligentUI

- Data: 2026-10-11
- Fonte: https://github.com/CopilotKit/OpenIntelligentUI
- Classificação: **D — técnica**, com metodologia incorporável como **B**
- Decisão: **ADAPTAR a skill existente `generative-ui-engineering`; não criar uma nova skill nem instalar o framework automaticamente.**
- Segurança: **CAUTION** para deploy real; padrões metodológicos podem ser reutilizados sem executar código externo.

## O que realmente oferece
Aplicação demonstrativa de chat com UI generativa que roteia a resposta entre texto, componentes nativos/A2UI e HTML/CSS/JS customizado em sandbox. Mostra explicações, 3D, gráficos, calculadoras, mapas e follow-ups disparados por usuário. Stack documentada: Next.js/React + CopilotKit/AG-UI; Python FastAPI/LangGraph/Deep Agents; Websandbox no navegador; MCP independente opcional.

## Valor incremental sobre o Arsenal
O Arsenal já possui `generative-ui-engineering`, com component grammar, sandboxing, streaming, allowlists e bridges. Não cabe duplicar. Incrementos aproveitáveis:
1. roteamento orientado à tarefa (entender, comparar, construir ferramenta) e preferência por texto quando suficiente;
2. manter controles e cálculos locais, iniciando follow-up do agente somente por ação explícita com estado validado;
3. tratar outputs anteriores como snapshots, sem assumir DOM patch entre gerações;
4. controles com validação numérica, reset, fallback sem JS, responsividade e reduced motion;
5. transparência para dados de exemplo, ausência de fonte ao vivo e limites de persistência.

## Dependências, limites e portabilidade
O README exige Node.js 22+, pnpm 9+, Python 3.12+, uv e credenciais de provedores. O modelo de resposta e o roteador de visualização podem exigir chaves OpenAI/Jev, com cobranças próprias. O contrato de `generateSandboxedUi` e a bridge `Websandbox.connection.remote` são específicos daquele runtime, não ferramentas nativas do ChatGPT. O MCP standalone monta HTML, mas não reproduz automaticamente o streaming, renderer ou bridge do aplicativo.

## Revisão de segurança (estática, não exaustiva)
- Credenciais inseridas pelo visitante trafegam pelo servidor de aplicação até provedores; confiar no operador do deployment é requisito.
- Sandbox restringe acesso a host DOM, storage e network conforme documentação; revisar CSP, permissões, importmaps e validação de messages antes de uso real.
- A UI criada pode conter JS; não executar scripts da fonte para avaliar e não passar segredos ao documento gerado.
- Dependências npm incluem versões preview de CopilotKit; Python combina versões pinadas com ranges. Fixar versões/lockfiles e auditar cadeia de dependências e updates.
- Checkpoint em memória (BoundedMemorySaver) não equivale a persistência durável, especialmente com múltiplas instâncias.
- Testes e builds não comprovam conectividade real dos provedores, segurança de produção ou funcionamento completo do deployment.
- Veredicto: **CAUTION para implementação em produção**, não identificado comportamento malicioso na documentação inspecionada; isto não substitui auditoria de código, execução, supply chain e infraestrutura.

## Arquivos consultados
- https://github.com/CopilotKit/OpenIntelligentUI/blob/main/README.md
- https://github.com/CopilotKit/OpenIntelligentUI/blob/main/docs/architecture.md
- https://github.com/CopilotKit/OpenIntelligentUI/blob/main/docs/bring-to-your-app.md
- https://github.com/CopilotKit/OpenIntelligentUI/blob/main/apps/agent/skills/master-playbook/SKILL.md
- https://github.com/CopilotKit/OpenIntelligentUI/blob/main/apps/agent/skills/advanced-visualization/SKILL.md
- https://github.com/CopilotKit/OpenIntelligentUI/blob/main/apps/app/package.json
- https://github.com/CopilotKit/OpenIntelligentUI/blob/main/apps/agent/pyproject.toml
- https://github.com/paulociano/skill-arsenal/blob/main/skills/generative-ui-engineering/SKILL.md

## Mudanças realizadas e verificação
Atualizada `skills/generative-ui-engineering/SKILL.md` com roteamento por intenção, estado/follow-up e nota de implementação e limitações específicas. Não há mudança de descrição ou nova skill, portanto o índice não requer modificação. Verificação estática/read-after-write de ambos os arquivos; sem instalação ou execução de código externo.
