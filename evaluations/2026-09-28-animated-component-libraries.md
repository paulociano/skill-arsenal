# Avaliação — 20 bibliotecas de componentes animados e efeitos

**Data:** 2026-09-28  
**Objetivo:** ampliar o Arsenal com referências de animação, efeitos de superfície e componentes com interação, sem repetir o catálogo já existente.

## Resultado

A pesquisa selecionou 20 referências adicionais e as registrou em `skills/creative-web-effects/references/animated-component-libraries.md`. O lote foi dividido em:

- **8 referências gerais para começar:** Animata, Aceternity UI, Cult UI, Fancy Components, SmoothUI, UI Layouts, Skiper UI e Hover.dev.
- **6 referências de efeitos e superfícies:** ScrollX UI, ParticleUI, Marvelous UI, Canvas UI, Paper Shaders e Aurora.
- **6 referências por stack ou modelo de distribuição:** Vue Bits, Svelte Bits, Svelte Animations, Inspira UI, Motion UI e Myndui.

## Leitura técnica

- **Copiar o código é uma decisão de ownership.** Animata, Cult UI, Fancy, ScrollX UI e vários catálogos shadcn-like favorecem copiar um componente; isso reduz acoplamento, mas transfere manutenção, acessibilidade e atualização para o projeto.
- **Motion não é o efeito.** As referências usam CSS, Motion, GSAP, Canvas, WebGL ou WebGPU em proporções diferentes. Escolher o runtime pelo tipo de movimento e pelo custo da tela.
- **Canvas UI exige cautela.** A própria documentação informa que a maioria das variantes HTML-in-canvas depende de Chrome Origin Trial. Usar apenas em uma superfície experimental, com fallback semântico em HTML.
- **Licença é por item.** Alguns sites misturam código livre, exemplos comunitários e blocos pagos. Confirmar o arquivo de licença e os assets do commit usado antes de incorporar.
- **Catálogos são repertório.** Nenhuma contagem de componentes, claim de acessibilidade ou indicação de “production-ready” foi tratada como teste do Arsenal; o runtime real ainda precisa passar por runtime-ui-verification e web-quality-audit.

## Recomendações práticas

1. Para um hero React com pouco risco, começar por Animata ou Aceternity e extrair apenas um efeito.
2. Para uma identidade mais autoral, comparar Cult UI, SmoothUI e Paper Shaders; limitar a uma assinatura visual.
3. Para Vue/Svelte, usar Vue Bits, Svelte Bits ou Svelte Animations como repertório e verificar dependências originais.
4. Para páginas de marketing com scroll, comparar ScrollX UI, Skiper UI e Motion UI; manter uma versão sem scroll-linked motion.
5. Para shaders, começar por Paper Shaders ou Aurora; deixar Canvas UI para protótipos em que o suporte experimental seja aceitável.
