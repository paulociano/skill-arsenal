# Avaliação: Maigret, Build Signal Engine e Cole's AI Skills

Data: 2026-10-15
Método: arsenal-autopilot + skill-security-review; inspeção documental estática, sem executar instaladores, scripts nem conectores de pesquisa OSINT.

## Fontes
- https://github.com/torerobo/maigret
- https://github.com/soxoj/maigret (upstream)
- https://github.com/coleam00/skills/tree/main/.claude/skills/build-signal-engine
- https://github.com/coleam00/skills/tree/main/.claude/skills

## Decisões

| Fonte/capability | Classe | Decisão | Owner |
|---|---|---|---|
| torerobo/maigret (fork de Sherlock) | B/D | KEEP_EXTERNAL_REFERENCE | registro OSINT de 2026-09-30 |
| soxoj/maigret (projeto principal atual) | B/D | KEEP_EXTERNAL_REFERENCE | registro OSINT de 2026-09-30 |
| build-signal-engine | A/D | CREATE_NEW (metodologia portátil) | signal-intelligence-digest |
| Cole's AI Skills, ciclo prime→plan→implement→validate→review→commit→PR | A/B | KEEP_EXTERNAL_REFERENCE, owner canônico já existe | software-engineering-cycle e respectivas skills de engenharia |
| Cole's AI Skills, worktrees/hooks/desktop/AST/tooling | D | KEEP_EXTERNAL_REFERENCE | capacidades dependentes de runtimes específicos |
| Cole's AI Skills, curso/tutorial | C/D | REJECT para importação | sem owner necessário |

## Evidência e valor incremental

**Maigret**: o link enviado é um fork histórico de Sherlock (último push do fork em 2020); o README recomenda `soxoj/maigret`. O upstream oferece consulta de usernames, correlação recursiva de perfis, relatórios e recursos técnicos; há riscos de privacidade, falsos positivos, rastreamento e termos de serviços. Já consta em `evaluations/2026-09-30-identity-email-osint-batch.md`. Não se cria skill de profiling de pessoas.

**Signal Engine**: o SKILL.md ensina ingestão em uma fonte primeiro, ID estável, dedupe antes de despesas, filtros determinísticos, decisão separada da leitura, casos rotulados keep/drop, digest curto e semana de shadow feedback. Isto introduz um workflow específico de *curadoria de sinal informacional* que não é equivalente a monitoramento de vagas ou automação genérica. Adotado como skill `signal-intelligence-digest`, sem prometer runtime persistente inexistente.

**Cole's AI Skills**: README inventaria 35 skills e define loop de engenharia prime→plan→implement→validate→review→commit→PR. O Arsenal já tem owners de arquitetura, gestão de produto, coding agents, revisão, testes, engenharia e stacks de entrega. Nenhuma instalação em lote se justifica. Comandos `/plugin`, `npx skills`, hooks de Claude, worktrees e desktop executável não são capacidades automaticamente disponíveis no ChatGPT. Os subdiretórios foram inventariados; não se afirma auditoria linha a linha das 35 skills.

## Security gate
- **Signal Engine (adaptação textual): CAUTION → APPROVE condicionado ao runtime**. Uso de APIs, credenciais, coleta automatizada e agendamento precisa de autorização, orçamento, escopos mínimos, respeito aos TOS, validação de fontes e testes. Nenhuma credencial ou script foi executado nesta avaliação.
- **Maigret: CAUTION**. Ferramenta real OSINT com implicações de privacidade e exposição de terceiros; não transformar em capacidade autônoma por prompt.
- **Catálogo Cole: CAUTION para instalação integral**. Hooks podem executar ações imediatamente, ferramentas invocam shell e algumas skills são próprias de Claude Code; não instalar em massa.

## Portabilidade e validação
O owner novo usa capacidades genéricas, com alternativas explícitas para pesquisa em chat versus pipeline implantado por runtime externo. Aceitação: radar recorrente com foco específico, dados e URL rastreáveis, deduplicação verificável, falsos negativos auditados, custo controlado e boletim curto. Não houve execução real de pipeline, teste de rede, revisão de scripts ou instalação de hooks. Registrar sem alegar cobertura não testada.
