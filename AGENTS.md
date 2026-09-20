# Skill Arsenal

O Skill Arsenal é a biblioteca de métodos, workflows e Agent Skills do usuário.

As Agent Skills estão instaladas globalmente em:

C:\Users\ph_gr\.agents\skills

## Regra principal

Quando o usuário apresentar uma tarefa, identifique se alguma skill
instalada melhora materialmente o resultado.

Se sim, utilize a menor combinação necessária.

Se não, execute normalmente.

Não utilize skills mecanicamente.

## use <skill>

Quando o usuário escrever:

use <skill>

localize e utilize explicitamente a skill correspondente.

Exemplo:

use web-design-engineer

deve utilizar `web-design-engineer`.

## arsenal: <tarefa>

Quando o usuário escrever:

arsenal: <tarefa>

utilize primeiro `arsenal-router`.

O router deve:

1. entender a tarefa;
2. identificar skills candidatas;
3. selecionar a menor combinação necessária;
4. carregar somente os SKILL.md selecionados;
5. executar;
6. validar o resultado.

## Seleção eficiente

Não leia todos os SKILL.md para cada tarefa.

Use inicialmente nomes e descriptions das skills para seleção.

Depois leia somente as skills escolhidas.

## Portabilidade

Skills podem ter sido originadas de Claude, Claude Code, Codex ou
outros agentes.

Preserve metodologias úteis.

Substitua ferramentas específicas por capacidades equivalentes
realmente disponíveis no ambiente atual.

Nunca invente ferramentas.

Remova dependências sem equivalente quando necessário.

## Verificação

Quando fizer sentido, utilize skills de validação como:

- verify-before-claim
- runtime-ui-verification
- code-review
- skill-security-review

sem adicioná-las mecanicamente a toda tarefa.