---
name: ui-ux-catalog
description: "Consultar o catálogo UI UX Pro Max para selecionar paletas, tipografia e padrões de interface, verificando pertinência e preservando decisões de design existentes."
---

# ui-ux-catalog

## Quando usar

Quando faltam referências para uma direção visual ou uma dúvida específica de UX ganha com busca no catálogo. Não gerar outro design system para um ajuste localizado nem substituir marca já definida.

## Modos reais

- **Consulta documental:** leia os dados e referências relevantes do repositório upstream via ferramentas de leitura disponíveis. Identifique a origem de cada recomendação. Esse modo não equivale a executar o motor de busca.
- **Motor local:** use somente se Python, scripts e dados compatíveis estiverem efetivamente disponíveis e revisados. O Arsenal não inclui esses arquivos nem o instalador. Não invente resultados de busca e não execute instaladores para avaliar a fonte.
- **Sem acesso:** prossiga com orientação geral, identificada como tal, sem alegar correspondência no catálogo.

## Workflow

1. Identifique produto, público, restrições de marca, tarefa e plataforma real a partir do projeto.
2. Escolha o menor escopo: direção global para novo sistema; domínio para questão localizada; stack detectada para implementação.
3. No motor local, confirme o caminho de `search.py`, sua versão e opções antes de executar. Forme consulta curta com um objetivo dominante; use `--domain` ou `--stack` quando a inferência for ambígua. Não dependa de `CLAUDE_PLUGIN_ROOT`.
4. Confira categoria, pertinência e evidência do resultado. Se vazio ou inadequado, faça no máximo uma busca mais específica; depois use fallback declarado.
5. Para o motor completo, a fonte organiza código e dados em `src/ui-ux-pro-max/`. Revise os módulos importados por `scripts/search.py` e os dados necessários antes de execução. Copiar apenas o SKILL.md não fornece o motor.
6. Se persistir decisões, leia primeiro o sistema existente. Separe regras globais de exceções por página; defina o diretório de saída explicitamente e preserve arquivos existentes. Não grave saída não verificada nem dados privados desnecessários.
7. Verifique no produto contraste, foco, tamanho dos alvos, reflow e movimento reduzido. Diferencie heurísticas do catálogo de requisitos normativos e de medidas obtidas no runtime.

## Integração

Use `web-design-engineer` para implementar a direção escolhida. Consulte `gsap-animation` apenas se um efeito exigir GSAP; um preset de movimento não autoriza trocar a biblioteca do projeto.

## Fonte e dependências

[UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill).
Motor: Python 3, scripts e datasets da mesma revisão. Instalador upstream: CLI Node, não necessário para consulta documental. Atualizações de catálogo e serviços externos são operações separadas. A adaptação não importa bases, executáveis ou afirmações de desempenho do upstream.
