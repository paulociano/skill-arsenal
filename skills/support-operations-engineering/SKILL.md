---
name: support-operations-engineering
description: "Projetar operações de suporte/helpdesk com inbox compartilhada, threading confiável, SLAs, filas duráveis, automações, KB, permissões, retenção, exports e assistência de IA governada."
---

# Support Operations Engineering

## Objetivo

Estruturar atendimento ao cliente como um sistema operacional auditável, com fila, ownership, prioridades, metas de resposta, automações e conhecimento reutilizável.

## Quando usar

- helpdesk;
- customer support;
- shared inbox;
- ticket operations;
- SLA/SLO de atendimento;
- support automation;
- knowledge base;
- AI-assisted support;
- customer data export/erasure.

## Princípio central

**Suporte é uma fila operacional com estado, regras e responsabilidade explícita, não apenas uma caixa de e-mail.**

## Workflow

1. **Inbox contract**
   - organizações/workspaces;
   - inboxes;
   - customers;
   - tickets;
   - assignment;
   - status;
   - priority;
   - tags.

2. **Thread integrity**
   - Message-ID/In-Reply-To/References;
   - signed reply token quando necessário;
   - evitar depender apenas de subject matching;
   - spoofed subjects não podem unir tickets diferentes.

3. **Queue semantics**
   - new/open/pending/resolved;
   - snooze com motivo e wake-up;
   - customer reply pode reabrir/antecipar;
   - dead-letter queue para jobs de mail falhos;
   - retries idempotentes.

4. **SLA/targets**
   - first reply;
   - resolution;
   - priority-specific targets;
   - working hours/holidays/timezone;
   - due-soon vs overdue;
   - nada é overdue antes de existir policy explícita.

5. **Automation**
   - conditions + actions;
   - assignment/status/tag;
   - notifications/webhooks;
   - automação não deve enviar conteúdo sensível desnecessário;
   - payload mínimo quando IDs/status bastam.

6. **Knowledge base**
   - draft vs published;
   - search;
   - help center;
   - version/provenance;
   - AI draft pode usar KB como source, mas não inventar política.

7. **AI assistance**
   - opt-in por workspace;
   - summarize/classify/translate/draft;
   - read-only integration por default quando write approval não existe;
   - nenhuma resposta ao cliente é enviada sem boundary explícito;
   - provider/data policy precisa ser conhecida.

8. **Permissions**
   - Owner/Admin/Agent;
   - scoped API keys;
   - inherited privilege ceiling;
   - demotion/revocation deve reduzir capacidade da key;
   - key shown once, never retrievable.

9. **Attachments/data**
   - validated authorized upload;
   - tenant isolation;
   - retention;
   - export;
   - erasure workflow que também alcança queued messages/attachments;
   - backups/extracts devem omitir secrets/hashes quando apropriado.

10. **Reporting**
    - volume;
    - response time;
    - resolution time;
    - backlog;
    - SLA misses;
    - CSAT com denominador;
    - export window explicit.

11. **Recovery**
    - scheduled retry for stalled jobs;
    - orphan cleanup;
    - readiness check;
    - mail DNS/config verification;
    - durable evidence for failures.

## Regras

- subject line alone is not a trustworthy threading key;
- retry without idempotency can duplicate outbound messages;
- AI draft is not authorization to send;
- read-only MCP/API is preferable until approval UX exists;
- support metrics need denominator and time window;
- customer export/erasure is a workflow, not one database delete;
- snoozed tickets should not secretly count as active overdue work unless policy says so.

## Integração

`agent-action-governance`, `durable-workflow-engineering`, `software-observability-engineering`, `kb-retriever`, `agent-memory-engineering`, `production-go-live`.

## Provenance

Adaptada de mirza-rizvi/ResolveHQ. Preserva shared inbox, reliable mail threading, durable queues, SLA-aware work calendars, scoped API keys, read-only MCP, AI opt-in, export/erasure e recovery jobs sem presumir Cloudflare, Resend ou qualquer provider específico.
