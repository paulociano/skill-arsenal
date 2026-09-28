---
name: production-go-live
description: "Planejar e executar a ida de uma aplicação para produção com inventário de dependências, approval gates, verificação, handoff, drift check e teardown seguro."
---

# production-go-live

## Objetivo

Levar uma aplicação de desenvolvimento para produção sem tratar deploy como um único botão. O fluxo cobre descoberta, plano, aprovação, execução, verificação, registro de ownership, handoff e eventual teardown.

## Quando usar

- publicar uma aplicação nova;
- conectar hosting, banco, auth, domínio, email, pagamentos ou outros serviços de produção;
- revisar um processo de lançamento;
- preparar handoff operacional de uma aplicação;
- auditar drift ou remover recursos criados por um lançamento anterior.

Não usar para simples preview/local build. Para arquitetura do sistema, combinar com `system-design-engineering`. Para release já configurado e sem mudança de infraestrutura, usar apenas a menor parte necessária deste fluxo.

## Princípios

1. **Detect before configure.** Primeiro identificar o que a aplicação já usa e quais dependências faltam.
2. **Plan before write.** Toda mudança externa relevante deve aparecer em um plano legível antes de execução.
3. **Approval is bound to the plan.** Mudança material de destino, provider, conta, versão ou parâmetros invalida a aprovação anterior.
4. **Verify observable behavior.** Deploy acionado não prova que a aplicação funciona.
5. **Ownership must be explicit.** Registrar o que foi criado, onde, por quem e como remover ou recuperar.
6. **No silent leftovers.** Teardown só afirma remoção do que pode verificar; resíduos desconhecidos ficam explícitos.
7. **Secrets stay out of artifacts.** Planos, relatórios e handoffs devem registrar nomes/fingerprints/metadados, não valores secretos.

## Workflow

### 1. Detect

Inventariar:
- runtime e build;
- hosting;
- banco e migrations;
- auth;
- storage;
- domain/DNS;
- email;
- pagamentos;
- queues/cron/webhooks;
- env vars e secrets necessários;
- dependências já provisionadas.

Separar `observed`, `inferred` e `missing`.

### 2. Resolve destination

Para cada recurso, definir:
- provider;
- conta/projeto/ambiente;
- região quando material;
- sandbox/test/live;
- domínio/hostname;
- ownership humano.

Nunca inferir que um destino é de teste apenas pelo nome.

### 3. Plan

Produzir plano ordenado com:
- writes exatos;
- prerequisites;
- dados que podem ser afetados;
- approval gates;
- checks pós-etapa;
- rollback possível;
- etapas manuais;
- itens irreversíveis ou não automatizáveis.

### 4. Approval gate

Antes de writes externos consequenciais, exigir autorização compatível com o escopo. Aprovação deve estar vinculada ao alvo e parâmetros atuais.

Mudanças de produção, DNS, pagamentos live, deleção ou operações irreversíveis exigem gate explícito proporcional ao risco.

### 5. Apply

Executar em etapas pequenas. Parar em:
- prerequisito ausente;
- conflito com estado observado;
- permissão insuficiente;
- falha de verificação intermediária;
- destino diferente do aprovado.

Não continuar em cascata tentando “consertar no caminho” sem atualizar o plano.

### 6. Verify

Verificar o comportamento observável relevante:
- deployment acessível;
- health/route principal;
- conexão ao banco;
- migrations esperadas;
- auth quando aplicável;
- domínio/DNS resolvendo;
- email de teste quando autorizado;
- webhook;
- fluxo de pagamento em test mode quando for o escopo.

Checks parciais autorizam apenas claims parciais.

### 7. Handover

Registrar sem secrets:
- recursos criados ou conectados;
- contas/projetos;
- URLs e identificadores não secretos;
- env var names;
- owner;
- checks executados e data;
- itens manuais pendentes;
- recovery/rollback;
- caminho de remoção;
- limitações de observabilidade.

### 8. Drift check

Quando houver estado anterior, comparar:
- expected/recorded;
- observed now;
- verifiable/unverifiable;
- ação recomendada.

Drift check é read-only por padrão e não redefine baseline sozinho.

### 9. Teardown

Remover somente recursos cuja ownership do fluxo possa ser demonstrada. Antes de apagar:
- confirmar alvo atual;
- revalidar ownership;
- listar impacto;
- exigir approval apropriado.

Depois, reconsultar o estado e reportar resíduos que não puderam ser removidos/verificados.

## Recovery

- Retry não é automaticamente seguro para writes externos.
- Se a resposta do provider se perdeu, consultar o estado antes de repetir.
- Rollback deve ser específico ao recurso e comprovadamente suportado.
- Nunca prometer rollback universal de DNS, dados, pagamentos ou integrações.
- Se um recurso não puder ser lido, marcar `unverifiable`, não `clean`.

## Segurança

- usar least privilege;
- nunca expor secrets em chat, logs, argv ou documentos compartilháveis quando houver alternativa segura;
- tratar CLIs, installers, SDKs e plugins externos como dependências reais;
- não instalar ou executar software de terceiros apenas porque uma referência metodológica o utiliza;
- preferir sandbox/test mode antes de live quando isso atender ao objetivo.

## Ferramentas e dependências

Adaptar ao ambiente real. Vercel, Netlify, Supabase, Neon, Cloudflare, Stripe, Resend e outros são exemplos possíveis, não requisitos. Usar conectores/CLIs/APIs somente quando realmente disponíveis e autorizados.

Esta skill descreve o contrato operacional. Ela não torna providers automaticamente acessíveis.

## Integração

Combina com:
- `system-design-engineering`;
- `verify-before-claim`;
- `behavior-contract-validation`;
- `loop-engineering` para drift recorrente;
- `handoff`;
- skills específicas de provider quando existirem.

## Referências

Metodologia adaptada de [mikehasa/golive-skill](https://github.com/mikehasa/golive-skill), preservando detect → plan → approve → apply → verify → handoff/status/teardown e removendo dependência do runtime GoLive.
