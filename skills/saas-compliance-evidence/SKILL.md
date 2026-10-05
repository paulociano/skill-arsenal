---
name: saas-compliance-evidence
description: "Projetar controles e evidências de compliance contínuo para SaaS com escopo, versões de frameworks, mapeamento requisito-controle, testes, exceções, drift e revisão humana, sem confundir scanner com certificação."
---

# SaaS Compliance Evidence

## Objetivo e fronteira
Transformar requisitos estabelecidos em controles testáveis e evidências rastreáveis. Usar para preparar auditorias técnicas, due diligence, matrizes de controles e compliance contínuo de SaaS.

Delegar cálculo de SLI/SLO e alertas a software-observability-engineering; dependências e artefatos a software-supply-chain-engineering; vulnerabilidades de código e fluxos pessoais a secure-code-privacy-review; SLA de tickets a support-operations-engineering. Não duplicar esses workflows nem inferir obrigação legal.

## Workflow
1. **Delimitar:** registrar produto, ambiente, conta/região, tenants, ativos, dados, responsabilidade do fornecedor/cliente e período. Identificar requisitos contratuais e frameworks com versão e fonte oficial atual. Mapear o que é aplicável, não aplicável com justificativa e ainda desconhecido.
2. **Definir controle:** para cada requisito registrar ID, risco, controle, owner, teste, frequência, evidência exigida e limite de cobertura. Um check pode apoiar vários requisitos sem provar nenhum integralmente.
3. **Planejar coleta:** usar exports ou APIs somente quando disponíveis e autorizados, com acesso mínimo. Registrar ferramenta/regra/versão, fonte, recurso, horário UTC, período, cobertura e erros de coleta. Redigir dados sensíveis e restringir acesso/retencão das evidências.
4. **Avaliar:** distinguir desenho do controle de funcionamento durante o período. Classificar cada teste como pass, fail, error, not-applicable ou not-tested. Não converter erro de permissão, recurso ausente ou dado velho em aprovação. Um snapshot não demonstra eficácia contínua.
5. **Aplicar políticas quando cabível:** separar avaliação de enforcement. Testar regras em audit/dry-run e casos permitidos/proibidos antes de bloquear deploys ou admissão. Declarar comportamento em indisponibilidade do motor; evitar que a política derrube operações essenciais. Não presumir Kubernetes ou qualquer vendor.
6. **Tratar gaps:** priorizar exposição e impacto; registrar evidência, owner, prazo e reteste. Exceções exigem escopo, justificativa, responsável autorizado, controle compensatório e expiração. Não remediar infraestrutura por inferência de um relatório.
7. **Detectar drift:** comparar baseline versionada e inventário observado; preservar histórico de alterações, revisão e exceções. Definir cadência e gatilho; criar automação apenas com ferramenta real e autorização compatível.
8. **Entregar:** matriz de controles, pacote de evidências com proveniência, gaps, exceções e cobertura desconhecida. Atestados/certificações e conclusões jurídicas permanecem sob revisão competente.

## Contrato mínimo de evidência
Registrar: control_id, framework/version, resource_scope, owner, test/version, collected_at, period, result, evidence_ref, coverage_limit, reviewer e exception_expiry quando aplicável. Manter referência restrita à prova; não copiar secrets/PII para Git ou relatórios públicos.

Controles de disponibilidade devem apontar para o contrato/versão, relatório SLI, regras de exclusão e incidentes reconciliados. Nunca criar créditos, exclusões ou compromissos de SLA sem fonte contratual. Inventário de endpoints, eventos de runtime e secrets management são fontes parciais, não provas globais de conformidade.

## Verificação
- Um teste sem permissão produz error/not-tested, com lacuna visível.
- Evidência fora do período ou sem escopo é insuficiente.
- Exceção vencida reaparece como gap.
- Check aprovado não promove automaticamente requisito/framework inteiro a conforme.
- Política nova distingue audit de enforcement e demonstra casos de permitir/negar.
- Toda conclusão aponta para evidência e informa cobertura não verificada.

## Dependências e segurança
Nenhum scanner é obrigatório ou instalado por esta skill. Execução exige ambiente, credenciais e permissões reais. Coletores cloud/endpoints podem ler metadados sensíveis; scanners ativos podem alterar sistemas; remediação requer autorização específica. Usar menor privilégio, proteção de evidências e revisão da edição/licença antes de selecionar software.

## Fontes
Metodologia adaptada de [Prowler](https://github.com/prowler-cloud/prowler), [CloudQuery](https://github.com/cloudquery/cloudquery), [ComplianceAsCode](https://github.com/ComplianceAsCode/content), [OpenSCAP](https://github.com/OpenSCAP/openscap), [OPA](https://github.com/open-policy-agent/opa), [Gatekeeper](https://github.com/open-policy-agent/gatekeeper) e [Kyverno](https://github.com/kyverno/kyverno). O contrato de evidência e as fronteiras acima são síntese do Arsenal; não declarações de recursos universais desses produtos. Revisões consultadas: ../../evaluations/2026-10-05-saas-sla-compliance-repositories.md.
