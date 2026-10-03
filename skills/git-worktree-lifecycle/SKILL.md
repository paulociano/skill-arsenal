---
name: git-worktree-lifecycle
description: "Usar quando uma mudança de código precisa de workspace Git isolado ou quando uma branch/worktree concluída precisa ser integrada, publicada em PR, preservada ou descartada com segurança."
---

# Git Worktree Lifecycle

## Objetivo

Isolar mudanças de desenvolvimento e concluir o ciclo de uma branch/worktree sem contaminar a árvore principal, perder trabalho, apagar estado útil cedo demais ou declarar integração antes de verificar o resultado.

## Quando usar

- implementação paralela ou agentic que precisa de isolamento de filesystem;
- mudança substancial que não deve ocorrer diretamente em main/master;
- trabalho já executado em worktree que precisa virar merge, PR, preservação ou cleanup;
- retomada de uma branch/worktree cujo estado de integração não está claro.

Não usar apenas para leitura do repositório ou para tarefas sem mutação de código.

## Princípios

1. Detectar o estado real do Git antes de criar qualquer isolamento novo.
2. Preferir mecanismo nativo de worktree do ambiente quando existir.
3. Não criar worktree dentro de diretório versionável que possa ser adicionado ao próprio repositório.
4. Baseline quebrado é evidência a preservar, não um erro a esconder.
5. Push, merge e descarte são decisões distintas e não devem ser inferidas uma da outra.
6. Cleanup só acontece depois de integração verificada ou descarte explicitamente autorizado.
7. Estado ambíguo deve ser inspecionado antes de repetir comandos.

## Workflow

### 1. Detectar o ambiente

Antes de criar ou remover qualquer coisa, identificar:
- raiz do repositório;
- branch ou detached HEAD atual;
- git dir e common git dir;
- worktrees existentes;
- base branch conhecida ou provável;
- dirty state e commits ainda não publicados.

Se já estiver em uma worktree vinculada, não criar uma worktree aninhada por conveniência.

### 2. Escolher o isolamento

Ordem de preferência:
1. ferramenta nativa de worktree/isolation do ambiente, quando realmente disponível;
2. worktree Git criada por terminal, quando o runtime permite;
3. branch comum no workspace atual, quando isolamento por worktree não for possível.

Ao usar git worktree manual:
- respeitar preferência explícita do projeto;
- reutilizar diretório de worktrees já convencionado apenas se ele for seguro;
- se um diretório interno ao repo não estiver ignorado, preferir um diretório irmão/externo em vez de alterar .gitignore silenciosamente;
- criar uma branch com nome ligado à tarefa e base explícita.

Nunca assumir que main/master é a base correta apenas pelo nome.

### 3. Estabelecer baseline

No workspace isolado:
- seguir o setup documentado pelo projeto, sem executar instaladores arbitrários de terceiros;
- registrar HEAD/base SHA quando isso ajudar a rastrear a mudança;
- rodar os checks mínimos que provam o estado inicial;
- se o baseline já falhar, registrar o que era pré-existente e só continuar quando for possível separar falha antiga de regressão nova.

### 4. Executar a mudança

Durante a implementação:
- manter escopo ligado à tarefa;
- usar commits pequenos quando o repositório trabalhar dessa forma;
- não misturar cleanup de Git com refatorações laterais;
- em execução paralela, cada writer recebe branch/worktree própria ou ownership de arquivos claramente separado.

### 5. Verificar conclusão

Antes de qualquer integração:
- rodar os testes/checks proporcionais ao risco no estado final da branch;
- verificar diff, commits e arquivos não rastreados relevantes;
- confirmar que o resultado corresponde à spec/tarefa, não apenas que Git está limpo.

Falha de testes ou estado desconhecido bloqueia cleanup.

### 6. Resolver o destino da branch

Se o usuário ou workflow já definiu o destino, seguir essa decisão. Caso contrário, manter a branch/worktree preservada até que a decisão de integração exista.

Destinos possíveis:
- merge local na base confirmada;
- push + Pull Request;
- preservar branch/worktree para continuação;
- descarte explícito.

Para merge local:
- confirmar base;
- integrar a partir do workspace apropriado;
- rodar novamente os checks relevantes no estado mesclado antes de remover a origem.

Para push + PR:
- publicar a branch correta;
- abrir o PR contra a base correta;
- preservar a worktree enquanto houver chance razoável de feedback/ajustes.

Detached HEAD não deve ser tratado como branch nomeada. Para publicar, criar um nome de branch remoto/local adequado ou preservar o estado.

### 7. Cleanup seguro

Remover worktree/branch somente quando:
- a integração foi verificada; ou
- o usuário autorizou descarte de forma explícita.

Regras:
- sair do diretório da worktree antes de removê-la;
- confirmar quais commits pertencem ao trabalho antes de apagar;
- preferir deleção não forçada de branch;
- force delete ou perda deliberada de commits exige confirmação explícita;
- se merge, PR ou testes falharem, preservar o workspace para recuperação.

## Falhas comuns

- criar worktree sem verificar se já existe isolamento;
- trabalhar diretamente em main por conveniência;
- adicionar diretório de worktree ao próprio repo;
- rodar setup/install genérico ignorando a documentação do projeto;
- apagar worktree logo após push, dificultando resposta a review;
- tratar detached HEAD como branch comum;
- repetir push/merge após timeout sem verificar se a operação já ocorreu;
- remover branch antes de provar que a integração contém os commits esperados.

## Integração

Combina com:
- surgical-engineering;
- tdd;
- code-review;
- multi-agent-orchestration;
- software-factory-operations;
- merge-conflict-resolution;
- verify-before-claim.

## Provenance

Adaptada principalmente de obra/superpowers, nas skills using-git-worktrees e finishing-a-development-branch. ECC (affaan-m/ECC) foi usado como contraste para branching, merge/rebase e colaboração. O Arsenal preserva isolamento, baseline, escolha explícita de integração, provenance e cleanup seguro, removendo dependências de hooks, diretórios e comandos específicos de outros harnesses.
