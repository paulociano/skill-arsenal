# Skill Arsenal

O Skill Arsenal é a biblioteca canônica de métodos, workflows, stacks e Agent Skills do usuário.

## Fonte canônica

A fonte técnica oficial e atualizada do Skill Arsenal é o repositório privado:

https://github.com/paulociano/skill-arsenal

No Windows, a cópia de trabalho local esperada é:

C:\Users\ph_gr\Skill-Arsenal

As Agent Skills utilizadas pelo Codex são expostas em:

C:\Users\ph_gr\.agents\skills

Essa pasta deve apontar para:

C:\Users\ph_gr\Skill-Arsenal\skills

O GitHub vence cópias antigas, exports, documentos do Google Drive e snapshots locais não versionados.

O Google Drive deve ser tratado como documentação, material de origem ou legado histórico, salvo instrução explícita do usuário.

## Regra principal

Quando o usuário apresentar uma tarefa, identifique se alguma skill ou stack do Arsenal melhora materialmente o resultado.

Se sim, utilize a menor combinação necessária.

Se não, execute normalmente.

Não utilize skills mecanicamente.

## Descoberta eficiente

Não leia todos os SKILL.md para cada tarefa.

Use primeiro nomes e descriptions das skills para selecionar candidatas.

Depois leia somente:
- SKILL.md das skills escolhidas;
- stacks necessários;
- references necessários;
- scripts necessários;
- assets necessários.

Prefira uma skill a várias quando uma for suficiente.

## use <skill>

Quando o usuário escrever:

use <skill>

localize em `skills/<skill>/SKILL.md` e utilize explicitamente a skill correspondente.

Exemplo:

use web-design-engineer

deve utilizar `skills/web-design-engineer/SKILL.md`.

## use <stack>

Quando o usuário escrever:

use <stack>

localize o stack correspondente em `stacks/` e aplique o fluxo definido nele.

Um stack pode orquestrar múltiplas skills, mas carregue apenas as realmente necessárias.

Se o diretório `stacks/` ainda não existir, não invente o stack. Informe a ausência e prossiga com a menor combinação de skills equivalente quando isso preservar a intenção do usuário.

## arsenal: <tarefa>

Quando o usuário escrever:

arsenal: <tarefa>

utilize primeiro `arsenal-router`.

O router deve:

1. entender a tarefa;
2. identificar skills e stacks candidatas;
3. selecionar a menor combinação necessária;
4. carregar somente os arquivos selecionados;
5. executar;
6. validar o resultado.

## avaliar skill: <url>

Quando o usuário escrever:

avaliar skill: <url>

faça o seguinte:

1. analise a fonte ou repositório indicado;
2. verifique segurança, qualidade e utilidade;
3. compare com as skills existentes no Arsenal;
4. identifique sobreposição, ganho real e lacunas;
5. adapte implementações específicas de Claude, Claude Code, Codex ou outros agentes para capacidades realmente disponíveis no ambiente atual;
6. classifique a candidata como A, B, C ou D;
7. se houver valor real, crie ou atualize a skill correspondente em `skills/`;
8. quando existir `evaluations/`, registre a avaliação também nesse diretório;
9. valide frontmatter, estrutura, segurança e portabilidade;
10. mostre claramente quais arquivos foram criados ou alterados.

Não copie skills externas cegamente.

Use `skill-security-review`, `source-to-skill` ou `skill-builder` quando agregarem valor.

## Instalação de nova skill

Uma nova skill deve ser instalada no repositório canônico, preferencialmente em:

skills/<nome-da-skill>/SKILL.md

O SKILL.md deve conter frontmatter válido com pelo menos:

---
name: nome-da-skill
description: descrição específica de quando utilizar esta skill
---

Preserve metodologia útil, mas remova dependências sem equivalente real.

Depois da criação ou alteração:

1. valide a skill;
2. mostre o diff quando apropriado;
3. não faça commit ou push sem autorização explícita do usuário;
4. quando autorizado, use uma mensagem de commit clara e específica.

## Atualização local

Antes de modificar o Arsenal, quando houver risco de divergência com o remoto:

git pull --ff-only

Depois das alterações, use:

git status
git diff

Commit e push somente com autorização explícita.

## Portabilidade

Skills podem ter sido originadas de Claude, Claude Code, Codex ou outros agentes.

Preserve metodologias úteis.

Substitua ferramentas específicas por capacidades equivalentes realmente disponíveis no ambiente atual.

Nunca invente ferramentas, conectores, comandos ou integrações.

Remova dependências sem equivalente quando necessário.

## Verificação

Quando fizer sentido, utilize skills de validação como:

- verify-before-claim
- runtime-ui-verification
- code-review
- skill-security-review

sem adicioná-las mecanicamente a toda tarefa.

## Alterações no próprio Arsenal

Ao editar o Arsenal:

- preserve compatibilidade com o formato Agent Skills;
- evite duplicar skills com objetivos equivalentes;
- prefira melhorar uma skill existente a criar uma variante quase idêntica;
- mantenha nomes em kebab-case;
- mantenha descriptions úteis para roteamento automático;
- não altere várias skills sem necessidade;
- trate o repositório GitHub como fonte técnica autoritativa.
