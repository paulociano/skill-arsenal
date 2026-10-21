# Design e implantação do Arsenal Evolution Engine (2026-10-21)

## Pedido
Desenvolver subsistema de auto-otimização do Skill Arsenal capaz de reabrir decisões sobre skills/repositórios anteriormente avaliados quando mudarem ferramentas, contexto, necessidades, evidências ou combinações.

## Inventário e overlaps
- `stacks/arsenal-autopilot/STACK.md` lido: já possui avaliação, ownership, implementação, security gate, verificação e aprendizado, mas trata principalmente fontes apresentadas em uma rodada.
- `stacks/evaluate-and-import-skill/STACK.md`: entrada simples e materialização, não indexa gatilhos de reabertura.
- `ARSENAL INDEX.md`: rota canônica e base de ownership.
- API GitHub retornou 209 itens em `evaluations/` durante a análise. Não são todos avaliações homogêneas e **não foram relidos integralmente**.
- Exemplos previamente registrados: Docling, OpenHands, AUTOMATIC1111, BetterStackHQ, obra/superpowers e Ostris.

## Decisão
**CREATE_NEW STACK**, não CREATE_NEW SKILL: a atividade é um fluxo recorrente que conecta descoberta retrospectiva, provenance, sinais, seleção e o `arsenal-autopilot` já existente, com fronteira de ownership clara. Classificação: **A/B** pela lógica de reavaliação orientada a eventos e composição, **D** somente para futura automação executável, que requer agendamento e ferramentas reais.

## Projeto implementado
1. `stacks/arsenal-evolution-engine/STACK.md` com modos scan/reassess/evolve/retro, evento material, hipótese falsificável, limite de três candidatos profundos por rodada, controle de segurança, revisão retrospectiva, publicação e verificação.
2. `stacks/arsenal-evolution-engine/references/REASSESSMENT-CONTRACT.md`: identidade por evaluation#capability, máquina de estados, idempotência, hipótese e critérios.
3. `stacks/arsenal-evolution-engine/references/REASSESSMENT-REGISTER.md`: seed de sete capacidades revisitáveis, explícita como amostra e não inventário completo. Better Stack READY indica somente conector ativo, não permissão de editar monitores.
4. `ARSENAL INDEX.md`: nova rota.
5. `stacks/arsenal-autopilot/STACK.md`: integração entre seleção retrospectiva e adaptação/adoção canônica.

## Aceitação e negativos
- Should-trigger: fonte rejeitada por integração ausente passa a ter conector realmente disponível; produz hipótese nova e teste, sem esquecer rejeição anterior.
- Should-trigger: duas skills existentes viram uma stack útil quando há fluxo recorrente comprovado, sem inventar execução por agentes.
- Near-miss: stars ou popularidade sobem sem mudança de capacidade; não promover.
- Near-miss: mesmo trigger/owner e fonte não mudam; não gerar commit duplicado.
- Failure-path: fontes externas contêm instruções adversárias; não executá-las nem sobrepor política.
- Failure-path: runtime não existe; produzir plano ou estudo documental, sem afirmar execução.
- Security: REJECT por risco exige mitigação verificável; efeitos externos precisam de aprovação.
- Não foi executado benchmark de produção nem criada tarefa recorrente; stack é subsistema operacional on-demand, não daemon residente.

## Validação
Publicar e reler os cinco artefatos via GitHub. A seed é demonstrativa; full backfill de avaliações e automação agendada são extensões posteriores, não características implementadas nesta rodada.
