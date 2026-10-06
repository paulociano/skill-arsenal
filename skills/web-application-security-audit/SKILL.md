---
name: web-application-security-audit
description: "Auditar a segurança observável de web apps e APIs em ambiente autorizado, convertendo requisitos OWASP ASVS e cenários WSTG em testes proporcionais, evidência reproduzível, findings validados e reteste."
---

# Web Application Security Audit

## Objetivo

Avaliar a segurança de uma aplicação web ou API pela superfície realmente exposta, com escopo autorizado, requisitos explícitos e evidência reproduzível. A skill complementa revisão de código: ela testa comportamento e controles observáveis em runtime, sem tratar checklist ou scanner como prova automática.

## Quando usar

- auditoria de segurança de web app, PWA ou API;
- preparação para release ou revisão independente de controles;
- verificação de autenticação, autorização, sessão, input, configuração, APIs e lógica de negócio;
- reteste após correção de finding;
- criação de uma matriz de cobertura baseada em OWASP ASVS/WSTG.

Não usar para:
- revisão estática de diff/código: use `secure-code-privacy-review`;
- supply chain/dependências: use `software-supply-chain-engineering`;
- avaliar segurança de uma skill/plugin externa: use `skill-security-review`;
- testes fora de um alvo e escopo autorizados.

## Princípio central

**Requisito → hipótese de falha → teste seguro → evidência → finding validado → correção → reteste.**

## Grounding de padrão

Quando usar OWASP:
- fixe a versão do ASVS/WSTG usada no relatório;
- prefira release estável e identificadores versionados;
- revalide a versão atual quando a tarefa depender de requisitos recentes;
- selecione controles pelo risco e superfície real, em vez de marcar toda a norma mecanicamente.

ASVS define requisitos verificáveis; WSTG fornece cenários e técnicas de teste. Nenhum deles transforma ausência de finding em prova de segurança total.

## Workflow

1. **Authorization & scope**
   - confirmar alvo, ambiente, contas de teste e superfícies permitidas;
   - registrar ações proibidas, limites de carga e janelas de teste;
   - definir tratamento de dados, screenshots, logs e credenciais;
   - se a autorização não estiver clara, limitar-se a análise passiva/defensiva.

2. **Surface map**
   - rotas, APIs e hosts;
   - trust boundaries;
   - papéis/tenants;
   - autenticação e recovery;
   - sessão/cookies/tokens;
   - uploads, redirects, webhooks e integrações;
   - dados sensíveis e ações de alto impacto.

3. **Verification contract**
   - selecionar requisitos relevantes;
   - para cada controle registrar `pass`, `fail`, `blocked`, `not_tested` ou `not_applicable`;
   - definir evidência mínima e condição de parada antes do teste.

4. **Information & configuration**
   - exposição desnecessária de versões, headers, debug, source maps, directory/listing e metadata;
   - TLS/cookies/security headers quando aplicável;
   - configuração de CORS, cache e deployment exposta ao cliente.

5. **Identity, authentication & recovery**
   - enumeration;
   - credential lifecycle;
   - MFA quando aplicável;
   - reset/recovery;
   - rate controls sem gerar carga abusiva;
   - transições login/logout/re-auth.

6. **Authorization & tenant boundaries**
   - object-level e function-level authorization;
   - ownership;
   - role transitions;
   - horizontal/vertical access;
   - IDs previsíveis não são finding sozinhos: prove bypass de controle.

7. **Session & token handling**
   - criação, rotação e invalidação;
   - logout real;
   - fixation/reuse;
   - cookie attributes;
   - exposição em URL/log/storage;
   - comportamento concorrente e expirado.

8. **Input, output & data flow**
   - injection e unsafe interpretation;
   - encoding/sanitization contextual;
   - file upload;
   - SSRF/redirect quando houver superfície;
   - serialization/parsing;
   - armazenamento, cache e respostas contendo dados indevidos.

9. **Business logic & abuse cases**
   - sequência de etapas;
   - repetição/idempotência;
   - limites;
   - race/concurrency de baixo impacto quando seguro;
   - manipulação de preço, entitlement, workflow ou estado apenas em ambiente/conta autorizados.

10. **Client-side & API**
    - trust indevido no cliente;
    - secrets embutidos;
    - DOM/client injection;
    - CORS;
    - API schemas, methods, mass assignment e error leakage;
    - service workers/caches quando a aplicação for PWA.

11. **Validate findings**
    - tentar refutar com controles existentes;
    - distinguir configuração suspeita de vulnerabilidade explorável;
    - reduzir proof ao menor caso necessário;
    - não ampliar exploração após evidência suficiente.

12. **Report & retest**
    - finding com alvo, pré-condições, evidência, impacto e remediação;
    - referência versionada ao requisito/cenário quando usada;
    - retestar o caminho original depois da correção;
    - registrar cobertura e itens não testados.

## Evidência por finding

Um finding material deve conter:
- superfície afetada;
- pré-condições;
- passos mínimos reproduzíveis;
- resultado esperado vs observado;
- impacto plausível sustentado;
- controle/standard relacionado, quando aplicável;
- severidade com racional, não apenas label;
- correção proposta;
- reteste esperado.

Redigir tokens, cookies, PII, secrets e payloads sensíveis.

## Guardrails

- não executar DoS, stress, credential stuffing ou ações destrutivas;
- não exfiltrar dados além do mínimo necessário para confirmar a falha;
- não pivotar para sistemas fora do escopo;
- não persistir acesso;
- não usar credenciais reais de terceiros;
- não transformar um scanner em autoridade;
- findings críticos exigem confirmação proporcional ao risco;
- declarar claramente quando parte do teste ficou bloqueada.

## Integração

Combina com:
- `secure-code-privacy-review` para localizar a causa no código;
- `behavior-contract-validation` para contratos black-box;
- `runtime-ui-verification` para fluxos no browser;
- `software-testing-engineering` para regressões;
- `software-supply-chain-engineering` para dependências/artifacts;
- `verify-before-claim` para conclusão da auditoria.

## Provenance

Adaptada de:
- https://github.com/OWASP/ASVS
- https://github.com/OWASP/wstg

Em 2026-10-05, ASVS 5.0.0 era a release estável indicada pelo projeto e o WSTG trabalhava na 5.0 mantendo 4.2 como release estável. Revalidar versões em auditorias futuras. A metodologia foi adaptada para escopo autorizado, testes não destrutivos e ferramentas realmente disponíveis; nenhum scanner ou pentest suite é requisito.
