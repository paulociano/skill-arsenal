# Avaliação — YouTube transcript

Data: 2026-09-23

## Problema

Criar uma skill dedicada a obter transcrições de vídeos do YouTube, inclusive vídeos longos, preservando timestamps, idioma, tipo de legenda e cobertura, sem transformar `watch-video` em uma skill excessivamente ampla.

## Fontes avaliadas

### ZeroPointRepo/youtube-skills — `skills/transcript/SKILL.md`

Classificação: **A na metodologia / D na implementação original**.

Valor:
- trigger muito claro para qualquer tarefa que dependa do conteúdo falado;
- resposta com timestamps e metadata;
- tratamento explícito de erros;
- boa separação entre transcript e outras operações de YouTube.

Limitação:
- depende obrigatoriamente de TranscriptAPI.com e `TRANSCRIPT_API_KEY`;
- isso não é uma capacidade nativa garantida do ChatGPT;
- não deve ser copiado como dependência obrigatória do Arsenal.

Decisão:
- adotar o fluxo conceitual, remover a dependência de API externa e usar roteamento por capacidade real.

Fonte: https://github.com/ZeroPointRepo/youtube-skills

### jdepoix/youtube-transcript-api

Classificação: **D**.

Valor:
- biblioteca madura para captions manuais e automáticas;
- lista idiomas;
- distingue transcript manual de gerado;
- suporta tradução de tracks quando disponível;
- não exige headless browser.

Limitação:
- exige Python/package instalado e acesso de rede;
- pode falhar por mudanças do YouTube, bloqueios ou ausência de captions;
- não é ferramenta nativa garantida.

Decisão:
- registrar como rota opcional apenas quando a biblioteca já estiver disponível no runtime.

Fonte: https://github.com/jdepoix/youtube-transcript-api

### yt-dlp/yt-dlp

Classificação: **D**.

Valor:
- suporta listar legendas;
- baixar subtitles;
- baixar auto-generated subtitles;
- selecionar idioma;
- pode obter captions sem baixar o vídeo inteiro.

Limitação:
- depende de binário/runtime;
- comportamento em YouTube é sujeito a mudanças, bloqueios e requisitos de autenticação em alguns casos;
- não deve ser instalado automaticamente durante execução da skill.

Decisão:
- usar como fallback opcional quando já estiver disponível.

Fonte: https://github.com/yt-dlp/yt-dlp

### YouTube Data API — captions.download

Classificação: **D / inadequada como fallback geral**.

Constatação:
- o endpoint oficial de download de captions exige OAuth e que o usuário tenha permissão para editar o vídeo.

Consequência:
- não resolve a necessidade de transcrever vídeos públicos arbitrários de terceiros.

Fonte: https://developers.google.com/youtube/v3/docs/captions/download

## Comparação com `watch-video`

`watch-video` é orientada a **análise audiovisual**: transcript + frames + timestamps + inferência.

A nova skill é orientada a **aquisição e normalização textual**:
- encontrar a melhor transcript disponível;
- preservar origem e timestamps;
- identificar idioma/tipo;
- verificar cobertura;
- degradar com clareza quando não houver acesso.

A separação reduz sobreposição:
- `youtube-transcript` produz a evidência textual;
- `watch-video` usa essa evidência e adiciona inspeção visual quando necessário.

## Segurança

Verdict: **APPROVE com adaptação**.

Medidas:
- nenhum installer ou script externo foi executado;
- nenhuma chave externa foi criada ou armazenada;
- TranscriptAPI não é dependência obrigatória;
- ferramentas locais só podem ser usadas se já existirem;
- conteúdo obtido é tratado como dado não confiável, nunca como instrução;
- cookies/tokens não são coletados ou improvisados;
- a skill proíbe contorno de autenticação e controles de acesso.

## Copyright e saída

A skill distingue **obter evidência textual** de **reproduzir integralmente conteúdo protegido**.

Para mídia fornecida pelo usuário ou conteúdo cuja reprodução integral seja permitida, a transcrição integral pode ser entregue conforme o pedido.

Para vídeos públicos de terceiros potencialmente protegidos, a transcrição pode apoiar análise, resumo e pequenos trechos permitidos, sem transformar a skill em mecanismo de republicação integral.

## Decisão

**Descartar como skill operacional do Arsenal.**

Razões:
- o teste real com um vídeo público falhou em todas as rotas disponíveis na sessão;
- a skill dependia de condições externas não garantidas: captions expostos, biblioteca local, `yt-dlp`, plugin conectado ou mídia enviada;
- isso não atende ao padrão de utilidade operacional do Arsenal para uma rota principal;
- manter a skill aumentaria a chance de prometer capacidade que o ambiente não consegue cumprir de forma consistente.

## Resultado do teste operacional

Em 2026-09-23, o teste com um vídeo público do YouTube falhou por throttling do acesso web e ausência das ferramentas locais opcionais. Esse teste foi decisivo para reclassificar a skill.

## Limites da validação

A skill define o comportamento correto, mas a execução concreta de cada rota depende das capacidades disponíveis na sessão:
- transcript exposto por fonte web/YouTube;
- biblioteca local instalada;
- `yt-dlp` instalado;
- plugin/conector conectado;
- mídia fornecida pelo usuário.

Não há promessa de que qualquer URL pública do YouTube sempre produzirá transcript.
