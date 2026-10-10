# Avaliação de pbakaus/impeccable (2026-10-10)

Fonte: https://github.com/pbakaus/impeccable (README.md, skill/SKILL.src.md, PRODUCT.md, DESIGN.md, LICENSE). Avaliação documental pelo arsenal-autopilot, confrontada com ARSENAL INDEX.md.

## Classificação

**A/D: metodologia útil com runtime técnico opcional**. O design guidance é portável; os 24 comandos, 59 regras determinísticas, browser live mode, binário, hooks e extensão dependem da infraestrutura própria e não podem ser assumidos no ChatGPT.

## Capacidades e ownership

- PRODUCT.md para fatos duráveis do produto, distinto de DESIGN.md, que documenta direção/tokens por superfície: **UPDATE_EXISTING** em `web-design-engineer`. Não impor novos arquivos a projetos simples.
- Quatro modos por superfície (Persuade, Operate, Read, Experience), em vez de um estilo por produto inteiro: **UPDATE_EXISTING** em `web-design-engineer`.
- Ciclo de QA com inspeção agrupada, reparo e confirmação limitada: **UPDATE_EXISTING** em `web-design-engineer`; limite de polish não derroga testes mandatórios.
- 59 detectores e CLI/browser: **KEEP_EXTERNAL_REFERENCE**; sem execução, instalação, pacote ou hooks. Distinguir checks objetivos de crítica heurística.
- Comandos de layout, tipos, motion, adaptação, hardening, critique, audit e refine: **REJECT_DUPLICATE**; owners existentes incluem `web-design-engineer`, `design-principles-audit`, `design-system-governance`, `web-quality-audit`, `interaction-polish`, `ui-motion-design`, `design-direction`.
- Proibições gerais de fontes, gradientes, preto/cinza ou easing: **REJECT** como dogmas estéticos; brief, identidade e evidências prevalecem.

## Revisão de segurança/portabilidade

O instalador npm, o launcher com download de binário, hooks específicos de agentes e modo live exigem análise dinâmica de supply chain, permissões, privacidade e escopo antes de uso; não foram executados. A licença de origem é Apache-2.0, com obrigações próprias em redistribuição. Adotada apenas paráfrase curta de metodologia com atribuição; não copiados scripts nem regras da CLI. O número de detectores e comandos foi obtido do README, não verificado por execução.

## Mudanças efetivadas

Atualizada `skills/web-design-engineer/SKILL.md`: seção Produto, superfície e QA limitado (Impeccable). Não foi criada nova skill ou stack; o índice permanece válido sem mudança de rotas/descriptions. Nenhuma instalação externa e nenhuma modificação a projetos consumidores.

## Teste de incremento

Deve ativar: revisão de um app já existente com ambiguidade entre preservar produto e trocar visual, múltiplas superfícies e necessidade de QA em runtime.

Não deve ativar: ajuste de cor isolado, backend-only, ou pedido que não envolve UI.

Critério de aceitação: produto e visual ficam separados, escopo preservação/redesign explicitado, checks técnicos separados de julgamentos heurísticos e QA com evidências; sem prometer CLI externa.

Links:
- https://github.com/pbakaus/impeccable/blob/main/README.md
- https://github.com/pbakaus/impeccable/blob/main/skill/SKILL.src.md
- https://github.com/pbakaus/impeccable/blob/main/PRODUCT.md
- https://github.com/paulociano/skill-arsenal/blob/master/skills/web-design-engineer/SKILL.md
