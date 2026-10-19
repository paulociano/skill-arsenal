---
name: react-next-performance
description: Auditar e otimizar performance de React e Next.js por métricas, waterfall, bundle, cache, server/client boundaries e re-renders, respeitando versões e testes de regressão.
---

# React / Next.js Performance

## Quando usar
Escrita, revisão ou otimização de React/Next.js com riscos reais de latência, bundle, waterfall, serialização, hidratação, render e consumo de recursos. Não ativar para UI estática de outro framework.

## Workflow
1. Identificar React/Next.js e versões reais; perfilar ou obter evidência antes de otimizar código estável.
2. Priorizar causalmente: (a) waterfalls de requests/await sequencial que poderiam ocorrer em paralelo; (b) bundle pesado e imports/third-party; (c) CPU/IO no servidor, serialização e limites server-client; (d) fetch/cache em cliente; (e) re-render e cálculo; (f) layout/render e micro-otimização.
3. Para cada hipótese, preservar baseline, rota/arquivo envolvido e métrica correspondente. Checar contexto de autenticação, tenancy e cache antes de introduzir memoização persistente ou cache cross-request.
4. Reduzir waterfalls com paralelismo somente entre operações independentes; iniciar chamadas cedo e aguardar tarde, controlar falhas e cancelamento.
5. Reavaliar importação de barrel, dynamic import, lib carregada condicionalmente, JS de terceiros e dados desnecessários na fronteira de Server Components.
6. Para renders, derivar estado em render em vez de effects redundantes quando correto, evitar component definitions internas, usar memo/deferred/transition só se medições e UX justificarem.
7. Para SSR/hidratação, validar equivalência inicial server/client, acessibilidade, diferenças de locale, temas e flicker. Não suprimir warnings de hydration para ocultar bugs reais.
8. Escolher 1–3 correções com maior impacto, executar testes e comparar condições equivalentes; regressão sem runtime verificado deve permanecer UNKNOWN.
9. Verificar versão em docs oficiais para APIs como React Compiler, Activity, after(), cache(), useDeferredValue e flags do Next.js. Nenhuma guideline substitui as semânticas e limites da versão instalada.

## Regras
- Claims de ganhos exigem medição no projeto, não apenas regra de catálogo.
- Não trocar cache sem revisar correctness, permissões e invalidação.
- Não converter pequenos microbenchmarks em prioridade acima de I/O, JS transferido e UX.
- Não presumir CLI, build, métricas ou observabilidade disponíveis.
- Consultar apenas a categoria pertinente no guia original, sem despejar 70 regras no prompt.

## Integração
Usar com `web-quality-audit` para UX/CWV, `software-engineering-cycle` para mudanças substanciais e `verify-before-claim` para resultado comprovado.

## Fonte
Metodologia adaptada de https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices (consultada em 2026-10-19). Instruções da Vercel não constituem benchmarks da aplicação.
