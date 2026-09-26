# Avaliação — FreeLLMAPI

- Data: 2026-09-26.
- Fonte: https://github.com/tashfeenahmed/freellmapi
- Revisão inspecionada: `a0befbc6718bbbf2d856c9cf08d01a92aefbe1e4`.
- Classificação principal: **D — ferramenta técnica**. Metodologia extraível: **B**.
- Decisão: **adaptar em `model-routing-gateway`**, sem criar skill ou stack duplicada.
- Segurança: **CAUTION** para adoção do software; revisão manual estática e seletiva, não auditoria integral.
- Resultado incorporado: [skill atualizada](../skills/model-routing-gateway/SKILL.md).

## O que faz e quando usar

Gateway que agrega provedores e endpoints próprios em APIs compatíveis com clientes LLM, com seleção de destino, fallback, contabilidade de cotas, credenciais e painel administrativo. Pode servir a experimentação pessoal e comparação de provedores quando há runtime e chaves reais.

O repositório é uma aplicação, não uma Agent Skill pronta. Vai além de um prompt porque executa roteamento, mantém estado e integra APIs; essas capacidades dependem de software em execução. O Arsenal incorpora o procedimento de projeto/verificação, sem afirmar instalação ou conectividade.

O README anuncia bilhões de tokens mensais e centenas de endpoints. São alegações agregadas do catálogo do autor, não disponibilidade demonstrada para o usuário. Não foram verificadas contas, termos ou cotas individuais. Pools compartilhados, credenciais disponíveis, qualidade e elegibilidade podem reduzir muito a capacidade útil.

## Comparação e extração

A skill existente já cobre seleção por capacidade, retry, fallback, cooldown, orçamento, observabilidade e privacidade. Criar outra com a marca do produto duplicaria esse contrato.

| Fragmento da fonte | Capacidade reutilizável | Decisão e prova esperada |
| --- | --- | --- |
| Quota engine; `ratelimit.ts` | RPM/RPD/TPM/TPD, pools compartilhados e leases | Incorporar; duas chamadas não podem consumir a mesma última vaga |
| Cooldown com origem | Separar hipótese de Retry-After, crédito e plano | Incorporar; chave válida não remove bloqueio de crédito |
| Headroom em cache | Separar ranking de admissão | Incorporar; cache não autoriza exceder contador atual |
| Catálogo assinado e overrides | Atualizar metadados preservando decisões locais | Incorporar; assinatura inválida rejeitada e desativação preservada |
| Compatibilidade e modelos unificados | Verificar contrato por endpoint e grupo equivalente | Incorporar; não substituir tools ausentes por texto silenciosamente |
| Fusion e compressão opcionais | Avaliar custo/qualidade/privacidade antes de ativar | Manter como opção; não tornar padrão |
| Instaladores, setup de agentes e MCP | Integrações dependentes de runtime | Não importar comandos nem presumir conexão |

Adaptações próprias: exigir coordenação atômica entre workers, reset conforme cada provedor, escopo de cota por conta/projeto e respeito integral ao prazo explícito do provedor. Essas exigências são critérios do Arsenal, não afirmações de que o projeto já as satisfaz. O código inspecionado usa leases em memória e limita determinado Retry-After a um dia; não copiar esses detalhes como regra universal.

A documentação de catálogo contém formulações divergentes sobre a idade/cadência dos modelos entre tiers. Não transportar promessas de frescor para a skill; verificar catálogo e conta efetivos antes de implantar.

## Dependências e portabilidade

- Implementação: Node.js/TypeScript, servidor Express, armazenamento SQLite e dependências npm; Docker e desktop são alternativas de distribuição.
- Operação: chaves dos provedores, credencial do gateway, chave de criptografia, rede e persistência.
- Catálogo hospedado: serviço externo e assinatura; atualização premium é opcional e não concede cotas upstream.
- ChatGPT: conectores/terminal podem apoiar inspeção e configuração autorizada; não oferecem controle do roteador interno desta conversa.
- Não instalar pacotes, executar setup, alterar clientes consumidores ou provisionar credenciais para avaliar.
- Licença MIT confirmada em `LICENSE`; incorporada metodologia em redação própria, sem copiar implementação.

## Revisão de segurança

Evidências positivas observadas: AES-256-GCM e validação da chave em `crypto.ts`; chave explícita exigida em produção; assinatura verificada antes do parse/aplicação do catálogo em `catalog-sync.ts`; Compose vinculado a loopback por padrão.

Superfícies sensíveis: concentração de chaves upstream, exportações/backups, chamadas a múltiplos terceiros, sincronização remota e dependências de distribuição. A imagem Compose usa `:latest`, inadequada para fixação reprodutível sem digest. Criptografia em repouso não elimina o risco de comprometimento do host/processo.

`SECURITY.md` declara uso individual em rede confiável e ausência de autenticação multi-tenant por design; o README recomenda experimentação, sem SLA, e troca para API paga antes de entrega de produto. Não aprovar automaticamente como serviço público de produção.

O veredito CAUTION não indica malware comprovado nem certifica segurança. Não foram executados scanners, instaladores, dependências, imagens, testes upstream ou chamadas de inferência. Binários desktop, cadeia completa de distribuição, todos os adapters e comportamento de rede não foram auditados.

## Validação da adaptação

- Preservados nome, description e escopo da skill existente; índice não necessita mudança.
- Alteração aditiva, preservando decision engines, Ollama, segurança e integrações existentes.
- Cenários estáticos incluídos na skill: pool compartilhado, concorrência, Retry-After, plano/crédito, assinatura e fallback incompatível.
- Should-trigger: desenhar pool multi-provider gratuito com cotas; investigar 429 sob concorrência.
- Near-miss: responder pergunta comum nesta conversa; criar uma imagem; usar uma única API sem problema de roteamento.
- Ganho sobre a versão anterior: critérios explícitos para dupla contagem de cota, corrida de admissão, cooldown com origem e catálogo remoto.
- Validação documental/estrutural, sem benchmark with/without-skill ou teste operacional do gateway. Não alegar economia ou resiliência medidas.

## Fontes inspecionadas

Todos os caminhos abaixo se referem à revisão fixada acima:

- [README](https://github.com/tashfeenahmed/freellmapi/blob/a0befbc6718bbbf2d856c9cf08d01a92aefbe1e4/README.md)
- [Quota e cooldown](https://github.com/tashfeenahmed/freellmapi/blob/a0befbc6718bbbf2d856c9cf08d01a92aefbe1e4/docs/en/architecture/02-quota-and-cooldown-engine.md)
- [Catálogo](https://github.com/tashfeenahmed/freellmapi/blob/a0befbc6718bbbf2d856c9cf08d01a92aefbe1e4/docs/en/architecture/05-catalog-sync.md)
- [Chaves e segurança](https://github.com/tashfeenahmed/freellmapi/blob/a0befbc6718bbbf2d856c9cf08d01a92aefbe1e4/docs/en/env/02-security-and-keys.md)
- Código: `server/src/services/ratelimit.ts`, `server/src/services/catalog-sync.ts`, `server/src/lib/crypto.ts`.
- Operação/licença: `server/package.json`, `docker-compose.yml`, `SECURITY.md`, `LICENSE`.

Publicação autorizada pelo pedido atual e pelo fluxo de avaliações em AGENTS.md; restrita ao Arsenal.
