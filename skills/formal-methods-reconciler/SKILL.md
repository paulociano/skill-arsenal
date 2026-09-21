---
name: formal-methods-reconciler
description: "Traduzir dúvidas críticas de correção de software em modelos mínimos verificáveis e interpretar provas ou contraexemplos."
---

# formal-methods-reconciler

## Objetivo

Transformar dúvidas críticas de correção de software em pequenos modelos verificáveis e traduzir counterexamples/provas de volta para decisões de domínio.

## Quando usar

Traduzir dúvidas críticas de correção de software em modelos mínimos verificáveis e interpretar provas ou contraexemplos.

## Workflow

1. Identificar fonte(s) de verdade: spec, docs, contratos, código, testes, config, logs.
2. Extrair claims antes de escolher ferramenta: permitido, proibido, alcançável, equivalente, sempre/eventualmente, invariantes.
3. Classificar problema: predicado, relação, transição de estado, protocolo, contrato sequencial, teorema ou protocolo de segurança.
4. Escolher o menor verificador apropriado: solver/model checker/proof assistant somente quando agregar valor.
5. Construir modelo mínimo e incluir sanity cases positivos + variante quebrada quando possível.
6. Usar resultado da ferramenta como juiz; o LLM propõe modelos e interpreta, não certifica a prova por conta própria.
7. Traduzir SAT/UNSAT/trace/proof failure para linguagem do domínio e criar regression guard ou pergunta para o dono da decisão.

## Executable reference como oracle

Quando um sistema possui várias implementações da mesma semântica, uma implementação pequena e legível pode servir como **reference oracle**:

- declarar qual artefato define o comportamento canônico;
- manter compiler/runtime/hardware/otimizações subordinados ao mesmo contrato;
- comparar resultados em fixtures comuns, idealmente bit-for-bit quando o domínio permitir;
- adicionar variante quebrada para provar que o conformance test detecta divergência;
- não confundir o modelo de referência com performance ou microarquitetura real;
- versionar mudanças semânticas no oracle e revalidar consumidores downstream.

Esse padrão é especialmente útil em compiladores, VMs, protocolos, formatos e hardware/software co-design.

## Condição

Só afirmar resultado formal como verificado quando o solver/verifier realmente foi executado e seu resultado está disponível. Conformance contra executable reference é evidência de equivalência no conjunto testado, não uma prova universal, salvo quando a ferramenta formal realmente estabelece isso.

## Referências

Adaptada de [mizchi/skills · formal-methods-reconciler](https://github.com/mizchi/skills/tree/main/formal-methods-reconciler).

Executable reference como source of truth inspirado em [penberg/titania](https://github.com/penberg/titania), sem importar runtime, modelo ou acesso de shell sem confirmação.

Origem local: [formal-methods-reconciler.docx](../formal-methods-reconciler.docx).
