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
