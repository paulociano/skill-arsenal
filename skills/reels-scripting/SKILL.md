---
name: reels-scripting
description: "Analisar a estrutura narrativa de um Reel e criar roteiro original no mesmo padrão, sem copiar conteúdo ou presumir desempenho."
---

# reels-scripting

## Objetivo

Reverse-engineer a estrutura de um Reel de referência e criar um novo roteiro usando o padrão narrativo sem copiar conteúdo ou inventar contexto do autor.

## Quando usar

Analisar a estrutura narrativa de um Reel e criar roteiro original no mesmo padrão, sem copiar conteúdo ou presumir desempenho.

## Workflow

1. Receber Reel/vídeo de referência ou transcript/análise equivalente.
2. Usar `watch-video` quando houver acesso real ao vídeo.
3. Extrair transcript, hook, ritmo, estrutura, transições, before/after e CTA.
4. Separar forma reutilizável de conteúdo específico do criador original.
5. Aplicar a estrutura a um tema do usuário usando `voice-builder`/perfil quando disponível.
6. Não chamar um Reel de outlier sem dados comparativos reais do mesmo criador.

## Ferramentas e dependências

Usar vídeo acessível, frames ou transcrição e a skill watch-video conforme a necessidade. Não exigir Apify ou Gemini. Se houver apenas transcrição, limitar a análise a texto e fala documentada.

## Referências

[GitHub · charlie947/social-media-skills · reels-scripting](https://github.com/charlie947/social-media-skills/tree/main/skills/reels-scripting)

Origem local: [reels-scripting.docx](../reels-scripting.docx).
