# Avaliação: Docling, OpenHands e AUTOMATIC1111 (2026-10-21)

## Escopo e método
Fontes oficiais consultadas diretamente no GitHub, READMEs da branch principal e `ARSENAL INDEX.md`; comparação com `document-extraction-pipeline`, `document-to-markdown`, `coding-agent-engineering`, `software-factory-operations`, `agent-action-governance` e `high-fidelity-image-generation`. Análise estática documental, sem executar installers, modelos ou scripts. Stack: `arsenal-autopilot` e `evaluate-and-import-skill`.

## 1. docling-project/docling
- Fonte: https://github.com/docling-project/docling
- Classe: **D/B** (runtime técnico com metodologia útil).
- Capacidade: conversão multiformato; DoclingDocument como árvore semântica, reading order, tabelas, OCR, exportação estruturada, MCP/API opcionais, processamento local.
- Owner: `skills/document-extraction-pipeline/SKILL.md` (já menciona e incorpora Docling, representation intermediária, locators e OCR seletivo); `document-to-markdown` cobre fast path.
- Decisão: **KEEP_EXTERNAL_REFERENCE**, sem duplicação ou alteração. A adoção de Docling em runtime depende de instalação e custo/permissões para modelos; limites de licença dos modelos devem ser checados separadamente da licença MIT do código.
- Trigger: PDF complexo e ingestion estrutural. Near-miss: arquivo Office textual simples.

## 2. OpenHands/OpenHands
- Fonte: https://github.com/OpenHands/OpenHands
- Classe: **D/B**.
- Capacidade: Agent Canvas como control plane independente do execution plane; backends intercambiáveis, ACP, automações, sandboxes e sessão durável.
- Owner: `skills/coding-agent-engineering/SKILL.md`; complementa factory e governance sem criar owner paralelo.
- Decisão: **UPDATE_EXISTING**: seção 'Agent Canvas e backend intercambiável'. Teste planejado: troca de backend, patch, falha, interrupção/retomada e denied action. Near-miss: tarefa trivial de edição sem agentes externos.
- Riscos: acesso integral ao host sem sandbox, mounts compartilhados, extensões/credenciais e automação com efeitos externos. Docker não prova isolamento de todos os serviços. O ChatGPT não herda disponibilidade do OpenHands.

## 3. AUTOMATIC1111/stable-diffusion-webui
- Fonte: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- Classe: **D/B**.
- Capacidade: txt2img/img2img, máscara/inpainting, matriz de parâmetros, seed e metadata, upscaling, LoRA/extensões e API.
- Owner: `skills/high-fidelity-image-generation/SKILL.md`.
- Decisão: **UPDATE_EXISTING**: seção 'Experimentos reproduzíveis com difusão'. Preserva metodologia de variantes, metadados e QA e não promete controles não expostos pelo gerador real. Near-miss: geração simples sem controles de difusão.
- Riscos: código arbitrário opcional na UI, scripts/extensões, supply chain, modelos/licenças, GPU e exposição de API/UI à rede.

## Portabilidade, segurança e validação
Não houve instalação nem execução externa. READMEs fornecem evidências de funcionalidades anunciadas, não prova de segurança ou desempenho em runtime. Foram revisadas fronteiras de permissões, risco de conteúdo/execução externa, credenciais, local versus remoto e limites dos modelos. Nenhuma nova skill foi criada; o índice não precisa mudar pois nomes/descriptions continuam iguais.

## Mudanças publicadas
- `skills/coding-agent-engineering/SKILL.md` — absorção OpenHands.
- `skills/high-fidelity-image-generation/SKILL.md` — absorção AUTOMATIC1111.
- `evaluations/2026-10-21-docling-openhands-automatic1111.md` — este registro.

Verificação: conferir conteúdos publicados na branch canônica e registrar o commit resultante no relato final.