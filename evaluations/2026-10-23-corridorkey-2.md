# CorridorKey 2.0 — avaliação técnica (2026-10-23)

## Fonte e classificação
- Fonte: https://github.com/nikopueringer/CorridorKey2.0 (branch master; README, LICENSE, requirements.txt, infer.py, scripts/download_weights.py e launcher Windows consultados).
- Stack: stacks/evaluate-and-import-skill/STACK.md.
- Classe: **D — ferramenta técnica dependente de runtime externo**; metodologia de produção aproveitável, mas não há skill autônoma diretamente executável no ChatGPT.
- Decisão: **KEEP_EXTERNAL_REFERENCE**. Não copiar código, pesos, nem presumir instalação. Reavaliar quando houver demanda real por composição com runtime NVIDIA/CUDA disponível e licença adequada.

## Capacidade real
Modelo neural de chroma key/video matting: no-hint, máscara inicial ou hint em vídeo, alpha matte, primeiro plano, checker, cutout com despill e saída ProRes 4444 ou sequências OpenEXR. Processamento temporal com janelas Hann e modo low-VRAM com memmaps. Admite sequência de imagens, sRGB-like e scene-linear EXR mediante sinalização explícita. Não faz conversão automática de ACEScg, LogC, PQ/HLG ou outros espaços gerenciados.

## Dependências
- NVIDIA RTX série 30 ou superior e CUDA; 4 GB VRAM até 1440p e aproximadamente 6 GB a 4K segundo README; qualidade/continuidade e velocidade dependem do perfil de memória.
- PyTorch CUDA (README testa torch 2.9.1), FFmpeg, Python, deps em requirements, ~5 GB pesos e três modelos-base C-RADIO, MoGe-2 e RVM.
- Downloader fixa revisões C-RADIO/MoGe e verifica MD5 do RVM, mas revisão do modelo CorridorKey fica opcional e a dependência utils3d instala do GitHub (commit pinado).
- Nenhum download, instalação, inferência, benchmark ou teste em GPU foi executado nesta avaliação.

## Sobreposição e ownership
- `skills/video-editing-pipeline/SKILL.md`: owner do pipeline geral, transcrição, montagem, composição e QA; não implementa neural keying.
- `stacks/ai-reels-production/STACK.md`: possível consumidor de composições/efeitos, não um substituto de matting.
- Não criar `video-matting` somente para empacotar comando que depende de infraestrutura ausente.
- Em demanda concreta, usar vídeo-editing-pipeline para contrato/QA e CorridorKey como referência de backend externo condicional.

## Segurança e licença
- **CAUTION** na adoção operacional: execução local de código de terceiros, pesos remotos e dependências pesadas. Revisão estática parcial do README, downloader, entrypoint e launcher Windows; não é auditoria integral de todo o código/pesos.
- Downloader acessa Hugging Face e Google Storage; revisão do modelo principal pode variar. Recomenda-se fixar SHA/revisions, usar ambiente isolado, revisar licenças dos modelos de base, e verificar checksums antes de usar material sensível.
- LICENSE: variante CC BY-NC-SA 4.0 com termos adicionais; permite resultados comerciais, proíbe revenda/reempacotamento, cobrança por API/inferência e integração em software comercial sem acordo; derivadas publicadas têm restrições de licença/nome; entidades com receita > US$20 mi exigem seats por pessoa. Não tratar como licença open source permissiva.
- O projeto comercial de plugins é distinto da distribuição do código.

## Ganho incremental e limites
- Matting temporal, hints, baixa VRAM e export linear HDR são incrementais em VFX.
- Acesso ao GitHub permite inspecionar/instruir, não confere GPU NVIDIA/CUDA ou direito de redistribuição.
- Caso de ativação: usuário fornece vídeo e solicita extração de sujeito com fundo transparente, com ambiente GPU externo autorizado.
- Near miss: remover fundo de foto única, cortes simples, legendagem ou reenquadramento sem alpha matte.
- Evidência de funcionamento futura: teste de frames/clip de referência, inspeção das bordas, flicker, alpha, alinhamento, cor, codec, métricas de GPU e render final.

## Conclusão/publicação
- Decisão: registrar como referência técnica; nenhuma skill nem stack operacional nova.
- Fonte de comparação: `ARSENAL INDEX.md`, `stacks/evaluate-and-import-skill/STACK.md`, `skills/video-editing-pipeline/SKILL.md`, `skills/skill-security-review/SKILL.md`, `skills/verify-before-claim/SKILL.md`.
