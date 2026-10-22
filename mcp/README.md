# Arsenal MCP: fase 1 (catálogo e contratos)

Este diretório fornece **metadados portáveis**, não um gateway em execução, instalador, servidor MCP, credenciais ou concessão de acesso. A autoridade para seleção de skills continua em `ARSENAL INDEX.md`; `AGENTS.md` e `skills/` permanecem intactos.

## Artefatos

- `registry.json`: integração candidata por ID, protocolo, capacidades, classes de efeito e exigência de credencial.
- `compatibility.json`: matriz de clientes/transporte e política conservadora.
- `../scripts/validate_mcp_catalog.py`: validação estrutural, integridade, duplicidade, escopo e proibição de segredos.

## Fluxo de execução (futuro adaptador)

1. Ler `ARSENAL INDEX.md`, selecionar a menor skill/stack útil e somente seus arquivos necessários.
2. Ler `registry.json` e `compatibility.json`. Um ID listado **não** significa ferramenta conectada.
3. Descobrir ferramentas reais do runtime e verificar catálogo, transporte, schema, permissões e credencial sem revelar o segredo ao modelo.
4. Resolver identidade/target, classificar efeito e aplicar política **deny by default**, inclusive sobre ferramentas desconhecidas; registrar decisão antes de efeito.
5. Executar somente operações autorizadas, verificar o estado final e registrar evidência. Nunca declarar sucesso a partir de resposta textual do agente.

## Convenções

- IDs em kebab-case e estáveis; nomes de ferramentas são descritivos e não equivalem a chamadas disponíveis.
- `mcp_stdio`: servidor iniciado no host do cliente; não disponível diretamente no ChatGPT web.
- `mcp_remote`: conexão remota sujeita a compatibilidade, plano, autenticação e política da plataforma.
- `native_connector`: integração do produto, **não presume** implementação via MCP.
- Classes de efeito: `read`, `local_write`, `remote_write`, `shell`; risco desconhecido deve bloquear até classificação.
- `verification: unverified_per_runtime` permanece até teste real por cliente/conta, não deve ser convertido globalmente para "instalado".
- A política descritiva neste JSON **não impõe controle de acesso**; enforcement exige gateway/adaptador testado.

## Critérios de aceite para fase 1

Executar `python scripts/validate_mcp_catalog.py` em ambiente Python 3.9+. Confere parse JSON, chaves, valores, referências, IDs únicos, classes de efeito e ausência de padrões óbvios de segredo. Esse teste é estático; testes diretos MCP, autenticação, autorização efetiva, UI, compatibilidade real e agent-choice permanecem pendentes.

## Próxima fase

Criar adaptador/gateway real com discovery MCP, contrato de schema, policy enforcement server-side, credenciais isoladas, audit-before-act, testes reais e suporte remoto autenticado. Não instalar servidores de terceiros automaticamente.

## Metodologia reutilizada

- `skills/ai-workflow-automation-engineering/SKILL.md`
- `skills/agent-action-governance/SKILL.md`
- `skills/mcp-agent-behavior-testing/SKILL.md`
