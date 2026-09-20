---
name: web-design-engineer
description: "Construir ou redesenhar interfaces e artefatos web com direção visual, interação, fidelidade à marca e verificação em runtime."
---

# web-design-engineer

## Objetivo

Projetar, construir ou redesenhar artefatos visuais para navegador com nível alto de acabamento, tratando design, interação, sistema visual e implementação como um único problema.

## Quando usar

- landing pages, dashboards, protótipos, interfaces, visualizações e experiências web;
- redesign de UI existente;
- HTML/CSS/JS/React com exigência visual alta;
- exploração de design system ou direção visual.

## Workflow

1. Verificar fatos atuais quando o design depende de produto, marca, SDK ou especificação instável.
2. Ler primeiro os recursos fornecidos pelo usuário: código, screenshots, brand assets, design system.
3. Classificar mudanças em UI existente como `extension`, `preserve` ou `overhaul`.
4. Produzir um **Design Read** com artefato, público, linguagem visual e cinco dials: variância visual, movimento, densidade, dependência de assets e fidelidade de marca.
5. Antes de codar, declarar decisões de design: paleta, tipografia, spacing, radius, shadow, motion e referência visual.
6. Quando a tarefa for longa e permitir iteração, mostrar uma direção/v0 cedo para reduzir retrabalho. Não impor checkpoints extras quando o pedido já estiver suficientemente determinado ou quando regras superiores exigirem execução direta.
7. Construir a experiência completa.
8. Fazer revisão final em quatro lentes complementares:
- **brand/system fidelity:** aderência a tokens, tipografia, spacing, estados e contratos;
- **anti-slop:** detectar clusters de padrões genéricos sem contexto, sem condenar isoladamente cards, gradients ou estilos específicos;
- **interface feel:** motion, target size, contraste, CLS, focus, reduced motion, response time e demais detalhes mensuráveis, distinguindo spec de preferência;
- **final QA:** evidência concreta para acessibilidade, responsividade, links/assets e comportamento antes de chamar o artefato de pronto.

## Regras

- Contexto e assets reais vencem estética genérica.
- Logo e imagens reais têm mais valor de reconhecimento que apenas cores.
- Não substituir assets de marca por silhuetas genéricas quando a fidelidade importa.
- Código existente é fonte melhor que screenshot para reconstrução de UI.
- Evitar padrões visuais genéricos de IA quando não servirem ao produto.
- Não chamar algo de `AI slop` por causa de uma cor, radius, card ou gradient isolado; o problema é a convergência de padrões sem justificativa de produto.
- Separar **defeito objetivo** (acessibilidade, overflow, estado ausente), **slop/context mismatch** e **preferência estética**.
- Quando usar números de UI, distinguir especificação/standard de convenção ou heurística; não vender opinião como regra normativa.
- Findings de revisão devem trazer evidência e correção acionável, não apenas `looks good` ou score de gosto.

## Direção visual e escrita de interface

Antes de implementar, revise o plano visual contra o produto, público e tarefa principal. Se a mesma composição pudesse servir a qualquer produto apenas trocando o nome, refine a escolha pouco específica. Preserve a direção explícita do usuário e o sistema existente; cores, cards e famílias tipográficas não são proibidos por si só.

- Concentre a expressão visual em um elemento memorável quando isso servir ao objetivo; retire decoração que compete com a tarefa.
- Use numeração para sequências reais e divisores/rótulos para relações informativas, não para preencher espaço.
- Diferencie movimento que responde a uma ação de movimento automático. Dê propósito ao segundo e evite repetir entradas em todas as seções.
- Nomeie ações pelo efeito que o usuário entende. Mantenha o mesmo vocabulário entre botão, confirmação e estado final.
- Em erros, explique a causa conhecida e a recuperação possível; em estados vazios, ofereça uma próxima ação concreta.
- Revise screenshots quando houver navegador disponível; não transforme a revisão em checkpoint de aprovação desnecessário.

## Estrutura antes do tema

Para páginas novas ou redesign com mudança de composição, use [seleção de estrutura e escopo](references/structure-first-design.md) quando houver risco de repetir a mesma página apenas trocando cores. Para componente isolado, preserve a estrutura da página e o sistema existente.

## Referências visuais sob demanda

Estas referências refinam uma direção já indicada pelo briefing; não são padrões para toda interface.

- [Brutalismo industrial](references/industrial-brutalist-ui.md): quando o pedido ou referência pede linguagem industrial, impressão suíça, blueprint ou terminal tático. Não acionar apenas porque o produto é um dashboard.
- [Interfaces imersivas](references/immersive-ui.md): quando a tarefa pede experiência cinematográfica, portfolio interativo ou movimento expressivo. Escolher efeitos por função e validar comportamento com toque, teclado e movimento reduzido.

Leia somente a referência pertinente; nenhuma exige instalar bibliotecas ou reconstruir o sistema do projeto.

## Especializações sob demanda

- `shadcn-ui-engineering`: quando o projeto usa shadcn e a tarefa exige composição, atualização ou diagnóstico dos componentes.
- `ui-ux-catalog`: quando faltam referências de paleta, tipografia ou padrões e consultar um catálogo agregaria valor.
- `gsap-animation`: quando GSAP já é usado ou a complexidade de animação justifica sua adoção no escopo autorizado.

Carregue somente a especialização necessária. Direção de marca e comportamento do produto prevalecem sobre presets.

## Evidência dos findings de UI

Antes de reportar um finding de UI existente, separar candidato de finding e exigir, quando aplicável:

1. **Contract** — regra de design vinculante ou contradição real na experiência.
2. **Runtime** — prova de que o token/componente/owner citado realmente chega à superfície afetada.
3. **Correction** — uma correção determinada pela evidência, não uma preferência inventada.

Reabrir a fonte e tentar falsificar o finding antes de entregá-lo. Repetição, proximidade de arquivos ou "parece inconsistente" geram candidatos, não prova.

### Acessibilidade e motion

- preferir semântica HTML nativa antes de ARIA;
- preservar focus, keyboard, accessible names e reduced motion;
- para motion, preferir transform/opacity; evitar layout thrash, polling de scroll e loops sem stop condition;
- não migrar biblioteca de UI/animação sem pedido explícito;
- heurísticas numéricas continuam heurísticas, não standards universais.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Para páginas web, usar o navegador controlável disponível e sua API documentada; separar inspeção de DOM, evidência visual e estado de aplicação. Controle de navegador não implica controle de aplicativos nativos ou dispositivos móveis. Usar stack e assets do projeto; consultar as skills específicas de framework quando contribuírem. Não exigir Claude Code ou subagentes.

## Referências

Metodologia de direção visual consultada: [Anthropic · frontend-design](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md). Síntese própria, sem importar persona, proibições estéticas universais ou dependências do agente original.

[GitHub · ConardLi/garden-skills · web-design-engineer](https://github.com/ConardLi/garden-skills/tree/main/skills/web-design-engineer)

Origem local: [web-design-engineer.docx](../web-design-engineer.docx).
