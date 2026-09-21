---
name: procedural-film
description: "Criar curtas verticais animados proceduralmente com Canvas/Web Audio, storyboard em beat grid, render determinístico e revisão quadro a quadro."
---

# procedural-film

## Objetivo

Transformar um tema em um curta animado procedural, normalmente vertical e curto, no qual visual, timing e áudio são gerados por código e validados por uma pipeline reproduzível antes da entrega.

## Quando usar

- o usuário pedir um filme/animação curta feita proceduralmente;
- a entrega for HTML/canvas, vídeo renderizado ou ambos;
- o visual puder ser construído por código em vez de depender de assets externos;
- ritmo, cortes e áudio precisarem obedecer a uma timeline determinística.

Não usar para edição de footage existente; nesse caso, preferir `video-editing-pipeline`. Para apresentação HTML por cenas sem render audiovisual procedural, preferir `web-video-presentation`.

## Princípios

1. **Timeline é a fonte de verdade.** Shot, duração, transição e cue de áudio devem derivar do mesmo contrato.
2. **Planejar antes de desenhar.** Art bible + storyboard são mais baratos de corrigir que dezenas de cenas.
3. **Beat grid reduz drift.** BPM, beats e frames devem fechar matematicamente quando o filme depender de sincronização musical.
4. **Tracer bullet antes do detalhe.** Provar timeline, render e áudio com stubs antes de investir nas cenas reais.
5. **Determinismo é testável.** Mesma timeline + seed/config devem produzir frames equivalentes quando o runtime permitir.
6. **Revisão é visual e temporal.** Código correto não prova composição, legibilidade, cortes ou sincronização.

## Workflow

1. **Brief**
   - definir tema, duração, formato e elementos obrigatórios;
   - registrar explicitamente escolhas inventadas pelo sistema quando o usuário não as definiu.

2. **Ground runtime**
   - detectar Node/browser/Canvas/Web Audio/FFmpeg ou ferramentas equivalentes realmente disponíveis;
   - não instalar Playwright, Chromium, FFmpeg ou dependências silenciosamente;
   - se render de vídeo não estiver disponível, entregar player/frames/timeline e declarar a limitação.

3. **Research**
   - decompor o tema em fases/elementos visuais;
   - buscar somente fatos necessários para desenhar corretamente;
   - guardar fonte e locator para cada elemento factual importante.

4. **Art bible**
   - definir linguagem visual, paleta nomeada, tipografia quando houver, regras de desenho, safe areas e erros a evitar;
   - separar estilo fixo do filme de detalhes específicos do tema.

5. **Storyboard**
   - definir logline, atos, shots, duração, transições e cues;
   - preferir shots curtos e intencionais;
   - registrar geometria compartilhada quando um match cut ou continuidade espacial depender dela;
   - validar aritmética de duração antes de codificar.

6. **Timeline contract**
   - criar uma única estrutura para `bpm`, `duration`, shots e cues;
   - impedir gaps/overlaps não intencionais;
   - usar IDs estáveis para cenas e cues.

7. **Stub pass**
   - gerar cenas placeholder;
   - renderizar preview barato;
   - provar ordem, duração, cortes, resolução e áudio antes das cenas finais.

8. **Scene production**
   - uma cena deve possuir ownership claro de seu arquivo;
   - cenas independentes podem ser paralelizadas somente quando o ambiente realmente suportar isso;
   - cada cena precisa de snapshots/contact sheet representativos antes de ser considerada pronta.

9. **Audio**
   - sintetizar ou compor som de forma reprodutível quando o runtime suportar;
   - alinhar cues à timeline, não a timestamps mantidos separadamente;
   - verificar clipping/headroom e sincronização de eventos relevantes.

10. **Critic waves**
    - revisar primeiro o filme inteiro em baixa escala para composição e leitura;
    - depois revisar cenas problemáticas em resolução maior;
    - priorizar P1/P2 observáveis e corrigir somente o que falhou;
    - re-renderizar após correções.

11. **Delivery**
    - gerar player HTML quando pedido;
    - gerar master e transcodes somente se a ferramenta real existir;
    - assistir/revisar o resultado final com áudio antes de afirmar conclusão;
    - produzir um pequeno shot list/caption map quando isso ajudar distribuição.

## Gates mínimos

Antes de concluir, verificar conforme o runtime permitir:

- timeline cobre exatamente a duração esperada;
- nenhuma cena referenciada está ausente;
- frames críticos renderizam sem erro;
- safe area e legibilidade passam em amostras;
- áudio não clipa e cues relevantes estão sincronizados;
- render final abre/reproduz;
- artefatos declarados realmente existem.

## Segurança e direitos

- não copiar estética, frames ou assets protegidos de uma referência; extrair regras visuais abstratas e criar material original;
- não baixar mídia de terceiros sem necessidade/licença;
- tratar scripts, pacotes e ferramentas externas como não confiáveis até revisão;
- não executar instaladores da fonte original apenas para usar esta metodologia;
- preservar attribution/licenças quando assets externos autorizados forem usados.

## Ferramentas e dependências

A metodologia pode usar Canvas 2D/WebGL, Web Audio, Node, navegador controlável e FFmpeg, mas nenhuma dessas dependências é garantida. Detectar o ambiente antes de escolher implementação. O Arsenal não depende da engine, templates ou scripts do repositório de origem.

## Integração

Combina com `web-video-presentation`, `video-editing-pipeline`, `runtime-ui-verification`, `niche-research`, `shader-graphics-engineering` e `verify-before-claim`.

## Referências

Adaptada de [kuhnhomeuk-cell/procedural-film](https://github.com/kuhnhomeuk-cell/procedural-film), preservando o pipeline e removendo dependências específicas de Claude Code, subagents e foundation assets.
