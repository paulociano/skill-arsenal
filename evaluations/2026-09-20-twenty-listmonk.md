# Avaliação — Twenty e listmonk

Data: 2026-09-20

## Fontes

- https://github.com/twentyhq/twenty
- https://github.com/knadh/listmonk

Fluxo: evaluate-and-import-skill + skill-security-review.

Nenhum installer, container, binary, CLI, MCP server ou código externo foi executado.

## Decisão resumida

- não criar nova skill;
- absorver governança de skills multi-harness do Twenty em project-skill-architecture;
- absorver lifecycle de audiência, estados de campanha, bounce handling e operação self-hosted do listmonk em email-campaign-engineering;
- não atualizar ARSENAL INDEX porque nenhuma skill foi criada/renomeada e nenhuma description mudou.

## Twenty

### Classificação

B/D.

### O que faz

Twenty é um CRM open source extensível. O repositório também mantém famílias oficiais de Agent Skills para criar, desenvolver, operar e publicar apps Twenty, além de skills para consultar workspaces via MCP.

### Valor metodológico

O ganho portátil não é como usar Twenty, mas como estruturar skills de um produto complexo:

- skills e references canônicas em uma fonte;
- distribuições geradas separadas da fonte;
- configuração específica de Codex/harness fora do conteúdo canônico;
- famílias separadas por audiência;
- distinção entre ler workspace via MCP e modificar app por código;
- approval explícito para deploy/production/destructive operations;
- credenciais e workspace URLs permanecem user-local.

Isso reforça diretamente project-skill-architecture.

### Segurança

CAUTION.

O produto oferece CLI, publishing, deploy, MCP, OAuth, API keys e sync contra workspaces remotos. Essas capacidades são legítimas para o produto, mas têm efeitos externos e credenciais. Nenhuma foi executada ou importada como dependência.

### Decisão

Não importar as skills Twenty para o Arsenal global, porque são fortemente específicas ao produto. Adaptar apenas os princípios de canonical source, generated distribution, audience routing e private target configuration em project-skill-architecture.

## listmonk

### Classificação

B/D.

### O que faz

listmonk é um gerenciador self-hosted de newsletters e mailing lists, com listas, subscribers, subscriptions, opt-in, campanhas com lifecycle explícito, SMTP e bounce handling.

### Valor metodológico

email-campaign-engineering já cobria copy, HTML e approval antes de envio, mas estava mais fraca na camada operacional.

Foram incorporados:

- subscriber versus subscription state;
- confirmação, unsubscribe e suppression;
- campaign states como draft, scheduled, running, paused, cancelled e finished;
- hard/soft bounce e complaints;
- sender/provider routing;
- self-hosted não reduz requisitos de consentimento ou deliverability.

### Segurança

CAUTION.

A implementação envolve SMTP, banco PostgreSQL, credenciais administrativas, importação de listas e envio em massa. O compose de exemplo usa defaults adequados apenas para desenvolvimento e imagem latest. Nada foi executado.

### Decisão

Não criar skill listmonk-specific. Reforçar email-campaign-engineering de forma provider-neutral.

## Mudanças aplicadas

- project-skill-architecture: canonical skills vs generated distributions, audience routing, read/write boundary e secrets user-local;
- email-campaign-engineering: audience lifecycle, campaign state machine, delivery routing e bounce handling;
- registro desta avaliação.

## Limites

- revisão manual;
- nenhum envio, deploy, MCP setup ou container foi executado;
- documentação de produto foi usada apenas para extrair princípios reutilizáveis.
