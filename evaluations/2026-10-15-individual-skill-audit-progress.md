# Avaliação individual de skills externas — rastreador de cobertura

Data: 2026-10-15. **Estado: PARCIAL, não concluído.**

## Inventário com fonte verificável
Foram localizados **1719** SKILL.md nas árvores recursivas dos 12 repositórios e criadas fichas **individuais de descoberta** por caminho. **283 skills** tiveram seus SKILL.md abertos e decisões documentais individuais registradas: 10 slavingia, 11 antfu, 23 MiniMax, 1 multica/Karpathy, 5 BrowserAct e 176 MengTo e 57 Google. **1436** permanecem sem leitura individual de SKILL.md. A leitura dos documentos principais não equivale a auditoria integral dos arquivos associados, scripts, referências e execução; a segurança permanece condicionada a revisão por adoção. Nas fichas, flags baseadas somente no caminho são **hipóteses**, não aprovação nem decisão real.

| Repositório | Arquivos SKILL.md | Inventário |
|---|---:|---|
| google-skills | 166 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-google-skills.md) |
| multica-ai-andrej-karpathy-skills | 1 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-multica-ai-andrej-karpathy-skills.md) |
| composiohq-awesome-claude-skills | 864 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-composiohq-awesome-claude-skills.md) |
| antfu-skills | 11 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-antfu-skills.md) |
| browser-act-skills | 103 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-browser-act-skills.md) |
| bankrbot-skills | 155 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-bankrbot-skills.md) |
| microsoft-skills | 210 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-microsoft-skills.md) |
| voltagent-awesome-openclaw-skills | 0 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-voltagent-awesome-openclaw-skills.md) |
| mengto-skills | 176 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-mengto-skills.md) |
| chalarangelo-30-seconds-of-code | 0 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-chalarangelo-30-seconds-of-code.md) |
| minimax-ai-skills | 23 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-minimax-ai-skills.md) |
| slavingia-skills | 10 | [abrir](https://github.com/paulociano/skill-arsenal/blob/master/evaluations/inventories/2026-10-15-slavingia-skills.md) |

## Catálogos sem SKILL.md local
- VoltAgent: milhares de links externos nas 30 categorias do diretório, não skills residentes em seu repositório. Cada link exige resolução no repositório original e auditoria de fonte, dependências e versão. Não foram inspecionados individualmente nesta rodada.
- 30-seconds-of-code: artigos/snippets, não um catálogo de SKILL.md; tratar como material de aprendizagem/código, com respeito à licença específica.

## Gate individual antes de importar
1. Abrir SKILL.md e referências executadas, identificar objetivo, trigger, técnicas e efeitos.
2. Classificar A/B/C/D em evidência do conteúdo, não só filename.
3. Conferir overlap com owner do índice, incluindo near-miss e valor incremental.
4. Revisar comandos, shell, chaves, redes, permissões, hooks, instalação, persistência e ações externas.
5. Registrar ADOPT/UPDATE_EXISTING/REFERENCE/REJECT, justificativa e validação.
6. Para fintech, carteiras, trading e ações de terceiros, revisão mais rigorosa e nenhuma ação externa durante avaliação.

Este arquivo é um checklist de progresso, não uma afirmação de auditoria exaustiva. Não foram executados scripts ou instaladores externos.

## Continuação registrada em 2026-10-15

- `slavingia/skills`: 10/10 SKILL.md lidos e decisões individuais registradas.
- `antfu/skills`: 11/11 SKILL.md lidos; guias de frameworks e convenções mantidos como referência contextual; não instalar em massa.
- `MiniMax-AI/skills`: 23/23 SKILL.md lidos; ferramentas de API/CLI não portáveis e dependências de mídia identificadas. `shader-dev` permanece candidata a aprofundamento dos arquivos de referência, sem adoção automática.
- `multica-ai/andrej-karpathy-skills`: 1/1 SKILL.md lido; metodologia de código enxuto já coberta pelo Arsenal.
- `browser-act/skills`: 5/103 SKILL.md lidos; dependência do browser-act CLI e de payload dinâmico exige revisão mais profunda, sem execução.

Para as 50 entradas, trata-se de avaliação individual do documento principal e não revisão exaustiva de dependências transitivas. As 1.436 restantes continuam com triagem apenas por nome/caminho. Fontes agregadoras VoltAgent e 30-seconds-of-code permanecem fora desse denominador por não conterem SKILL.md na própria árvore.

## Continuação MengTo (2026-10-15)

19 skills de `MengTo/Skills` lidas individualmente: 16 de 3D (materiais, volumetria, água, texturas, tours, ambientes e performance) e 3 de UI. Decisões documentadas em `evaluations/inventories/2026-10-15-mengto-skills.md`. As duas metodologias anti-clichês de design foram integradas ao owner `design-principles-audit`. Não foram executados shaders, benchmarks nem scripts upstream. Cobertura total: **69/1719**, pendentes **1436**. Em MengTo: **19/176** lidas.

## Continuação MengTo Codex e Workflow (2026-10-15)

24 SKILL.md adicionais (20 Codex + 4 workflow) lidos e avaliados no conteúdo principal. Cobertura acumulada: **93/1719**, pendentes **1436**. MengTo: **43/176**. Owner `design-principles-audit` foi ampliado com auditoria de originalidade referenciada. Não foram auditados scripts auxiliares, builds nem ambientes upstream.

## Continuação MengTo: gameplay e combate (2026-10-15)

26 SKILL.md lidas: 6 `game-combat` + 20 `game-development`; decisão individual registrada em `evaluations/inventories/2026-10-15-mengto-skills.md`. Reaproveitados contratos de combate data-driven, inventário atômico, inimigos e editor de fases no owner `game-development-engineering`. Não houve renderização dos efeitos, build, benchmarks ou validação de jogo real. Cobertura acumulada: **119/1719**; pendentes **1436**; MengTo: **69/176**.

## Continuação MengTo: web design (2026-10-15)

91 arquivos `agent-skills/web-design/*/SKILL.md` abertos e classificados individualmente no inventário MengTo. Classes provisórias por documento principal; não inclui dependências/assets/scripts nem verificação de UI no browser. Atualizado `ui-motion-design` com estados semânticos, visibilidade, ciclo de vida, controle de scroll e orçamento de GPU. Cobertura acumulada: **210/1719**; pendentes **1436**; MengTo **160/176**. Próxima área MengTo: 14 `illustration` e 2 `media`.

## Fechamento da leitura do MengTo (2026-10-15)

16 SKILL.md adicionais de `MengTo/Skills` (14 ilustração SVG, 2 referências a bancos de imagens) abertos individualmente e classificados em `evaluations/inventories/2026-10-15-mengto-skills.md`. Cobertura de documentos principais do MengTo concluída: **176/176**. Cobertura geral: **226/1719**; pendentes **1436**. As referências internas, scripts, ativos e resultados não foram auditados/executados. Estilos específicos permaneceram referências, evitando owners duplicados.

## Continuação Google: Ads, Analytics, Identity e Developers (2026-10-15)

21 SKILL.md abertos e analisados individualmente em `evaluations/inventories/2026-10-15-google-skills.md`, distinguindo leituras/alterações de conta, consentimento, versão SDK e execução externa. Cobertura Google **21/166**; total **247/1719**, pendentes **1436**. Somente documento principal; não executar credenciais, mutações ou scripts do fornecedor durante auditoria.

## Continuação Google Cloud: Agent Platform, BigQuery e infraestrutura (2026-10-15)

24 SKILL.md adicionais do Google Cloud examinados individualmente, com decisões na ficha `evaluations/inventories/2026-10-15-google-skills.md`. Incluem 13 Agent Platform e 11 BigQuery/bancos/infra. Cobertura Google **45/166**; acumulado **271/1719**, pendentes **1436**. Nenhuma operação GCP, uso de credenciais, criação de recursos ou execução de scripts externos. A auditoria de scripts/referências permanece pendente para adoção técnica.

## Continuação Google observabilidade (2026-10-15)

12 SKILL.md de Cloud Logging, Monitoring, Trace e Data Lineage examinados e registrados individualmente em `evaluations/inventories/2026-10-15-google-skills.md`. Cobertura Google **57/166**, total **283/1719**, restantes **1436**. Não executados Terraform, APIs Cloud ou consultas reais. Segurança operacional e scripts auxiliares exigem validação antes de uso.
