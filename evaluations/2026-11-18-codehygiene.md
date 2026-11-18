# Avaliação: CodeHygiene

- Data: 2026-11-18
- Fonte: https://github.com/brianbell-x/codehygiene (branch `main`)
- Arquivos inspecionados: `README.md`, `codehygiene/SKILL.md`, `AGENTS.md`, `pyproject.toml`, `codehygiene/update_check.py`.
- Categoria: **B/D** (metodologia incremental útil + detector técnico externo).
- Decisão: **UPDATE_EXISTING** em `skills/code-review/SKILL.md`; não criar skill `codehygiene` redundante.
- Avaliação de segurança: **CAUTION / static_only**. Sem scanner nem execução do código completo.

## O que faz
O CodeHygiene é um detector de legibilidade estrutural para 20+ linguagens. Analisa aninhamento profundo, erros silenciados, comentários narrativos, nomes e cerimônia excessivos, números mágicos, especializações redundantes e blocos duplicados. O projeto descreve um modelo ternário compacto com `weights.npz`, execução Python/NumPy ou JavaScript, saída JSON por linha e workflow voltado a arquivos tocados. Não substitui testes, typecheck, segurança ou revisão semântica.

## Incremento e sobreposição
O owner `code-review` já cobria standards/spec, simplificação, findings acionáveis e verificação. Ganhos concretos incorporados: escopo pós-diff pequeno, triagem de novos smells estruturais, juízo humano sobre cada sinal, limite de duas passagens e distinção clara entre score heurístico e correção funcional. Não é justificável criar um segundo owner.

## Segurança e dependências
- `pyproject.toml` informa Python >=3.10, `numpy>=1.24` e licença MIT. Modelo e scripts requerem runtime não presumido.
- `update_check.py` consulta `raw.githubusercontent.com/brianbell-x/codehygiene/main/pyproject.toml` periodicamente quando habilitado e grava cache local; pode ser desligado por `--no-update-check`, ambiente CI ou variável própria. Esta chamada não ocorre na adaptação textual.
- Instalação sugerida na origem usa `npx skills` ou `uvx` remoto. **Nada foi instalado ou executado**, e não foram realizadas inspeção integral do modelo binário, auditoria de supply chain, teste de rede, benchmarks ou testes de regressão do detector.
- Tratamento: não assumir scores; não bloquear builds por falso positivo; não expor código privado em issues públicas sem consentimento e minimização.

## Modificação publicada
- `skills/code-review/SKILL.md`
- Commit: `b503c3accb121c610121eb244bf71bb16f1d7d62`
- `ARSENAL INDEX.md` sem alteração: nome e descrição da skill existente permanecem adequados.

## Critério de validação
Verificar pós-publicação que o owner contém a seção `Higiene estrutural em diffs pequenos (CodeHygiene, 2026-11-18)` e que esta avaliação existe na branch canônica. **Não alegar equivalência funcional ao detector executável**.
