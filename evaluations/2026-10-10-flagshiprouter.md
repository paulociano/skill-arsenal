# Avaliação: theRizwan/FlagshipRouter

- Data: 2026-10-10
- Fonte: https://github.com/theRizwan/FlagshipRouter (main)
- Stack: `arsenal-autopilot`, com revisão `skill-security-review` proporcional ao risco.
- Classe: **A/D** (método útil de hardening de gateway; implementação técnica não portátil sem runtime e credenciais).
- Decisão: **UPDATE_EXISTING** em `skills/model-routing-gateway/SKILL.md`; não criar skill ou stack nova.

## Evidências documentais

O README descreve gateway local multi-provider com endpoint compatível com OpenAI, roteamento somente para ofertas gratuitas por configuração, aliases e combos, painel de modelos e clientes de coding agent. Há Node.js >=20.9, instalação e execução via `npm run launch`, que pode instalar dependências e construir a aplicação. O README informa senha padrão de dashboard `123456`, instruindo alteração antes de exposição além de localhost. `docs/ARCHITECTURE.md` descreve camadas de API, tradução, execução, persistência local de credenciais, logs, OAuth e sync opcional. A skill externa `skills/flagshiprouter/SKILL.md` descreve endpoints e credenciais e encaminha para skills específicas de mídia.

## Matriz de capacidade

| Capacidade | Owner | Ação |
| --- | --- | --- |
| Cotas, seleção/fallback, autenticação, observabilidade | model-routing-gateway | já coberto; não duplicar |
| Política uniforme de provedores gratuitos entre catálogo, conexões, APIs e roteamento | model-routing-gateway | absorver e exigir teste de bypass |
| Segregação painel/API/upstream, senha default, bind remoto | model-routing-gateway | reforçar hardening |
| Tradução multimodal e SSE, aliases e combos | model-routing-gateway | reforçar compatibilidade por rota |
| Setup em múltiplos clientes que modifica suas configs | model-routing-gateway | exigir diff, backup e rollback |
| CLI, dashboard, instaladores, OAuth, servidor Next.js, templates de cliente, skills por modalidade | referência externa | não instalar/copiar |

## Segurança

**CAUTION para instalação e operação; APPROVE para metodologia adaptada.** A presença de senha inicial conhecida e armazenamento de credenciais torna inadequada a exposição sem hardening. Qualquer cloud sync e telemetria exigem tratamento explícito; compatibilidade declarada não é paridade de contrato. Provedor `free` não garante cota ou custo real, e aliases/fallbacks podem contornar restrições se não forem testados. Nenhum instalador, servidor, pacote ou teste dinâmico foi executado. A avaliação documental não certifica o software de terceiros.

## Incremento e testes

Should-trigger: implementação/auditoria de gateway multi-provider local, especialmente com modelo free-only, rota remota e configurações de coding agents.

Near-miss: resposta informacional sobre modelos; não é necessário instalar router nem alterar modelo desta conversa.

Checks de aceite: provider proibido não alcançável por alias/combo; senha inicial não autoriza painel exposto; clientes têm configs reversíveis; modalidade de streaming/tools validada; fallback não viola privacidade.

## Publicação

Alterada somente `skills/model-routing-gateway/SKILL.md` e criada esta avaliação. `ARSENAL INDEX.md` não exige mudança, pois não houve criação/renomeação nem alteração material da description.

## Fontes

- https://github.com/theRizwan/FlagshipRouter/blob/main/README.md
- https://github.com/theRizwan/FlagshipRouter/blob/main/docs/ARCHITECTURE.md
- https://github.com/theRizwan/FlagshipRouter/blob/main/skills/flagshiprouter/SKILL.md
- https://github.com/paulociano/skill-arsenal/blob/master/skills/model-routing-gateway/SKILL.md
