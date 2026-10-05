# Avaliação de 40 repositórios — SLA e compliance para SaaS

Data: 2026-10-05. Stack: arsenal-autopilot + revisão proporcional por skill-security-review.
Baseline do Arsenal: 14c1b35a2f946f3b887273eaf0ea0f802bbd892f.

## Escopo e evidência
Foram lidos os READMEs dos 40 repositórios da lista final da conversa. A tabela registra cada blob SHA consultado; o hash identifica o conteúdo, não uma release testada. Metadados/stars da pesquisa inicial são sinais de popularidade e não certificação de qualidade. updated_at não demonstra atividade de desenvolvimento. Não houve auditoria integral de código, licenças, releases, vulnerabilidades recentes ou validação de instalações. Consultar esses elementos antes de selecionar uma ferramenta para produção.

## Resultado e ownership
- CREATE_NEW: saas-compliance-evidence, skill A/B adaptada de sistemas D. Adiciona matriz requisito-controle-evidência, estados de teste, período/cobertura e exceções. Nenhum owner existente consultado cobria esse contrato; observabilidade, supply chain, revisão de código e SLA de suporte permanecem separados.
- UPDATE_EXISTING: software-observability-engineering recebe contrato SLI/SLO/SLA, matemática de orçamento e alertas multiwindow.
- UPDATE_EXISTING: software-supply-chain-engineering recebe ligação SBOM/digest, identidade/issuer de assinatura, atestados, limites de score e seleção de scanners.
- Índice atualizado; nenhuma stack adicional, instalação ou integração criada.

As fontes abaixo são classe D (software/runtime técnico). D/B indica metodologia absorvida além do software. Nenhuma é classificada C por ser um produto técnico, e nenhuma é declarada skill A pronta para importar. KEEP_EXTERNAL_REFERENCE significa cobertura existente ou ferramenta contextual, sem alteração causada por essa fonte. REJECT significa rejeitar nova adoção no Arsenal, não acusação de comportamento malicioso.

## Registro por fonte
| # | Fonte | Classe | Decisão | Owner | Capacidade, justificativa e dependências | README blob SHA |
|---|---|---|---|---|---|---|
| 1 | [prometheus/prometheus](https://github.com/prometheus/prometheus/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-observability-engineering | Coleta/consulta de métricas já coberta; requer servidor e targets. | 0465897e5cc16963a84fa6ba56b64b5dfa764009 |
| 2 | [prometheus/alertmanager](https://github.com/prometheus/alertmanager/blob/main/README.md) | D/B | UPDATE_EXISTING | software-observability-engineering | Agrupamento, inibição e silenciamento com responsabilidade; requer receivers. | 9c30662dde9fa2621d6b09d4a6953b000a9b0238 |
| 3 | [prometheus/blackbox_exporter](https://github.com/prometheus/blackbox_exporter/blob/master/README.md) | D/B | UPDATE_EXISTING | software-observability-engineering | Probes externos complementam medição interna; rede/targets autorizados. | 82ef9d29fb4321a6881c9bf02135673cd3a7494a |
| 4 | [grafana/grafana](https://github.com/grafana/grafana/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-observability-engineering | Dashboards já cobertos; backend e acesso a dados necessários. | 7b768e029f8ad89feae45d31bce9a57d42d9cf5c |
| 5 | [grafana/loki](https://github.com/grafana/loki/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-observability-engineering | Logs e labels já cobertos; storage, retenção e PII exigem operação. | 146c430b6ebe86fb9bb0ecd9b09dbb5823edbadc |
| 6 | [grafana/tempo](https://github.com/grafana/tempo/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-observability-engineering | Tracing já coberto; storage e propagação necessários. | 51f8ba21a7f381a15de7c5f9ce76b68f913b93ff |
| 7 | [open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-observability-engineering | Pipeline receive/process/export já incorporado; collectors/exporters reais. | 95bb0001d74b1415b0111e72f07ec2e806b80c0b |
| 8 | [open-telemetry/opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-observability-engineering | Demo de instrumentação, não template de produção; containers e serviços. | bd481aae43d4f9a017f486a85c4a56319568aa6f |
| 9 | [google/slo-generator](https://github.com/google/slo-generator/blob/master/README.md) | D/B | UPDATE_EXISTING | software-observability-engineering | Formalizar SLI, orçamento e burn rate; runtime Python/backends opcionais. | 056c81818e07bd74538385ff2197233e6f1d2e62 |
| 10 | [pyrra-dev/pyrra](https://github.com/pyrra-dev/pyrra/blob/main/README.md) | D/B | UPDATE_EXISTING | software-observability-engineering | SLOs e burn rates por janelas; Prometheus na implementação. | abc8a131d544c1fc8914494671f70f62d0ca776d |
| 11 | [slok/sloth](https://github.com/slok/sloth/blob/main/README.md) | D/B | UPDATE_EXISTING | software-observability-engineering | Alertas multiwindow/multiburn; geração de regras Prometheus. | 2a73355bf74e72effbef40b8e8efd2c185b4f01f |
| 12 | [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma/blob/master/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-observability-engineering | Uptime/status page complementar; hospedagem e conectividade. | d90d46c6563fcbeafb18477b695b4df215794b52 |
| 13 | [Netflix/chaosmonkey](https://github.com/Netflix/chaosmonkey/blob/master/README.md) | D | KEEP_EXTERNAL_REFERENCE | production-go-live | Chaos controlado como referência; dependências operacionais e interrupção deliberada, sem execução. | a97f19435da2b6ad5102f0f8b8797199e2dd4d21 |
| 14 | [osquery/osquery](https://github.com/osquery/osquery/blob/master/README.md) | D | KEEP_EXTERNAL_REFERENCE | saas-compliance-evidence | Evidência de host/inventário; agente e privilégios, não revisão de código. | a60d2f3bb4e8da5d7201ba105dd2bba6c928af16 |
| 15 | [fleetdm/fleet](https://github.com/fleetdm/fleet/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | saas-compliance-evidence | Postura de dispositivos; servidor/agentes e MDM, validar edição/licença. | d20a16c7b65f31229fc64e75f4b0892930b2719c |
| 16 | [prowler-cloud/prowler](https://github.com/prowler-cloud/prowler/blob/master/README.md) | D/B | ABSORB_METHOD_ONLY | saas-compliance-evidence | Checks mapeados a frameworks; separar controle, evidência e cobertura; credenciais cloud. | 2851101f05ed5e81527f12be23c61637c2ec9238 |
| 17 | [cloudquery/cloudquery](https://github.com/cloudquery/cloudquery/blob/main/README.md) | D/B | ABSORB_METHOD_ONLY | saas-compliance-evidence | Inventário e coleta de metadados como base do escopo; conectores/warehouse. | 494aab87c247e17be7ff2eb1fc8e6baab22062f3 |
| 18 | [bridgecrewio/checkov](https://github.com/bridgecrewio/checkov/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-supply-chain-engineering | IaC/SCA já cobertos; scanner e arquivos/configuração reais. | 46bac705728757d1f569bf8f6a8853645658e08a |
| 19 | [aquasecurity/tfsec](https://github.com/aquasecurity/tfsec/blob/master/README.md) | D | REJECT | software-supply-chain-engineering | Não adotar como nova capacidade: README orienta Trivy; manter referência de migração. | 8fa2cd0b4ee3df961fda4879e543abe6c5bde87d |
| 20 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-supply-chain-engineering | Scanner já incorporado; validar base de vulnerabilidades, versão e permissões. | 9ba2df0ea662b376ec36db33ed6a0120ae197b13 |
| 21 | [anchore/grype](https://github.com/anchore/grype/blob/main/README.md) | D/B | UPDATE_EXISTING | software-supply-chain-engineering | Registrar frescor da base e contexto do scan/SBOM; CLI e fontes de advisories. | 96767428109a45130594277f817c61c7ac26aa25 |
| 22 | [anchore/syft](https://github.com/anchore/syft/blob/main/README.md) | D/B | UPDATE_EXISTING | software-supply-chain-engineering | SBOM vinculada a digest/escopo; gerador CLI ou biblioteca. | d864e142875ca81737d5c94027bce41b838bead4 |
| 23 | [sigstore/cosign](https://github.com/sigstore/cosign/blob/main/README.md) | D/B | UPDATE_EXISTING | software-supply-chain-engineering | Verificar identidade/issuer e digest, não apenas assinatura; registry/trust roots. | 293d76bc813a579636e1030575ce604959b17615 |
| 24 | [sigstore/rekor](https://github.com/sigstore/rekor/blob/main/README.md) | D/B | UPDATE_EXISTING | software-supply-chain-engineering | Transparência não prova segurança; controlar publicação de metadados. | 2a81e440d473e70362f449638cc7ea9334fd1af8 |
| 25 | [in-toto/in-toto](https://github.com/in-toto/in-toto/blob/develop/README.md) | D/B | UPDATE_EXISTING | software-supply-chain-engineering | Etapas, materiais/produtos e executores autorizados; layouts/atestados. | 22d98a233e7a375c3da8c6781f1f142ccb31be0f |
| 26 | [ossf/scorecard](https://github.com/ossf/scorecard/blob/main/README.md) | D/B | UPDATE_EXISTING | software-supply-chain-engineering | Checks contextualizados e datados, sem autoridade da nota; API/CLI e permissões. | 5f290d6372cad5a32d51d77bdda4ed8b22288b4c |
| 27 | [renovatebot/renovate](https://github.com/renovatebot/renovate/blob/main/readme.md) | D | KEEP_EXTERNAL_REFERENCE | software-supply-chain-engineering | Atualização automatizada já incorporada; acesso a Git e registries. | 459384be19557f5cb0fa28b072afbe17f1198e9a |
| 28 | [semgrep/semgrep](https://github.com/semgrep/semgrep/blob/develop/README.md) | D | KEEP_EXTERNAL_REFERENCE | secure-code-privacy-review | SAST já coberto; regras/engine, validação de findings e licença da edição. | b3173abf26abb2f850807731959989b25eb8f8ea |
| 29 | [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks/blob/master/README.md) | D | KEEP_EXTERNAL_REFERENCE | software-supply-chain-engineering | Detecção de secrets já coberta; README limita novas releases a security patches. | 6bdd5d960fd9f81a5221819509c4e9f5cb7d251e |
| 30 | [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog/blob/main/README.md) | D/B | UPDATE_EXISTING | software-supply-chain-engineering | Verificação online de secrets requer autorização específica e controle de exposição. | 0a001e615024ca5bf185f84a31e9f27ee0c022e4 |
| 31 | [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | secure-code-privacy-review | DAST complementar; alvo e escopo autorizados, scanner ativo não executado. | e5efcf16bf926466a0dbb8e29f146884df227f05 |
| 32 | [aquasecurity/kube-bench](https://github.com/aquasecurity/kube-bench/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | saas-compliance-evidence | Benchmark Kubernetes como prova parcial; versão CIS/cluster e acesso ao host. | 52c8f8f56187728929213712a494f81f05259d53 |
| 33 | [aquasecurity/kube-hunter](https://github.com/aquasecurity/kube-hunter/blob/main/README.md) | D | REJECT | saas-compliance-evidence | Não adotar para novos fluxos: README declara sem desenvolvimento ativo; scanner ativo. | 17dc20ad4bb88247ad28057ba029485bf0255f25 |
| 34 | [kyverno/kyverno](https://github.com/kyverno/kyverno/blob/main/README.md) | D/B | ABSORB_METHOD_ONLY | saas-compliance-evidence | Políticas executáveis com teste/audit antes de enforcement; runtime de policy. | 11575c7e0ac68d2b585ab8ab388a9cc40dd25e78 |
| 35 | [open-policy-agent/opa](https://github.com/open-policy-agent/opa/blob/main/README.md) | D/B | ABSORB_METHOD_ONLY | saas-compliance-evidence | Decisão de política separada da aplicação; runtime Rego e dados de entrada. | 860399b5b7ac265f89508796831990a45eb485c4 |
| 36 | [open-policy-agent/gatekeeper](https://github.com/open-policy-agent/gatekeeper/blob/master/README.md) | D/B | ABSORB_METHOD_ONLY | saas-compliance-evidence | Constraints e auditoria/admissão; Kubernetes/CRDs e permissões. | 933b26be8cf1af8ce83b3231dbf9f6218e4f192b |
| 37 | [falcosecurity/falco](https://github.com/falcosecurity/falco/blob/master/README.md) | D | KEEP_EXTERNAL_REFERENCE | saas-compliance-evidence | Eventos de runtime como evidência parcial; Linux/kernel, agente e tuning. | 9fa6aeae085a904d5b74c6cee1a732ff68b1e5bf |
| 38 | [hashicorp/vault](https://github.com/hashicorp/vault/blob/main/README.md) | D | KEEP_EXTERNAL_REFERENCE | saas-compliance-evidence | Secrets/access audit como controle parcial; serviço, auth, operação e licença. | 90974651509752fbdb68b63db9d95b66fcd70eaf |
| 39 | [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content/blob/master/README.md) | D/B | ABSORB_METHOD_ONLY | saas-compliance-evidence | Conteúdo de políticas separado do motor; perfil/platform/version explícitos. | 0c55f58224eaef1d1302c67414219bc041381fbf |
| 40 | [OpenSCAP/openscap](https://github.com/OpenSCAP/openscap/blob/main/README.md) | D/B | ABSORB_METHOD_ONLY | saas-compliance-evidence | Avaliação SCAP e resultados rastreáveis; conteúdo compatível e acesso ao sistema. | 13c6f4551dc76513dcaedd2b0c5d9c59da72805e |

## Correções em relação à pesquisa inicial
- tfsec recomenda migração para Trivy; kube-hunter declara ausência de desenvolvimento ativo; Gitleaks declara apenas security patches futuros. Popularidade não justificava recomendação indiscriminada desses três.
- osquery e Fleet são fontes operacionais de endpoints; não foram absorvidos como métodos de revisão de código.
- SLA contratual, SLO operacional, suporte e compliance são fronteiras diferentes.
- google/sre, google/sre-workbook e Nobl9/ntk não pertencem à lista final dos 40 e não são usados como fontes verificadas.
- Nenhum scanner por si atesta SOC 2, ISO 27001, LGPD ou conformidade integral; não foram avaliadas obrigações jurídicas específicas.

## Segurança e portabilidade
Parecer: APPROVE para a adaptação documental delimitada; CAUTION para qualquer execução futura das ferramentas. Nenhum installer, scanner, agente, exploit, credential verification ou experimento de caos foi executado. A revisão foi estática/documental e não equivale a auditoria de segurança dos 40 produtos.
Credenciais cloud, acesso a endpoints, leitura de logs, publicação de atestados e scanners ativos exigem escopo e menor privilégio. Não copiar instruções de agentes/instaladores nem presumir ferramentas disponíveis. Binários, infraestrutura, MDM, registries, Kubernetes e serviços comerciais continuam dependências externas.
Licença/edição deve ser conferida na versão escolhida, especialmente em ferramentas com componentes comerciais; não se presume licença permissiva pelo repositório ser público.

## Casos de aceitação documental
- Should-trigger: preparar controles e pacote de evidências para auditoria técnica de um SaaS com duas regiões e dados incompletos. Resultado esperado: escopo/owner/período, resultados desconhecidos e gaps explícitos, sem declaração automática de conformidade.
- Near-miss: corrigir SQL injection em um diff. Encaminhar a secure-code-privacy-review, sem iniciar matriz de compliance.
- SLO: 1.000 eventos elegíveis, 998 bons, alvo 99,9%: permitidos aproximadamente 1, consumidos 2, restante -1 e burn rate 2. Não converter isso em minutos ou créditos contratuais.
- Sem tráfego ou perda de telemetria: evidência insuficiente, não 100%; alvo 100% não admite divisão por zero na fórmula de burn rate.
- Supply chain: assinatura válida com identidade inesperada ou SBOM de outro digest não satisfazem o gate.
- Compliance: erro de permissão, evidência velha ou exceção vencida não satisfazem o controle.

Validação realizada: inspeção de fronteiras e casos acima, frontmatter/names/rotas e cobertura de 40 decisões. Validação de runtime das ferramentas: não executada. Verificação de publicação é realizada após o commit, sem presumir sucesso no momento de redigir este registro.
