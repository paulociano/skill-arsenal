---
name: synthetic-test-data-engineering
description: "Gerar dados sintéticos e fixtures reproduzíveis para desenvolvimento, demos e testes de apps, com schemas, seeds, relacionamentos, distribuições, casos extremos, privacidade e validação."
---

# Synthetic Test Data Engineering

## Objetivo
Construir dados fictícios mas estruturalmente verossímeis para testar fluxos, povoar protótipos e revelar comportamentos de sistemas, sem confundir amostra sintética com evidência real.

## Trigger
Use quando o usuário pedir massa de teste, seed de banco, mock de CRM, fixtures, dados fake localizados, cenários de carga ou dataset sintético. Para métricas reais e inferência estatística, não substituir dados reais por Faker.

## Método
1. Identificar domínio, finalidade (demo, UI, regressão, integração, performance), schema, regras de validação, volume e campos sensíveis.
2. Escolher geradores conforme runtime: Faker.js para JS/TS, bibliotecas disponíveis para Python, ou geração explícita por código; não pressupor dependência instalada.
3. Fixar seed e versão da biblioteca. Registrar relógio/base date para determinismo de timestamps e testes de snapshot; evitar números aleatórios globais que vazem entre testes.
4. Gerar IDs estáveis e relacionamentos coerentes entre entidades (FK, cardinalidade, unicidade, limites financeiros, datas ordenadas, status permitidos).
5. Definir distribuição e segmentos intencionais: comuns, raros, nulos, extremos, inválidos para testes negativos, nomes/endereços brasileiros quando relevante. Não usar valores igualmente aleatórios se isso destruir a plausibilidade do cenário.
6. Separar casos de sucesso, erros e adversariais. Acrescentar ao menos um teste de invariantes e integridade referencial.
7. Validar shape, schema, localização, volume, seed, repetibilidade e cobertura. Comparar amostra produzida ao contrato, não apenas contar linhas.
8. Marcar e isolar ambiente sintético. Garantir que emails/telefones/domínios não causem mensagens reais, cobranças ou envios de webhook; usar domínios reservados e endereços de teste apropriados.
9. Entregar generator, seed, dataset e instrução de reset quando o usuário pedir artefatos executáveis. Nunca apresentar dados simulados como clientes, resultados ou métricas observadas.

## Ferramentas e fronteiras
- `@faker-js/faker` é referência para Node/browser, não ferramenta já instalada.
- A documentação da branch `next` pode divergir da API estável; pin de versão e consulta à documentação compatível são necessários.
- Evitar gerar dados sensíveis a partir de PII real; anonimização exige modelo de ameaça próprio e não é substituída por nomes falsos.
- Em testes de produção, usar ambiente segregado, permissões mínimas e limpeza segura.

## Acceptance
Should-trigger: "Povoe um CRM de demonstração com 5 mil contatos e histórico coerente, reproduzível por seed".
Near-miss: "Analise o crescimento real da minha carteira de clientes".
Verificar seed repetível, IDs/FKs válidos, campos obrigatórios, invariantes, isolamento de comunicações externas e sinalização ostensiva de dados simulados.

## Proveniência
Adaptada da metodologia e da ferramenta https://github.com/faker-js/faker, consultada em 2026-10-15. Sem dependência obrigatória de pacote ou runtime específico.
