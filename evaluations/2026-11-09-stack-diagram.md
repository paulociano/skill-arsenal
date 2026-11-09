# stack-diagram (2026-11-09)

## Fonte
- https://github.com/caru-ini/stack-diagram — commit `5af3b09` (2026-11-09)
- Lidos: `README.md`, `skills/stack-diagram/SKILL.md`, `references/geometry.md`, índice de `references/tsx.md`, varredura dos scripts (`fetch_icons.py`, `build.py`, `render_png.py`, `share.py`) por execução de processos e endpoints de rede
- Stack de avaliação: stacks/evaluate-and-import-skill/STACK.md

## O que é
Agent Skill que transforma uma frase sobre a stack ("Next.js e Hono na Vercel, Postgres no Neon, Clerk, Stripe") num diagrama de arquitetura no estilo dos fornecedores de nuvem: logos oficiais em tiles brancos, grupos rotulados, setas ortogonais com rótulos, fundo quadriculado. Entrega um HTML autocontido (fonte da verdade), PNG claro e escuro, componente React ou artifact. Busca logos em svgl → devicon → gilbarbara/logos e usa os pacotes oficiais de ícones de AWS, Google Cloud e Azure. Oferece, uma vez, publicar na galeria pública stacks.caru.moe. MIT; fontes Geist e JetBrains Mono em OFL; logos não são distribuídos.

## Classificação e decisão

| Item | Classe | Decisão |
|---|---|---|
| Método: política de logos oficiais, regras de AWS/Google Cloud/Azure, geometria nó = tile + texto, três tipos de aresta, HTML fonte única com render claro/escuro, checklist visual, gate de privacidade antes de publicar | **B** | ABSORB_METHOD — incorporado em `architecture-visualization` |
| Scripts, template, fontes | D | NÃO IMPORTAR — runtime externo (Python 3.9+, rede, Playwright/Chromium) |
| Galeria pública | D | NÃO ADOTAR — fora do escopo do Arsenal |

Não foi criada skill nova: `architecture-visualization` já é o owner de diagramas de arquitetura e tinha disciplina editorial, de layout e de evidência. Faltavam a política de logos de marca, as regras de cada nuvem e a geometria que impede seta atravessando texto.

## Sobreposição verificada
- `architecture-visualization` — owner.
- `interactive-system-diagram` — diagramas exploráveis; complementar, sem mudança.
- `publication-figure-engineering` — figuras científicas; sem sobreposição relevante.

## Implementado
- `skills/architecture-visualization/references/branded-stack-diagrams.md` (novo): método completo adaptado, em português.
- `skills/architecture-visualization/SKILL.md`: seção "Diagramas de stack com logos oficiais" e provenance.
- `ARSENAL INDEX.md`: sem mudança (description do owner não mudou materialmente).

## Segurança e portabilidade
Nenhum script foi executado (repositório clonado só para leitura). Na varredura: único subprocesso é `fc-list` (checagem de fonte japonesa); rede só para os hosts de ícones declarados e para a galeria (`share.py`). Pontos para quem instalar a skill original:
- a galeria é opt-in, oferecida uma vez, com dupla confirmação e aviso de dados internos — bom padrão, mesmo assim nunca publicar arquitetura da W1 ou de clientes;
- mantém por padrão o link "made with stack-diagram" no rodapé do HTML (fora do PNG);
- pacotes de ícones AWS/Google/Azure não devem ser versionados em repositórios;
- PNG exige `pip install playwright` + Chromium.

## Limites
Leitura documental; `tsx.md` e `template.html` não foram lidos por inteiro. Nenhum diagrama foi gerado para testar.

## Aceite futuro
Na primeira vez que o usuário pedir um diagrama de stack (ex.: arquitetura do reservasalas, do app de treino ou dos jogos), aplicar `architecture-visualization` com a referência nova. Se quiser os logos buscados e o render automáticos, instalar a skill original (no app Claude: subir `stack-diagram.zip` da página de Releases como skill; no Claude Code: `npx skills add caru-ini/stack-diagram`).
