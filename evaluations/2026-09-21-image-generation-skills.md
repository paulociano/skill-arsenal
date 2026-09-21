# Avaliação de cinco fontes de geração de imagens

Data: 2026-09-21. Stack: evaluate-and-import-skill, com skill-security-review e skill-builder. Fonte canônica consultada: ARSENAL INDEX.md e arsenal-router. As cinco URLs concatenadas do pedido foram separadas sem alterar seus destinos.

## Decisão

Enriquecer editable-visual-design com uma referência curta sobre consistência entre assets, edição por referência, capacidades reais e validação do arquivo final. Não criar skill genérica de geração nem stack nova: a ferramenta nativa já gera/edita imagens; o Arsenal já organiza design editável e exploração de logos. Não instalar provedores, CLIs ou MCPs externos.

A classificação principal abaixo descreve a fonte original. O conteúdo metodológico aproveitado de fontes D é categoria B, não uma integração instalada.

| Fonte | Categoria | Ganho real e ocasião de uso | Decisão |
| --- | --- | --- | --- |
| adamd9/skill-image-gen | D — técnica | Guia de chamadas OpenAI/Gemini para agentes sem ferramenta nativa; pouco valor incremental neste ambiente | Não importar; registrar redundância e problemas de onboarding |
| guinacio/claude-image-gen | D — técnica | CLI/MCP com referências, roteamento, máscaras e validações de entrada/saída; útil em pipeline de assets com runtime próprio | Adaptar apenas disciplina de referências, composição e validação para a skill existente |
| ZeroLu/Ultimate-AI-Media-Generator-Skill | D — técnica | Cliente CyberBara para tarefas de imagem/vídeo/áudio/música, cotação e acompanhamento assíncrono | Não instalar; aproveitar controle de custo e estado somente quando integração real exigir |
| lxfater/nano-image-generator-skill | D — técnica | Script Gemini com referências, séries e detecção de formato | Incorporar conceitos de âncora visual e validação, em redação própria; não copiar script |
| github/awesome-copilot — generate-image | D — técnica | Mesma implementação textual da fonte adamd9 no snapshot lido | Não importar duplicata |

Os dois arquivos generate-image foram comparados integralmente e são idênticos no conteúdo retornado. Isso não estabelece autoria histórica.

## Fontes e revisões

- [adamd9/skill-image-gen](https://github.com/adamd9/skill-image-gen/tree/1002e0312e3b1ee0750f6cb915875082a3d7979b): README.md, skills/generate-image/SKILL.md, install.sh, LICENSE.
- [guinacio/claude-image-gen](https://github.com/guinacio/claude-image-gen/tree/23d4c8cfc4d7cef1c6bfae27e9cf1ce1eb42201a): README.md, skills/image-generation/SKILL.md, references/prompt-crafting.md, .mcp.json, mcp-server/package.json e módulos src de runtime, referências, armazenamento e serviço.
- [ZeroLu/Ultimate-AI-Media-Generator-Skill](https://github.com/ZeroLu/Ultimate-AI-Media-Generator-Skill/tree/f28e58f2b9814b2056417377c46f34fd35219702): README.md, SKILL.md, módulos de configuração, cliente HTTP, credit_guard, wait_task e media_output.
- [lxfater/nano-image-generator-skill](https://github.com/lxfater/nano-image-generator-skill/tree/017d4c02b62f03f2486ec5f9b00ceafae8658e3d): README.md, SKILL.md e scripts/generate_image.py.
- [awesome-copilot/generate-image](https://github.com/github/awesome-copilot/blob/ad4c196b933c5ca7f82a5ba78969ddcd2603ba80/skills/generate-image/SKILL.md): arquivo solicitado e LICENSE.

As revisões foram verificadas pelos endpoints de commits. Modelos, limites, preços e alegações comerciais nos READMEs são declarações das fontes, não disponibilidade ou desempenho comprovados nesta avaliação.

## Dependências e segurança

Revisão estática manual, sem executar código externo ou instaladores. Veredito CAUTION para as cinco implementações originais; não é acusação de comportamento malicioso nem certificação de segurança.

### adamd9 e awesome-copilot

Dependem de chaves OpenAI/Gemini, rede e execução de chamadas HTTP. O onboarding pede fornecimento de chave e persistência em perfil de shell; não transportar esse procedimento para o Arsenal. O instalador adamd9 copia ou cria symlink em diretórios Claude/Copilot, sobrescreve SKILL.md e pode remover o diretório da skill no uninstall. Foi apenas lido. Os exemplos fixam modelos e parâmetros cuja validade atual não foi testada. Para este ambiente, solicitar chaves seria dependência desnecessária.

### guinacio

Depende de Node >=20, SDKs, bundle/CLI ou servidor MCP e chaves de provedores. O carregador verifica tamanho e assinatura de imagens; o armazenamento verifica contenção de caminho usando realpath e ajusta extensão conforme MIME. São controles úteis, mas não equivalem a isolamento total ou auditoria do bundle distribuído. Referências locais são enviadas ao provedor escolhido e saídas são gravadas no disco. Não transportar o gatilho amplo ALWAYS para todo site/deck nem a suposição de que uma seção sem imagem precisa de geração. Bundles, dependências transitivas e todos os clientes de provedores não foram auditados integralmente.

### ZeroLu

Depende de Python e API CyberBara. O cliente transmite prompts, arquivos e credencial ao serviço. config.py persiste chaves passadas por argumento ou prompt em arquivo local; tenta permissões 0700/0600, mas ignora erros de chmod. O prompt usa input, sem ocultação. credit_guard soma cotações e exige confirmação, com bypass --yes que depende de autorização prévia. wait_task acompanha a tarefa; timeout <=0 elimina o prazo. media_output aceita URLs HTTP/HTTPS retornadas pelo serviço, lê todo o corpo e pode abrir o arquivo por subprocess; o fluxo inspecionado não valida assinatura/tamanho da mídia antes dessa abertura. Esses comportamentos não são necessários à adaptação. Não afirmar que modelos, economia de créditos ou geração audiovisual estão disponíveis no ChatGPT.

### lxfater

Depende de Python e Gemini. get_api_key orienta inserir a chave diretamente no código e a requisição a coloca na query string: prática rejeitada para a adaptação. O script detecta assinaturas PNG/JPEG/WebP/GIF e corrige extensão, mas trata formato desconhecido como PNG, trunca referências excedentes e pode sobrescrever o destino. Preservar apenas a ideia de validar formato; exigir falha explícita para tipo desconhecido. Não transportar limites ou modelo fixo como capacidades nativas.

## Licença

LICENSE MIT lida em adamd9, guinacio, ZeroLu e awesome-copilot. Não foi encontrado arquivo LICENSE na árvore lxfater inspecionada; não presumir licença por ser público. A alteração usa síntese autoral de ideias gerais, sem redistribuir scripts, templates, bundles ou trechos substanciais dessas fontes.

## Ledger de adaptação

| Fragmento/capacidade | Preservar | Remover/adaptar | Destino |
| --- | --- | --- | --- |
| Composição e referências de guinacio | Papel do asset e referência explícita | Gatilho universal, CLI obrigatório e presets incidentais | Referência de editable-visual-design |
| Séries de lxfater | Primeira imagem como referência comum | Limite fixo de 14 e chamadas Gemini | Âncora estável com revisão lado a lado |
| Formato de lxfater/guinacio | Conferir arquivo e extensão | Fallback cego para PNG; MIME como prova suficiente | Verificação de integridade, dimensões e alpha |
| Cotação/estado de ZeroLu | Custo autorizado e tarefa acompanhada | Nova confirmação redundante, cache de chave e auto-open | Orientação condicional a integração real |
| Chamadas de adamd9/Copilot | Nenhuma capacidade nova necessária | Onboarding e duplicação do gerador nativo | Somente registro da avaliação |

## Validação e limites

- Alteração limitada a SKILL.md existente, uma referência e esta avaliação.
- Nome, description e fronteiras de acionamento preservados; não há necessidade de mudar o índice.
- Revisão de cenários: série de cards usa âncora comum; edição preserva imagem-base; arquivo de tipo desconhecido não é rotulado PNG; tarefa incerta não é reenviada.
- Near-misses: pedido de imagem isolada usa ferramenta nativa; página sem raster necessário não dispara geração; diagrama factual não vira imagem generativa.
- Ganho em relação ao texto anterior: passa de instruções genéricas de batch/crop para papéis de referência, âncora estável e validação explícita do arquivo.
- Estas verificações são estruturais e de cenários, não benchmark empírico de qualidade visual. Nenhuma imagem foi gerada e nenhuma API paga foi testada.
