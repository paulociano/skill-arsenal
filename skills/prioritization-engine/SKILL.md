---
name: prioritization-engine
description: "Priorizar trabalho, oportunidades ou problemas por impacto, urgência, dependências, risco e esforço com critérios explícitos e análise de sensibilidade."
---

# prioritization-engine

## Objetivo

Transformar uma fila de itens concorrentes em uma ordem de execução defensável, distinguindo prioridade estratégica, urgência operacional, dependências e capacidade real.

## Quando usar

- backlog de produto;
- projetos e iniciativas;
- leads/clientes;
- pautas de conteúdo;
- problemas/bugs;
- planos semanais ou trimestrais.

## Workflow

1. Definir o objetivo da priorização e horizonte.
2. Normalizar cada item em uma unidade comparável.
3. Separar:
   - impacto esperado;
   - urgência/time sensitivity;
   - dependências/unlocks;
   - risco/custo de atraso;
   - esforço/capacidade;
   - confiança na estimativa.
4. Identificar itens obrigatórios por compliance, segurança ou bloqueio.
5. Eliminar dupla contagem entre critérios.
6. Aplicar uma heurística simples primeiro.
7. Usar decision-analysis quando a escolha for sensível ou de alto impacto.
8. Fazer análise de capacidade: prioridade sem slot de execução não é plano.
9. Marcar quick wins, long bets, blockers e itens sem evidência suficiente.
10. Revisar ordem quando novas informações alterarem impacto, esforço ou dependências.

## Regras

- RICE, ICE, WSJF e matrizes impacto/esforço são heurísticas, não leis.
- Nunca usar score com falsa precisão.
- Urgência do solicitante não equivale automaticamente a importância.
- Dependência pode elevar prioridade mesmo sem alto valor isolado.
- Itens de alta incerteza podem pedir discovery/experiment antes de execução total.

## Integração

decision-analysis, execution planning via to-tickets/to-spec, project-complexity-management, experiment-design e domain-specific owners.

## Origem metodológica

Sintetiza princípios de MCDA, capacity-aware planning e priorização por impacto/esforço, sem adotar um framework único como padrão.
