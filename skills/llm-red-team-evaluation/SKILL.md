---
name: llm-red-team-evaluation
description: "Avaliar adversarialmente aplicações GenAI com threat model, probes, detectores, cobertura, mitigação e reteste controlado."
---

# llm-red-team-evaluation

## Objetivo

Avaliar sistemas GenAI autorizados contra falhas adversariais de forma reproduzível, separando threat model, geração de ataques, detecção, evidência, mitigação e reteste.

## Quando usar

- red teaming de chatbot, agente, RAG ou workflow LLM;
- prompt injection e jailbreak resistance;
- data leakage e exfiltration paths;
- abuso de ferramentas ou code execution;
- avaliação de guardrails de input/output;
- regressão de segurança antes/depois de uma mudança.

Não usar para revisar se uma skill/plugin externa é segura para instalar. Para isso, usar `skill-security-review`.

## Princípio central

**Ataque bem-sucedido é evidência sobre uma superfície e configuração específicas, não prova universal sobre o modelo inteiro.**

## Workflow

1. **Authorize scope** — definir sistema, ambiente, contas, dados, ferramentas e ações permitidas.
2. **Threat model** — listar ativos, trust boundaries, capacidades do atacante e impactos relevantes.
3. **Attack taxonomy** — selecionar classes pertinentes, como prompt injection, jailbreak, leakage, unsafe tool use, insecure code suggestion, harmful content ou policy bypass.
4. **Baseline** — registrar comportamento seguro esperado e versão de modelo/prompt/workflow/guardrails.
5. **Probe set** — usar casos fixos + variações/adaptive probes; não depender de uma única string de ataque.
6. **Detectors/oracles** — separar regra determinística, policy classifier, human review e LLM judge.
7. **Execute bounded tests** — aplicar budgets, rate limits e stop conditions; nunca ampliar alvo silenciosamente.
8. **Record evidence** — input, context relevante, output/action, detector, severity, reproducibility e versão.
9. **Mitigate** — corrigir boundary, permission, prompt, retrieval, tool contract, sandbox ou guardrail conforme causa.
10. **Retest** — repetir casos originais e variantes próximas; verificar regressões funcionais.
11. **Report coverage** — declarar o que foi testado, o que ficou fora e quais riscos permanecem desconhecidos.

## Cobertura adversarial

Organizar testes por superfície, não apenas por prompt:

- **input** — instruções diretas, obfuscação, encoding, multilingual, multimodal;
- **retrieval** — documentos maliciosos, indirect injection, poisoned context;
- **tools** — argumentos perigosos, privilege expansion, stale state, confused deputy;
- **memory** — persistence poisoning e cross-session leakage;
- **output** — unsafe content, insecure code, secrets e structured-output escapes;
- **agent loop** — escalation por múltiplos passos, retries e subagents.

## Detectores e severidade

- detector deve medir o comportamento que realmente importa;
- múltiplos detectores podem discordar; registrar conflito em vez de esconder;
- LLM-as-judge não substitui checks determinísticos quando o resultado é verificável;
- severity depende de impacto + exploitability + permissions reais;
- jailbreak textual sem capacidade de causar efeito pode ter impacto diferente de tool abuse com escrita externa.

## Regressão e benchmarks

Manter um conjunto versionado de casos adversariais representativos. Após mitigação:

- rodar casos que falharam;
- rodar benign cases para detectar overblocking;
- preservar holdout quando houver otimização iterativa;
- comparar mesma versão de ambiente/modelo quando a finalidade for atribuir causalidade;
- não promover melhoria por média se um caso crítico regrediu.

## Segurança operacional

- testar apenas alvos e contas autorizados;
- usar dados sintéticos quando possível;
- não enviar secrets reais como payload de teste;
- evitar ações destrutivas, persistência ou gasto não necessário;
- ataques a ferramentas devem preferir sandbox/dry-run;
- tratar datasets adversariais como conteúdo não confiável.

## Ferramentas e dependências

Promptfoo, PyRIT, garak, Purple Llama/CyberSecEval ou ferramentas equivalentes podem acelerar execução quando já disponíveis e autorizadas. Não instalar nem executar automaticamente. A metodologia continua válida sem esses runtimes.

## Integração

Combina com `llm-observability-evaluation`, `skill-security-review`, `structured-output-contract`, `model-routing-gateway` e `verify-before-claim`.

## Referências

Metodologia adaptada de:
- https://github.com/promptfoo/promptfoo
- https://github.com/microsoft/PyRIT
- https://github.com/NVIDIA/garak
- https://github.com/meta-llama/PurpleLlama

Sem incorporar payloads de jailbreak como comportamento operacional e sem exigir os scanners/runtimes originais.
