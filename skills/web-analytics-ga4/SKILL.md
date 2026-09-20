---
name: web-analytics-ga4
description: "Analisar tráfego, aquisição e conversão em GA4 ou exports equivalentes com períodos comparáveis e limitações de tracking."
---

# web-analytics-ga4

## Objetivo

Analisar dados agregados de web analytics, especialmente GA4, separando aquisição, comportamento e conversão, comparando períodos de forma válida e transformando métricas reais em hipóteses e ações priorizadas.

## Quando usar

- performance do site;
- tráfego e canais;
- landing pages;
- conversão/key events;
- dispositivos;
- países;
- comportamento orgânico;
- comparação de períodos;
- anomalias.

## Workflow

1. Definir pergunta de negócio antes das métricas.
2. Confirmar propriedade, período, timezone e granularidade.
3. Separar:
   - acquisition;
   - engagement/behavior;
   - conversion/key events.
4. Comparar períodos equivalentes quando sazonalidade/dia da semana importar.
5. Segmentar por dimensão somente quando houver volume suficiente.
6. Identificar mudança material e depois formular hipótese causal.
7. Não tratar correlação de analytics como causalidade.
8. Priorizar uma ação principal e poucas investigações secundárias.
9. Registrar caveats de tracking, consent mode, sampling/thresholding ou dados incompletos quando aplicável.
10. Verificar métricas na fonte antes de claim final.

## GA4 + SEO

GA4 explica comportamento e conversão após aquisição. Query, impression, CTR e posição orgânica pertencem ao Search Console. Para SEO:

- combinar com `seo-research-audit`;
- não inventar dados de query usando GA4;
- cruzar landing-page behavior com Search Console quando ambos existirem.

## Comparações

Preferir:

- janela atual vs janela anterior equivalente;
- mesmo dia da semana para alertas diários;
- segmentos comparáveis.

Evitar interpretar “hoje” como período completo quando a coleta ainda está em andamento.

## Regras

- métricas ausentes = unknown;
- não inventar attribution;
- bounce/engagement precisam ser interpretados no contexto do site;
- média pode esconder segmento crítico;
- mudanças de tracking podem parecer mudança de negócio;
- recomendações precisam apontar a métrica/evidência que as motivou.

## Segurança e privacidade

- least privilege;
- dados agregados sempre que possível;
- não expor credenciais;
- não tentar reidentificar usuários;
- não exportar dados sensíveis sem necessidade.

## Ferramentas e dependências

Usar plugin/conector de analytics se existir. Se não houver acesso aos dados, trabalhar com export fornecido pelo usuário ou produzir plano de análise, sem inventar resultados. Não depender dos scripts Bun/TypeScript do repo original.

## Integração

- `seo-research-audit`
- `social-analytics`
- `experiment-design`
- `verify-before-claim`

## Referências

Adaptada de LichAmnesia/lich-skills · google-analytics.

Origem local: [web-analytics-ga4.docx](../web-analytics-ga4.docx).
