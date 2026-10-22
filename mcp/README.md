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


## Fase 2: servidor MCP local funcional (somente leitura)

`mcp/catalog_server.py` expõe um servidor MCP **stdio** JSON-RPC 2.0, usando só Python da biblioteca padrão. Ele implementa `initialize`, `ping`, `tools/list`, `tools/call` e notificações sem resposta. Ferramentas:
- `arsenal_list_integrations`: enumera candidatos declarados no catálogo (não descobre instalações reais).
- `arsenal_get_integration`: lê um registro por ID exato.
- `arsenal_client_compatibility`: consulta matriz de compatibilidade declarativa.

Nenhuma ferramenta pode executar comandos, ler arquivos arbitrários, acessar redes, modificar o repositório ou transmitir tokens. Ferramentas desconhecidas e entradas extras falham fechadas. O servidor anuncia capacidades de **leitura**, sem prometer executar o MCP de terceiros ou conceder autorização por listar um item.

### Configuração Codex CLI (na cópia clonada do Arsenal)

Exige Python 3.9+ e Codex CLI instalado. Substitua `/CAMINHO/skill-arsenal` pelo caminho absoluto do clone local.

```sh
codex mcp add arsenal-catalog -- python /CAMINHO/skill-arsenal/mcp/catalog_server.py
codex mcp list
```

No Windows, use o executável Python instalado e o caminho absoluto correspondente:

```powershell
codex mcp add arsenal-catalog -- python "C:\\Users\\ph_gr\\Skill-Arsenal\\mcp\\catalog_server.py"
codex mcp list
```

O comando **registra** o servidor na configuração local do Codex, não conecta automaticamente GitHub, PostgreSQL ou Filesystem. Para desativar: `codex mcp remove arsenal-catalog`.

### Testes

```sh
python scripts/validate_mcp_catalog.py
python -m unittest discover -s tests -p 'test_mcp_catalog.py' -v
```

O workflow `.github/workflows/mcp-catalog.yml` executa esses dois comandos no GitHub Actions. Além dos checks do catálogo, os testes cobrem handshake, anúncio de tools read-only, leitura de registros, rejeição de comandos desconhecidos e round-trip stdio. Não afirmam compatibilidade real com uma instalação Codex local, nem com MCPs externos.

**Limites:** não existe autenticação externa, bridge HTTP, proxy para servidores terceiros, gateway com política de escrita ou discovery do runtime nesta fase. Qualquer habilitação futura de ferramentas com efeitos exige revisão de governança e aprovação apropriada.
