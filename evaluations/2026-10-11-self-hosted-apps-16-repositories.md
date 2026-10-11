# Avaliação de 16 aplicações open source | 2026-10-11

## Escopo e evidência
Fontes: branches default dos 16 repositórios listados abaixo; metadados oficiais GitHub e READMEs acessíveis nesta data. Exceto Grashjs/cmms (README.md em main indisponível), foram lidos READMEs. **Não** houve instalação, teste funcional, análise de código aprofundada, auditoria de segurança ou verificação empírica das alegações. Ausência de vulnerabilidades observadas **não** implica segurança demonstrada.

Referências canônicas: `ARSENAL INDEX.md`, `stacks/arsenal-autopilot/STACK.md`, `stacks/evaluate-and-import-skill/STACK.md`, `skills/ai-workflow-automation-engineering/SKILL.md`. As fontes são **aplicações**, não arquivos SKILL.md compatíveis. Classificação B = metodologia absorvível; D = runtime/aplicação técnica; C/A não atribuídas sem prova incremental de skill independente.

| Fonte | Classe | Decisão | Capacidade identificada | Owner / rota | Ressalva |
| --- | --- | --- | --- | --- | --- |
| [Worklenz/worklenz](https://github.com/Worklenz/worklenz) | B/D | `ABSORB_METHOD_ONLY` | planejamento de capacidade, tarefas, custos, timesheets e visões de projeto | product-management-cycle / gestão comercial | Aplicação AGPL; sem conector autorizado |
| [open-wanderer/wanderer](https://github.com/open-wanderer/wanderer) | D | `KEEP_EXTERNAL_REFERENCE` | catálogo GPX, rotas e busca geoespacial | domain-specific mapping | Servidor e dados GPS sensíveis; ganho genérico insuficiente |
| [degoog-org/degoog](https://github.com/degoog-org/degoog) | B/D | `KEEP_EXTERNAL_REFERENCE` | federação de buscadores e plugins de pesquisa | research-and-synthesize | Plugins executam código no servidor; não habilitar extensões automaticamente |
| [sorathiya903/pastedb](https://github.com/sorathiya903/pastedb) | D | `KEEP_EXTERNAL_REFERENCE` | compartilhamento de snippets com expiração e criptografia declarada | secure sharing / app engineering | Não validar E2EE apenas pelo README; execução de código amplia risco |
| [baserow/baserow](https://github.com/baserow/baserow) | B/D | `ABSORB_METHOD_ONLY` | modelagem de base relacional no-code, views, formulários, automações, APIs | data-modeling / functional-web-app-builder | Licenças open-core por componente; dependência de serviço explícita |
| [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | D | `KEEP_EXTERNAL_REFERENCE` | timeline, detecção de visitas, tracks e compartilhamento geográfico | geospatial apps | Exposição de localização, retenção e permissões sensíveis |
| [prasadpatil25/mindspark](https://github.com/prasadpatil25/mindspark) | B/D | `ABSORB_METHOD_ONLY` | mapas mentais editáveis, roundtrip Markdown, versionamento e export | knowledge structuring / visual thinking | App e integrações não disponíveis automaticamente |
| [Cloeille/picsou-finance](https://github.com/Cloeille/picsou-finance) | B/D | `KEEP_EXTERNAL_REFERENCE` | agregação multiativos, household finance e adapter ports | financial-analysis-cycle | Conectores focados em instituições europeias; licença com Commons Clause |
| [Grashjs/cmms](https://github.com/Grashjs/cmms) | D | `KEEP_EXTERNAL_REFERENCE` | ordens de serviço, ativos, manutenção preventiva | domain-specific asset maintenance | README no root/main não encontrado; avaliação restrita a metadados |
| [ptweezy/cronstable](https://github.com/ptweezy/cronstable) | B/D | `UPDATE_EXISTING` | agendamento com lint, time zones, missed runs, retries, DAG, histórico e alertas | ai-workflow-automation-engineering | Sem importar runtime; schedules e APIs exigem teste no ambiente real |
| [screentinker/screentinker](https://github.com/screentinker/screentinker) | B/D | `KEEP_EXTERNAL_REFERENCE` | playlists, publicação versionada, kiosk/offline, telemetria e signage | digital signage domain | Controle remoto e device-side requests precisam escopo/autorização |
| [LosaLosSantos/aurelio-finance](https://github.com/LosaLosSantos/aurelio-finance) | B/D | `ABSORB_METHOD_ONLY` | análise financeira local; propostas de alteração em cards confirmados | financial-analysis-cycle / agent-action-governance | Não reutilizar promessas/custos/modelos sem verificar; requer OpenRouter |
| [getopenpost/openpost](https://github.com/getopenpost/openpost) | B/D | `ABSORB_METHOD_ONLY` | adaptação multicanal, filas, calendário, aprovações e analytics | social-growth-engine / content-production | Publicação requer credenciais e confirmação |
| [MODSetter/SurfSense](https://github.com/MODSetter/SurfSense) | B/D | `ABSORB_METHOD_ONLY` | pesquisa documental local, citações, transformações e cópia auditável | research-and-synthesize / agent-memory-engineering | Air-gap depende de configuração real; jamais inferir acesso a arquivos locais |
| [harshalgajjar/Reminal](https://github.com/harshalgajjar/Reminal) | D | `KEEP_EXTERNAL_REFERENCE` | acesso remoto navegador a janelas e terminais | remote operations / security | Potencial controle pleno do host; jamais instalar shell scripts ou habilitar relay sem autorização |
| [ancsemi/Haven](https://github.com/ancsemi/Haven) | D | `KEEP_EXTERNAL_REFERENCE` | comunicação self-hosted, canais, voz e bridging | communication systems | Bridges e importações com tokens têm riscos de privacidade e permissão |

## Decisão editorial
- **UPDATE_EXISTING:** cronstable justifica explicitar verificação de calendários e agendamentos, além de retries já cobertos. Atualização limitada à skill de automações.
- **ABSORB_METHOD_ONLY:** Worklenz, Baserow, MindSpark, Picsou, Aurelio, OpenPost e SurfSense têm padrões aproveitáveis por seus owners atuais, sem demonstração de novo trigger/contrato que justifique criar skill. Suas observações permanecem neste ledger para uso contextual.
- **KEEP_EXTERNAL_REFERENCE:** Wanderer, Degoog, PasteDB, Reitti, CMMS, ScreenTinker, Reminal e Haven são tecnologias especializadas. Não importar infraestrutura ou instruções de instalação para o Arsenal.

## Gate de portabilidade e segurança
1. Não executar `curl | sh`, scripts de setup, imagens Docker ou binários de terceiros como parte da avaliação.
2. Não assumir integração ativa com Baserow, Worklenz, SurfSense, OpenPost, cronstable etc.; capacidade só existe se o runtime/conector for realmente disponível.
3. Tratar localização, extratos bancários, arquivos privados, históricos de mensagens e controle remoto como dados ou ações de alto impacto; preservar mínimo privilégio, revisão e confirmação de efeitos.
4. Respeitar licenças distintas (AGPL, MIT, open-core, Commons Clause e componentes com licenças próprias); nenhuma cópia de código foi feita.
5. Readmes são alegações de autores; E2EE, air-gap, compliance, segurança, desempenho e produção não foram auditados.

## Testes de aceitação do incremento
**Should trigger:** pedido para desenhar automação agendada com horários em fusos distintos, calendário de feriados e regras business-day; produzir casos de borda, run history, missed-run e testes de DST quando aplicável.
**Near miss:** pedido apenas para redigir um lembrete único no ChatGPT não deve introduzir cronstable nem presumir agendamento de segundos.
**Prova:** plano contendo entradas, timezone, horário esperado, exemplos negativos, tratamento de falha e evidência de execução do provedor quando disponível.

## Publicação
Somente um registro de lote e uma alteração incremental na skill existente; **sem novas skills/stacks e sem alteração do índice** porque rotas e descriptions atuais não mudaram.
