# Avaliação — quatro referências de UI para o Arsenal

Data: 2026-09-28 (America/Sao_Paulo).
Fluxo: arsenal-router → arsenal-autopilot; revisão proporcional de segurança e verificação pós-publicação.
Base consultada: cb82dc97a5aa023b865cfefbe385024eb2e534c7.

## Decisão

Adotar as quatro como referências externas condicionais. Classificação D: recursos técnicos que exigem código e runtime no projeto consumidor. Não são prompts sofisticados nem skills autônomas. Nenhuma instalação ou nova stack se justifica neste lote.

| Fonte | O que entrega / ganho real | Quando usar | Decisão / ownership |
| --- | --- | --- | --- |
| Beautiful UI | Padrões de UI para assistentes, tarefas, aprovação e proveniência | Produtos com IA e interfaces de revisão | KEEP_EXTERNAL_REFERENCE; web-design-engineer |
| OriginKit | Componentes e composição de páginas com preview ajustável | Landing pages e elementos visuais específicos | KEEP_EXTERNAL_REFERENCE com limite de licença; web-design-engineer |
| coss ui | Sistema React com Base UI e Tailwind v4, fonte editável | Controles consistentes de aplicações | KEEP_EXTERNAL_REFERENCE; nota de integração em shadcn-ui-engineering |
| Bencho | Repertório de comportamento interativo | Refinamento de UI já funcional | KEEP_EXTERNAL_REFERENCE; interaction-polish |

Valor além das capacidades normais do assistente: exemplos concretos e documentação de componentes reduzem invenção de APIs/estados e aceleram seleção. O valor depende de consultar a fonte e validar a integração; links não instalam capacidades.

## Compatibilidade e overlap

O Arsenal já possui owners para construção web, composição de componentes e polish. Atualizar esses owners é suficiente. Nenhuma nova metodologia independente foi demonstrada. A menor combinação útil por projeto é uma base de UI já compatível mais um padrão pontual quando necessário.

Heurística de aplicação, não benchmark: coss como candidata a base de controles; Beautiful UI para camada de assistente; OriginKit para composição visual; Bencho para microinterações. Não instalar as quatro em conjunto por padrão.

## Dependências, licenças e limites

- Beautiful UI: MIT declarada na página oficial. Manifesto/dependências universais não confirmados; conferir item obtido.
- OriginKit: código exige conta; CLI depende de Node; MCP/autenticação são externos e opcionais. Licença própria permite uso em aplicações, mas restringe distribuição como templates/kits/catálogos. Registrar somente links/notas no Arsenal.
- coss: React, Base UI, Tailwind v4; CLI shadcn ou cópia manual. A área apps/ui tem MIT; o monorepo tem licença padrão AGPL. Sem equivalência automática com Radix. Não confundir coss origin com OriginKit.
- Bencho: blocos exportados MIT; fotos, marca e aplicação ao redor têm condições distintas. Framework/imports devem ser conferidos por bloco.

Segurança: APPROVE para registro de referências e notas; CAUTION para futura integração de código ainda não auditado. Nenhum installer, MCP, pacote ou script externo foi executado. Nenhum projeto consumidor foi modificado. Não houve auditoria integral de supply chain nem certificação de acessibilidade.

## Alterações

- Atualizar web-design-engineer com rota para catálogo sob demanda.
- Acrescentar notas estreitas em shadcn-ui-engineering e interaction-polish.
- Criar referência central em skills/web-design-engineer/references/ui-component-references.md.
- Manter nomes/descriptions e ARSENAL INDEX.md: as três rotas já existem e não mudaram de escopo material.
- Registrar esta avaliação; não copiar catálogo/código nem criar quatro skills.

## Casos de aceitação (revisão documental)

- Pedido de painel com assistente: localizar Beautiful UI; exigir estados/dados reais, sem prometer backend.
- App React com formulário: avaliar coss compatível com versões; não usar API Radix por suposição.
- Landing page: avaliar OriginKit; conferir conta, dependências e licença.
- Card que precisa de feedback: consultar Bencho por meio de interaction-polish e manter teclado/toque.
- Starter kit redistribuível: não incorporar OriginKit sem permissão adequada.
- Site HTML simples já funcional: não forçar React/Tailwind para imitar referência.
- Pedido genérico de visual moderno: selecionar somente fonte pertinente, não instalar o lote.

Verificação prevista: leitura exata dos cinco arquivos na branch master após publicação, links relativos existentes e frontmatter preservado. Esta avaliação não constitui teste de runtime dos fornecedores.

## Fontes primárias

- https://www.beautifului.dev/
- https://www.beautifului.dev/license
- https://www.originkit.dev/docs/components
- https://www.originkit.dev/docs/licensing
- https://coss.com/ui/docs
- https://coss.com/ui/docs/get-started
- https://coss.com/ui/docs/radix-migration
- https://github.com/cosscom/coss/blob/main/apps/ui/README.md
- https://github.com/cosscom/coss/blob/main/LICENSING.md
- https://bencho.dev/
- https://bencho.dev/licence

Algumas páginas renderizadas tiveram extração direta vazia; os documentos de OriginKit e os termos de Bencho foram recuperados por busca nas próprias fontes oficiais. Não houve inspeção visual interativa; conclusões limitadas à documentação e catálogo textual.
