# Avaliação: RayCodes_Kitten_TTS_2

- **Data:** 2026-10-15
- **Fonte:** https://github.com/47thtechcorner/RayCodes_Kitten_TTS_2 (branch `main`, README `fe00454c3bc21c90a1439898d36132584fd275f5`, script `3e2c24f4fd5667c3ec01a7f581c3c02fb8feab10`)
- **Classificação:** **D — projeto técnico dependente de runtime, modelos e ambiente local**
- **Decisão:** **Não criar skill nova**. Preservar como referência opcional para a skill existente `synthetic-presenter-video`; sem alteração do índice ou do fluxo canônico.
- **Revisão de segurança:** **CAUTION** (avaliação estática somente).

## O que faz realmente
O `main.py` usa `kittenml.KittenTTS("KittenML/kitten-tts-2")` com `model.generate(text, reference=ref_audio_path, normalize=(lang == "EN"))` e `soundfile.write` para criar três saídas WAV com falas predefinidas em inglês, hindi e espanhol. Aceita flags `--ref` e `--out-dir`. A entrada de referência é um WAV fornecido pelo usuário. Não há implementação no script de ingestão de vídeo, transcrição automática, tradução automática, sincronização labial, diarização ou UI. A descrição e o README fazem promessas mais amplas (video dubber, 10+ idiomas, offline, qualidade de estúdio) que **não foram verificadas por execução**.

## Dependências e portabilidade
Python, `kittenml`, `soundfile`, `torchaudio`, pesos externos do modelo Hugging Face, ambiente compatível com Torch e eventualmente FFmpeg para preparação da referência. O código contém mensagens e ajuste de UTF-8 específicos para Windows, mas não é exclusivo dessa plataforma. O primeiro carregamento pode baixar pesos: `offline` só após cache/preparo. O repositório não declara licença e não contém lockfile nem testes. Compatibilidade real da API `KittenTTS` e a existência/licenciamento dos pesos exigem confirmação independente em ambiente de execução.

## Valor incremental vs. Arsenal
`synthetic-presenter-video` já inclui TTS, clonagem autorizada, dublagem, consentimento e QA; o projeto fornece apenas um exemplo pontual de implementação, não uma metodologia inédita ou comportamento reutilizável de agente. O exemplo pode inspirar um backend local opcional em projetos com execução Python, condicionado a verificação independente. Não incorpora capacidades de áudio local automaticamente ao ChatGPT.

## Segurança
Não foram observados no `main.py` comandos de shell, coleta de segredos, envio explícito de áudio para serviços, persistência fora dos paths de entrada/saída ou execução dinâmica. Entretanto, instalar dependências e baixar modelos envolve cadeia externa não auditada; modelo/pacote não estão pinados; referência vocal pode ser sensível e pode ser usada para personificação sem autorização. Necessário consentimento verificável, revisão de licenças, pinagem e inspeção de dependências, controles de identidade e disclosure para divulgação pública. Nenhum instalador ou código externo foi executado nesta avaliação.

## Decisão operacional
**Descartar como skill autônoma; manter referência de implementação.** Se houver futura necessidade explícita de TTS local, realizar prova de conceito com voz autorizada, confirmar licença e API, testar vozes/idiomas/latência e comparar a qualidade com alternativas antes de escolher esse backend. Não atualizar `ARSENAL INDEX.md`: nenhuma nova skill e nenhuma alteração material de description.
