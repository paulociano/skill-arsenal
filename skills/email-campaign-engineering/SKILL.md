---
name: email-campaign-engineering
description: "Planejar e construir campanhas de e-mail HTML com copy, assets, compatibilidade e verificação antes do envio autorizado."
---

# email-campaign-engineering

## Objetivo

Planejar, escrever, construir e verificar campanhas de e-mail HTML responsivas e compatíveis com clientes, com assets confiáveis, tracking/links claros, acessibilidade e gate explícito antes de qualquer envio.

## Quando usar

- campanha de lançamento;
- newsletter;
- sequência/drip;
- e-mail promocional ou lifecycle;
- transformar briefing em HTML e assets prontos para envio.

## Workflow

1. **Goal & audience** — objetivo, segmento, oferta, CTA e métrica.
2. **Source facts** — reunir somente claims e números sustentados.
3. **Audience state** — confirmar listas/segmentos, consentimento, suppression/blocklist e status de subscription.
4. **Message architecture** — subject/preheader → hook → proof/value → CTA → supporting detail → footer.
5. **Design system** — adaptar marca existente; evitar copiar tokens fixos da fonte como padrão universal.
6. **Email-safe build** — layout robusto, URLs absolutas, inline styles quando necessário, fallback para recursos não suportados.
7. **Assets** — imagens leves, alt text, dimensões adequadas, versionamento de arquivo quando cache importa.
8. **Media** — vídeo vira thumbnail/GIF/link; não depender de vídeo embutido.
9. **Accessibility/client pass** — contraste, leitura sem imagens, links, mobile, dark mode e clientes relevantes.
10. **Compliance pass** — remetente, unsubscribe/preferences, consentimento e requisitos legais aplicáveis ao contexto.
11. **Delivery setup** — verificar sender/from, domínio, SMTP/provider route, bounce handling e limites de throughput/concurrency quando aplicável.
12. **Pre-send verification** — links, assets, audience, subject/preheader, test send e rendering.
13. **Campaign state gate** — distinguir draft, scheduled, running, paused, cancelled e finished quando a plataforma tiver lifecycle equivalente.
14. **Approval gate** — iniciar, retomar, agendar ou enviar batch/drip só após autorização explícita do usuário.
15. **Post-send analysis** — usar métricas reais e não inventar attribution.

## Audience e subscription lifecycle

Quando a plataforma expuser estado por lista/assinante:

- separar subscriber habilitado/disabled/blocklisted de subscription em uma lista específica;
- distinguir unconfirmed, confirmed e unsubscribed quando houver opt-in;
- somente destinatários elegíveis segundo consentimento e status da lista entram no envio;
- unsubscribe ou suppression precisa vencer segmentação ou regra de campanha;
- importação de contatos não implica autorização para marketing;
- double opt-in ou confirmação equivalente deve ser preservado quando fizer parte da política escolhida.

## Delivery e bounce handling

Antes de um envio material:

- confirmar endereço/domínio de remetente e rota do provider;
- separar erro de conteúdo de erro de transporte;
- tratar hard bounce, soft bounce e complaint de forma distinta quando o provider/plataforma permitir;
- verificar suppression/blocklist antes de retry;
- não aumentar concurrency para resolver lentidão sem observar limites do provider e reputação;
- múltiplas rotas SMTP/provedores precisam de critério explícito de roteamento e fallback;
- test send não substitui validação de uma amostra real de destinatários/segmento.

## Lifecycle de campanha

Uma campanha pode ter estados operacionais diferentes. Quando a plataforma suportar:

- draft: ainda editável, nenhum envio;
- scheduled: envio futuro definido;
- running: execução ativa;
- paused: execução interrompida de forma reversível;
- cancelled: não deve ser retomada implicitamente;
- finished: execução encerrada.

Mudança de estado é efeito operacional, não simples edição de conteúdo. Agendar, iniciar, retomar e cancelar exigem o mesmo cuidado de ações outward-facing.

## Regras

- design tokens do repo original são exemplo, não identidade universal;
- nenhum número de performance entra sem fonte;
- URLs relativas não são suficientes em e-mail enviado;
- recursos CSS frágeis precisam de fallback;
- tamanho de GIF/imagem deve ser otimizado para o público/cliente real;
- “funcionou no browser” não prova “funcionou no inbox”;
- não importar listas nem enviar marketing sem base legítima/consentimento apropriado;
- ações outward-facing exigem aprovação;
- self-hosted não elimina responsabilidade por consentimento, deliverability, segurança ou reputação de domínio.

## Integrações

Se Resend, Gmail, listmonk ou outro serviço estiver realmente conectado, usar a integração e seus limites reais. Não presumir Resend, listmonk, ffmpeg, Vercel ou SMTP disponível.

## Integração com Arsenal

- writing-quality
- voice-builder
- content-matrix
- social-analytics
- verify-before-claim

## Referências

Adaptada de irinabuht12-oss/email-campaigns-claude.

Audience lifecycle, campaign states, bounces e operação self-hosted adaptados de https://github.com/knadh/listmonk, sem exigir o binário, Docker Compose, PostgreSQL ou configuração da fonte.

Origem local: [email-campaign-engineering.docx](../email-campaign-engineering.docx).
