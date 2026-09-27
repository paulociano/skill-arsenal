# OpenJev e revalidação do OpenMuse

Data: 2026-09-26. Método: `arsenal-autopilot` com comparação por capability, revisão documental conforme `skill-security-review` e verificação pós-escrita. Fontes canônicas consultadas no GitHub. Nenhum installer, modelo, script ou runtime externo foi executado.

## Resultado

| Fonte | Classe | Capability observada | Decisão |
| --- | --- | --- | --- |
| [SiliconLabAI/OpenJev](https://github.com/SiliconLabAI/OpenJev) | **D + B** | Playground para decisões tipadas com três backends: micro-scorers paralelos, chamada estruturada única e decision engine especializado; suporta choice, score e decisão binária/probabilística. | **UPDATE_EXISTING** em `model-routing-gateway`: registrar OpenJev como referência arquitetural e explicitar comparação entre modos de deployment. Não criar skill nova. |
| [CopilotKit/openmuse](https://github.com/CopilotKit/openmuse) | **D + B** | Agente pessoal com tarefas duráveis, browser/terminal/files, approvals, leases, receipts, recuperação e integrações Google. | **KEEP_EXTERNAL_REFERENCE**. Já avaliado em 2026-09-24 e os padrões incrementais já foram incorporados em `loop-engineering`. Nenhuma nova mudança necessária. |

## OpenJev

### O que faz de verdade

OpenJev recebe estado + perguntas tipadas e devolve respostas estruturadas. O README atual documenta três estratégias:

1. **parallel** — uma chamada pequena por opção, seguida de softmax;
2. **oneshot** — uma chamada JSON estruturada a modelo OpenAI-compatible;
3. **decider** — integração com Mapika/decider via endpoint `/v1/systemone`, com pesos especializados e calibração declarada pelo upstream.

O projeto é uma implementação técnica, não uma metodologia completa de decisão humana. Seu ganho depende do workload, modelo/checkpoint, idioma, cardinalidade de opções, calibração, latência e custo.

### Valor incremental para o Arsenal

O owner canônico já é `model-routing-gateway`, que cobre decision engines tipados, capability gates, calibração, fallback e observabilidade. OpenJev acrescenta uma referência concreta para comparar **micro-scoring paralelo vs structured oneshot vs engine especializado** sob o mesmo contrato de saída.

Não foi criada nova skill porque isso duplicaria ownership. `decision-analysis` continua responsável por decisões humanas complexas com critérios, incerteza e trade-offs; `model-routing-gateway` continua responsável pela arquitetura de execução/roteamento de modelos e decision engines.

### Segurança e portabilidade

**APPROVE** para a adaptação textual. **CAUTION** para adoção técnica do OpenJev/decider.

O README exige Node/npm e chave de modelo para os backends LLM. O backend decider exige runtime Python, download/execução de modelo e GPU CUDA no cenário documentado. URLs de backend e API keys são superfícies de configuração e envio de dados. Nenhuma dependência, installer, checkpoint ou serviço foi auditado em profundidade ou executado nesta avaliação.

Probabilidades retornadas não devem autorizar automaticamente ações consequenciais sem calibração e validação no domínio real. Benchmarks ou alegações de calibração do upstream não foram reproduzidos aqui.

## OpenMuse

OpenMuse já possui avaliação canônica em `evaluations/2026-09-24-openmuse-open-glean-unreal-zcode-bongocat-laya-mini-agi.md`. Desde então, a capability relevante continua com owner em `loop-engineering`: persistência antes de efeitos, deduplicação, leases, estados recuperáveis, approvals vinculados ao alvo/versão, receipts e tratamento de resultado externo incerto.

A releitura do README atual não justificou nova skill nem alteração adicional. O produto continua dependente de runtime próprio, CopilotKit, workers, credenciais e, para recursos live, integrações externas.

## Evidência e limites

Fontes lidas:
- [OpenJev README](https://github.com/SiliconLabAI/OpenJev/blob/main/README.md)
- [OpenMuse README](https://github.com/CopilotKit/openmuse/blob/main/README.md)
- `skills/model-routing-gateway/SKILL.md`
- `skills/decision-analysis/SKILL.md`
- `skills/loop-engineering/SKILL.md`
- avaliações canônicas anteriores de Jev e OpenMuse.

Esta foi uma revisão documental estática. Não houve benchmark, teste de precisão, medição de custo/latência, scanner de supply chain ou execução dos projetos. Portanto, a conclusão cobre somente valor metodológico e ownership dentro do Arsenal.
