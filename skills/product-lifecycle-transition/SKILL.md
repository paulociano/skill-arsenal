---
name: product-lifecycle-transition
description: "Diagnosticar produtos maduros ou em declínio e decidir entre estender, substituir, colher ou retirar, conectando evidência de mercado, economia, migração, comunicação e critérios de saída."
---

# Product Lifecycle Transition

## Objetivo

Decidir o que fazer quando um produto parou de crescer, ficou caro de sustentar, perdeu relevância ou precisa ser substituído, sem confundir preferência interna por novidade com evidência de declínio.

## Quando usar

Use quando:
- receita, uso ou retenção estabilizam ou caem;
- suporte, manutenção ou risco operacional aumentam;
- existe debate entre reescrever, substituir ou encerrar;
- um sucessor precisa coexistir temporariamente com o produto antigo;
- é necessário planejar EOL, sunset ou migração de clientes.

Para crescimento de um produto saudável use `product-management-cycle`. Para GTM do sucessor use `go-to-market-strategy`.

## Princípio central

**Diagnostique o estágio e a pressão antes de escolher a jogada.**

## Quatro respostas possíveis

- **Extend** — manter o produto e ampliar capacidade, segmento, canal ou proposta.
- **Replace** — lançar sucessor e migrar clientes/uso.
- **Harvest** — reduzir investimento, preservar operação rentável e revisar em data definida.
- **Retire** — encerrar sem sucessor próprio ou transferir o job para outra solução.

Nenhuma delas é automaticamente superior.

## Workflow

1. **Establish the trigger**
   - crescimento;
   - retenção;
   - margem;
   - suporte;
   - dívida técnica;
   - risco/compliance;
   - mudança de mercado;
   - estratégia corporativa;
   - pressão interna.

   Separar sinais externos de preferências internas.

2. **Diagnose lifecycle**
   Avaliar evidências como:
   - tendência de receita/uso;
   - retenção e frequência;
   - capacidade de defender share;
   - custo de manutenção;
   - reclamações e workarounds;
   - mudança tecnológica;
   - alternativas e substitutos;
   - importância estratégica.

   Dados insuficientes viram assumptions, não certeza.

3. **Test the cheapest credible play**
   Antes de replace/retire, testar se uma extensão razoável resolve a pressão:
   - melhoria específica;
   - novo packaging;
   - canal;
   - integração;
   - redução de custo;
   - simplificação.

   Se não resolver, registrar por quê.

4. **Compare plays**
   Para cada opção relevante, explicitar:
   - valor preservado/criado;
   - custo;
   - risco;
   - tempo;
   - dependências;
   - impacto sobre clientes;
   - impacto operacional;
   - reversibilidade.

5. **If replacing**
   Tratar sucessor e produto legado como dois sistemas concorrendo por atenção:
   - GTM do novo;
   - migração;
   - compatibilidade;
   - data portability;
   - dual-run quando necessário;
   - suporte;
   - incentivos;
   - kill/revisit gates.

6. **If retiring**
   Definir:
   - owner executivo;
   - inventário de usuários/clientes;
   - contratos e obrigações;
   - datas;
   - comunicação;
   - alternativas;
   - export/migração de dados;
   - suporte de transição;
   - desativação técnica;
   - pós-EOL review.

7. **Communication sequence**
   Adaptar por stakeholder:
   - equipe interna;
   - vendas/suporte;
   - parceiros;
   - clientes críticos;
   - base geral.

   Mensagem deve explicar o que muda, quando, impacto, opções e suporte disponível.

8. **Decision gate**
   Registrar:
   - decisão;
   - evidência;
   - assumptions;
   - riscos;
   - data de revisão;
   - condição que faria reabrir a decisão.

## EOL readiness

Antes de anunciar retirada, verificar:
- obrigações contratuais e regulatórias;
- dependências técnicas;
- integrações;
- dados/export;
- clientes críticos;
- suporte e documentação;
- plano para incidentes durante migração;
- owner e calendário;
- critério observável de conclusão.

## Guardrails

- flat growth não prova decline;
- dívida técnica isolada não justifica replacement;
- rewrite é uma aposta, não um diagnóstico;
- EOL não termina no anúncio;
- migração precisa ser tratada como produto;
- não usar score único para automatizar decisão;
- não retirar funcionalidade crítica sem mapear dependências e obrigações.

## Integração

Combina com:
- `product-management-cycle`;
- `go-to-market-strategy`;
- `stakeholder-strategy`;
- `decision-analysis`;
- `product-metrics-diagnostics`;
- `after-action-review`;
- `production-go-live`.

## Provenance

Adaptada de `deanpeters/Product-Manager-Skills`, em especial `lifecycle-play-advisor`, `product-lifecycle-plays` e `eol-process`. Preserva diagnóstico antes da escolha, as opções extend/replace/retire/harvest, viés pelo teste menos custoso e EOL como processo completo. Remove dependência de skills auxiliares da fonte e thresholds universais.
