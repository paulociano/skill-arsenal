---
name: meeting-knowledge-capture
description: "Converter gravações, transcrições ou notas de reuniões em decisões e ações rastreáveis no destino autorizado."
---

# meeting-knowledge-capture

## Objetivo

Transformar gravação ou transcrição de uma reunião em memória operacional: transcript rastreável, resumo, decisões, ações, pessoas/entidades relevantes e links para a fonte, salvando no destino autorizado pelo usuário.

## Quando usar

- reunião gravada;
- call de trabalho;
- entrevista interna;
- aula/podcast que precisa virar notas;
- transcrição já fornecida;
- captura para Drive/Docs/knowledge base.

## Workflow

1. **Source** — recording, transcript ou notes.
2. **Transcription/diarization** — somente quando ferramenta real estiver disponível.
3. **Preserve raw** — manter transcript/fonte separado do resumo.
4. **Normalize speakers/time** — timestamps e speaker labels quando existentes.
5. **Summarize**:
   - topics;
   - decisions;
   - action items;
   - owners/deadlines quando explicitamente ditos;
   - open questions;
   - notable quotes somente quando úteis.
6. **Entity links** — pessoas/projetos/documentos somente com identidade suportada pela fonte.
7. **Write destination** — arquivo local ou destino conectado escolhido e autorizado.
8. **Cross-link** — nota ↔ transcript ↔ source.
9. **Verify write-back** antes de afirmar conclusão.

## Regras

- não inventar owner ou deadline;
- não transformar intenção vaga em decisão;
- decisão precisa estar distinguida de sugestão;
- transcript é fonte, resumo é interpretação;
- pesquisas sobre pessoas citadas não entram automaticamente;
- notas pessoais/terceiros exigem necessidade e autorização apropriadas;
- não poluir um vault/base existente com estruturas novas sem pedido.

## Profundidade

- **Minimal**: resumo, decisões, ações e open questions.
- **Detailed**: tópicos por seção, contexto, quotes, entity links e follow-ups.
Se o usuário já especificou profundidade/formato, não perguntar de novo.

## Transcrição

Preferir capacidade nativa/conector. External transcription provider só com autorização e aviso de privacidade/custo quando material.

## Integração

- `watch-video`
- `call-evaluation` quando a reunião for uma call comercial a avaliar;
- `session-learn` para transformar decisões em memória durável;
- `golden-circle-feedback` quando o objetivo for feedback;
- `verify-before-claim`.

## Referências

Adaptada de reysu/ai-life-skills · summarize-call / summarize.

Origem local: [meeting-knowledge-capture.docx](../meeting-knowledge-capture.docx).
