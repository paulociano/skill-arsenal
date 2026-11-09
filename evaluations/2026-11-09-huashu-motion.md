# huashu-motion (2026-11-09)

## Fonte
- https://github.com/alchaincyf/huashu-motion — commit `52467f9` (2026-10-22), skill `skills/huashu-motion` v0.3.1
- Lidos: `SKILL.md`, `references/director.md`, `references/verification.md`, índice de `references/` (rhythm, colour, sound, music, depth, contract, craft, biblioteca de 20 linguagens de motion) e `bin/om`
- Stack de avaliação: stacks/evaluate-and-import-skill/STACK.md

## O que é
Agent Skill (padrão agentskills.io) para agentes de código produzirem filmes de lançamento de produto, explainers e vinhetas como código: uma composição `index.html` (HTML + GSAP, Canvas, Three.js, SVG) renderizada quadro a quadro no Chrome do usuário. Inclui CLI `om` (captura de material, estúdio local para comentar apontando no quadro, trilha a partir de partitura ABC, voz/TTS, render MP4/MOV/WebM/GIF, checagens de layout e QA de ritmo) e uma biblioteca de 20 linguagens de motion. README em chinês e inglês. MIT, com GSAP sob licença própria, fontes OFL e um personagem reservado.

## Classificação e decisão

| Item | Classe | Decisão |
|---|---|---|
| Método de direção (ler o produto, forma da mensagem → linguagem, personalidade em 5 eixos, três direções com uma em profundidade, tratamento com folha de ritmo/4 stills/cadeia de continuidade, regras de gosto, revisão com "três notas", ajustes por apontamento, aprendizado preferência/observado/verificado) | **B** | ABSORB_METHOD — incorporado em `procedural-film` |
| CLI `om`, estúdio, biblioteca de sons, render | D | NÃO IMPORTAR — runtime externo (Node 22+, Chrome, FFmpeg; testado só em macOS) |
| Biblioteca de 20 linguagens de motion | B/D | REFERÊNCIA — consultar na fonte quando um filme for produzido; não copiada |

Não foi criada skill nova: `procedural-film` já tinha "Product-film mode" (brand-first, claims reais, componentes reais) e o contrato de render determinístico. O valor incremental é a camada de direção, que faltava.

## Sobreposição verificada
- `procedural-film` — owner (render determinístico, beat grid, product-film mode).
- `cinematic-visual-direction` — shot contract e gramática de câmera; complementar.
- `explainer-video-production` — sincronia voz/visual; complementar para filmes narrados.
- `gsap-animation`, `ui-motion-design` — implementação e motion de interface; não substituem a direção.

## Implementado
- `skills/procedural-film/references/launch-film-direction.md` (novo): método completo adaptado, em português.
- `skills/procedural-film/SKILL.md`: seção "Direção de filme de lançamento", description ampliada e provenance.
- `ARSENAL INDEX.md`: description de `procedural-film` atualizada.

## Segurança e portabilidade
Nenhum instalador ou script da fonte foi executado (o repositório foi clonado só para leitura). Pontos de atenção para quem instalar a skill original:
- `bin/om` cai em `npx --yes huashu-motion` quando o CLI local não existe: baixa e executa pacote npm sem confirmação.
- **Assinatura "Made with huashu-motion" ligada por padrão** em filmes de 4 s ou mais; a skill só desliga se o usuário pedir ou em trabalho comissionado. Para entregas a clientes, desligar com `data-om-signature="off"`.
- Checagem de versão periódica via `git ls-remote` (só lê tags; desligável com `off` em `.last-update-check`).
- `om samples build` baixa ~55 MB de samples; TTS opcional baixa modelo de ~325 MB.
- `om studio` sobe servidor em 127.0.0.1 e `om grab` captura telas, que podem expor dados privados.
- Números de "o que funciona" (cortes por minuto, BPM, salvamentos) são medições do próprio autor, não verificadas.

Na adaptação foram removidos: CLI, assinatura, checagem de versão, auto-promoção do autor e dependência de GSAP.

## Limites
Leitura documental dos arquivos da skill; `rhythm.md`, `colour.md`, `sound.md`, `depth.md`, `contract.md` e os 20 arquivos de linguagem foram lidos só nos títulos de seção. Nenhum filme foi produzido para testar o método.

## Aceite futuro
Na primeira vez que o usuário pedir um vídeo de lançamento, aplicar `procedural-film` com a referência nova e registrar se o método produziu filme aprovado em menos rodadas. Se o usuário quiser o pipeline completo (estúdio + trilha + render), instalar a skill original no Claude Code, com a assinatura desligada para trabalho de cliente.
