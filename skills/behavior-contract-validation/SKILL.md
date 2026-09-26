---
name: behavior-contract-validation
description: Validar aplicações, CLIs, APIs e artefatos como caixa-preta contra um contrato de comportamento observável, separando evidência de runtime de revisão de implementação.
---

# Behavior Contract Validation

## Objetivo
Verificar o que o sistema realmente faz pela superfície visível ao usuário ou operador, sem depender da implementação interna.

## Quando usar
Use para validar:
- aplicações web em runtime;
- CLIs;
- APIs;
- fluxos end-to-end;
- arquivos ou artefatos gerados;
- correções em que a prova precisa ser independente da implementação.

## Workflow
1. Obtenha um contrato de comportamento. Se não existir, derive um contrato curto a partir da solicitação do usuário.
2. Liste cada cláusula observável, setup necessário, resultado esperado e evidência exigida.
3. Teste somente por superfícies externas: browser, CLI, API, arquivo gerado, logs públicos ou acessibilidade.
4. Para cada cláusula, registre `pass`, `fail`, `blocked` ou `out_of_scope`.
5. Use probes anti-falso-positivo:
   - varie os dados;
   - teste vazio e inválido;
   - repita ou atualize;
   - verifique persistência quando relevante;
   - confirme que ações produzem efeito real, não apenas mensagem de sucesso.
6. Capture evidência reproduzível do comportamento observado.
7. Relate lacunas contra o contrato, sem inferir causa interna sem evidência adicional.

## Separação de responsabilidades
- Esta skill valida comportamento externo.
- `code-review` avalia implementação e diff.
- `runtime-ui-verification` pode fornecer a interação/runtime quando a tarefa for especificamente UI.
- Use ambos quando for importante provar comportamento e também explicar a causa no código.

## Guardrails
- Não declarar sucesso sem cobrir todas as cláusulas relevantes.
- Não transformar conhecimento do código em atalho para uma validação que deveria ser black-box.
- Se a validação exigir fonte interna, marque a limitação e mude explicitamente de modo antes de inspecionar a implementação.
- Não registrar segredos em evidências, screenshots ou logs.

## Origem adaptada
Metodologia inspirada em `openclaw/agent-skills`, especialmente `behavior-validator`, adaptada às ferramentas reais do ChatGPT.
