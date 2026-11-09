# reanimate (2026-11-09)

## Fonte
- https://github.com/NiazMorshed2007/reanimate — commit `3f7a55a` (2026-10-31)
- Lidos: `README.md`, `skills/reanimate/SKILL.md`, `references/analysis.md`, `references/verify.md`, `scripts/setup.sh`; índice de `capture.md`, `implementation.md` e `webgl.md`
- Stack de avaliação: stacks/evaluate-and-import-skill/STACK.md

## O que é
Skill do Claude Code (padrão Agent Skills) que clona uma seção, widget ou animação a partir de um site, gravação de tela, vídeo, GIF ou Lottie, e prova o resultado: grava a referência quadro a quadro, escreve uma especificação de movimento, implementa na stack do projeto, grava o clone do mesmo jeito e compara tempos, curvas de easing e pixels em rodadas até passar. Para canvas/WebGL/WebGPU/three.js, rastreia shaders, uniforms e grafo de cena num relógio virtual que torna as capturas idênticas. Exemplos publicados com clones de Vercel, Stripe, Clerk, Resend e outros, com métricas. MIT.

## Classificação e decisão

| Item | Classe | Decisão |
|---|---|---|
| Método: níveis de fidelidade, captura em condições idênticas, especificação de movimento com origem dos números, tabela de padrões, critérios de aprovação, tabela sintoma → causa, regra de parada e relatório com residuais | **A/B** | ABSORB_METHOD — incorporado em `ui-motion-design` |
| Scripts de captura, comparação, ajuste de easing e rastreio GL | D | NÃO IMPORTAR — runtime externo (Bun, Playwright/Chromium, ffmpeg estático, ~250 MB) |

Nenhum owner do Arsenal cobria "reproduzir um movimento existente com verificação medida". `ui-motion-design` cobre função, timing e custo do motion e tinha vocabulário por demonstração (motion-prompt), mas não o ciclo captura → especificação → comparação. Preferido enriquecer a skill a criar uma nova.

## Sobreposição verificada
- `ui-motion-design` — owner.
- `gsap-animation`, `motion-asset-engineering`, `interaction-polish` — implementação; sem mudança.
- `runtime-ui-verification` — verificação de UI em runtime; complementar.
- `stacks/clean-room-product-reconstruction` — rota para reconstruir produtos inteiros de terceiros, citada na regra de direitos.

## Implementado
- `skills/ui-motion-design/references/reference-motion-reconstruction.md` (novo): método completo adaptado, em português.
- `skills/ui-motion-design/SKILL.md`: seção "Reconstrução de motion a partir de referência".
- `ARSENAL INDEX.md`: sem mudança (description do owner não mudou materialmente).

## Segurança e portabilidade
Nenhum script foi executado (clonado só para leitura). `setup.sh` roda `bun install` e, se faltar, `bunx playwright install chromium`; é idempotente e não faz nada além disso. Pontos para quem instalar a skill original: baixa ~250 MB (Chromium + ffmpeg); grava sites de terceiros em headless (respeitar termos de uso); testado só no Claude Code, em macOS/Linux. O README alerta corretamente que fontes, imagens e código de outros sites continuam de seus donos.

## Limites
Leitura documental; os scripts TypeScript não foram lidos por inteiro nem executados. Nenhuma animação foi clonada para testar o método.

## Aceite futuro
Na primeira vez que o usuário pedir para reproduzir uma animação de referência (ex.: nos jogos ou em landing pages), aplicar `ui-motion-design` com a referência nova. Se quiser a captura e a comparação automáticas, instalar a skill original no Claude Code: `npx skills add NiazMorshed2007/reanimate -g -a claude-code` (exige Bun 1.1+).
