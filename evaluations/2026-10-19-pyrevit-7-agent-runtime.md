# Avaliação — pyRevit v7.0.0.26278+2233

Data: 2026-10-19

## Fonte
- Release oficial: https://github.com/pyrevitlabs/pyRevit/releases/tag/v7.0.0.26278%2B2233
- Publicação da release: 2026-10-06
- GitHub do Arsenal: ARSENAL INDEX.md e stack evaluate-and-import-skill
- Owner analisado: skills/bim-ifc-engineering/SKILL.md
- Owner de governança correlato: skills/agent-action-governance/SKILL.md

## O que é
pyRevit é um ambiente de extensão e automação do Autodesk Revit. A release 7.0 adiciona runtime de agentes MCP (host opt-in dentro do Revit e servidor stdio), com programas Python enviados à Revit API, além de shell IronPython interativo no ribbon. Também incorpora melhorias de build, assinatura, CI, desempenho, interface e configuração.

O runtime documenta get_context, inspect_elements, lookup_revit_api, show_elements, capture_view, run_query, run_modify, get_run e get_skill. A release declara guardrails transacionais: query sem alteração, rollback para violações, bloqueio de save/export/sync durante run, falha quando outro documento é alterado, fechamento de documentos auxiliares sem salvar, timeout, rejeição de transações abertas e Undo único para mudanças aprovadas. No modo padrão ask, aprovação Keep/Discard ocorre no Revit após seleção/isolation temporária de elementos alterados.

## Avaliação
**Classe A/D.** A metodologia é realmente útil para agentes que manipulam modelos BIM; sua execução depende do Revit e host pyRevit configurados. Não equivale a um runtime nativo do ChatGPT.

**Decisão: UPDATE_EXISTING.** A habilidade genérica deve viver em bim-ifc-engineering; não criar skill pyRevit-specific duplicada. O ganho incremental em relação ao owner anterior é separar query read-only de modificação transacional, visualizar diff, aprovação nativa do aplicativo, rollback/undo único e checagem do documento ativo, de transações abertas e de operações save/export/sync.

### Segurança
**CAUTION.** Execução de Python dentro de um Revit autenticado pode modificar modelos importantes. O host reduz risco para runs guardadas, mas não valida arbitrariamente todo código ou efeitos externos. Não pressupor controle de scripts executados fora desse runtime. Verificar versão, política, fonte do script e permissões; manter usuário responsável pelo Keep/Discard. Instaladores assinados disponibilizados na release não foram executados nem auditados binariamente. Notas de release não substituem teste local.

### Valor e testes
- Should-trigger: usuário pretende consultar/modificar modelo Revit via agente em host pyRevit real.
- Near-miss: elaboração conceitual de planta ou leitura de arquivo IFC sem Revit.
- Aceitação: consulta que tenta alterar modelo reverte; modificação aguardando aprovação permite descartar sem alteração; alteração aceita tem escopo verificado e Undo; export/sync bloqueados durante run; referências entre documentos protegidas.
- Estes são testes recomendados, não resultados já executados.

### Implementação
- Atualizado: skills/bim-ifc-engineering/SKILL.md
- Commit: 07bacd8a69c60309eb576a66ab1295546f997690
- INDEX inalterado porque não foi criado novo owner nem alterada description.
- Nenhuma instalação, conexão MCP, execução de scripts ou alteração de modelos Revit foi realizada.

## Limitações
Revisão documental da release e dos owners do Arsenal. Sem teste runtime e sem inspeção de executáveis. A disponibilidade prática das ferramentas requer Revit/pyRevit e ambiente compatível, explicitamente configurados.
