---
name: video-editing-pipeline
description: "Editar vídeos com transcrição, decisões de corte explícitas, EDL, render e revisão audiovisual preservando as fontes."
---

# video-editing-pipeline

## Objetivo

Editar vídeo de forma conversacional usando transcript como superfície primária, visuais sob demanda, um plano aprovado antes do corte, EDL explícita, render e verificação do resultado.

## Quando usar

Editar vídeos com transcrição, decisões de corte explícitas, EDL, render e revisão audiovisual preservando as fontes.

## Princípios

1. **Transcript first, visuals on demand.** Não despejar milhares de frames no contexto.
2. **Áudio orienta cortes; visual confirma decisões.**
3. **Ask → confirm → execute → verify → persist.**
4. Não assumir o tipo de vídeo antes de inspecionar material e objetivo.
5. Separar regras de produção de decisões de gosto.
6. Não apresentar render sem revisão do próprio output.

## Workflow

1. **Inventory** — listar fontes, durações, formato e objetivo.
2. **Transcribe** — obter timestamps em nível de palavra quando o corte depender de fala; cachear por arquivo/fingerprint.
3. **Pack** — criar uma visão compacta por frases/takes para raciocínio.
4. **Strategy** — propor estrutura, ritmo, tratamento visual, legendas, overlays e critérios de corte em linguagem simples.
5. **Approval gate** — não alterar o corte antes da aprovação quando a estratégia envolver julgamento criativo/material.
6. **EDL** — registrar decisões de segmentos e timeline de saída explicitamente.
7. **Render** — gerar preview preservando as fontes originais.
8. **Self-eval** — revisar fronteiras de corte, áudio, legendas, overlays, continuidade e erros visuais.
9. **Bounded correction** — corrigir e re-renderizar somente problemas observados, com limite de iterações.
10. **Final + persistence** — salvar output final e notas de sessão/decisões em área separada das fontes.

## Modo de produção generativa

Quando o pedido começa por tema/brief em vez de footage pronto, usar uma cadeia explícita e auditável:

1. pesquisa/brief;
2. roteiro;
3. termos de busca e plano de assets;
4. aquisição/geração de footage, imagens e áudio;
5. voiceover/TTS quando autorizado;
6. legendas alinhadas;
7. música/SFX;
8. composição;
9. render;
10. revisão audiovisual.

Cada estágio deve poder ser inspecionado e, quando útil, interrompido/reutilizado sem refazer toda a cadeia.

### Runtime e modo de composição

Escolher runtime pelo trabalho real e pela disponibilidade do ambiente:

- FFmpeg para montagem, trims, transcodes, overlays e composição determinística simples;
- runtime programático de cenas, como Remotion, quando UI/texto/animação React-like forem centrais;
- HTML/GSAP/WebGL ou equivalente quando a composição for uma experiência visual autoral e o runtime suportar render determinístico.

Separar:
- **templated**: cenas/blocks existentes cobrem o briefing com eficiência;
- **atelier/custom**: composição precisa ser autorada porque o catálogo impõe repetição ou limita a direção.

Nunca fingir que um runtime/provider está disponível. Verificar primeiro e usar fallback apenas quando o resultado continua atendendo ao contrato.

## Regras de produção

Quando o pipeline usar timestamps de fala + ffmpeg ou ferramenta equivalente:

- nunca cortar dentro de palavra quando a intenção é preservar fala natural;
- usar pequena folga nas bordas quando o ASR tiver drift;
- prevenir pops/clicks em cortes de áudio com fades/crossfades apropriados;
- recalcular legendas para a timeline final, não para timestamps absolutos da fonte;
- aplicar legendas por último quando overlays poderiam cobri-las;
- validar que overlays/animações entram no instante correto da timeline;
- não retranscrever fonte imutável sem necessidade.

Valores exatos como 30 ms de fade ou 30–200 ms de padding pertencem ao pipeline de referência e devem ser tratados como defaults de implementação, não leis universais.

## Eficiência

- Para talking-head/interview, carregar transcript antes de frames.
- Usar filmstrip/timeline visual apenas em pausas ambíguas, comparação de takes e sanity checks de corte.
- Para várias animações independentes, paralelizar somente quando o ambiente realmente suportar execução independente.
- Reutilizar transcrição, EDL e evidência entre iterações.

## Ferramentas e dependências

Usar leitura e escrita de arquivos e execução de código pelo terminal disponível. Localizar os runtimes e bibliotecas fornecidos pelo ambiente antes de usá-los; verificar separadamente SDKs, CLIs e dependências do projeto. Verificar ferramentas de mídia e transcrição antes de usá-las; FFmpeg, ASR, TTS e geração de vídeo não estão garantidos. Sem render, entregar estratégia/EDL e declarar que edição materializada e revisão audiovisual não ocorreram.

## Recortes verticais orientados pela cena

Quando transformar footage longo em shorts:
- selecionar trechos com ideia completa e contexto suficiente; quantidade e duração são metas editoriais, não garantias de alcance;
- inspecionar a cena antes de escolher layout: pessoa única pode usar crop com acompanhamento; duas pessoas simultâneas podem usar split; plano/contraplano não deve duplicar o mesmo rosto; demonstração de tela precisa preservar informação fora do centro;
- registrar timestamps na fonte e sua correspondência na timeline final, especialmente ao recortar um clip já produzido;
- verificar legendas preexistentes antes de queimar novas e posicionar texto sem cobrir rostos ou conteúdo essencial;
- reverificar mudanças de plano, perda do sujeito e resolução de entrada no preview;
- separar geração, armazenamento privado, galeria pública e publicação social. Produzir um vídeo não autoriza upload público ou postagem;
- em integração real, tratar 401 como falha de autenticação até verificar configuração, nunca como prova de modo anônimo; preservar job ID e respeitar quotas sem reenviar tarefa incerta.

Método sintetizado de [OpenShorts](https://github.com/mutonby/openshorts/blob/4b2cf58922587ecb17b990a9575e46320bdb3118/skills/openshorts/SKILL.md), sem exigir seu serviço, MCP, providers ou presets.

## Referências

Adaptada de browser-use/video-use.

Pipeline tema→roteiro→assets→voz→legendas→música→composição adaptado de https://github.com/harry0703/MoneyPrinterTurbo. Seleção explícita de runtime e modos templated/atelier adaptados de https://github.com/calesthio/OpenMontage, sem exigir seus providers, Remotion, HyperFrames ou ferramentas vendorizadas.

Origem local: [video-editing-pipeline.docx](../video-editing-pipeline.docx).
