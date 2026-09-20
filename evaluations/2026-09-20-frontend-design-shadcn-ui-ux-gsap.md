# Avaliação: design de interfaces e animações

Data: 2026-09-20. Método: evaluate-and-import-skill + skill-security-review; adaptação conforme skill-creator. Autorização de aplicar e publicar ao final dada pelo usuário nesta data.

## Decisões aplicadas

| Fonte | Classe | Valor adicional e sobreposição | Destino |
|---|---|---|---|
| Anthropic frontend-design | B | Revisão do plano contra o tema, contenção visual e escrita de interface; sobrepõe web-design-engineer | Enriquecimento de web-design-engineer |
| shadcn/ui | D | Contexto real do projeto, composição por base, documentação e atualização com diff | shadcn-ui-engineering |
| UI UX Pro Max | D | Catálogo pesquisável e decisões globais com exceções por página | ui-ux-catalog, com consulta documental e motor local condicionado a dependências |
| GSAP Skills | D | Timelines, ScrollTrigger e ciclo de vida específicos | gsap-animation, com módulos upstream sob demanda |

Não criada nova stack: improve-existing-web-app recebeu roteamento condicional. As três skills novas são adaptações próprias, não cópias integrais nem instalação de pacotes.

## Revisão de segurança e portabilidade

- Frontend Design: APPROVE para a síntese metodológica própria. Retiradas persona, confirmações desnecessárias e proibições estéticas universais. O LICENSE.txt apontado pelo frontmatter não foi encontrado no diretório da skill; não redistribuído texto integral. Licença de uma futura cópia deve ser resolvida antes da cópia.
- shadcn: CAUTION para execução do original (CLI remoto e escrita em projetos/registries); APPROVE para a orientação adaptada sem execução. Removidas permissões de shell específicas do agente e contexto supostamente injetado. Origem, versão, diff e configuração real precedem alterações.
- UI UX Pro Max: CAUTION para instalar/executar o pacote completo, que não foi auditado integralmente. Lidos README, SKILL.md e entrada search.py; módulos importados, catálogo completo e instalador não foram validados em runtime. Adaptação documental utilizável; motor e datasets não incluídos nem apresentados como instalados.
- GSAP: APPROVE para adaptação documental; execução depende do projeto. Lidos README e módulos React/ScrollTrigger. Retirado gatilho de recomendar GSAP indiscriminadamente. Não importados o exemplo com Max.max, a mistura de unidades xPercent/pixels ou limpeza global indiscriminada.
- Revisão manual/documental; nenhum scanner automatizado de segurança nem instalador externo executado. Isso não certifica todos os arquivos upstream.

## Fontes e revisões consultadas

- [anthropics/claude-code](https://github.com/anthropics/claude-code/tree/7974a70773fa229e4cc65aa1b356cc21f5c216c4) — revisão observada: `7974a70773fa229e4cc65aa1b356cc21f5c216c4`.
- [shadcn-ui/ui](https://github.com/shadcn-ui/ui/tree/a87a63b2ca25143d26c8bd0903e4e9bc77b3f824) — revisão observada: `a87a63b2ca25143d26c8bd0903e4e9bc77b3f824`.
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/de5f12b400775997d213524ef02a7c7d2746806f) — revisão observada: `de5f12b400775997d213524ef02a7c7d2746806f`.
- [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760) — revisão observada: `aed9cfd3277740755f6bfc1155c7aa645403b760`.

Arquivos principais: plugins/frontend-design/skills/frontend-design/SKILL.md; skills/shadcn/SKILL.md; .claude/skills/ui-ux-pro-max/SKILL.md e src/ui-ux-pro-max/scripts/search.py; skills/gsap-react/SKILL.md e skills/gsap-scrolltrigger/SKILL.md. As fontes evoluem; verificar a versão antes de reutilizar APIs.

## Critérios de aceitação

Frontmatter e nomes válidos, índice com as três novas entradas, referências internas existentes, preservação do conteúdo anterior e publicação sem force-push. Nenhum aplicativo consumidor foi alterado ou testado; a entrega é a biblioteca de instruções.
