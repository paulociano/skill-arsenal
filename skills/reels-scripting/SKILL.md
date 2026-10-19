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
6. Quando a entrada for long-form, identificar **clip candidates** por unidade semântica completa, hook potencial, payoff, prova/exemplo e independência de contexto. Não usar duração isolada como critério.
7. Para cada candidato selecionado, gerar um mini edit brief: início/fim lógico, first-frame text, trechos que podem ser removidos, B-roll opportunities e CTA compatibility.
8. Não chamar um Reel de outlier ou “viral” sem dados comparativos reais do mesmo criador.

## Ferramentas e dependências

Usar vídeo acessível, frames ou transcrição e a skill watch-video conforme a necessidade. Não exigir Apify ou Gemini. Se houver apenas transcrição, limitar a análise a texto e fala documentada. Para execução audiovisual, rotear para `short-form-video-engineering` e `vertical-video-reframing` quando necessário.

## Referências

[GitHub · charlie947/social-media-skills · reels-scripting](https://github.com/charlie947/social-media-skills/tree/main/skills/reels-scripting)

Origem local: [reels-scripting.docx](../reels-scripting.docx).

## Primeiro quadro e hipótese visual (lote 30 repositórios, 2026-10-19)

Antes de fechar o roteiro, propor um primeiro quadro com ação visual concreta, assunto imediatamente identificável e texto curto legível sem som; evitar intro de logo ou cartela parada quando a narrativa depende de retenção inicial. Descrever o que aparece em 0–3 s, como o movimento se conecta à promessa, a sequência de beats e o payoff. Se a peça usa personagens recorrentes, fazer a ação deles avançar a explicação em vez de decoração repetida. Entregar variante de primeiro quadro estático quando o objetivo ou acessibilidade pedir. Tratar evidências observacionais de outros criadores como hipóteses, não garantia de viralização; nunca copiar imagens, marcas ou roteiros protegidos.

Fonte metodológica: https://github.com/Ootto-AI/claude-content-skills/tree/main/skills/virality . Resultados numéricos divulgados pelo autor não foram auditados independentemente.
