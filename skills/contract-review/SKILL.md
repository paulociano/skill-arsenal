---
name: contract-review
description: "Revisar contratos (prestação de serviço, consultoria, NDA, parceria, fornecedor, termos de uso) do ponto de vista de uma parte: checklist ou parecer com riscos por cláusula, posições de negociação e comentários sem alterar o texto, sem substituir advogado."
---

# contract-review

## Objetivo

Ajudar a entender e negociar um contrato antes de assinar: o que ele obriga, onde está o risco para a parte representada e o que pedir em troca, com rastreabilidade até a cláusula.

## Quando usar

- "Revisa esse contrato", "posso assinar?", "o que devo negociar?", "compara essas duas versões".
- Contratos de prestação de serviço, consultoria, representação comercial, NDA, parceria, fornecedor, SaaS/termos de uso, locação comercial simples.

## Quando não usar

- Litígio, defesa em processo, questão criminal, trabalhista com risco alto, societário complexo, M&A → advogado.
- Privacidade e tratamento de dados como programa → `privacy-program-governance` (aqui só a cláusula).
- Gerar contrato do zero para uso real sem revisão profissional.

## Aviso fixo

Começar e terminar com: **não é parecer jurídico; para decisões relevantes, consulte um advogado habilitado na jurisdição do contrato.** Lei e jurisprudência mudam; ao citar norma (Código Civil, CDC, LGPD, CLT etc.), conferir a versão vigente na fonte oficial antes de afirmar.

## Workflow

1. **Completude.** Documento inteiro, anexos, versão e data. Faltando parte, dizer o que falta e limitar a análise.
2. **Perspectiva.** De qual lado o usuário está (contratante ou contratado, comprador ou fornecedor)? Toda avaliação de risco é a partir desse lado. Se não estiver claro, perguntar.
3. **Modo.**
   - *Checklist:* tabela item × status (ok / ausente / problema) × observação.
   - *Parecer:* avaliação geral (verde/amarelo/vermelho), resumo em 3–5 pontos, problemas por cláusula com risco, sugestão de redação e posição de recuo.
   - *Comparação:* o que mudou entre versões e quem ganha ou perde com cada mudança.
4. **Quatro camadas de leitura.**
   - **Partes:** razão social, CNPJ/CPF, representante com poderes, consistência entre preâmbulo e assinaturas.
   - **Básico:** objeto, prazo, vigência e renovação, valores e forma de pagamento, datas e anexos consistentes, definições.
   - **Comercial:** escopo e entregáveis, critérios de aceite, prazos de pagamento e multa por atraso, reajuste e índice, exclusividade, metas, mudanças de escopo, despesas.
   - **Jurídico:** responsabilidade e limite de indenização, multas e cláusula penal (proporcionalidade), rescisão (motivos, aviso prévio, efeitos), propriedade intelectual e direito de uso, confidencialidade (prazo, exceções), não concorrência e não aliciamento (prazo, território, contrapartida), proteção de dados, foro ou arbitragem, lei aplicável, cessão, caso fortuito, garantias, renúncia de direitos.
5. **Sinais de alerta comuns.**
   - obrigações ou multas só de um lado; indenização ilimitada para uma parte;
   - renovação automática longa sem janela clara de saída;
   - rescisão sem motivo só para uma parte, ou sem aviso prévio;
   - cessão total de propriedade intelectual sem preço ou sem exceção para o know-how prévio;
   - não concorrência ampla sem prazo, território ou contrapartida;
   - prestação de serviço com subordinação, horário fixo e pessoalidade (risco de vínculo empregatício);
   - pagamento condicionado a "aprovação" sem critério; reajuste sem índice;
   - foro distante da parte mais fraca; arbitragem cara para valores pequenos.
6. **Posições de negociação.** Para cada problema: redação preferida, posição de recuo aceitável e o que oferecer em troca. Priorizar poucos pontos de alto impacto.
7. **Entrega.** Em documento do usuário, preferir **comentários** a edições no texto; nunca alterar o original sem pedido. Idioma da saída = idioma do contrato, salvo pedido.

## Guardrails

- Citar a cláusula e o trecho que sustenta cada ponto; não inventar cláusula ausente.
- "Não encontrei" ≠ "não existe": dizer quando um tema pode estar em anexo não fornecido.
- Não tratar práticas de outro país como regra local.

## Integração

`negotiation-preparation`, `consulting-engagement-lifecycle`, `privacy-program-governance`, `document-extraction-pipeline`, `evidence-claim-verification`.

## Origem

Método adaptado de [skala-io/legal-skills](https://github.com/skala-io/legal-skills) (Apache-2.0; `contractor-agreement-review`: modos checklist/parecer, perspectiva do cliente, posições preferida e de recuo) e [LawMotion-AI/Vibe-Lawyering](https://github.com/LawMotion-AI/Vibe-Lawyering) (MIT; `contract-review`: comentários sem alterar o texto, quatro camadas de revisão, idioma do contrato), avaliados em 2026-11-10. Sinais de alerta reescritos para o contexto brasileiro; conferir a legislação vigente. Garantia `static_only`.
