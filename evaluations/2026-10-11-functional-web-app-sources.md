# Avaliação: fontes para criar web apps completos e interfaces modernas (2026-10-11)

## Fonte canônica e escopo
Índice lido primeiro: `ARSENAL INDEX.md` (GitHub oficial). Owners analisados: `web-design-engineer`, `ui-ux-catalog`, `shadcn-ui-engineering`, `creative-web-engineering` e `improve-existing-web-app`. Nova lacuna confirmada: fluxo explícito de criação end-to-end de **app funcional** (UI + dados + contratos + segurança + operação), distinto de site criativo ou melhoria de app existente.

## Fontes primárias verificadas
README e LICENSE foram lidos dos respectivos repositórios GitHub em 2026-10-11.

| Repositório | Classe | Evidência no README | Licença | Decisão |
| --- | --- | --- | --- | --- |
| https://github.com/mantinedev/mantine | A/D | 100+ componentes, 80+ hooks, form, charts, notifications, Spotlight, dropzone, modals, schedule | MIT | Referência de biblioteca coesa para apps funcionais; sem importação massiva |
| https://github.com/Kiranism/next-shadcn-dashboard-starter | A/D | Next 16/shadcn/Base UI, forms, Zod, TanStack Query/SSR, tabelas URL-synced, auth/billing | MIT | Absorver metodologia de fluxos reais, cache/invalidation e contratos |
| https://github.com/openstarterkit/nextjs-saas-starter-kit | A/D | Next 16, Better Auth, Prisma/Postgres, Stripe, emails, admin, i18n, demo | MIT | Referência de arquitetura SaaS modular e diferenciação demo/produção; verificar segurança |
| https://github.com/ColorlibHQ/velora-ui | B/D | 100 componentes animados, template multipágina, tamanho/dependências/reduced-motion documentados | MIT | Absorver escolha por custo, a11y e fit; manter como catálogo externo |

Adoção não implica aprovar qualidade real, ausência de vulnerabilidades nem compatibilidade futura. Relatos do README são claims dos autores, não testes independentes.

## Riscos e limites
- OpenStarterKit documenta no changelog de 2026-10-03 correção urgente relacionada a Better Auth, magic-link/OAuth. Revisar advisories, versões e configurações antes de usar base SaaS; jamais considerar auth segura só porque starter diz production-ready.
- Mantine e shadcn/UI são sistemas alternativos de componentes: não recomendar instalação simultânea por default.
- Velora é orientado a React/Next, Tailwind, Motion; conferir licença efetiva dos assets, API e primitives antes de copiar itens.
- Templates dependem de serviços externos, segredos, migrations, autorização e testes; sem instalação/execução nesta pesquisa.
- Nenhum script, starter, CLI, dependência, hook ou token externo foi executado ou copiado.

## Capability ledger e ownership
| Capability | Owner |
| --- | --- |
| Interface responsiva, visual direction e layout | `web-design-engineer` (existente) |
| Design system e componentes | `design-system-governance`, `shadcn-ui-engineering` quando aplicável |
| Site expressivo, animações | `creative-web-engineering` (existente) |
| Aplicação nova ponta a ponta, capacidades, dados, estados e produção | `functional-web-app-builder` (nova stack) |
| Auditoria e runtime | `design-principles-audit`, `runtime-ui-verification`, `web-quality-audit` |
| Melhorar aplicação já existente | `improve-existing-web-app` |

Decisão `CREATE_NEW` apenas para a stack, porque nenhum owner/stack atual organiza esse fluxo end-to-end específico. Para as quatro fontes: `ABSORB_METHOD_ONLY` + `KEEP_EXTERNAL_REFERENCE`; não criar novas skills derivativas.

## Should-trigger / near-miss
- `arsenal: crie CRM responsivo, com autenticação, organização, dados, formulários e dashboard` → stack funcional; contratos por feature, auth server-side, reteste.
- `arsenal: crie plataforma SaaS de agendamento com perfis, pagamento e notificações` → stack funcional, apenas serviços necessários e dependências verificadas.
- `arsenal: crie uma landing page premium animada` → preferir `creative-web-engineering` / `web-design-engineer`; não carregar stack full-stack.
- `arsenal: redesenhe app existente sem quebrar comportamento` → preferir `improve-existing-web-app`.
- `arsenal: mostre uma tela inspirada no Mantine` → direção visual; não instalar backend.
- Sem browser/CI disponível → marcar testes `UNKNOWN`, não afirmar resultado em runtime.

## Verificação e resultados
Registros publicados no GitHub: stack nova e roteamento no índice. O fluxo foi revisado documentalmente; **nenhum app foi construído ou testado em execução** durante esta avaliação. Próxima validação empírica: executar os cenários above com repositório de app de exemplo, medir resultado e corrigir lacunas verificadas.
