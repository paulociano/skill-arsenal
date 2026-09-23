---
name: web-design-engineer
description: "Construir ou redesenhar interfaces e artefatos web com pesquisa visual, direção explícita, estrutura, interação, fidelidade à marca e verificação em runtime."
---

# web-design-engineer

## Objetivo

Projetar, construir ou redesenhar artefatos visuais para navegador com alto acabamento, tratando pesquisa, direção, estrutura, interação, sistema visual e implementação como um único problema.

## Quando usar

- landing pages, dashboards, protótipos, interfaces, visualizações e experiências web;
- redesign de UI existente;
- HTML/CSS/JS/React com exigência visual alta;
- implementação de uma direção visual já decidida.

## Pipeline

Escolha somente as fases necessárias ao estado do projeto:

1. **Research** — reunir contexto, assets, design system e referências reais quando a direção depende delas.
2. **Direction** — usar design-direction quando a linguagem visual ainda não está resolvida.
3. **Contract** — usar design-system-extraction/governance quando há sistema existente ou quando decisões precisam persistir.
4. **Greybox / structure** — definir macroestrutura, IA visual, proporções, seções/estados e responsividade sem tentar polir tudo ao mesmo tempo.
5. **Build** — implementar conteúdo e interação reais.
6. **Motion** — usar ui-motion-design; gsap-animation somente quando a complexidade justificar.
7. **Runtime verification** — verificar o artefato renderizado antes de concluir.

Projetos pequenos podem combinar fases. O importante é preservar a ordem lógica: não escolher estilo antes de ler o sistema existente e não confundir polimento com estrutura.

## Workflow

1. Verificar fatos atuais quando o design depende de produto, marca, SDK ou especificação instável.
2. Ler primeiro recursos fornecidos: código, screenshots, brand assets, design system e DESIGN.md/design-system.md.
3. Classificar mudança em extension, preserve ou overhaul.
4. Se direção estiver aberta, executar design-direction ou produzir um Design Read equivalente.
5. Declarar decisões de design: visual thesis, paleta, type roles, spacing, radius/depth, layout grammar, motion stance e signature elements.
6. Para página nova/redesign estrutural, fazer greybox:
   - regiões e hierarquia;
   - eixo dominante;
   - densidade;
   - navegação;
   - ritmo;
   - responsive behavior;
   - loading/empty/error quando aplicável.
7. Construir a experiência completa com conteúdo real ou placeholders claramente marcados.
8. Verificar no runtime em viewports relevantes e nos estados principais.
9. Fazer revisão final em quatro lentes:
   - brand/system fidelity;
   - anti-slop/context mismatch;
   - interface feel;
   - final QA.
10. Corrigir findings evidenciados; não reestilizar por gosto.

## Research-first sem burocracia

Pesquisa é obrigatória apenas quando reduz incerteza material. Em UI existente com sistema claro, ler código/assets pode ser suficiente. Para referências externas:
- preferir produtos reais, fontes oficiais e exemplos atuais;
- extrair estrutura, ritmo, type roles, cor, assets e relações;
- não clonar pixels ou identidade;
- registrar provenance das decisões relevantes.

## Greybox e memória de projeto

Em projetos multi-página, pode ser útil manter um documento de páginas/estados que registre:
- página/superfície;
- objetivo;
- hierarquia;
- assinatura visual;
- estado de implementação;
- dependências;
- motion thesis.

Esse artefato é opcional e deve complementar, não duplicar, DESIGN.md.

## Regras

- Contexto e assets reais vencem estética genérica.
- Logo e imagens reais têm mais valor de reconhecimento que apenas cores.
- Código existente é fonte melhor que screenshot para reconstrução de UI.
- Evitar padrões genéricos de IA quando não servirem ao produto.
- Não chamar algo de AI slop por um padrão isolado; o problema é convergência sem justificativa.
- Separar defeito objetivo, context mismatch e preferência estética.
- Números de UI devem ser distinguidos entre standard, spec do projeto e heurística.
- Findings precisam de evidência e correção acionável.

## Fingerprint estrutural e referências

- escolher macroestrutura coerente com a tarefa antes do tema;
- registrar 2–4 knobs como eixo dominante, densidade, hero/conteúdo, navegação e ritmo;
- em redesign, preservar copy, IA, constraints e marca antes de trocar estrutura;
- em estudo de screenshot/URL, extrair relações, não pixels;
- referência visual é matéria-prima de decisão, não licença para cópia.

## Acessibilidade e motion

- preferir HTML semântico;
- preservar focus, keyboard, accessible names e reduced motion;
- usar ui-motion-design para intenção e gsap-animation para implementação quando necessário;
- não migrar biblioteca sem pedido/necessidade;
- verificar toque, teclado e comportamento sem motion.

## Especializações sob demanda

- design-direction;
- design-system-extraction / design-system-governance;
- landing-craft;
- ui-motion-design;
- gsap-animation;
- shadcn-ui-engineering;
- ui-ux-catalog;
- runtime-ui-verification;
- web-quality-audit.

Carregue somente o necessário.

## Evidência dos findings

Antes de reportar finding de UI existente, exigir quando aplicável:
1. Contract;
2. Runtime;
3. Correction.

Reabrir a fonte e tentar falsificar o finding antes de entregá-lo.

## Ferramentas e dependências

Usar leitura/escrita, browser e terminal realmente disponíveis. Não exigir Claude Code, subagentes ou instaladores externos. Separar inspeção de DOM, evidência visual e estado de aplicação.

## Referências

Metodologia de direção visual: Anthropic frontend-design. Macrostructure/fingerprint: Nutlope/hallmark. Pipeline research → direction → greybox → real content e contratos persistentes adaptado de Firzus/agent-skills, mblode/agent-skills, dawitlabs/ui-skills e nolly-studio/agent-skills, sem importar dependências específicas dos agentes de origem.

Origem local: web-design-engineer.docx.
