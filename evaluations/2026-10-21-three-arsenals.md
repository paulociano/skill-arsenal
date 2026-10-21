# Avaliação de três arsenais — 2026-10-21

## Escopo e método
Stack arsenal-autopilot; revisão manual estática e seletiva de README e candidatos incrementais, comparação com owners canônicos lidos no GitHub. Não é auditoria integral de todos os módulos ou scripts. Nenhum installer, pacote ou código externo executado. Nenhum catálogo importado em massa.

## Decisões por fonte
| Fonte | Classe | Decisão | Valor e limites |
| --- | --- | --- | --- |
| mgiovani/cc-arsenal | A/D; B para métodos absorvidos | UPDATE_EXISTING | README anuncia 52 skills; shortlist ci-local e i18n-check. Incorporados espelho local de CI com tabela de cobertura e comparação de catálogos. Outros grupos de review, docs, design, Git, imagem e orquestração ficam como referência por overlap plausível no índice; não foram todos auditados individualmente. |
| manyuegong33/r0crawl_skills | D; B para método de evidência | UPDATE_EXISTING / KEEP_EXTERNAL_REFERENCE | README anuncia 196 módulos. Lidos router e reconstruction-and-parity. Absorvidos preservação raw/derived, validação de dump e primeira divergência em fixtures. Catálogo especializado permanece referência; não importar evasão, anti-bot, hooks, anti-cheat ou execução de amostras. Não há conclusão de segurança sobre os módulos não lidos. |
| gutomec/ai-public-arsenal | A/D; B para contratos portáveis | UPDATE_EXISTING | Lidos README, protocolo v2 (marcado superseded), protocolo v4 ativo e aiox-autopilot. Absorvidos requisitos obrigatórios/opcionais, limites e distinção prompt/enforcement, além de falhas compartilhadas de wave. Não importar harness ou pipeline de deploy irrestrito. |

## Capability ledger e arquivos alterados
- CI local → skills/software-testing-engineering/SKILL.md: comandos derivados do workflow, versões/matriz/serviços/secrets e resultado por step; execução local não prova gate remoto.
- Integridade i18n → skills/web-quality-audit/SKILL.md: ausentes/idênticas/órfãs, plural/ICU/placeholders, strings hardcoded e scaffold honestamente pendente.
- Investigação reproduzível → skills/code-understanding-audit/SKILL.md: evidência bruta/derivada, dump validado por consumidor, fixture e primeira divergência.
- Portabilidade de workflows → skills/graph-engineering/SKILL.md: dependências de runtime, fallback opcional, requisitos bloqueantes, contratos de handoff e limites efetivos.

São quatro enriquecimentos de owners existentes, sem nova skill, stack ou alteração de name/description; rotas do ARSENAL INDEX.md permanecem válidas, sem necessidade de mudar índice/README.

## Segurança e portabilidade
CAUTION para adoção das fontes como sistemas completos; aceitas somente adaptações metodológicas escritas independentemente. Não alegar ausência de vulnerabilidades sem revisar scripts e dependências.
- cc-arsenal: i18n-check sugere instalador curl-pipe-shell de uv; não adotado. ci-local pode tocar serviços/secrets e executar run steps: adaptação limita escopo e não reproduz deploy/publicação implicitamente.
- r0crawl: módulos sensíveis exigem contexto e autorização específicos; somente métodos genéricos de investigação absorvidos. Frida, IDA/Ghidra e ferramentas especializadas não presumidos.
- ai-public-arsenal: README/v2 anunciam proteções de loop que v4 §20 classifica como propostas. Preferida distinção explícita da v4; compatibilidade declarada não comprova execução. Autopilot tem defaults arbitrários de score, quantidade de requisitos e deploy automático; não incorporados. Paths de templates no squad não presumidos disponíveis.
- Nenhum aumento de permissões, hook persistente, credencial, serviço ou runtime foi instalado.

## Validação e casos de aceite
Cada adição contém cenário de aceite e near-miss. Validação desta alteração é documental/estática, não benchmark nem execução dos workflows em projetos consumidores.
1. CI com três versões e uma executada → duas não verificadas, sem claim de paridade integral.
2. Chave copiada da origem → presente mas ainda pendente; marca idêntica não é bug confirmado.
3. Dump existente sem leitura por consumidor → validação pendente; string não prova call chain.
4. Paralelismo opcional ausente → sequencial; sandbox obrigatório ausente → bloqueado.

Publicação via contents API com SHA da versão lida, sem force-push. Releitura pós-escrita comparada ao conteúdo esperado para cada arquivo e avaliação antes de comunicar conclusão.

## Fontes e snapshots
Todos consultados na default branch via GitHub em 2026-10-21. SHAs abaixo são blobs, não commits:
- https://github.com/mgiovani/cc-arsenal — README b2d45c94fd8f47babe566662f53859758eebc8bd; skills/i18n-check/SKILL.md 3cceb0a5279eb6e918220fe1d26a527da164e9c4.
- https://github.com/manyuegong33/r0crawl_skills — README 694bfed378f66347a3043f9fa42864ba97f092f7; SKILL.md edd90bcfb0fb4d1dc1820916bcfe7f2779217e70; skills/reconstruction-and-parity/SKILL.md 436e165284ab1071c19e78acc20783b0bc1fa1de.
- https://github.com/gutomec/ai-public-arsenal — README 9cc422141898094426f2cfe8a5630a312160efea; skills/squads/SQUAD_PROTOCOL_V4.md e189f7cbeae9eee9343172ab7e87f59c8f8786a9; skills/aiox-autopilot/SKILL.md cf72c5e82f6346cc9946f4904a1dd59227c97012.
