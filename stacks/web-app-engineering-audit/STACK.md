---
name: web-app-engineering-audit
description: "Auditar web apps e PWAs existentes como consultoria técnica, conectando arquitetura, código, testes, segurança, qualidade web, supply chain, PWA e runtime em findings priorizados e roadmap verificável."
---

# Web App Engineering Audit

## Objetivo

Executar uma auditoria técnica de web app/PWA sem transformar a revisão em checklist infinito. A stack seleciona os owners necessários, cruza evidências e entrega riscos, oportunidades e roadmap com trade-offs explícitos.

## Quando usar

- due diligence técnica de web app;
- revisão independente antes de escala ou release;
- auditoria de qualidade/arquitetura/segurança;
- diagnóstico de dívida técnica;
- avaliação de uma PWA existente;
- consultoria de modernização ou inovação tecnológica baseada no sistema atual.

## Owners candidatos

- `code-understanding-audit` — mapa do sistema e decisões existentes;
- `system-design-engineering` — arquitetura, SLOs, scale e failure modes;
- `code-review` — qualidade e blast radius de mudanças;
- `software-testing-engineering` — estratégia e lacunas de teste;
- `web-application-security-audit` — segurança observável autorizada;
- `secure-code-privacy-review` — causa em código e privacy;
- `web-quality-audit` — performance, acessibilidade e best practices;
- `pwa-engineering` — somente quando PWA/offline/installability fizer parte do produto;
- `software-supply-chain-engineering` — dependências, artifacts e provenance;
- `runtime-ui-verification` — jornadas, estados de componente e visual baselines no app real;
- `resilience-engineering` — somente quando dependency/network failure e recovery forem risco material;
- `progressive-delivery-verification` — somente quando o audit incluir estratégia de release/canary;
- `decision-analysis` — trade-offs de modernização/adoção tecnológica;
- `verify-before-claim` — fechamento por evidência.

Não carregar todos automaticamente.

## Fluxo

1. **Scope**
   - objetivos de negócio e técnicos;
   - superfícies críticas;
   - ambientes;
   - usuários/roles;
   - restrições de segurança, compliance, prazo e budget;
   - mudanças em curso que não devem ser confundidas com baseline.

2. **System map**
   - arquitetura e dataflow;
   - módulos e ownership;
   - dependências externas;
   - deploy/runtime;
   - persistência;
   - trust boundaries;
   - PWA/service worker se existir.

3. **Risk hypotheses**
   - listar riscos antes de abrir frentes profundas;
   - priorizar por impacto, probabilidade/evidência e reversibilidade;
   - escolher apenas os owners que conseguem testar essas hipóteses.

4. **Architecture & maintainability**
   - SLOs/failure modes;
   - seams e acoplamento;
   - state/data ownership;
   - bottlenecks;
   - dívida que aumenta custo de mudança.

5. **Testing & runtime**
   - mapear jornadas críticas para a camada mínima de teste;
   - confirmar comportamento no app real;
   - distinguir ausência de teste de defeito observado.

6. **Security & privacy**
   - code review proporcional ao risco;
   - auditoria black-box/gray-box somente em escopo autorizado;
   - supply chain quando dependências/artifacts forem relevantes.

7. **Web quality**
   - performance;
   - accessibility;
   - browser/device behavior;
   - network/runtime errors;
   - regressões mensuráveis.

8. **PWA, quando aplicável**
   - manifest/installability;
   - service worker;
   - caching/offline;
   - update lifecycle;
   - sensitive storage;
   - network degradation.

9. **Technology decisions**
   - separar “tecnologia nova” de problema real;
   - avaliar fit, maturidade, lock-in, custo de migração, operação, skills do time e reversibilidade;
   - classificar recomendações como experimentar, adotar, manter ou evitar somente quando evidência justificar;
   - não usar popularidade como decisão.

10. **Synthesize**
    - deduplicar findings;
    - conectar causa → impacto → recomendação;
    - distinguir quick win, risco estrutural e aposta;
    - registrar incerteza/itens não verificados.

11. **Roadmap**
    - Now: risco alto/baixo custo ou blocker;
    - Next: melhorias estruturais com dependências claras;
    - Later: experimentos e modernização;
    - cada item com owner sugerido, verificação e condição de sucesso.

12. **Verify**
    - confirmar que findings materiais têm evidência;
    - não declarar área “saudável” quando ela não foi testada;
    - separar revisão documental, inspeção de código e runtime.

## Entregável

Produzir, proporcionalmente ao escopo:
- resumo executivo;
- system map;
- matriz de findings;
- evidências e limitações;
- risk register;
- oportunidades de simplificação/modernização;
- roadmap priorizado;
- testes/retestes necessários.

Cada finding material deve distinguir:
- evidência;
- impacto;
- urgência;
- esforço aproximado ou faixa;
- recomendação;
- como provar a correção.

## Regra de parcimônia

Uma landing page simples pode exigir apenas `web-quality-audit` + `runtime-ui-verification`. Uma PWA autenticada crítica pode justificar arquitetura, testing, security, privacy, supply chain e PWA. A stack serve para selecionar, não para inflar escopo.
