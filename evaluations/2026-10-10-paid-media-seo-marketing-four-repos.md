# Avaliação consolidada: anúncios, SEO e marketing (2026-10-10)

## Fontes consultadas (branches main)
- https://github.com/AgriciDaniel/claude-ads — README, `ads/SKILL.md`, `skills/ads-audit/SKILL.md`, diretório skills.
- https://github.com/irinabuht12-oss/marketing-skills — README, 49 pastas em skills, `ai-visibility-audit/SKILL.md`, `wasted-spend-finder/SKILL.md`.
- https://github.com/AgriciDaniel/claude-seo — README, diretório skills, `seo-geo/SKILL.md`.
- https://github.com/onewave-ai/claude-skills — README, catálogo raiz, `competitor-content-analyzer/SKILL.md`.
- Fonte canônica: `ARSENAL INDEX.md`, `stacks/arsenal-autopilot/STACK.md`, `skills/seo-research-audit/SKILL.md`, `skills/skill-security-review/SKILL.md`.

## Capabilities, classificação e decisão
| Fonte | Classe | Ganho material | Decisão |
| --- | --- | --- | --- |
| Claude Ads | A/D | Auditoria de mídia paga por evidências e janela, controle de mudanças e resultados parciais; engines externos não são portáveis | CREATE_NEW: `paid-media-operations` em versão ChatGPT-only |
| Ryze marketing-skills | B/D | Diagnósticos PPC, eficiência de gasto, experimentos, painel AI visibility; Ryze MCP não está presumido instalado | ABSORB_METHOD_ONLY em `paid-media-operations` e `seo-research-audit` |
| Claude SEO | B/D | GEO conectado ao SEO clássico, auditoria de citabilidade com verificação e cautela sobre `llms.txt`; agentes/scripts Claude não portáveis | UPDATE_EXISTING: `seo-research-audit` |
| OneWave claude-skills | C predominante, D em skills agent/runtime | Vasto catálogo, mas exemplo inspecionado de competitor-content-analyzer é prompt genérico e grande sobreposição com skills/stacks existentes | KEEP_EXTERNAL_REFERENCE; não importar em massa |

## Owners e mudanças
- Novo owner: `skills/paid-media-operations/SKILL.md`, com triggers, modelo de métricas, observação vs diagnóstico, comparação por plataforma, dados ausentes, priorização, experimentos e gates de alteração de campanhas.
- Owner atualizado: `skills/seo-research-audit/SKILL.md`, com painel medido e comparável de visibilidade em respostas de IA, lacunas de fontes citadas, limites e anti-hype.
- Índice atualizado: `ARSENAL INDEX.md` com paid-media-operations.
- Não importados: comandos Claude, scripts Python, instaladores shell, benchmarks não validados, agentes paralelos, bibliotecas inteiras, credenciais e integrações de publicidade de terceiros.
- No marketing orgânico, manter `social-growth-engine` e `content-production` como owners.

## Segurança e portabilidade
Veredito **CAUTION** para instalação/execução original: Claude Ads/SEO têm instaladores, dependências externas e caminhos de alteração de contas; Ryze requer um endpoint MCP de terceiro e potencial acesso a contas; OneWave assume ferramentas/agents Claude que não são automaticamente disponíveis no ChatGPT. A inspeção foi estática e amostral; nenhum instalador, conexão, modificação de campanha ou teste de runtime foi executado. A skill adaptada é exclusivamente metodológica, sem autoexecução, com dados não confiáveis, mínima permissão e aprovação para ações externas.

## Prova de valor incremental
- Should trigger: "Tenho CSV das minhas campanhas Meta e Google, encontre gargalos de CPA e proponha realocação segura de verba."
- Near miss: "Faça um post orgânico para Instagram" => `social-growth-engine`, não mídia paga.
- SEO trigger: "Quero medir se minha marca aparece nas respostas de IA" => `seo-research-audit`, sem alegar acesso a sistemas não conectados.
- Aceitação: sem números inventados; separar plataformas e origem/atraso de atribuição; ausência de dados sinalizada; mudanças de campanha ficam no rascunho; resultado de AI visibility limitado a respostas realmente observadas.
