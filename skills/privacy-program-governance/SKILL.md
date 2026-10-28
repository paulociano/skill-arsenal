---
name: privacy-program-governance
description: "Estruturar e revisar um programa de proteção de dados pessoais: inventário e registro de operações, base legal, minimização, relatório de impacto, direitos dos titulares, incidentes, operadores e transferências, ancorado na lei vigente (LGPD e outras) e sem emitir parecer jurídico."
---

# Privacy Program Governance

## Objetivo

Organizar como uma empresa ou profissional coleta, usa, compartilha e protege dados pessoais, produzindo evidências defensáveis e decisões práticas. O foco é governança e processo, não o código (para código, use `secure-code-privacy-review`).

Origem metodológica: agente `data-privacy-officer` de msitarzewski/agency-agents (MIT), adaptado. O original é centrado em GDPR/CCPA e usa prazos e artigos europeus; esta versão exige ancorar as obrigações na legislação aplicável ao caso (no Brasil, a LGPD e a regulamentação da ANPD) e verificar o texto vigente antes de citar artigo ou prazo.

## Quando usar

- mapear dados pessoais tratados por uma operação (clientes, leads, colaboradores);
- escolher e documentar a base legal de cada finalidade;
- decidir se é preciso relatório de impacto (RIPD ou DPIA) e montá-lo;
- criar o fluxo de atendimento a pedidos de titulares (acesso, correção, eliminação, portabilidade, oposição);
- preparar resposta a incidente de segurança com dados pessoais;
- avaliar fornecedores e compartilhamentos, inclusive transferência internacional.

Não usar para:
- revisar implementação em código ou diff: `secure-code-privacy-review`;
- auditar evidências de conformidade de SaaS (SOC 2 e similares): `saas-compliance-evidence`;
- parecer jurídico vinculante: encaminhar a advogado especializado.

## Ancoragem na lei (obrigatório)

Antes de citar obrigação, artigo, prazo ou autoridade, identificar a jurisdição aplicável (onde estão os titulares, onde atua o controlador) e consultar o texto e a regulamentação vigentes em fonte oficial. No Brasil, partir da LGPD (Lei nº 13.709/2018) e das normas da ANPD, verificando em especial os prazos de comunicação de incidente, o papel do encarregado, o registro das operações e os casos de relatório de impacto. Se não for possível verificar, declarar a limitação em vez de citar de memória.

## Workflow

1. **Delimitar o escopo:** quem trata, quais titulares, quais finalidades, em quais sistemas.
2. **Inventário e fluxo de dados:** categorias de dado (marcar os sensíveis), origem, finalidade, onde é guardado, com quem é compartilhado (operadores e terceiros), prazo de retenção, medidas de segurança. É a base do registro das operações.
3. **Minimizar primeiro:** para cada campo, perguntar se é necessário para a finalidade. O dado que não é coletado não precisa ser protegido.
4. **Base legal por finalidade:** registrar a base escolhida e por quê. Consentimento é revogável e deve ser específico e livre; avaliar se outra base, como execução de contrato, obrigação legal ou legítimo interesse (com teste de balanceamento documentado), é mais adequada. Dados sensíveis têm hipóteses próprias.
5. **Relatório de impacto:** recomendar quando houver tratamento de alto risco (dados sensíveis em escala, decisões automatizadas relevantes, monitoramento, dados de crianças); descrever riscos, medidas e risco residual, antes do início do tratamento.
6. **Direitos dos titulares:** definir canal, verificação de identidade, responsável, prazos legais e modelo de resposta; registrar cada pedido e a decisão.
7. **Incidentes:** plano com detecção, contenção, avaliação de risco ao titular, decisão de comunicação à autoridade e aos titulares dentro do prazo vigente, e registro. Nunca orientar a ocultar ou retardar avaliação para evitar comunicação.
8. **Operadores e transferências:** contrato com obrigações de proteção, avaliação do fornecedor e mecanismo válido para transferência internacional.
9. **Governança:** responsável designado, políticas curtas e aplicáveis, treinamento, revisão periódica e registro de decisões como se fossem ser auditadas.

## Saída padrão

Conforme o pedido: tabela de inventário e base legal, checklist de relatório de impacto, fluxo de atendimento a titulares, plano de resposta a incidente, lista de ações por prioridade com responsável e prazo. Citar as fontes legais consultadas e a data da consulta.

## Limites

- Não é aconselhamento jurídico; indicar quando é preciso advogado ou o encarregado.
- Não recomendar coletar mais dados do que a finalidade exige, nem obstruir pedidos válidos de titulares.
- Não registrar dados pessoais reais dentro dos documentos de governança além do necessário; usar categorias e referências.
- Dados de clientes de consultoria financeira costumam incluir informações patrimoniais; tratar com sigilo reforçado e acesso mínimo.
