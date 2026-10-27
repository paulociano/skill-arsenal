# Avaliação em lote — 10 fontes externas, diagramas, motion e vídeo (2026-10-27)

## Escopo e método

Roteamento: `ARSENAL INDEX.md` → `evaluate-and-import-skill`. Foram lidos os READMEs e a estrutura de pastas de cada repositório e os resultados foram cruzados com `evaluations/` e com os owners existentes. Seis fontes já tinham decisão anterior, que foi mantida. Quatro eram novas. Apenas o SeeCode teve SKILL.md e scripts lidos (auditoria estática); os demais não tiveram código auditado.

## Ledger e decisões

| Fonte | Classe | Decisão | Observação |
|---|---|---|---|
| [devdotfast/whiteboard](https://github.com/devdotfast/whiteboard) | A/D | MANTER decisão de 2026-09-27 (UPDATE_EXISTING em `code-review`) | App desktop com fork do Code OSS; não instalar |
| [axtonliu/axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills) | B/D | KEEP_EXTERNAL_REFERENCE | 3 skills experimentais (Excalidraw, Mermaid, Canvas), baixa manutenção; sobrepõe `obsidian-vault-authoring` e `architecture-visualization`. Ideia aproveitável: lista de prevenção de erros de sintaxe Mermaid |
| [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | B/D | MANTER decisão de 2026-10-13 | Runtime exige Node 22, Chrome, ffmpeg, ElevenLabs; GSAP com licença não aberta |
| [reladraw/reladraw](https://github.com/reladraw/reladraw) | A/B/D | MANTER decisão de 2026-09-27 (absorvido em `architecture-visualization`) | Sintaxe ainda instável (v0.16) |
| [Aryanutkarsh/SeeCode](https://github.com/Aryanutkarsh/SeeCode) | A/D | CANDIDATO A INSTALAÇÃO NO CLAUDE; owner conceitual `interactive-system-diagram` | MIT, v0.6.2. Auditoria estática limpa: sem `eval`, sem exfiltração, `child_process` só para ffmpeg e Chrome (na exportação), rede só Google Fonts, jsDelivr (encoders de GIF/MP4 no navegador) e fetch da URL de marca informada pelo usuário; configuração em `~/.seecode`. Teste de execução feito depois da instalação no Claude: `render` de um sankey a partir de CSV gerou o HTML sem erros (6 nós, 5 fluxos). Valor incremental: gráficos financeiros (sankey, waterfall, barras a partir de CSV) |
| [diffusionstudio/lottie](https://github.com/diffusionstudio/lottie) | A/D | KEEP_EXTERNAL_REFERENCE; ligar a `motion-asset-engineering` | Gera Lottie JSON, o que o owner não faz; exige workspace Vite. Sem caso de uso atual |
| [Remocn/remocn-studio](https://github.com/Remocn/remocn-studio) | A/D | MANTER decisão de 2026-10-06 | Protótipo Tauri só macOS, 11 estrelas |
| [GTKottman/mortiflix-oss](https://github.com/GTKottman/mortiflix-oss) | A/D | MANTER decisão de 2026-10-10 (ABSORB_METHOD_ONLY) | AGPL-3.0; exige Claude Code ou API |
| [ResearAI/AutoFigure-Edit](https://github.com/ResearAI/AutoFigure-Edit) | D | DISCARD como skill; referência para `publication-figure-engineering` | Pipeline Python com SAM3 e API de imagem, cerca de US$ 0,50 por figura; não é skill |
| [alexgreensh/anidoodle](https://github.com/alexgreensh/anidoodle) | A/D | MANTER decisão de 2026-09-27 (UPDATE_EXISTING / KEEP_EXTERNAL_REFERENCE em `procedural-film`) | Pacote de som de 373 MB opcional |

## Pendências

- SeeCode: `render` testado e funcionando; a exportação (SVG/PNG/GIF/MP4) ainda não foi testada.
- Skills do Arsenal que absorveram estas ideias e não estão instaladas no Claude: `architecture-visualization`, `interactive-system-diagram`, `motion-asset-engineering`, `obsidian-vault-authoring`, `procedural-film`.
