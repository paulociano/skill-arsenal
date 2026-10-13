# Avaliação: doodledood/scrollytelling (2026-10-13)

- **Fonte:** https://github.com/doodledood/claude-code-plugins/blob/3c29306a42255bb58c1fdfd0060d449b7dd1335e/claude-plugins/frontend-design/skills/scrollytelling/SKILL.md
- **Versão avaliada:** commit fixo `3c29306a42255bb58c1fdfd0060d449b7dd1335e`; arquivo SKILL.md, sem diretórios auxiliares na pasta fornecida.
- **Classificação:** B — boa metodologia, incrementalmente útil, mas não justifica skill independente.
- **Decisão:** adaptar conteúdo específico à skill existente `skills/scroll-storytelling/SKILL.md`, sem nova skill ou alteração do router.

## Comportamento real

Documento prescritivo para planejar narrativas por scroll, com 5 técnicas (graphic sequence, animated transition, pan and zoom, moviescroller, show-and-play), sticky sections, IntersectionObserver, CSS scroll timelines, Motion/GSAP, responsive/mobile e QA de acessibilidade/performance. Exemplos são snippets educativos, não uma engine executável.

## Sobreposição

O Arsenal já tem `scroll-storytelling` e a stack `creative-web-engineering`, cobrindo beats, flow/reveal/sticky/progress-linked, DOM/WebGL, fallback, acessibilidade, performance e execução. O ganho incremental é a taxonomia de 5 técnicas, contraste entre mecanismos nativos, atenção explícita às unidades de viewport e eventos touch, e checklist mobile mais concreto.

## Adaptação

Adicionar à skill canônica seções curtas para taxonomia visual, implementação progressiva via CSS/IntersectionObserver, e cuidados mobile/QA. Não copiar 28k caracteres nem os questionários específicos de outros agentes. APIs, bibliotecas e padrões são candidatos sujeitos a suporte e contexto; nenhum comando do Claude Code é necessário.

## Segurança

**APPROVE para incorporação textual.** Inspeção manual da única SKILL.md da pasta: snippets React, CSS e JS ilustrativos; nenhuma instalação ou execução de código externo foi realizada. Nenhuma exigência identificada de acesso a segredos, exfiltração, comandos de shell, hooks persistentes ou alterações irreversíveis. Uso de libs de terceiros em projetos requer auditoria de dependências separada. Não foi usado scanner estático; análise restrita à fonte versionada informada.

## Reservas técnicas e evidência

- Números sobre +400% de tempo, 67% de memória, 5x compartilhamento e conversão 25–40% aparecem sem referência verificável individual e não foram incorporados.
- Afirmações de suporte por navegador, tamanhos de bundle e ganhos de performance são temporalmente sensíveis e devem ser confirmadas na implementação; há inconsistência de cronologia na referência a Chrome 115.
- Regras absolutas sobre parallax, scroll snap, `svh` e touch devem ser decisões contextuais, não verdades universais.
- Fallback reduced-motion e sem JS deve manter conteúdo acessível, não simplesmente manter elementos ocultos.

## Validação

Revisão documental comparativa de fonte e skill existente. Não há projeto web de destino nesta tarefa, portanto nenhum teste de runtime, bundle, FPS, mobile real ou conversão foi executado. A publicação dos arquivos não valida comportamento em navegador.
