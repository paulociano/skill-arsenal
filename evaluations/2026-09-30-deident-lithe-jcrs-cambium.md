# Avaliação em lote — de-identification, IDE lightweight, compatibility oracle e repository governance

Data: 2026-09-30

## Escopo

Fontes:
- https://github.com/ikuV/deident-wasm
- https://github.com/1lck/Lithe-IDEA
- https://github.com/OlegSotnikov/jc-rs
- https://github.com/KimGLee/Cambium

Fluxo aplicado: `arsenal-autopilot`.

Nenhum installer, binário, script, daemon, MCP externo ou runtime das fontes foi executado.

## Resumo

| Fonte | Classe | Decisão | Owner |
| --- | --- | --- | --- |
| ikuV/deident-wasm | A/B/D | ABSORB_METHOD_ONLY | `secure-code-privacy-review` |
| 1lck/Lithe-IDEA | B/D | KEEP_EXTERNAL_REFERENCE | arquitetura de app/IDE; sem owner novo |
| OlegSotnikov/jc-rs | A/B/D | UPDATE_EXISTING | `behavior-contract-validation` |
| KimGLee/Cambium | A/B/D | UPDATE_EXISTING | `project-skill-architecture`, `verify-before-claim`, `handoff` |

## ikuV/deident-wasm

### O que faz
Motor de transformação de privacidade para datasets estruturados, com pseudonimização, anonimização por política, detectores em conteúdo, relatórios de risco, DICOM, vault reversível e sandbox WASM.

### Valor incremental
Forte metodologia para distinguir:
- pseudonimização reversível de anonimização com risco residual;
- identificadores diretos, quasi-identifiers, dados sensíveis e campos utilitários;
- política fail-closed para campos não classificados;
- detector por padrão textual versus detector com validação estrutural/checksum;
- heurística de revisão humana versus transformação automática;
- mapping vault como material sensível;
- k-anonymity como post-condition mensurável, não certificado universal de anonimato.

### Decisão
Absorver metodologia em `secure-code-privacy-review`. Não importar CLI, Rust, WASM, DICOM, crypto implementation ou claims de performance como capacidade nativa.

## 1lck/Lithe-IDEA

### O que faz
IDE leve para Java/Spring Boot, com Rust Core compartilhado entre macOS e Windows, serviços de linguagem sob demanda, diff review, debug, history e banco de dados.

### Valor incremental
Boas ideias arquiteturais:
- serviços pesados on-demand;
- shared deterministic core com UIs nativas distintas;
- contratos JSON/fixtures como fronteira cross-platform;
- revisão de diff como função de primeira classe para código gerado por IA.

### Decisão
Manter referência externa. Os princípios já cabem em `system-design-engineering`, `crossplatform-mobile-engineering` e `code-review`; não justificam skill nova.

## OlegSotnikov/jc-rs

### O que faz
Reimplementação Rust compatível com jc, com diferencial testado contra um oracle canônico e denominator explícito.

### Valor incremental
Excelente disciplina de compatibilidade:
- a implementação original é autoridade semântica;
- somente fixtures que o próprio oracle valida entram no denominador;
- exclusões permanecem visíveis por categoria;
- timezone/ambiente fazem parte do contrato quando alteram output;
- mirror de fixtures deve ser byte-faithful para impedir ajuste do esperado à implementação;
- CI pode bloquear drift apenas sobre o denominador realmente qualificado.

### Decisão
Absorver em `behavior-contract-validation` como padrão de differential/oracle validation. Não importar parser/runtime/benchmarks.

## KimGLee/Cambium

### O que faz
Padrão de governança para knowledge repositories mantidos por agentes, com kernel normativo, profile selecionado, ledgers de coverage/queue/progress, receipts, resume/recovery e tooling determinístico.

### Valor incremental
Forte metodologia de governança:
- separar norma canônica, perfil adotado, estado runtime e projeções derivadas;
- três ledgers com responsabilidades distintas em vez de uma task list ambígua;
- checar estado existente antes de iniciar nova tarefa;
- dry-run antes de writes e writers exclusivos por tipo de estado;
- evidence/receipt append-only e locks como recovery evidence;
- distinguir entrega de contexto de prova de leitura/entendimento pelo agente;
- agente prepara candidato, mas não infere decisão de domínio não confirmada;
- issue pública como owner do problema antes de implementação;
- integração compartilhada serial mesmo quando batches disjuntos podem trabalhar em paralelo.

### Decisão
Absorver metodologia apenas nos owners existentes. Não importar o kernel, scripts, MCP, profiles ou runtime inteiro como stack/skill separada nesta rodada.

## Segurança e portabilidade

- deident-wasm manipula PII, chaves, vaults e DICOM: uso real exige revisão de threat model, jurisdição e controles operacionais.
- Lithe inclui download/install/update e ferramentas de execução; nenhuma instalação foi executada.
- jc-rs é uma implementação técnica; claims de benchmark não foram reproduzidos.
- Cambium executa tools e mantém estado; não assumir locks, filesystem capabilities, identity ou protected runner fora de runtime real.

## Conclusão

O maior ganho metodológico deste lote está em três pontos:
1. de-identification com promessas e failure modes explícitos;
2. differential validation com oracle e denominator íntegro;
3. governança de trabalho agent-maintained com owners, ledgers, receipts e recovery boundaries.

Nenhuma nova skill foi criada.