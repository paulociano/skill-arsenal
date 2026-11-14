# Avaliação externa: hotheadhacker/seedbox-lite

- Data da avaliação: 2026-11-14
- Fonte: https://github.com/hotheadhacker/seedbox-lite
- Versão examinada: branch main, commit `6a89d19747e1b050ea5cc1d12265d5e97f7d38d7` (último commit recuperado, 2025-08-20)
- Classificação do Arsenal: **D — aplicação técnica que depende de runtime e infraestrutura**
- Decisão: **REFERENCE_ONLY / não adotar como skill ou stack**
- Revisão de segurança: **CAUTION para estudo estático; não recomendado para deploy público sem correções**
- Evidência: **static_only**, sem instalação, execução, scanner ou teste dinâmico.

## O que faz de verdade

Aplicação web para gerenciamento e streaming progressivo de torrents. Frontend React/Vite; servidor Node.js/Express e WebTorrent; Docker Compose e PM2. Não contém processo de agente, skill ou instruções de roteamento para o ChatGPT.

## Quando seria útil

Como aplicativo pessoal self-hosted para reproduzir conteúdos via torrents quando o usuário tem direitos legais de acesso e compartilhamento; como arquitetura de referência para avaliação de aplicações de mídia, streaming e containers. Não é pertinente à execução nativa de tarefas por ChatGPT.

## Ganho marginal e overlap

Não acrescenta metodologia nova relevante a `application-build-audit-loop`, auditoria de segurança ou fluxos gerais de construção de aplicações. Não importar código nem criar skill artificial. Uma eventual implementação específica deve partir de requisitos do usuário e passar pelos owners existentes.

## Dependências e portabilidade

Requer Node.js, WebTorrent, Express, React/Vite, armazenamento e conectividade P2P, opcionalmente Docker/PM2. ChatGPT não se converte em servidor BitTorrent por meio de prompt/skill. A licença personalizada é somente não comercial; proíbe uso comercial sem permissão escrita. Não é uma licença permissiva padrão.

## Revisão de segurança (inspeção estática)

Arquivos analisados: `README.md`, `LICENSE`, `server/index.js`, `server/package.json`, `client/package.json`, `docker-compose.yml` e `.env.example`.

1. `server/index.js` linha 1133 verifica senha apenas no endpoint `/api/auth/login`, retornando sucesso/falha sem sessão ou token; rotas sensíveis como `POST /api/torrents` (linha 1162), upload (1247) e `DELETE /api/torrents` (2102) não apresentam middleware de autorização no arquivo examinado. Risco: operações sem autenticação efetiva.
2. CORS é configurado com `origin: true`, `credentials: true` e cabeçalhos adicionais `Access-Control-Allow-Origin: *` (linhas 1092-1123), configuração excessivamente permissiva e contraditória.
3. `ACCESS_PASSWORD || 'seedbox123'` (linha 1135) usa senha de fallback previsível.
4. `docker-compose.yml` publica backend e frontend via mapeamento padrão sem restringir binding ao loopback; atenção se exposto na rede.
5. README menciona comandos de testes que não aparecem em `server/package.json` e `client/package.json` inspecionados, indício de documentação não alinhada à automação disponível.
6. Licença restringe explicitamente uso comercial e redistribuição requer avisos apropriados; há implicações jurídicas e de direitos autorais para os conteúdos transmitidos.

Não se afirma ocorrência de ataque, exfiltração ou vulnerabilidade explorada. É revisão estática, limitada aos arquivos selecionados.

## Classificação e decisão

**D**, por depender de sistema rodando e não fornecer skill reutilizável em ChatGPT. **Não adotar** nem incorporar metodologia: valor incremental insuficiente, sobreposição com owners existentes, riscos de segurança e limitações de licença. Não atualizar índice pois nenhuma skill foi criada/alterada.

## Fontes e trilha

- https://github.com/hotheadhacker/seedbox-lite
- https://github.com/hotheadhacker/seedbox-lite/blob/main/server/index.js
- https://github.com/hotheadhacker/seedbox-lite/blob/main/LICENSE
- https://github.com/paulociano/skill-arsenal/blob/master/stacks/evaluate-and-import-skill/STACK.md
- https://github.com/paulociano/skill-arsenal/blob/master/skills/skill-security-review/SKILL.md

Registro de avaliação externa; publicação e SHA registrados no commit GitHub que adicionar este arquivo.
