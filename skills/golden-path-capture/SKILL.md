---
name: golden-path-capture
description: Capturar workflows difíceis já verificados como caminhos reutilizáveis, registrando condição de promoção, falhas descartadas, escopo e higiene de segredos antes de codificar o aprendizado como skill ou documentação.
---

# Golden Path Capture

## Objetivo
Transformar uma descoberta operacional ou técnica difícil, comprovada durante uma sessão, em conhecimento reutilizável sem cristalizar palpites, segredos ou detalhes one-off.

## Quando usar
Use após:
- debugging não trivial que exigiu várias tentativas;
- descoberta de sequência operacional não óbvia;
- workflow recorrente de deploy, migração, acesso, verificação ou recuperação;
- correção do usuário que alterou materialmente o caminho correto;
- pedido explícito para preservar um processo reutilizável.

## Regra de promoção
Promova para conhecimento durável apenas quando houver:
1. **verificação positiva**: teste, build, comando, repro ou checagem que prove o caminho;
2. **padrão de falha nomeado**: o problema que o caminho evita ou diagnostica;
3. **dead-end descartado**: pelo menos uma abordagem tentada e eliminada com motivo.

Se faltar qualquer um, registre no máximo como nota provisória, não como procedimento autoritativo.

## Workflow
1. Extraia o caminho que funcionou: ordem, comandos, arquivos, dependências, pré-condições e verificação.
2. Registre os dead-ends relevantes e por que falharam.
3. Classifique a descoberta:
   - processo reutilizável -> skill, runbook ou referência;
   - fato isolado -> nota/contexto;
   - one-off -> não persistir.
4. Escolha o menor escopo seguro: projeto antes de global quando houver dependência local.
5. Procure conhecimento existente e atualize-o em vez de duplicar.
6. Remova valores secretos e preserve apenas ponteiros para onde credenciais vivem.
7. Escreva a versão reutilizável separando invariantes de detalhes acidentais da sessão.
8. Valide o artefato final e informe o que foi capturado e onde.

## Guardrails
- Nunca persistir tokens, senhas, chaves, strings de conexão ou valores de credenciais.
- Não promover processos não verificados.
- Não transformar uma resposta específica em uma skill genérica sem abstração.
- Preserve o dead-end quando ele economizar tempo futuro.
- Prefira melhorar uma skill existente a criar outra com gatilho concorrente.

## Origem adaptada
Metodologia inspirada em `Kulaxyz/self-learning-skills`, adaptada ao Arsenal e integrada com `retrospective-codify`, `session-learn`, `skill-builder` e `verify-before-claim`.
