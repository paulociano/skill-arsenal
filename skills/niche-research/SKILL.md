---
name: niche-research
description: "Pesquisar pautas atuais de um nicho e propor ângulos editoriais com fontes e datas verificadas."
---

# niche-research

## Objetivo

Pesquisar pautas atuais de um nicho e transformá-las em oportunidades de conteúdo com fontes, datas e ângulos claros.

## Quando usar

Pesquisar pautas atuais de um nicho e propor ângulos editoriais com fontes e datas verificadas.

## Modos de pesquisa

Antes de buscar, escolher o modo dominante:

- **facts/news**: priorizar fontes primárias, veículos confiáveis, datas e evidência verificável;
- **discourse/reactions**: mapear o que comunidades e criadores estão dizendo, incluindo comentários, threads, transcripts e sinais de engajamento;
- **mixed**: usar fontes factuais para o que aconteceu e fontes sociais para como o público reagiu.

Engajamento mede saliência/discussão, não credibilidade. Um post popular não vira fato por ter muitos likes, views ou upvotes.

## Workflow

1. Definir nicho e objetivo editorial.
2. Usar pesquisa web atual quando o pedido depender de tendências/notícias.
3. Verificar datas, fonte primária quando possível e contexto suficiente para não transformar manchete em fato distorcido.
4. Separar fato confirmado, interpretação da fonte e ângulo editorial sugerido.
5. Evitar comentários/replies como fonte principal quando a tarefa é mapear notícias ou tendências.
6. Quando o pedido tiver janela temporal, preservar exatamente o período pedido; não transformar automaticamente "recente" em 30 dias se o usuário especificou outra janela.
7. Para pesquisa social, buscar texto relevante em título, corpo, comentários e transcript quando disponíveis; deduplicar cross-posts e versões republicadas.
8. Registrar quais fontes realmente responderam, quais estavam indisponíveis e onde a cobertura dependeu de fallback.
9. Entregar cobertura com links/fontes e indicar lacunas de feed/plataforma quando houver.

## Regras

Pesquisa indexada na web não equivale a varredura completa de feed social. Declarar essa diferença quando relevante.

## Referências

[GitHub · charlie947/social-media-skills · niche-research](https://github.com/charlie947/social-media-skills/tree/main/skills/niche-research)

Separação facts/news vs discourse, janela temporal explícita e source-health awareness adaptadas de https://github.com/mvanhorn/last30days-skill, sem importar scripts, cookies, APIs ou métricas proprietárias.

Origem local: [niche-research.docx](../niche-research.docx).

## Pesquisa social com amostragem e reputação (BrowserAct, 2026-10-15)

Quando pesquisar mercado/reações de plataformas como Reddit, Instagram, Threads, Facebook, YouTube, Trustpilot e Product Hunt, especificar plataforma, busca, período, conjunto realmente observado e viés de acesso/paginação. Separar posts, comentários, anúncios, perfis e avaliações verificadas; não converter likes/upvotes em demanda ou qualidade comprovada. Para reclamações e reviews, registrar nota, data, variante, verificação, resposta empresarial e recorrência apenas quando observáveis. Deduplicar republicações e respeitar privacidade; agregar dados de pessoas em vez de montar dossiês.

Incluir sinais de launch e concorrência em backlog de hipóteses testáveis. Não automatizar aquecimento de contas, falsa participação orgânica ou mensagens/replies em massa. Proveniência: BrowserAct producthunt-launches, reddit-competitor-analysis-api-skill, trustpilot-reviews, instagram-post-comments, instagram-hashtag-posts, threads-keyword-search e outras interfaces sociais.

## Protocolo de escuta social comparável (BrowserAct, lote 61–80, 2026-10-15)

Quando a pergunta envolver posts, hashtags, locais, perfis, threads ou avaliações públicas, construir uma unidade de evidência com: `plataforma, URL/ID, entidade/tema, janela, tipo (post/comentário/review), data original, data de coleta, contexto, amostra, condição de acesso`. Distinguir publicação própria de resposta, perfil empresarial de pessoa, conversa completa de amostra paginada. Para threads de X e comentários de Instagram, preservar relações reply-to e reconhecer respostas ocultas, apagadas ou indisponíveis; não imputar posição favorável a ausências. Em buscas por hashtag e localização, não tratar feed ranqueado como censo e não inferir residência de pessoas a partir de geotag.

Para estudos Trustpilot, desagregar nota (1–5), idioma, data de experiência versus publicação, verificação, resposta da empresa, período e filtros; comparar taxas com denominador e janela compatíveis; considerar reviews incentivados, base pequena e viés de seleção. Em Reddit, classificar menção de marca em afirmação verificável, opinião, objeção, pedido e hipótese, cruzando fontes antes de inferir oportunidade. Excluir identificação persistente de participantes quando não necessária e não extrair dados de ambientes restritos.

Entregar evidências e confiança por achado, temas recorrentes, contraexemplos, lacunas de cobertura e ação editorial/comercial. Fonte metodológica: browser-act/skills, lote 61–80, sem dependência de suas APIs autenticadas.

## Vídeos curtos e discussões por consulta (BrowserAct 81–100, 2026-10-15)

Para pesquisa em X, Xiaohongshu, Douyin, TikTok e YouTube: registrar consulta/hashtag, mercado, idioma, janela temporal, ordenação, link canônico, data do post, data da coleta e se o resultado veio de busca, perfil ou URL direta. Comparar sinais com mesma amostra e distinguir recomendação algorítmica de relevância de mercado. Extrair hipótese de demanda de perguntas, objeções e comentários, preservando contexto e contraexemplos. Vídeos com alto engajamento não comprovam satisfação nem intenção de compra. Ao usar transcrições, citar trecho e timecode quando disponível; indicar idiomas, transcrição automática, lacunas e impossibilidade de verificar audiovisual sem acesso ao vídeo. Não afirmar coleta exaustiva, downloads ou scripts executados sem ferramentas reais. Proveniência: BrowserAct x-tweet-search(-by-query), xiaohongshu-search(-full), douyin-video-search, tiktok-search-videos, youtube-transcript-analysis-api-skill.
