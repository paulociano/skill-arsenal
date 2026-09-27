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

### 5.1. Decidir por critérios explícitos

Aplicar uma triagem curta, inspirada nas decisões tipadas do Laya:
- **Escolha:** selecionar entre as candidatas pertinentes do índice; incluir "nenhuma skill" quando execução direta bastar. Não enviar o catálogo inteiro a um classificador.
- **Suficiência:** verificar se a candidata resolve a tarefa e suas ferramentas estão disponíveis. Ausência de contexto é "desconhecido", não "não".
- **Complexidade:** distinguir tarefa direta, composição com dependências e decisão aberta por critérios observáveis, sem inventar uma nota de confiança.
- **Encaminhamento:** usar caminho direto quando a escolha for clara; investigar a lacuna decisiva ou usar análise aprofundada quando houver ambiguidade relevante.

Preservar a escolha explícita do usuário. Registrar motivo e limitação em uma frase quando isso ajudar; não expor JSON em toda conversa nem carregar outra skill só para cumprir esta triagem.

Se um runtime Laya estiver instalado e verificado no ambiente atual, pode apoiar classificações repetitivas de baixo risco com uma shortlist. Confirmar sua disponibilidade com inferência real; instalar o pacote ou executar apenas detecção de idioma não basta. Consultar o [runtime opcional](../structured-output-contract/references/laya-runtime.md) somente nesse caso ou quando o usuário pedir instalação. Uma resposta do modelo não autoriza execução, não substitui a leitura dos arquivos selecionados e não deve sobrepor instruções explícitas. Se indisponível, usar a mesma metodologia no assistente e identificar o fallback quando relevante.

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
- `avaliar skill: <url>`: preferir `evaluate-and-import-skill` para uma fonte simples; usar `arsenal-autopilot` para lotes, ecossistemas grandes ou quando a comparação de overlap/ownership for central.
- `arsenal autopilot: <urls/tarefa>`: usar a stack `arsenal-autopilot` para avaliar e evoluir o Arsenal de ponta a ponta.

## Manutenção do índice
Quando uma skill ou stack for criada, removida, renomeada ou tiver sua `description` alterada materialmente, atualize também `ARSENAL INDEX.md`.

## Regras
Não carregue todo o Arsenal.
Não invente ferramentas, stacks ou integrações.
Preserve metodologia útil de skills externas, mas adapte dependências incompatíveis.
Prefira melhorar recursos existentes a criar duplicatas.
