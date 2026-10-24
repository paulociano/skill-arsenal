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

### Shot ledger para produção generativa

Para vídeo gerado por cenas, não trate o projeto como um prompt monolítico. Mantenha um ledger por shot com, quando relevante:
- função narrativa;
- duração/alvo de ritmo;
- enquadramento/câmera;
- personagens/objetos/local;
- frame inicial/final ou referência;
- prompt/direção de movimento;
- backend/modelo realmente usado;
- status `planned → generated → review → approved/rework`;
- motivo de re-geração.

A continuidade deve ser revisada entre shots, não apenas dentro de cada clip. Refilmar/regenerar somente o shot que falhou quando o restante permanece válido. Storyboard/previs é evidência intermediária e pode ser aprovado antes do custo maior de geração final.

### Runtime e modo de composição

Escolher runtime pelo trabalho real e pela disponibilidade do ambiente:

- FFmpeg para montagem, trims, transcodes, overlays e composição determinística simples;
- runtime programático de cenas, como Remotion, quando UI/texto/animação React-like forem centrais;
- HTML/GSAP/WebGL ou equivalente quando a composição for uma experiência visual autoral e o runtime suportar render determinístico.

Separar:
- **templated**: cenas/blocks existentes cobrem o briefing com eficiência;
- **atelier/custom**: composição precisa ser autorada porque o catálogo impõe repetição ou limita a direção.

Nunca fingir que um runtime/provider está disponível. Verificar primeiro e usar fallback apenas quando o resultado continua atendendo ao contrato.

## Remotion: composição React determinística

Aplicar quando texto animado, tipografia, gráficos, templates, dados dinâmicos ou reutilização de layouts forem parte central do vídeo. Não escolher Remotion só porque há um vídeo: cortes lineares e transcodes simples costumam ser mais eficientes no FFmpeg.

### Gate de ambiente e licença

1. Verificar se Node.js, dependências React/Remotion, browser/render backend, codecs e espaço de armazenamento estão disponíveis no ambiente de execução real.
2. Consultar a licença corrente em https://github.com/remotion-dev/remotion/blob/main/LICENSE.md antes de produção comercial. A licença gratuita publicada em outubro de 2026 cobre indivíduos, organizações sem fins lucrativos e empresas com até três funcionários; outras empresas comerciais podem precisar de licença.
3. Não executar `npx create-video@latest` ou instaladores do repositório apenas para inspecioná-lo. Em projetos aprovados, preferir dependências versionadas e lockfile.
4. Separar geração de código, preview, render e verificação. Código JSX ou preview no navegador não são prova de arquivo de vídeo finalizado.

### Workflow especializado

1. Definir contrato: duração, fps, resolução, proporção, codec, canais de áudio, safe areas, conteúdo e formatos de saída.
2. Especificar timeline em frames, entradas de dados, assets, fontes e suas licenças.
3. Criar cenas e componentes React isolando dados editoriais de animação; manter animações derivadas do frame/tempo da composição, evitando relógios não determinísticos.
4. Verificar assets, dimensionamento, carregamento de fontes, sincronismo de áudio, legendas e tratamento de durações variáveis.
5. Gerar render de amostra e inspecionar começo, transições, pontos de texto denso e fim; revisar quadro e áudio quando as ferramentas estiverem disponíveis.
6. Renderizar o formato final e verificar existência, duração, resolução, fps, codec, integridade audiovisual e ausência de frames pretos ou texto cortado.
7. Para escala/batch, testar poucos exemplos representativos antes de paralelizar ou provisionar execução remota. Registrar custos, limites e falhas.
8. Se o runtime estiver indisponível, entregar projeto/código e plano reproduzível, sinalizando explicitamente que preview e render não foram executados.

### Fronteiras

- Remotion compõe/renderiza; não equivale a um gerador de vídeo por IA, ASR ou editor humano.
- Não presumir disponibilidade de render em Lambda, Vercel ou browser só por existir documentação dessas opções.
- Não expor chaves ou dados sensíveis em assets públicos, bundles ou outputs.
- Não substituir `video-editing-pipeline` ou `explainer-video-production`: este é apenas um backend de composição que elas podem selecionar.

**Fonte:** https://github.com/remotion-dev/remotion · https://www.remotion.dev/docs · https://github.com/remotion-dev/remotion/blob/main/LICENSE.md (consulta 2026-10-15).

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

Shot ledger, storyboard→filming→continuity review→rework queue e roteamento de modelo por shot refinados a partir de `LudwigKienle/ai-video-production-editor`, `headline-design/seq` e `openslop/openslop`, sem importar seus providers, plugins ou runtimes.

Origem local: [video-editing-pipeline.docx](../video-editing-pipeline.docx).
## Editor conversacional local: lições de editonny

O projeto [editonny](https://github.com/soumatheusgomes/editonny) descreve um editor guiado por instruções em linguagem natural para cortar pausas e erros, gerar legendas, corrigir áudio, reframar e inserir cenas de motion. Seu workflow depende de engine/renderer, transcrição, ferramentas locais e integração com Claude Code/Codex: **não declarar esse runtime disponível por padrão**.

Quando o usuário pedir edição conversacional de footage, reaproveitar a metodologia sem instalar o software:
1. Converter o pedido informal em operações auditáveis sobre segmentos, fala, legendas, áudio e composição.
2. Manter instrução editorial separada de EDL/timestamps e registrar source-to-output mapping.
3. Para motion baseado na fala, especificar cenas e cue points ligados ao transcript, sem alterar conteúdo factual do áudio.
4. Usar preview representativo e inspeção audiovisual antes de batch render, principalmente em cortes automáticos, captions e reformatação vertical.
5. Preservar material original; explicitar se apenas o plano foi produzido ou se mídia final foi de fato renderizada/validada.

Adoção metodológica, não instalação de skill/scripts de terceiros. Fonte revisada em 2026-10-22.

## Render local com preflight, revisão e entregáveis isolados (Showtime, 2026-10-24)

Para pipelines automatizados de vídeo por agentes, antes de qualquer render: confirmar runtime, bibliotecas, fontes, espaço livre, downloads/modelos, GPU/CPU, direitos de assets e se dados saem da máquina; custo zero em API não implica custo zero em armazenamento/compute. Separar modo rápido (assumptions declaradas) de modo studio (storyboard, look e aprovação) e revisão lean de quality, sem pular QA de material publicado. Usar pasta única por job com manifest, fontes, timeline, prévia, poster, render final, exports e evidências de QA, sem sobrescrever entregas. Fazer primeiro render parcial de baixo custo; verificar textos na safe area, clipping, sobreposição, áudio sincronizado e legibilidade em 9:16 e 16:9, inclusive quadros intermediários. Validar arquivo final reproduzindo amostras e comparar export com manifest; critic/reviewer não substitui inspeção objetiva.

Referência: https://github.com/FavioVazquez/showtime . A ferramenta requer dependências e downloads locais, e seu CLI/Agent Skills não estão presumidos disponíveis no ChatGPT.
