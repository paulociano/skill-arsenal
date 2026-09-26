# Skill Arsenal

Biblioteca operacional de skills, métodos e stacks reutilizáveis para pesquisa, escrita, design, desenvolvimento, análise e gestão.

**115 skills · 12 stacks** — catálogo conferido em 26/09/2026.

O [repositório no GitHub](https://github.com/paulociano/skill-arsenal) é a fonte oficial. Para selecionar o recurso adequado a uma tarefa, comece pelo [ARSENAL INDEX.md](https://github.com/paulociano/skill-arsenal/blob/master/ARSENAL%20INDEX.md) e consulte as instruções completas somente das skills ou stacks necessárias.

## Navegação

- [Como usar](#como-usar)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Todas as skills](#todas-as-skills)
- [Stacks disponíveis](#stacks-disponíveis)
- [Avaliação de novas skills](#avaliação-de-novas-skills)
- [Manutenção do catálogo](#manutenção-do-catálogo)

## Como usar

| Comando | Resultado esperado |
| --- | --- |
| `arsenal: <tarefa>` | Consulta o índice e seleciona a menor combinação útil de skills ou stacks. |
| `use <skill>: <tarefa>` | Aplica a skill indicada. |
| `use <stack>: <tarefa>` | Aplica o fluxo indicado, carregando apenas as skills necessárias. |
| `avaliar skill: <url>` | Analisa uma fonte externa, compara com o Arsenal e avalia sua utilidade e adaptação. |

Exemplos:

```text
arsenal: melhore a interface deste site preservando as funcionalidades
use writing-quality: revise este texto mantendo o significado e a voz
use research-and-synthesize: pesquise o tema e produza uma síntese com fontes
avaliar skill: https://github.com/organizacao/repositorio
```

Uma **skill** descreve uma competência ou método reutilizável. Uma **stack** organiza um fluxo que pode combinar várias competências. Stacks são uma convenção do Arsenal, não Agent Skills nativas.

Os arquivos orientam a execução; ferramentas, scripts e integrações precisam estar realmente disponíveis no ambiente. Leia o `SKILL.md` ou `STACK.md` selecionado antes de executar o trabalho.

## Estrutura do repositório

| Caminho | Conteúdo |
| --- | --- |
| [ARSENAL INDEX.md](https://github.com/paulociano/skill-arsenal/blob/master/ARSENAL%20INDEX.md) | Índice de nomes e descrições para roteamento. |
| [AGENTS.md](https://github.com/paulociano/skill-arsenal/blob/master/AGENTS.md) | Regras de operação, portabilidade e manutenção do Arsenal. |
| [skills/](https://github.com/paulociano/skill-arsenal/tree/master/skills) | Competências individuais em `skills/<nome>/SKILL.md`, com referências e outros recursos quando existentes. |
| [stacks/](https://github.com/paulociano/skill-arsenal/tree/master/stacks) | Fluxos compostos em `stacks/<nome>/STACK.md`. |
| [evaluations/](https://github.com/paulociano/skill-arsenal/tree/master/evaluations) | Avaliações e decisões sobre fontes externas. |

## Todas as skills

As 115 skills abaixo estão em ordem alfabética. Cada nome abre suas instruções completas; as descrições vêm do índice oficial.

| Skill | Para que serve |
| --- | --- |
| [3gpp-standards-research](https://github.com/paulociano/skill-arsenal/blob/master/skills/3gpp-standards-research/SKILL.md) | Pesquisar padrões celulares 3GPP, protocolos e evolução de releases com TS/TR e status normativo verificáveis. |
| [academic-paper-orchestration](https://github.com/paulociano/skill-arsenal/blob/master/skills/academic-paper-orchestration/SKILL.md) | Estruturar e revisar manuscritos acadêmicos a partir de pesquisa real, verificando claims, resultados, figuras e citações. |
| [after-action-review](https://github.com/paulociano/skill-arsenal/blob/master/skills/after-action-review/SKILL.md) | Conduzir retrospectivas e postmortems de eventos ou projetos concluídos, ligando causas e impacto a ações verificáveis. |
| [agenda-operations](https://github.com/paulociano/skill-arsenal/blob/master/skills/agenda-operations/SKILL.md) | Auditar e operar a agenda por capacidade, preparação, conflitos, dívida de reuniões e blocos de foco, propondo alterações seguras antes de executar mudanças. |
| [architecture-visualization](https://github.com/paulociano/skill-arsenal/blob/master/skills/architecture-visualization/SKILL.md) | Criar diagramas de arquitetura, sequência, estados e fluxos a partir de descrições ou código com topologia rastreável. |
| [arsenal-router](https://github.com/paulociano/skill-arsenal/blob/master/skills/arsenal-router/SKILL.md) | Seleciona e orquestra a menor combinação necessária de skills e stacks do Skill Arsenal. |
| [beautiful-web-article](https://github.com/paulociano/skill-arsenal/blob/master/skills/beautiful-web-article/SKILL.md) | Transformar fontes fornecidas em artigos ou páginas editoriais HTML legíveis, explicativamente bem estruturados e fiéis ao conteúdo. |
| [brand-logo-exploration](https://github.com/paulociano/skill-arsenal/blob/master/skills/brand-logo-exploration/SKILL.md) | Explorar conceitos de logo e identidade, testar escala e monocromia e refinar a direção escolhida. |
| [call-evaluation](https://github.com/paulociano/skill-arsenal/blob/master/skills/call-evaluation/SKILL.md) | Avaliar ligações comerciais de consultoria financeira pelo Card de Ligação, com evidências, rubrica e qualidade do agendamento. |
| [code-review](https://github.com/paulociano/skill-arsenal/blob/master/skills/code-review/SKILL.md) | Revisar mudanças de código e feedback de PR separando conformidade com padrões, fidelidade à spec e impacto real. |
| [code-understanding-audit](https://github.com/paulociano/skill-arsenal/blob/master/skills/code-understanding-audit/SKILL.md) | Explicar código ou auditar decisões arquiteturais com evidências, ajustando profundidade ao conhecimento do leitor. |
| [codex-cost-efficiency](https://github.com/paulociano/skill-arsenal/blob/master/skills/codex-cost-efficiency/SKILL.md) | Reduzir tokens e gasto em tarefas de desenvolvimento no Codex por medição, leitura seletiva, controle de saída e comparação de tarefas concluídas. |
| [compose-performance-audit](https://github.com/paulociano/skill-arsenal/blob/master/skills/compose-performance-audit/SKILL.md) | Auditar desempenho de Jetpack Compose com baseline, diagnóstico, correção e comparação de métricas antes e depois. |
| [content-matrix](https://github.com/paulociano/skill-arsenal/blob/master/skills/content-matrix/SKILL.md) | Gerar ideias específicas de posts cruzando pilares editoriais com formatos e selecionando oportunidades sustentadas. |
| [creative-web-effects](https://github.com/paulociano/skill-arsenal/blob/master/skills/creative-web-effects/SKILL.md) | Selecionar e integrar efeitos visuais contemporâneos para web como shaders, texturas, partículas, pós-processamento, WebGL e backgrounds procedurais sem sacrificar legibilidade ou performance. |
| [crossplatform-mobile-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/crossplatform-mobile-engineering/SKILL.md) | Implementar ou revisar apps Flutter e React Native/Expo respeitando versões, comportamento nativo e testes por plataforma. |
| [customer-interview](https://github.com/paulociano/skill-arsenal/blob/master/skills/customer-interview/SKILL.md) | Preparar e analisar entrevistas de descoberta focadas em comportamento passado, dor, alternativas e compromissos reais. |
| [dashboard-design](https://github.com/paulociano/skill-arsenal/blob/master/skills/dashboard-design/SKILL.md) | Projetar dashboards e sistemas de gestão à vista orientados a decisão, exceção e ação, com métricas confiáveis, ownership, cadência, comparação e hierarquia operacional. |
| [decision-analysis](https://github.com/paulociano/skill-arsenal/blob/master/skills/decision-analysis/SKILL.md) | Estruturar decisões complexas com alternativas, critérios, incerteza, trade-offs, reversibilidade e sensibilidade sem esconder julgamento humano em uma pontuação arbitrária. |
| [deep-grill](https://github.com/paulociano/skill-arsenal/blob/master/skills/deep-grill/SKILL.md) | Conduzir entrevistas aprofundadas sobre planos ou decisões, resolvendo uma árvore de ambiguidades em rodadas sucessivas. |
| [design-direction](https://github.com/paulociano/skill-arsenal/blob/master/skills/design-direction/SKILL.md) | Transformar um briefing visual vago em uma direção de design explícita, específica ao produto e reutilizável antes da implementação. |
| [design-system-extraction](https://github.com/paulociano/skill-arsenal/blob/master/skills/design-system-extraction/SKILL.md) | Extrair tokens, componentes e padrões visuais de sites ou código, separando valores observados de decisões derivadas e podendo materializar um contrato DESIGN.md. |
| [design-system-governance](https://github.com/paulociano/skill-arsenal/blob/master/skills/design-system-governance/SKILL.md) | Criar ou evoluir design systems rastreando princípios, decisões, tokens, contratos de componentes, implementação e um contrato DESIGN.md quando útil. |
| [diagnosing-bugs](https://github.com/paulociano/skill-arsenal/blob/master/skills/diagnosing-bugs/SKILL.md) | Diagnosticar bugs difíceis e regressões com reprodução mínima, hipóteses falsificáveis e teste da correção. |
| [discovery-research-synthesis](https://github.com/paulociano/skill-arsenal/blob/master/skills/discovery-research-synthesis/SKILL.md) | Sintetizar entrevistas, tickets e pesquisas em padrões, contradições e decisões com evidência rastreável. |
| [document-extraction-pipeline](https://github.com/paulociano/skill-arsenal/blob/master/skills/document-extraction-pipeline/SKILL.md) | Converter documentos complexos em conteúdo estruturado, usando extração textual primeiro e OCR seletivo quando necessário. |
| [editable-visual-design](https://github.com/paulociano/skill-arsenal/blob/master/skills/editable-visual-design/SKILL.md) | Criar pôsteres, infográficos, capas, banners e social cards editáveis com hierarquia, composição tipográfica, assets rastreáveis e revisão visual do render. |
| [eli5](https://github.com/paulociano/skill-arsenal/blob/master/skills/eli5/SKILL.md) | Explicar conceitos a um público específico com linguagem, analogias, exemplos e profundidade adequadas, sem infantilizar. |
| [email-campaign-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/email-campaign-engineering/SKILL.md) | Planejar e construir campanhas de e-mail HTML com copy, assets, compatibilidade e verificação antes do envio autorizado. |
| [empirical-prompt-tuning](https://github.com/paulociano/skill-arsenal/blob/master/skills/empirical-prompt-tuning/SKILL.md) | Avaliar e melhorar prompts ou skills mediante pedido de otimização empírica, com cenários fixos, baseline e holdout. |
| [experiment-design](https://github.com/paulociano/skill-arsenal/blob/master/skills/experiment-design/SKILL.md) | Desenhar experimentos falsificáveis com hipótese, métrica primária, guardrails e critérios de decisão anteriores aos resultados. |
| [explanation-architecture](https://github.com/paulociano/skill-arsenal/blob/master/skills/explanation-architecture/SKILL.md) | Escolher e estruturar a forma certa de explicar um assunto entre tutorial, how-to, explanation e reference, ajustando sequência, exemplos e profundidade ao objetivo do leitor. |
| [formal-methods-reconciler](https://github.com/paulociano/skill-arsenal/blob/master/skills/formal-methods-reconciler/SKILL.md) | Traduzir dúvidas críticas de correção de software em modelos mínimos verificáveis e interpretar provas ou contraexemplos. |
| [founder-diagnose](https://github.com/paulociano/skill-arsenal/blob/master/skills/founder-diagnose/SKILL.md) | Diagnosticar gargalos de startups em produto, mercado, posicionamento, distribuição ou monetização antes de escolher uma intervenção. |
| [golden-circle-feedback](https://github.com/paulociano/skill-arsenal/blob/master/skills/golden-circle-feedback/SKILL.md) | Redigir feedback comportamental usando POR QUÊ, COMO e O QUÊ, com propósito, fatos observáveis e próxima ação. |
| [graph-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/graph-engineering/SKILL.md) | Modelar workflows com dependências e paralelismo reais como grafos limitados, com contratos de saída, joins e recuperação local. |
| [gsap-animation](https://github.com/paulociano/skill-arsenal/blob/master/skills/gsap-animation/SKILL.md) | Implementar e revisar animações GSAP com timelines, ScrollTrigger, matchMedia, performance e integração ao ciclo de vida, preservando acessibilidade e limpeza. |
| [handoff](https://github.com/paulociano/skill-arsenal/blob/master/skills/handoff/SKILL.md) | Preparar contexto compacto para continuar uma tarefa em outra sessão ou obter comparação independente ou crítica. |
| [idea-refine](https://github.com/paulociano/skill-arsenal/blob/master/skills/idea-refine/SKILL.md) | Refinar ideias vagas, explorar alternativas, testar premissas e definir uma direção e escopo de MVP. |
| [instagram-growth-diagnostics](https://github.com/paulociano/skill-arsenal/blob/master/skills/instagram-growth-diagnostics/SKILL.md) | Diagnosticar onde o crescimento de um perfil do Instagram está travado usando métricas disponíveis e rotear o gargalo para a intervenção adequada. |
| [interaction-polish](https://github.com/paulociano/skill-arsenal/blob/master/skills/interaction-polish/SKILL.md) | Refinar o último nível de qualidade de uma interface por microinterações, feedback, estados, tipografia animada e comportamento contextual sem transformar polish em decoração excessiva. |
| [jtbd-framing](https://github.com/paulociano/skill-arsenal/blob/master/skills/jtbd-framing/SKILL.md) | Reformular decisões de produto por Jobs-to-be-Done, situações reais, dificuldades e critérios de adoção ou abandono. |
| [kb-retriever](https://github.com/paulociano/skill-arsenal/blob/master/skills/kb-retriever/SKILL.md) | Responder perguntas em bases documentais grandes por busca progressiva, leitura localizada e citações rastreáveis. |
| [landing-craft](https://github.com/paulociano/skill-arsenal/blob/master/skills/landing-craft/SKILL.md) | Projetar landing pages como narrativas de scroll com conceito visual, message match, prova, objeções e CTA coerentes. |
| [legacy-system-reconstruction](https://github.com/paulociano/skill-arsenal/blob/master/skills/legacy-system-reconstruction/SKILL.md) | Reconstruir documentação, regras e arquitetura de sistemas legados em descoberta somente leitura antes de planejar modernização. |
| [library-version-grounding](https://github.com/paulociano/skill-arsenal/blob/master/skills/library-version-grounding/SKILL.md) | Fundamentar decisões de programação na versão instalada de bibliotecas e na documentação oficial correspondente. |
| [linkedin-profile-optimizer](https://github.com/paulociano/skill-arsenal/blob/master/skills/linkedin-profile-optimizer/SKILL.md) | Reestruturar perfis de LinkedIn com posicionamento, headline, About, experiências e provas factuais. |
| [llm-observability-evaluation](https://github.com/paulociano/skill-arsenal/blob/master/skills/llm-observability-evaluation/SKILL.md) | Instrumentar e avaliar aplicações LLM com traces, datasets, métricas e comparações reproduzíveis entre versões. |
| [llm-red-team-evaluation](https://github.com/paulociano/skill-arsenal/blob/master/skills/llm-red-team-evaluation/SKILL.md) | Avaliar adversarialmente aplicações GenAI com threat model, probes, detectores, cobertura, mitigação e reteste controlado. |
| [locale-adapter](https://github.com/paulociano/skill-arsenal/blob/master/skills/locale-adapter/SKILL.md) | Localizar conteúdo e UX copy para outro idioma ou mercado preservando fatos, termos protegidos e comportamento do produto. |
| [loop-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/loop-engineering/SKILL.md) | Projetar trabalho recorrente ou iterativo com trigger, execução, verificação, estado persistido e limites de parada. |
| [material-design-3](https://github.com/paulociano/skill-arsenal/blob/master/skills/material-design-3/SKILL.md) | Implementar ou auditar interfaces Material Design 3 em Compose, Flutter ou web conforme a plataforma e versão reais. |
| [meeting-knowledge-capture](https://github.com/paulociano/skill-arsenal/blob/master/skills/meeting-knowledge-capture/SKILL.md) | Converter gravações, transcrições ou notas de reuniões em decisões e ações rastreáveis no destino autorizado. |
| [ml-production-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/ml-production-engineering/SKILL.md) | Projetar e operar sistemas de machine learning do dado à produção com testes, avaliação, serving, monitoramento e ciclos seguros de melhoria. |
| [mobile-device-automation](https://github.com/paulociano/skill-arsenal/blob/master/skills/mobile-device-automation/SKILL.md) | Executar e verificar tarefas em dispositivos móveis somente com controle real disponível, por ações pequenas e observação de estado. |
| [model-routing-gateway](https://github.com/paulociano/skill-arsenal/blob/master/skills/model-routing-gateway/SKILL.md) | Projetar ou configurar roteamento de modelos LLM com seleção por capacidade, retries, fallback, orçamento e observabilidade. |
| [motion-asset-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/motion-asset-engineering/SKILL.md) | Escolher, integrar e validar assets animados em web entre SVG/CSS, Lottie, Rive, Canvas e vídeo conforme interação, peso, editabilidade e acessibilidade. |
| [niche-research](https://github.com/paulociano/skill-arsenal/blob/master/skills/niche-research/SKILL.md) | Pesquisar pautas atuais de um nicho e propor ângulos editoriais com fontes e datas verificadas. |
| [powerbi-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/powerbi-engineering/SKILL.md) | Projetar, construir, auditar e versionar soluções Power BI com modelo semântico, DAX, performance, temas, embedding e práticas de ALM conforme ferramentas realmente disponíveis. |
| [presentation-template-adaptation](https://github.com/paulociano/skill-arsenal/blob/master/skills/presentation-template-adaptation/SKILL.md) | Adaptar conteúdo a um deck de referência preservando identidade visual, elementos fixos e capacidade dos layouts. |
| [prioritization-engine](https://github.com/paulociano/skill-arsenal/blob/master/skills/prioritization-engine/SKILL.md) | Priorizar trabalho, oportunidades ou problemas por impacto, urgência, dependências, risco e esforço com critérios explícitos e análise de sensibilidade. |
| [procedural-3d-reconstruction](https://github.com/paulociano/skill-arsenal/blob/master/skills/procedural-3d-reconstruction/SKILL.md) | Reconstruir objetos de imagens como modelos procedurais Three.js por estágios e comparação visual com a referência. |
| [procedural-film](https://github.com/paulociano/skill-arsenal/blob/master/skills/procedural-film/SKILL.md) | Criar curtas verticais animados proceduralmente com Canvas/Web Audio, storyboard em beat grid, render determinístico e revisão quadro a quadro. |
| [product-metrics-diagnostics](https://github.com/paulociano/skill-arsenal/blob/master/skills/product-metrics-diagnostics/SKILL.md) | Diagnosticar movimentos de métricas por definição, funil, cohort, segmento, drivers e qualidade de dados antes de propor ação. |
| [project-complexity-management](https://github.com/paulociano/skill-arsenal/blob/master/skills/project-complexity-management/SKILL.md) | Diagnosticar focos de complexidade técnica, organizacional e externa e definir intervenções proporcionais às evidências. |
| [project-health-review](https://github.com/paulociano/skill-arsenal/blob/master/skills/project-health-review/SKILL.md) | Revisar saúde de projetos por evidências de entrega, marcos, dependências, bloqueios, riscos, aging e próximas ações sem esconder incerteza em uma nota única. |
| [project-planning](https://github.com/paulociano/skill-arsenal/blob/master/skills/project-planning/SKILL.md) | Transformar objetivos em plano executável com outcomes, workstreams, marcos, dependências, caminho crítico, capacidade, riscos e critérios de conclusão sem falsa precisão. |
| [project-skill-architecture](https://github.com/paulociano/skill-arsenal/blob/master/skills/project-skill-architecture/SKILL.md) | Organizar ou migrar regras e workflows de projetos em skills pequenas, com proprietários canônicos e rotas sem duplicação. |
| [prose-lint](https://github.com/paulociano/skill-arsenal/blob/master/skills/prose-lint/SKILL.md) | Auditar prosa por clareza, redundância, ambiguidade, jargão, inconsistência e linguagem potencialmente excludente usando checks como sinais, não regras absolutas. |
| [publication-figure-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/publication-figure-engineering/SKILL.md) | Produzir figuras científicas alinhadas aos claims de papers, separando diagramas conceituais de gráficos quantitativos exatos. |
| [quick-grill](https://github.com/paulociano/skill-arsenal/blob/master/skills/quick-grill/SKILL.md) | Fazer uma rodada curta de perguntas de alinhamento quando o usuário pedir explicitamente para ser questionado antes da execução. |
| [reels-scripting](https://github.com/paulociano/skill-arsenal/blob/master/skills/reels-scripting/SKILL.md) | Analisar a estrutura narrativa de um Reel e criar roteiro original no mesmo padrão, sem copiar conteúdo ou presumir desempenho. |
| [retrieval-quality-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/retrieval-quality-engineering/SKILL.md) | Diagnosticar e melhorar retrieval/RAG com conjunto de consultas, baseline e avaliação de chunking, busca híbrida e reranking. |
| [retrospective-codify](https://github.com/paulociano/skill-arsenal/blob/master/skills/retrospective-codify/SKILL.md) | Codificar aprendizados recorrentes quando solicitado, escolhendo entre atualizar skill, regra, checklist, teste ou documentação. |
| [root-cause-analysis](https://github.com/paulociano/skill-arsenal/blob/master/skills/root-cause-analysis/SKILL.md) | Investigar causas de problemas operacionais, comerciais ou de produto separando sintomas, mecanismos, fatores contribuintes e evidência causal. |
| [runtime-ui-verification](https://github.com/paulociano/skill-arsenal/blob/master/skills/runtime-ui-verification/SKILL.md) | Verificar mudanças de UI no app em execução por consequências de domínio, estado e rede além da aparência visual. |
| [scenario-forecasting](https://github.com/paulociano/skill-arsenal/blob/master/skills/scenario-forecasting/SKILL.md) | Construir forecasts e cenários com baseline, backtesting, intervalos, premissas e gatilhos de atualização sem transformar projeção em certeza. |
| [scroll-storytelling](https://github.com/paulociano/skill-arsenal/blob/master/skills/scroll-storytelling/SKILL.md) | Projetar experiências narrativas guiadas por scroll com estágios, pinning, parallax, transições e sincronização DOM/WebGL sem sacrificar acessibilidade ou performance. |
| [seo-research-audit](https://github.com/paulociano/skill-arsenal/blob/master/skills/seo-research-audit/SKILL.md) | Pesquisar palavras-chave ou auditar SEO e concorrentes com evidências reais, métricas disponíveis e prioridades acionáveis. |
| [session-learn](https://github.com/paulociano/skill-arsenal/blob/master/skills/session-learn/SKILL.md) | Extrair aprendizados duráveis de uma sessão quando solicitado ou autorizado, com deduplicação e rastreabilidade. |
| [shadcn-ui-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/shadcn-ui-engineering/SKILL.md) | Implementar, atualizar e depurar componentes em projetos shadcn/ui preservando configuração, composição acessível e personalizações locais. |
| [shader-graphics-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/shader-graphics-engineering/SKILL.md) | Implementar, depurar ou otimizar shaders GLSL/WebGL e gráficos procedurais conforme efeito, runtime, integração DOM/3D e orçamento de desempenho. |
| [skill-builder](https://github.com/paulociano/skill-arsenal/blob/master/skills/skill-builder/SKILL.md) | Criar ou atualizar skills reutilizáveis a partir de workflows recorrentes, com gatilhos claros, dependências reais e validação. |
| [skill-security-review](https://github.com/paulociano/skill-arsenal/blob/master/skills/skill-security-review/SKILL.md) | Inspecionar segurança de skills, agentes ou plugins antes da adoção sem executar instaladores ou código da fonte avaliada. |
| [social-analytics](https://github.com/paulociano/skill-arsenal/blob/master/skills/social-analytics/SKILL.md) | Analisar exports de redes sociais para identificar tendências e desempenho sem extrapolar amostras ou métricas indisponíveis. |
| [social-post-review](https://github.com/paulociano/skill-arsenal/blob/master/skills/social-post-review/SKILL.md) | Revisar posts separando qualidade editorial de comparação com o histórico real do autor, sem prever desempenho por score. |
| [source-to-skill](https://github.com/paulociano/skill-arsenal/blob/master/skills/source-to-skill/SKILL.md) | Converter fontes longas em skills de conhecimento com entrada compacta, referências sob demanda e fidelidade à origem. |
| [sprite-sheet-pipeline](https://github.com/paulociano/skill-arsenal/blob/master/skills/sprite-sheet-pipeline/SKILL.md) | Converter animações ou frames em sprite sheets com registro, escala, transparência e timing verificados. |
| [structured-output-contract](https://github.com/paulociano/skill-arsenal/blob/master/skills/structured-output-contract/SKILL.md) | Definir e validar schemas para saídas LLM consumidas por código, com tipos, incerteza explícita e retries limitados. |
| [svg-handdrawn-animation](https://github.com/paulociano/skill-arsenal/blob/master/skills/svg-handdrawn-animation/SKILL.md) | Animar o desenho progressivo de SVGs com strokes e revelação de fills preservando cores, estrutura e segurança do embed. |
| [swiftui-modern-ui](https://github.com/paulociano/skill-arsenal/blob/master/skills/swiftui-modern-ui/SKILL.md) | Implementar ou revisar SwiftUI adaptativo com APIs nativas compatíveis com o SDK e deployment target reais. |
| [system-design-engineering](https://github.com/paulociano/skill-arsenal/blob/master/skills/system-design-engineering/SKILL.md) | Projetar sistemas escaláveis a partir de requisitos, estimativas, trade-offs, componentes, dados, falhas e evolução operacional. |
| [tdd](https://github.com/paulociano/skill-arsenal/blob/master/skills/tdd/SKILL.md) | Aplicar desenvolvimento orientado a testes por ciclos red–green em fatias verticais de comportamento observável. |
| [teach](https://github.com/paulociano/skill-arsenal/blob/master/skills/teach/SKILL.md) | Organizar aprendizagem em múltiplas sessões com arquitetura de explicação, prática de recuperação, espaçamento e progressão por domínio demonstrado. |
| [team-health-management](https://github.com/paulociano/skill-arsenal/blob/master/skills/team-health-management/SKILL.md) | Avaliar sinais operacionais de saúde de equipe e converter problemas de clareza, carga, fluxo, dependências e coordenação em ações de gestão observáveis, sem psicologizar pessoas. |
| [to-questionnaire](https://github.com/paulociano/skill-arsenal/blob/master/skills/to-questionnaire/SKILL.md) | Transformar lacunas de decisão em perguntas direcionadas à pessoa que possui o contexto necessário. |
| [to-spec](https://github.com/paulociano/skill-arsenal/blob/master/skills/to-spec/SKILL.md) | Converter decisões de uma conversa ou projeto em especificação executável sem reiniciar descoberta já resolvida. |
| [to-tickets](https://github.com/paulociano/skill-arsenal/blob/master/skills/to-tickets/SKILL.md) | Decompor specs e planos em tickets verticais pequenos, demonstráveis e com dependências e critérios de aceitação explícitos. |
| [typographic-composition](https://github.com/paulociano/skill-arsenal/blob/master/skills/typographic-composition/SKILL.md) | Projetar tipografia expressiva e legível em layouts, títulos e peças visuais usando hierarquia, ritmo, line breaks, spacing e forma das palavras sem confundir composição com engenharia de fontes. |
| [ui-motion-design](https://github.com/paulociano/skill-arsenal/blob/master/skills/ui-motion-design/SKILL.md) | Projetar e auditar motion de interface por função, timing, acessibilidade e custo antes de escolher CSS, Motion, GSAP, Rive ou outra tecnologia. |
| [ui-ux-catalog](https://github.com/paulociano/skill-arsenal/blob/master/skills/ui-ux-catalog/SKILL.md) | Consultar o catálogo UI UX Pro Max para selecionar paletas, tipografia e padrões de interface, verificando pertinência e preservando decisões de design existentes. |
| [value-investing-company-analysis](https://github.com/paulociano/skill-arsenal/blob/master/skills/value-investing-company-analysis/SKILL.md) | Analisar empresas por fundamentos e value investing com dados atuais, cenários de valuation e riscos que podem invalidar a tese. |
| [verify-before-claim](https://github.com/paulociano/skill-arsenal/blob/master/skills/verify-before-claim/SKILL.md) | Verificar afirmações consequenciais de conclusão, correção ou publicação com evidência fresca do escopo afirmado. |
| [video-editing-pipeline](https://github.com/paulociano/skill-arsenal/blob/master/skills/video-editing-pipeline/SKILL.md) | Editar vídeos com transcrição, decisões de corte explícitas, EDL, render e revisão audiovisual preservando as fontes. |
| [visual-explanation-sketch](https://github.com/paulociano/skill-arsenal/blob/master/skills/visual-explanation-sketch/SKILL.md) | Transformar conceitos, processos e relações em esboços visuais simples com caixas, setas, agrupamentos, anotações e destaques para facilitar compreensão. |
| [voice-builder](https://github.com/paulociano/skill-arsenal/blob/master/skills/voice-builder/SKILL.md) | Construir perfis de voz e posicionamento a partir de amostras reais, distinguindo identidade, estilo, audiência e canal. |
| [watch-video](https://github.com/paulociano/skill-arsenal/blob/master/skills/watch-video/SKILL.md) | Analisar vídeos com transcrição e frames disponíveis, ancorando conclusões em timestamps e distinguindo visto, dito e inferido. |
| [wayfinder](https://github.com/paulociano/skill-arsenal/blob/master/skills/wayfinder/SKILL.md) | Planejar projetos que atravessam sessões como mapas de decisões, resolvendo primeiro as incertezas já desbloqueadas. |
| [web-analytics-ga4](https://github.com/paulociano/skill-arsenal/blob/master/skills/web-analytics-ga4/SKILL.md) | Analisar tráfego, aquisição e conversão em GA4 ou exports equivalentes com períodos comparáveis e limitações de tracking. |
| [web-design-engineer](https://github.com/paulociano/skill-arsenal/blob/master/skills/web-design-engineer/SKILL.md) | Construir ou redesenhar interfaces web com pesquisa, direção, estrutura, interação, motion e efeitos contemporâneos, preservando marca, acessibilidade, performance e verificação em runtime. |
| [web-extraction-pipeline](https://github.com/paulociano/skill-arsenal/blob/master/skills/web-extraction-pipeline/SKILL.md) | Extrair conteúdo estruturado de sites quando busca comum não basta, com técnica mínima, escopo limitado e validação. |
| [web-quality-audit](https://github.com/paulociano/skill-arsenal/blob/master/skills/web-quality-audit/SKILL.md) | Auditar qualidade web em runtime com performance, acessibilidade, best practices e evidência reproduzível. |
| [web-video-presentation](https://github.com/paulociano/skill-arsenal/blob/master/skills/web-video-presentation/SKILL.md) | Criar apresentações HTML por cenas e narração para navegação por clique ou gravação, quando a entrega em navegador é parte do pedido. |
| [weekly-review-planning](https://github.com/paulociano/skill-arsenal/blob/master/skills/weekly-review-planning/SKILL.md) | Executar revisão semanal baseada em calendário, compromissos, projetos, pendências e capacidade para fechar loops e definir poucos outcomes realistas para a próxima semana. |
| [writing-quality](https://github.com/paulociano/skill-arsenal/blob/master/skills/writing-quality/SKILL.md) | Rascunhar, estruturar, revisar ou auditar prosa preservando significado, evidência, voz, clareza e adequação ao meio. |

## Stacks disponíveis

As 12 stacks abaixo coordenam fluxos recorrentes. As skills citadas em cada stack são candidatas: aplique apenas as que contribuírem para a tarefa.

| Stack | Para que serve |
| --- | --- |
| [business-decision-intelligence](https://github.com/paulociano/skill-arsenal/blob/master/stacks/business-decision-intelligence/STACK.md) | Investiga métricas e causas, estrutura decisões, prioriza ações, projeta cenários e comunica resultados em dashboards ou Power BI. |
| [checkpoint-nao-iniciados](https://github.com/paulociano/skill-arsenal/blob/master/stacks/checkpoint-nao-iniciados/STACK.md) | Lista clientes com status “Não iniciado” em um período informado, agrupando por mês e por líder direto ou responsável do consultor, e entrega o resultado pronto para WhatsApp. |
| [content-production](https://github.com/paulociano/skill-arsenal/blob/master/stacks/content-production/STACK.md) | Planeja, produz, adapta, governa e revisa conteúdo para múltiplos canais mantendo consistência de mensagem e capacidade operacional. |
| [creative-web-engineering](https://github.com/paulociano/skill-arsenal/blob/master/stacks/creative-web-engineering/STACK.md) | Orquestra direção, estrutura, scroll, motion, microinterações e gráficos criativos para websites contemporâneos de alta expressão com verificação de acessibilidade e performance. |
| [debug-and-fix](https://github.com/paulociano/skill-arsenal/blob/master/stacks/debug-and-fix/STACK.md) | Investiga, corrige e valida bugs em software com diagnóstico estruturado, testes e revisão proporcional ao risco. |
| [evaluate-and-import-skill](https://github.com/paulociano/skill-arsenal/blob/master/stacks/evaluate-and-import-skill/STACK.md) | Avalia uma skill externa, compara com o Arsenal, adapta para o ambiente atual, revisa segurança e importa somente quando houver valor real. |
| [gestao-comercial-da-semana](https://github.com/paulociano/skill-arsenal/blob/master/stacks/gestao-comercial-da-semana/STACK.md) | Organizar a gestão semanal do time de consultoria financeira com retrospectiva, avaliação de conversas, slots de agenda, prioridades verificáveis, mensagens e continuidade entre semanas. |
| [improve-existing-web-app](https://github.com/paulociano/skill-arsenal/blob/master/stacks/improve-existing-web-app/STACK.md) | Melhora uma aplicação web existente preservando funcionalidades, refinando design e validando o resultado no runtime. |
| [meeting-to-actions](https://github.com/paulociano/skill-arsenal/blob/master/stacks/meeting-to-actions/STACK.md) | Transforma reuniões, transcrições ou notas em conhecimento reutilizável, decisões, ações e handoffs. |
| [research-and-synthesize](https://github.com/paulociano/skill-arsenal/blob/master/stacks/research-and-synthesize/STACK.md) | Pesquisa um tema com múltiplas fontes, reconcilia evidências e produz uma síntese clara, útil e verificável. |
| [research-to-presentation](https://github.com/paulociano/skill-arsenal/blob/master/stacks/research-to-presentation/STACK.md) | Converte pesquisa, documentos ou dados em apresentações e dashboards executivos editáveis, estruturados por evidência, narrativa e QA visual. |
| [social-growth-engine](https://github.com/paulociano/skill-arsenal/blob/master/stacks/social-growth-engine/STACK.md) | Diagnostica gargalos de crescimento social, pesquisa oportunidades, planeja conteúdo, produz, mede e realimenta o próximo ciclo. |

## Avaliação de novas skills

A avaliação considera o que a skill faz, quando deve ser usada, o ganho sobre instruções comuns, suas dependências e sua relação com o Arsenal existente.

| Categoria | Significado |
| --- | --- |
| A — Skill realmente útil | Processo claro com mudança relevante de comportamento. |
| B — Boa metodologia | Método útil que pode ser incorporado a uma skill existente. |
| C — Prompt sofisticado | Pouco ganho sobre uma boa instrução comum. |
| D — Skill técnica | Depende de ferramentas, código, scripts ou integrações externas. |

A decisão pode ser adotar, adaptar ou descartar. Preserve a metodologia útil, adapte dependências às capacidades reais do ambiente e prefira melhorar recursos existentes a criar duplicações. Consulte a stack [evaluate-and-import-skill](https://github.com/paulociano/skill-arsenal/blob/master/stacks/evaluate-and-import-skill/STACK.md) para o procedimento completo.

## Manutenção do catálogo

1. Atualize o índice quando uma skill ou stack for criada, removida, renomeada ou tiver sua descrição alterada materialmente.
2. Atualize este README para refletir os mesmos nomes, descrições, links e contagens.
3. Confira cada entrada contra os arquivos `skills/*/SKILL.md` e `stacks/*/STACK.md`.
4. Preserve nomes em kebab-case e frontmatter válido com `name` e `description` nos arquivos de skills e stacks.
5. Siga as regras de publicação e preservação de alterações concorrentes descritas em [AGENTS.md](https://github.com/paulociano/skill-arsenal/blob/master/AGENTS.md).

**Base deste catálogo:** [commit cee2efa](https://github.com/paulociano/skill-arsenal/commit/cee2efad1e4115a9b279f3363fa2684d85ed6717), consultado em 26/09/2026. A árvore completa do repositório foi comparada ao índice: 115 skills e 12 stacks, sem entradas ausentes ou excedentes. Os links do catálogo apontam para a branch `master`, para facilitar o acesso às versões atuais.
