# Avaliação: github/spec-kit e Renhuai123/ziwei-doushu

- Data: 2026-11-10
- Fluxo: `evaluate-and-import-skill` + `skill-security-review` (inspeção estática; nada foi instalado ou executado)
- Fontes: https://github.com/github/spec-kit · https://github.com/Renhuai123/ziwei-doushu

## 1. github/spec-kit

- Evidência: README.md, `spec-driven.md`, `templates/commands/*.md` (analyze, checklist, clarify, constitution, converge, implement, plan, specify, tasks), listagem de `extensions/`, `presets/`, `bundles/`, `src/specify_cli/`.
- Histórico: já triado em 2026-09-20 (A, sem nova skill) e 2026-10-22 (A/D, KEEP_EXTERNAL_REFERENCE, pendente "etapa verificável fora do task contract"). `to-spec` já tinha absorvido a cadeia spec → plano → tarefas → convergência.
- Classificação: **A/D** — metodologia forte (A) entregue por CLI Python + templates com hooks e scripts por agente (D).
- Decisão: **UPDATE_EXISTING** em `skills/to-spec/SKILL.md`, seção "Gates de qualidade da spec".

### Delta incorporado (o que faltava no Arsenal)
1. `clarify`: varredura de ambiguidade por taxonomia Clear/Partial/Missing com cota máxima de 5 perguntas e gravação incremental na spec.
2. `checklist`: "testes unitários dos requisitos" — itens que testam a redação da spec (completude, clareza, consistência, mensurabilidade), explicitamente separados de testes de comportamento.
3. `analyze`: análise cruzada somente leitura spec/plano/tarefas com severidade e princípio do projeto como CRITICAL.

Não incorporado: o CLI `specify`, `.specify/extensions.yml`, hooks, presets, bundles, catálogos comunitários e scripts bash/PowerShell — runtime específico, sem ganho para o ChatGPT/Claude chat. `converge` e `constitution` já estavam cobertos em `to-spec`. As extensões `bug` e `assess` sobrepõem `debug-and-fix` e `idea-refine`/`venture-building-cycle`.

### Segurança: CAUTION (para instalar o CLI)
- `uv tool install specify-cli` instala pacote Python; `specify init` escreve comandos/skills e scripts no projeto.
- Hooks obrigatórios (`optional: false`) instruem o agente a executar comandos automaticamente.
- Catálogos comunitários de extensões/presets não são auditados (o próprio README alerta).
- Mitigação: só em repositório de código, com revisão do diff gerado por `specify init`, sem extensões comunitárias não revisadas.

### Instalar no Claude?
- Claude chat/claude.ai: não há skill instalável; o método já está no Arsenal via `to-spec`.
- Claude Code em projeto de software: opcional, `specify init <projeto> --integration claude`. Sobrepõe superpowers (`brainstorming`, `writing-plans`, `executing-plans`) e mattpocock (`to-spec`, `to-tickets`, `implement-spec`) já instalados; escolher um fluxo por projeto.

## 2. Renhuai123/ziwei-doushu

- Evidência: README.md (zh), package.json, listagem de `lib/ziwei/`, `lib/classics/`, `lib/nihai/`, `app/`, `components/`, seções "开源边界" e "协议".
- Função real: aplicação Next.js 16 de 紫微斗数 (Zi Wei Dou Shu, astrologia chinesa) — motor de mapa natal (calendário lunar, hora solar verdadeira, horário de verão chinês, 四化, padrões), textos clássicos e datasets de leituras (até 56,6 GB). Não contém SKILL.md, agente, nem metodologia de trabalho.
- Classificação: **D** — software/dataset de domínio.
- Decisão: **REJECT** (fora de escopo do Arsenal; nenhuma metodologia reutilizável).
- Licença: código MIT; datasets CC BY 4.0; citações do mestre 倪海厦 CC BY-NC-SA 4.0 (não comercial). O banco de interpretações e os prompts de IA do serviço online não são abertos (`db-analysis.ts` é placeholder).
- Segurança (se rodar o app): dependências `@anthropic-ai/sdk`, `pg`, `ioredis`; exige chaves de API e banco; não executado.
- Instalar no Claude: não aplicável. Se um dia houver interesse no tema, o caminho seria usar o motor `lib/ziwei/` como biblioteca em um projeto próprio, não como skill.

## Limites da validação
Leitura estática de README, templates e manifestos; nenhum script, instalador ou teste foi executado; código-fonte completo e dependências não foram auditados.
