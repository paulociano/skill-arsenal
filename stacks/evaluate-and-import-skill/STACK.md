---
name: evaluate-and-import-skill
description: Avalia uma skill externa, compara com o Arsenal, adapta para o ambiente atual, revisa segurança e importa somente quando houver valor real.
---

# Evaluate And Import Skill

## Objetivo
Adicionar skills externas sem copiar dependências incompatíveis, redundância ou riscos desnecessários.

## Skills candidatas
- source-to-skill
- skill-security-review
- skill-builder
- verify-before-claim

## Workflow
1. Leia a fonte original e identifique metodologia, dependências e ferramentas.
2. Compare a candidata com as skills existentes no Arsenal.
3. Classifique A, B, C ou D considerando utilidade, novidade, segurança, portabilidade e sobreposição.
4. Use `skill-security-review` para riscos de execução, dados, credenciais e dependências.
5. Use `source-to-skill` ou `skill-builder` quando houver valor real e a adaptação precisar ser estruturada.
6. Adapte comandos específicos de outros agentes para capacidades realmente disponíveis.
7. Crie ou atualize `skills/<nome>/SKILL.md` somente quando justificado.
8. Registre a avaliação em `evaluations/` quando esse diretório estiver disponível.
9. Valide frontmatter, nomes, descriptions e portabilidade.

## Regra de parcimônia
Prefira melhorar uma skill existente a criar uma duplicata quase equivalente.
