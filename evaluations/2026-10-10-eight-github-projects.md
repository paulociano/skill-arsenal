# Avaliação em lote — 2026-10-10 — oito repositórios

## Método
Fonte canônica: `ARSENAL INDEX.md`, `AGENTS.md` e `stacks/arsenal-autopilot/STACK.md` do Arsenal. Fontes externas: READMEs dos oito repositórios e SKILL.md original de good-css e iso-figure. Revisão estática, sem execução de instaladores, benchmarks, builds ou auditoria integral do código.

| Repositório | Classe | Capability / dependências | Owner e decisão |
| --- | --- | --- | --- |
| [vojtaholik/good-css](https://github.com/vojtaholik/good-css) | A | CSS adaptativo, container/grid, foco, movimento reduzido; Skill original e referências CSS | CREATE_NEW `modern-css-practices`: contrato CSS-first com compatibilidade e fallback, sem regras absolutas do original |
| [nachisama/ai-data-extractor](https://github.com/nachisama/ai-data-extractor) | D | Extrai históricos locais Claude/Codex/Cursor/Windsurf etc. via Python, SQLite/JSONL | KEEP_EXTERNAL_REFERENCE; não disponibilizar acesso automático ao disco local nem ingerir segredos. Uso somente com arquivos autorizados |
| [thesysdev/open-intelligent-ui](https://github.com/thesysdev/open-intelligent-ui) | A/D | Component grammar, streaming, mapas com estado compartilhado; Next.js, OpenUI Gateway/THESYS_API_KEY ou Ollama | ABSORB_METHOD_ONLY via `generative-ui-engineering`; não equiparar API externa ao runtime do ChatGPT. Licença não confirmada nos metadados |
| [MrBongoC/ai-iso-skill](https://github.com/MrBongoC/ai-iso-skill) | A | Prancha HTML/SVG, projeção isométrica e interação real; sem biblioteca obrigatória | CREATE_NEW `interactive-isometric-figure`; foco estreito não coberto por sketch geral |
| [studioigor/ref2game](https://github.com/studioigor/ref2game) | A/D | Imagem de referência → vertical slice, style bible, rigs, QA de movimento e comparação de frames; imagegen, Python, Node, engine WebGL2 | ABSORB_METHOD_ONLY; aplicar no contexto de `game-development-cycle`/`game-development-engineering`, sem prometer geração paralela, live reload ou build sem runtime |
| [lithos-ai/lithos-metal](https://github.com/lithos-ai/lithos-metal) | D | Servidor/kernels Metal para LLMs, DSpark e modelos específicos; Apple Silicon/macOS 26+ | KEEP_EXTERNAL_REFERENCE sob `local-llm-inference-engineering`; desempenho e compatibilidade exigem benchmark no dispositivo |
| [pavellunev/trading_chart](https://github.com/pavellunev/trading_chart) | D | SwiftUI/Swift Charts para candles, indicadores, crosshair, histórico e indicadores; iOS/Xcode reais | KEEP_EXTERNAL_REFERENCE sob `swiftui-modern-ui`; não serve para charts HTML nem substitui engenharia financeira |
| [marmottajr/habblaud](https://github.com/marmottajr/habblaud) | D | Escritório pixel-art de sessões Codex/Claude, telemetria e ações; Node, Docker e mods/hooks locais | KEEP_EXTERNAL_REFERENCE para observabilidade de agentes; aprovações/terminal não podem ser replicados por texto, atenção a permissões/hook e exposição de sessões |

## Segurança
- Não executar `npx`, `npm`, `brew`, instaladores ou modificadores de hooks durante triagem.
- Não importar histórico pessoal nem publicar JSONL de chats/código; revisar segredos, caminhos e direitos de uso.
- Chaves de APIs em servidor seguro; render de saída do modelo restrito por allowlist/validação; URLs e geodados precisam de proveniência.
- Para motores 3D/WebGL, SDKs e kernels Metal: capacidades externas só existem em ambiente com dependências e hardware disponíveis.
- As metodologias novas são texto original adaptado; não há cópia de código integral ou assets de terceiros.

## Valor incremental
- `modern-css-practices`: checklists CSS específicos, exemplo de should-trigger: modernizar cards responsivos; near-miss: app SwiftUI.
- `interactive-isometric-figure`: representação geométrica e interação real, should-trigger: sintetizador isométrico clicável; near-miss: diagrama de arquitetura estático.
- Demais fontes já possuem owners ou são softwares externos cujo runtime não é transferível.

## Limites e follow-up
A avaliação considera documentação, não prova de que todos os recursos anunciados funcionam. Verificação dinâmica, licenças de componentes transitivos, segurança de dependências e performance exigem auditoria separada antes de usar em produção.
