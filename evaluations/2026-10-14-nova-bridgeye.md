# Avaliação: bridgeyeai/nova-bridgeye (2026-10-14)

## Fonte e escopo
- Repositório: https://github.com/bridgeyeai/nova-bridgeye (branch `main`, consultado em 2026-10-14).
- Fontes inspecionadas: README.md, LICENSE, metadados e listagem do diretório raiz no GitHub.
- O repositório público contém README.md e LICENSE, sem fonte do agente ou testes publicados nesse repositório. Não foi instalado ou executado o pacote.
- A documentação anuncia CLI Python 3.10+, `pip install nova-bridgeye`, execução de scripts, diagnóstico por traceback, edições localizadas, reinstalação de dependências e reexecução. São alegações do fornecedor, não resultados verificados.

## Classificação e decisão
**D — ferramenta técnica dependente de runtime externo e pacote proprietário.**
**Decisão: registrar e não importar uma nova skill.** O padrão útil de executar → observar traceback → localizar causa → aplicar patch mínimo → reexecutar → verificar já está coberto por `coding-agent-engineering` e `diagnosing-bugs`; não há ganho metodológico novo demonstrado. Uma ferramenta instalável não equivale a uma Agent Skill portátil. Não há integração nativa confirmada com o ChatGPT.

## Licença e revisão de segurança
- **Inconsistência relevante:** o README declara MIT, mas o arquivo LICENSE é intitulado `MASTER PROPRIETARY LICENSE AND EULA` e restringe engenharia reversa, redistribuição, obras derivadas e benchmarking competitivo. A licença efetiva necessita esclarecimento jurídico junto ao titular; não assumir autorização MIT.
- O produto declara confirmação humana antes de alterações e instalação de pacotes; essa salvaguarda não foi testada.
- O README afirma que o código permanece local; LICENSE prevê coleta possível de tracebacks anonimizados. É necessário esclarecer fluxo de dados e tratamento de informações sensíveis.
- Instalação de dependências, alteração automática de código, autenticação e execução de comandos ampliam riscos de supply chain, credenciais e efeitos locais.
- **Parecer de segurança: CAUTION / insuficiente para aprovação de execução.** Não há código-fonte nem cadeia de instalação auditáveis neste repositório. Não é alegação de comportamento malicioso.

## Relação com Arsenal
- `skills/coding-agent-engineering/SKILL.md`: já documenta loop edit-test-repair, boundaries, patches, análise de diff e testes.
- `skills/diagnosing-bugs/SKILL.md`: já exige reprodução, hipóteses, correção causal e teste de regressão.
- `skills/skill-security-review/SKILL.md`: exige revisão sem executar instalador.
- `stacks/evaluate-and-import-skill/STACK.md`: rota de avaliação aplicada.

## Critério de reconsideração
Reavaliar somente se houver documentação técnica e evidência auditável do comportamento, licença esclarecida, transparência sobre dados enviados, permissões, controles para instalaçōes e patches, e demonstração de ganho incremental além das competências existentes.

## Alterações no Arsenal
Apenas este registro; nenhuma nova skill/stack ou mudança no índice.
