# Avaliação: elder-plinius/T3MP3ST (2026-10-11)

## Fonte e roteamento

- Origem: https://github.com/elder-plinius/T3MP3ST
- Fonte canônica: `ARSENAL INDEX.md`, seguido de `stacks/evaluate-and-import-skill/STACK.md`.
- Escopo da leitura estática: `README.md`, `FEATURES.md`, `SECURITY.md` e `package.json` do projeto; owners `web-application-security-audit`, `llm-red-team-evaluation` e `agent-action-governance`.
- Não houve execução de scripts, scans, exploits, instalação, benchmark ou acesso a alvos.

## Classificação e decisão

**Classe A/D**: metodologia de avaliação com registro de autorização e evidência útil, mas a implementação é um **framework técnico ofensivo independente**. **UPDATE_EXISTING** em `skills/web-application-security-audit/SKILL.md`. **KEEP_EXTERNAL_REFERENCE** para o framework; não instalar T3MP3ST, não criar skill de ofensiva autônoma e não importar payloads.

## Capacidades encontradas e ownership

- Orquestração de agentes, War Room, CLI, MCP e modelo local/remoto: runtime próprio, não disponível como ferramenta nativa do ChatGPT. Owner contextual `multi-agent-orchestration`.
- Testes web/CTF e scanners com ações de rede: exigem alvo explicitamente autorizado, isolamento, limites, verificação e avaliação de consequências. Owner `web-application-security-audit`.
- Governança de escopo e Rules of Engagement: owner existente `agent-action-governance`.
- Claims re-deriváveis e benchmarks versionados: boa referência, mas recontar resultados de artefatos armazenados não substitui replicação independente, validação de ground truth ou prova de generalização. Owners `llm-observability-evaluation` e `verify-before-claim`.
- Superfícies cloud/mobile/binário no README marcadas como scaffold/experimental; não tratar como cobertura demonstrada.

## Incremento material publicado

Aprimorado `web-application-security-audit` com: recibo de autorização verificável vinculado a alvo, janela, ações e condições de parada; separação observação/hipótese/achado confirmado; tentativa de refutação e reteste; cuidado com evidências de benchmarks, denominador, vazamento e verificador. Mantida toda a proibição de ações destrutivas, exfiltração, persistência, movimento fora de escopo e credenciais de terceiros.

## Segurança / portabilidade

**CAUTION** para executar framework externo: scripts npm, scanner HTTP/DNS/TCP, descoberta de serviços, payloads, credenciais, agentes locais e conectores MCP, supply chain, eventuais exports e provedores de LLM. Licença declarada AGPL-3.0-or-later. README declara uso exclusivo mediante autorização escrita. Avaliação de superfície documental, não auditoria completa de código ou confirmação da qualidade dos testes. Não presumir proteção por Docker isoladamente.

## Cenários de aceite

- Should-trigger: auditoria autorizada com múltiplos agentes ou ferramentas, precisando provar que cada achado pertence ao escopo e tem evidência reproduzível.
- Near-miss: análise estática simples de código sem alvo em runtime não exige scanner, War Room ou recibo de ataque; alegações de benchmark do autor não devem ser apresentadas como resultados reproduzidos nesta avaliação.
- Uma skill existente foi enriquecida; nenhuma nova descrição foi alterada. `ARSENAL INDEX.md` permanece inalterado por design.
