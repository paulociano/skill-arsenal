---
name: watch-video
description: "Analisar vídeos com transcrição e frames disponíveis, ancorando conclusões em timestamps e distinguindo visto, dito e inferido."
---

# watch-video

## Objetivo

Analisar vídeos combinando **evidência visual** (frames) e **evidência sonora/textual** (legendas ou transcrição), com foco em respostas ancoradas em timestamps.

## Quando usar

Analisar vídeos com transcrição e frames disponíveis, ancorando conclusões em timestamps e distinguindo visto, dito e inferido.

## Workflow

1. Confirmar acesso à fonte e quais evidências existem.
2. Ler legendas/transcrição e selecionar intervalos relevantes.
3. Inspecionar frames apenas quando necessários à pergunta.
4. Cruzar texto e visual por timestamp.
5. Entregar conclusões separando visto, dito e inferência.

## Metodologia

- Priorizar legendas/transcrição antes de processar vídeo completo.
- Extrair frames apenas quando a pergunta exige evidência visual.
- Ajustar densidade de frames ao tamanho do vídeo e ao trecho relevante.
- Preferir análise focada em `start/end` quando o usuário aponta um momento específico.
- Deduplicar frames quase idênticos para reduzir custo/contexto.
- Combinar frames + transcript com timestamps.
- Em follow-ups, reutilizar evidência já obtida em vez de reprocessar.

## Ferramentas e dependências

### Roteamento por capacidade

1. **Se o vídeo/arquivo estiver disponível diretamente ao ambiente e a superfície suportar análise multimodal suficiente:** usar a capacidade nativa e responder com timestamps quando possível.
2. **Se houver arquivo de vídeo acessível em ambiente com execução de código/arquivos:** extrair amostras/frames com ferramentas disponíveis. Usar `ffmpeg` somente se realmente disponível; não prometer instalação automática.
3. **Se a fonte for URL pública:** primeiro usar recursos web/YouTube/fontes disponíveis para obter transcript, capítulos ou mídia suportada. Se a pergunta depender de elementos visuais não acessíveis, informar a limitação e pedir upload do vídeo/trecho ou usar o navegador disponível quando sua API suportar o acesso necessário.
4. **Se houver legendas/transcrição mas não frames:** responder somente ao que o áudio/texto suporta e distinguir explicitamente o que não foi visualmente verificado.
5. **Se houver frames mas não transcript:** analisar o visual e dizer que o áudio/fala não foi verificado.
6. **Nunca solicitar ou armazenar API keys dentro da skill.** Se uma transcrição externa depender de um serviço conectado, usar o mecanismo seguro daquele conector/plugin e somente quando necessário.

## Modos conceituais

- `transcript` — texto/legendas apenas; menor custo.
- `efficient` — poucos frames-chave + transcript.
- `balanced` — seleção visual mais densa + transcript; padrão quando vídeo completo realmente precisa ser visto.
- `focused` — analisar somente o intervalo relevante; preferido para perguntas sobre momentos específicos.

## Regras de eficiência

- Para vídeos longos, começar por transcript/capítulos e só então escolher trechos visuais relevantes.
- Não processar dezenas de minutos em alta densidade se a pergunta é localizada.
- Dar preferência a frames distintos, não sequências redundantes.
- Aumentar resolução apenas quando for necessário ler texto pequeno na tela.

## Resposta

Quando possível, estruturar a conclusão com referências temporais, por exemplo `02:15–02:32`, distinguindo:

- **Visto no vídeo**
- **Dito/transcrito**
- **Inferência**

## Dependências e limites

Esta skill só executa análise audiovisual completa quando o ambiente fornece acesso real ao vídeo e ferramentas adequadas para imagem/áudio. Se isso não estiver disponível, deve degradar graciosamente para transcript, web, frames fornecidos pelo usuário ou solicitar o arquivo/trecho necessário. Nunca afirmar que 'assistiu' ao vídeo quando só leu transcript ou metadata.

## Roteamento para YouTube

Se a tarefa principal for obter a transcrição de um vídeo do YouTube, preferir `youtube-transcript`. Depois, usar `watch-video` somente quando a pergunta depender também de evidência visual, frames ou sincronização entre fala e imagem.

## Roteamento para edição

Se o objetivo for **editar** o vídeo, não apenas analisá-lo, preferir `video-editing-pipeline`. `watch-video` fornece evidência audiovisual; `video-editing-pipeline` adiciona strategy approval, EDL, render e self-eval.

## Referências

[GitHub · bradautomates/claude-video](https://github.com/bradautomates/claude-video)

Origem local: [watch-video.docx](../watch-video.docx).
