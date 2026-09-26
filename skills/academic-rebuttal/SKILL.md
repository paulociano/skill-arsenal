---
name: academic-rebuttal
description: Estruturar rebuttals e author responses acadêmicos a partir de reviews, paper, código, regras confirmadas do venue, evidência rastreável, triagem de experimentos e cobertura completa das preocupações dos revisores.
---

# Academic Rebuttal

## Objetivo
Transformar reviews acadêmicos em uma resposta estratégica, factual e rastreável, sem inventar resultados, permissões do venue ou posições de revisores.

## Entradas
Quando disponíveis:
- paper ou manuscrito;
- reviews brutos;
- código e resultados;
- regras atuais do venue;
- limites de formato;
- experimentos já concluídos ou realmente viáveis.

## Workflow
1. **Intake**: mapear paper, reviews, código, regras e lacunas.
2. **Normalização**: preservar o texto original dos reviews e decompor em preocupações atômicas.
3. **Agrupamento**: identificar concerns recorrentes sem perder autoria ou contexto.
4. **Evidência**: ligar cada preocupação a paper, código, resultado, regra do venue ou input explícito do autor.
5. **Triagem de experimentos**: separar necessário, alto valor opcional, baixo valor e inviável; nunca assumir que experimento será executado.
6. **Estratégia**: definir resposta por concern, concessões legítimas, esclarecimentos, evidência e mudanças já realizadas.
7. **Cobertura**: garantir que cada concern foi respondido, explicitamente deferido ou marcado como dependente de input.
8. **Drafting**: escrever no formato confirmado pelo venue, preservando concisão e tom profissional.
9. **Stress test**: releia como reviewer/AC e procure claims frágeis, lacunas e excesso de promessa.
10. **Safety gate**: validar provenance, tom, anonimato, regras de formato e compromissos antes da versão final.

## Regras de evidência
- Diferencie fato do paper, resultado experimental, inferência e proposta futura.
- Números e claims experimentais precisam existir em fonte verificável.
- Regras de venue devem ser atuais e confirmadas pelo usuário quando houver incerteza.
- Não atribua intenção, má-fé ou incompetência a reviewers.
- Não prometa revisão futura como se já estivesse concluída.

## Artefatos úteis
Conforme a tarefa:
- concern ledger;
- matriz concern -> evidence -> response;
- plano de experimentos;
- draft por reviewer ou resposta unificada;
- coverage map;
- checklist final de venue, anonimato e provenance.

## Relação com outras skills
Use `academic-paper-orchestration` para trabalho no manuscrito e `research-and-synthesize` ou pesquisa web para regras atuais e evidência externa. Use `writing-quality` somente depois de a estratégia estar factual e completa.

## Origem adaptada
Metodologia inspirada em `xiongqi123123/awesome-rebuttal`, simplificada para o Arsenal e sem dependência de workspace local obrigatório, schemas próprios, Overleaf ou scripts específicos.
