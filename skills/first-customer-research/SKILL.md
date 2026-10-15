---
name: first-customer-research
description: Pesquisar potenciais primeiros clientes, beta users ou design partners a partir de sinais públicos recentes, qualificando dor, fit, timing, alcance e evidência sem tratar prospect como comprador confirmado nem automatizar outreach.
---

# First Customer Research

## Objetivo
Encontrar empresas ou profissionais plausíveis para validação inicial de um produto usando sinais públicos verificáveis de dor, timing e fit.

## Workflow
1. Entenda o produto:
   - outcome;
   - usuário;
   - comprador;
   - ticket ou motion;
   - geografia;
   - caso de uso principal;
   - desqualificadores.
2. Defina um ICP principal e um adjacente.
3. Monte queries por sinais públicos como:
   - pedidos explícitos por ferramenta ou alternativa;
   - workflows manuais;
   - reclamações recorrentes;
   - migração/churn;
   - lançamento, contratação, expansão ou mudança operacional relevante.
4. Use busca como descoberta, mas abra a fonte original antes de qualificar.
5. Registre separadamente:
   - data da publicação;
   - data em que a evidência foi verificada.
6. Para cada prospect, avalie:
   - força da dor;
   - fit do produto;
   - timing;
   - alcance público adequado;
   - qualidade da evidência.
7. Remova duplicatas, sinais resolvidos, sellers disfarçados de buyers e candidatos sem evidência suficiente.
8. Nunca preencha quota com matches fracos.
9. Se o usuário pedir copy de outreach, escreva uma abertura curta baseada na dor observada e em CTA de baixa fricção, mas não envie.
10. Entregue shortlist, padrões recorrentes, limitações e próximos passos de validação.

## Evidência mínima
Um prospect primário precisa ter:
- entidade identificável;
- fonte original;
- sinal relevante;
- data;
- ligação clara entre sinal e produto;
- cautela ou contraevidência quando existir.

## Privacidade
Use apenas informação profissional ou empresarial pública e intencionalmente compartilhada. Não use:
- data brokers;
- emails pessoais descobertos;
- telefones enriquecidos;
- grupos privados;
- atributos sensíveis;
- inferências de vulnerabilidade.

## Guardrails
- Prospect não é cliente confirmado.
- Interesse público não equivale a consentimento para publicidade.
- Score é prioridade de pesquisa, não probabilidade de conversão.
- Não envie mensagens, formulários ou conexões sem pedido separado e autorização explícita.

## Relação com outras skills
Use `niche-research` para pesquisa temática, `customer-interview` para validação qualitativa e `brand-strategy` ou `founder-diagnose` para refinar ICP/posicionamento quando necessário.

## Origem adaptada
Metodologia inspirada em `Kappaemme-git/codex-first-customer-finder-skill`, removendo dependência de scripts locais, workspace/state obrigatório e artefatos específicos.

## Qualificação de empresas por fontes públicas (BrowserAct, 2026-10-15)

Quando a pesquisa envolver estabelecimentos, marketplaces ou perfis empresariais, executar o percurso: **identidade da empresa → site oficial → sinal atual de dor/fit → canal empresarial publicamente indicado → verificação cruzada**. Para cada candidato, registrar nome, região, domínio, fonte, data do sinal, verificação, confiança da identidade e possíveis homônimos. Mapas, buscadores, páginas sociais e diretórios servem para descoberta, não validação final isolada. Não inferir email pessoal, extrair contatos privados, vincular perfis homônimos sem evidência ou automatizar outreach. Contribuição pública no GitHub não significa consentimento comercial.

Origens adaptadas: BrowserAct google-maps-contact-extract, business-contact-social-links-skill, industry-key-contact-radar-api-skill, github-project-contributor-finder-api-skill, youtube-channel-business-email.


## Qualificação explicável e estratégia de contato (ComposioHQ, 2026-10-15)

Para listas de leads, definir ICP e desqualificadores antes da busca. Para cada empresa, distinguir evidência de fit (setor, tamanho, stack verificada), dor atual, timing (contratação, expansão, mudança), capacidade potencial de compra quando observável e contato empresarial explicitamente público. Pontuação 1–10, quando pedida, é priorização heurística com justificativa e confiança, nunca probabilidade de compra. Separar sinais corroborados de inferências; não preencher quotas com falsos positivos. Entregar uma hipótese de abordagem personalizada que reflita problema observável e sem envio automático. Adaptada de ComposioHQ/awesome-claude-skills/lead-research-assistant, sem diretório local obrigatório ou data brokers.


## Deduplicação e enriquecimento prudente de prospecção (ComposioHQ 62–91, 2026-10-15)

Ao integrar pesquisa de empresas com CRM ou serviço de prospecção autorizado, identificar a organização preferencialmente por domínio canônico validado e identificador da fonte, antes de associar profissionais por cargo. Busca de empresa pode não trazer domínio; validar em fonte primária antes de cruzar registros. Distinguir contato descoberto, canal corporativo comprovado e informações pessoais, que não devem ser enriquecidas ou reveladas automaticamente. Em listas já existentes, procurar registros antes de criar novos; uma operação com sucesso parcial não equivale a todos os contatos enriquecidos. Registrar tamanho real do lote, conflitos de identidade, registros faltantes e custos observáveis. Alterar estágio de CRM apenas quando houver conexão ativa, IDs atuais e autorização explícita; a busca pública não legitima envio nem armazenamento de dados pessoais de terceiros. Método adaptado de ComposioHQ/awesome-claude-skills/composio-skills/apollo-automation, sem importação do Rube MCP.
