# Avaliação individual de skills externas — rastreador de cobertura

Data: 2026-10-15. **Estado: PARCIAL, não concluído.**

## Inventário com fonte verificável
Foram localizados **1719** SKILL.md nas árvores recursivas dos 12 repositórios e criadas fichas **individuais de descoberta** por caminho. **50 skills** tiveram seus SKILL.md abertos e decisões documentais individuais registradas: 10 slavingia, 11 antfu, 23 MiniMax, 1 multica/Karpathy e 5 BrowserAct. **1669** permanecem sem leitura individual de SKILL.md. A leitura das 50 não equivale a auditoria integral dos arquivos associados, scripts, referências e execução; a segurança permanece condicionada a revisão por adoção. Nas fichas, flags baseadas somente no caminho são **hipóteses**, não aprovação nem decisão real.

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

Para as 50 entradas, trata-se de avaliação individual do documento principal e não revisão exaustiva de dependências transitivas. As 1.669 restantes continuam com triagem apenas por nome/caminho. Fontes agregadoras VoltAgent e 30-seconds-of-code permanecem fora desse denominador por não conterem SKILL.md na própria árvore.
