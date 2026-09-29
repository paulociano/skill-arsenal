# Referências de componentes: Beautiful UI, OriginKit, coss ui e Bencho

Consulta: 2026-09-28. Revalidar documentação, licença e dependências ao integrar.
Owner deste catálogo: web-design-engineer. Estas fontes são referências técnicas externas (D), não novas skills nem bibliotecas obrigatórias.

## Seleção por problema

| Necessidade | Referência candidata | Owner de execução | Limite |
| --- | --- | --- | --- |
| Interface de assistente, estados de tarefa, aprovação, fontes e streaming | [Beautiful UI](https://www.beautifului.dev/) | web-design-engineer | UI não implementa agente, retrieval, permissões ou backend |
| Landing page, seção ou componente visual ajustável | [OriginKit](https://www.originkit.dev/) | web-design-engineer; landing-craft se pertinente | Conta para obter código; licença própria restringe redistribuição |
| Formulários, menus, calendários e controles de aplicação React | [coss ui](https://coss.com/ui) | shadcn-ui-engineering quando integração usa seu registry/CLI | Base UI e Tailwind v4; não assumir API Radix |
| Feedback de press/drag, seleção, confirmação e reorder | [Bencho](https://bencho.dev/) | interaction-polish | Validar teclado/toque; fotos da demo não estão incluídas na licença dos blocos |

Escolher uma base coerente com o projeto. Acrescentar somente os padrões que resolvam uma necessidade concreta. Não combinar quatro sistemas visuais por padrão, trocar a stack por aparência ou criar uma skill por fornecedor.

## Beautiful UI

Catálogo voltado a interfaces com IA: approval cards, context cards, task rows, composer, streaming, tabelas e sugestões. Valor incremental: repertório de estados, proveniência e controle do usuário, além de chat genérico.

Usar status e eventos reais. Não simular execução, fontes, precisão de confiança, progresso ou aprovação efetiva com dados de demonstração. Representar atividade por resumos públicos e eventos observáveis, não expor raciocínio privado. Conferir o código e suas dependências no componente obtido; a análise do catálogo não confirmou um manifesto universal.

[Licença MIT](https://www.beautifului.dev/license): preservar avisos aplicáveis em cópias substanciais.

## OriginKit

A documentação distingue componentes, seções e templates. Componentes podem ser adaptados para React/Vite/Next.js e Framer; suporte Framer não se estende automaticamente às seções/templates. Ajustar controles e conferir viewports antes de obter o código. Dependências são específicas do item.

[Documentação](https://www.originkit.dev/docs/components): explorar é aberto; obter código exige conta. CLI requer Node; autenticação e cotas variam por canal/plano. MCP é opção externa documentada, não uma capacidade instalada do Arsenal. Não configurar ou executar CLI/MCP só para avaliar.

[Termos](https://www.originkit.dev/docs/licensing): permitem aplicações e trabalhos para clientes, mas restringem redistribuir componentes em templates, themes, starter kits e catálogos, inclusive gratuitos/modificados, salvo permissão adequada. Manter no Arsenal links e notas próprias; não espelhar código nem disponibilizá-lo como catálogo para outros agentes. Revalidar os termos para o uso concreto.

## coss ui

React, Base UI, Tailwind CSS v4 e distribuição de fonte via cópia/registry compatível com shadcn CLI. Candidata para aplicações densas e consistentes; não substitui modelagem de dados, autenticação ou APIs.

- Inspecionar componentes locais, aliases, versões, tokens e dependências antes de incorporar.
- Evitar setup completo em app existente quando um componente basta: presets podem alterar tema e fontes.
- Base UI não é Radix. Verificar composição e estado por componente; usar `render` onde suportado em vez de substituir `asChild` mecanicamente.
- Ler [migração](https://coss.com/ui/docs/radix-migration) e [setup](https://coss.com/ui/docs/get-started) atuais.
- [Licenciamento do repositório](https://github.com/cosscom/coss/blob/main/LICENSING.md): `apps/ui/` e `apps/origin/` têm MIT; o padrão do monorepo é AGPL. Verificar o caminho exato de qualquer fonte copiada.

Não confundir coss origin (`apps/origin/`) com originkit.dev: são fontes diferentes.

## Bencho

Galeria de blocos interativos com exemplos de comparação de imagens, menus, checklist, upload, confirmação e reorder. Usar como referência de comportamento para interações prioritárias.

Adaptar timing e estilo à biblioteca já presente. Não tornar hover/drag a única maneira de executar uma ação; fornecer alternativa por teclado e toque, foco visível, reduced motion e cancelamento/undo quando pertinentes. Não presumir framework ou dependências de todo o catálogo sem ler o bloco específico.

[Licença](https://bencho.dev/licence): blocos/código exportado sob MIT; a aplicação Bencho, marca e fotos não estão cobertos da mesma maneira. Trocar imagens por assets autorizados; respeitar licenças de fontes e dependências.

## Gate de incorporação

1. Identificar tarefa e componente exatos; manter referências de URL/data/versão quando disponíveis.
2. Conferir licença do código, assets e dependências separadamente.
3. Ler imports, rede, persistência, event handlers e permissões antes de executar.
4. Integrar ao sistema de tokens existente, sem sobrescrever customizações.
5. Validar estados realistas, teclado, foco, toque, responsividade, reduced motion e custo de renderização.
6. Declarar o que foi somente pesquisado e o que foi executado/testado.

Esta avaliação foi documental, sem instalação, auditoria completa do código, benchmark ou teste interativo de acessibilidade.
