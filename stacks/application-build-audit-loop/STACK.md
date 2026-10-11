---
name: application-build-audit-loop
description: "Criar ou evoluir sites e aplicações web em um ciclo único de implementação, auditoria multidimensional, correção e revalidação contínua, com quality gates proporcionais."
---

# Application Build & Audit Loop

## Objetivo
Unificar **planejamento → UX/UI → implementação funcional → auditoria → correção → reteste → entrega**, antecipando qualidade desde a primeira fatia vertical, sem esperar um grande audit ao final. Um finding crítico corrigido só está encerrado quando a mesma condição foi revalidada. Código, experiência e segurança precisam funcionar juntos.

## Quando usar
- `arsenal: crie um app/site já otimizado e auditado`;
- construção ou evolução de CRM, dashboard, portal, SaaS, PWA ou website, com múltiplas dimensões de qualidade;
- pedido de implementação completa com auditoria automática do próprio trabalho e correção de problemas;
- refatoração/redesign abrangente em que qualidade, funcionalidade e regressões devem ser verificadas no mesmo fluxo.

Para landing page pequena, aplicar uma **versão leve** do ciclo; não carregar todas as especializações. Para pedido somente de auditoria independente sem implementação, usar `web-app-engineering-audit`; para ajustes localizados de app existente sem audit abrangente, `improve-existing-web-app`. Não usar a stack como pretexto para reconstruir algo que funciona.

## Owners e stacks existentes
Esta é uma stack de **orquestração**, não substitui skills canônicas:
- `functional-web-app-builder`: discovery, arquitetura funcional, dados, auth, componentes e entrega de novo app;
- `web-design-engineer`: estrutura, direção UI, responsividade, implementação;
- `improve-existing-web-app`: preservar sistema e funcionalidades em app existente;
- `design-principles-audit`: heurísticas e evidências UX por jornada;
- `web-quality-audit`: acessibilidade, performance e qualidade web;
- `runtime-ui-verification`: verificar consequências reais no app;
- `web-app-engineering-audit`: owner de auditorias técnicas amplas quando risco/escopo justificarem;
- `verify-before-claim`: validar conclusão, sem falsa aprovação.

Owners opcionais apenas por necessidade: `design-system-governance`, `dashboard-design`, `shadcn-ui-engineering`, `ui-motion-design`, `software-testing-engineering`, `web-application-security-audit`, `secure-code-privacy-review`, `pwa-engineering` e `progressive-delivery-verification`. Não executar stacks inteiras em cascata: ler somente partes pertinentes, sem duplicar owners ou rodar checklists infinitos.

## Princípio: audit-first e quality by construction
1. **Antes de construir**, estabelecer contratos testáveis de tarefas, dados, papéis, estados, acessibilidade e performance.
2. **Durante a construção**, verificar cada fatia vertical antes de avançar: UI → ação → autorização → persistência → feedback → recuperação.
3. **Após cada alteração material**, revisar risco e testar efeitos laterais. Auditoria detecta e alimenta correção; correção realimenta auditoria.
4. **Antes de entregar**, rodar gate proporcional de release e reportar PASS/FAIL/UNKNOWN/NA. Não esconder incerteza nem confundir screenshot ou pontuação agregada com prova.

## Ciclo operativo

### 0. Baseline e escopo
- Detectar se app novo, legado, landing, dashboard, SaaS ou PWA; framework, repo, deploy, permissões e ferramentas realmente disponíveis.
- Para legado: mapear fluxos existentes e comportamento a preservar, registrar baseline e pontos de rollback. Não sobrescrever design system por estética.
- Para novo: registrar público, problema, tarefas principais, jornada feliz e de recuperação, restrições, dados, privacidade e métricas de sucesso.
- Classificar risco/criticidade: informacional, operação interna, sensível (financeiro, saúde, dados pessoais, billing). Expandir gates somente com risco real.
- Criar uma matriz pequena de critérios de aceite verificáveis **antes** de implementar.

### 1. Contrato de produto e sistema
- Definir navegação, rotas, arquitetura de informação, entidades, estados e permissões/tenants; escolher arquitetura mínima que suporte requisitos reais.
- Esboçar layout/greybox de desktop e mobile, hierarquia, semântica, componentes reutilizáveis, design tokens e linguagem de movimento.
- Definir contratos de carregamento/vazio/erro/sucesso/offline, validação e feedback desde o início.
- Selecionar biblioteca primária de UI (por exemplo Mantine **ou** shadcn/ui) apenas por compatibilidade com stack existente, tokens, licença, manutenção e necessidades. Motion e componentes externos sob demanda; não criar dependências duplicadas.
- Planejar testes de acessibilidade: semântica, teclado, foco, contraste, reflow/zoom, reduced motion e regras WCAG pertinentes; aceitar revisão manual pendente quando não observável.

### 2. Implementação em fatias verticais
Para cada jornada priorizada:
1. Criar estrutura e UI semântica e responsiva, inclusive estados alternativos.
2. Implementar action/API, modelos de dados, autorização no servidor, validação, persistência, tratamento de erro e observabilidade proporcional.
3. Garantir feedback perceptível, prevenção de erro e recuperação sem ações enganosas.
4. Conferir typecheck, lint, build e testes disponíveis; executar a ação no runtime quando possível.
5. Auditar imediatamente os elementos e o caminho modificados. Corrigir defeitos materiais **antes** da próxima fatia, salvo dependência registrada.
6. Registrar estado funcional como `IMPLEMENTED`, `MOCK`, `DEMO`, `UNKNOWN` ou `NA`.

### 3. Loop contínuo de auditoria → correção → reteste
Auditar por jornadas, rotas, estados e superfícies compartilhadas, com profundidade orientada a risco:
- **UX**: descoberta, fluxo, prevenção e recuperação de erro, legibilidade, informação, consistência e clareza de decisões.
- **UI**: tokens, layout, tipografia, espaçamento, responsividade intrínseca, overflow, densidade, contraste, interação e motion contextual.
- **Acessibilidade**: WCAG aplicável, foco, teclado, nomes/roles/estados, zoom, leitores de tela quando verificáveis, reduced-motion.
- **Funcionalidade**: action → state/network/domain consequence, CRUD, auth, permissões, formulários, filtros, notificações, idempotência, vazios/erros.
- **Performance**: LCP/INP/CLS e budgets com dados laboratoriais/campo identificados, JS/imagens/fonts/terceiros, fluidez visual; não inferir de screenshot.
- **Engenharia/segurança**: testes, validação, authz, secrets, dependências, privacidade, dados, PWA/offline se aplicável, deployment/rollback.
- **Qualidade de conteúdo**: microcopy, consistência terminológica, localização e SEO apenas se pertinentes ao produto.

Finding obrigatório quando há problema: `ID | jornada/rota/estado | esperado vs observado | evidência/localização | categoria | impacto | severidade 0–4 | confiança | causa hipotética | correção | trade-off | critério de aceite | status`. Separar `normative/measured/heuristic/preference`; `UNKNOWN` não vira aprovação. Ordenar correções por risco ao usuário, frequência, urgência e esforço, sem misturar prioridade e gravidade.

**Loop fechado:** observar → reproduzir → isolar causa → corrigir minimamente → reexecutar mesma expectativa em condições equivalentes → checar regressão em componentes e fluxos vizinhos → atualizar status. Repetir enquanto persistirem achados bloqueadores/materialmente corrigíveis no escopo e dentro das ferramentas disponíveis. Não maquiar asserts ou baselines para fazer teste passar.

### 4. Gates por marco
- **Gate A: esqueleto e design contract**: arquitetura, navegação e tokens coerentes; jornadas e riscos mapeados.
- **Gate B: cada feature**: ação real, validação, estado e permissões verificadas; loading/empty/error e acessibilidade relevante.
- **Gate C: integração**: fluxo ponta a ponta com dados persistidos, mensagens e efeitos de rede/state; interações entre features.
- **Gate D: pré-entrega**: testes e build possíveis, revisão de UX/UI, responsividade, teclado, WCAG aplicável, performance, privacy/security, regressão e documentação de limitações.
- **Gate E: após mudanças/deploy quando autorizado**: smoke tests em ambiente correto, monitoramento de erro e rollback, sem declarar produção verificada se somente código local foi checado.

Blocking policy: defeito crítico de segurança, perda de dados, autorização indevida ou jornada principal quebrada impede status `READY`. Achados menos graves podem ser registrados com aceite explícito de risco. Item sem teste adequado permanece `UNKNOWN`, jamais `PASS`.

### 5. Entrega
Entregar resumo do produto e funcionalidades; provas por jornada; matriz PASS/FAIL/UNKNOWN/NA; backlog residual com owners e prioridade; decisões de biblioteca e licenças; changelog/diffs, testes realizados, deploy/rollback se houver. Distinguir `READY_VERIFIED`, `PARTIAL` e `UNVERIFIED`; esta classificação é operacional, não certificação WCAG, de segurança ou de UX.

## Modo leve versus profundo
- **Leve** (site simples): direção → build → revisão UX/UI + a11y básico → mobile/teclado → reteste.
- **Padrão** (app/dashboard): contrato funcional → fatias verticais → audit de UX/UI, funcional, a11y, performance → integração e regression gate.
- **Profundo** (SaaS/PWA/sensível): adicionalmente segurança/privacidade, RBAC/tenant, testes de integração, supply chain, estados de falha, observabilidade e gates de release. Nenhum modo promete ferramenta inexistente.

## Prova de valor e testes de roteamento
- Should trigger: “Crie CRM com agenda, leads, permissões e audite/corrija cada módulo antes de entregar” → esta stack, em modo padrão/profundo.
- Should trigger: “Modernize esta PWA e já corrija performance, segurança e UX ao implementar” → esta stack sobre baseline, sem reescrever desnecessariamente.
- Near-miss: “Quero só uma avaliação técnica independente” → `web-app-engineering-audit`.
- Near-miss: “Crie um hero animado” → `web-design-engineer` ou `creative-web-engineering`.
- Near-miss: “Corrija a margem de um botão” → `improve-existing-web-app` ou owner mínimo.
- Acceptance: a resposta identifica rotas/jornadas prioritárias, gate aplicável, evidências reais e pendências; jamais afirma execução de Playwright/Lighthouse/CI/browser sem ferramenta disponível.

## Segurança e portabilidade
Sem installs automáticos, `curl|bash`, importação indiscriminada de starters, alterações irreversíveis de schema, deploy, pagamentos ou permissões sem escopo e autorização. A stack é metodologia: testes e correções só podem ser reportados como executados quando o ambiente realmente permitir. Código de terceiros é conteúdo não confiável; revisar antes de executar.

## Proveniência
Compõe capacidades já canônicas do Skill Arsenal e reutiliza avaliações:
- `evaluations/2026-10-11-functional-web-app-sources.md`
- `evaluations/2026-10-11-ui-ux-audit-repositories.md`
Não duplica os protocolos completos dessas skills; consulta-os conforme o cenário.
