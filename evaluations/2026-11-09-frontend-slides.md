# frontend-slides (2026-11-09)

## Fonte
- https://github.com/zarazhangrui/frontend-slides — commit `9906a34` (2026-06-23), MIT
- Lidos: `README.md`, `SKILL.md` (fases 0–6), lista de arquivos (STYLE_PRESETS.md, viewport-base.css, html-template.md, animation-patterns.md, bold-template-pack com ~20 templates, scripts de PPTX, PDF e deploy)
- Stack de avaliação: stacks/evaluate-and-import-skill/STACK.md

## O que é
Skill/plugin do Claude Code para criar apresentações HTML de arquivo único (CSS/JS inline, sem build) do zero, convertendo PPTX ou melhorando um deck existente. Diferenciais: descoberta de estilo por três prévias visuais, modo de densidade (falado vs. leitura), palco fixo 1920×1080 escalado, regras anti-"AI slop", pacote opcional de templates ousados com carregamento progressivo, edição de texto inline, export para PDF e deploy no Vercel.

## Classificação e decisão
| Item | Classe | Decisão |
|---|---|---|
| Método: perguntas em uma rodada com modo de densidade, imagens antes do roteiro, três prévias reais (segura/ousada/curinga) com regras de autenticidade, palco fixo 16:9, regras de edição de deck existente, verificação de sobreposição por screenshot, conversão de PPTX | **B** | ABSORB_METHOD — incorporado em `web-video-presentation` |
| Template pack, presets, scripts (PPTX, PDF, deploy Vercel) | D | NÃO IMPORTAR — assets e runtime externos |

## Sobreposição verificada
- `web-video-presentation` — owner de apresentações HTML; já tinha preview obrigatório e alerta de overflow, mas não descoberta visual de estilo, modo de densidade, palco fixo nem regras de edição.
- `presentation-template-adaptation`, `cinematic-presentation`, `stacks/research-to-presentation` — complementares; sem mudança.
- A linha existente "1920×1080 são escolhas do Open Slide, não regras universais" continua válida: o palco fixo entrou como padrão recomendado para decks, com exceção explícita para páginas de leitura.

## Implementado
- `skills/web-video-presentation/SKILL.md`: seção "Deck HTML de arquivo único com descoberta visual de estilo".

## Segurança
Nada executado. Para quem instalar o original: `deploy.sh` publica no Vercel (exige conta e login; o deck vira URL pública), `extract-pptx.py` requer `python-pptx`, e o plugin é instalado por marketplace do Claude Code a partir do GitHub.

## Limites
Não lidos: `html-template.md`, `animation-patterns.md`, `STYLE_PRESETS.md` e os templates. Nenhum deck gerado para teste.
