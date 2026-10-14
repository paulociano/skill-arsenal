---
name: mcp-agent-behavior-testing
description: "Testar contratos MCP e comportamento observável de agentes, distinguindo teste direto, escolha de ferramentas, evidências, repetições e segurança."
---
# MCP Agent Behavior Testing

## Objetivo
Validar servidores MCP e agentes consumidores sem confundir a execução de um teste com a correção da decisão do agente.

## Workflow
1. Contrato independente: derivar resultados esperados de especificação ou requisito, nunca copiar o output atual só para passar.
2. Teste direto primeiro: conectar cliente MCP autorizado, verificar catálogo, schemas, casos válidos, limites, erros, estado, cleanup e resultados estruturados.
3. Teste com agente quando o requisito é seleção ou uso: oferecer alternativas plausíveis, não revelar a ferramenta-alvo e conferir chamadas gravadas, argumentos, sequência, ações proibidas e saída.
4. Evidência: separar testes coletados, execuções realmente registradas, avaliações aprovadas e capturas incompletas. Resposta textual dizendo que usou ferramenta não prova a chamada.
5. Repetição: comparar versões/harnesses com cenários constantes, registrar todas as tentativas, erros, denominador e limitações. Nunca mostrar só o melhor resultado.
6. Segurança: isolar credenciais, limitar privilégios, simular efeitos destrutivos e evitar logs/payloads sensíveis; upload de traces exige autorização.
7. Reportar o que foi testado, o que passou, falhou ou não foi executado e os critérios para nova verificação.

## Portabilidade
Inspirada em https://github.com/sineframe/m3 e sua skill testing-with-m3. O M3 original é uma implementação opcional com Python/pytest, CLI sf-m3-cli, SDK sf-m3 e harnesses. Esta skill não pressupõe instalação do M3 nem integração do ChatGPT com servidores ou traces ausentes. Use somente clientes e ferramentas realmente disponíveis. Não execute instaladores externos por padrão.

## Combinação
software-testing-engineering, skill-security-review, verify-before-claim, conforme necessidade.
