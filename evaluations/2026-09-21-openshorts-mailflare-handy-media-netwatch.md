# Avaliação: OpenShorts, Mailflare, Handy, mStream, NetWatch, JellyBox e assemblrr

Data: 2026-09-21. Workflow: evaluate-and-import-skill, com comparação pelo índice, revisão estática de segurança e adaptação metodológica. Continuação do pedido de avaliar e publicar mudanças úteis no Arsenal.

## Resultado

Atualizar somente video-editing-pipeline (recortes verticais orientados pela cena) e diagnosing-bugs (cobertura e validade das medições de rede). Não criar sete skills para sete produtos nem nova stack. Não instalar aplicativos, conectar contas, capturar tráfego, enviar mensagens, publicar vídeos ou alterar serviços.

A categoria D identifica dependência técnica do material original, não baixa qualidade. Fora OpenShorts, os itens são principalmente aplicações, não Agent Skills. Os fragmentos metodológicos incorporados são categoria B.

| Fonte | Classe | O que faz e quando usar | Decisão para o Arsenal |
| --- | --- | --- | --- |
| OpenShorts | D | Plataforma e skill API/MCP para cortes, legendas, produção generativa e publicação; útil para produção de shorts com runtime próprio | Adaptar seleção de layout e cuidados de timeline em video-editing-pipeline |
| Mailflare | D | Caixa de e-mail para domínios próprios, com delegação, regras, anexos e APIs; útil quando há projeto de hospedagem de e-mail | Registrar; não confundir inbox com plataforma de campanhas nem duplicar email-campaign-engineering |
| Handy | D | Ditado desktop com transcrição local, atalhos e inserção de texto; útil para acessibilidade e entrada por voz | Registrar como aplicação; instalar uma skill não fornece microfone, ASR ou controle do desktop |
| mStream | D | Servidor de biblioteca musical, streaming, descoberta e federação | Registrar sem importar: nenhuma necessidade atual de operação musical justifica skill |
| NetWatch | D | Diagnóstico de rede por terminal com métricas, captura e detectores dependentes da plataforma | Incorporar disciplina de cobertura/baseline em diagnosing-bugs, sem importar comandos privilegiados |
| JellyBoxPlayer | D | Cliente musical para Jellyfin, Emby e Navidrome, com cache/offline e integração por plataforma | Registrar; padrões gerais já cabem em crossplatform-mobile-engineering; não criar skill de player |
| assemblrr | D | Provisionamento e manutenção de stack de mídia via scripts e Docker/WSL2 | Registrar sem importar; é operação de infraestrutura e não stack metodológica do Arsenal |

## Revisões consultadas

- [mutonby/openshorts](https://github.com/mutonby/openshorts/tree/4b2cf58922587ecb17b990a9575e46320bdb3118) — `4b2cf58922587ecb17b990a9575e46320bdb3118`.
- [hieunc229/mailflare](https://github.com/hieunc229/mailflare/tree/1bf70d2ef2771360a546704182752eb7a1ff63f2) — `1bf70d2ef2771360a546704182752eb7a1ff63f2`.
- [cjpais/Handy](https://github.com/cjpais/Handy/tree/8f9cf53cd1410cda26beea39ff802ac306e39585) — `8f9cf53cd1410cda26beea39ff802ac306e39585`.
- [IrosTheBeggar/mStream](https://github.com/IrosTheBeggar/mStream/tree/ccf78c82017ee46c818caff26c81260b9e1a64e6) — `ccf78c82017ee46c818caff26c81260b9e1a64e6`.
- [matthart1983/netwatch](https://github.com/matthart1983/netwatch/tree/6e282321b845b380e0b3e3fcbb6bb3f935e6003b) — `6e282321b845b380e0b3e3fcbb6bb3f935e6003b`.
- [avdept/JellyBoxPlayer](https://github.com/avdept/JellyBoxPlayer/tree/007e6ccfd64ae1fbd3ca827a00b6982b65f82063) — `007e6ccfd64ae1fbd3ca827a00b6982b65f82063`.
- [soulis-1256/assemblrr](https://github.com/soulis-1256/assemblrr/tree/c7d9ff1648c8db16f552cbe93777be83172dd89f) — `c7d9ff1648c8db16f552cbe93777be83172dd89f`.

Fontes lidas: README e licença raiz dos sete projetos; árvore de arquivos para localizar dependências e instruções. Leitura adicional:
- OpenShorts: skills/openshorts/SKILL.md e cloud/LICENSE.
- Mailflare: docs/api.md.
- Handy: src-tauri/Cargo.toml e trecho relevante de src/components/settings/post-processing/PostProcessingSettings.tsx.
- NetWatch: docs/CAPABILITIES.md.
- assemblrr: platform/linux/bootstrap.sh e trecho inicial de bin/setup.sh cobrindo dependências, delegação de scripts, cópia de configuração e início da geração de ambiente.

A avaliação é proporcional à decisão de não executar/importar aplicações. Não é auditoria completa de código, dependências transitivas, instaladores, binários, serviços hospedados ou compatibilidade de plataformas. Preços, velocidade, popularidade e alcance dos READMEs não foram validados e não viraram regras do Arsenal.

## Revisão de segurança e dependências

Veredito de adoção das implementações: **CAUTION** para os sete, pelas superfícies abaixo e pela ausência de teste de runtime. Isso não afirma malícia. A adaptação textual dispensa essas dependências.

### OpenShorts

Docker, Python, FFmpeg, ASR e modelos de visão são necessários na instalação própria; algumas funções usam Gemini, fal.ai, ElevenLabs, Upload-Post e S3. O README distingue clipper local de funcionalidades que ainda precisam de modelos externos, e descreve galeria pública para UGC/avatares. Hospedar por conta própria não significa que todos os dados permaneçam locais.

A skill manda inferir modo self-hosted/anônimo de 401/404 em /api/me: **não incorporar**. Falha de autenticação não comprova autorização ou ausência de quota. Também há divergências documentais sobre quantidade de ferramentas, necessidade de GPU/Gemini e nome do reconhecimento de direitos; não transportar exemplos como contrato executável sem conferir a API real. Publicação, quota e autenticação ficam sob as regras do ambiente e autorização existente.

### Mailflare

Cloudflare Workers/D1/R2 e permissões de DNS/Email Routing no modo Cloudflare; Docker/SQLite/arquivos e SMTP no modo alternativo documentado. Conectar ou remover domínio altera recursos de roteamento; a API também pode configurar MX/SPF/DKIM/DMARC. Chaves com escopos, caixas delegadas, anexos, encaminhamento e envio são superfícies sensíveis. Não aplicar tokens amplos sugeridos no README, alterar DNS nem tratar teste de envio como ação implícita de avaliação. A documentação de permissões não prova que todos os controles foram testados.

### Handy

Tauri/Rust, modelos ASR baixados e recursos do sistema operacional. Microfone, acessibilidade, atalhos, clipboard e autostart exigem análise específica no dispositivo. A interface de pós-processamento inclui provedor, URL, chave e modelo: a alegação de ASR local não deve ser generalizada para todo caminho opcional. Dependências Git e atualizador também precisam de verificação antes de instalação. Nenhum áudio foi gravado ou enviado.

### mStream

Servidor e biblioteca em disco, com integrações de transcodificação e recursos opcionais externos. O README declara acesso público por padrão até adicionar usuário; não expor serviço assumindo autenticação habilitada. Quick Sync, P2P e federação têm escopos diferentes; federação concede leitura entre servidores segundo a documentação. Integrações de torrent/yt-dlp e backup podem produzir downloads e escritas. Não há método novo suficientemente específico para importar.

### NetWatch

Rust, coletores por plataforma e permissões de captura; Windows depende de Npcap. O README oferece execução elevada e capacidades de rede/BPF, mas a matriz registra limites reais: métricas TCP ausentes no Windows, atribuição potencialmente obsoleta, gaps de amostragem e aceitação privilegiada pendente. A matriz também contém referências de planejamento desatualizadas em relação ao doctor descrito no início; não transformar documentação em prova de execução.

Captura, PCAP, keylogs TLS e metadados podem conter dados sensíveis. AI Insights é opcional e envia resumos ao endpoint configurado; localhost não prova inferência local. Aproveitar limites de evidência, sem instalar, elevar privilégio ou alterar resolver.

### JellyBoxPlayer

Flutter/Dart, servidor musical acessível, credenciais, armazenamento offline e integrações de mídia do sistema. O README limita a validação OpenSubsonic a Navidrome e marca recursos automotivos como beta. Não prometer compatibilidade universal. A recomendação de ignorar aviso de instalador sem assinatura não foi transportada para o Arsenal. Não houve download ou execução de binários.

### assemblrr

Bash/PowerShell, Docker Compose, Linux/WSL2, credenciais VPN e serviços de mídia. O bootstrap Linux baixa uma branch e executa setup.sh; o trecho inspecionado delega a bibliotecas e pode instalar pacotes com sudo, incluindo atualização integral no caminho Arch. README descreve comandos de purge, destroy, restore e uninstall com efeitos em múltiplos sistemas e disco.

A cadeia foi identificada até setup e seus encaminhamentos, mas bibliotecas chamadas, bootstrap Windows, imagens e payloads não foram integralmente auditados: **instalação não aprovada por esta avaliação**. Não executar curl-pipe-shell/iex para avaliar. Métodos de backup e health checks são genéricos e não justificam nova skill.

## Licenças observadas

- OpenShorts: MIT no núcleo, com exceção explícita de cloud/, sob licença comercial própria.
- Handy e NetWatch: MIT.
- Mailflare e JellyBoxPlayer: GNU AGPL v3 nos arquivos consultados.
- mStream e assemblrr: GNU GPL v3 nos arquivos consultados.

Não redistribuir código, screenshots, binários, instaladores ou templates neste commit. As mudanças são sínteses autorais de métodos, com links para as fontes e revisões.

## Extração e ganho incremental

| Capacidade | Preservar | Excluir | Proprietário e evidência de utilidade |
| --- | --- | --- | --- |
| Recorte vertical | Layout conforme cena, tela legível, duas pessoas realmente simultâneas, timestamps da fonte e prevenção de legenda duplicada | Presets obrigatórios, promessa de viralidade e dependência API/MCP | video-editing-pipeline: texto anterior já tinha EDL/legendas, mas não distinguia split de plano/contraplano |
| Diagnóstico observável | Origem, plataforma, amostragem, cobertura e frescor dos dados | Suposição de saúde por ausência de alerta, privilégios e remediação automática | diagnosing-bugs: texto anterior tinha repro/hipótese, mas não qualificava lacunas de coletores |
| Inbox/ditado/players/provisionamento | Conhecimento da finalidade e limites | Novas skills artificiais e instalação sem necessidade | Somente este registro; sem contrato recorrente novo demonstrado |

## Validação

Frontmatter, nomes e descriptions das duas skills preservados; índice não necessita alteração. Inserções restritas aos dois contextos, sem ampliar permissões.

Revisão de cenários:
- entrevista em plano/contraplano: não usar split que duplica pessoa;
- demonstração com planilha: preservar informação periférica e testar leitura no crop;
- fonte legendada: detectar legenda antes de sobrepor outra;
- coletor sem métricas TCP: ausência de finding não significa ausência do problema;
- baseline com poucas amostras: não declarar prontidão por tempo decorrido;
- pedido de instalar player ou gerenciar inbox: essas duas adições não são gatilhos.

Verificação estrutural e de coerência, sem benchmark, geração/render audiovisual ou captura real. Não foi demonstrada melhoria empírica de performance. Publicar somente mudanças revisadas e verificar conteúdo remoto.
