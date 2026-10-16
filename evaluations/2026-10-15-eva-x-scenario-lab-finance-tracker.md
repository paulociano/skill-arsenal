# Avaliação: EVA-X, Scenario Lab e Personal Finance Tracker

Data: 2026-10-15. Fonte canônica: https://github.com/paulociano/skill-arsenal (ARSENAL INDEX consultado antes dos owners). Avaliação de documentação original, sem instalação ou testes de runtime.

## EVA-X
- Origem: https://github.com/hustvl/eva-x ; branch main; README e links para classificação/segmentação.
- Capacidade: Vision Transformers auto-supervisionados especializados em radiografias de tórax, pesos ViT Tiny/Small/Base, classificação, segmentação e análise Grad-CAM.
- Classe **D**, método útil em domínio técnico mas dependente de checkpoints, datasets médicos, licenças e stack Python/CUDA.
- Decisão: **KEEP_EXTERNAL_REFERENCE**. Sem skill clínica nova; não converter artigo e benchmarks relatados em aprovação para diagnóstico. Qualquer adoção exigiria avaliação prospectiva/externa, privacidade de dados de saúde, análise de viés e supervisão clínica.

## Scenario Lab
- Origem: https://github.com/YSLAB-ai/scenario-lab ; branch main; README e docs/limitations.md.
- Capacidade: simulação exploratória por domínios e ações/reações com pacote de evidências aprovado, belief state, MCTS, relatórios e replays.
- Classe **B/D**. O método é reutilizável; o runtime Python e adaptadores para Codex/Claude não são assumidos disponíveis.
- Decisão: **UPDATE_EXISTING** em skills/scenario-forecasting/SKILL.md, commit `3ff1af13b26cf6ea94a8f3c81beceaf7c71b49a4`. Adicionados cenários condicionais com estado/ações/terminais explícitos, aprovação de evidências, efeitos de segunda ordem, calibração versus regressão e disclosure de outcomes ausentes.
- Limites: preview v0.1.0. A documentação informa replays históricos parcialmente ancorados e divergências de fontes; regressão não prova habilidade de prever eventos reais. Não usar scores internos como probabilidades verificadas.

## Personal Finance Tracker with AI Expense Prediction
- Origem: https://github.com/48Naveenkumar/Personal-Finance-Tracker-with-AI-Expense-Prediction ; branch main; README e estrutura backend/ consultada.
- Capacidade declarada: registro/categorização de despesas, orçamento, dashboard, previsão de gastos com Django/React/TensorFlow/PostgreSQL.
- Classe **C/D**: proposta genérica e implementação técnica dependente do app. O README não apresenta protocolo mensurável de backtesting da previsão.
- Decisão: **KEEP_EXTERNAL_REFERENCE**; skills/personal-financial-planning/SKILL.md e skills/scenario-forecasting/SKILL.md já incluem fluxo de caixa, orçamento, baseline, avaliação temporal e premissas. Não criar skill, não executar treinamento, não presumir segurança apenas de alegações de encriptação.

## Fechamento
1 melhoria metodológica incorporada a owner existente; duas referências sem importação. Nenhum código externo executado nem integrações instaladas. Esta avaliação não inclui auditoria completa de código, dataset ou inferência de modelos, e não atesta performance ou segurança em produção.
