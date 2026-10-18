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

## Seleção contextual e saída auditável (UI UX Pro Max v2)

Quando consultar o upstream, considerar seus grupos **categoria de produto, estrutura de página, estilo, paleta, tipografia e stack** como dimensões independentes. A combinação é recomendação inicial, não sistema comprovadamente correto:
1. Verificar se o resultado reflete produto, missão do usuário, marca, conteúdo, densidade de dados e padrões esperados na plataforma.
2. Explicitar **por quê** pattern, type roles e color roles funcionam juntos; rejeitar combinações de catálogo quando prejudicarem hierarquia, legibilidade ou identidade.
3. Separar restrição comprovada (contraste medido, foco, reflow) de antipattern por gosto (banimento de cor/fonte/estilo). Não tratar contagem de regras e estilos do README como evidência de qualidade.
4. Entregar um contrato pequeno: escolha, alternativas descartadas, tokens semânticos sugeridos, componentes/states e validação planejada. Somente persista como DESIGN.md após checar owner canônico.
5. Caso o motor Python não seja executado, rotular decisões como **síntese documental**, nunca como ranking/resultado do mecanismo BM25.

Proveniência: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), README v2 consultado em 2026-10-17. Nenhum CLI, instalador, dataset ou ferramenta do upstream foi executado.

## Catálogos interativos de componentes (Lucian)

Quando for útil consultar exemplo de UI, avaliar código e comportamento do componente, não só screenshot: estados default/disabled/loading/error, input por teclado/toque, foco, responsividade, dark/light e reduced motion. Mapear tokens e escopo CSS/JS para o design system vigente; testar a versão portada com dados reais e não copiar efeitos que quebrem acessibilidade. Inspecionar scripts antes de incorporar; preservar atribuição e licença da fonte. Fonte: https://github.com/Seokwoooo/lucian-uxui-prompt (2026-10-18). A galeria anunciada de 400 exemplos não foi testada aqui.
