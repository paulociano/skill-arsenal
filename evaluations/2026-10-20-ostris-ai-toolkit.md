# Avaliação — ostris/ai-toolkit

Data: 2026-10-20

## Fonte
https://github.com/ostris/ai-toolkit (branch main; README, metadados e estrutura de arquivos consultados).

## Classe
**A/D** — metodologia útil de engenharia de treinamento, apoiada em toolkit técnico com runtime externo.

## Capacidades identificadas
- Planejar fine-tuning de modelos de difusão de imagem e vídeo, LoRA/adaptadores e edição.
- Preparar dataset imagem+caption, buckets de proporção e token opcional de ativação.
- Configurar jobs YAML, capturar checkpoints, retomar e comparar outputs.
- Seleção de layers em LoRA e monitoramento via GUI/CLI.
- Requisitos de GPU, Python, PyTorch, Node.js, downloads de modelos e infraestrutura opcional de nuvem.

## Sobreposição e novo ganho
- `character-continuity`: owner de consistência de identidade e decisão de escalar, mas não da preparação/validação de treino.
- `high-fidelity-image-generation`: owner de geração visual, mas não do ciclo de treinamento.
- Ganho incremental: contrato reproduzível para dataset, captions, configurações, checkpoints, holdout e avaliação; workflow não dependente de instalar AI Toolkit.

## Decisão
**CREATE_NEW + KEEP_EXTERNAL_REFERENCE**: criada `skills/diffusion-finetuning-planning/SKILL.md` e adicionada rota ao `ARSENAL INDEX.md`.

Não copiar código, receitas de versões antigas ou dependências do AI Toolkit. Treinamento real requer GPU e runtime disponíveis; o ChatGPT nesta sessão apenas planeja, revisa configs/datasets e valida evidência fornecida.

## Segurança e portabilidade
**CAUTION**: manager experimental pode instalar/update dependências; scripts shell/batch, Docker, submódulos, pacotes Python/Node, downloads de pesos, tokens Hugging Face/Modal, nuvem e exposição da UI. Verificar supply chain, licenças individuais dos modelos, permissões e proteção dos datasets pessoais. Nenhum installer nem job foi executado; não houve auditoria integral de código.

## Validação e limites
- Verificado por leitura: README, licença MIT e arquivos root.
- Skill exige critérios de qualidade, holdout, controle de identidade, aprovação e provas de execução.
- Benchmarks e performance de GPU **não reproduzidos**.
- Não afirmar que cada modelo listado funciona no hardware do usuário.
- Arquivos publicados: `skills/diffusion-finetuning-planning/SKILL.md` e `ARSENAL INDEX.md`.
