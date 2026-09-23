---
name: web-design-engineer
description: "Construir ou redesenhar interfaces web com pesquisa, direção, estrutura, interação, motion e efeitos contemporâneos, preservando marca, acessibilidade, performance e verificação em runtime."
---

# web-design-engineer

## Objetivo

Projetar, construir ou redesenhar artefatos visuais para navegador com alto acabamento, tratando pesquisa, direção, estrutura, interação, sistema visual e implementação como um único problema.

## Quando usar

- landing pages, dashboards, protótipos, interfaces, visualizações e experiências web;
- redesign de UI existente;
- HTML/CSS/JS/React com exigência visual alta;
- implementação de uma direção visual já decidida;
- websites contemporâneos com motion, scroll storytelling ou creative graphics.

## Pipeline

Escolha somente as fases necessárias:

1. **Research** — contexto, assets, sistema e referências.
2. **Direction** — design-direction quando a linguagem visual ainda não está resolvida.
3. **Contract** — design-system-extraction/governance quando decisões precisam persistir.
4. **Greybox / structure** — macroestrutura, IA visual, proporções, estados e responsividade.
5. **Build** — conteúdo e interação reais.
6. **Narrative motion** — scroll-storytelling quando scroll participa da experiência.
7. **Motion** — ui-motion-design define paradigma e tecnologia.
8. **Creative layer** — motion-asset-engineering ou creative-web-effects quando necessário.
9. **Polish** — interaction-polish depois de estrutura/conteúdo estabilizados.
10. **Runtime verification** — comportamento, acessibilidade e performance antes de concluir.

Projetos pequenos podem combinar fases. Não escolher efeito antes da estrutura e não confundir polish com redesign.

## Workflow

1. Verificar fatos atuais quando o design depende de produto, marca, SDK ou especificação instável.
2. Ler recursos fornecidos: código, screenshots, brand assets, design system e DESIGN.md/design-system.md.
3. Classificar mudança em extension, preserve ou overhaul.
4. Se direção estiver aberta, executar design-direction ou produzir Design Read equivalente.
5. Declarar visual thesis, paleta, type roles, spacing, radius/depth, layout grammar, motion stance e signature elements.
6. Para página nova/redesign estrutural, fazer greybox com regiões, eixo dominante, densidade, navegação, ritmo, responsive behavior e estados.
7. Construir a experiência completa com conteúdo real ou placeholders claramente marcados.
8. Escolher deliberadamente se a página precisa de:
   - scroll storytelling;
   - motion de interface;
   - asset animado;
   - efeito criativo/procedural;
   - nenhum deles.
9. Aplicar interaction-polish somente depois que a interface já funciona sem os efeitos.
10. Verificar no runtime em viewports/inputs/estados relevantes.
11. Fazer revisão final em brand/system fidelity, context mismatch, interface feel e final QA.
12. Remover efeitos cujo custo, competição ou dependência não justifique benefício.

## Contemporary design sem checklist estético

"Moderno" é uma relação entre conteúdo, estrutura, tecnologia e cultura visual atual. Não impor:
- glassmorphism;
- gradients;
- giant typography;
- bento;
- animated borders;
- smooth scroll;
- WebGL;
- cursor customizado.

Em vez disso, procurar uma assinatura coerente e poucas decisões fortes.

## Research-first sem burocracia

Pesquisa é obrigatória apenas quando reduz incerteza material. Para referências externas:
- preferir produtos reais, fontes oficiais e exemplos atuais;
- extrair estrutura, ritmo, type roles, cor, assets, motion e relações;
- não clonar pixels ou identidade;
- registrar provenance das decisões relevantes.

## Greybox e memória de projeto

Em projetos multi-página, pode ser útil manter documento de páginas/estados com objetivo, hierarquia, assinatura, estado, dependências e motion thesis. Deve complementar, não duplicar, DESIGN.md.

## Regras

- Contexto e assets reais vencem estética genérica.
- Código existente é fonte melhor que screenshot para reconstrução.
- Separar defeito objetivo, context mismatch e preferência estética.
- Números de UI devem ser distinguidos entre standard, spec do projeto e heurística.
- Findings precisam de evidência e correção acionável.
- HTML/semântica não deve ser substituído por Canvas/WebGL quando conteúdo precisa ser acessível, indexável ou selecionável.
- Creative effects são enhancement; a experiência base deve continuar coerente sem eles quando possível.

## Fingerprint estrutural

- escolher macroestrutura antes do tema;
- registrar 2–4 knobs como eixo, densidade, hero/conteúdo, navegação e ritmo;
- preservar copy, IA, constraints e marca antes de trocar estrutura;
- extrair relações de referências, não pixels.

## Especializações sob demanda

- design-direction;
- design-system-extraction / design-system-governance;
- landing-craft;
- scroll-storytelling;
- ui-motion-design;
- interaction-polish;
- motion-asset-engineering;
- creative-web-effects;
- shader-graphics-engineering;
- gsap-animation;
- shadcn-ui-engineering;
- ui-ux-catalog;
- runtime-ui-verification;
- web-quality-audit.

## Evidência dos findings

Antes de reportar finding de UI existente, exigir quando aplicável Contract, Runtime e Correction. Reabrir a fonte e tentar falsificar o finding.

## Ferramentas e dependências

Usar leitura/escrita, browser e terminal realmente disponíveis. Não exigir biblioteca criativa apenas porque uma referência a usa. Verificar versão, licença, custo e stack real antes de integrar.

## Referências

Metodologia de direção visual: Anthropic frontend-design. Macrostructure/fingerprint: Nutlope/hallmark. Pipeline estruturado: Firzus, mblode, dawitlabs e nolly-studio. Creative web routing refinado a partir de Motion, Lenis, r3f-scroll-rig, ecossistema pmndrs, React Bits, Animate UI e Magic UI.

Origem local: web-design-engineer.docx.
