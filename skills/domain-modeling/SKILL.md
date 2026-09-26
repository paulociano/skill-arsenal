---
name: domain-modeling
description: Construir e refinar o modelo de domínio de um projeto com linguagem canônica, cenários de borda, glossário e ADRs somente quando decisões irreversíveis e surpreendentes exigirem contexto.
---

# Domain Modeling

## Objetivo
Criar uma linguagem de domínio compartilhada entre pessoas, código e agentes, reduzindo ambiguidade e retrabalho sem transformar documentação em depósito de detalhes de implementação.

## Quando usar
Use quando:
- termos do domínio estiverem vagos, conflitantes ou sobrecarregados;
- o usuário estiver definindo entidades, estados, relações ou regras de negócio;
- houver divergência entre linguagem falada e comportamento do código;
- for útil registrar um glossário de domínio ou uma decisão arquitetural.

Não use apenas para ler um glossário existente.

## Workflow
1. Identifique os termos centrais usados na conversa, documentação e código.
2. Confronte termos ambíguos ou conflitantes e proponha uma forma canônica.
3. Teste o modelo com cenários concretos e casos-limite.
4. Verifique se o código e a documentação existente sustentam o significado acordado.
5. Registre somente o significado do domínio em um glossário/contexto, sem detalhes de implementação.
6. Quando uma decisão for difícil de reverter, surpreendente sem contexto e fruto de trade-off real, registre um ADR.
7. Atualize os termos assim que forem resolvidos, evitando acumular divergências para o final.

## Regras
- Separe claramente domínio de implementação.
- Um termo canônico deve ter um significado estável dentro do contexto em que é usado.
- Se houver múltiplos bounded contexts, torne a fronteira explícita em vez de forçar um único vocabulário global.
- Use cenários de borda para expor ambiguidades antes de codificar.
- ADR não é diário nem changelog: registre apenas decisões que um leitor futuro realmente precisará entender.

## Saída
Entregue:
- glossário ou contexto atualizado;
- ambiguidades resolvidas ou explicitamente pendentes;
- cenários que validam o modelo;
- ADRs apenas quando realmente justificados.

## Origem adaptada
Metodologia inspirada em `mattpocock/skills`, especialmente `domain-modeling`, adaptada para capacidades reais do ChatGPT e para a regra de parcimônia do Skill Arsenal.
