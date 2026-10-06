---
name: pwa-engineering
description: "Projetar, revisar e validar Progressive Web Apps por installability, manifest, service worker, caching, offline/update lifecycle, storage, resiliência, performance e experiência de instalação sem confundir PWA com um score ou framework."
---

# PWA Engineering

## Objetivo

Projetar ou auditar uma PWA como um sistema de entrega resiliente no navegador: identidade instalável, service worker, políticas de cache, comportamento offline, atualizações seguras e experiência coerente sob rede ruim, sem tornar Workbox, PWABuilder ou qualquer framework obrigatórios.

## Quando usar

- transformar web app em PWA;
- revisar manifest/installability;
- projetar service worker e cache;
- corrigir conteúdo stale ou update quebrado;
- suportar offline/poor network;
- revisar storage, push ou background sync;
- preparar uma PWA para packaging/distribuição;
- auditar regressões específicas de PWA.

Não usar apenas para performance web genérica: use `web-quality-audit`. Não usar apenas para redesign: use `web-design-engineer`.

## Princípio central

**Offline e cache são modelos de consistência. Declare source of truth, freshness e fallback antes de escrever o service worker.**

## Workflow

1. **Product contract**
   - definir por que instalação/offline agrega valor;
   - listar jornadas que devem funcionar online, degradadas ou offline;
   - separar requisito real de “ter PWA” como badge.

2. **App identity & manifest**
   - name/short name;
   - start URL e scope;
   - display/orientation quando relevantes;
   - icons/maskable assets;
   - theme/background;
   - validar URLs, MIME e assets no ambiente real;
   - não assumir critérios de instalação idênticos em todos os browsers/plataformas.

3. **Service worker boundary**
   - definir o que o worker controla;
   - separar app shell, conteúdo estático, navigation, API e media;
   - registrar install/activate/update lifecycle;
   - evitar interceptar requests sem política explícita.

4. **Caching by resource class**
   - escolher estratégia por dado, não por preferência:
     - cache-first para assets imutáveis/versionados;
     - network-first quando freshness domina;
     - stale-while-revalidate quando conteúdo antigo ainda é aceitável;
     - network-only para operações que não devem ser cacheadas;
   - declarar TTL/invalidation quando existir;
   - evitar cache indiscriminado de respostas autenticadas ou personalizadas.

5. **Offline contract**
   - definir quais rotas abrem;
   - fallback de navigation;
   - estados “sem conexão” úteis;
   - distinguir dado cached, stale e indisponível;
   - não simular sucesso para ação que ainda não foi persistida/sincronizada.

6. **Update lifecycle**
   - testar cliente antigo + service worker antigo recebendo nova versão;
   - evitar incompatibilidade entre shell e API/schema;
   - definir quando ativar atualização e quando pedir reload;
   - versionar/migrar caches quando necessário;
   - garantir rollback coerente com assets ainda referenciados.

7. **Storage & sensitive data**
   - mapear Cache Storage, IndexedDB/local storage e memória;
   - assumir que browser pode aplicar quota/eviction;
   - limpar dados apropriados no logout;
   - não persistir secrets/sensitive payloads sem necessidade explícita;
   - tratar device compartilhado como boundary quando relevante.

8. **Background capabilities**
   - push, background sync e periodic work somente quando suportados e justificados;
   - pedir permissão em contexto, não na primeira visita;
   - definir idempotência e retry para ações reenviadas;
   - fornecer fallback quando a API não existir.

9. **Performance & accessibility**
   - medir cold/warm load;
   - não trocar freshness por score;
   - lazy-load e precache dentro de budget;
   - manter navegação, focus, reduced motion e estados de erro acessíveis;
   - combinar com `web-quality-audit` para métricas reproduzíveis.

10. **Runtime verification**
    - primeira visita;
    - instalação quando disponível;
    - reload;
    - offline startup;
    - navegação offline;
    - rede lenta/intermitente;
    - atualização de versão;
    - logout;
    - cache vazio/corrompido ou storage eviction quando simulável;
    - múltiplas abas quando o lifecycle puder conflitar.

11. **Distribution**
    - packaging/store apenas quando necessário;
    - tratar pacote como derivado da aplicação web e da configuração publicada;
    - validar a versão realmente empacotada/promovida;
    - não depender de PWABuilder para a PWA existir.

## Failure modes que merecem atenção

- service worker “zumbi” servindo bundle incompatível;
- HTML novo + JS antigo ou vice-versa;
- cache key sem versionamento;
- API privada armazenada em cache compartilhável;
- logout que deixa dados offline legíveis;
- offline fallback mascarando erro real;
- fila de sync duplicando ação não idempotente;
- prompt de instalação/permissão prematuro;
- experiência que funciona em Chromium mas quebra em outro alvo suportado.

## Ferramentas

Quando disponíveis e apropriadas:
- Lighthouse para sinais de qualidade/performance;
- Workbox para estratégias e lifecycle;
- PWABuilder para diagnóstico/packaging;
- browser automation para cenários de runtime.

Nenhuma dessas ferramentas é requisito. Grounding de versão é obrigatório quando comportamento depender de API/browser/tool atual.

## Integração

Combina com:
- `web-quality-audit`;
- `runtime-ui-verification`;
- `software-testing-engineering`;
- `web-application-security-audit`;
- `production-go-live`;
- `web-design-engineer`.

## Provenance

Adaptada de:
- https://github.com/GoogleChrome/workbox
- https://github.com/pwa-builder/PWABuilder
- práticas já consolidadas em `web-quality-audit` a partir do Lighthouse.

Preserva caching, service-worker lifecycle, offline resilience e packaging sem exigir Workbox, PWABuilder, Node, Docker ou tooling específico.
