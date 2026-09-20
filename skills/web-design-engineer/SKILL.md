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

[GitHub · ConardLi/garden-skills · web-design-engineer](https://github.com/ConardLi/garden-skills/tree/main/skills/web-design-engineer)

Origem local: [web-design-engineer.docx](../web-design-engineer.docx).
