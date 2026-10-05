---
name: software-supply-chain-engineering
description: "Governar dependências e supply chain de software com version pinning, automated updates, vulnerability/SBOM/secret/license scanning, artifact provenance e triage por reachability/impact."
---

# Software Supply Chain Engineering

## Objetivo

Reduzir risco de dependências, builds e artefatos de terceiros sem transformar scanners ou bots em autoridade automática.

## Quando usar

- dependency updates;
- Renovate/Dependabot-style automation;
- SBOM;
- vulnerability scanning;
- secret scanning;
- license scanning;
- container/IaC scanning;
- artifact provenance/signatures.

## Workflow

1. **Inventory**
   - dependencies;
   - direct/transitive;
   - images;
   - build tools;
   - package registries;
   - artifacts;
   - licenses.

2. **Pinning**
   - lockfiles;
   - digest/commit pinning where appropriate;
   - avoid floating production dependencies;
   - record source.

3. **Automated updates**
   - group compatible updates deliberately;
   - schedules;
   - automerge only for low-risk + green verification;
   - major updates require changelog/migration review;
   - rollback path.

4. **Scanning**
   - CVE/dependency;
   - secrets;
   - IaC/misconfig;
   - container/OS packages;
   - licenses;
   - SBOM generation when useful.

5. **Triage**
   - affected component;
   - version;
   - exploitability/reachability;
   - runtime exposure;
   - fix availability;
   - business impact;
   - false-positive evidence.

6. **Artifact integrity**
   - checksum/signature/provenance;
   - trusted registry;
   - immutable artifact;
   - build/release identity.

7. **CI gate**
   - severity alone is not enough;
   - define blocking policy;
   - exception with owner/expiry;
   - fail closed for secrets/critical provenance violations when justified.

8. **Monitor**
   - stale dependencies;
   - unsupported runtimes;
   - exception debt;
   - mean time to remediate.

## Regras

- scanner finding is evidence, not verdict;
- update bot PR is still code change;
- pinning can freeze vulnerabilities, so freshness also matters;
- secret found in history requires rotation, not only deletion;
- SBOM does not prove security;
- do not install scanners merely to inspect an external skill.

## Integração

`secure-code-privacy-review`, `skill-security-review`, `production-go-live`, `software-testing-engineering`, `code-review`.

## Provenance

Consolidada de Trivy, Renovate and Semgrep supply-chain/static-analysis patterns. Preserva automation + triage + provenance sem exigir seus serviços/CLIs.


## Evidência de artefato e seleção de scanners

- Vincular SBOM e relatório ao digest do artefato realmente promovido. Registrar formato, gerador/versão, escopo, horário e versão/frescor da base de vulnerabilidades; ausência de finding pode refletir cobertura incompleta.
- Verificar assinatura contra digest, identidade esperada e issuer/trust root permitido. Assinatura criptograficamente válida de uma identidade arbitrária não atende à política.
- Distinguir assinatura, inclusão em transparency log e proveniência das etapas. Verificar materiais/produtos, steps e executores autorizados quando atestados estiverem disponíveis; registro público não garante build seguro.
- Avaliar destino e visibilidade de metadados antes de publicar em transparency logs. Não publicar secrets, PII ou detalhes privados inadvertidamente.
- Tratar Scorecard por checks, data, revisão e cobertura, sem transformar nota agregada em garantia de segurança ou compliance.
- Verificar manutenção, licença da versão/edição e permissões reais antes de escolher ferramentas. READMEs consultados em 2026-10-05: tfsec orienta migração para Trivy; kube-hunter informa ausência de desenvolvimento ativo; Gitleaks informa releases futuras de security patches. Revalidar esses estados em novas adoções.
- Verificação online de credenciais encontradas pode chamar terceiros e usar secrets reais; exigir escopo autorizado, redigir resultados e priorizar revogação/rotação, não experimentação.
- Testar rejeição de digest divergente, identidade/issuer inesperado e evidência ausente. Distinguir scanner error de scan limpo.

Fontes adicionais: [Syft](https://github.com/anchore/syft), [Grype](https://github.com/anchore/grype), [Cosign](https://github.com/sigstore/cosign), [Rekor](https://github.com/sigstore/rekor), [in-toto](https://github.com/in-toto/in-toto) e [Scorecard](https://github.com/ossf/scorecard). Revisões em ../../evaluations/2026-10-05-saas-sla-compliance-repositories.md.
