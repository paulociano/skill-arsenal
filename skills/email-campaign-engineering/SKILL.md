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
3. **Message architecture** — subject/preheader → hook → proof/value → CTA → supporting detail → footer.
4. **Design system** — adaptar marca existente; evitar copiar tokens fixos da fonte como padrão universal.
5. **Email-safe build** — layout robusto, URLs absolutas, inline styles quando necessário, fallback para recursos não suportados.
6. **Assets** — imagens leves, alt text, dimensões adequadas, versionamento de arquivo quando cache importa.
7. **Media** — vídeo vira thumbnail/GIF/link; não depender de vídeo embutido.
8. **Accessibility/client pass** — contraste, leitura sem imagens, links, mobile, dark mode e clientes relevantes.
9. **Compliance pass** — remetente, unsubscribe/preferences, consentimento e requisitos legais aplicáveis ao contexto.
10. **Pre-send verification** — links, assets, audience, subject/preheader, test send e rendering.
11. **Approval gate** — envio/batch/drip só após autorização explícita do usuário.
12. **Post-send analysis** — usar métricas reais e não inventar attribution.

## Regras

- design tokens do repo original são exemplo, não identidade universal;
- nenhum número de performance entra sem fonte;
- URLs relativas não são suficientes em e-mail enviado;
- recursos CSS frágeis precisam de fallback;
- tamanho de GIF/imagem deve ser otimizado para o público/cliente real;
- “funcionou no browser” não prova “funcionou no inbox”;
- não importar listas nem enviar marketing sem base legítima/consentimento apropriado;
- ações outward-facing exigem aprovação.

## Integrações

Se Resend, Gmail ou outro serviço estiver conectado, usar a integração real e seus limites. Não presumir Resend/ffmpeg/Vercel.

## Integração com Arsenal

- `writing-quality`
- `voice-builder`
- `content-matrix`
- `social-analytics`
- `verify-before-claim`

## Referências

Adaptada de irinabuht12-oss/email-campaigns-claude.

Origem local: [email-campaign-engineering.docx](../email-campaign-engineering.docx).
