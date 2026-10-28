# Avaliação — msitarzewski/agency-agents

Data: 2026-10-28
Fonte: https://github.com/msitarzewski/agency-agents (branch `main`, clone raso, MIT)
Pedido do usuário: instalar o repositório como skills no Claude e registrar no Arsenal.
Triagem anterior: `2026-10-22-github-top100-stars-triage.md` (item 54, KEEP_EXTERNAL_REFERENCE por inspeção só do README).

## Escopo

Coleção de cerca de 300 arquivos `.md`, um por "agente" (persona especialista), em 20+ divisões (engenharia, design, vendas, finanças, marketing, suporte, jurídico etc.). Cada arquivo tem frontmatter `name`/`description` e um corpo com identidade, missão, regras e templates. Não há scripts de runtime nas divisões lidas; `scripts/` e `integrations/` do repositório são instaladores para outras ferramentas e não foram executados.

## O que foi feito para o usuário (fora do Arsenal)

- Convertidos 283 agentes em pastas `SKILL.md` (nome em kebab-case, description preservada) e empacotados em `.zip` para upload nas configurações de Skills do Claude. Foram ignorados 16 arquivos sem frontmatter de agente (guias de fases e cenários).
- Busca nas skills do Claude do usuário: nenhuma do repositório estava instalada. O catálogo de cards de skills não ofereceu equivalentes.
- A instalação no Claude depende de upload manual feito pelo usuário.

## Segurança

Revisão por leitura e varredura de padrões (`curl`, `wget`, `eval`, `base64`, `rm -rf`, `sudo`, chaves, senha, token) nas divisões de vendas, finanças e no agente de chief of staff. Resultado: dois acertos benignos ("tokens de personalização" em sequências de outbound e "design tokens" em padrões de saída). Nenhum comando executável, rede ou credencial. Não foram analisadas as demais divisões.

## Candidatas examinadas e decisão

| Agente | Overlap no Arsenal | Classe | Decisão |
|---|---|---|---|
| `sales-discovery-coach` | Nenhum owner de metodologia de descoberta. `call-evaluation` avalia ligação pelo Card e proíbe frameworks externos sem pedido; `sales-objection-handling` cobre objeção; `gestao-comercial-da-semana` cita SPIN só como lente de análise. | A | CREATE_NEW como `discovery-call-coaching` |
| `sales-deal-strategist` (MEDDPICC, Challenger) | Sem owner, mas voltado a vendas B2B enterprise com comitê de compra; o fluxo do usuário é consultoria financeira com decisor individual. | B | KEEP_EXTERNAL_REFERENCE |
| `sales-coach` | Coberto por `coaching-development-loop` e `call-evaluation`; foco em pipeline review de time de SaaS. | C | Não instalar |
| `finance-financial-analyst` | `financial-modeling-valuation`, `financial-planning-analysis`, stack `financial-analysis-cycle`. Corpo em USD/GAAP, sem base brasileira. | C | Não instalar |
| `finance-fpa-analyst` | `financial-planning-analysis` já cobre budget, forecast e variance. Templates de plano operacional corporativo. | C | Não instalar |
| `specialized-chief-of-staff` | Há skill de mesmo nome com função diferente no Claude do usuário e no Arsenal; risco de colisão. | D | Rejeitar |
| Demais ~275 agentes | Fora do perfil de uso atual ou sem avaliação individual. | n/a | Não avaliados; permanecem como referência externa no repositório de origem |

## Implementação

- Criada `skills/discovery-call-coaching/SKILL.md`: SPIN, Gap Selling e funil de dor combinados em roteiro e estrutura de conversa. Adaptações: persona, "memória" fictícia e estatísticas de objeção sem fonte removidas; limites éticos (sem urgência artificial, sem exploração de vulnerabilidade, sem promessa de resultado em consultoria financeira); roteamento explícito para `call-evaluation` e `sales-objection-handling` para evitar sobreposição.
- Atualizado `ARSENAL INDEX.md` com a nova skill, ao lado de `sales-objection-handling`.

## Limites da validação

- Só `sales-discovery-coach` foi lido integralmente. As demais decisões se apoiam em descrição, cabeçalhos e comparação com os owners existentes.
- A nova skill não foi testada em conversas reais nem passou por `skill-security-review` formal; é texto instrucional sem scripts.
- As equivalências com o Claude (skills instaladas) foram checadas só pelos nomes e descriptions listados em 2026-10-28.
