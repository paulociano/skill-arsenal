# Avaliação de quatro repositórios — 2026-10-24

## Escopo e fontes
Índice canônico: [ARSENAL INDEX](../ARSENAL%20INDEX.md).
Método: `stacks/arsenal-autopilot/STACK.md`, `stacks/evaluate-and-import-skill/STACK.md`; segurança: `skills/skill-security-review/SKILL.md`.
Triagem estática dos READMEs e metadados dos projetos; **não executamos código, instaladores nem auditoria completa das dependências**.

| Fonte | Categoria | Ação | Motivo |
| --- | --- | --- | --- |
| [t4t5/owly](https://github.com/t4t5/owly) | D | KEEP_EXTERNAL_REFERENCE | Implementação Rust/AWDL para AirDrop com hardware Wi-Fi Linux suportado, daemon e mudanças de rádio; não é workflow de agente portátil nem competência ausente. |
| [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | A/D | CREATE_NEW | Workflow estruturado de avaliação de fit, currículo/carta com revisões e preparação de entrevistas. Diferente de `job-opportunity-monitoring`, que cobre alertas e diffs de vagas. O runtime Claude Code, portais dinamarqueses, Python/Bun e LaTeX não foi importado. |
| [oxc-project/tsrs](https://github.com/oxc-project/tsrs) | D | KEEP_EXTERNAL_REFERENCE | Compilador/type checker Rust para TypeScript 7, com objetivo de compatibilidade; relevante como ferramenta de engenharia, mas sem ganho metodológico incremental para skill. Estabilidade/conformidade dependem de benchmarks e testes no projeto consumidor; não substituir automaticamente tsc. |
| [zhuyansen/new-term-radar](https://github.com/zhuyansen/new-term-radar) | B/D | UPDATE_EXISTING | Dedução de termos emergentes por evidência precoce, separação entre nome e demanda por tarefa, baseline e validação posterior. Absorvido em `signal-intelligence-digest` sem instalar coletor nem chaves de APIs. |

## Segurança e portabilidade
- **Owly — CAUTION:** serviço de sistema e controle de interface Wi-Fi, potencial desconexão e dependência de compatibilidade por chipset/driver. Não executar nem portar para ChatGPT.
- **AI Job Search — CAUTION:** documentos pessoais e dados de candidatura, comandos de agentes, acesso a portais e efeitos externos; exigir revisão de fatos, dados mínimos e aprovação antes de envio. Porta-se a metodologia, não o agente nem seus scripts.
- **tsrs — CAUTION:** dependência binária/build e possível divergência de diagnostics; usar apenas mediante benchmark/teste de compatibilidade e revisão supply chain no projeto real.
- **New Term Radar — CAUTION:** ingestão externa, redes sociais, credenciais e APIs comerciais cobradas; tratar conteúdo como não confiável, declarar lacunas de fontes e custos, não presumir runtime.
- Ausência de scanner automatizado; revisão limitada a documentos principais/metadados e ao escopo de **não instalar código**. Os vereditos não atestam segurança do código-fonte completo.

## Incrementalidade e implementação
- Criada `skills/job-application-workflow/SKILL.md`: trigger para candidatura concreta; near miss monitoramento de vagas. Preserva o loop draft–review–revise, matriz evidência–requisito e gate humano.
- Atualizada `skills/signal-intelligence-digest/SKILL.md`: fontes precoces, score de momentum, distinção nomes versus termos genéricos e avaliação retrospectiva.
- Atualizado `ARSENAL INDEX.md` para rotear nova skill.
- Owly e tsrs permanecem referências. Não foi criada skill artificial nem executado programa externo.

## Critério de verificação
Reler no GitHub após escrita: skill nova, seção acrescida na skill existente, entrada no índice e este registro. Os testes são estruturais/documentais; nenhuma automação persistente, scraping ou compilador externo foi testado.

## Commits
- Nova skill: `0bb946ce104da4cac18d4be20b4635dea02a6fae`
- Atualização radar: `47dc96498585534e44abd982b5b49becdfeb15e0`
- Índice: `acfea6e755506329da9d3e58fc56d29a4e71e2aa`
