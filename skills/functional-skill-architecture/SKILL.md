---
name: functional-skill-architecture
description: Modularizar skills complexas como pipelines de funções com contratos explícitos de entrada e saída, referências compartilhadas, scripts determinísticos, traces e casos de regressão quando a complexidade justificar essa estrutura.
---

# Functional Skill Architecture

## Objetivo
Tornar skills grandes e evolutivas mais fáceis de manter, observar e testar sem transformar skills simples em frameworks desnecessários.

## Quando usar
Use quando uma skill:
- acumulou muitas etapas, exceções e handoffs implícitos;
- contém parsing, formatação ou validação determinística misturados com julgamento;
- sofre regressões difíceis de localizar;
- precisa preservar comportamento durante uma migração estrutural;
- possui casos reais que deveriam virar testes de regressão.

Não use em skills pequenas e estáveis que já são legíveis.

## Modelo
Trate cada etapa significativa como uma função com:
- propósito;
- inputs explícitos;
- outputs explícitos;
- invariantes;
- dependências;
- critério de conclusão.

Mantenha:
- `SKILL.md` como orquestração do pipeline;
- regras e vocabulário compartilhados em referências;
- lógica determinística em scripts quando houver runtime real;
- casos de comportamento em testcases/evals;
- traces somente quando houver benefício observável e política segura de dados.

## Workflow
1. Leia o pacote completo da skill atual, não apenas o `SKILL.md`.
2. Mapeie o comportamento existente que precisa ser preservado.
3. Identifique handoffs implícitos e incompatibilidades de I/O.
4. Proponha fronteiras funcionais que concentrem uma responsabilidade cada.
5. Normalize os contratos de entrada e saída entre as funções.
6. Extraia regras compartilhadas para uma única fonte.
7. Mova trabalho determinístico para scripts apenas quando isso trouxer confiabilidade real.
8. Converta falhas e execuções representativas em casos de regressão.
9. Valide funções isoladas e o pipeline completo.
10. Compare o resultado com o comportamento legado antes de concluir a migração.

## Guardrails
- Preserve comportamento antes de otimizar arquitetura.
- Não crie runtime, viewers, logs ou scripts se o ambiente não oferecer ganho real.
- Redija dados sensíveis antes de qualquer trace.
- Não duplique regras em múltiplas funções.
- Use esta arquitetura proporcionalmente à complexidade.

## Relação com outras skills
Complementa `skill-builder`, `project-skill-architecture`, `empirical-prompt-tuning` e `golden-path-capture`.

## Origem adaptada
Metodologia inspirada em `AGI-comming/functional-skill-creator`, removendo a exigência de runtime Node, viewers e scaffolding específico.
