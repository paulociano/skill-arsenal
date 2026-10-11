---
name: functional-web-app-builder
description: "Construir aplicações web funcionais com UX/UI moderna, arquitetura, dados, autenticação, componentes, estados e verificação real, escolhendo apenas as dependências justificadas."
---

# Functional Web App Builder

## Objetivo
Construir web apps completos e manteníveis, visualmente coerentes e acessíveis, com fluxos reais e integração entre frontend, dados e backend. Evitar confundir template bonito com produto pronto, ou empilhar bibliotecas em nome de modernidade.

## Quando usar
- novo CRM, portal, ferramenta interna, app operacional, dashboard interativo ou SaaS;
- pedido de app/site com muitas funcionalidades conectadas a dados reais;
- implementação end-to-end que exige auth, permissões, forms, CRUD, estados de rede e verificação;
- pedido explícito por UX/UI moderna **e** comportamento funcional.

Não ativar a stack completa para landing page estática, componente isolado ou redesign cosmético. Para site predominantemente editorial/expressivo, preferir `web-design-engineer` ou `creative-web-engineering`. Para app já existente, preferir `improve-existing-web-app` preservando arquitetura, salvo autorização explícita de reconstrução.

## Owners candidatos (somente conforme necessidade)
- `web-design-engineer`: visual thesis, greybox, responsividade, implementação UI;
- `design-direction`, `design-system-governance`: identidade, tokens e contrato durável;
- `shadcn-ui-engineering`: quando shadcn realmente escolhido ou existente;
- `dashboard-design`: vistas de decisão, métricas e exceções;
- `design-principles-audit`: revisão heurística e jornadas críticas;
- `ui-motion-design` / `interaction-polish`: movimento funcional e refinamento;
- `runtime-ui-verification`: ações e consequências observáveis;
- `web-quality-audit`: WCAG aplicável, responsividade, performance;
- `verify-before-claim`: gate final de evidência.

Outras competências de segurança, modelagem de domínio, testes, privacidade e engenharia entram apenas se apontadas pelo índice e pelo risco.

## Pipeline
1. **Descoberta e contrato**: especificar público, jornadas principais, entidades, tipos de dados, papéis, permissões, integrações, ambientes, riscos e acceptance criteria. Separar must-have do opcional. Não escolher framework pelo hype.
2. **Escolha de base**: inspecionar stack/código existente. Definir se é site, dashboard, app interno, SaaS multi-tenant ou CMS; justificar build versus adaptação. Verificar licença, maturidade, security advisories, versões, lockfile, manutenção e compatibilidade com deploy.
3. **Design first**: estabelecer direção visual e tokens, estrutura das rotas, hierarquia de informação, navegação, jornadas completas, responsividade intrínseca, loading/empty/error/offline/permission states. Não confundir muitas telas com UX consistente.
4. **Matriz de funcionalidade**: para cada recurso definir UI, modelo/owner de dados, contrato de API, validação, autorização, loading/error, persistência, cache/invalidation, falhas, observabilidade e teste.
5. **Sequenciamento vertical**: executar um fluxo ponta a ponta pequeno, com dados reais ou mock explicitamente identificado. Validar antes de replicar padrões. Componentes reutilizáveis surgem de repetição concreta, não abstração antecipada.
6. **UI e interações**: escolher uma biblioteca primária de componentes. Adicionar componentes de outras fontes apenas quando compatíveis com primitivos, tokens, estilos, SSR e licença. Formularios acessíveis, navegação por teclado, feedback e recuperação são comportamento, não acabamento.
7. **Auth e segurança**: autorização verificada no servidor, isolamento por organização/tenant, políticas de acesso, sessão/CSRF conforme arquitetura, segredos fora do cliente, validação do input e auditoria de dependências. Billing, auth e webhook templates não são seguros por herança.
8. **Qualidade verificável**: typecheck/lint/build e testes de fluxos críticos quando ferramentas disponíveis. Testar ações no app real, estado final, mobile/desktop, teclado, zoom, reduced-motion, acessibilidade e regressões. Não alegar teste que não rodou.
9. **Operação**: preparar migrações, envs, backups, monitoramento, erro, rollback, deploy e documentação somente na proporção necessária. Confirmar ambiente e acesso antes de ações externas.
10. **Entrega**: relatar o que funciona, o que é mock, dependências/serviços externos, testes realizados, lacunas/UNKNOWN e próximos passos; não chamar demo de produção.

## Catálogo de capacidades sob demanda
Selecionar funcionalidades pelo trabalho do usuário e mapa de dados, não por disponibilidade:
- autenticação, MFA, papéis, organizações e permissões;
- CRUD, tabelas (busca/filtro/ordenação/paginação), formulários, uploads;
- dashboards, gráficos, relatórios, exportação e auditoria de ações;
- calendários, agendamentos, notificações, centro de comandos e atalhos;
- conteúdo administrável, editor, busca e internacionalização;
- billing, assinaturas, webhooks e entitlements;
- sync, cache, optimistic UI e modo offline quando viável;
- logs, métricas de produto, analytics e tratamento de falhas.

Para cada item marcar `IMPLEMENTED/DEMO/MOCK/UNKNOWN/NOT_APPLICABLE` e teste de aceitação; não inventar progresso.

## Escolha tecnológica por fit
- **Mantine**: React com muitas funções integradas (forms, charts, dropzone, spotlight, notifications, schedule etc.); escolher quando coesão e velocidade compensarem adoção do sistema visual.
- **shadcn/ui**: controle e customização com ownership do código; bom quando o projeto já usa Tailwind/primitivos compatíveis e quer design próprio.
- **Kiranism next-shadcn-dashboard-starter**: referência de integração real de forms, server prefetch, cache, tabelas com URL state; usar como ponto de partida só se stack, auth e dependências fizerem sentido.
- **OpenStarterKit**: referência para SaaS Next.js com Better Auth, Prisma, PostgreSQL, Stripe e administração. Avaliar cada integração, segurança e versão antes de reutilizar.
- **Velora UI**: componentes e templates expressivos para React/shadcn; selecionar individualmente por custo, acessibilidade, reduced motion e coerência com design system. Não adicionar motion a fluxos operacionais por decoração.

Não combinar Mantine e shadcn como defaults simultâneos; uma biblioteca primária evita duplicar tokens, CSS, regras de foco e dependências. Bibliotecas de tabelas, gráficos e calendário entram após exigência real.

## Gate de qualidade
Cada jornada crítica deve ter: intenção do usuário, entrada, decisão, ação, resultado de domínio, estado de erro/recuperação, contrato de permissão, evidência e status.
- **UX**: descoberta, fluxo, feedback, redução de atrito e legibilidade;
- **UI**: consistência de tokens, estados, breakpoints, conteúdo longo;
- **A11y**: semântica, foco, teclado, contraste, zoom, reduced motion;
- **Funcional**: persistência, autorização, validação, falhas e idempotência;
- **Performance**: budgets proporcionais e comparação reprodutível;
- **Operacional**: segredos, atualização de dependências, logs e recuperação.

Falha em gate crítico impede alegação de produto pronto. Teste automatizado não prova conformidade WCAG total nem qualidade com usuários reais.

## Dependências e segurança
Não rodar `curl | bash`, `npx ...@latest`, clone, migrations ou instaladores de repositórios externos sem necessidade real e revisão. A stack descreve métodos, não garante que o ChatGPT tem shell, navegador, CI, credenciais, acesso de deploy, licenças de assets ou integração backend. Confirme capacidade e autorização antes de mutações externas.

## Referências externas
- https://github.com/mantinedev/mantine — biblioteca React integrada, MIT;
- https://github.com/Kiranism/next-shadcn-dashboard-starter — padrões de dashboard funcional, MIT;
- https://github.com/openstarterkit/nextjs-saas-starter-kit — SaaS funcional; atenção a advisories de auth, MIT;
- https://github.com/ColorlibHQ/velora-ui — custo/dependências por componente e reduced motion, MIT.

Estas fontes são **referências**, não dependências da stack. Consulte avaliação `evaluations/2026-10-11-functional-web-app-sources.md`.
