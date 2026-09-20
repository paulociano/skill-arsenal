\---

name: arsenal-router

description: Seleciona e orquestra a menor combinação necessária de skills do Skill Arsenal. Use quando o usuário escrever "arsenal:", pedir para usar o Arsenal, pedir seleção automática de skills ou quando uma tarefa complexa puder se beneficiar de múltiplas skills.

\---



\# Arsenal Router



\## Objetivo



Selecionar a menor combinação de Agent Skills disponível que melhore

materialmente o resultado de uma tarefa.



\## Quando usar



Use esta skill quando:



\- o usuário escrever `arsenal:`;

\- o usuário pedir para usar o Skill Arsenal;

\- for necessário selecionar skills automaticamente;

\- houver dúvida sobre qual skill utilizar;

\- uma tarefa complexa puder exigir múltiplas skills.



\## Workflow



\### 1. Entender a tarefa



Determine:



\- objetivo final;

\- artefato esperado;

\- domínio;

\- restrições;

\- necessidade de pesquisa, implementação ou validação.



\### 2. Identificar candidatas



Considere primeiro os nomes e descriptions das skills instaladas.



Não leia todos os SKILL.md.



\### 3. Selecionar



Escolha a menor combinação de skills que resolva adequadamente a tarefa.



Prefira uma skill a três quando uma for suficiente.



\### 4. Carregar



Leia somente:



\- SKILL.md das skills selecionadas;

\- references necessários;

\- scripts necessários;

\- assets necessários.



\### 5. Executar



Siga as metodologias das skills selecionadas, adaptando-as às

capacidades realmente disponíveis no ambiente atual.



\### 6. Validar



Antes de concluir:



\- verifique se a tarefa foi realmente concluída;

\- utilize skills de verificação quando elas agregarem valor;

\- não declare sucesso sem evidência suficiente.



\## Regras



Não carregue todo o Arsenal.



Não use skills apenas porque estão disponíveis.



Não invente ferramentas ou integrações.



Não preserve comandos específicos de Claude, Claude Code ou outro

agente quando não existirem neste ambiente.



Preserve a metodologia útil e adapte a implementação.



\## Regra de composição



A ordem preferida é:



tarefa

→ identificação

→ menor conjunto de skills

→ execução

→ verificação



Use stacks ou múltiplas skills somente quando houver ganho real.

