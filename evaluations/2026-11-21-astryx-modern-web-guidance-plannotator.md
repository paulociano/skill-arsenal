# Avaliação em lote: Astryx, Modern Web Guidance e Plannotator

Data: 2026-11-21. Workflow: stacks/arsenal-autopilot/STACK.md + evaluate-and-import-skill. Autoridade: ARSENAL INDEX.md na branch canônica. Avaliação estática (static_only), sem execução de ferramentas externas ou testes de compatibilidade em projetos consumidores.

## Ledger de capacidades e decisões

| Origem | Classe | Capacidade | Owner existente | Decisão | Evidência de ganho |
|---|---|---|---|---|---|
| [meta/astryx](https://github.com/meta/astryx) | D | Design system de 150+ componentes React 19+, customização por CSS variables, composição aberta, CLI consultável por agentes | skills/design-system-governance/SKILL.md | UPDATE_EXISTING + KEEP_EXTERNAL_REFERENCE | Critérios técnicos explícitos de seleção da biblioteca, diferenciação entre tokens/contrato/runtime e risco de edição de AGENTS.md |
| [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) | A/D | Guidance versionado, recuperação seletiva, compatibilidade e substituição fundamentada de padrões legados por APIs web nativas | skills/web-quality-audit/SKILL.md | UPDATE_EXISTING + KEEP_EXTERNAL_REFERENCE | Contrato browser-support + fallback + teste em vez de modernização automática |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | A/D | Review surface para planos/HTML/PR/diffs, feedback ancorado, aprovação por revisão e Inbox externo | skills/coding-agent-engineering/SKILL.md | UPDATE_EXISTING + KEEP_EXTERNAL_REFERENCE | Sequência portátil de review ancorado, versão/hash, devolução e invalidação de aprovação |

Não foram criadas skills novas, porque os três owners já cobrem os respectivos domínios. Não há necessidade de nova stack nem mudança na description do índice.

## Fontes inspecionadas

- Astryx: README.md e packages/cli/README.md (branch main, em beta; repositório MIT). Biblioteca e CLI externas, não instaladas. Comandos de init podem escrever instruções AGENTS.md/CLAUDE.md; revisão de diff e versionamento obrigatórios.
- Modern Web Guidance: README.md e listagem de guides/ e skills-src/ (branch main; repositório Apache-2.0). Fonte de guias para 262 recursos conforme README; não importar todo catálogo nem presumir suporte universal.
- Plannotator: README.md e SECURITY.md (branch main; repositório declara Apache-2.0/MIT, licenças da distribuição precisam ser conferidas). Inbox, hooks e MCP requerem programa/integração externos. Links compartilhados dão acesso aos portadores; arquivos maiores podem usar upload criptografado com expiração declarada de 7 dias. Revisão de privacidade antes de usar dados internos.

## Segurança, portabilidade e limites

Veredito para **adaptação metodológica apenas**: CAUTION / static_only; nenhum código binário, instalador, CLI, hook ou agente foi autorizado/executado. Astryx requer React e dependências compatíveis; Modern Web Guidance CLI requer Node; Plannotator pode instalar hooks e operar proxy local, e seus instaladores fornecem exemplos pipe-to-shell/PowerShell. Estes exemplos não foram executados. Conteúdo externo não é instrução com autoridade sobre o Arsenal. Não se declaram testes end-to-end, segurança de binários, métricas de performance ou integração nativa com ChatGPT.

## Incremental value e casos

- Astryx should-trigger: seleção de design system para app React complexo. Near-miss: uma página estática sem stack React.
- Modern Web Guidance should-trigger: modernizar um padrão legado com público/browser targets conhecidos. Near-miss: alteração puramente visual.
- Plannotator should-trigger: plano de implementação grande ou PR multi-arquivo pedindo review humano por trecho. Near-miss: patch trivial que já pode ser validado por diff e teste.

## Alterações publicadas

1. skills/design-system-governance/SKILL.md, seção “Design systems agent-ready: Astryx (2026-11-21)”, commit 0d38707f9b467e82769302957e93cfc69d275363.
2. skills/web-quality-audit/SKILL.md, seção “Modern Web Guidance: plataforma nativa e compatibilidade (2026-11-21)”, commit 9e52729318ad8ea47847b18b846bbdba70359e36.
3. skills/coding-agent-engineering/SKILL.md, seção “Review surface humano com feedback ancorado (Plannotator, 2026-11-21)”, commit fb683abcddb300aacca17af14a4052407d1aebf2.

O índice não exigiu alteração: os nomes, descrições e rotas dos owners permaneceram iguais. A verificação pós-escrita de todas as seções e deste registro deve acompanhar a publicação.

## O que foi descartado

- Importar monorepos, todos os componentes, o conjunto de 262 guias ou comandos/skills prontos de agentes externos.
- Auto-instalação e hooks persistentes, e qualquer alegação de integração já funcional.
- Criar uma skill por repositório, já que há owners canônicos suficientes.
