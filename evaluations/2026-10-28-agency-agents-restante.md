# Avaliação — msitarzewski/agency-agents, restante do repositório

Data: 2026-10-28
Fonte: https://github.com/msitarzewski/agency-agents (branch `main`, clone raso, MIT)
Continuação de: `2026-10-28-msitarzewski-agency-agents.md` (seis agentes de vendas, finanças e chief of staff) e da triagem `2026-10-22-github-top100-stars-triage.md`.
Pedido do usuário: avaliar o restante.

## Escopo e método

Foram avaliados os 277 agentes restantes (277 + 6 da avaliação anterior = 283 arquivos de agente com frontmatter válido; 16 arquivos de guia, fases e cenários foram ignorados). Pipeline do `arsenal-autopilot`: inventário, comparação por capacidade contra o `ARSENAL INDEX.md`, lacunas confirmadas por busca no índice, leitura integral ou extensa dos candidatos de valor, decisão, implementação e verificação.

### Nível de evidência (importante)

- **Leitura extensa (início do arquivo, frameworks, regras e templates):** change-management-consultant, corporate-training-designer, sales-pipeline-analyst, sales-proposal-strategist, customer-success-manager, operations-manager, academic-statistician, marketing-ai-citation-strategist, design-persona-walkthrough, engineering-incident-response-commander, sales-outbound-strategist, marketing-pr-communications-manager, zk-steward, support-executive-summary-generator, data-privacy-officer, specialized-pricing-analyst.
- **Cabeçalhos e estrutura:** finance-investment-researcher, finance-tax-strategist, finance-bookkeeper-controller, chief-financial-officer, loan-officer-assistant.
- **Apenas frontmatter (nome e descrição) mais comparação com owners existentes:** os demais. Para eles, a decisão `REJECT` ou `KEEP_EXTERNAL_REFERENCE` significa "sem valor incremental evidente frente ao Arsenal e ao uso atual", não "analisado e sem mérito". Uma reavaliação pode mudar a classe se o uso do usuário mudar.

### Segurança

Os agentes são Markdown de instruções, sem scripts de runtime nas divisões lidas. Varredura de padrões (`curl`, `wget`, `eval`, `base64`, `rm -rf`, `sudo`, chaves, senha, token) nas divisões de vendas, finanças e no chief of staff: apenas dois acertos benignos ("tokens de personalização", "design tokens"). Não foi feita varredura nas demais divisões. Nada foi executado; `scripts/` e `integrations/` do repositório (instaladores para outras ferramentas) não foram usados.

### Critérios de rejeição recorrentes

1. Já coberto por owner do Arsenal.
2. Jurisdição ou plataforma sem uso (China, EUA federal, GAAP, HIPAA, TRID, ICD/CPT).
3. Persona sem workflow reutilizável.
4. Execução autônoma de ação externa (pagamentos, envio automático, publicação) em conflito com `agent-action-governance`.
5. Conflito com convenções do Arsenal (por exemplo, psicologizar pessoas ou obrigar frases de persona).

## Resultado

| Decisão | Quantidade |
|---|---|
| CREATE_NEW | 6 |
| KEEP_EXTERNAL_REFERENCE | 109 |
| REJECT | 162 |
| Total avaliado nesta rodada | 277 |

## Skills criadas e prova de valor incremental

| Skill criada | Origem | Comportamento novo | Por que owner existente não resolve | Deve ativar | Não deve ativar |
|---|---|---|---|---|---|
| `change-adoption-management` | change-management-consultant | plano de adoção por ADKAR, diagnóstico de resistência e sustentação 30/60/90 | `stakeholder-strategy` mapeia stakeholders, mas não conduz adoção nem sustentação | "lançamos o novo processo e ninguém usa" | "mapeie o poder de cada stakeholder" |
| `training-program-design` | corporate-training-designer | do problema de negócio ao objetivo mensurável, formação de multiplicadores e avaliação Kirkpatrick | `teach` é aprendizagem individual; `coaching-development-loop` acompanha pessoas | "monte a trilha de capacitação dos multiplicadores" | "me ensine previdência em 4 semanas" |
| `sales-pipeline-diagnostics` | sales-pipeline-analyst | conversão por etapa, tempo parado, cobertura e previsão em faixas com qualidade de dados | `crm-data-quality` limpa cadastro; `product-metrics-diagnostics` é de produto | "por que o funil C2 para C3 caiu este mês" | "deduplique esta planilha de leads" |
| `customer-success-lifecycle` | customer-success-manager | onboarding com critério de sucesso escrito, sinais antecipados de risco, revisão com resultado e expansão conquistada | `support-operations-engineering` é helpdesk; nada cobre o pós-venda | "monte o plano de retenção deste cliente em risco" | "projete a fila de suporte" |
| `process-mapping-improvement` | operations-manager | SIPOC, mapa com tempos, desperdícios, capacidade, SOP e baseline antes e depois | `work-delivery-flow` opera itens; `root-cause-analysis` trata problema pontual | "mapeie o fluxo semanal e ache o gargalo" | "qual a causa raiz deste erro específico" |
| `privacy-program-governance` | data-privacy-officer | inventário, base legal, relatório de impacto, direitos de titulares e incidente, ancorado em LGPD verificada | `secure-code-privacy-review` revisa código, não governança | "como adequamos o tratamento de dados dos clientes à LGPD" | "revise este diff por vazamento de PII" |

Evidência que provaria o funcionamento: casos de teste acima (ativação e quase-acertos) e uso real. Nenhum foi executado ainda; não há afirmação de ganho medido.

Adaptações comuns: remoção de persona e "memória" fictícia, de estatísticas e benchmarks sem fonte, de pesos numéricos fixos e de dependências de plataforma; inclusão de limites éticos e de autorização para contato externo; roteamento explícito para owners vizinhos. No caso de privacidade, o original usava GDPR/CCPA e artigos europeus; a nova skill exige verificar o texto vigente da LGPD e da ANPD antes de citar obrigação ou prazo.

## Candidatas sem ação e por quê (lidas)

- `marketing-ai-citation-strategist`, `marketing-aeo-foundations`, `marketing-agentic-search-optimizer`: já cobertas pela seção "Auditoria AEO e citações em mecanismos de resposta" e por "AI visibility" em `seo-research-audit`.
- `academic-statistician`: `experiment-design` já exige pré-especificação e proíbe inventar poder e MDE. Interpretação de efeito com intervalo e comparações múltiplas ficam como referência externa para futura absorção.
- `design-persona-walkthrough`: o teste de cinco segundos e o LIFT são úteis, mas o perfil psicológico de persona (estilo de apego) contraria o princípio de não psicologizar; a simulação é hipótese, não evidência.
- `engineering-incident-response-commander`: sem demanda atual; `after-action-review` cobre o pós-incidente.
- `sales-outbound-strategist` e `sales-outreach`: sequências em escala exigem base legal (LGPD) e autorização por envio; alegações de conversão sem fonte.
- `sales-proposal-strategist`: servem para RFP; baixo ajuste ao fluxo atual.
- `support-executive-summary-generator`: SCQA e pirâmide já cabem em `explanation-architecture`; limite fixo de palavras é arbitrário.
- `zk-steward`: regras de persona (chamar pelo nome, declarar especialista) conflitam com as convenções do Arsenal.
- `accounts-payable-agent`: execução autônoma de pagamentos, rejeitada por governança de ações.
- Agentes de finanças do repositório: orientados a GAAP, IRS e TRID dos EUA e redundantes com `accounting-financial-statements`, `tax-financial-modeling`, `investment-portfolio-analysis` e `financial-planning-analysis`.

## Limites reais

- Só 16 dos 277 agentes foram lidos de forma extensa; 5 por cabeçalhos; os demais por descrição. Ver "Nível de evidência".
- As seis skills novas são texto instrucional não testado em conversas reais e não passaram por `skill-security-review` formal (não têm scripts nem rede).
- A equivalência com skills instaladas no Claude foi checada só por nome e descrição em 2026-10-28.
- Skills instaláveis no Claude dependem de upload manual pelo usuário; nada foi instalado na conta.

## Matriz de decisão por agente

Classes: A útil e muda comportamento; B boa metodologia; C prompt sofisticado com pouco ganho; D depende de runtime, plataforma ou integração.

### academic (6)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `academic-anthropologist` | C | REJECT | persona de domínio sem workflow reutilizável |
| `academic-geographer` | C | REJECT | persona de domínio sem workflow reutilizável |
| `academic-historian` | C | REJECT | persona de domínio sem workflow reutilizável |
| `academic-narratologist` | C | REJECT | coberto por `narrative-dialogue-engineering` |
| `academic-psychologist` | C | REJECT | persona de domínio sem workflow reutilizável |
| `academic-statistician` | B | KEEP_EXTERNAL_REFERENCE | `experiment-design` já cobre poder, MDE e pré-especificação; manter como referência para interpretação de efeito e intervalo |

### design (10)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `design-brand-guardian` | C | REJECT | coberto por `brand-strategy` e `brand-guidelines-authoring` |
| `design-image-prompt-engineer` | C | REJECT | coberto por `high-fidelity-image-generation` e `directional-prompting` |
| `design-inclusive-visuals-specialist` | B | KEEP_EXTERNAL_REFERENCE | viés e representação em imagens geradas não têm owner; referência para futura absorção |
| `design-persona-walkthrough` | B | KEEP_EXTERNAL_REFERENCE | lido por inteiro: teste de cinco segundos e LIFT são úteis, mas o perfil psicológico de persona (apego etc.) contraria o princípio de não psicologizar; simulação é hipótese, não evidência |
| `design-ui-designer` | C | REJECT | coberto por `design-system-governance`, `ui-ux-catalog` e `web-design-engineer` |
| `design-ui-finish-gate-reviewer` | C | REJECT | coberto por `design-principles-audit` e `web-quality-audit` |
| `design-ux-architect` | C | REJECT | coberto por `web-design-engineer` e `modern-css-practices` |
| `design-ux-researcher` | C | REJECT | coberto por `customer-interview` e `discovery-research-synthesis` |
| `design-visual-storyteller` | C | REJECT | coberto por `visual-explanation-sketch` e `explanation-architecture` |
| `design-whimsy-injector` | C | REJECT | coberto por `interaction-polish` e `ui-motion-design` |

### engineering (66)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `engineering-ai-data-remediation-engineer` | B | KEEP_EXTERNAL_REFERENCE | sem owner de limpeza de dados com SLM local; `crm-data-quality` cobre só CRM |
| `engineering-ai-engineer` | C | REJECT | coberto por `ml-production-engineering` |
| `engineering-api-platform-engineer` | C | REJECT | coberto por `developer-platform-engineering` |
| `engineering-ats-validator-architect` | D | REJECT | coberto em parte por `job-application-workflow`; referência a regulações dos EUA |
| `engineering-autonomous-optimization-architect` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-backend-architect` | C | REJECT | coberto por `system-design-engineering` |
| `engineering-china-network-engineer` | D | REJECT | jurisdição e fornecedores chineses; sem uso |
| `engineering-cms-developer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-code-reviewer` | C | REJECT | coberto por `code-review` |
| `engineering-codebase-onboarding-engineer` | C | REJECT | coberto por `code-understanding-audit` |
| `engineering-data-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-data-visualization-engineer` | C | REJECT | coberto por `dashboard-design` e `publication-figure-engineering` |
| `engineering-database-optimizer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-database-reliability-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-desktop-app-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-developer-tooling-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-devops-automator` | C | REJECT | coberto por `release-engineering` e `progressive-delivery-verification` |
| `engineering-drupal-performance` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-drupal-shopping-cart` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-electrical-engineer` | D | KEEP_EXTERNAL_REFERENCE | engenharia elétrica de sites de telecom; fora do uso atual |
| `engineering-email-intelligence-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-embedded-firmware-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-feishu-integration-developer` | D | REJECT | plataforma Feishu/Lark sem uso |
| `engineering-filament-optimization-specialist` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-finops-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-frontend-developer` | C | REJECT | coberto por `web-design-engineer` e `react-next-performance` |
| `engineering-gaussdb-expert` | D | REJECT | banco Huawei GaussDB sem uso |
| `engineering-git-workflow-master` | C | REJECT | coberto por `git-worktree-lifecycle` e `merge-conflict-resolution` |
| `engineering-i18n-engineer` | C | REJECT | coberto por `locale-adapter` |
| `engineering-identity-access-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-incident-response-commander` | B | KEEP_EXTERNAL_REFERENCE | lido: severidade, papéis e cadência de comunicação em incidente não têm owner; `after-action-review` cobre só o pós-incidente. Sem demanda atual; revisar se houver serviço em produção |
| `engineering-iot-fleet-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-it-service-manager` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-knowledge-graph-engineer` | C | REJECT | coberto por `graph-engineering` |
| `engineering-llm-post-training-engineer` | C | REJECT | coberto por `ml-production-engineering` |
| `engineering-minimal-change-engineer` | B | KEEP_EXTERNAL_REFERENCE | princípio de diff mínimo é útil; já alinhado a `surgical-engineering`, que é o owner provável |
| `engineering-mobile-app-builder` | C | REJECT | coberto por `crossplatform-mobile-engineering` e `swiftui-modern-ui` |
| `engineering-mobile-release-engineer` | C | REJECT | coberto por `release-engineering` |
| `engineering-multi-agent-systems-architect` | C | REJECT | coberto por `multi-agent-orchestration` |
| `engineering-network-engineer` | D | KEEP_EXTERNAL_REFERENCE | redes Cisco/Juniper/Palo Alto; fora do uso atual |
| `engineering-orgscript-engineer` | D | REJECT | depende de linguagem e parser próprios sem equivalente |
| `engineering-payments-billing-engineer` | C | REJECT | coberto por `payment-billing-operations` |
| `engineering-pdf-engine-architect` | D | KEEP_EXTERNAL_REFERENCE | compilação determinística HTML para PDF depende de runtime (Playwright); referência |
| `engineering-platform-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-privacy-engineer` | C | REJECT | coberto por `secure-code-privacy-review`; processo em `privacy-program-governance` |
| `engineering-prompt-engineer` | C | REJECT | coberto por `empirical-prompt-tuning` e `directional-prompting` |
| `engineering-rag-pipeline-engineer` | C | REJECT | coberto por `retrieval-quality-engineering` |
| `engineering-rapid-prototyper` | C | REJECT | coberto por `python-interactive-prototyping` e `functional-web-app-builder` |
| `engineering-realtime-collaboration-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-rust-refactoring-specialist` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-search-relevance-engineer` | C | REJECT | coberto por `retrieval-quality-engineering` |
| `engineering-section-508-specialist` | D | REJECT | norma federal dos EUA; acessibilidade geral coberta por `web-quality-audit` |
| `engineering-senior-developer` | C | REJECT | persona de stack específica (Laravel/Livewire) |
| `engineering-servicenow-developer-mentor` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-software-architect` | C | REJECT | coberto por `system-design-engineering` e `domain-modeling` |
| `engineering-solidity-smart-contract-engineer` | D | KEEP_EXTERNAL_REFERENCE | sem owner de contratos EVM; fora do uso atual (`onchain-token-due-diligence` é de análise) |
| `engineering-sre` | C | REJECT | coberto por `software-observability-engineering` e `resilience-engineering` |
| `engineering-technical-writer` | C | REJECT | coberto por `repository-evidence-docs` e `writing-quality` |
| `engineering-universal-document-compiler` | D | KEEP_EXTERNAL_REFERENCE | depende de pipeline próprio de AST de documentos; referência |
| `engineering-uswds-developer` | D | REJECT | design system do governo dos EUA |
| `engineering-video-streaming-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-voice-ai-integration-engineer` | C | REJECT | coberto por `realtime-voice-agent-engineering` |
| `engineering-webassembly-engineer` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-wechat-mini-program-developer` | D | REJECT | plataforma WeChat sem uso |
| `engineering-wordpress-performance` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |
| `engineering-wordpress-shopping-cart` | B | KEEP_EXTERNAL_REFERENCE | domínio de engenharia sem owner dedicado; fora do uso atual |

### finance (3)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `finance-bookkeeper-controller` | C | REJECT | coberto por `accounting-financial-statements`; foco em GAAP dos EUA |
| `finance-investment-researcher` | C | REJECT | coberto por `investment-portfolio-analysis`, `value-investing-company-analysis` e `financial-filings-analysis` |
| `finance-tax-strategist` | C | REJECT | coberto por `tax-financial-modeling`; jurisdição EUA/multinacional, sem base brasileira |

### game-development (21)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `blender-addon-engineer` | B | KEEP_EXTERNAL_REFERENCE | sem owner de add-ons Blender; `procedural-3d-reconstruction` cobre outra face |
| `economy-designer` | B | KEEP_EXTERNAL_REFERENCE | economia virtual sem owner; parcial em `game-matchmaking-social-engineering` |
| `game-audio-engineer` | C | REJECT | coberto pelos owners `game-*-engineering` e stack `game-development-cycle` |
| `game-designer` | C | REJECT | coberto pelos owners `game-*-engineering` e stack `game-development-cycle` |
| `godot-gameplay-scripter` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |
| `godot-multiplayer-engineer` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |
| `godot-shader-developer` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |
| `level-designer` | C | REJECT | coberto pelos owners `game-*-engineering` e stack `game-development-cycle` |
| `narrative-designer` | C | REJECT | coberto pelos owners `game-*-engineering` e stack `game-development-cycle` |
| `roblox-avatar-creator` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |
| `roblox-experience-designer` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |
| `roblox-systems-scripter` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |
| `technical-artist` | C | REJECT | coberto pelos owners `game-*-engineering` e stack `game-development-cycle` |
| `unity-architect` | C | REJECT | coberto por `unity-game-engineering` |
| `unity-editor-tool-developer` | C | REJECT | coberto por `unity-game-engineering` |
| `unity-multiplayer-engineer` | C | REJECT | coberto por `unity-game-engineering` |
| `unity-shader-graph-artist` | C | REJECT | coberto por `unity-game-engineering` |
| `unreal-multiplayer-architect` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |
| `unreal-systems-engineer` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |
| `unreal-technical-artist` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |
| `unreal-world-builder` | B | KEEP_EXTERNAL_REFERENCE | engine sem owner próprio; `game-development-engineering` cobre o geral |

### gis (13)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `gis-3d-scene-developer` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-analyst` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-bim-specialist` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-cartography-designer` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-drone-reality-mapping` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-geoai-ml-engineer` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-geoprocessing-specialist` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-qa-engineer` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-solution-engineer` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-spatial-data-engineer` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-spatial-data-scientist` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-technical-consultant` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |
| `gis-web-gis-developer` | B | KEEP_EXTERNAL_REFERENCE | GIS sem owner; fora do uso atual |

### healthcare (3)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `healthcare-clinical-evidence-agent` | B | KEEP_EXTERNAL_REFERENCE | saúde: exige adaptação ao contexto brasileiro; evidência clínica não substitui profissional |
| `healthcare-innovation-strategist` | B | KEEP_EXTERNAL_REFERENCE | saúde: exige adaptação ao contexto brasileiro; evidência clínica não substitui profissional |
| `healthcare-sovereign-health-systems-agent` | D | REJECT | sistemas de saúde governamentais fora do Brasil |

### marketing (37)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `marketing-aeo-foundations` | C | REJECT | coberto pela seção AEO de `seo-research-audit` |
| `marketing-agentic-search-optimizer` | C | REJECT | coberto por `seo-research-audit` (visibilidade em respostas de IA) |
| `marketing-ai-citation-strategist` | C | REJECT | lido: coberto pela seção "Auditoria AEO e citações" de `seo-research-audit` |
| `marketing-app-store-optimizer` | B | KEEP_EXTERNAL_REFERENCE | ASO sem owner; fora do uso atual |
| `marketing-baidu-seo-specialist` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-bilibili-content-strategist` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-book-co-author` | B | KEEP_EXTERNAL_REFERENCE | colaboração em livro de autoridade; parcial com `illustrated-ebook-production` |
| `marketing-carousel-growth-engine` | D | REJECT | publicação autônoma; `social-carousel-engineering` cobre a construção |
| `marketing-china-ecommerce-operator` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-china-market-localization-strategist` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-content-creator` | C | REJECT | coberto por stack `content-production` e `content-matrix` |
| `marketing-cross-border-ecommerce` | B | KEEP_EXTERNAL_REFERENCE | comércio exterior; fora do uso atual |
| `marketing-developer-community-builder` | B | KEEP_EXTERNAL_REFERENCE | comunidade de desenvolvedores; fora do uso atual |
| `marketing-douyin-strategist` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-email-strategist` | C | REJECT | coberto por `email-campaign-engineering` |
| `marketing-global-podcast-strategist` | B | KEEP_EXTERNAL_REFERENCE | podcast sem owner; fora do uso atual |
| `marketing-growth-hacker` | C | REJECT | coberto por `experiment-design` e stack `social-growth-engine` |
| `marketing-instagram-curator` | C | REJECT | coberto por `instagram-growth-diagnostics` e `social-post-review` |
| `marketing-kuaishou-strategist` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-linkedin-content-creator` | C | REJECT | coberto por `linkedin-profile-optimizer`, `content-matrix` e `social-post-review` |
| `marketing-livestream-commerce-coach` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-multi-platform-publisher` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-podcast-strategist` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-pr-communications-manager` | B | KEEP_EXTERNAL_REFERENCE | lido: assessoria de imprensa e crise sem owner; fora do uso atual |
| `marketing-private-domain-operator` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-reddit-community-builder` | B | KEEP_EXTERNAL_REFERENCE | comunidade em Reddit; fora do uso atual |
| `marketing-seo-specialist` | C | REJECT | coberto por `seo-research-audit` |
| `marketing-short-video-editing-coach` | C | REJECT | coberto por `video-editing-pipeline` e `short-form-video-engineering` |
| `marketing-social-media-strategist` | C | REJECT | coberto por stack `social-growth-engine` |
| `marketing-tiktok-strategist` | C | REJECT | coberto por stack `social-growth-engine` |
| `marketing-twitter-engager` | C | REJECT | coberto por stack `social-growth-engine` |
| `marketing-video-optimization-specialist` | B | KEEP_EXTERNAL_REFERENCE | otimização de YouTube sem owner; parcial em `short-form-video-engineering` |
| `marketing-wechat-official-account` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-weibo-strategist` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-x-twitter-intelligence-analyst` | D | KEEP_EXTERNAL_REFERENCE | depende de acesso a dados do X; parcial com `signal-intelligence-digest` |
| `marketing-xiaohongshu-specialist` | D | REJECT | plataforma ou mercado chinês sem uso |
| `marketing-zhihu-strategist` | D | REJECT | plataforma ou mercado chinês sem uso |

### paid-media (7)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `paid-media-auditor` | C | REJECT | coberto por `paid-media-operations` |
| `paid-media-creative-strategist` | C | REJECT | coberto por `paid-media-operations` |
| `paid-media-paid-social-strategist` | C | REJECT | coberto por `paid-media-operations` |
| `paid-media-ppc-strategist` | C | REJECT | coberto por `paid-media-operations` |
| `paid-media-programmatic-buyer` | C | REJECT | coberto por `paid-media-operations` |
| `paid-media-search-query-analyst` | C | REJECT | coberto por `paid-media-operations` |
| `paid-media-tracking-specialist` | C | REJECT | coberto por `paid-media-operations` |

### product (6)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `product-behavioral-nudge-engine` | B | KEEP_EXTERNAL_REFERENCE | nudges comportamentais têm risco de manipulação; sem owner, exigiria guardrails éticos antes de adotar |
| `product-dx-engineer` | C | REJECT | coberto por `developer-platform-engineering` |
| `product-feedback-synthesizer` | C | REJECT | coberto por `discovery-research-synthesis` |
| `product-manager` | C | REJECT | coberto por stack `product-management-cycle` |
| `product-sprint-prioritizer` | C | REJECT | coberto por `prioritization-engine` |
| `product-trend-researcher` | C | REJECT | coberto por `strategic-landscape-mapping` e `research-and-synthesize` |

### project-management (7)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `project-management-experiment-tracker` | C | REJECT | coberto por `experiment-design` |
| `project-management-jira-workflow-steward` | D | KEEP_EXTERNAL_REFERENCE | depende de Jira; sem conector atual |
| `project-management-meeting-notes-specialist` | C | REJECT | coberto por `meeting-knowledge-capture` e stack `meeting-to-actions` |
| `project-management-project-shepherd` | C | REJECT | coberto por `project-planning` e `project-health-review` |
| `project-management-studio-operations` | C | REJECT | coberto por `process-mapping-improvement` e `work-delivery-flow` |
| `project-management-studio-producer` | C | REJECT | coberto por `project-planning` e `project-complexity-management` |
| `project-manager-senior` | C | REJECT | coberto por `to-spec`, `to-tickets` e `project-planning` |

### research (1)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `research-synthesist` | C | REJECT | coberto por `research-and-synthesize` e `evidence-claim-verification` |

### sales (6)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `sales-account-strategist` | B | REJECT | método pós-venda absorvido em `customer-success-lifecycle`; sem skill própria |
| `sales-engineer` | B | KEEP_EXTERNAL_REFERENCE | pré-venda técnica B2B; fora do fluxo atual |
| `sales-offer-lead-gen-strategist` | C | REJECT | coberto por `go-to-market-strategy` |
| `sales-outbound-strategist` | B | KEEP_EXTERNAL_REFERENCE | lido: prospecção por sinais é útil, mas sequências em escala exigem base legal (LGPD) e autorização de envio; `first-customer-research` cobre a pesquisa. Alegações de conversão sem fonte |
| `sales-pipeline-analyst` | A | CREATE_NEW | `sales-pipeline-diagnostics` |
| `sales-proposal-strategist` | B | KEEP_EXTERNAL_REFERENCE | lido: temas de vitória e narrativa em três atos servem para RFP; baixo ajuste ao fluxo atual |

### security (12)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `security-ai-generated-code-auditor` | C | REJECT | coberto por `web-application-security-audit` e a skill `vibe-security` do Claude |
| `security-appsec-engineer` | C | REJECT | coberto por `secure-code-privacy-review` |
| `security-architect` | B | KEEP_EXTERNAL_REFERENCE | modelagem de ameaças sem owner dedicado; `web-application-security-audit` cobre aplicações web |
| `security-blockchain-security-auditor` | D | KEEP_EXTERNAL_REFERENCE | auditoria de contratos inteligentes; fora do uso atual |
| `security-cloud-security-architect` | B | KEEP_EXTERNAL_REFERENCE | sem owner de segurança em nuvem; fora do uso atual |
| `security-compliance-auditor` | C | REJECT | coberto por `saas-compliance-evidence` |
| `security-incident-responder` | B | KEEP_EXTERNAL_REFERENCE | DFIR sem owner; fora do uso atual |
| `security-penetration-tester` | D | KEEP_EXTERNAL_REFERENCE | ofensivo; só sob autorização formal e escopo; fora do uso atual |
| `security-secrets-credential-engineer` | B | KEEP_EXTERNAL_REFERENCE | ciclo de vida de segredos sem owner dedicado; parcial em `secure-code-privacy-review` |
| `security-senior-secops` | C | REJECT | coberto por `secure-code-privacy-review` |
| `security-threat-detection-engineer` | D | KEEP_EXTERNAL_REFERENCE | depende de SIEM |
| `security-threat-intelligence-analyst` | D | KEEP_EXTERNAL_REFERENCE | depende de fontes de inteligência de ameaças |

### spatial-computing (6)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `macos-spatial-metal-engineer` | D | KEEP_EXTERNAL_REFERENCE | Swift e Metal nativos; fora do uso atual |
| `terminal-integration-specialist` | D | KEEP_EXTERNAL_REFERENCE | SwiftTerm; nicho |
| `visionos-spatial-engineer` | D | KEEP_EXTERNAL_REFERENCE | visionOS; fora do uso atual |
| `xr-cockpit-interaction-specialist` | C | REJECT | coberto por `xr-game-engineering`; arquivo curto sem workflow |
| `xr-immersive-developer` | C | REJECT | coberto por `xr-game-engineering` |
| `xr-interface-architect` | C | REJECT | coberto por `xr-game-engineering` |

### specialized (58)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `accounts-payable-agent` | D | REJECT | executa pagamentos de forma autônoma, contra `agent-action-governance` e a proibição de movimentar dinheiro sem aprovação |
| `agentic-identity-trust` | B | KEEP_EXTERNAL_REFERENCE | identidade e confiança entre agentes; cobertura parcial em `agent-action-governance` |
| `agents-orchestrator` | C | REJECT | coberto por `multi-agent-orchestration` |
| `automation-governance-architect` | C | REJECT | coberto por `ai-workflow-automation-engineering` e `agent-action-governance` |
| `business-strategist` | C | REJECT | coberto por `strategic-landscape-mapping`, `go-to-market-strategy` e `decision-analysis` |
| `change-management-consultant` | A | CREATE_NEW | `change-adoption-management` |
| `chief-financial-officer` | C | REJECT | coberto por `corporate-treasury-management` e stack `financial-analysis-cycle` |
| `corporate-training-designer` | A | CREATE_NEW | `training-program-design` |
| `customer-service` | C | REJECT | coberto por `support-operations-engineering` |
| `customer-success-manager` | A/B | CREATE_NEW | `customer-success-lifecycle` |
| `data-consolidation-agent` | C | REJECT | coberto por `document-extraction-pipeline` e `dashboard-design` |
| `data-privacy-officer` | A/B | CREATE_NEW | `privacy-program-governance` (ancorada em LGPD, não em GDPR/CCPA) |
| `esg-sustainability-officer` | B | KEEP_EXTERNAL_REFERENCE | sem owner de ESG; fora do uso atual |
| `government-digital-presales-consultant` | D | REJECT | mercado governamental chinês |
| `grant-writer` | B | KEEP_EXTERNAL_REFERENCE | sem owner de captação de recursos; fora do uso atual |
| `healthcare-aging-parent-care-companion` | D | REJECT | contexto de saúde e HIPAA dos EUA; risco de conselho clínico |
| `healthcare-customer-service` | D | REJECT | contexto HIPAA dos EUA |
| `healthcare-marketing-compliance` | D | REJECT | legislação publicitária médica da China |
| `hospitality-guest-services` | B | KEEP_EXTERNAL_REFERENCE | vertical de hotelaria; fora do uso atual |
| `hr-onboarding` | B | KEEP_EXTERNAL_REFERENCE | sem owner de onboarding de pessoas; fora do uso atual (`training-program-design` cobre o lado de treinamento) |
| `identity-graph-operator` | D | KEEP_EXTERNAL_REFERENCE | depende de um grafo de identidade compartilhado entre agentes |
| `language-translator` | C | REJECT | coberto por `locale-adapter` |
| `legal-billing-time-tracking` | D | REJECT | práticas e regras dos EUA (IOLTA) |
| `legal-client-intake` | B | KEEP_EXTERNAL_REFERENCE | vertical jurídica; exigiria adaptação ao Brasil |
| `legal-document-review` | B | KEEP_EXTERNAL_REFERENCE | vertical jurídica; parecer exige advogado |
| `loan-officer-assistant` | D | REJECT | crédito hipotecário dos EUA (TRID) |
| `lsp-index-engineer` | D | KEEP_EXTERNAL_REFERENCE | depende de servidores LSP e runtime próprio |
| `ma-integration-manager` | B | KEEP_EXTERNAL_REFERENCE | sem owner de integração pós-fusão; fora do uso atual |
| `medical-billing-coding-specialist` | D | REJECT | codificação médica dos EUA (ICD-10-CM/CPT) |
| `operations-manager` | A/B | CREATE_NEW | `process-mapping-improvement` |
| `organizational-psychologist` | C | REJECT | `team-health-management` evita psicologizar pessoas; a persona contraria essa regra |
| `personal-growth-mentor` | C | REJECT | coberto por `coaching-development-loop` |
| `real-estate-buyer-seller` | B | KEEP_EXTERNAL_REFERENCE | parcial com `real-estate-investment-analysis`; processo de transação não coberto |
| `recruitment-specialist` | D | REJECT | plataformas de recrutamento chinesas |
| `report-distribution-agent` | D | REJECT | envio automático de relatórios; exige autorização por envio |
| `resume-tailor` | C | REJECT | coberto por `job-application-workflow` |
| `retail-customer-returns` | B | KEEP_EXTERNAL_REFERENCE | vertical de varejo; fora do uso atual |
| `sales-data-extraction-agent` | C | REJECT | coberto por `document-extraction-pipeline` |
| `sales-outreach` | B | KEEP_EXTERNAL_REFERENCE | ver `sales-outbound-strategist`; mesmos limites de LGPD e autorização |
| `specialized-civil-engineer` | C | REJECT | coberto por `structural-analysis-modeling` |
| `specialized-codebase-archaeologist` | C | REJECT | coberto por `code-understanding-audit` |
| `specialized-cultural-intelligence-strategist` | B | KEEP_EXTERNAL_REFERENCE | revisão de exclusão cultural em software; sem owner |
| `specialized-developer-advocate` | B | KEEP_EXTERNAL_REFERENCE | sem owner de advocacy; fora do uso atual |
| `specialized-document-generator` | C | REJECT | coberto pelas skills docx, pdf, pptx e xlsx do Claude |
| `specialized-fedramp-rmf-compliance` | D | REJECT | conformidade federal dos EUA |
| `specialized-focus-music-architect` | C | REJECT | coberto por `music-generation-engineering` |
| `specialized-french-consulting-market` | D | REJECT | mercado francês de consultoria |
| `specialized-korean-business-navigator` | D | REJECT | cultura de negócios coreana |
| `specialized-master-plan-architect` | C | REJECT | coberto por `to-spec` e `project-planning` |
| `specialized-mcp-builder` | B | KEEP_EXTERNAL_REFERENCE | sem owner de construção de servidores MCP; `mcp-agent-behavior-testing` só testa |
| `specialized-model-qa` | C | REJECT | coberto por `ml-production-engineering` e `llm-observability-evaluation` |
| `specialized-pricing-analyst` | B | KEEP_EXTERNAL_REFERENCE | lido: custo, margem e sensibilidade; `saas-pricing-monetization` cobre o caso de SaaS. Referência para preço de serviços |
| `specialized-salesforce-architect` | D | KEEP_EXTERNAL_REFERENCE | depende de Salesforce; sem conector atual |
| `specialized-strategy-duel-agent` | C | REJECT | jogo de simulação sem ganho de método |
| `specialized-workflow-architect` | B | KEEP_EXTERNAL_REFERENCE | mapeamento de árvores de fluxo; parcial com `durable-workflow-engineering` e `graph-engineering` |
| `study-abroad-advisor` | B | KEEP_EXTERNAL_REFERENCE | vertical de educação; fora do uso atual |
| `supply-chain-strategist` | B | KEEP_EXTERNAL_REFERENCE | sem owner de cadeia de suprimentos; fora do uso atual |
| `zk-steward` | C | REJECT | lido: regras de persona (chamar pelo nome, declarar especialista) conflitam com as convenções do Arsenal; `obsidian-vault-authoring` cobre o vault |

### support (6)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `support-analytics-reporter` | C | REJECT | coberto por `dashboard-design` e stack `business-decision-intelligence` |
| `support-executive-summary-generator` | C | REJECT | SCQA e pirâmide já cabem em `explanation-architecture` e `writing-quality`; limite fixo de palavras é arbitrário |
| `support-finance-tracker` | C | REJECT | coberto por `financial-planning-analysis` e `personal-financial-planning` |
| `support-infrastructure-maintainer` | C | REJECT | coberto por `software-observability-engineering` |
| `support-legal-compliance-checker` | B | KEEP_EXTERNAL_REFERENCE | revisão de conformidade ampla; jurisdição EUA, exigiria adaptação ao Brasil |
| `support-support-responder` | C | REJECT | coberto por `support-operations-engineering` |

### testing (9)

| Agente | Classe | Decisão | Owner ou motivo |
|---|---|---|---|
| `testing-accessibility-auditor` | C | REJECT | coberto por `web-quality-audit` e `runtime-ui-verification` |
| `testing-api-tester` | C | REJECT | coberto por `software-testing-engineering` |
| `testing-evidence-collector` | C | REJECT | coberto por `runtime-ui-verification` |
| `testing-performance-benchmarker` | C | REJECT | coberto por `software-testing-engineering` e `response-latency-optimization` |
| `testing-reality-checker` | C | REJECT | coberto por `verify-before-claim` |
| `testing-test-automation-engineer` | C | REJECT | coberto por `software-testing-engineering` |
| `testing-test-results-analyzer` | C | REJECT | coberto por `software-testing-engineering` |
| `testing-tool-evaluator` | C | REJECT | coberto por `agent-choice-audit` e `decision-analysis` |
| `testing-workflow-optimizer` | C | REJECT | coberto por `process-mapping-improvement` |
