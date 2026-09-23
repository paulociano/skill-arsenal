---
name: landing-craft
description: "Projetar landing pages como narrativas de scroll com conceito visual, message match, prova, objeções e CTA coerentes."
---

# landing-craft

## Objetivo

Projetar landing pages de alto impacto como uma narrativa de scroll, combinando conceito visual, conversão, composição variada, densidade deliberada e QA real.

## Quando usar

- landing page / one-pager / hero-to-footer;
- campanhas, lançamentos, páginas de produto e experiências de scroll;
- páginas com tráfego de anúncio, e-mail ou campanha que exigem continuidade de promessa.

## Workflow

1. Ler design system/brand context, briefing, oferta, público e origem provável do tráfego.
2. Quando houver anúncio, e-mail, Reel, busca ou campanha de origem, preservar **message match**: a promessa da entrada deve continuar no hero, sem mudar subitamente de benefício ou linguagem.
3. Criar um conceito visual em uma frase e, quando a direção ainda estiver aberta, usar design-direction.
4. Escolher a estrutura antes do tema. Selecionar a arquitetura pela intenção:
   - classic hero + sections para ofertas compreensíveis rapidamente;
   - long-form story quando educação e objeções importam;
   - minimal conversion para tráfego de alta intenção;
   - comparison page quando a intenção real é comparar alternativas.
5. Storyboardar cada seção por função: promessa, prova, argumento, mecanismo, objeção, risco e CTA. Quantidade de seções deriva do conteúdo real.
6. Colocar prova próxima do claim que ela sustenta. Não inventar métricas, depoimentos, logos, resultados ou garantias.
7. Tratar objeções como parte da narrativa, não como rodapé automático. FAQ só entra quando responde fricções reais.
8. Manter uma ação primária clara acima da dobra; CTAs secundários só entram quando representam uma jornada realmente distinta.
9. Definir um ponto de clímax visual e o respiro que o antecede.
10. Planejar assets reais ou gerados, evitando decoração genérica sem função narrativa.
11. Construir responsivamente, com contraste, reduced motion, no-JS fallback quando necessário e prioridade clara da CTA.
12. Revisar densidade, hierarquia, responsividade, sobreposição, contraste, ritmo de scroll, continuidade da promessa e clareza do próximo passo.
13. Corrigir defeitos encontrados sem reconstrução total por estética.

## Message match e conversão

- O hero deve continuar a intenção que trouxe o visitante.
- Benefício vem antes de lista de features quando o objetivo é conversão.
- Especificidade vence abstrações como "transforme", "otimize" ou "leve ao próximo nível".
- Uma CTA deve dizer o que acontece ou o que a pessoa recebe.
- Redução de risco deve refletir uma condição verdadeira da oferta; nunca inventar trial, garantia, cancelamento ou gratuidade.
- Prova social sem fonte vira placeholder explícito, não copy fictícia.
- Para otimização baseada em dados, formular hipótese e teste em vez de declarar uma estrutura universalmente vencedora.

## SEO/AEO

Quando a landing for evergreen e indexável:
- alinhar title/meta com intenção e promessa real;
- preservar conteúdo textual compreensível sem depender de animação;
- usar perguntas e respostas claras quando FAQ fizer sentido;
- não adicionar schema sem correspondência real ao conteúdo.

Páginas estritamente temporárias ou de campanha não devem ser indexadas automaticamente; a decisão depende da estratégia do site.

## Regras

- DESIGN/brand facts existentes vencem heurísticas genéricas.
- Não inventar métricas, prova social, logos ou fatos de marca.
- Uma landing não deve ser apenas uma sequência de cards repetidos.
- Motion deve explicar progressão, origem, feedback ou continuidade; não decorar por padrão.
- Acessibilidade e legibilidade são parte do impacto, não um pós-processo.
- Não importar fórmulas rígidas de ordem de seção quando a oferta ou audiência pedir outra narrativa.

## Integração com o Arsenal

Usar junto com web-design-engineer. Quando direção visual não estiver resolvida, usar design-direction. Para decidir entre composições e evitar variar apenas cores, consultar a referência de estrutura de web-design-engineer. Para motion complexo, ui-motion-design decide a linguagem e gsap-animation implementa quando apropriado. Quando existir um design system robusto, design-system-governance define a autoridade e landing-craft define a narrativa da página.

## Referências

Adaptada de oh-my-design · omd-landing e enriquecida com princípios portáveis de elayadesign/ai-design-skills e dawitlabs/ui-skills, sem importar proibições tipográficas, fórmulas universais ou claims de conversão não verificados.

Origem local: landing-craft.docx.
