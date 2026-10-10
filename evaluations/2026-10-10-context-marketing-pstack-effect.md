# Avaliação de lote — 2026-10-10 — context-mode, marketingskills, pstack-claude, Effect

## Escopo
Comparação com o `ARSENAL INDEX.md` e `stacks/arsenal-autopilot/STACK.md` canônicos. Leitura dos README atuais das quatro fontes, com aprofundamento nos owners existentes relevantes. Não foram executados scripts, hooks, servidores ou testes de runtime.

| Fonte | Classe | O que oferece | Decisão / ownership |
| --- | --- | --- | --- |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | B/D | MCP local que isola outputs volumosos, executa filtros próximos da fonte e preserva eventos em SQLite/FTS5; hooks específicos de hosts | UPDATE_EXISTING `response-latency-optimization`: incluir processamento próximo da fonte, evidência rastreável, continuidade sem suposição de hooks. Não instalar servidor, capturar transcrições ou alegar MCP disponível |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | A/B | Coleção ampla de skills em SEO, CRO, pricing, copy, growth, onboarding, research e integrações; contexto de product marketing como base | KEEP_EXTERNAL_REFERENCE / ABSORB_METHOD_ONLY quando tarefas futuras exigirem especialização. Arsenal já possui owners para SEO, growth, content, pricing/marketing correlato, pesquisa e experimentação. Não copiar catálogo nem recomendações comerciais/parceiros |
| [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude) | B/D | Orquestrador `poteto-mode` e playbooks de depuração, arquitetura, agente/revisão/verificação; depende de hooks, plugins e subagentes de harness específico | KEEP_EXTERNAL_REFERENCE: `software-engineering-cycle`, `debug-and-fix`, `code-review`, `arsenal-router` já têm propriedade funcional. Não instalar hooks nem replicar comandos inexistentes |
| [Effect-TS/effect](https://github.com/Effect-TS/effect) | D | Framework TypeScript 4.x LTS com erros tipados, DI, concorrência estruturada, scheduling, tracing e schema; exige TS strict e runtime compatível | KEEP_EXTERNAL_REFERENCE: escolha tecnológica dentro de `software-engineering-cycle` e arquitetura de serviços, não uma skill autônoma; recomendações condicionais à versão e projeto |

## Gates de segurança e portabilidade
- `context-mode`: licença ELv2 informada no README, requer verificação de obrigações antes de reutilização de código. Dados brutos locais e históricos de sessão exigem autorização, redaction, retenção e fronteiras de trust.
- `marketingskills`: fontes de marketing podem sugerir ferramentas parceiras ou integrações autenticadas; manter análise independente, acesso mínimo e ações externas com autorização.
- `pstack-claude`: hooks, modelos específicos, agentes paralelos, scripts e leitura de transcripts são exclusivos dos hosts compatíveis. Não alegar que tais componentes rodam dentro deste ChatGPT.
- `Effect`: não adicionar uma biblioteca de runtime a projetos automaticamente; considerar complexidade, compatibilidade com Effect 4.x e risco de migração.
- Não há auditoria completa de dependências, execução, benchmark ou validação de segurança dinâmica.

## Prova de valor incremental
`response-latency-optimization` ganhou procedimento explícito para análise local com filtragem e proveniência, em contraste com apenas reduzir round trips. Should-trigger: análise de grande volume de logs. Near-miss: pergunta simples. Não houve justificativa para novas skills, stacks ou mudança do índice.

## Resultado
Um owner existente atualizado e três fontes mantidas como referências técnicas/metodológicas, sem cópia indiscriminada. Avaliação baseada na documentação dos projetos; capacidades externas não estão instaladas nem testadas.
