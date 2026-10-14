# Avaliação — 47thtechcorner/RayCodes_MiniCPM-V-4.7-1B (2026-10-14)

## Fontes consultadas
- https://github.com/47thtechcorner/RayCodes_MiniCPM-V-4.7-1B
- Branch `main`, árvore `ca2d69de713b45d2c784313172af50f41ab4e85b`.
- README.md, main.py, Modelfile e estrutura do repositório.
- Arsenal: `ARSENAL INDEX.md`, `stacks/evaluate-and-import-skill/STACK.md` e `skills/local-llm-inference-engineering/SKILL.md`.

## Capacidade real
Demonstra pipeline Python/Ollama de quatro tarefas multimodais: OCR de recibos, explicação de diagrama científico, interpretação de gráfico e comparação entre duas imagens. Exporta respostas e durações totais por tarefa em Markdown. O Modelfile aponta para um checkpoint GGUF local externo. Dependências declaradas: Python, Ollama, modelo MiniCPM-V, download de pesos externos. Não existe modelo nem backend de inferência fornecido pelo próprio repositório.

## Divergências e limitações
- README promete TTFT e throughput, mas main.py mede apenas duração total com time.time(), sem métricas de tokenização.
- README anuncia tabelas estruturadas e JSON, porém prompts e arquivo de saída não garantem schema ou validação.
- O script filtra silenciosamente paths de imagem inexistentes e não tem manejo explícito de falha de conexão/modelo.
- O script não verifica exatidão do OCR nem compara benchmark com ground truth.
- Não foram encontrados testes automatizados ou licença explícita no diretório listado.
- Roadmap de webcam, Pydantic, bounding boxes, áudio e watcher não são funcionalidades implementadas.
- Não houve execução do modelo, instalação do pacote, verificação de qualidade real ou comparação de performance; claims do README são do autor.

## Classificação e decisão
**D — ferramenta técnica dependente de Ollama, modelo GGUF, Python e hardware.**
**Não importar nova skill ou stack.** O owner `local-llm-inference-engineering` já contempla runtime, quantização, cold/warm latency, TTFT, throughput e benchmark pareado a qualidade. Um exemplo pequeno de script não adiciona método especializado suficiente.
O projeto pode ser citado como exemplo opcional de pipeline, sem pressupor compatibilidade com qualquer máquina ou disponibilidade nativa no ChatGPT.

## Segurança e direitos
**CAUTION:** pesos e arquitetura baixados externamente; exigir validação de repositório, licença do modelo, compatibilidade com Ollama e política de dados, antes de executar. Rodar inferência local não elimina riscos de supply chain. O repositório não declara licença em arquivo listado; código publicamente visível não implica autorização para redistribuir/adaptar. Não executar installers ou downloads automaticamente.

## Alterações
Publicar somente este registro em `evaluations/`; sem duplicar skill ou mudar o índice.
