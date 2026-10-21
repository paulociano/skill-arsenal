---
name: diffusion-finetuning-planning
description: Planejar, revisar e validar fine-tuning/LoRA de modelos de difusão de imagem e vídeo com dataset, captions, configuração, hardware, checkpoints, testes e direitos de uso, sem pressupor runtime de treino disponível.
---

# Diffusion Fine-tuning Planning

## Objetivo
Ajudar a decidir quando treinar um adaptador/modelo de difusão e entregar um plano reproduzível e auditável, separando especificação de treino de execução real.

## Quando usar
- usuário quer treinar LoRA/fine-tune de personagem, estilo, objeto ou edição em modelos de difusão;
- preparação, diagnóstico e comparação de datasets e captions para treinamento;
- estimar viabilidade de GPU, configurar treinamento, checkpointing e critérios de validação;
- inspecionar logs/amostras de treino para reconhecer drift, overfitting e falhas de identidade.

Não use para a geração pontual de uma imagem nem imponha treino quando referências e edição localizada resolvem. `character-continuity` decide primeiro se treino é proporcional ao problema.

## Contrato de execução
- Confirmar modelo-base exato e sua licença, caso de uso, tipo de adaptador, versão de toolkit e forma de execução.
- Diferenciar plano conceitual, YAML ilustrativo, validação estática, execução em GPU e avaliação experimental comprovada.
- Não presumir disponibilidade de AI Toolkit, CUDA, GPU, conector remoto, tokens, hospedagem ou capacidade de executar treinamento nesta sessão.
- Escolher ferramenta somente quando o usuário já tiver runtime acessível; scripts devem seguir documentação/versionamento confirmado da ferramenta selecionada.

## Workflow
1. **Justificativa**: identificar o erro recorrente que referências/atlas/edição não resolveram; registrar a evidência e critérios de sucesso.
2. **Modelo e direitos**: verificar licença/termos do modelo-base e pesos, finalidade comercial, consentimento/direitos de imagens, armazenamento e eventual uso biométrico.
3. **Dataset**: auditar cobertura por ângulo, expressão, iluminação e pose, duplicatas e near-duplicates, qualidade, diversidade, vazamento e split holdout por cena/sujeito. Não adicionar conteúdo artificial idêntico para inflar a contagem.
4. **Captions**: manter legenda por imagem com distinção entre identidade estável, atributos editáveis e cenário/pose; usar token de ativação apenas quando a família de modelo/receita justificar e confirmar sintaxe.
5. **Plano de treino**: escolher LoRA/adaptador ou fine-tune total conforme GPU, capacidade do modelo, custo, risco de sobreajuste e habilidade de reversão. Usar configs de exemplo da versão real como base, não copiar valores como universais.
6. **Recursos**: documentar VRAM, memória, espaço em disco, versões CUDA/PyTorch, tamanho de imagem, batch, gradient accumulation, precisão, caching e duração como **estimativas** até benchmark real.
7. **Execução segura**: snapshots de configuração, origem do dataset, checkpoints, seeds, logging de métricas, validação de integridade antes de retomar; não interromper checkpoint em escrita.
8. **Avaliação**: definir prompts fixos e prompts fora de distribuição, sementes comparáveis, mesma geração-base, versões de checkpoint, revisão humana de identidade, estilo, diversidade e defeitos, e decisão explícita entre aceitar/reverter/ajustar.
9. **Entrega**: relatório de modelo, versão, licença, proveniência do dataset, parâmetros, artefatos, limitações e condição de reprodução; marcar sempre as partes não executadas.

## Failure modes e controles
- Overfit: boa reprodução da foto-base, baixa diversidade de poses e contextos. Reduzir redundância ou revisar passos/capacidade.
- Underfit: identidade inconsistente em prompts de teste. Melhorar cobertura, captions e avaliação antes de aumentar treino automaticamente.
- Drift estilístico: medir separadamente similaridade de identidade e aderência à direção artística.
- Data leakage: separar exemplos de validação por cenas distintas e, quando aplicável, por pessoa.
- UI de treinamento exposta: restringir rede, autenticação e credenciais; token simples não substitui revisão completa de segurança.
- Supply chain: não rodar automaticamente managers experimentais, scripts, Docker ou update; revisar lockfiles, submódulos, downloads e versões de pesos.
- Privacidade: evitar enviar datasets de pessoas reais a GPU remota sem direitos e consentimento.

## Conexões
- `character-continuity` controla a identidade e determina quando escalar a treino;
- `high-fidelity-image-generation` controla as gerações de amostra e inspeção;
- `ai-reels-production` consome outputs de vídeo quando realmente exportados.

## Acceptance checks
- A decisão de treinar está justificada frente ao fallback sem treino?
- O modelo/versão e licença são identificados?
- Há cobertura, metadados e holdout suficientes para medir o resultado?
- O plano pode ser reproduzido numa infraestrutura descrita, sem fingir que ela existe aqui?
- O QA compara prompts e versões fixas e preserva direitos/segurança?
- Qualquer alegação de sucesso tem execução e artefatos comprováveis?

## Proveniência
Metodologia adaptada de https://github.com/ostris/ai-toolkit, README (consulta em 2026-10-20): suporte extensivo a modelos de imagem/vídeo, datasets de imagens e .txt, bucketing, configuração YAML, LoRA por grupos de layers, checkpoints, UI/CLI. AI Toolkit (MIT) é **referência técnica opcional**, não dependência instalada. Nenhum comando de instalação/treino foi executado.
