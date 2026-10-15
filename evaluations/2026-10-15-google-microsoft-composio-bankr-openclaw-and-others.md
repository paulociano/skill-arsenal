# Avaliação em lote — 12 fontes / coleções (2026-10-15)

## Escopo e método
Solicitação: avaliar todas as skills dos endereços enviados. Links originais abrangem **12 repositórios distintos** após corrigir o URL colado `MengTo/Skillshttps://github.com/Chalarangelo/30-seconds-of-code`. Fonte oficial de ownership: `ARSENAL INDEX.md` do Skill Arsenal. Método: `arsenal-autopilot` + `skill-security-review`. A presente rodada faz **inventário estrutural e triagem de capacidades por coleção** e leitura aprofundada de exemplos-chave, **não** auditoria individual de cada uma das milhares de skills. Nunca interpretar classes abaixo como aprovação de instalação de cada integrante.

Nenhum installer, navegador externo, transação, CLI, script ou pacote foi executado.

## Matriz de decisão (por coleção)
| Origem | Evidência de escopo | Classe | Decisão | Owner/justificativa |
|---|---|---|---|---|
| [google/skills](https://github.com/google/skills) | `skills/` por ads, analytics, cloud, developers, identity; 140 pastas Cloud e 14 Ads e 2 Analytics observadas | A/D | KEEP_EXTERNAL_REFERENCE | Cloud/GCP e Google Ads são SDKs/produtos; ativar por projeto e documentação de versão, não copiar integrações sem credenciais |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 1 skill `karpathy-guidelines`, lida integralmente | B | ABSORB_METHOD_ONLY, sem alteração | coding-agent-engineering, code-review, verify-before-claim: simplificação, edits cirúrgicos, sucesso verificável já cobertos |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | `composio-skills/` com 833 entradas no endpoint consultado; outras skills raiz | D | KEEP_EXTERNAL_REFERENCE | catálogo de wrappers SaaS; requer provider, autorização, APIs; não importar massas de automação |
| [antfu/skills](https://github.com/antfu/skills) | 11 pastas: `antfu`, `antfu-create-pr`, `nitro`, `nuxt`, `pinia`, `pnpm`, `unocss`, `vite`, `vitepress`, `vitest`, `vue` | B/D | KEEP_EXTERNAL_REFERENCE | preferências/guia vivo do ecossistema Vue; bom padrão de origem de docs por submodules, não substituir documentação atual com cópia fixa |
| [browser-act/skills](https://github.com/browser-act/skills) | `browser-act/SKILL.md` lido | D | KEEP_EXTERNAL_REFERENCE | depende de `browser-act-cli` e browser/CDP, pede comandos que carregam instruções dinamicamente; não disponível automaticamente |
| [BankrBot/skills](https://github.com/BankrBot/skills) | endpoint raiz retorna 157 entradas; muitas habilidades DeFi, carteira, tokens, monitoramento; `aeon-skill-security-scan` analisado | B/D | UPDATE_EXISTING (somente revisão de segurança) | absorver detecção de Unicode invisível/obfuscação/delta em `skill-security-review`; **não instalar nem ativar execução financeira** |
| [microsoft/skills](https://github.com/microsoft/skills) | README declara ~175 skills; `.github/skills` com 61 subpastas mais plugins/linguagens | A/D | KEEP_EXTERNAL_REFERENCE | alta especificidade Azure/Foundry/M365; usar somente quando projeto depender daquele SDK e validar versão |
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | README declara >5.300 links externos organizados em 30 categorias | D | KEEP_EXTERNAL_REFERENCE | diretório de descoberta e não pacote de 5.300 skills auditadas; origem individual deve ser resolvida e revisada |
| [MengTo/Skills](https://github.com/MengTo/Skills) | 9 áreas `agent-skills/`; 20 pastas em `agent-skills/codex` observadas | B/D | KEEP_EXTERNAL_REFERENCE | referências de web, motion, 3D e design; owners já existentes `web-design-engineer`, `creative-web-engineering`, `runtime-ui-verification` |
| [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | README: artigos e snippets, não catálogo de agent skills | B | KEEP_EXTERNAL_REFERENCE | referência de código; nunca importar snippets como instructions. Licença de snippets CC-BY-4.0 e conteúdo de site com restrição distinta |
| [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | 17 pastas em `skills/`; `mmx-cli` lida | B/D | KEEP_EXTERNAL_REFERENCE | owners existentes em frontend, mobile, media e shaders; mmx CLI, chaves/API e custos não automaticamente disponíveis |
| [slavingia/skills](https://github.com/slavingia/skills) | 10 skills de empreendedorismo, `processize` lida | B | ABSORB_METHOD_ONLY, sem nova skill | `venture-building-cycle`, `first-customer-research` e validação manual-first já cobrem esta abordagem |

## Riscos e gates
- Catálogos massivos `ComposioHQ`/`VoltAgent` são inventários de fornecedores, não evidência de qualidade. Não assumir que cada link foi auditado.
- BankrBot: exposição a trading, tokens, blockchains, transações e carteiras; não executar comandos, transferências, bridges, assinaturas, connects ou movimentação financeira com autorização genérica para avaliação de skills. Avaliação individual obrigatória antes de qualquer adoção.
- BrowserAct: skill substitui leitura estática por instrução dinâmica de CLI, tem instalação Python e processamento de captcha/controle de browser. Exige boundary de autorização e verificação real do payload.
- MiniMax: API keys e `--yes`/non-interactive em comandos; evitar bypass de gates e não colar secrets no chat.
- Google/Microsoft: SDKs e comandos cloud com custos, rede, permissões e possibilidade de alteração de infraestrutura. Validar documentação e escopos de serviço.
- Não copiar o conteúdo de repositórios externos sem licença/proveniência adequadas; Chalarangelo distingue licença de snippets do restante do conteúdo.
- Metodologia de scanner isolada não prova ausência de vulnerabilidade; findings contextuais importam.

## O que foi materializado
- `skills/skill-security-review/SKILL.md`: adicionados controles para caracteres invisíveis/bidi, comandos codificados, URLs exfiltradoras, false-positives em blocos de código e delta findings auditáveis.
- Nenhuma nova skill ou stack: não demonstrado ganho suficientemente singular sem sobreposição.
- Índice sem alteração: nomes e descriptions não mudaram.

## Limites de cobertura e próximos passos técnicos
Esta rodada avaliou o **escopo, a arquitetura, os agrupamentos e casos representativos dos 12 repositórios**, mas não leu cada `SKILL.md` dos catálogos de 833+ e 5.300+ entradas. Os números são fotografias de endpoints/readmes em 2026-10-15, podem mudar e não equivalem a contagem de arquivos SKILL.md válidos. Não declarar aprovação, descarte individual definitivo nem auditoria de supply chain de cada entrada. Para adoção futura, resolver cada candidata de alto valor na fonte original e aplicar revisão estática, ownership e validação funcional antes de editar o Arsenal.
