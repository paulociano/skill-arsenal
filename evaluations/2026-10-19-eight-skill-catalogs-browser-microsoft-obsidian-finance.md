# Oito repositórios externos: triagem por capacidade (2026-10-19)

## Fonte oficial e método
- GitHub canônico: https://github.com/paulociano/skill-arsenal ; `ARSENAL INDEX.md` lido antes da seleção.
- Stack: `arsenal-autopilot`; owners existentes só quando acrescentam valor real.
- Método: árvore recursiva do GitHub (branch main) para inventário; README de cada fonte; amostra focal de SKILL.md de candidatos; comparação com owners canônicos. Contagens de SKILL.md são ocorrências de arquivo na árvore e **não** cardinalidade de skills únicas ou auditadas.
- Limitação: inventário automatizado de milhares de arquivos não equivale a revisão semântica, segurança ou execução individual. Nenhuma dependência, script, CLI, proxy ou agente externo foi instalado/executado.

## Inventário das fontes e decisão

| Fonte | SKILL.md na árvore | Enquadramento e decisão |
|---|---:|---|
| https://github.com/browser-act/skills | 103 | **B/D**. Browser automation e extração vertical, dependentes da CLI BrowserAct e serviços; absorver somente gestão de sessão, approvals e portabilidade em `agent-action-governance`; demais KEEP_EXTERNAL_REFERENCE. O core requer Python/uv e recomenda stealth, proxies e CAPTCHA; não instalar e não presumir sessão existente. |
| https://github.com/BankrBot/skills | 155 | **D**. DeFi, EVM, smart contracts, wallets, pagamentos, marketplaces e skill security. Múltiplas operações financeiras/on-chain sensíveis e runtimes terceiros. KEEP_EXTERNAL_REFERENCE; `skill-security-review` do Arsenal já inclui padrões da fonte aeon-skill-security-scan. Não importar trades, ordens, chaves ou automações de pagamento. |
| https://github.com/Shubhamsaboo/awesome-llm-apps | 10 | **B/D**. Grande catálogo de apps de exemplo e alguns agent skills. Incorporar scope-creep-detector em `code-review` (B); demais exemplos de apps são referências técnicas que exigem execução, dependências e avaliação caso a caso. |
| https://github.com/microsoft/skills | 212 | **A/D** no ecossistema Azure, majoritariamente SDK/infra específicos (.github/plugins). Skills recentes de custo exigem conexão e métricas reais; KEEP_EXTERNAL_REFERENCE e source-led quando trabalho Azure aparecer. Não alegar integração Azure genérica ou ler dados de conta inexistente. |
| https://github.com/AlphaGBM/skills | 27 | **B/D**. Research quantitativo, mercados, options e carteiras com APIs com restrição; alguns pacotes são **referência**, não integração de API. KEEP_EXTERNAL_REFERENCE; análise pode ser aplicada com dados fornecidos e fontes oficiais, sem inferir preços, garantias ou ordens. |
| https://github.com/sickn33/agentic-awesome-skills | 8360 | **B/D** grande agregador; README declara 2.712+ skills instaláveis, portanto 8.360 SKILL.md em árvore incluem duplicatas/variantes e não são 8.360 skills independentes. AAS Core prioriza descoberta/manifests/preview; métodos já atendidos por arsenal-router/autopilot. KEEP_EXTERNAL_REFERENCE; filtrar origem antes de incorporar. |
| https://github.com/kepano/obsidian-skills | 6 | **A/B/D**. Obsidian Markdown, Bases YAML, JSON Canvas, CLI, Defuddle e Knap. CREATE_NEW `obsidian-vault-authoring` apenas para formatos portáveis; CLI/extração/render externo permanecem referência. |
| https://github.com/browserbase/skills | 18 | **A/B/D**. Browser traces, API observacional, agent experience, UI test, Browserbase cloud, cookie-sync. UPDATE_EXISTING `computer-use-agent-engineering` e `agent-action-governance`; requisitos específicos de Browserbase/CDP são referência. |

**Total inventariado: 8.891 ocorrências de SKILL.md**, não revisadas individualmente. Contagem inclui 103+155+10+212+27+8360+6+18. O inventário usou árvore recursiva completa sem flag de truncamento reportada nas oito respostas; a verificação de qualidade foi por seleção metodológica, não por 8.891 leituras.

## Implementações publicadas
- `skills/computer-use-agent-engineering/SKILL.md`: traces observacionais, correlação ação/network/DOM, limites de OpenAPI derivada, privacidade e compatibilidade. https://github.com/paulociano/skill-arsenal/commit/f0b24b96670eb742c20a5a3a603d08a8c0f06ce8
- `skills/code-review/SKILL.md`: detecção de scope creep; KEEP/SPLIT/JUSTIFY no diff sem modificar working tree. https://github.com/paulociano/skill-arsenal/commit/4788d4682d4895da40e6e25734c9fc7c7cac3de7
- `skills/agent-action-governance/SKILL.md`: cookies, perfis autenticados, browser cloud, takeover e limites de trust/consentimento. https://github.com/paulociano/skill-arsenal/commit/010633c074b2280a83b2b0463f6700380cb1078a
- `skills/obsidian-vault-authoring/SKILL.md`: owner novo para Markdown, Bases, Canvas e templates. https://github.com/paulociano/skill-arsenal/commit/854ed41b1ffeb0b19573b83e0f9dd60588122b89
- `ARSENAL INDEX.md`: rota nova. https://github.com/paulociano/skill-arsenal/commit/e1bac7e3ff36e054a4048216a594cadce3c00680

## Segurança e limitações
- **CAUTION** para execução externa: credenciais, cookies, perfil do browser, proxies, evasão antibot, CDP e traces sensíveis.
- **CAUTION** para operações financeiras: carteira, chaves, assinatura, gastos, contratos e transações irreversíveis. Nenhuma ação de trading ou instalação foi realizada.
- **CAUTION** para catálogo massivo: entradas de múltiplos fornecedores sem trust uniforme; leia fonte específica e versões antes da promoção.
- **CAUTION** para Azure SDKs: versões, subscrição e permissões são pré-requisitos de runtime; apenas uma skill Azure Cost Optimization foi inspecionada em profundidade de cabeçalho/workflow.
- Verificação de código de terceiros: parcial e estática. Ausência de revisão integral impede declarar APPROVE de software externo.
- Nesta rodada não se realizou comparação substantiva de todas as 8.891 definições. A decisão é por capacidade representativa e owners existentes. Reabrir novas candidatas conforme demanda real e evidência.

## Revisão incremental
Adota A/B com implementação materializada e rastreabilidade. D e alternativas já existentes permanecem referência. Nenhum grande catálogo é importado integralmente ou usado como autoridade superior ao índice GitHub do Arsenal.
