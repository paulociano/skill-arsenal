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

## Loop visual sobre código real

Quando a interface já existe e o ambiente permite selecionar/inspecionar elementos do runtime, preferir um loop de edição ancorado no artefato real:
1. identificar o elemento e seu owner no código;
2. capturar intenção visual em termos de layout/tokens/estado, não coordenadas frágeis;
3. produzir uma mudança pequena e revisável;
4. inspecionar diff antes de aplicar quando houver efeito material;
5. validar type/lint/build conforme o projeto;
6. verificar a consequência no render real;
7. manter checkpoint/rollback quando a ferramenta real oferecer.

Visual editor é uma interface sobre o código ou modelo canônico, não uma segunda fonte de verdade. Alterações manuais, de agente e visuais devem convergir para representação diffable/versionável quando possível.

## Design constraints versus design dogma

Fontes externas de UI frequentemente trazem listas rígidas de fontes, spacing, radius, backgrounds ou efeitos proibidos. Tratar essas listas como **estilo/opinião da fonte**, não como defaults universais.

Importar somente quando houver valor metodológico:
- um único objetivo/conversão dominante em landing pages;
- message match entre origem do tráfego e hero;
- prova próxima ao claim;
- visual hierarchy e structural variety;
- contraste e acessibilidade verificáveis;
- prototipagem de variantes quando a direção é incerta;
- preservação do design system real do produto.

Não promover para o Arsenal:
- banimentos universais de fontes ou gradientes;
- escalas fixas de spacing/radius sem vínculo com o sistema real;
- uma única receita de hero ou seção;
- motion obrigatório por estética;
- anti-patterns que sejam apenas preferência pessoal sem evidência contextual.

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

Landing-page strategy e discipline de conversão foram revisadas contra [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills), preservando princípios úteis e rejeitando presets rígidos de tipografia, spacing, radius e estética universal. O catálogo [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills), [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills), [MengTo/Skills](https://github.com/MengTo/Skills) e [jakubkrehel/skills](https://github.com/jakubkrehel/skills) foi tratado como radar de capabilities e overlap, não como fonte para importar catálogos inteiros.

Loop visual↔código, seleção de elemento, diff revisável, checkpoints e validação no render refinados a partir de `onlook-dev/onlook`, `SandeepBaskaran/design-mode`, `Kalmuraee/OpenMagic`, `winchxyz/loupe` e `buildingopen/openpage`. Os produtos/runtimes permanecem referências externas e não são presumidos disponíveis.

Origem local: web-design-engineer.docx.

## Catálogo externo de componentes sob demanda

Quando a tarefa se beneficiar de referências concretas de UI para IA, componentes de aplicação, landing pages ou microinterações, consultar [referências de componentes](references/ui-component-references.md): Beautiful UI, OriginKit, coss ui e Bencho. Selecionar por problema e stack existente; registrar licença/dependências do item e validar a integração. A referência não exige instalar bibliotecas nem copiar catálogos.

## Componentes animados e efeitos

Para referências de landing pages, motion e efeitos de superfície, consultar [bibliotecas de componentes animados e efeitos](../creative-web-effects/references/animated-component-libraries.md). Reutilizar somente padrões compatíveis com a arquitetura, acessibilidade e licença do projeto.

## Resizable workspace panels

Quando dashboards, IDEs ou workspaces usarem painéis redimensionáveis:
- separar engine de resizing da camada visual/framework;
- medir o espaço real disponível em vez de assumir a largura total do container;
- suportar min/max, pixel e percentage sizes quando isso corresponder ao produto;
- folding/collapse/snap devem animar o layout real, não apenas aplicar opacity/transform decorativo;
- nesting, reordering e separator intersections precisam de regras explícitas;
- keyboard e RTL continuam requisitos de interação;
- motion deve preservar previsibilidade durante resize, não competir com o controle do usuário.

Padrão refinado a partir de letstri/motion-panels, sem exigir Motion ou React.

## Produtos e runtimes como referência

Quando o projeto exigir editor Office embutido, conhecimento documental, CRM WhatsApp, visualização geográfica ou agentes de equipe, consultar [produtos web e limites de integração](references/office-knowledge-agent-products.md). Distinguir componente, produto completo e serviço externo; escolher somente quando o requisito justificar operação, licenças e dependências.

## Projetos HTML e CSS

Para páginas estáticas, HTML único, componentes sem framework JS e efeitos CSS, consultar [referências HTML/CSS](references/html-css-component-references.md). Diferenciar snippets, tokens, frameworks, temas e dependências de build; preservar a stack existente e validar comportamento além da aparência.

## Pesquisa visual e templates

Para referências como Dribbble, Canva, galerias de sites e fluxos de apps, consultar [bibliotecas de referências de design](../design-direction/references/design-reference-libraries.md). Extrair estrutura e comportamento conforme design-direction; usar o catálogo HTML/CSS para implementação quando essa for a stack do projeto.