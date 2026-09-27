# Avaliação de repositórios externos — lote 2026-09-27

## Escopo

Fontes avaliadas:
- xiaolai/insidebar-ai
- ZA1815/caniscrape
- kayba-ai/agentic-context-engine
- wangshy31/OneRec-Think
- xiongsiheng/DeepVerify
- anthropics/sandbox-runtime
- gokapso/whatsapp-cloud-inbox
- KartikLabhshetwar/quotick
- dovvnloading/Graphite
- CogitatorTech/infera
- tanin47/backdoor

Router usado: ARSENAL INDEX.md.
Stack: arsenal-autopilot.
Gate de segurança: skill-security-review, revisão estática sem executar installers ou código externo.

## Decisões

### kayba-ai/agentic-context-engine
Classificação: A/D.
Decisão: UPDATE_EXISTING.
Owner: loop-engineering.

Valor incremental:
- pipeline Execute → Evaluate → Reflect → Update → Deduplicate;
- aprendizagem só depois de avaliação;
- deduplicação de estratégias persistidas;
- separação entre experiência observada e estratégia promovida.

Adaptação:
- metodologia incorporada a loop-engineering;
- runtime Kayba/ACE, CLI e hosted service não foram importados;
- auto-update ficou condicionado a baseline, reversibilidade e approval.

### xiongsiheng/DeepVerify
Classificação: A/D.
Decisão: CREATE_NEW.
Owner criado: evidence-claim-verification.

Valor incremental:
- verificação em nível de claim;
- decomposição em subclaims;
- busca orientada por evidência discriminante;
- entailment graph leve;
- verdict proporcional;
- disciplina de whitelist de ferramentas.

Adaptação:
- sem dependência de Pixi, LangGraph, MCP server próprio, SERPAPI, Jina, LangSmith ou modelos treinados do projeto.

### anthropics/sandbox-runtime
Classificação: D.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- referência para isolamento de filesystem e network;
- fail-closed para configuração inválida;
- boundaries por processo.

Motivo:
- runtime específico;
- a política de segurança já pertence a skill-security-review;
- não presumir srt disponível no ambiente atual.

### ZA1815/caniscrape
Classificação: D.
Decisão: REJECT como skill; referência técnica opcional.

Valor:
- reconhecimento de WAF, CAPTCHA, rate limiting, fingerprinting e honeypots.

Motivo:
- foco técnico em recon e anti-bot;
- browser impersonation, proxy rotation e CAPTCHA solving não são metodologia que o Arsenal deva incorporar como padrão;
- web-extraction-pipeline deve continuar priorizando técnica mínima, respeito a controles e validação.

### gokapso/whatsapp-cloud-inbox
Classificação: D.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- inbox para WhatsApp Cloud API;
- templates, interactive buttons, media e janela de 24h.

Motivo:
- produto de integração/runtime dependente de Meta/Kapso;
- não acrescenta metodologia geral suficiente para skill independente;
- útil como referência em projeto real de inbox WhatsApp.

### dovvnloading/Graphite
Classificação: B/D.
Decisão: ABSORB_METHOD_ONLY, sem nova skill.

Valor:
- canvas visual com branching;
- nós especializados;
- persistência local;
- preview/approval antes de escrita.

Overlap:
- graph-engineering já cobre DAGs, branching, contracts, joins e recuperação;
- interactive-system-diagram cobre visualização explorável;
- multi-agent-orchestration cobre coordenação quando runtime real existe.

### CogitatorTech/infera
Classificação: D.
Decisão: KEEP_EXTERNAL_REFERENCE.

Valor:
- inferência ONNX dentro de DuckDB via SQL;
- reduz movimentação de dados em workflows analíticos.

Motivo:
- extensão técnica específica;
- útil em projetos DuckDB/ML, mas não muda o comportamento geral do ChatGPT;
- owner conceitual continua ml-production-engineering quando houver projeto real.

### tanin47/backdoor
Classificação: D.
Decisão: KEEP_EXTERNAL_REFERENCE com CAUTION.

Valor:
- ferramenta self-hosted de exploração e edição de bancos;
- masked users;
- suporte a PostgreSQL, ClickHouse e SQLite;
- possibilidade de SSH tunnel/VPN.

Risco:
- executa SQL arbitrário e operações destrutivas como drop/delete;
- credenciais e acesso a banco exigem permission boundary forte;
- qualquer uso futuro deve adotar least privilege, network restriction, audit logs e approval explícito para escrita.

Não virou skill porque é produto/runtime, não metodologia nova.

### KartikLabhshetwar/quotick
Classificação: D/C.
Decisão: REJECT como skill.

Motivo:
- utilitário específico para converter quotes em backticks em template literals;
- não cria capability reutilizável relevante para o Arsenal;
- melhor tratado como ferramenta/editor plugin quando necessário.

### xiaolai/insidebar-ai
Classificação: D.
Decisão: REJECT como skill; referência de produto.

Motivo:
- extensão de navegador para acesso lateral a AI;
- é interface/produto, não metodologia transferível;
- capacidades equivalentes dependem de browser/extension runtime e não justificam owner no Arsenal.

### wangshy31/OneRec-Think
Classificação: D/B.
Decisão: KEEP_EXTERNAL_REFERENCE, sem importação por enquanto.

Valor potencial:
- raciocínio deliberativo aplicado a recommendation systems;
- separação entre processo de pensamento/planejamento e ranking/recomendação.

Motivo:
- domínio especializado de recommender systems;
- o ganho para o Arsenal geral é estreito;
- caso surja demanda recorrente de recommendation-engineering, pode justificar skill própria ou extensão de ml-production-engineering.

## Mudanças publicadas

1. Criada `skills/evidence-claim-verification/SKILL.md`.
2. Atualizada `skills/loop-engineering/SKILL.md` com learning loop por experiência.
3. Atualizado `ARSENAL INDEX.md` com evidence-claim-verification.

## Segurança e portabilidade

Nenhum installer, setup script ou binário dos repositórios externos foi executado.
Dependências externas foram tratadas como indisponíveis até prova em runtime.
Ferramentas específicas de fornecedores não foram convertidas em capacidades fictícias do ChatGPT.

## Resumo de ownership

- DeepVerify → evidence-claim-verification.
- Agentic Context Engine → loop-engineering.
- Graphite → graph-engineering / interactive-system-diagram, sem novo owner.
- Infera → ml-production-engineering como referência técnica.
- sandbox-runtime → skill-security-review como referência de arquitetura.
- Caniscrape → web-extraction-pipeline apenas como referência negativa/limite, sem evasão.
- WhatsApp Cloud Inbox → referência de integração, sem skill.
- Backdoor → referência de tooling DB, sem skill.
- Quotick → descartado.
- Insidebar AI → descartado como skill.
- OneRec-Think → referência especializada.
