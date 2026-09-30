# Pesquisa de ecossistema — IA para carrosséis, posts sociais, crescimento orgânico e paid creative

Data: 2026-09-30

## Objetivo

Pesquisar 30 repositórios GitHub relacionados a:
- criação de carrosséis por IA;
- desenvolvimento de posts e hooks;
- ideação e repurposing;
- engajamento e crescimento orgânico;
- analytics e feedback loops;
- criativos e experimentação para tráfego pago;
- automação/publicação social.

Fluxo aplicado: `arsenal-autopilot`.

A busca combinou GitHub Search e pesquisa pública; repositórios com novidade plausível foram aprofundados na fonte canônica. Nenhum installer, app, scheduler, MCP, API de ads, modelo ou publisher foi executado.

## 30 repositórios pesquisados

### Carrossel e visual generation
1. `wasimjalali/swipekit` — script → typed slides → brand config → backgrounds → PDF/PNG.
2. `tomaskub292929/open-carrusel` — carrossel HTML/CSS, edição por slide, referências visuais, safe zones e export.
3. `kenkirito/carousel` — estrutura hook → value slides → CTA, temas por nicho e edição.
4. `FranciscoMoretti/carousel-generator` — gerador de carrossel LinkedIn com IA.
5. `Simonstorms/slidelot` — TikTok slideshow com aprovação e analytics feedback loop.
6. `AgriciDaniel/linkedin-content-creator` — pesquisa, posts, imagens, carrossel, calendário e batch variants.
7. `Thaynabarreiro/social-content-automation` — RSS → IA → revisão humana → carrossel → publicação.
8. `matefs/instagram-carousel-ai-generator` — geração de carrosséis Instagram por IA.
9. `EliteSystemsAI/instagram-carousel-generator` — gerador de carrossel Instagram.
10. `Maazsiddiqui01/linkedin-carousel-generator` — gerador dedicado a LinkedIn.

### Estratégia, copy, hooks e repurposing
11. `agentreacher/skills` — content pillars, cadence, viral hooks, repurpose e packaging.
12. `rediumvex/viral-hooks-skill` — biblioteca de famílias de hooks e adaptação por plataforma.
13. `sarveshtalele/linkedin-content-skill` — posts, carrosséis, newsletters e calendário LinkedIn.
14. `tcintern-016/content-strategist` — business description → audience/platform/pillars → posts.
15. `hermeias-org/HookForge` — geração de hooks e posts LinkedIn.
16. `Devanik21/Linkedin-post-generator` — templates de hook, tone/length, variantes e hashtags.
17. `Dev-derah/simple-content-ai` — geração/repurposing social.
18. `Synergy-Forge/RepurposeAI` — repurposing de conteúdo com IA.
19. `RumbleInCybertron/content-repurposer-tool` — transformação de source content em formatos sociais.
20. `replynodes/awesome-social-media-skills` — catálogo de discovery para skills sociais; usado apenas como radar.

### Analytics, scheduling e feedback
21. `trypostit/trypost` — brand-aware copilot, carousel builder, scheduling, approvals e analytics.
22. `Anil-matcha/Free-AI-Social-Media-Scheduler` — copy por plataforma, memória de campanha e scheduling.
23. `adarsh-mamgain/schedowl` — scheduler + analytics + AI suggestions.
24. `reforia/influence-hub` — agregação de analytics e trend/audience insights.
25. `sjcripps/mcp-social-media-analytics` — profile, engagement, trends e hashtags via MCP.
26. `postmill-ai/postmill-app` — multi-brand social management, AI media tools e analytics.
27. `lumizone/postsider` — scheduling, per-platform validation, UTM/snippets e recycling.

### Paid creative e ads
28. `pmlabs-org/mcp-meta-ads` — creative ops, dynamic creative testing, insights e write confirmations.
29. `Synter-Media-AI/meta-ads-agent` — AI agent para Meta Ads, audience/creative testing/optimization.
30. `Anil-matcha/Open-AI-UGC` — geração de variantes UGC em vídeo para anúncios sociais.

## Síntese das melhores ideias

### 1. Carrossel é narrativa, não template
Os projetos mais fortes estruturam o conteúdo antes do layout. O padrão recorrente é:
`hook → progressão → proof/value → implication → CTA`.

A unidade de design útil não é apenas o slide individual, mas a função que ele exerce no arco.

### 2. Hook precisa de follow-through
Bibliotecas de hooks são úteis como famílias de exploração, mas score de "viralidade" não é evidência. Hook bom cria tensão relevante e o restante do conteúdo precisa satisfazê-la.

### 3. Uma ideia dominante por slide
A sequência melhora quando cada swipe avança o raciocínio. Repetição, excesso de copy e slides que só reformulam o anterior devem ser comprimidos.

### 4. Brand profile deve ser estrutural
Separar brand config de provider/modelo reduz drift. Paleta, type roles, logo, voz, safe zones e padrões visuais devem sobreviver à troca de LLM ou image model.

### 5. Edição granular supera regeneração total
A capacidade de revisar um único slide/hook/visual sem destruir a sequência inteira é um padrão forte para workflows assistidos por IA.

### 6. Preview e export precisam convergir
Quando possível, a mesma fonte de layout deve alimentar preview e export. HTML/CSS → render/export é um padrão útil porque reduz diferença entre editor e asset final.

### 7. Human approval antes de publicação
Automação de conteúdo madura separa geração de aprovação e publicação. Repetição de tema, claims sensíveis, campanha paga e ações externas merecem gates explícitos.

### 8. Repurposing não é cross-posting
Uma fonte deve ser destilada em atomic ideas/proof/story/objections e depois reconstruída para cada canal. Reutilizar fatos é diferente de duplicar wording.

### 9. Organic e paid não têm o mesmo contrato
Orgânico pode otimizar para descoberta, saves, shares, conversa, visitas ou cliques. Paid creative precisa registrar hipótese, audience, offer, hook, proof, CTA e conceito visual para permitir comparação.

### 10. Feedback loop é o maior ganho de IA
O padrão mais valioso encontrado é:
`generate → approve → publish → measure → compare → next hypothesis`.

Analytics deve alimentar hipóteses futuras sem transformar correlação de um post vencedor em causalidade.

## Claims que NÃO foram absorvidos

Vários READMEs usam linguagem como "viral", "high-converting" ou publicam multiplicadores de engagement. Esses claims não foram tratados como evidência universal.

Também não foram adotados:
- horários universais de postagem;
- quantidade fixa universal de slides;
- hashtags como requisito;
- tom controverso como default;
- benchmark de engagement externo como meta;
- conclusão de causalidade a partir de top posts;
- promessa de crescimento ou ROAS.

## Mudanças no Arsenal

### CREATE
`skills/social-carousel-engineering/SKILL.md`

Novo owner para carrossel social como narrativa slide a slide, cobrindo:
- distillation;
- arc selection;
- hook variants;
- slide map;
- progressive disclosure;
- visual grammar;
- continuity;
- CTA fit;
- organic vs paid;
- feedback loop;
- QA de exportação.

### UPDATE
`stacks/social-growth-engine/STACK.md`
- adiciona `social-carousel-engineering` como skill candidata;
- roteia produção de carrossel explicitamente;
- adiciona hipótese criativa para paid/testes com audience, offer, hook, proof, CTA e visual concept;
- usa `experiment-design` quando a intenção é aprender por comparação.

### INDEX
`ARSENAL INDEX.md` atualizado com o novo owner.

## Segurança e portabilidade

- nenhum scheduler/publicador foi conectado;
- nenhuma conta social ou de ads foi acessada;
- nenhum MCP de terceiros foi instalado;
- nenhum token/API key foi usado;
- nenhuma campanha foi criada ou alterada;
- nenhuma dependência Claude Code/Postiz/Meta Ads foi presumida como capacidade nativa;
- automação externa continua exigindo ferramenta real e autorização.

## Conclusão

A pesquisa justificou uma nova capability canônica: `social-carousel-engineering`.

Para engajamento e orgânico, o Arsenal já possuía bons owners de diagnóstico, ideação, revisão e analytics; o ganho foi fechar o gap do formato carrossel e reforçar o loop de aprendizado.

Para paid social, não foi necessário criar uma skill de operação de Meta Ads. O ganho metodológico foi incorporar creative hypothesis + experiment discipline à stack social, mantendo execução de campanhas dependente de integração real e autorização.

## Continuação — consolidação do sistema de posts

Após materializar `social-carousel-engineering`, foi feita uma segunda passagem de ownership para evitar criar skills estreitas demais.

### UPDATE — `content-matrix`

Em vez de criar um owner separado para "viral hooks", `content-matrix` passou a cobrir:
- audience tension;
- famílias de ângulo;
- hook families;
- proof/source;
- escolha de formato;
- CTA e função no funil;
- visual opportunity;
- creative hypothesis para paid;
- distillation/idea inventory para repurposing;
- roteamento para carrossel, vídeo curto, social card e texto.

A decisão reduz fragmentação: hooks são parte da arquitetura da ideia e do formato, não um produto isolado.

### UPDATE — `content-production`

O fluxo agora explicita:
- idea inventory antes de repurpose;
- reconstrução nativa por canal em vez de cross-posting literal;
- roteamento para `social-carousel-engineering`, `editable-visual-design` e `reels-scripting`;
- sequence logic de campanha;
- registro da variável alterada entre variantes;
- `experiment-design` quando a comparação pretende produzir aprendizado causal.

### Decisão de ownership

Não foram criadas skills separadas para:
- viral hooks;
- social repurposing;
- paid creative generator.

Essas capacidades têm owners naturais em `content-matrix`, `content-production`, `social-carousel-engineering`, `experiment-design` e `social-growth-engine`. Criá-las separadamente aumentaria overlap sem ganho comportamental claro.
