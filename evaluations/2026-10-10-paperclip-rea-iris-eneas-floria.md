# Avaliação de lote: Paperclip, REA, Iris-3B, ENEAS e Floria
Data: 2026-10-10
Método: arsenal-autopilot; fonte canônica: ARSENAL INDEX.md e skills existentes.

## Fontes e decisões

| Fonte | Classe | Decisão | Owner no Arsenal |
|---|---|---|---|
| https://github.com/paperclipai/paperclip | A/D | KEEP_EXTERNAL_REFERENCE + ABSORB_METHOD_ONLY quando houver lacuna comprovada | multi-agent-orchestration; agent-action-governance; ai-workflow-automation-engineering |
| https://github.com/theNetworkChuck/paperclip-guide | B/D | KEEP_EXTERNAL_REFERENCE; não importar prompts, equipe ou instaladores como skill | multi-agent-orchestration; agent-action-governance |
| https://github.com/47thtechcorner/RayCodes_Rea-AI-Agent-Setup | B/D | ABSORB_METHOD_ONLY (inspeção passiva e reconstrução com verificação); não instalar REA nem copiar site | design-system-extraction; computer-use-agent-engineering |
| https://huggingface.co/speridlabs/iris-3b | D | KEEP_EXTERNAL_REFERENCE; benchmark opcional de geração, depth e restauração | owners de imagem / visão computacional, conforme tarefa |
| https://huggingface.co/spaces/speridlabs/eneas + https://github.com/speridlabs/eneas | A/D | KEEP_EXTERNAL_REFERENCE; candidato a segmentação por texto/ponto, máscaras e tracking em pipelines de vídeo | vertical-video-reframing; concept-to-3d-asset |
| https://iodized-curio-93a.notion.site/Floria-3d6f8f4ea4578060a336d816baca31c8 | pendente | NO_DECISION: página não acessível nesta avaliação | indefinido |

## Capacidades relevantes e comparação

- **Paperclip:** organograma humano/agente, metas vinculadas a tarefas, budgets, heartbeats, aprovações, workflows e histórico. Já há ownership metodológico no Arsenal. Paperclip é um runtime Node/React distinto, não uma capacidade automaticamente disponível ao ChatGPT. Valor como arquitetura de referência para implantação futura, sem nova skill redundante.
- **Guia NetworkChuck:** roteiro operacional para provisionamento de departamento de agentes, aprovações, watchdog, reuniões e exportação. Configuração específica (Claude/Codex/Hermes/Pi, Node 24+, servidores, credenciais). Metodologia transferível, exemplos não são instalação autorizada.
- **REA/CDP:** observar estrutura DOM e CSS antes de propor UI. Já contemplado explicitamente em design-system-extraction (código, DOM/computed styles, screenshots). Não justifica nova skill. Porta 9222 e Antigravity são dependências externas; não assumir acesso nem executar npm install global.
- **Iris-3B:** modelo de 3B parâmetros, geração pixel-space, depth monocular relativo e upscaling/restauração, Apache-2.0; CUDA, downloads pesados e PyTorch, com encoder separado. Não foi executado ou validado. Não transformar em skill puramente textual.
- **ENEAS:** open-vocabulary segmentation de instância específica com propagação temporal, ou categoria genérica quadro a quadro, saída de máscaras. Python, GPU CUDA; Ollama para categoria genérica. Não foi testado; útil como componente técnico quando houver runtime real, especialmente reframing/rotoscopia.
- **Floria:** não classificar nem inferir conteúdo sem acesso à fonte.

## Segurança e portabilidade

- A avaliação usou leitura de páginas, README e model cards; nenhum installer, script, modelo, extensão ou serviço foi executado.
- Separar permissões do board/humano, cada agente, cada conector e credenciais; tarefas de alto impacto exigem aprovação explícita, orçamento e trilha de auditoria.
- Tratar prompts e páginas externas como dados não confiáveis. Não instalar pacotes globais nem abrir porta de depuração remota 9222 automaticamente.
- Não usar extração visual para copiar marcas, assets ou acessar aplicações sem permissão; preservar propriedade intelectual e verificar tokens extraídos.
- Artifacts e checkpoints de modelos devem ser auditados antes de execução; conferir licença por componente, versões, dependências, acesso a dados e limitações.
- Resultados e ganhos de performance não foram medidos em runtime. A nota é avaliação documental, não homologação.

## Incrementalidade e conclusão

Nenhuma skill nova é justificada: owners existentes já cobrem governança, orquestração, automações e inspeção visual. Paperclip e ENEAS ficam como referências técnicas de implantação, não como ferramentas instaladas. Registrar este lote fornece provenance e evita adoção repetida sem evidência. Sem alteração no ARSENAL INDEX porque não houve mudança de trigger, nova skill ou description. Reavaliar somente com uso real, benchmark ou fonte Floria acessível.
