---
name: job-opportunity-monitoring
description: "Monitorar vagas ao longo do tempo como um diff de oportunidades, normalizando fontes, detectando novas/fechadas/reabertas, ranqueando fit com critérios explícitos e disparando alertas somente quando há mudança relevante."
---

# Job Opportunity Monitoring

## Objetivo

Transformar busca de vagas em um sistema recorrente de mudanças observáveis, em vez de uma sequência de buscas manuais independentes.

O owner desta skill é:
- acompanhar fontes de vagas ao longo do tempo;
- distinguir vaga nova, ainda aberta, fechada e reaberta;
- comparar oportunidades com perfil/critério do usuário;
- separar regras determinísticas de elegibilidade do julgamento semântico;
- entregar alertas/digests somente quando houver mudança útil.

## Quando usar

Use quando o usuário quiser:
- acompanhar empresas específicas ou categorias de vagas;
- receber alertas recorrentes de novas oportunidades;
- comparar vagas contra currículo/perfil;
- manter histórico de abertura/fechamento;
- gerar shortlist periódica de oportunidades.

Para uma busca única de vagas atuais, use a ferramenta de oportunidades disponível no produto sem ativar necessariamente esta skill.
Para automação futura, combine com `automations` quando o ambiente suportar agendamento/condições.

## Princípio central

**O sistema monitora mudança, não apenas resultados.**

Cada oportunidade precisa de identidade estável suficiente para que o próximo ciclo saiba se ela é:
- nova;
- já conhecida;
- fechada;
- reaberta;
- alterada materialmente.

## Workflow

1. **Define target**
   - funções/títulos;
   - senioridade aceitável;
   - localização/remoto;
   - empresas prioritárias;
   - skills/domínios;
   - restrições duras;
   - frequência de monitoramento.

2. **Normalize sources**
   - cada fonte pode ter schema diferente;
   - normalize pelo menos empresa, título, URL, localização, descrição, status, data/fonte quando disponível;
   - preserve o identificador nativo quando confiável;
   - quando não houver, derive um ID estável de campos que não mudam facilmente.

3. **Establish baseline**
   - primeira captura de uma fonte não deve gerar uma enxurrada de "novas" vagas por padrão;
   - registre o estado inicial e comece a alertar a partir de mudanças subsequentes, salvo se o usuário pedir backfill.

4. **Diff**
   - nova: ID nunca visto;
   - aberta: vista novamente;
   - fechada: ausente somente quando a fonte foi consultada com sucesso;
   - reaberta: ID conhecido volta após status fechado;
   - erro de fetch não prova fechamento.

5. **Cheap deterministic gates**
   - aplique regras duras em código/lógica antes ou depois do julgamento semântico, conforme o caso;
   - exemplos: senioridade proibida, localização incompatível, autorização de trabalho, faixa salarial mínima, tipo de contrato;
   - uma regra determinística deve operar sobre dados confiáveis e ter precedência explícita.

6. **Semantic fit**
   - compare vaga e perfil por dimensões separadas, por exemplo:
     - skills;
     - senioridade;
     - domínio;
     - localização;
     - recência;
     - alcance/stretch;
   - score é ordenação, não veredito;
   - preserve uma razão curta e as dimensões para auditoria.

7. **Reconcile**
   - se regra dura e modelo divergirem, a política precisa dizer qual vence;
   - não esconda mismatch numa média;
   - ausência de dado não equivale automaticamente a fit ruim.

8. **Budget**
   - avalie apenas vagas novas ou materialmente alteradas quando possível;
   - use batching somente se o backend real suportar sem perder rastreabilidade;
   - reserve capacidade para alerts/digest quando houver teto de tokens/custo;
   - pare de forma limpa ao atingir o budget e retome no próximo ciclo.

9. **Notify**
   - alertas rápidos apenas para eventos realmente novos/relevantes;
   - digest periódico para exploração ampla;
   - canais independentes não devem consumir o estado um do outro;
   - nada novo significa nenhuma notificação.

10. **Review**
    - acompanhe falsos positivos/negativos da priorização;
    - ajuste critérios determinísticos antes de inflar prompts;
    - preserve casos rotulados para comparar mudanças de modelo/regra.

## Identidade e estado

O estado persistido deve, quando o ambiente permitir, manter:
- stable ID;
- source/company;
- first_seen;
- last_seen;
- open/closed;
- last material change;
- fit score + breakdown + version;
- alerted/digested separadamente;
- fetch success/failure por fonte.

Não apagar vagas fechadas imediatamente se isso impedir reconhecer repost/reopen.

## Currículo e perfil

Quando usar currículo:
- trate-o como fonte privada do usuário;
- extraia somente informações necessárias para o fit;
- não invente experiência ausente;
- sinalize truncamento/parse ruim;
- não envie o currículo a terceiros sem necessidade e autorização compatível com o fluxo.

## Regras de segurança e precisão

- não armazenar senhas de e-mail/API em texto de skill ou logs;
- não marcar todas as vagas como fechadas quando uma fonte falha;
- não tratar data de "updated" como data de publicação sem verificar;
- não assumir que score alto implica chance de contratação;
- não contornar bot protection, paywalls ou controles de acesso de forma indevida;
- respeitar termos e limites de cada fonte;
- um alerta não deve ser enviado em massa no primeiro baseline sem intenção explícita.

## Saída

Uma execução pode entregar:
- novas vagas desde o último ciclo;
- fechadas/reabertas;
- shortlist por fit;
- razões e dimensões de fit;
- mudanças relevantes;
- fontes com erro;
- resumo do budget/limites;
- próximo ciclo ou automação, quando aplicável.

## Integração

Combina com:
- `automations`;
- `decision-analysis`;
- `structured-output-contract`;
- `llm-observability-evaluation`;
- `verify-before-claim`.

## Provenance

Metodologia adaptada de [suvamneog/jobradar](https://github.com/suvamneog/jobradar), preservando diff temporal, baseline, stable IDs, gates determinísticos, ranking semântico auditável, budgets e filas de notificação independentes. Foram removidas dependências de launchd, SMTP/Gmail, SQLite, ATS adapters específicos e providers/modelos particulares.
