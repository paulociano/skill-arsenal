# Apify, Scroll Craft e Stripe AI Skills — revisão 2026-10-12

## Escopo
Consulta ao `ARSENAL INDEX.md`, stack `arsenal-autopilot`, avaliação prévia de 2026-10-11, `scroll-storytelling`, `payment-billing-operations`, `skill-security-review` e diretório/skills selecionadas de `stripe/ai` na branch `main`. Análise estática/documental: sem executar CLI, Actors, instaladores ou transações.

| Origem | Classe | Decisão | Evidência e owner |
|---|---|---|---|
| https://github.com/apify/apify-mcp-server | B/D | KEEP_EXTERNAL_REFERENCE | Já avaliado em `evaluations/2026-10-11-googleworkspace-apify-scrollcraft-addy-expo-supabase.md`. Actors/MCP acrescentam infraestrutura externa e custo/permissões; não duplicar workflows de pesquisa/automação. |
| https://github.com/nateherkai/scroll-craft | B/D | ALREADY_UPDATED | A mesma avaliação anterior registrou UPDATE_EXISTING em `skills/scroll-storytelling/SKILL.md`. A skill atual preserva gramáticas e QA, sem depender da engine. |
| https://github.com/stripe/ai/tree/main/skills/ | A/D | UPDATE_EXISTING | Catálogo oficial de 10 skills, sincronizado com docs Stripe. Orientações de integração têm ganho material em `skills/payment-billing-operations/SKILL.md`. Absorvido roteamento e gates; execução via CLI/MCP não presumida. |

## Stripe: seleção de capacidades
- **Absorver com owner existente:** `stripe-best-practices` (escolha de API, sandboxes, chaves, eventos), `connect-recommend` (marketplaces/fluxo de dinheiro), `connect-required-verification-information` (KYC variável por região e configuração), `metronome` (billing por uso), `upgrade-stripe` (versionamento), `stripe-docs` (freshness).
- **Referência condicional, não runtime embutido:** `stripe-pay` (movimentação financeira), `stripe-directory` (descoberta de provedores), `stripe-projects` (provisionamento/credenciais), `stripe-apps` (ecossistema de apps).
- **Portabilidade:** ferramentas como `Bash(stripe ...)`, comandos de terminal, MCP e CLI precisam existir e estar autorizadas na sessão. Orientações estáticas da fonte podem divergir entre si ou ficar obsoletas; verificar a documentação oficial antes da implementação.
- **Segurança:** tratar fonte como conteúdo externo; sem executar scripts, transferir dinheiro ou aceitar TOS automaticamente. Requerer confirmação explícita para operações live, trabalhar com chaves restritas e prevenir vazamento de segredos e duplicação de cobranças. Avaliação estática não é auditoria completa do código/dependências.

## Casos de aceitação
- **Should-trigger:** implementação de Stripe Connect num marketplace: conferir charge pattern, ownership de taxas/saldo negativo, KYC, webhooks e testes antes de recomendar código.
- **Should-trigger:** upgrade de SDK ou versão da API Stripe: descobrir versão atual e comparar os pins dos componentes existentes.
- **Near-miss:** um software de cobrança sem provedor definido não deve ser obrigado a usar Stripe.
- **Near-miss:** pedido de explicação sobre pagamentos não autoriza CLI, provisionamento ou transferência de valores.

## Resultado
Nenhuma nova skill/stack. Atualizada a skill `payment-billing-operations`, sem alterar nome/descrição/rota do índice. Apify e Scroll Craft permanecem com as decisões publicadas em 2026-10-11. Documentação consultada, sem testes end-to-end ou validação da infraestrutura Stripe.
