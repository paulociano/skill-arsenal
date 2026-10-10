# Avaliação: God's Eye View + Pinokio (2026-10-10)

## Fontes
- https://github.com/bilawalsidhu/gods-eye-view (branch main; README, package.json, SECURITY.md consultados em 2026-10-10)
- https://github.com/pinokiocomputer/pinokio (branch main; README, package.json consultados em 2026-10-10)
- Arsenal: `ARSENAL INDEX.md`, `stacks/arsenal-autopilot/STACK.md`, `stacks/evaluate-and-import-skill/STACK.md` e `skills/skill-security-review/SKILL.md`.

## God's Eye View
- **O que faz:** aplicação web local-first de visualização geoespacial 3D com camadas de fontes públicas de aeronaves, navios, satélites, fenômenos naturais, câmeras e outras fontes; controles de visualização e agente de voz opcional.
- **Classe:** **D — sistema técnico**. Não é uma Agent Skill nem um método portável diretamente para ChatGPT.
- **Dependências:** Node 24.14+ ou 26, npm/Vite/Cesium, browser/WebGL, provedores de dados; Cesium ion/Google Maps/OpenAI e demais chaves apenas para determinadas funcionalidades.
- **Valor incremental:** arquitetura modular por camadas, telemetria com estado de frescor/fallback, localização visual e interface comandada por voz; referências de implementação para engenharia geoespacial, produto 3D e agentes de voz. O Arsenal já cobre engenharia de software, realtime-voice-agent-engineering e creative-web-engineering de forma geral.
- **Decisão:** `KEEP_EXTERNAL_REFERENCE`; não criar skill autônoma sem caso recorrente de engenharia geoespacial.
- **Segurança:** `CAUTION`. Dados públicos não equivalem a cobertura em tempo real integral; tráfego é parcialmente simulado. O SECURITY.md identifica limites de hardening para produção e chaves publicadas no cliente que exigem restrições. Segredos de servidor em arquivos locais ignorados, mas não criptografados. Integração experimental com credenciais Codex/OAuth não deve ser presumida disponível ou suportada. Provedores, licenças e cotas requerem validação. O material não foi instalado ou executado; nenhum audit completo de dependências ou runtime.
- **Licença:** package.json identifica MIT; conferir termos específicos de dados/assets e LICENSE antes de reutilizar conteúdo.

## Pinokio
- **O que faz:** lançador desktop Electron que instala e inicia apps/scripts locais com interface.
- **Classe:** **D — infraestrutura de execução**; não é uma skill utilizável nativamente por este ChatGPT.
- **Dependências:** Electron, Node, instaladores e scripts/gerenciadores locais de terceiros; permissões de shell e rede.
- **Valor incremental:** padronização da experiência de instalação, descoberta e execução de projetos open source. O Arsenal já contém `ai-workflow-automation-engineering`, `software-engineering-cycle` e `skill-security-review`; isso não gera novo workflow portátil.
- **Decisão:** `KEEP_EXTERNAL_REFERENCE`; não criar skill nem stack. Pode ser recomendado como opção de infraestrutura quando o ambiente desktop do usuário puder executá-lo.
- **Segurança:** `CAUTION`. O README informa expressamente que scripts podem executar quaisquer comandos, downloads e operações shell. Isolamento por diretórios e processo de revisão de scripts não equivalem a sandbox forte, imunidade contra malware ou segurança garantida. Inspecionar cada script e suas dependências, fixar versões e limitar credenciais/permissões antes de executar. Nenhum instalador foi executado nem auditado integralmente.
- **Licença:** MIT no repositório.

## Relação
O God's Eye View documenta instalação via Pinokio 8.2+ como caminho local sem terminal. Essa integração é operacional e externa ao Arsenal; não cria capacidade disponível automaticamente na sessão ChatGPT.

## Ownership e resultado
- **Owners já existentes:** software-engineering-cycle, realtime-voice-agent-engineering, creative-web-engineering, skill-security-review.
- **Novo comportamento comprovado para Agent Skill:** nenhum.
- **Should-trigger futuro:** pedido concreto para projetar sistema com camadas de dados geoespaciais 3D e fontes públicas, quando houver ambiente/código alvo.
- **Near-miss:** compartilhar links de aplicativos desktop sem pedido de instalação/alteração de software.
- **Modificações:** somente este registro em `evaluations/`; `ARSENAL INDEX.md` não muda pois não há skill/stack nova ou description alterada.
- **Limites:** avaliação documental estática baseada nas fontes acima, não é certificação de segurança nem teste de runtime.
