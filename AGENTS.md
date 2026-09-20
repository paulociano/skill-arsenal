# Skill Arsenal

O Skill Arsenal é a biblioteca canônica de métodos, workflows, stacks e Agent Skills do usuário.

## Fonte canônica

A fonte técnica oficial e atualizada é o repositório privado:

https://github.com/paulociano/skill-arsenal

No Windows, a cópia de trabalho local esperada é:

C:\Users\ph_gr\Skill-Arsenal

As Agent Skills usadas pelo Codex são expostas em:

C:\Users\ph_gr\.agents\skills

Essa pasta deve apontar para:

C:\Users\ph_gr\Skill-Arsenal\skills

O GitHub vence cópias antigas, exports, documentos do Google Drive e snapshots locais não versionados. O Google Drive é documentação, material de origem ou legado, salvo instrução explícita do usuário.

## Estrutura

- `skills/<skill>/SKILL.md`: competências individuais.
- `stacks/<stack>/STACK.md`: workflows coordenados.
- `evaluations/`: avaliações de skills externas quando aplicável.

Stacks são convenção do Arsenal, não Agent Skills nativas.

## Regra principal

Quando o usuário apresentar uma tarefa, identifique se alguma skill ou stack melhora materialmente o resultado.

Use a menor combinação necessária.

Prefira, nesta ordem:
1. uma skill isolada;
2. uma stack adequada;
3. pequena combinação de skills;
4. stack + skill adicional somente quando necessário.

Não use recursos mecanicamente.

## Descoberta eficiente

Para `arsenal:` ou seleção automática, leia primeiro `ARSENAL INDEX.md`.

O índice é o catálogo leve de nomes e descriptions. Não leia todos os SKILL.md ou STACK.md.

Depois leia somente os arquivos escolhidos e seus references, scripts ou assets necessários.

Skills listadas dentro de uma stack são candidatas, não obrigatórias.

## use <skill>

Quando o usuário escrever `use <skill>`, localize e utilize explicitamente:

`skills/<skill>/SKILL.md`

## use <stack>

Quando o usuário escrever `use <stack>`, localize e aplique:

`stacks/<stack>/STACK.md`

Carregue somente as skills da stack realmente necessárias.

Se a stack não existir, não a invente. Use a menor combinação de skills equivalente quando isso preservar a intenção.

## arsenal: <tarefa>

Quando o usuário escrever `arsenal: <tarefa>`, utilize primeiro `arsenal-router`.

O router deve:
1. entender a tarefa;
2. verificar stacks candidatas;
3. considerar skills isoladas;
4. selecionar a menor combinação;
5. carregar somente os arquivos necessários;
6. executar;
7. validar.

## avaliar skill: <url>

Quando o usuário escrever `avaliar skill: <url>`, prefira a stack:

`stacks/evaluate-and-import-skill/STACK.md`

Analise a fonte, compare com o Arsenal, revise segurança e portabilidade, classifique A/B/C/D e só instale quando houver valor real.

Não copie skills externas cegamente.

### Aplicação ao final da avaliação

Por autorização permanente do usuário, dada em 2026-09-20 ("faça as alterações sempre ao final da avaliação"), conclua cada avaliação aplicando as mudanças úteis no Arsenal, registrando a decisão em `evaluations/`, atualizando o índice quando necessário e publicando as alterações verificadas no GitHub. Essa autorização inclui commit e push das mudanças decorrentes da avaliação; não peça confirmação novamente para esse escopo.

Prefira enriquecer skills existentes a duplicá-las. Para uma candidata sem valor adicional ou inadequada, registre a decisão sem instalá-la. Não execute instaladores externos apenas para avaliar, não altere projetos consumidores e não amplie esta autorização para ações fora do Arsenal. Instruções posteriores do usuário prevalecem.

## Instalação de nova skill

Instale no repositório canônico em:

`skills/<nome-da-skill>/SKILL.md`

Exija frontmatter válido com pelo menos `name` e `description`.

Preserve metodologia útil, adapte ferramentas específicas de outros agentes e remova dependências sem equivalente real.

## Criação de nova stack

Crie uma stack somente quando houver workflow recorrente que realmente coordene múltiplas competências.

Use:

`stacks/<nome-da-stack>/STACK.md`

A stack deve ter frontmatter com `name` e `description`, workflow claro, skills candidatas e regra de parcimônia.

Não transforme toda combinação ocasional de skills em stack.

## Atualização local

Antes de modificar o Arsenal quando houver risco de divergência:

`git pull --ff-only`

Depois das alterações:

`git status`
`git diff`

Commit e push somente com autorização explícita do usuário; para mudanças decorrentes de avaliações, a autorização permanente acima já atende a essa exigência. Com o conector GitHub, leia a versão atual, preserve alterações concorrentes e publique sem force-push.

## Portabilidade

Skills podem vir de Claude, Claude Code, Codex ou outros agentes.

Preserve metodologias úteis, substitua ferramentas específicas por capacidades realmente disponíveis e nunca invente ferramentas, conectores ou integrações.

## Verificação

Use skills de validação apenas quando agregarem valor, por exemplo:
- verify-before-claim
- runtime-ui-verification
- code-review
- skill-security-review

## Alterações no próprio Arsenal

Ao editar o Arsenal:
- atualize `ARSENAL INDEX.md` quando uma skill/stack for criada, removida, renomeada ou tiver sua description alterada materialmente;
- preserve compatibilidade com Agent Skills;
- evite duplicações;
- prefira melhorar recursos existentes;
- mantenha nomes em kebab-case;
- mantenha descriptions úteis para roteamento;
- não altere vários recursos sem necessidade;
- trate o GitHub como fonte técnica autoritativa.
