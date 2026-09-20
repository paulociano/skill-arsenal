---
name: arsenal-router
description: Seleciona e orquestra a menor combinação necessária de skills e stacks do Skill Arsenal. Use quando o usuário escrever "arsenal:", pedir para usar o Arsenal, pedir seleção automática ou quando uma tarefa complexa puder se beneficiar de workflows coordenados.
---

# Arsenal Router

## Objetivo
Selecionar a menor combinação de stacks e Agent Skills que melhore materialmente o resultado.

## Fonte de roteamento
Para seleção automática, leia primeiro `ARSENAL INDEX.md`.

O índice é o catálogo leve de nomes e descriptions. Não abra todos os SKILL.md ou STACK.md.

Depois de selecionar candidatas, abra somente os arquivos necessários.

## Workflow

### 1. Entender a tarefa
Determine objetivo final, artefato esperado, domínio, restrições e necessidade de pesquisa, implementação ou validação.

### 2. Consultar o índice
Leia `ARSENAL INDEX.md` e identifique as candidatas mais específicas.

### 3. Verificar stacks
Use uma stack quando ela representar claramente um workflow recorrente compatível com a tarefa.

Não use stack apenas porque existe.

### 4. Considerar skills isoladas
Se uma skill resolver adequadamente a tarefa, prefira a skill isolada.

### 5. Selecionar a menor combinação
Ordem de preferência:

1. uma skill isolada;
2. uma stack compatível;
3. pequena combinação de skills;
4. stack + skill adicional somente quando necessário.

### 6. Carregar somente o necessário
Leia apenas:
- STACK.md selecionado;
- SKILL.md das skills realmente necessárias;
- references, scripts e assets necessários.

Skills listadas em uma stack são candidatas, não obrigatórias.

### 7. Executar
Siga o workflow selecionado e adapte ferramentas às capacidades realmente disponíveis no ambiente atual.

### 8. Validar
Antes de concluir:
- verifique se o objetivo foi atingido;
- use skills de verificação quando agregarem valor;
- não declare sucesso sem evidência suficiente.

## Comandos do Arsenal
- `use <skill>`: usar explicitamente a skill correspondente.
- `use <stack>`: usar explicitamente a stack correspondente.
- `arsenal: <tarefa>`: consultar o índice e selecionar automaticamente a menor combinação.
- `avaliar skill: <url>`: preferir a stack `evaluate-and-import-skill`.

## Manutenção do índice
Quando uma skill ou stack for criada, removida, renomeada ou tiver sua `description` alterada materialmente, atualize também `ARSENAL INDEX.md`.

## Regras
Não carregue todo o Arsenal.
Não invente ferramentas, stacks ou integrações.
Preserve metodologia útil de skills externas, mas adapte dependências incompatíveis.
Prefira melhorar recursos existentes a criar duplicatas.
