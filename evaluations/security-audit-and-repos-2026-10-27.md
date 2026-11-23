# Avaliação de 8 repositórios — 2026-10-27

## Escopo e método
Fontes: READMEs e, para cloudflare/security-audit-skill, o conteúdo completo da skill (clonado em área temporária; commit `c1c8a8c`). Comparação com `ARSENAL INDEX.md`. Revisão estática: busca por rede, `eval`, instaladores e `child_process`; os validadores `.cjs` usam só `fs`/`path`/`util`; `child_process` aparece apenas nos arquivos de teste. **Nenhum código externo foi executado** (testes dos validadores não rodados nesta sessão).

## Decisões

| Fonte | Classe | Decisão | Motivo |
| --- | --- | --- | --- |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | A/D | **ADOPT** → `skills/security-audit/` | Auditoria de código com ledger de cobertura, validação independente e schema; não duplica `secure-code-privacy-review` (revisão de diffs/privacidade) nem `web-application-security-audit` (runtime). MIT; preservada sem alteração além do frontmatter e da seção de integração. |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | D | **JÁ ABSORVIDO** | Regras de grafo de evidência já em `code-understanding-audit`. Ferramenta opcional (`graphifyy`); instalar só no Claude Code/Codex se o usuário quiser. |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | D/B | **DESCARTAR (já avaliado)** | Ver `ruvnet-ecosystem-2026-10-24.md`; método já em `multi-agent-orchestration`. |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | B | DESCARTAR | Princípios genéricos já cobertos por skills de engenharia/verificação existentes. |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | D | DESCARTAR | Sem ganho sobre `agent-memory-engineering`. |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | D | DESCARTAR | Backend externo pesado (GPU); sem método novo. |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | D | DESCARTAR | Agente de código concorrente, não skill/método. |
| [stablyai/orca](https://github.com/stablyai/orca) | D | DESCARTAR | Aplicativo de orquestração; sem método incremental. |

Observação: os descartes de karpathy-skills, ai-memory, ComfyUI, opencode e orca vêm da triagem anterior por README; não houve leitura de código.

## Segurança e portabilidade
`security-audit`: requer subagentes, Node e sandbox imposto pelo SO para executar código de alvo; sem isso opera em modo guidance/`needs_validation`. Termos da fonte mapeados para `Agent`/`Explore`/`general-purpose`.

## Prova mínima de utilidade
Should trigger: "faça uma auditoria de segurança completa deste repositório". Near-miss: "revise este diff por vazamento de PII" (→ `secure-code-privacy-review`).

## Pendências
- Rodar `node validate-findings.test.cjs` e `node validate-coverage-ledger.test.cjs` em ambiente aprovado antes de confiar nos validadores.
- README está defasado (cabeçalho "163 skills · 21 stacks" vs. 268 skills e 32 stacks no repositório; muitas skills sem linha); só a linha de `security-audit` foi adicionada.
