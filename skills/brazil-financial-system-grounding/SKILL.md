---
name: brazil-financial-system-grounding
description: "Ancorar tarefas financeiras brasileiras em fontes atuais e oficiais do BCB, CVM, Tesouro Nacional, Receita e Open Finance Brasil, incluindo Pix, taxas, títulos, dados públicos e regras, sem congelar normas que mudam."
---

# Brazil Financial System Grounding

## Objetivo

Garantir que análises e implementações financeiras brasileiras usem fonte, versão, data e jurisdição corretas.

## Quando usar

- Pix;
- Open Finance Brasil;
- Bacen/BCB data;
- CVM filings/funds;
- Tesouro/Tesouro Direto;
- Selic, IPCA e indicadores brasileiros;
- regras tributárias/previdenciárias brasileiras;
- produtos financeiros regulados no Brasil.

## Source hierarchy

Preferir, conforme o tema:
1. Banco Central do Brasil;
2. CVM;
3. Tesouro Nacional;
4. Receita Federal;
5. legislação/Diário Oficial quando norma for material;
6. Open Finance Brasil para specifications;
7. B3 quando market infrastructure/data for aplicável;
8. secondary libraries apenas como adapters.

## Workflow

1. Identificar:
   - tema;
   - data de referência;
   - pessoa física/jurídica;
   - jurisdição Brasil;
   - produto/mercado.

2. Localizar fonte oficial atual.

3. Registrar:
   - versão/release;
   - data;
   - vigência;
   - endpoint/document;
   - status draft/stable quando houver.

4. Adaptar cálculo/integração somente depois do grounding.

5. Para APIs:
   - schemas;
   - auth/consent;
   - permissions;
   - environment;
   - idempotency;
   - security manual separado da OpenAPI quando indicado.

6. Para dados:
   - série/identificador;
   - unidade;
   - periodicidade;
   - revision policy;
   - timezone/date.

7. Para regras:
   - separar regra vigente de proposta;
   - não inferir de blog/tutorial;
   - usar `tax-financial-modeling` quando houver cálculo tributário.

## Pix

- usar especificação/release oficial atual do BCB;
- cobrança, recorrência, payload e endpoints precisam seguir versão real;
- segurança/autorização não deve ser inferida apenas da OpenAPI;
- ações live exigem ambiente, credenciais e autorização explícita.

## Open Finance Brasil

- consentId, permissions e token scopes são parte do contract;
- usar versão vigente da API;
- specs draft não equivalem a produção;
- minimizar dados conforme consentimento.

## CVM/Tesouro

- dados públicos podem sofrer atualização/reprocessamento;
- filings/fundos exigem período e identificador claros;
- adapters como filings-cvm/tesouropy são conveniência, não fonte de autoridade.

## Regras

- não hardcodar Selic, limites, alíquotas ou regras correntes em uma skill permanente;
- sempre buscar valor/regra atual quando material;
- não extrapolar regra brasileira para outro país;
- implementação de pagamento/open finance exige security review específico.

## Integração

`fixed-income-analysis`, `tax-financial-modeling`, `financial-filings-analysis`, `payment-billing-operations`, `banking-ledger-engineering`, `retirement-income-planning`, `personal-financial-planning`.

## Provenance

Consolidada de bacen/pix-api, OpenBanking-Brasil/openapi e all-services-repo, CVM open-data adapters e StrategicProjects/tesouropy. Fontes secundárias servem como adapters; BCB/CVM/Tesouro/Receita permanecem autoridade.
